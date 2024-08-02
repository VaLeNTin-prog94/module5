my_dict={'Val':1994,'Ben':1995,'Kamilla':1996}
print("Dict:",my_dict)
print("Existing value:",my_dict['Val'])
print("Not existing value:",my_dict.get('Bena'))
my_dict.update({'Gena':4344,'Lena':3223})
print("Deleted value:", my_dict.pop('Gena'))
print("Modified dictionary:",my_dict)
my_set ={1,1,2,2,3,4,55,5,5,'Str','Str',False,(0,2,1)}
print("Set:",my_set)
my_set.add('photoshop')
my_set.add('67')
#my_set.discard(1)
my_set.remove(1) #в данном случае ошибку не выдает так как элементе есть в множестве
print("Modified set:",my_set)
