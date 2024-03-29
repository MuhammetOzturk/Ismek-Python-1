def us_alma(taban, us):
    if us == 0:
        return 1
    else:
        return taban * us_alma(taban, us-1)

print(us_alma(2, 3)) 
