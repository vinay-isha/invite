/**
 * ============================================================================
 * WEDDING INVITATION - GOOGLE SHEETS BACKEND (Google Apps Script)
 * ============================================================================
 *
 * This script connects your Wedding Invitation Website (hosted on GitHub Pages
 * or any web server) directly to Google Sheets on your Google Drive.
 *
 * It automatically handles:
 * 1. RSVP Submissions: Guest Name, Phone, Attending Status, Guest Count,
 *    Ceremonies, and Notes stored in the "RSVP Responses" sheet.
 * 2. Wedding Wishes: Wishes sent by guests stored in the "Wishes" sheet
 *    and dynamically served back to the website in real-time.
 *
 * ----------------------------------------------------------------------------
 * QUICK SETUP INSTRUCTIONS (Takes ~2 minutes):
 * ----------------------------------------------------------------------------
 * 1. Go to Google Drive (https://drive.google.com/) and create a new Google Sheet.
 * 2. Name your Google Sheet (e.g., "Vinay & Isha Wedding - RSVPs & Wishes").
 * 3. In the top menu, click Extensions > Apps Script.
 * 4. Delete any code in the editor, and paste THIS ENTIRE FILE into the editor.
 * 5. (Optional) Select 'testSetup' from the function dropdown and click 'Run'
 *    to verify that sheets and headers are created automatically.
 * 6. Click Deploy > New deployment (blue button in top right).
 * 7. Click the gear icon (Select type) > Choose 'Web app'.
 * 8. Set the following options:
 *    - Description: "Wedding Invitation Backend"
 *    - Execute as: "Me" (your email)
 *    - Who has access: "Anyone" (IMPORTANT: must be "Anyone" so guests can submit!)
 * 9. Click Deploy, authorize permissions if prompted.
 * 10. Copy the "Web app URL" (starts with https://script.google.com/macros/s/...).
 * 11. Open 'index.html' in your wedding website project and paste your URL into:
 *     window.GOOGLE_SHEETS_API_URL = "YOUR_COPIED_URL_HERE";
 * 12. Save and commit/push to GitHub! All RSVPs and Wishes will now show
 *     instantly in your Google Sheet on Google Drive!
 * ============================================================================
 */

// Configuration
var RSVP_SHEET_NAME = "RSVP Responses";
var WISHES_SHEET_NAME = "Wishes";

var RSVP_HEADERS = [
  "Timestamp",
  "Guest Name",
  "Phone Number",
  "Attending?",
  "Guest Count",
  "Ceremonies Attending / Notes",
  "Host / Company"
];

var WISHES_HEADERS = [
  "Timestamp",
  "Sender Name",
  "Wish Message",
  "Approved"
];

/**
 * Handle POST requests (RSVP submissions & Wish submissions)
 */
function doPost(e) {
  try {
    var contents = "";
    if (e && e.postData && e.postData.contents) {
      contents = e.postData.contents;
    } else if (e && e.parameter && e.parameter.data) {
      contents = e.parameter.data;
    }

    var data = {};
    if (contents) {
      try {
        data = JSON.parse(contents);
      } catch (jsonErr) {
        // Fallback if URL-encoded form
        data = e.parameter || {};
      }
    } else if (e && e.parameter) {
      data = e.parameter;
    }

    var action = (data.action || "").toLowerCase();
    var ss = SpreadsheetApp.getActiveSpreadsheet();

    if (action === "rsvp") {
      var rsvpSheet = getOrCreateSheet(ss, RSVP_SHEET_NAME, RSVP_HEADERS);
      var timestamp = data.timestamp || new Date().toLocaleString();
      var guestName = data.guestName || "Guest";
      var guestPhone = data.guestPhone || "";
      var attending = (data.attendingStatus === "yes" || data.attendingStatus === true) ? "Yes (Attending)" : "No (Declined)";
      var guestCount = data.guestCount || 0;
      var message = data.message || "";
      var company = data.company || "";

      rsvpSheet.appendRow([
        timestamp,
        guestName,
        guestPhone,
        attending,
        guestCount,
        message,
        company
      ]);

      return createJsonResponse({
        success: true,
        message: "RSVP successfully recorded in Google Sheets!",
        data: { guestName: guestName, attending: attending }
      });

    } else if (action === "wish") {
      var wishesSheet = getOrCreateSheet(ss, WISHES_SHEET_NAME, WISHES_HEADERS);
      var wishTimestamp = data.timestamp || new Date().toLocaleString();
      var senderName = data.name || data.company || "Well-wisher";
      var wishMessage = data.message || "";

      wishesSheet.appendRow([
        wishTimestamp,
        senderName,
        wishMessage,
        "Yes" // Default approved
      ]);

      return createJsonResponse({
        success: true,
        message: "Wish successfully recorded in Google Sheets!",
        data: {
          id: new Date().getTime(),
          name: senderName,
          message: wishMessage,
          submittedAt: new Date().toISOString()
        }
      });

    } else {
      return createJsonResponse({
        success: false,
        error: "Unknown action: " + action + ". Expected 'rsvp' or 'wish'."
      });
    }

  } catch (error) {
    return createJsonResponse({
      success: false,
      error: error.toString()
    });
  }
}

/**
 * Handle GET requests (Retrieve approved Wishes for display on the website)
 */
function doGet(e) {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var wishesSheet = getOrCreateSheet(ss, WISHES_SHEET_NAME, WISHES_HEADERS);
    var rows = wishesSheet.getDataRange().getValues();
    var wishes = [];

    // Row 0 is header; rows 1..N are entries
    for (var i = 1; i < rows.length; i++) {
      var row = rows[i];
      var timestamp = row[0];
      var sender = row[1];
      var msg = row[2];
      var approved = String(row[3]).toLowerCase();

      // Show if approved or not explicitly marked "no"
      if (msg && approved !== "no" && approved !== "false") {
        wishes.push({
          id: i,
          name: sender || "Well-wisher",
          message: msg,
          submittedAt: timestamp ? String(timestamp) : new Date().toISOString()
        });
      }
    }

    // Return most recent wishes first
    wishes.reverse();

    return createJsonResponse({
      success: true,
      data: {
        wishes: wishes,
        total: wishes.length
      }
    });

  } catch (error) {
    return createJsonResponse({
      success: false,
      error: error.toString(),
      data: { wishes: [] }
    });
  }
}

/**
 * Helper: Find or create sheet with headers and beautiful wedding theme styling
 */
function getOrCreateSheet(ss, sheetName, headers) {
  var sheet = ss.getSheetByName(sheetName);
  if (!sheet) {
    sheet = ss.insertSheet(sheetName);
  }

  // If sheet is empty, add headers and format
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(headers);
    var headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setFontWeight("bold");
    headerRange.setBackground("#8B1812"); // Royal Maroon
    headerRange.setFontColor("#FFFFFF");  // White text
    sheet.setFrozenRows(1);

    for (var col = 1; col <= headers.length; col++) {
      sheet.autoResizeColumn(col);
    }
  }

  return sheet;
}

/**
 * Helper: Output JSON response with proper CORS headers
 */
function createJsonResponse(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

/**
 * One-click test function to verify sheet creation directly in Apps Script
 */
function testSetup() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var rsvpSheet = getOrCreateSheet(ss, RSVP_SHEET_NAME, RSVP_HEADERS);
  var wishesSheet = getOrCreateSheet(ss, WISHES_SHEET_NAME, WISHES_HEADERS);

  // Add sample RSVP if empty
  if (rsvpSheet.getLastRow() === 1) {
    rsvpSheet.appendRow([
      new Date().toLocaleString(),
      "Sample Guest (Test)",
      "+91 9876543210",
      "Yes (Attending)",
      2,
      "Sangeet, Muhurtham, Reception",
      "Friend of Vinay"
    ]);
  }

  // Add sample Wish if empty
  if (wishesSheet.getLastRow() === 1) {
    wishesSheet.appendRow([
      new Date().toLocaleString(),
      "Aunt Sunita & Family",
      "Wishing Vinay & Isha a lifetime of love, laughter, and endless blessings! 🌸",
      "Yes"
    ]);
  }

  Logger.log("Test Setup Completed Successfully! Sheets created and formatted.");
}
