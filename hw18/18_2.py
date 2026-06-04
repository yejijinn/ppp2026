#word ="ABC"

def caesar_encode(word):
    text = list(word)
    result = "" #바구니 
    for c in text:
        if ord(c)>=65 and ord(c)<=90:
            cal = chr(ord(c)+3)
            result += cal #누적함
            
    return result

def caesar_decode(word):
    text = list(word)
    result = "" #바구니 
    for c in text:
        if ord(c)>=65 and ord(c)<=122:
            cal = chr(ord(c)-3)
            result += cal #누적함
            
    return result

def main():
    print(caesar_encode("ABC"))
    print(caesar_decode("Def"))


if __name__ =="__main__":
    main()