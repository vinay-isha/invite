target_file = r'd:\Clone Website\Second\assets\v1-DqMLs4V3.js'
with open(target_file, 'r', encoding='utf-8') as f:
    cnt = f.read()

# 1. Define _r2 function right after _r function
pos_r = cnt.find('function _r({config:e,locale:t})')
if pos_r == -1:
    print('Error: function _r not found!')
    exit(1)

# Find the end of function _r
# It ends at: dangerouslySetInnerHTML:{__html:a}})})})]})})})}
end_marker = 'dangerouslySetInnerHTML:{__html:a}})})})]})})})}'
pos_end_r = cnt.find(end_marker, pos_r)
if pos_end_r == -1:
    print('Error: end of _r not found!')
    exit(1)

pos_insert_r2 = pos_end_r + len(end_marker)

lineage_code = '''
var lineageHtml = `<p style="letter-spacing:0.18em;font-size:0.88em;text-transform:uppercase;color:var(--tpl-color-parentsStory,#3f5230);font-weight:600;margin-bottom:0.35em;">BELOVED FAMILIES</p><h3 style="margin:0.25em 0 0.8em;font-family:'Rufina',Georgia,serif;font-size:1.6em;color:var(--tpl-color-parentsStory,#3f5230);font-weight:400;">Family Lineage</h3><div style="font-family:'Rufina',Georgia,serif;line-height:1.45;color:var(--tpl-color-parentsStory,#3f5230);"><div style="margin:0.4em 0 0.25em;"><b><span style="font-size:1.25em;color:rgb(139,24,18);letter-spacing:0.1em;">GROOM</span></b></div><div style="font-size:1.12em;font-weight:700;margin-bottom:0.15em;">Mr. Vinay Agarwal</div><div style="font-size:1.02em;">S/o. Mrs. Anita Agarwal</div><div style="margin:0.2em 0;font-size:0.95em;color:rgb(139,24,18);">&amp;</div><div style="font-size:1.02em;">Mr. Hanuman Agarwal</div><div style="margin-top:0.35em;font-size:0.95em;font-weight:700;color:rgb(139,24,18);letter-spacing:0.06em;">✦ BURDAK, KOLKATA PRAVASI ✦</div><div style="margin:0.9em 0;font-size:1.2em;color:rgb(139,24,18);">&amp;</div><div style="margin:0.25em 0 0.25em;"><b><span style="font-size:1.25em;color:rgb(139,24,18);letter-spacing:0.1em;">BRIDE</span></b></div><div style="font-size:1.12em;font-weight:700;margin-bottom:0.15em;">Ms. Isha Pansari</div><div style="font-size:1.02em;">D/o. Mrs. Anita Pansari</div><div style="margin:0.2em 0;font-size:0.95em;color:rgb(139,24,18);">&amp;</div><div style="font-size:1.02em;">Mr. Raj Kumar Pansari</div><div style="margin-top:0.35em;font-size:0.95em;font-weight:700;color:rgb(139,24,18);letter-spacing:0.06em;">✦ SINGHAL, KOLKATA PRAVASI ✦</div></div>`;
function _r2({config:e,locale:t}){let{ref:n,revealed:r}=rt(),i=N(e,`familiesEmblemImage`,`/assets/ganesha-emblem-DoE-wTD4.png`)||`/assets/ganesha-emblem-DoE-wTD4.png`,a=lineageHtml,o=fr(a),s=N(e,`familiesStoryLineHeight`,1.35)||1.35;return(0,I.jsx)(Se,{features:he,children:(0,I.jsx)(`div`,{ref:n,children:(0,I.jsxs)(gn,{layers:nn,order:gr,motion:hr,active:r,className:pr.stage,children:[(0,I.jsx)(R,{x:407,y:180,w:266,h:266,className:pr.emblemSlot,children:(0,I.jsx)(B,{show:r,delay:mr.emblem,distance:10,className:pr.fill,children:(0,I.jsx)(`img`,{src:i,alt:``,"aria-hidden":`true`,className:pr.emblem})})}),(0,I.jsx)(R,{x:190,y:410,w:700,h:1080,className:pr.storySlot,children:(0,I.jsx)(B,{show:r,delay:mr.story,distance:10,className:pr.fill,children:(0,I.jsx)(`div`,{ref:o,className:pr.story,style:{"--story-line-height":s},dangerouslySetInnerHTML:{__html:a}})})})]})})})}
'''

cnt = cnt[:pos_insert_r2] + lineageHtml_def + cnt[pos_insert_r2:] if False else cnt # draft

