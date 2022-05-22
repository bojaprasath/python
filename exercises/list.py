a = [1,2,3,4,5]
a.append(6)
print(a)
b = [7,8]
a.append(b)  # just appends the list to list
print(a)
c = a
c.extend(b) ## Extend append the list values 1 by 1
print(c)
print(type(c[6]))
print(type(c[5]))
print(a.remove(6))  ## removes value 6
print(a)
print(a.pop(2))  ##removes value at index 2
print(a)
print(a.index(2))
print(a)
print('####clearing######')
print(c)

print(id(a))
print(id(b))
c =a
print(id(a))
print(id(c))
print('After coopying')
c = list(a)
# print(id(a))
# print(id(c))
# print(min(a))
# print(max(a))
# print(all(a))
# print(enumerate(a))

def mod_list(team):
    team.append('6')
team = [1]
mod_list(team[:])
print(team)
mod_list(list(team))
print(team)
mod_list(team)
print(team)


def mod_string(string):
    string = 'modififed'
    print(string)
string = 'asd'
mod_string(string)
print(string)

def mod_dict(team):
    team['name'] = 'name'
    print(dict)
team = {}
team['id'] = 0
mod_dict(dict(team))
print(team)


# def mod_list(list):
#     list.append('6')
# list = [1]
# mod_list(list[:])
# print(list)

