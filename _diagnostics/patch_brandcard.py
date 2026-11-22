target_file = r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js'
with open(target_file, 'r', encoding='utf-8') as f:
    cnt = f.read()

old_str = '(0,I.jsxs)(`div`,{className:L.brandCard'
if old_str in cnt:
    print('Found brandCard in assets/v1-DqMLs4V3.js!')
    new_str = 'null&&(0,I.jsxs)(`div`,{className:L.brandCard'
    cnt = cnt.replace(old_str, new_str)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(cnt)
    print('Patched brandCard in assets/v1-DqMLs4V3.js!')
else:
    print('brandCard string not found!')
