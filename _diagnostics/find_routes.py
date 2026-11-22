with open(r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

import re
matches = re.findall(r'path:[`"\'][^`"\']+[`"\']', cnt)
for m in matches[:30]:
    print(' ', m)
