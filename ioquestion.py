
# 1. Open students.txt in read mode and print its content.
# 2. Read only the first line of the file.
# 3. Read all lines into a list and print them.
# 4. Loop through the file and print each line separately.
# 5. Count the number of students (lines) in the file.
# 2. Write Mode (w)
# 6. Open students.txt in write mode and write 3 new student records.
# 7. After writing, open the file again and print its content.
# 3. Append Mode (a)
# 8. Open students.txt in append mode and add a new student: "Karan, 23, Pune".
# 9. Verify that the new student was added at the end.
# 4. Read & Write Mode (r+)
# 10. Open the file in r+ mode and update the first student’s name from "Amit" to "Amit Kumar".
# 11. Use r+ mode to move the cursor to the end of the file and add a new student "Sneha, 20,
# Hyderabad".
with open('sample.txt','r') as file:
    content = file.read()
    print (content)
    first_line = file.readline()
    print (first_line)
    for line in content:
        print (line.strip())
    