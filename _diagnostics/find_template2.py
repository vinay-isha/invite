with open(r'd:\Clone Website\Second\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('"mangalammoments/v1"')
print(cnt[pos:pos+250])
