import urllib.request, re

url = 'https://wedinviteglobal.com/assets/index-BnkS49by.css'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
css_cnt = urllib.request.urlopen(req).read().decode('utf-8')
with open(r'd:\Clone Website\Second\index-BnkS49by.css', 'w', encoding='utf-8') as f:
    f.write(css_cnt)

fonts = set(re.findall(r'url\([^\)]+\)', css_cnt))
print('Fonts/assets in index-BnkS49by.css:', fonts)
