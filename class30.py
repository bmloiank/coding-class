# 이선 19004
# 블루웨일 60817


# 클래스 여러개와 연결하기
# 서버(서비스를 제공하는 컴퓨터) - 보안
# 
# 웹서버 개발 


class Server:
    def __init__(self):
        # NIS server를 이용해 통신 할 수 있는 transmitter 리스트
        # 내가 승인한 유저리스트
        self.trm_list = []
        #각 주파수 별로 현재 전파되고 있는 메시지
        self.msg_list = [None,'Hi there','>>#=@.......$#^','2_8_...M..{{{#','243','today\'s news broadcasting.','this is NIS server','%$#&^#^','Input secret code.','@*DW)R_#IO-','#$$$@__&*$%','+)@!((^@',';nNiIssssss023;','16837','\sdkf','...Hel*^%-!Pp....','call with a secret code','wewrh','service location','add user','not now','commercial zone','438759234','/32.1/2/','&*)','q3284023','.....','add transmitter','....008800888','fire','438759234','baseball','&*)','q3284023','.....','........','no excuses','hey','...bal','/32.1/2/','2375','000','.....']
    # 유저를 등록하는 기능
    def addUser(self, t, c):
        self.trm_list.append(t) # t = transmitter인스턴스 
        print('New user', c ,'added.')

    # 유저를 삭제하는 기능
    def delUser(self, id):
        for i in range(len(self.trm_list)):
            if self.trm_list[i].id == id:
                del self.trm_list[i]
        print('delete completed.')

    # 메세지를 수정
    def emitMsg(self, msg):
        for freq in self.msg_list:
            freq = msg
    
    # 서버에서 메세지를 받는 메서드를 만들자.
    # 입력
    # - 유저인스턴스 : 인증된 유저들만 메세지를 받을 수 있도로 하기
    # - 해당 주파수 
    def message(self, user, freq):
        # (1) user가 trm_list안에 있는지 확인하기
        print(user.id)
        if user in self.trm_list:
            # (2) 해당 주파수에 해당되는 메세지를 가져와보자
            print(self.msg_list[freq])
        else:
            print('bye')


# 무전기 유저
class Transmitter:
    def __init__(self, id):
        self.id=id
        self.freq = 5
        print('Transmitter', id,'enrolled.')

    # 주파수 변경 : 15번
    def changeFreq(self, server, newFreq):
      if newFreq <= len(server.msg_list):
        self.freq=newFreq
        print('Frequency set to', newFreq, 'completed.')
      else:
        print('Invalid Frequency.')
    
    # 메세지 보내기
    def send(self, server, msg):
        server.msg_list[self.freq] = msg

    # 서버 연결
    def connect(self, server):
        server.message(self, self.freq)

# 서버 인스턴스를 생성
server = Server()
# 이선 19004
# 블루웨일 60817
leesan = Transmitter(19004)
bluewhale = Transmitter(60817)
# (1) 서버에 유저를 등록 

server.addUser(leesan, '이선')
server.addUser(bluewhale, '블루웨일')

# (2) 주파수를 15로 변경하기

leesan.changeFreq(server, 15)
bluewhale.changeFreq(server, 15)

leesan.connect(server)

