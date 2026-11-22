with open(r'd:\Clone Website\Second\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos2 = cnt.find('__vite__mapDeps=')
sub = cnt[pos2:pos2+4000]
start = sub.find('["')
end = sub.find('])')
arr_str = sub[start:end+1]
import json
deps = json.loads(arr_str)
print('Total deps:', len(deps))
indices = [52,1,5,42,43,50,44,35,47,6,37,2,18,24,3,29,20,30,53]
for idx in indices:
    print(f'{idx}: {deps[idx]}')
