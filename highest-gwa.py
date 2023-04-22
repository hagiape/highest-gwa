# Write a Python program that read a binary file containing the 
# name of 20 students together with their GWA. The program will 
# outputs the name of the student who got the highest GWA (including the GWA).

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
        top_student= student[2:8]
# print highest gwa with the name of the student
print(highest_gwa)
print(top_student)
read_gwa.close()