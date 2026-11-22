with open(r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

import re
matches = re.findall(r'.{0,50}wrapLocked.{0,50}', cnt)
for m in matches:
    print(' ', m.strip())
