out_file = open("name.txt", "w")

name = input("Please enter your name: ")
out_file.write(name)
out_file.close()

name_file = open("name.txt", "r")
name = name_file.read().strip()
name_file.close()
print("Your name is", name)

numbers_file = open("numbers.txt", "r")
num1 = int(numbers_file.readline())
num2 = int(numbers_file.readline())
numbers_file.close()
print(num1 + num2)

numbers_file = open("numbers.txt", "r")
total = 0
for line in numbers_file:
    number = int(line)
    total = total + number
numbers_file.close()
print(total)

