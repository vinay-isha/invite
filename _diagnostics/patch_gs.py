target_file = r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js'
with open(target_file, 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('function gS(){')
if pos != -1:
    target = cnt[pos:pos+150]
    print('Found gS:', target)
    end_brace = target.find('}')
    old_func = target[:end_brace+1]
    print('Old func:', old_func)
    new_func = 'function gS(){return"bare"}'
    cnt = cnt.replace(old_func, new_func)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(cnt)
    print('Patched gS to return "bare" successfully!')
else:
    print('function gS not found!')
