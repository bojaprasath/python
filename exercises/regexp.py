import re
out = 'abccabddabxxab' #<html>asd<html>
m = re.findall(r'(?<=ab).+?(?=ab)',out)
# print(m.group(1))
print(m)


out = 'abcabdabxab' #<html>asd<html>
m = re.findall(r'(?<=ab).+(?=ab)',out) ##greedy
# print(m.group(1))
print(m)


out = 'abccabddabxxab' #<html>asd<html>
m = re.findall(r'(?<=ab).+?(?=ab)',out) ###non greedy lazy
# print(m.group(1))
print(m)

m = re.findall(r'(?<=ab)[^ab]+(?=ab)',out) ###greedy
# print(m.group(1))
print(m)


#sub,subn,find,finditer,findall

# out = 'abxabcdef'
# print(re.sub('a','A',out))  ## returns result string
# print(out)
# print(re.subn('a','A',out)) ## returns no of replace along with result string in list
#

out = 'abccabddabxxab'
pat = re.compile('ab.+?ab')
result = pat.split(out)

# to find no of pattern
out = 'abccabddabxxab'
print(re.findall('ab',out).__len__())
result = pat.split(out)
