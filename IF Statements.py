temperature = input("Give temp: ")
if int(temperature) >= 30:  # Temp is from 30 to infinite
    print("Gaand phar garmi")
    print("Mu mei le")
elif int(temperature) >= 20:  # Temp is from 20 to 30
    print("Acha din")
elif int(temperature) >= 10:  # Temp is form 10 to 20 
    print("boht acha hei")
else:  # Temp is from negative infinity to 10
    print("Gand phar sardi")