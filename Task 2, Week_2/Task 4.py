A = ["A1_T1", "A1_T2", "A1_T3", "A1_T4", "A1_T5", "A1_T6", "A1_T7"]
A1 = int(input("A1_T1: "))
A2 = int(input("A1_T2: "))
A3 = int(input("A1_T3: "))
A4 = int(input("A1_T4: "))
A5 = int(input("A1_T5: "))
A6 = int(input("A1_T6: "))
A7 = int(input("A1_T7: "))
Total = A1+A2+A3+A4+A5+A6+A7
Average = Total / len(A)

print(f"In total you spent {Total} minutes on programming.")
print(f"Average per task was {Average} min and same rounded to the nearest integer {round(Average)} min.")