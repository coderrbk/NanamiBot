# for i,val in enumerate(list1):
#     if val in hash_map
list1 = [1,1,2,3,5]
list2 = []
num = 8

for i in range(len(list1)):
    list2.append(num-list1[i])
list3 = list(set(list1)&set(list2))

if len(list3)==1:
    print(list3[0])
    print(list3[0])
else:
    print(list3[0])
    print(list3[1])

# 我TM就是SB