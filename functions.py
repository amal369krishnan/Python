# def newFunction():# output-->none
# 	pass
# print(newFunction())

# def newFunction(greetings):
# 	print(greetings)
# newFunction('hi')

# def function(greeting,name):
# 	# msg = '{} {}, how are you!'.format(greeting,name)
# 	msg = msg = f'{greeting} {name}, how are you!'
# 	return msg;
# print(function('Hello','Amal'))

# courses = ['Hi', 'Hello'];
# info = {'name': 'Amal', 'age': 27}
def function(*args,**kwargs):
 	print(args)
 	print(kwargs)

# function('Hi','Hello',name='Amal',age=27)
# function(*courses,**info)
