# __author: Administrator
# date:  2020/7/20

# f = open('小重山2', 'w', encoding='utf-8')
#
# # data = f.read(5)
# # print(data)
#
# f.write('he  llo world \n')
# f.write('alex')
#
# f.close()

# f = open('小重山', 'a', encoding='utf-8')

# print(f.read(5))
# print(f.read(5))

# line = f.readline()

# print(f.readline())
# print(f.readline())

# print(f.readlines())
# article = f.readlines()
#
# f.close()
#
# for i, v in enumerate(article, 1):
#     if i == 6: v = ''.join((v.strip(), 'i like it'))
#     print(v.strip())

# for i, v in enumerate(f, 1): # for 内部将f对象做成一个迭代器，用一行取一行
#     if i == 6: v = ''.join((v.strip(), 'i like it'))
#     print(v.strip())

# print(f.tell())
# print(f.read(2))
# print(f.tell())
#
# print(f.seek(0))
# print(f.read(4))

# import  sys, time
# for i in range(30):
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     time.sleep(0.1)

# import  time
# for i in range(30):
#     print('*',end='', flush=True)
#     time.sleep(0.1)

f = open('小重山', 'r', encoding='utf-8')

f.truncate(5)

f.close()

