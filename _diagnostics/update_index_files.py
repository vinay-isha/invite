import shutil, os

with open(r'd:\Clone Website\Second\user_draft_mangalammoments.json', 'r', encoding='utf-8') as f:
    import json
    draft = json.load(f)
    draft_json_str = json.dumps(draft)

html_content = f'''<!DOCTYPE html>
<html lang="en" data-theme="light" class="hide-scrollbar">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#1a1815">
  <title>Wedding Invitation | Vinay &amp; Isha</title>
  <meta name="description" content="Wedding Invitation of Vinay &amp; Isha on 16 February 2027">

  <link rel="icon" type="image/x-icon" href="/favicon.ico">

  <!-- Preconnect & Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,700&family=Jost:wght@300;400;500;600&display=swap">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Rufina:wght@400;700&display=swap">

  <!-- Core Styles -->
  <link rel="stylesheet" href="/assets/index-BnkS49by.css">
  <link rel="stylesheet" href="/assets/CompatVideo-C4rgbSCZ.css">
  <link rel="stylesheet" href="/assets/v1-DVDfQgyA.css">

  <style>
    /* Absolute cleanup of any watermark, CTA dock, or branding residuals */
    [data-wm-host],
    .wm-10kkvf,
    ._root_1rkxo_20,
    ._mesh_1rkxo_28,
    ._pill_1rkxo_79,
    ._brandCard_l6edf_3953,
    ._ctaDock_21jj1_12,
    ._brandLogo_l6edf_3969,
    ._brandContacts_l6edf_3996,
    ._brandWhatsapp_l6edf_3982 {{
      display: none !important;
      visibility: hidden !important;
      opacity: 0 !important;
      pointer-events: none !important;
      height: 0 !important;
      width: 0 !important;
      overflow: hidden !important;
    }}

    /* Remove Header and Footer shown in reference images */
    header,
    footer,
    nav,
    ._nav_1qf2a_1,
    ._footer_1qf2a_1,
    [class*="_header_"],
    [class*="_footer_1"],
    [class*="_stack_1q711"],
    [class*="_scrollTopBtn"],
    [class*="_whatsappGroup"],
    [class*="_whatsappBtn"] {{
      display: none !important;
      visibility: hidden !important;
      opacity: 0 !important;
      pointer-events: none !important;
      height: 0 !important;
    }}

    /* Hide scrollbar on third page story and duplicate page */
    ._story_19nrv_9,
    [class*="_story_19nrv"],
    [class*="_storySlot_19nrv"] {{
      scrollbar-width: none !important;
      -ms-overflow-style: none !important;
    }}
    ._story_19nrv_9::-webkit-scrollbar,
    [class*="_story_19nrv"]::-webkit-scrollbar,
    [class*="_storySlot_19nrv"]::-webkit-scrollbar {{
      display: none !important;
      width: 0 !important;
      height: 0 !important;
    }}
  </style>

  <script>
    // 1. Initialize user draft in LocalStorage and IndexedDB
    const userDraft = {draft_json_str};
    const templateKey = 'mangalammoments/v1';
    const lsKey = 'wedinvite:draft:' + templateKey;

    try {{
      localStorage.setItem(lsKey, JSON.stringify(userDraft));
      localStorage.setItem('app-theme', 'light');
    }} catch (e) {{
      console.warn('LocalStorage error:', e);
    }}

    // Seed IndexedDB for seamless dual-persistence
    try {{
      const req = indexedDB.open('wedinvite_customizer_db', 1);
      req.onupgradeneeded = function(e) {{
        const db = e.target.result;
        if (!db.objectStoreNames.contains('drafts')) {{
          db.createObjectStore('drafts', {{ keyPath: 'templateKey' }});
        }}
      }};
      req.onsuccess = function(e) {{
        const db = e.target.result;
        if (db.objectStoreNames.contains('drafts')) {{
          const tx = db.transaction('drafts', 'readwrite');
          tx.objectStore('drafts').put({{
            templateKey: templateKey,
            draft: userDraft,
            savedAt: Date.now()
          }});
        }}
      }};
    }} catch (e) {{
      console.warn('IndexedDB error:', e);
    }}

    // Ensure URL has draft=1 for compatibility with preview handlers
    if (!window.location.search.includes('draft=1')) {{
      const sep = window.location.search ? '&' : '?';
      const newUrl = window.location.pathname + window.location.search + sep + 'draft=1' + window.location.hash;
      window.history.replaceState(null, '', newUrl);
    }}
  </script>

  <script src="/gtag-init.js"></script>
  <script src="/theme-init.js"></script>
</head>
<body style="overflow: hidden;">
  <div id="root"></div>
  <script type="module" crossorigin src="/assets/index-Dsnx8wPW.js"></script>
</body>
</html>
'''

with open(r'd:\Clone Website\Second\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

shutil.copyfile(r'd:\Clone Website\Second\index.html', r'd:\Clone Website\Second\templates\mangalammoments\v1\preview\index.html')
print('Updated index.html and templates/.../index.html!')
