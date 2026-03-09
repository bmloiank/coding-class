# gui지원하는 모듈 tkinter tk
# import 모듈명 as 별칭

import tkinter as tk
import random
# (1) 윈도우 만들기 
# 윈도우이름 = tk.Tk() 
w = tk.Tk()
# 윈도우의 사이즈 정하기 : 윈도우이름.geometry("가로x세로")
w.geometry('900x900')


########## 창 내부 위젯 설정 ############

# 그리드시스템 grid vs pack() 
# row : 행 / column 열


# (2) 라벨 위젯을 생성하기
# 위젯이름 = tk.Label(윈도우이름, text="넣고싶은 내용")
# 위젯이름.pack() 
a = tk.Label(w, text = 'ㅎㅎ')
# a.pack()
# 위젯이름.gird(row=행번호, column=열번호)
a.grid(row = 0, column = 0)


# (3) 버튼 위젯을 생성하기
# 위젯이름 = tk.Button(윈도우이름, text="버튼에 넣고싶은 내용",command=연결한 함수이름)
def c():
    # (2-2) 라벨위젯 변경하기
    # 라벨위젯이름.config(text="바꿀내용")
    a.config(text = 'ㅋㅋ')
    print('클릭 click!')

b = tk.Button(w, text = 'ㅎㅎ', command = c)
# b.pack()
b.grid(row = 1, column = 1)



def lotto_auto():
    pick = []
    while len(pick) < 6:             # while 조건 : 조건이 만족하면 반복하다.
        num = str(random.randrange(1,46))
        if num not in pick:
            pick.append(num)
            # print(pick)
    pick.sort()                      # 리스트 정렬하기 => sorted(리스트) 리스.sort()
    print(pick)

    # map => 리스트 모든요소에 함수를 적용이 가능합니다.
    # 문자열로 넣어야한다. "구분인자".join(리스트) 
    pick_s = ' '.join(pick)
    print(pick_s)
    # ListBox에 삽입하기 listbox위젯.insert(삽입위치,내용)
    # - 맨앞은 0 / 맨뒤는 tk.END
    d.insert(tk.END, pick_s)


# 자동뽑기 버튼 만들어보기 _btn
pick_btn = tk.Button(w, text = '로!자동뽑기!또', command = lotto_auto)
# pick_btn.pack()
pick_btn.grid(row = 2, column = 6)

# 리스트박스 위젯: 여러개를 뭔가 넣을만한 위젯
# 위젯이름 = tk.Listbox(윈도우이름) 
d = tk.Listbox(w)
# d.pack()
d.grid(row = 3, column = 9)

# Entry위젯 : 한줄입력
# 위젯이름 = tk.Entry(윈도우이름,내용) 
e = tk.Entry(w)
e.grid(row = 4, column = 0)

# 로또 버튼 1~45 버튼을 생성해보기
# 9행 5열 => 별도 잘만들기 => 이차원리스트 잘 다루기^ㅁ^

# [*****] * 9행
# [*****] 



start_row = 5
# 카운트 변수 만들기
count = 0

# tkinter 사이즈 = 폰트
# font = ("폰트이름",사이즈,"스타일- bold, italic,underline,overstrike")
# width =가로 , height=높이

phone = ('Arial', 18, 'italic')

for i in range(9):          # 행 row
    for j in range(5):      # 열 column
        count = count +1
        pick_m = tk.Button(w, text = count, font = phone, width = 3, height = 1)
        pick_m.grid(row = start_row+i, column = j)


# 람다

# for i in range(45):
#     pick_m = tk.Button(w, text = i+1)
#     # pick_m.pack()
#     # if i < 10:
#     #     pick_m.grid(row = 4, column = i)
#     # elif i < 19:
#     #     pick_m.grid(row = 5, column = )
#     for j in range():
        



#####################################

# (*) 윈도우를 무한으로 띄우기
# 윈도우이름.mainloop()
w.mainloop()
