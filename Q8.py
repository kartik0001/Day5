# Q8.

l1=[]
a=int(input("Enter number of elements in the list: "))
print("Enter the elemets of list: ")
for i in range(a):
    el=input("Enter element no.{}: ".format(i+1))
    l1.append(el)
print("The entered list is as follows: ")
print(l1)
sel=input("Enter element to be searched in the list: ")
f=0
for i in l1:
    if i==sel:
        l1.remove(i)
        print("Element found and deleted")
        f+=1
if f==0:
    print("Element not found")

print("The list is as follows: ")
print(l1)