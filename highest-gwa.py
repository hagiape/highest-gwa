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
# convert to int
# if placeholder > index then replace placeholder with index
# print highest gwa with the name of the student