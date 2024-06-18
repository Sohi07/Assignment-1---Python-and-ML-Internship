list1=[]
size=int(input("Enter the number of nos you want to input: "))
for i in range (0,size):
    int1=int(input(f"Enter number {i+1}: "))
    list1.append(int1)
print(f"The list is {list1}")
sum=0
for i in list1:
    sum=sum+i
print(sum)
