import random
import PySimpleGUI as sg


def play_game():
    word_list = ["apple","banana","grape","peach","melon","lemon"]
    quiz = random.choice(word_list)
    answer_list = []
    for _ in range(len(quiz)):
        answer_list.append("_")

    trial = 7
    
    sg.popup("hangman 게임을 시작합니다!!!!!", title="시작")

    
    for ans in range(trial): 
        question = "" 
        for i in range (len(answer_list)):
            if i == len(answer_list) -1: #글자를 하나하난 쪼갠거 마지막 글자 
                question+= answer_list[i] #question에 문자 넣기..
            else:
                question+= answer_list[i] +" "# 문자가 아니면 공백넣기 -> 눈에 잘띄게 하기 위해사
        guess = sg.popup_get_text(f"{question} (trial={trial}) 답을 입력하시오 => ", title="행맨")

        if guess in quiz: #정답일때
            for i in range(len(quiz)):
                if quiz[i] == guess: #i번째 글자 == guess 리스트니까 [] 사용
                    answer_list[i] = guess #입력값 넣어주기
        trial -= 1

        # _ 가 없어짐(다채워짐 => 성공 / trial이 끝남 -> 실패

        if "_" not in answer_list:
            sg.popup(f"축하합니다!!!!!!!!!! 정답 {quiz}를 맞추셧습니다!!", title="성공")            
            break 
        #중단하고 성공했다고 알리기
         

    # 기회가 끄탐
    if trial == 0:
        sg.popup(f"게임 오버! 아쉽지만 기회를 모두 소진했습니다. 정답은 '{quiz}' 였습니다.", title="실패")


def main():
    start = play_game()

if __name__=="__main__":
    main()