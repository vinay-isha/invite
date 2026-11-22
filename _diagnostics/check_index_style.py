with open(r'd:\Clone Website\Second\index.html', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('<style>')
print(cnt[pos:pos+600])
