# Cloned Wedding Invitation — Mangalam Moments (Vinay & Isha)

A complete, self-contained clone of the **Mangalam Moments (v1)** wedding invitation template from WedInvite Global with **all draft modifications loaded**, **all original animations and effects intact**, and the **WedInvite watermark & branding completely removed**.

---

## 🌟 Key Features & Verification

1. **Complete Watermark Removal**
   - The tiled overlay mesh (`data-wm-host`, `.wm-10kkvf`, `_mark_1rkxo`) repeating "WedInvite" across the screen has been completely eliminated in code and styling.
   - The floating "WedInvite" pill badge has been removed.
   - The React watermark portal component (`py`) is permanently disabled (`null`).
   - The `mark` parameter is forced to `0` / inactive.

2. **Complete WedInvite Branding Removal**
   - The bottom brand card (`_brandCard_l6edf_3953`) featuring the WedInvite logo, "Chat with us", and company contact info has been detached from rendering.
   - The floating "Personalise this design" action bar (`_ctaDock_21jj1_12`) is removed.
   - The page title is updated to **"Wedding Invitation | Vinay & Isha"**.

3. **User Draft Changes Loaded (`draft=1`)**
   - Reverse-engineered from the user's Chrome browser profile storage (`wedinvite:draft:mangalammoments/v1` in `wedinvite_customizer_db` and LocalStorage).
   - **Couple Names**: Vinay & Isha (English, Tamil, Hindi translations preserved).
   - **Date**: 16 February 2027 (Tuesday).
   - **Events**: Sangeet on 15 February 2027 (Monday) 6:30 PM at Kanha Banquet (beside Mothers Wax Museum).
   - **Venue**: Bika Banquet (VIP Road, Baguiati), 2, 4, VIP Rd, Raghunathpur, Baguiati, Kolkata, West Bengal 700059.
   - **Family Blessings**: Agarwal Family (Late Savitri Devi & Late Ram Niwas Ji Agarwal) & Pansari Family (Late Fuliya Devi Pansari & Late Jugal Kishore Ji Pansari).
   - Pre-seeded dual persistence in both LocalStorage and IndexedDB upon page load so the customizations persist permanently.

4. **100% Exact Animations & Interactive Effects Preserved**
   - **Gate / Door Opening Cinematic Transition**: Realistic temple door opening animation with glowing light rays (`doors-DrT2MJX0.webm`).
   - **Background Ambience & Music Player**: Authentic shehnai/mangalam music (`mangalam-D-l39dQU.mp3`) with play/pause and mute/unmute control.
   - **Floating Petals Animation**: Dynamic floral ambient particles flowing smoothly on canvas.
   - **Scroll Reveals & Interactive Cards**: Couple names, story quote, ceremony countdown, interactive maps, wish book, and calendar reminder download.
   - **Multi-language Support**: Interactive locale toggle (English, Tamil, Hindi).
   - **All 142 Assets Hosted Locally**: All WebP motifs, golden frames, fonts (Cormorant Garamond, Rufina, Playfair Display, Jost, Afterglow), icons, and videos are bundled locally.

---

## 🚀 How to Run Locally

### Option 1: One-Click Windows Batch Script
Double-click `start.bat` in this folder. It will launch the local web server and automatically open:
```
http://localhost:8080/
```

### Option 2: Python Command Line
```powershell
python server.py 8080
```
Then visit `http://localhost:8080/` or `http://localhost:8080/templates/mangalammoments/v1/preview?draft=1`.

### Option 3: Node.js (serve / http-server / npx)
```powershell
npx serve -p 8080 -s .
```

---

## 📁 Project Structure

```
d:\Clone Website\Second/
├── index.html                   # Main entry point with pre-seeded draft state & watermark removal
├── server.py                    # Local SPA HTTP server with proper MIME types & routing
├── start.bat                    # One-click launcher script
├── user_draft_mangalammoments.json # Clean JSON export of the user's customized draft
├── theme-init.js                # Theme initialization
├── gtag-init.js                 # Privacy-clean analytics stub
├── assets/                      # All 142 reverse-engineered & patched local assets
│   ├── index-Dsnx8wPW.js        # Main React runtime bundle (watermark & brand card bypassed)
│   ├── v1-DqMLs4V3.js           # Mangalam Moments template module (brand card decoupled)
│   ├── index-BnkS49by.css       # Core stylesheet (watermark suppression rules applied)
│   ├── v1-DVDfQgyA.css          # Template stylesheet
│   ├── doors-DrT2MJX0.webm      # Temple doors cinematic animation video
│   ├── mangalam-D-l39dQU.mp3    # Background audio
│   └── ...                      # Golden frames, lotus motifs, temple graphics, WebP images
├── fonts/                       # Local wedding typography fonts
├── api/                         # Mock API responses for config, branding & translations
└── templates/                   # Direct template route support for static hosts
```
