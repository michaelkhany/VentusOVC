# -------------------------------------------------------------
# 
# Project:      Machine Vision Workshop (Fundamentals, Functions and Classes)
# Developers:   ENG. Michael B.Khani   
#               Beyza Nur
#               Umut Furkan Dugan
#               Zeynep Altunel
#               Omer Berkay Kaynar
# Session id:   SIII-T
#
# -------------------------------------------------------------

import os
# Preparing the environment
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()

print('Machine Vision Workshop (Fundamentals, Functions and Classes)')
print('\t')

class Matrix_5x5:
    def __init__(self, matrix_5x5):
        self.matrix =matrix_5x5

    def print_matrix(self):
        result =""
        for i in range(len(self.matrix)):
            result +="\t"
            for j in range(len(self.matrix[0])):
                result +=str(self.matrix[i][j])+","
            result +="\n"
        print (result)

    def length_matrix(self):
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        return (rows * columns)

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ADD FUNCTION (A) HERE

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ADD FUNCTION (B) HERE

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ADD FUNCTION (C) HERE

#Main code continues here:
matrix_a = Matrix_5x5([[17,18,20,22,17],
                       [22,11,18,21,18],
                       [18,23,21,20,19],
                       [11,11,20,22,21],
                       [21,18,17,23,22]])
matrix_b = Matrix_5x5([[20,12,22,20,18],
                       [12,13,15,19,16],
                       [22,11,18,21,18],
                       [18,23,21,20,19],
                       [12,13,14,15,16]])
print(">> Matrix A:")
matrix_a.print_matrix();
print(">> Matrix B:")
matrix_b.print_matrix();

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USE Matrix_5x5 Class, FUNCTION (A) HERE

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USE Matrix_5x5 Class, FUNCTION (B) HERE

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USE Matrix_5x5 Class, FUNCTION (C) HERE

#Printing matrices for seeing any changes
print(">> Matrix A (after):")
matrix_a.print_matrix();
print(">> Matrix B (after):")
matrix_b.print_matrix();
