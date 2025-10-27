weight = float(input("weight"))
unit =input("K or l")
if unit == "K":
    weight = weight * 2.205
    print("weight in Lbs: " + str(round(weight,2)))
else:
    weight = weight /2.205
    print("weight in Kgs: " + str(round(weight,2    )))