with open(r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('r.get(`draft`)')
if pos == -1:
    pos = cnt.find('get("draft")')
if pos == -1:
    pos = cnt.find('draft')
print('pos of r.get(`draft`):', pos)
print(cnt[pos-50:pos+250])
