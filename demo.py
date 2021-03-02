l=[10,20,30,40,70]
l1=l
print('id l--',id(l),'id l1---',id(l1))
l1=l[:]
l1[1]=888
print(l1)
print('id l--',id(l),'id l1---',id(l1))
