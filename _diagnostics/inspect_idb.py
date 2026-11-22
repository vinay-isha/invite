import sys

log_path = r'C:\Users\user\AppData\Local\Google\Chrome\User Data\Profile 2\IndexedDB\https_wedinviteglobal.com_0.indexeddb.leveldb\000004.log'
with open(log_path, 'rb') as f:
    data = f.read()

pos = data.rfind(b'mangalammoments/v1')
idx = pos + len(b'mangalammoments/v1')
print('pos:', pos, 'idx:', idx)
print('bytes:', repr(data[idx:idx+150]))
