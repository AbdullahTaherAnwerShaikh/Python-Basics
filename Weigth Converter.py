weigth= input("Weight: ")
measurement= input("(K)g or (L)bs: ")
if str(measurement.upper()) == "K" :
    x=int(weigth) * 2.20462
    print(x)
elif str(measurement.upper()) == "L":
    y= int(weigth) // 2.20462
    print(y)