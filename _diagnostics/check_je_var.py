with open(r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

import re
matches = [m.start() for m in re.finditer(r'je\s*=', cnt)]
print('je= matches:', matches)
for p in matches:
    print(cnt[p-20:p+100])
