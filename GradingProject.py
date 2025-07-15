#------ Grading System ------#

for i in range(5):
    Marks = int(input("Enter your marks (0–100): "))
    
    if 0 <= Marks <= 100:
        if Marks >= 90:
            grade = "A"
        elif Marks >= 80:
            grade = "B+"
        elif Marks >= 70:
            grade = "B"
        elif Marks >= 60:
            grade = "C"
        else:
            grade = "D"
        print("Grade of student is ->", grade)
    else:
        print("❗ Invalid marks! Please enter a value between 0 and 100.")

print("\n✅ Code Ended. Congrats to those who got an A Grade!")
