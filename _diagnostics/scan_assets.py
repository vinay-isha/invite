with open(r'd:\Clone Website\Second\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    js_cnt = f.read()

import re
assets_js = set(re.findall(r'\/assets\/[a-zA-Z0-9_\-\.]+', js_cnt))
print('Assets in v1-DqMLs4V3.js:', assets_js)

# Download v1-DVDfQgyA.css if not exists
import urllib.request
css_url = 'https://wedinviteglobal.com/assets/v1-DVDfQgyA.css'
req = urllib.request.Request(css_url, headers={'User-Agent': 'Mozilla/5.0'})
css_cnt = urllib.request.urlopen(req).read().decode('utf-8')
with open(r'd:\Clone Website\Second\v1-DVDfQgyA.css', 'w', encoding='utf-8') as f:
    f.write(css_cnt)

assets_css = set(re.findall(r'\/assets\/[a-zA-Z0-9_\-\.]+', css_cnt))
print('Assets in v1-DVDfQgyA.css:', assets_css)

fonts_css = set(re.findall(r'\/fonts\/[a-zA-Z0-9_\-\.]+', css_cnt))
print('Fonts in v1-DVDfQgyA.css:', fonts_css)
