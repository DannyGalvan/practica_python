list = [x * x for x in range (5)]
def fun(lts):
    del lts[lts[2]]
    return lts

print(fun(list))

dd = {"dd": "0", "jj":"1"}
for x in dd.values():
    print(x, end= " ")    
print()
