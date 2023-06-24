import random

def passgen(length):
    # butun olasi karakterler
    charset = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789[]_-."
    
    password = str()

    # 16 kere kod dondurme
    for i in range(length + 1):

        # password degiskenine yeni karakter ekleyip password degiskenine tekrar ata
        
        # password = password + charset[random.randint(0, len(charset) - 1)] 
        password += charset[random.randint(0, len(charset) - 1)]

    # password degiskenini passgen fonksiyonunun degeri haline getir (dondur) 
    return password

print(passgen(20))