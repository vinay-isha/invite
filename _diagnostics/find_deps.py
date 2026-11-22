with open(r'd:\Clone Website\Second\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('__vite__mapDeps(')
print('pos:', pos)
# Find the definition of __vite__mapDeps
pos2 = cnt.find('function __vite__mapDeps')
if pos2 == -1:
    pos2 = cnt.find('__vite__mapDeps=')
print(cnt[pos2:pos2+1000])
