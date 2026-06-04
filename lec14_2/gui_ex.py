import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk() #변수명 (창 이름을 정해줌 (root로 정해줌)/ 중복조심
ROOT.withdraw()

def gui_input(text):
    return simpledialog.askstring(title="Test",
                                  prompt=text)

def main():

    name = gui_input("이름을 입력하세요 =")
    print(f"{name}님 안녕하세여")

if __name__=="__main__":
    main()