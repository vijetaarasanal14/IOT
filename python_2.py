# ----------------------------------------------------------
# Student Performance Analyzer
# ----------------------------------------------------------

students = [
    {"name": "Asha", "Maths": 78, "VLSI": 88, "Python": 92},
    {"name": "Ravi", "Maths": 95, "VLSI": 81, "Python": 89},
    {"name": "Megha", "Maths": 62, "VLSI": 72, "Python": 70},
    {"name": "Kiran", "Maths": 85, "VLSI": 90, "Python": 80},
    {"name": "Pooja", "Maths": 90, "VLSI": 78, "Python": 85}
]

# 1. Function to calculate total marks
def calculate_total(student):
    return student["Maths"] + student["VLSI"] + student["Python"]

# 2. Add 'total' key to each student's dictionary
for student in students:
    student["total"] = calculate_total(student)

# 3. Sort students by total marks (descending)
students_sorted = sorted(students, key=lambda x: x["total"], reverse=True)

# 4. Identify topper and lowest performer
topper = students_sorted[0]
lowest = students_sorted[-1]

# Subject-wise highest scores
highest_maths = max(students, key=lambda x: x["Maths"])
highest_vlsi = max(students, key=lambda x: x["VLSI"])
highest_python = max(students, key=lambda x: x["Python"])

# ----------------------------------------------------------
# 5. Save report to a text file
# ----------------------------------------------------------

report = []
report.append("STUDENT PERFORMANCE REPORT")
report.append("----------------------------------------")
report.append("Sorted Student List (High to Low Total):\n")

for s in students_sorted:
    report.append(f"{s['name']} - Maths: {s['Maths']}, VLSI: {s['VLSI']}, Python: {s['Python']}, Total: {s['total']}")

report.append("\nTOPPER:")
report.append(f"{topper['name']} with {topper['total']} marks")

report.append("\nLOWEST PERFORMER:")
report.append(f"{lowest['name']} with {lowest['total']} marks")

report.append("\nSUBJECT-WISE HIGHEST SCORERS:")
report.append(f"Maths: {highest_maths['name']} ({highest_maths['Maths']})")
report.append(f"VLSI: {highest_vlsi['name']} ({highest_vlsi['VLSI']})")
report.append(f"Python: {highest_python['name']} ({highest_python['Python']})")

# Write to file
with open("student_report.txt", "w") as f:
    f.write("\n".join(report))

print("Report saved successfully as 'student_report.txt'")
