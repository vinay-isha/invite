with open(r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('function Wn({')
sub = cnt[pos:pos+3000]
pos_c = sub.find(',C=')
print(sub[pos_c:pos_c+1200])
