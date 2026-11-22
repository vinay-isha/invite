with open(r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('function Mn({')
sub = cnt[pos:pos+4000]
pos_click = sub.find('onClick:S')
print(sub[pos_click-500:pos_click+200])
