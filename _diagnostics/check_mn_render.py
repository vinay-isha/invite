with open(r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('function Mn({')
sub = cnt[pos:pos+3500]
pos_ret = sub.find('return(0,I.jsx)')
if pos_ret == -1:
    pos_ret = sub.find('return(0,I.jsxs)')
print(sub[pos_ret:pos_ret+1200])
