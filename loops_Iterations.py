a = [1,2,3,4,5,6,7,8,9,0]

for items in range(1,len(a)+1):
	for item in range(1,items+1):
		print(item,end=' ')
	print()
	

for items in range(len(a),0,-1):
	for item in range(1,items+1):
		print(item,end=' ')
	print()


# output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 10 
# 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7 
# 1 2 3 4 5 6 
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 