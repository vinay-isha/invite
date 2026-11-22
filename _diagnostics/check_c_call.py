with open(r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('function Wn({')
sub = cnt[pos:pos+3000]
import re
for m in re.finditer(r'onEnd[^,;)]*', sub):
    print(' ', m.group(0))
for m in re.finditer(r'onFilmDone[^,;)]*', sub):
    print(' ', m.group(0))
