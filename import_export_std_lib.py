# import functions
# from functions import function
from functions import *
import sys
import os

course = ['Java','Python','Ruby']
students = {'name':'Amal','age':27,'place':'Sooranadu'}

# functions.function(*course,**students)
function(*course,**students)

"""Finding current directory path"""
print(sys.path)
"""Find curent working directory"""
print(os.getcwd())
print(os.__file__)
