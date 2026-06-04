import time
import PySimpleGUI as sg

# sg.popup("카운트다운을 시작합니다!", title="시작")

layout = [[sg.Text("10",key = "end")]]
window = sg.Window("타이머", layout, size=(150, 100))

for i in range(10,0,-1):
    event,values = window.read(timeout=10) #timeout - 0.01초 보고 아무일 없으면 카운트다운 계속 진행
    #print(i) 그대로 순서대로 진행
    #print(f"{i:3d}", end= "\r")
    if event == sg.WINDOW_CLOSED:
        break
    window.read(timeout=10) 
    window["end"].update(f"{i:3d}")
    window.refresh()

    time.sleep(1)

sg.popup("종료되었습니다!", title="끝") 
