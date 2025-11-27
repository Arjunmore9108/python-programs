# 8. List and Tuple Generator

# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

#------------------------------------------------------------------------------------------------------------------------------------------------------------
def listTupleGenerator(string):
    List=[]
    for i in string:
        if i!=',':
            List.append(i)
            
    print('List:',List)
    Tuple=tuple(List)
    print("Tuple",Tuple)
        
    
    
str="2,3,4,5,6"

listTupleGenerator(str)
