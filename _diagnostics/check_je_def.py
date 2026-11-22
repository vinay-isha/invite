with open(r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('je(e,[')
# look backwards for je=
pos2 = cnt.rfind('je=', 0, pos)
print('pos2:', pos2)
print(cnt[pos2-50:pos2+200])
