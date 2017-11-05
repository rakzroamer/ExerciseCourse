score = input("Enter Score: ")
fscore = float(score)

if not fscore <= 0.0 or fscore >= 1.0:
    if fscore >0.0 and fscore <0.6:
        print ("F")
    elif fscore >=0.6 and fscore <0.7:
        print ("D")
    elif fscore >=0.7 and fscore <0.8:
        print ("C")
    elif fscore >=0.8 and fscore <0.9:
        print ("B")
    else:
        print ("A")

'''Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
 Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 

if (h > 40):
    pay = (40 * r) + (h - 40) * 1.5 * r
else:
    pay = (h * r)
return pay'''