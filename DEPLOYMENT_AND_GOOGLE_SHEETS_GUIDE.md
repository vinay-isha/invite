# 🌸 Wedding Invitation Website - Deployment & Google Drive Integration Guide

This guide explains how to:
1. **Deploy your wedding invitation website worldwide for free using GitHub Pages** (or Netlify/Vercel).
2. **Connect Google Sheets (Google Drive)** so every guest's **RSVP** and **Wish** is recorded in real time in your Google Spreadsheet.

---

## Part 1: Connect Google Sheets / Google Drive (Takes ~2 minutes)

Your project includes a pre-built backend script: [`google_apps_script.js`](./google_apps_script.js).

### Step 1: Create a new Google Spreadsheet
1. Open [Google Drive](https://drive.google.com/) and click **New > Google Sheets > Blank spreadsheet**.
2. Name your sheet in the top left:
   ```text
   Vinay & Isha Wedding - RSVPs & Wishes
   ```

### Step 2: Open the Apps Script Editor
1. In the Google Sheets menu, click **Extensions > Apps Script**.
2. A new tab will open with code editor. Delete any default code inside `Code.gs`.
3. Open [`google_apps_script.js`](./google_apps_script.js) from your project folder, copy its **entire content**, and paste it into the editor.
4. Click the **Save** icon (diskette icon) or press `Ctrl + S`.

### Step 3: (Optional) Quick Test
1. At the top toolbar, select `testSetup` from the function dropdown menu and click **Run**.
2. Google may ask for authorization ("Review permissions" > choose your Google account > "Advanced" > "Go to Untitled project (unsafe)" > "Allow").
3. Switch back to your Google Sheet tab. You will see two beautifully formatted sheets created automatically:
   - **`RSVP Responses`** (Maroon header with columns: *Timestamp*, *Guest Name*, *Phone Number*, *Attending?*, *Guest Count*, *Ceremonies Attending / Notes*, *Host / Company*).
   - **`Wishes`** (Maroon header with columns: *Timestamp*, *Sender Name*, *Wish Message*, *Approved*).

### Step 4: Deploy as a Web App
1. In the Apps Script tab, click the blue **Deploy** button (top right) > **New deployment**.
2. Click the gear icon next to "Select type" and choose **Web app**.
3. Configure the settings:
   - **Description**: `Wedding Invitation Backend`
   - **Execute as**: `Me (your email)`
   - **Who has access**: `Anyone` *(IMPORTANT: Must be "Anyone" so guests visiting your website can submit without needing Google login).*
4. Click **Deploy**.
5. Copy the **Web app URL** that appears (starts with `https://script.google.com/macros/s/.../exec`).

### Step 5: Link the URL to your Website
1. Open [`index.html`](./index.html) in your code editor.
2. Locate line 51:
   ```javascript
   window.GOOGLE_SHEETS_API_URL = "";
   ```
3. Paste your Web app URL between the quotes:
   ```javascript
   window.GOOGLE_SHEETS_API_URL = "https://script.google.com/macros/s/AKfycby.../exec";
   ```
4. Copy the same URL into [`404.html`](./404.html) line 51.

---

## Part 2: Deploy to GitHub Pages (Live on the Internet)

### Option A: Using Git CLI (Recommended)

1. Open PowerShell or Terminal in your project directory (`d:\Clone Website\Second`):
   ```bash
   git init
   git add .
   git commit -m "Deploy Vinay & Isha Wedding Invitation"
   git branch -M main
   ```
2. Go to [GitHub](https://github.com/) and create a new repository (e.g., `wedding-invitation`).
   - Choose **Public** (free GitHub Pages hosting).
3. Connect your local folder to GitHub and push:
   ```bash
   git remote add origin https://github.com/<YOUR-USERNAME>/wedding-invitation.git
   git push -u origin main
   ```
4. In your GitHub repository:
   - Go to **Settings** > **Pages** (in the left sidebar).
   - Under **Build and deployment > Source**, select **Deploy from a branch**.
   - Under **Branch**, select **main** and folder **/(root)**.
   - Click **Save**.
5. Within 1–2 minutes, your website is live worldwide at:
   ```text
   https://<YOUR-USERNAME>.github.io/wedding-invitation/
   ```

> [!NOTE]
> All asset paths, stylesheets, video/audio tracks, animations, and SPA fallback routes have been configured with relative paths and dynamic base path resolution. It works cleanly on both root domains (`https://yourwedding.com/`) and GitHub subpaths (`https://user.github.io/wedding-invitation/`).

---

### Option B: Instant Drag-and-Drop Deployment via Netlify (No Git required)

If you prefer not to use Git command line:
1. Go to [app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag and drop the `Second` folder directly into the browser window.
3. Your wedding invitation is live instantly on the internet with free SSL and custom domain support!

---

## What Happens When Guests Interact:

- **Opening the Website**: The opening temple doors video film plays, followed by the Ganpati blessings, countdown, family lineage, photo gallery, events, interactive venue map, RSVP form, and wishes board.
- **Submitting RSVP**: The guest selects attending status ("Accept with Pleasure" or "Regretfully Decline"), enters their name, phone number, ceremony attendance, and optional note. The submission is appended directly to your Google Sheet in Google Drive, the envelope folds, and wedding petals burst on their screen!
- **Sending Wishes**: The guest writes a heartfelt wish and clicks "Send Wish". It is logged directly into the Google Sheet in Google Drive, confirms with a thank-you note, and immediately floats among the wedding wishes on their screen!
