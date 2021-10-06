student = {'name':'John','age':26,'course':['Mathematics','Science']}
print(student)
# print(student.keys())
# print(student.values())
# print(student.get('name'))
# print(student.get('phone','not found'))
student['phone']='255-555-5656'
# 

# Deleting  item from dic

# del student['age']
# student.pop('age')
# print(student)

for key,value in student.items():
	print(key,value)