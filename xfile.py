from random import randint

mathQuiz = open("abc.txt","w")

questions = int(input("How many questions: "))
fname = input("First name: ")
lname = input("Last name: ")

mathQuiz.write("name: %s %s\n\n"%(fname,lname))

for i in range(1,questions+1):
    a = str(randint(0,1000))
    b = str(randint(0, 1000))
    problem = "%s) %s + %s = \n"%(i,a,b)
    mathQuiz.write(problem)

mathQuiz.close()





