# Q4.

l1=['abc',2,66.2,'def','ghi',20,55.66,56,'jkl',5.0,'mno',16]

l2=[]
l3=[]
l4=[]

for index in range(len(l1)):
	if type(l1[index])==str:
		l2.append(l1[index])
	elif type(l1[index])==int:
		l3.append(l1[index])
	elif type(l1[index])==float:
		l4.append(l1[index])
print(l2)
print(l3)
print(l4)