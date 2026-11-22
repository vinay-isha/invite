with open(r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('Ay=()=>{')
print(cnt[pos:pos+200])
