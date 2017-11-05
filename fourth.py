#Lists
def fun_with_for_loop():
    student_name = ['Rajes','Kavin','Sudha']
   # print (student_name[1])

    value_pos_pars = zip(student_name,range(len(student_name)) )
    print (value_pos_pars)
#for name in student_name:
  #  print("Hi my name is {0:*^9}".format(name))
# primitive for loop will loop through list and we wont have index for the listed items.
    #if index is required for the list item, we need to go with enumerate() -> index,item or (list of item)
    for index, item in enumerate(student_name):
        if index == 0:
            index = '1st'
            print ("Hi, I'm {0} student and my name is {1:*^9}".format(index,item))
        elif index == 1:
            index = '2nd'
            print ("Hi, I'm {0} student and my name is {1:*^9}".format(index,item))
        else:
            index = '3rd'
            print ("Hi, I'm {0} student and my name is {1:*^9}".format(index,item))

fun_with_for_loop()

question:
#based on each value of for loop i want to print that in my statement eg: 1 = 1st, 2- 2nd ...