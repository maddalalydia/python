'''total_students = int(input("Enter the total number of students: "))
telugu_marks = []
english_marks = []
maths_marks = []
hindi_marks = []
science_marks = []
social_marks = []
total_marks = []
students_names = []
for i in range(total_students):
    name = input("Enter the name of student: ")
    students_names.append(name)
    telugu, english, hindi, maths, science, social = map(int,
        input("Enter marks in order (telugu english hindi maths science social): ").split())
    telugu_marks.append(telugu)
    english_marks.append(english)
    hindi_marks.append(hindi)
    maths_marks.append(maths)
    science_marks.append(science)
    social_marks.append(social)
    total = telugu + english + hindi + maths + science + social
    total_marks.append(total)
# find max marks
max_marks = max(total_marks)
# find topper index
topper_inds = []
for i in range(len(total_marks)):
    if total_marks[i] == max_marks:
        topper_inds.append(i)
# print topper details
print("\nTopper Details:")
for i in topper_inds:
    print("Name:", students_names[i])
    print("Total Marks:", total_marks[i])'''

total_students = int(input("Enter total students: "))
names = []
totals = []
for i in range(total_students):
    name = input("Enter student name: ")
    names.append(name)
    t,e,h,m,s,so = map(int,input("Enter 6 subject marks: ").split())
    total = t+e+h+m+s+so
    totals.append(total)
max_marks = max(totals)
index = totals.index(max_marks)
print("Topper Name:", names[index])
print("Total Marks:", max_marks)