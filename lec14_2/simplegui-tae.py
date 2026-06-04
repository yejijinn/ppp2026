import PySimpleGUI as sg
# 다시해봐야함 (결과물이 다름)(계산은 잘 됨))

def c2f(tc):
    return tc*1.8 +32

def f2c(tf):
    temp_c = (tf-32)*5/9
    return temp_c

def main():
    # Define the window's contents
    layout = [[sg.Text("섭씨"),
               [sg.Input(key='-INPUT_C-',size =10)],
               [sg.Button('->')],
               [sg.Button('<-')],
               [sg.Input(key='-INPUT_F-',size =10)],
               [sg.Text("화씨")]],
               [sg.Button('Quit')]]

    
# Create the window
    window = sg.Window('섭씨 <-> 화씨 변환기', layout)

# Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        elif event == "->":
            print("섭씨를 화씨로 바꿔야해")
            window['-INPUT_F-'].update(f"{c2f(float(values['-INPUT_C-'])):.1f}")
        elif event == "<-":
            print("화씨를 섭씨로 바꿔야해")
            window['-INPUT_C-'].update(f"{f2c(float(values['-INPUT_F-'])):.1f}")     

        # Output a message to the window

# Finish up by removing from the screen
    window.close()
if __name__=="__main__":
    main()