target_file = r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js'
with open(target_file, 'r', encoding='utf-8') as f:
    cnt = f.read()

pos1 = cnt.find('function gS(){return"bare"}')
pos2 = cnt.find('var _S=`app-theme`;', pos1)
print('pos1:', pos1, 'pos2:', pos2)
old_chunk = cnt[pos1:pos2]
print('Replacing chunk:', old_chunk)

cnt = cnt[:pos1] + 'function gS(){return"bare"}' + cnt[pos2:]
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(cnt)
print('Cleaned up gS replacement perfectly!')
