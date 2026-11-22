target_file = r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js'
with open(target_file, 'r', encoding='utf-8') as f:
    cnt = f.read()

# 1. Patch watermark in Oy
old_wm = 'l&&(0,P.jsx)(py,{settings:u})'
new_wm = 'null/*wm-removed*/'
if old_wm in cnt:
    cnt = cnt.replace(old_wm, new_wm)
    print('Patched watermark in Oy!')
else:
    print('old_wm not found!')

# 2. Patch py definition
old_py = 'py=({settings:e})=>{'
new_py = 'py=()=>{return null;};var _py_old=({settings:e})=>{'
if old_py in cnt:
    cnt = cnt.replace(old_py, new_py)
    print('Patched py definition!')
else:
    print('old_py not found!')

# 3. Patch l in Ay
old_l = 'l=r.get(`mark`)!==`0`'
new_l = 'l=!1'
if old_l in cnt:
    cnt = cnt.replace(old_l, new_l)
    print('Patched l in Ay!')
else:
    print('old_l not found!')

# 4. Patch ctaDock
old_cta = '!o&&(0,P.jsx)(`div`,{className:ky.ctaDock'
new_cta = 'null&&(0,P.jsx)(`div`,{className:ky.ctaDock'
if old_cta in cnt:
    cnt = cnt.replace(old_cta, new_cta)
    print('Patched ctaDock in Ay!')
else:
    print('old_cta not found!')

# 5. Redirect API calls to local /api/...
# In index.js, find baseURL or api.wedinviteglobal.com
cnt = cnt.replace('https://api.wedinviteglobal.com', '')
print('Replaced https://api.wedinviteglobal.com with relative path!')

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(cnt)

print('Updated index-Dsnx8wPW.js successfully!')
