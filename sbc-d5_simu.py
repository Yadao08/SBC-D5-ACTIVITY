# t = (1,2,3,4,5,0) #tuple(cannot be change)immu
# l = [1,2,3,4,5,0] #list (can be change)muta

# print(t[1:4])
# print(l[1:4])
# l[5] = 6
# t[5] = 6
# print(l)
# print(t)

# l = [5,4,7,1,2]
# print(l[0]) #accessing
# l.append(1, 3)
# print(l)

# l.insert(1,3)
# print(l)

# l = [5,4,7,1,2]
# l[1] = 3
# l.remove(7) # remove by object
# l.pop() # remove by index //default value is -1 maong nag last ang mawala if walay ibutang nga value

# l = [5,4,7,1,2]
# #l.clear() # delete all
# # l.remove(1) # 5472
# # l.pop(-3) #572
# #l.sort(reverse=True)
# l.reverse()
# print(l)

# l=[]
# l.append("china")
# l.append("eleven,")
# l.append("john")
# l.insert(0,"stacy")

# l.pop(0)
# l.reverse()

data = [["carlo", "p.", "maneja", 18,"single"],
        ["rj", "p.", "baron", 18,"taken"]]

final = []
for d in data:
    label = {}
    label["firstname"] = d[0]
    label["initial"] = d[1]
    label["lastname"] = d[2]
    label["age"] = d[3]
    label["status"] = d[4]
    final.append(label)
print(final)


