list=[1,2,-4,5,-7]
neg_count=0
pos_count=0
for i in list:
	if i>=0:
		pos_count+=1
	else:
		neg_count+=1

print("positive numbers",pos_count)
print("negative numbers",neg_count)

	