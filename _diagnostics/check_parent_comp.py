with open(r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('var _r=')
if pos == -1:
    pos = cnt.find('function _r(')
if pos == -1:
    pos = cnt.find('_r=')
print(cnt[pos-50:pos+2000])
