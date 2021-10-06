import os
os.chdir('/home/rajeevam/Desktop')

print(os.listdir())

# f = open('renamed_text',r) #r->read,w->write,a->append,readwrite->r+,rb->readbinary,wb->writebinary
# print(f.mode)
# print(f.name)
# print(f.read())
# f.close()


with open('renamed_text','r') as f:
	# print(f.read())
	# f_contents = f.readline()
	# print(f_contents,end='')
	f_contents = f.readlines()
	for list in f_contents:
		print(list,end='')
	
	
	f.closed