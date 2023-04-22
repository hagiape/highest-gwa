# Write a Python program that read a binary file containing the 
# name of 20 students together with their GWA. The program will 
# outputs the name of the student who got the highest GWA (including the GWA).

# variable to read binary file
read_gwa = open("d:College/22-23/2nd-Sem/OOP/assignment/assignment-3/gwa/gwa.bin", "rb")
# placeholder variable for storing the current highest GWA
highest_gwa = 5
# placeholder variable for the name and gwa of student with highest gwa
top_student = ''
# for index [2:7] in binary file
for i in read_gwa:
    current_gwa = int(i[3:7])
    if current_gwa > highest_gwa:
        highest_gwa = current_gwa
        # when converting the contents binary file as list, after the name of student
        # you will encounter a backslash character. it will be utilized as the stopping
        # point of the string
        backslash = i.find('\\')
        top_student = i[3:backslash]
# convert to int
# if placeholder > index then replace placeholder with index
# print highest gwa with the name of the student