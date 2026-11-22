with open(r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('{family:t,version:n}=tn()')
print('pos:', pos)
print(cnt[pos-30:pos+150])
