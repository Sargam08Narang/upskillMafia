user_input = input("Enter text to write to the file: ")
file = open('output.txt', 'w')
file.write(user_input + '\n')
file.close()

more_input = input("Enter more text to append: ")
file = open('output.txt', 'a')
file.write(more_input + '\n')
file.close()


file = open('output.txt', 'r')
print("\nFinal content of the file:")
for line in file:
    print(line.strip())
file.close()
