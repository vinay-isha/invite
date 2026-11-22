target_file = r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js'
with open(target_file, 'r', encoding='utf-8') as f:
    cnt = f.read()

# Route patch
old_route = '(0,P.jsx)(M,{path:`/`,element:(0,P.jsx)($m,{})})'
new_route = '(0,P.jsx)(M,{path:`/`,element:(0,P.jsx)(Ay,{})})'
if old_route in cnt:
    cnt = cnt.replace(old_route, new_route)
    print('Patched root route to Ay!')
else:
    print('old_route not found!')

# Default family/version in Ay
old_ay_params = '{family:t,version:n}=tn(),[r]=Dr(),i=r.get(`invitation`),a=!0'
new_ay_params = '{family:_t,version:_n}=tn(),t=_t||`mangalammoments`,n=_n||`v1`,[r]=Dr(),i=r.get(`invitation`),a=!0'
if old_ay_params in cnt:
    cnt = cnt.replace(old_ay_params, new_ay_params)
    print('Patched default params in Ay!')
else:
    print('old_ay_params not found!')

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(cnt)
print('Done!')
