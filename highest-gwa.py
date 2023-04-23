# Write a Python program that read a binary file containing the 
# name of 20 students together with their GWA. The program will 
# outputs the name of the student who got the highest GWA (including the GWA).

# the code below is a progress bar, imported from a code snippet
# credits to  https://stackoverflow.com/a/34482761
import sys, time
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("{}[{}{}] {}%/{}%\r".format(prefix, "█"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()  
for i in progressbar(range(100), '\033[32mFinding the student with highest GWA: \033[32m', 50):
    time.sleep(0.025)

try:
    # variable to read binary file
    read_gwa = open('D:/College/22-23/2nd-Sem/OOP/assignment/assignment-3/highest-gwa/gwa.bin', 'rb')
    # placeholder variable for storing the current highest GWA
    highest_gwa = 5
    # placeholder variable for the name and gwa of student with highest gwa
    top_student = ''
    # for index [2:7] in binary file
    for i in read_gwa:
        current_gwa = float(i[0:4])
        if current_gwa < highest_gwa:
            highest_gwa = current_gwa
            student = str(i[5:])
            top_student= student[2:student.find('\\')]
    # print highest gwa with the name of the student
    print('\033[32m~' * (len(top_student)) + '\033[0m')
    print('\033[33m  Congratulations!\033[0m')
    print(str(highest_gwa).center(18))
    print('\033[36m' + top_student + '\033[36m')
    print('\033[32m~' * (len(top_student)) + '\033[0m')
    read_gwa.close()
except:
    print('An error occurred. Please try again.')