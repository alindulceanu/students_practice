user_choice = input("Please enter your choice (A, B, or C): ")

if user_choice == "A":
    # Run file A
    exec(open("file_A.py").read())
elif user_choice == "B":
    # Run file B
    exec(open("file_B.py").read())
elif user_choice == "C":
    # Run file C
    exec(open("file_C.py").read())
else:
    print("Invalid choice.")