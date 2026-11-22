with open(r'd:\Clone Website\Second\index-Dsnx8wPW.js', 'r', encoding='utf-8') as f:
    cnt = f.read()

pos = cnt.find('iy={')
# find mangalammoments inside iy
sub = cnt[pos:]
end_pos = sub.find('}')
iy_content = sub[:end_pos]
pos2 = iy_content.find('mangalammoments')
print('inside iy:', iy_content[pos2-20:pos2+200])
