with open(r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('function je(')
if pos == -1:
    pos = cnt.find('var je=')
if pos == -1:
    pos = cnt.find('je=')
print(cnt[pos:pos+500])
