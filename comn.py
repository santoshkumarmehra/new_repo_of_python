arr=['pqrstu','zxcstu','prostu','lmqstu','zxystu']
s=''
for i in range(0,len(arr)-1):
	x=arr[i]
	for j in range(i+1,len(arr)):
		y=arr[j]
		for k in range(0,len(x)):
			if x[k]==y[k]:
				if x[k] not in s:
					s=s+x[k]
		break
print("common suffix of list in entire array = ",s)