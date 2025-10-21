# taking 5 marks of students and making avg and grde 
marks = []# list create kari ek empty 
for i in range(5):# for loops runs 1 less alwys agr 5 dia haito it runs 0,1,2,3,4
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark) # apeend fuction is to add elements to list 

average = sum(marks) / len(marks) # sum in list is to add add elements 
# avg kya hota hai type kar yahan average = sum / total 
# len is to take the eln of the list 

print(f"The average marks are: {average:.2f}")

if average > 90:
    print("Grade: A")
elif average > 80:
    print("Grade: B")
elif average > 70:
    print("Grade: C")
elif average > 60:
    print("Grade: D")
else:
    print("Grade: F")
    
# match case