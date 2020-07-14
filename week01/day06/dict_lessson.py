# __author: Administrator
# date:  2020/7/14

dic = {'name': "alex", 'age': 35, 'hobby': {'girl_name': '铁锤', 'girl_age': 45}, 'is_handsome': True}
for i, v in dic.items():
    print(i, v)
# print(dic["name"])
#
# a = dict([(1, 2), [1, 3]])
# print(a)
#
# print(dic.keys())
# print(dic.values())
#
# print(dic.items())
# dic.setdefault('aa', 54)
# print(dic)

# dic6 = dict.fromkeys(['host1', 'host2', 'host3'], 'test')
# print(dic6)

dic7 = dict.fromkeys(['host1', 'host2', 'host3'], ['test', 'test2'])
print(dic7)

dic7['host2'][1] = 'abc'
print(dic7)

st = 'hello kitty'
print(st.center(50, '*'))

