# basic use of if ata hai
# if  is used to check some condition
# dhyn idhr
# 1) agr age 18> --- voter and age<18 ----not a voter
# likh program
n = int(input("Enter age :- "))
if n>= 18:
    print("Voter")
else:
    print("Not a Voter")

# elif ---- more than 2 conditions

# accha marks ---- 90> A , 80-90 -- B and so on marks 
# 1) ek subjject ke 
# 2) 5 subjects --- unki average and avg se grade 
# 3) User defined no. of subjects 

# 1 One subject 
marks = int(input("Enter marks :- "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")


# 2nd 5 subjects and 3rd also done
# this can be done using (Chosse now --- List , arrays or direct input)
marks = []# ham list ka use karenge cause data taking easy hai and better bhi 
n = int(input("Enter number of subjects :- "))
for i in range (n):
    marks = int(input("Enter marks :- "))
     
    avg = sum(marks) / len(marks) # sum and len list ke functions hain 
    if avg >= 90:
        print("A")
    elif avg >= 80:
        print("B")
    elif avg >= 70:
        print("C")
    elif avg >= 60:
        print("D")
    else:
        print("F")  

# make a calculator --- Classwork 10 min do it and post code on whatsapp
# take number two numbers 
# ask user ki kya karna hai like + , - , * ,% , / , //
# isko phele if se kar and elif se and then match case 
# phele if and elif use kar and do it on ur pc without auto completion use and send code on whatsapp u have 10 min starting now
# 7 min 