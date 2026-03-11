'''
Git
: 누가,언제,어디서, 무엇을, 어떻게, 왜 변경했는지를 기록하는 버전관리시스템

git 버전 확인
$ git --version

git config --global user.name "bmloiank"
git config --global user.email "hajupark110324@gmail.com"
git config --global core.precomposeunicode true
git config --global core.quotepath false



< git 시작하기 >
1. 원격저장소 만들기
$ git init 
>> Initialized empty Git repository in C:/Users/user/Desktop/python/.git/

2. git 현재상태보기
$ git status
- 빨간색 : 수정한 파일
- 초록색 : 저장대기 파일(add한 파일)

3. git 저장대기상태로 만들기
$ git add 디렉토리/파일이름

4. 대기상태파일들을 저장하기 
$ git commit -m "커밋한 메세지"

first project - gui

5. git 히스토리(log) 살펴보기
$ git log

commit 201ea0b3a0af77706116b878fd4fae8582a28d85 (HEAD -> main)
Author: bmloiank <hajupark110324@gmail.com>
Date:   Mon Mar 9 23:01:24 2026 +0900

    first project - gui

6. 리모트 추가
git remote add origin https://github.com/bmloiank/coding-class.git

7. 리모트 확인
git remote -v

8. 업로드 git push -u origin main


<git 흐름>
파일을 수정하면 -> stage 상태로 올려놓기 -> 저장
- untracked(저장을한번도안한파일)
- modify(저장햇으나 수정한 파일)

# 예제 opencv폴더 안에 cv01.py
# git add opencv/cv01.py
# git status
# git commit -m ""
# git log


# git remote -v
# git push -u origin main


#  임시저장하기 add
#  임시저장 취소하기 reset
# $ git reset 파일

# 전체 임시저장하기 git add . git add -A git add --all
# data dist build





# git commit -m "간단한 메세지"

# # 누구 언제 어디서 왜 자세하게 적어야한다.
# git commit # 본격적인 메세지


# VIM 리눅스(서버 컴퓨터) 에디터
# :q
# i insert모드 수정가능하다.
# esc + :q : 종료
# esc + :q! : 강제종료

# :wq : 저장하고 종료
# :wq! : 강제로 저장하고 종료
# 키보드로 명령어를 쳐서 명령어는 방법을 command line 명령어
'''