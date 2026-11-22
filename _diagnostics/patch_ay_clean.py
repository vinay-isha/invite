target_file = r'd:\Clone Website\Second\assets\index-Dsnx8wPW.js'
with open(target_file, 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('Ay=()=>{let{t:e}=Ls(),{family:t,version:n}=tn()')
if pos != -1:
    target = cnt[pos:pos+150]
    print('Found target:', target)
    repl = 'Ay=()=>{let{t:e}=Ls(),{family:_t,version:_n}=tn(),t=_t||`mangalammoments`,n=_n||`v1`,[r]=Dr(),i=r.get(`invitation`),a=!0'
    end_of_a = target.find(',o=r.get')
    sub_to_replace = target[:end_of_a]
    print('Replacing:', sub_to_replace)
    cnt = cnt.replace(sub_to_replace, repl)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(cnt)
    print('Replaced successfully!')
else:
    print('Ay not found!')
