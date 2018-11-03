import re
import pandas

json_file = open('champion_info.json', 'r')
json_string = json_file.read()

# find all nodes
# a = re.fidall(r'\"([A-Za-z0-9]+)\": {', json_string)
# print(a)


titles = re.findall(r'\"title\":\s*\"(.*)\"', json_string)
id = re.findall(r'\"id\":\s*(.*)?\,', json_string)
key = re.findall(r'\"key\":\s*\"(.*)\"', json_string)
name = re.findall(r'\"name\":\s*\"(.*)\"', json_string)


json_file.close()

heroes = [[titles[i], id[i], key[i], name[i]] for i in range(len(titles))]
print(heroes)

json_file = open('champion_info_2.json', 'r')
json_string = json_file.read()

tags = re.findall(r'\"tags\":\s*\[(.*?\])', json_string, re.DOTALL)#not optimal
new_tags = []
for i in tags:
    new_tags.append(i.replace('\n', '').replace(']','').replace('\"', '').replace(' ', ''))

id = re.findall(r'\"id\":\s*(.*)?\,', json_string)
name = re.findall(r'\"name\":\s*\"(.*)\"', json_string)

heroes_roles = [[new_tags[i], id[i]] for i in range(len(new_tags))]
print(heroes_roles)

result = []

for h in heroes:
    for it, r in enumerate(heroes_roles):
        if h[1]==r[1]:
            h.extend(r)
            result.append(h)
            break
    heroes_roles.pop(it)

print(result)

result_file = open('result.csv', 'w')
for i in result:
    result_file.write(','.join(i[:-1])+'\n')

result_file.close()

json_file.close()

#\"([A-Za-z0-9]+)\"