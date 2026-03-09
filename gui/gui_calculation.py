# .exe으로 바꿔보기
# PyInstaller설치하기
# (1) pip install pyinstaller

# pyinstaller --onefile --noconsole 폴더이름/파일이름.py
# gui/gui_calculation.py
# https://customtkinter.tomschimansky.com/documentation/
import customtkinter as ctk
ctk.set_appearance_mode("dark")
'''
-------------
            0             <- 엔트리
-------------
[7][8][9][/]            <- 버튼 20개
[6][5][4][*]
[1][2][3][-]
[c][0][=][+]


'''
# import tkinter as tk
w = ctk.CTk()
# 윈도우.title("제목")
# 윈도우.resizable(False, False)
w.title('천재인 내가 만든 계산기')
w.geometry('248x407')
w.resizable(False, False)

# 엔트리위젯생성하기
# 위젯이름 = tk.Entry(윈도우이름)
# 위젯이름 = tk.Button(윈도우이름,text="버튼내용")
# 배치는 이제 그리드로! 위젯이름.grid(row=행번호, column=열번호, columnspan=차지할칸수)
# 글씨 font = ("글꼴이릅",사이즈,스타일(bold,itelic,underline)
# 엔트리위젯옵션: justify="right"
# border_width
n = ctk.CTkEntry(w, justify = 'right', font = ('Arial', 50), border_width = 0)
# grid에게 꽉차게 하기 sticky="ew"
# grid옵션 ;ipady="여백크기"
n.grid(row = 0, column = 0, columnspan = 4, sticky = 'ew', ipady = '70')


# 버튼 내용과 위치를 따로 변수
# button text를 2차원리스



button_text = [
    [7, 8, 9, '/'],
    [4, 5, 6, "*"],
    [1, 2, 3, "-"],
    ['AC', 0, '=', '+']
]


# 위젯이름 = tk.Button(윈도우이름,text="버튼내용", command=함수이름)
def clickbutton(text):
    print(text)
    # 클릭버튼을 눌렀을때, n엔트리에 추가하기(뒤로,tk.END)
    # 엔트리이름.insert(위치, 내용)
    n.insert(ctk.END, text)


# lambda : 한줄함수
# lambda : 표현식  => return문 없이도 바로 표현식이 반환된다.
# lambda 매개변수: 표현식  => return문 없이도 바로 표현식이 반환된다.



def allclear():
    print('지우기')
    # 엔트리의 전체 내용을 지우기
    # 엔트리이름.delete(시작, 끝tk.END)
    n.delete(0, ctk.END)

def total():
    print('계산')
    # 위에 내용을 가져와서 계산하기
    # 앤트리이름.get()
    # eval("수식문자열") : 계산해주는 함수 "1+2"
    eclipse = n.get()
    # 전체를 지우고
    # 계산한 값을 엔트리에 추가하기 
    allclear()
    n.insert(ctk.END, eval(eclipse))

for i in range(len(button_text)):    
    for j in range(len(button_text[i])):
        # 버튼내용에 *,/,+,-,ac,del,....
        a = button_text[i][j]

        # 버튼 내용이 =일경우, 조건문 써서 따로 만들기
        # 아닐경우에는 기존 버튼 사용
        # 계산하는 함수와 연결하기
        if a == '=':
            but = ctk.CTkButton(w, text = a, command = total, font = ('Arial', 27), width = 60, height = 50) 
        elif a == 'AC':
            but = ctk.CTkButton(w, text = a, command = allclear, font = ('Arial', 27), width = 60, height = 50)
        else :
            # 사이즈 옵션 : width=가로길이, height=세로길이
            but = ctk.CTkButton(w, text = a, command = lambda x=a: clickbutton(x), font = ('Arial', 27), width = 60, height = 50)
        but.grid(row = 1 + i, column = j, pady = 1, padx = 1)


# 숫자를 두개넣으면 두수의 합을 구하고
# # 1개만 넣을경우에는 1을 더해서 결과를 내보내는 함수
# def addone(x,y=1):
#     return x+y

# print(addone(1))
# print(addone(5,3))

w.mainloop()






