with open(r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('function Mn({')
sub = cnt[pos:pos+4000]
import re
for m in re.finditer(r'([a-zA-Z0-9_$]+)\s*=\s*\([^)]*\)\s*=>', sub):
    print('  arrow func:', m.group(1))
