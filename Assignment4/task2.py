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
final_content=file.read()
print(final_content)
file.close()
