import random
import PySimpleGUI as sg

# popup - 팝업찹
# popiup_get_text - 새로운 팝업창이 뜨게 됨

def gugudan_correct():
    a= random.randint(2,9)
    b= random.randint(2,9)
    #ans = input (f"{a} x {b} =>>>?")
    ans =sg.popup_get_text(f"{a} x {b} =>>>?")
    return int(ans) == a*b

def main():
    sg.popup("구구단을 시작합니다!", title="시작")
    # while True:
    count = 0
    score = 0
    for i in range (10):
        if gugudan_correct():
            score+=10
            count+=1
            sg.popup("정답입니다!", title="결과")
        else:
            sg.popup("오답입니다!", title="결과")
    sg.popup(f"정답을 맞힌 개수는 {count}개, {score}점 입니다.")

if __name__=="__main__":
    main()