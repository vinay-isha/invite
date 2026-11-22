import os, urllib.request, concurrent.futures, json

BASE_URL = 'https://wedinviteglobal.com'
TARGET_DIR = r'd:\Clone Website\Second'

# Collect all assets
assets_to_download = [
    # Core scripts
    '/assets/index-Dsnx8wPW.js',
    '/assets/v1-DqMLs4V3.js',
    '/assets/jsx-runtime-CdArH33I.js',
    '/assets/gestures-BfluCb-v.js',
    '/assets/textFit-aC3ZDXQ-.js',
    '/assets/layout-DUJqjjkC.js',
    '/assets/party-popper-CuPBKlVq.js',
    '/assets/calendar-days-DEZmq6u4.js',
    '/assets/volume-x-8SGV_G6X.js',
    '/assets/user-check-DyNwYMnY.js',
    '/assets/minus-D_Uxv_ZA.js',
    '/assets/sun-CHsmKl25.js',
    '/assets/music-2-BY1dm-Ac.js',
    '/assets/calendarLinks-B9am4CqP.js',
    '/assets/useBrandingSettings-6oMJ9PmE.js',
    '/assets/SectionGate-CVyW9sIQ.js',
    '/assets/CompatVideo-Bcg8dZA5.js',
    '/assets/videoAttrs-C9te08DJ.js',
    '/gtag-init.js',
    '/theme-init.js',
    # CSS
    '/assets/index-BnkS49by.css',
    '/assets/v1-DVDfQgyA.css',
    '/assets/CompatVideo-C4rgbSCZ.css',
    # Fonts
    '/fonts/afterglow-regular.ttf',
    '/fonts/cac_champagne.ttf',
    # Icons / root
    '/favicon.ico',
    '/site.webmanifest',
    '/brand-logo-card.png',
    '/logo-with-text.png'
]

# Add all template assets discovered
import re
with open(os.path.join(TARGET_DIR, 'v1-DqMLs4V3.js'), 'r', encoding='utf-8') as f:
    js_cnt = f.read()
found_in_js = re.findall(r'\/assets\/[a-zA-Z0-9_\-\.]+', js_cnt)
assets_to_download.extend(found_in_js)

# Deduplicate
assets_to_download = sorted(list(set(assets_to_download)))
print(f'Total unique assets to download: {len(assets_to_download)}')

def download_file(rel_path):
    # normalize path
    clean_rel = rel_path.lstrip('/')
    dest_path = os.path.join(TARGET_DIR, clean_rel.replace('/', os.sep))
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # skip if already exists and non-empty
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
        return (rel_path, True, 'cached')
    
    url = BASE_URL + rel_path
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        with open(dest_path, 'wb') as f:
            f.write(data)
        return (rel_path, True, len(data))
    except Exception as e:
        return (rel_path, False, str(e))

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(download_file, assets_to_download))

failed = []
for rel, success, info in results:
    if not success:
        failed.append((rel, info))
        print(f'FAILED: {rel} -> {info}')

print(f'Downloaded {len(results) - len(failed)} of {len(results)} files. Failed: {len(failed)}')
