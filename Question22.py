size=int(input("Enter the size of list: "))
list1=[]
for i in range (0,size):
    int1=int(input(f"Enter the {i+1} element: "))
    list1.append(int1)
min1=min(list1)
max1=max(list1)
print(f"The min value in the list is {min1} and the max value in the list is {max1}")