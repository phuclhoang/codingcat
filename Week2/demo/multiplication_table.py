"""multiplication_table.py: A simple program that displays a multiplication 
table of given row and column size."""
__author__= "Phuc"

print("\nMULTIPLICATION TABLE", end = "\n\n")
col = int(input("Column size: "))
row = int(input("Row size: "))

print('      ', end = '')
for i in range(1,col+1):
    print("{:>4}".format(i), end = " ")
print()
for i in range((col+1)*5):
    print('-', end= '')
print()
for i in range(1, row+1):
    print("{:>4}|".format(i), end = " ")
    for j in range(1, col+1):
        print("{:>4}".format(i*j), end = " ")
    print()