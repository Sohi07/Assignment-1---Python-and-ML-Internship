size=int(input("Enter the size of list: "))
list1=[]
for i in range (0,size):
    int1=int(input(f"Enter the {i+1} element: "))
    list1.append(int1)
element=int(input("Enter the element you want to check: "))
count1=list1.count(element)
print(f"{element} occurs {count1} times in the list")