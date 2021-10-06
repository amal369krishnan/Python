import os

os.chdir('/home/rajeevam/Desktop')


try:
	f = open('renamed_text','r')
	print(f.read())
	# var = bad
	# raise Exception #manually raising exception
except Exception as e:
	print('Exception : ',e)
else:
	f.close()
	print(f.closed)
finally:
	print('finally block excuted')