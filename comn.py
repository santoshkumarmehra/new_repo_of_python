arr=[-1,2,-1,3,2]
s=set(arr)
for ele in s:
	count=0
	for j in arr:
		if  ele==j:
			count=count+1			
	if count==1:
		print("\n","This is non repeat element = ",ele)


