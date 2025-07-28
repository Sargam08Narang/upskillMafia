students={'Sargam':90,'Simran':91,'Manya':80}

name=input("Enter student's name:")

if name in students:
   print(f"{name}'s Marks: {students[name]}")
else:
    print("Student not found.")