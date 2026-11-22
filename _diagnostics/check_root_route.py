with open(r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('path:`/`,')
if pos == -1:
    pos = cnt.find('path:"/",')
print('pos:', pos)
print(cnt[pos-50:pos+300])
