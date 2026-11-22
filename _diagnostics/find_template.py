with open(r'd:\Clone Website\Second\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('iy={')
sub = cnt[pos:pos+4000]
import re
for m in re.finditer(r'"mangalam[^"]*"[^,]+', sub):
    print(m.group(0))
