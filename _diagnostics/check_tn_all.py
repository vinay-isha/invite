with open(r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

import re
matches = [m.start() for m in re.finditer(r'\{family:t,version:n\}=tn\(\)', cnt)]
print('Matches count:', len(matches))
for pos in matches:
    print('pos:', pos, cnt[pos-20:pos+80])
