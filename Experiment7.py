import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Rahul", 20, "BTech"])
    writer.writerow(["yash", 21, "BCA"])
    writer.writerow(["yuvi", 19, "BTech"])

print("CSV file created")
