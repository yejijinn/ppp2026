text = input(f"변환하고 싶은 문자열을 입력해주세요. = ")

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

    print(toggle_text(text))


if __name__ =="__main__":
    main()