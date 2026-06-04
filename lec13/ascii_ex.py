def toggle_ch(alphabet):
    if ord(alphabet)>=65 and ord(alphabet)<=90: #A~Z 소문자로 바꿔야함
        return chr(ord(alphabet) + 32)
    elif ord(alphabet)>=97 and ord(alphabet)<=122: #a~z 대문자로 바꿔야함
        return chr(ord(alphabet) - 32)
    return alphabet

def toggle_text(text):
    result = ""
    for c in text:
        result += toggle_ch(c)
    return result


def main():
    print(ord("가"))
    print(ord("A"))
    print(chr(65))
    print(ord("z"))
    print(ord("Z"))
    print(toggle_ch("A"))
    print(toggle_text("Hello, World!")) # 결과값 : hELLO, wORLD!

if __name__ =="__main__":
    main()