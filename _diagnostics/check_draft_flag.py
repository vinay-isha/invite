with open(r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

import re
matches = re.findall(r'.{0,40}draft.{0,40}', cnt)
for m in matches[:10]:
    print(' ', m.strip())
