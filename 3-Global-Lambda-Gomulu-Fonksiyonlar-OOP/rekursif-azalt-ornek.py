def azaltarak_yaz(text):
    if len(text) == 0:        
        return text
    else:
        print(text)
        azaltarak_yaz(text[:-1])
        #print(text)
azaltarak_yaz("merhaba")
