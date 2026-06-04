import random
import PySimpleGUI as sg

def random_number(rotate):
    #n =random.randint(1,45)

    for n in range(int(rotate)):
        number = random.sample(range(1,46),6)
    sg.popup(number, title="로또 번호 추출 완료")


def main():
    rotate = sg.popup_get_text(f"반복을 원하시는 횟수를 알려주세요. = ")

    random_number(rotate)

if __name__=="__main__":
    main()