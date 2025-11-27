# 9.print second highest number from the array

numbers=[12,34,68,244,0,33,67,88]
firstMax = max(numbers)

for i in range(0,len(numbers)-1):
    if numbers[i]==firstMax:
        del(numbers[i])
        
secondMax=max(numbers)
print(secondMax)

# ----------done-----------

# OUTPUT:
#     98