# https://customtkinter.tomschimansky.com/documentation/
import customtkinter as ctk
from datetime import datetime

# 디데이 계산기
# https://superkts.com/cal/d_day/



app = ctk.CTk()
app.title("my app")
app.geometry("800x200")



# 오늘날짜를 출력해줄 라벨을 만들어보기
# ~년~월~일 ~시 ~분 ~초
today = datetime.now()

label = ctk.CTkLabel(app, text=today.strftime('%Y년 %m월 %d일 %H시 %M분 %S초 %Z'), fg_color="transparent")
# 열합치기 columnspan=합칠칸수
label.grid(row = 1, column = 0, columnspan = 6)




# 2. 특정날짜를 지정하기윈 입력받는 공간(엔트리)를 만들어보기
# [   ]년 [   ]월 [    ]일
# 2-1 세부영역 frame - 세부영역안에다가 버튼이나 글자들을 배치하기
# frame(master=윈도우이름, 사이즈)
frame = ctk.CTkFrame(master=app, width=200, height=200, fg_color = "transparent")
frame.grid(row = 2, column = 0, padx=40, pady=20)
 
entry_y = ctk.CTkEntry(frame, placeholder_text="CTkEntry")
entry_y.grid(row = 0, column = 0)
label_y = ctk.CTkLabel(frame, text='년', fg_color="transparent")
label_y.grid(row = 0, column = 1)

entry_m = ctk.CTkEntry(frame, placeholder_text="CTkEntry")
entry_m.grid(row = 0, column = 2)
label_m = ctk.CTkLabel(frame, text='월', fg_color="transparent")
label_m.grid(row = 0, column = 3)

entry_d = ctk.CTkEntry(frame, placeholder_text="CTkEntry")
entry_d.grid(row = 0, column = 4)
label_d = ctk.CTkLabel(frame, text='일', fg_color="transparent")
label_d.grid(row = 0, column = 5)

def button_callback():
    # 입력된 시간 가져오기
    #위젯이름.get()
    
    
    # 디데이 계산하기(날짜만 가져오고싶다. - 값에서 .days)
    # datime끼리 계산하면 timedelta 객체가 나온다. .days속성이 있다.
    # D-day : 당일
    # D-123123 : 미래 
    # D+123124 : 과거
    # today에서 시간을 버리고 날짜만 갖기 .date()

    '''
    <예외처리>
    - 오류가 나는 상황을 캐치해서 오류말고 메세지나 다른 행동으로 처리하는
    - 입력쪽에 예외처리를 꼭 해줘야한다.

    try:
        오류가 날수 있는 코드

    except:
        try코드 중에서 예외가 발생했을때, 처리할 코드
    
    '''
    try:
        day = int(entry_d.get())
        month = int(entry_m.get())
        year = int(entry_y.get())
        # 
        ip_date = datetime(year, month, day).date()
        ttoday = today.date()
        dday = (ip_date - ttoday).days
        result = ""
        if dday == 0:
            # 디데이라벨에 수정하기 위젯이름.configure(text=)
            result = 'D-Day'
            print('D-Day')
        elif dday > 0:
            result = 'D-' + str(dday)
            print('D-' + str(dday))
        else:
            result = 'D-' + str(-1*dday)
            print('D+' + str(-1*dday))
        label_dday.configure(text = result)

    except ValueError:
        # 디데이계산할려면 datetime객체
        # 입력이 잘못되었습니다. 다시한번 확인해주세요.
        label_dday.configure(text = '입력이 잘못되었습니다. 다시한번 확인해주세요.')
    # except 오류명: NameError, IndexError, ValueError, TypeError, FileNotFoundError
        # 해당 오류일때만 처리하기
    except:
        label_dday.configure(text = 'Error')
    


    
    
button = ctk.CTkButton(app, text="my button", command=button_callback)
button.grid(row=2, column=6, columnspan = 6, padx=20, pady=20)

# 라벨위젯: D-day 결과 표시 라벨
label_dday = ctk.CTkLabel(app, text='', fg_color="transparent")
label_dday.grid(row = 3, column = 0, columnspan = 6)
app.mainloop()


# .exe으로 바꿔보기
# PyInstaller설치하기
# (1) pip install pyinstaller

# pyinstaller --onefile --noconsole 폴더이름/파일이름.py
# gui/gui_calculation.py