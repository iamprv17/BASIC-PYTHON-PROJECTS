#ASCII Art Generator.
 
def pyramid():
    pyramid = ["   #   ", "  ###  ", " ##### ", "#######"]
    for row in pyramid:
        print(row)

print("Welcome to the ASCII Art Generator!")
print("1. Pyramid")
print("2. Exit")

user_choice = int(input("Please select an option: "))
if user_choice == 1:
    pyramid()
else:
    exit()
