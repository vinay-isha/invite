with open(r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('var ia=({config:e,')
sub = cnt[pos:pos+4000]
import re
for m in re.finditer(r'u\([^)]*\)', sub):
    print(' ', m.group(0))
