import tkinter as tk
from tkinter import messagebox
import json
import os


def download_plants():
    if not os.path.exists('plantmbti.json'):
        return {}
    with open('plantmbti.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def show_result(total_score, data, root):
    result_message = ""

    for name, info in data.items():
        r = info['range']

        if r[0] <= total_score <= r[1]:
           
            result_message = result_message + "이름: " + name + "\n"
            result_message = result_message + "특징: " + info['explain'] + "\n"
            result_message = result_message + "관리: " + info['care'] + "\n\n"

    messagebox.showinfo("최종 분석 결과", result_message)
    root.quit()


def process_answer(score, responses, current_q_number, questions, label, button1, button2, button3, data, root):
    responses.append(score)
    current_q_number[0] += 1
    
    if current_q_number[0] < len(questions):
        label['text'] = questions[current_q_number[0]]
    else:
        show_result(sum(responses), data, root)



def main():
   
    data = download_plants()
    questions = [
        "1. 하루 햇빛이 들어오는 시간은? (1: 적음(1~3시간)) 2: 보통(3~6시간)) 3: 많음(6시간 이상))",
        "2. 물 주는 주기는? (1: 2주 이상 2: 1주~2주 3: 1주일 이내)",
        "3. 식물을 배치할 장소는? (1: 책상 2: 거실 3: 베란다)",
        "4. 키우는 주목적은? (1: 인테리어 2: 공기정화 3: 관찰)",
        "5. 식물 관리 경험 횟수는? (1: 처음 2: 1~3번  3: 4번 이상)"
    ]
    root = tk.Tk()
    root.title("식물 MBTI 분석기")
    root.geometry("500x550")
    
    messagebox.showinfo("안내", "식물 MBTI 분석기를 시작합니다.")

    responses = []
    current_q_number = [0]
    
    label = tk.Label(root, text=questions[0], font=("Arial", 12))
    label.pack(pady=40) 

    def click_1(): 
        process_answer(1, responses, current_q_number, questions, label, button1, button2, button3, data, root)
    def click_2(): 
        process_answer(2, responses, current_q_number, questions, label, button1, button2, button3, data, root)
    def click_3(): 
        process_answer(3, responses, current_q_number, questions, label, button1, button2, button3, data, root)

    button1 = tk.Button(root, text="1점", width=20, height=2, command=click_1)
    button2 = tk.Button(root, text="2점", width=20, height=2, command=click_2)
    button3 = tk.Button(root, text="3점", width=20, height=2, command=click_3)
    
    button1.place(x=150, y=200)
    button2.place(x=150, y=270)
    button3.place(x=150, y=340)

    root.mainloop()
if __name__ == "__main__":
    main()




    