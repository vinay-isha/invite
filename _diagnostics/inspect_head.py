from bs4 import BeautifulSoup

with open(r'd:\Clone Website\Second\settled_user_page.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print('Scripts in head:')
for s in soup.head.find_all('script'):
    print(' ', s.get('src') or s.get_text()[:60])

print('Links in head:')
for l in soup.head.find_all('link'):
    print(' ', l.get('rel'), l.get('href'))
