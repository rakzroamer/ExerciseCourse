#boolean = truthy is any digit other than 0, string = a value
number = 5
if number:
    print ("number is defineed and truthy")
else:
    print("not working")

python_course = True
if python_course:
    print ("hi Python")
alien_found = None
if alien_found:
    print ("super")
else:
    print ("im not worried")

number = 5
if number != 5:
    print ("no")
else:
    print ("yes")

python_course = True
'''if not python_course:
    print ("false")
else:
    print("its ok")'''

"good" if not python_course else print("its ok,im a bit of expert in \"coding\" hehe")