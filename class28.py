class pixel:
    def __init__(self, r, g, b):
        self.red=r
        self.green=g
        self.blue=b



import random
import copy
random.seed(16)
paintingsample = [[0]*8 for i in range(8)]
for i in range(8):
  for j in range(8):
   paintingsample[i][j]=pixel(random.randint(0,255), random.randint(0,255), random.randint(0,255))
painting1=copy.deepcopy(paintingsample)
##pixel 클래스 객체 painting1, painting2 생성부. 미션 수행 시 수정하지 않습니다.
pic1 = copy.deepcopy(painting1[0])
pic1[0].red = 0
pic1[1].red = 1
pic1[2].red = 0
pic1[3].red = 0
pic1[4].red = 0
pic1[5].red = 0
pic1[6].red = 1
pic1[7].red = 1
pic2 = copy.deepcopy(painting1[1])
pic2[0].red = 0
pic2[1].red = 1
pic2[2].red = 1
pic2[3].red = 0
pic2[4].red = 1
pic2[5].red = 1
pic2[6].red = 1
pic2[7].red = 1
pic3 = copy.deepcopy(painting1[2])
pic3[0].red = 0
pic3[1].red = 1
pic3[2].red = 1
pic3[3].red = 0
pic3[4].red = 0
pic3[5].red = 1
pic3[6].red = 0
pic3[7].red = 0
pic4 = copy.deepcopy(painting1[3])
pic4[0].red = 0
pic4[1].red = 1
pic4[2].red = 1
pic4[3].red = 0
pic4[4].red = 0
pic4[5].red = 1
pic4[6].red = 0
pic4[7].red = 1
pic5 =copy.deepcopy(painting1[4])
pic5[0].red = 0
pic5[1].red = 0
pic5[2].red = 1
pic5[3].red = 0
pic5[4].red = 1
pic5[5].red = 1
pic5[6].red = 0
pic5[7].red = 1
pic6 =copy.deepcopy(painting1[5])
pic6[0].red = 0
pic6[1].red = 1
pic6[2].red = 0
pic6[3].red = 1
pic6[4].red = 1
pic6[5].red = 0
pic6[6].red = 0
pic6[7].red = 0

pic7 = copy.deepcopy(painting1[6])
pic7[0].red = 0
pic7[1].red = 1
pic7[2].red = 0
pic7[3].red = 0
pic7[4].red = 1
pic7[5].red = 1
pic7[6].red = 1
pic7[7].red = 1
pic8 = copy.deepcopy(painting1[7])
pic8[0].red = 0
pic8[1].red = 1
pic8[2].red = 0
pic8[3].red = 1
pic8[4].red = 0
pic8[5].red = 0
pic8[6].red = 1
pic8[7].red = 0
painting2=[]*8
painting2.append(pic1)
painting2.append(pic2)
painting2.append(pic3)
painting2.append(pic4)
painting2.append(pic5)
painting2.append(pic6)
painting2.append(pic7)
painting2.append(pic8)
##pixel 클래스 객체 painting1, painting2 생성부. 미션 수행 시 수정하지 않습니다.


# 미션: painting1과 painting2는 동일한 그림에서 복제한 것이다.
# 복제한거면.... 색상이 같야아 정상이죠.
# 조작했데... 조가

print(painting1)
print(painting2)

for i in range(len(painting1)):
    painting1_row = '0b'
    painting2_row = '0b'
    for j in range(len(painting1[i])):
    #   print(painting1[i][j])
      # red, green, blue 각각 속성별로 출력해보기
      # 인스턴스.속
        # print(painting1[i][j].red)
        # print(painting2[i][j].red)
    #   print(painting1[i][j].green)
    #   print(painting1[i][j].blue)
    #   if painting1[i][j].red != painting2[i][j].red:
    #      print('error')
    #   if painting1[i][j].green != painting2[i][j].green:
    #      print('error1')
    #   if painting1[i][j].blue != painting2[i][j].blue:
    #      print('error2')
        red1 = painting1[i][j].red
        red2 = painting2[i][j].red
        # print(bin(red1)[-1])
        # print(bin(red2)[-1])
        painting1_row += bin(red1)[-1]
        painting2_row += bin(red2)[-1]
    # print(painting1_row)
    # print(painting2_row)
    # print(chr(int(painting1_row, 2)))
    print(chr(int(painting2_row, 2)), end = '')