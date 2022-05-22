import re
ip = '2001:db8:3333:4444:CCCC:DDDD:EEEE:AAAA'
m = re.search(r'([0-9a-fA-F]{1,4}:){1,7}:{0,1}[0-9a-fA-F]{1,4}',ip)
print(m.group)