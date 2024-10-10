#Soru 7
def rekursif(n):
    print(n)
    if not type(n)== list :
        return [n]
    elif type(n) == list and len(n) == 0:
        return []
    return rekursif(n[0]) + rekursif(n[1:])



liste = [[1,2],3,[[[4,5]]],[6]]
print(rekursif(liste))
