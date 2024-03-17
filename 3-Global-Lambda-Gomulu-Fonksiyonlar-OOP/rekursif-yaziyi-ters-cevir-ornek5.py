def ters_çevir(s):
    if len(s) < 1:
        return s
    else:
        return  s[-1] + ters_çevir(s[:-1])
        

x=ters_çevir('Merhaba')
print(x)
