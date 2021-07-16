A=int(input("score="))
if (A >= 80 and A <= 100):
    print("A")
elif (A >= 75 and A <= 79):
    print("B+")
elif (A >= 70 and A <= 74):
    print("B")
elif (A >= 65 and A <= 69):
    print("C+")
elif (A >= 60 and A <= 64):
    print("C")
elif(A >= 55 and A <= 59):
    print("D+")
elif (A >= 50 and A <= 54):
    print("D")
elif (A >= 0 and A <= 49):
    print("F")
else:
    print ("error") 