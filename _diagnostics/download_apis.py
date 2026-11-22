import urllib.request, json, os

TARGET_DIR = r'd:\Clone Website\Second'
API_BASE = 'https://api.wedinviteglobal.com'

endpoints = [
    '/api/v1/templates/mangalammoments/v1/config',
    '/api/v1/settings/branding',
    '/api/v1/settings/translations/en',
    '/api/v1/settings/translations/ta',
    '/api/v1/settings/translations/hi'
]

for ep in endpoints:
    url = API_BASE + ep
    dest_path = os.path.join(TARGET_DIR, ep.lstrip('/').replace('/', os.sep))
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
        with open(dest_path, 'wb') as f:
            f.write(data)
        print(f'Saved {ep} ({len(data)} bytes)')
    except Exception as e:
        print(f'Failed {ep}: {e}')
