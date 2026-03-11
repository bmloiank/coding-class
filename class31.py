#미션
# 블루웨일이 23시 40분 로봇들이 들은 목소리를 출력해보기


#Code
# 목소리
class voice:
    def __init__(self, tone, pitch, frequency, speed, decibel):
        self.tone = tone #85~255
        self.pitch = pitch #60~300
        self.frequency = frequency #100~400Hz 
        self.speed = speed #0~500spm
        self.decibel = decibel # 50~2000

# 공원로봇
class park_info_robot:
    def __init__(self, list, name=0):
        self.list = list # 시간/보이스 저장된 딕셔너리 리스트
        self.name = name # 로봇이름
  
    def say_hi():
        print('Hi, ask me anything.')
    
    # 시간이 주어졌을때, 해당 시간(2050 숫자로)에 들은 목소리를 출력하기 => 메서드
    # 딕셔너리의 값뽑기 변수이름[key명] 변수이름.get(key)
    def speak_voice(self, time, target):
        for i in range(len(self.list)):
            dic = self.list[i]
            # print(dic['time'])
            if dic['time'] == time:
                # 보이스의 속성을 tone, pitch, frequency, speed, decibel
                # 타겟 보이스랑 같은 목소리를 갖고 있는 로봇의 이름을 찾기
                if target.tone == dic['voice'].tone and target.pitch == dic['voice'].pitch and target.frequency == dic['voice'].frequency and target.speed == dic['voice'].speed and target.decibel == dic['voice'].decibel:
                    print(self.name)

# 인스턴스 생성을 많이 한다.

#voice 객체 생성부. 미션 수행시 수정하지 않습니다.
# 딕셔너리(시간이랑, 목소리인스턴스) 가 들어있는 리스트
list1 = [
    {
        'time':2050, #20시50분
        'voice':voice(183,70,389,196,19) # voice인스턴스
    },
    {'time':2306,'voice':voice(214,200,230,13,54)}
]
list2 = [
   {'time':1114,'voice':voice(205,82,270,227,68)},
   {'time':1744,'voice':voice(167,73,302,445,35)},
   {'time':2311,'voice':voice(177,230,266,446,51)}
   ]

list3 = [{'time':2250,'voice':voice(98,191,229,208,52)},{'time':1402,'voice':voice(109,241,197,224,33)}]
list4 = [{'time':1835,'voice':voice(195,290,137,471,61)},{'time':1440,'voice':voice(178,299,332,22,58)},{'time':1849,'voice':voice(162,250,192,320,61)}]
list5 = [{'time':1728,'voice':voice(160,285,327,439,60)},{'time':2340,'voice':voice(156,88,212,25,52)},{'time':2340,'voice':voice(96,268,113,170,70)}]
list6 = [{'time':1940,'voice':voice(203,103,340,10,18)},{'time':2340,'voice':voice(152,278,120,357,66)},{'time':1356,'voice':voice(174,215,266,106,41)}]
list7 = [{'time':1300,'voice':voice(103,107,258,430,19)},{'time':1413,'voice':voice(85,80,279,30,11)},{'time':1527,'voice':voice(116,181,248,144,22)}]
list8 = [{'time':1740,'voice':voice(194,86,391,68,19)},{'time':1627,'voice':voice(107,248,171,351,35)},{'time':2217,'voice':voice(88,101,278,434,10)}]
list9 = [{'time':2340,'voice':voice(151,270,113,170,70)},{'time':2340,'voice':voice(152,278,120,356,66)},{'time':2405, 'voice':voice(150,200,300,460,10)},{'time':2416, 'voice':voice(230,152,258,200,65)}]
#voice 객체 생성부. 미션 수행시 수정하지 않습니다.
 
#로봇 객체 rb_1~9 생성부. 미션 수행시 수정하지 않습니다.
# 로봇인스턴스
rb_1 = park_info_robot(list1, 'R1')
rb_2 = park_info_robot(list2, 'R2')
rb_3 = park_info_robot(list3, 'R3')
rb_4 = park_info_robot(list4, 'R4')
rb_5 = park_info_robot(list5, 'R5')
rb_6 = park_info_robot(list6, 'R6')
rb_7 = park_info_robot(list7, 'R7')
rb_8 = park_info_robot(list8, 'R8')
rb_9 = park_info_robot(list9, 'R9')
#로봇 객체 rb_1~9 생성부. 미션 수행시 수정하지 않습니다.

# 추가,
# 타겟목소리
target = voice(152, 278, 120, 356, 66)

rb_1.speak_voice(2340, target)
rb_2.speak_voice(2340, target)
rb_3.speak_voice(2340, target)
rb_4.speak_voice(2340, target)
rb_5.speak_voice(2340, target)
rb_6.speak_voice(2340, target)
rb_7.speak_voice(2340, target)
rb_8.speak_voice(2340, target)
rb_9.speak_voice(2340, target)

