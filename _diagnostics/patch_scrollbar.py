css_file = r'd:\Clone Website\Second\assets\v1-DVDfQgyA.css'
with open(css_file, 'r', encoding='utf-8') as f:
    cnt = f.read()

# Replace scrollbar-width:thin
cnt = cnt.replace('scrollbar-width:thin;', 'scrollbar-width:none;-ms-overflow-style:none;')

# Add webkit-scrollbar hiding rule
rule = '''
/* Hide scrollbar on third page story and duplicate page */
._story_19nrv_9,
[class*="_story_19nrv"],
[class*="_storySlot_19nrv"] {
  scrollbar-width: none !important;
  -ms-overflow-style: none !important;
}
._story_19nrv_9::-webkit-scrollbar,
[class*="_story_19nrv"]::-webkit-scrollbar,
[class*="_storySlot_19nrv"]::-webkit-scrollbar {
  display: none !important;
  width: 0 !important;
  height: 0 !important;
}
'''
cnt += '\n' + rule

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(cnt)

print('Updated assets/v1-DVDfQgyA.css with scrollbar-hiding rules!')
