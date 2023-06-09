##### 숫자, 문자, bool 공부 
  
###### 변수 
#  name="animal"
#  print("우리집"+name+"바보")
# station="사당"
# print(station + "헹 열차가 들어오고 있습니다.")

#####연산자 
#+=, !=,*=, %= 등 

#####수식 
# print(abs(-5)) 절대값
# print(pow(4,2)) 제곱
# print(max(-5,12)) 최대, 최소
# print(round(3.14)) 반올림 

##### random함수 
# from random import * 
# print(random())
# print(random()*10)
# print(int(random()*10)+1) 
# print(int(random()*45)+1) 
# print(randrange(1,46))
# # prin(randint)
# from random import *
# number=str(int((random()*24)+4)) 
# print("오프라이 스터디 모임 날짜는 매월 "+ number + "일로 선정되었습니다.")


# ###### 문자열 처리함수 
# python="Python is Amaizing"
# print(python.upper())
# print(python.lower())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python","Java"))
# index = python.index("n")
# print(index)
# index = python.index("n",index+1)
# print(index)
# # print(python.find("n")) 
# # print(python.find("Java")) 오류나면 무조건 -1로 반환됌 
# print(python.count("n"))


# ######문자열 포맷 
# #방법1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요"%"파이썬")
# print("Apple은 %c로 시작해요" %"A")
# #방법2
# print("나느 {}을 좋아해".format(20))
# print("나는 {}과 {}을 좋아해".format("노랑","빨강"))
# print(" 나는 {0}과 {1}을 좋아해".format("노랑","빨강"))
# print("나는 {1}과 {0}을 좋아해".format("노랑","빨강"))
# #방법3
# print("나는 {age}살이며 {color}을 좋아해".format(age=20,color="빨강"))
# #방법4
# age = 20 
# color = "빨강"
# print(f"나는 {age}살이며 {color}을 좋아해")


# #####탈출문자 
# print("백문이 불여일견 \n 백견이 불여일견")
# print('나도 "나는 코딩"입니다')
# print("red apple\rpine") 
# print("redd\bapple")
# print("/t")



##########리스트########(추가, 제거, 카운트, 찾기) 
# subway=["유재석","조세호","박명수"]
# print(subway.index("조세호"))
# subway.append("하하")
# print(subway)
# subway.insert(1,"정형돈")
# print(subway)
# # print(subway.pop())
# # print(subway)
# # print(subway.pop())
# # print(subway)
# subway.append("유재석")
# print(subway.count("유재석"))
# ######정렬(바로, 거꾸로, 지우기도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)
# num_list.clear()
# print(num_list)

# ######리스트 확장, 조합
# num_list=[5,2,4,3,1]
# mix_list = ["조세호",20,True]
# num_list.extend(mix_list)
# print(num_list)




############딕셔너리##########3

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[100])
# print(cabinet.get(100))
# # print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5,"사용가능"))
# print(3 in cabinet)
# print(5 in cabinet)

# cabinet["c-20"]="조세호"
# cabinet[3]="김종국"
# # print(cabinet)
# # del cabinet["c-20"]
# # print(cabinet)
# print(cabinet)
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())
# cabinet.clear()
# print(cabinet)


##########튜플)

# menu = ("e돈까스", "치즈까스")
# print(menu[1])
# # menu.add("생선까스") → 안됌 
# print(menu)
# name, age, hobby = ("김종국",20,"코딩")
# print(name,age,hobby)



########3set)
# # my_set = {1,2,3,3,3} → 중복 없음, 순서 없음 
# #교집합
# java = {"유재석","김태호","양세형"}
# python = set(["유재석", "박명수"])
# print(java&python)
# print(java.intersection(python))
# #합집합
# print(java|python)
# print(java.union(python))
# #차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java-python)
# print(java.difference(python))
# #python할 줄 아는 사람이 늘어남 
# python.add("김태호")
# print(python)
# #삭제
# python.remove("김태호")




############자료 구조의 변경 
# menu = {"커피","우유","쥬스"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))
# menu = tuple(menu)
# print(menu, type(menu))
# menu=set(menu)


# ######quiz##########
# from random import *
# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(list)
# good=(sample(list,4))
# print("치킨당첨자: {}".format(good[0]) )
# print("커피당첨자: {}".format(good[1:]) )




##########★if★########

# weather = input("오늘 날씨는 어떄요?")
# if weather =="비" or weather=="눈":
#     print("우산을 챙기세여")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("멀라잇")

# temp = int(input("기온 어때?"))
# if 30<= temp:
#     print("더워잇")
# elif 10<= temp and temp<30:
#     print("쏘 굿")
# elif 0<= temp and temp <10:
#     print("zz")
# else:
#     print("추우잇")



# ##############for###########3333

# for waitting_no in [0,1,2,3,4]:
#     print("대기번호:{}".format(waitting_no))
# for waitting_no in range(5):
#     print("대기번호:{}".format(waitting_no))
# starbucks = ["아이언맨","토르","아이엠","그루트"]
# for customer in starbucks:
#     print("{}, 커피 준비됌".format(customer))




##############while################3

# customer = "토르"
# index = 5 
# while index>=1:
#     print("{0},커피됌. {1}번 남았어".format(customer,index))
#     index-=1
#     if index ==0:
#         print("커피끝")

# customer = "아이맨" 
# person="unknown"
# while person !=customer:
#     print("{0}. 준비됌".format(customer))
#     person = input("이름이 어떻게 됫요?")



# ###########continue.break############
# absent=[2,5]
# no_book = [8]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("수업끝 {0} 따라왕".format(student))
#         break
#     print ("{0},책읽아".format(student))



############ # for 한줄 사용 
# students = [1,2,3,4,5]
# students = [i+100 for i in students]
# print(students)

# students = ["iron man","thor","i am groot"]
# students =[len(i) for i in students]
# print(type(students))
# print(students)

# students = ["Iron man","Thor","I am groot"]
# students= [i.upper() for i in students ]
# print(students)

# from random import *

# customer= list(range(1,51))
# random_num = list(range(5,51))
    
# for i in customer:
#     random_shuf=(sample(random_num,1))
#     if random_shuf[0] >=5 or random_shuf[0] <=15:
#         circle="O"
#     else:
#         circle=" "
#     print("[{0}] {1}번째 손님 (소요시간): {2}분".format(circle,customer,random_shuf))
#     i+=1 

# cnt= 0 
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <=15:
#         print("[0] {0}번째 손님 (소요시간): {1}분".format(i,time))
#         cnt += 1 
#     else:
#         print("[ ] {0}번째 손님 (소요시간): {1}분".format(i,time))

# print("총 탑승 승객 : {0} 분".format(cnt))




# ##########튜플 ########

# menu =("돈까스","치즈까스") # 값 추가, 삭제 불가능 
# print(menu[0])

# name = "김종국"
# age = 20
# hobby="코딩"
# print(name, age,hobby)

# # (name, age, hobby)=("김종국",20,"hobby")
# # print(name, age, hobby)




######## 세트 ######## #중복x 순서x#
# my_set = {1,2,3,3,3}
# print(my_set)

# java={"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])

# print(java&python)
# print(java.intersection(python))
# print(java|python)
# print(java.union(python))
# print(java-python)
# print(java.difference(python))
# python.add("김태호")
# print(python)
# java.remove("김태호")
# print(java)





# ########자료구조의 변경 #######

# menu = {"커피","우유","쥬스"}
# print(menu,type(menu))
# menu = list(menu)
# print(menu,type(menu))
# menu = tuple(menu)
# print(menu,type(menu))
# menu=set(menu)
# print(menu,type(menu))


# from random import * 
# re=list(range(1,21))
# num_one=sample(re,4)
# print(num_one)
# print("치킨 당첨자 {}".format(num_one[0]) )
# print("커피 당첨자: {}".format(num_one[1:]))





#########함수 #########
# def open_account():
#     print("새로운 계좌 생성됨")
# def deposit(balance, money):
#     print("입금 완료, 잔액은 {}입니다.".format(balance+money))
#     return balance + money
# def withdraw(balance,money):
#     if balance >=money: # 잔액이 출금보다 많으면
#         print("출금이 완료 되었고. 잔액은 {}".format(balance - money))
#         return balance
#     else:
#         print("출금이 완료 x. 잔액 {}이야".format(balance))
#         return balance

# def withdraw_night(balance,money):
#     commission = 100 
#     return commission, balance - money - commission

# balance= 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance,500)
# commission, balance = withdraw_night(balance,500)
# print("수수료 {0} 원, 잔액 {1}원".format(commission,balance))

# print(balance)



############기본값#####333

# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어:{2}" \
#           .format(name,age,main_lang))
# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")

# #같은 학교 같은 학년 같은 반 같은 수업
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이: {1}\t주 사용 언어:{2}" \
#           .format(name,age,main_lang))
# profile("유재석")
# profile("김태호")

# 함수변수의 순서를 다르게 입력해도 똑같이 출력 가능 !!!! 
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석",main_lang="파이썬",age=20)
# profile(main_lang="파이썬",name="김태호",age=20)


###########가변인자############

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0} \t 나이:{1} \t".format(name,age), end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)
# profile("유재석",20,"python","java","c","c++","c#")
# profile("유재석",20,"python","java","","c","")


# def profile(name, age, *language):
#     print("이름: {0} \t 나이:{1} \t".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end="")
#     print()
# profile("유재석",20,"python","java","c","c++","c#", "javascript")
# profile("유재석",20,"python","java","","","")



#######지역 변수, 전역 변수##########

# gun = 10 
# def checkpoint(soldiers):
#     gun=20  ##지역변수 
#     gun = gun - soldiers
#     print("[함수 내]남은 총: {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) 
# print("남은 총 : {0}".format(gun))

# gun = 10 
# def checkpoint(soldiers):
#      global gun  ##전역변수 
#      gun = gun - soldiers
#      print("[함수 내]남은 총: {0}".format(gun))

# def checkpoint_ret(gun,soldiers):
#     gun = gun - soldiers   
#     print("[함수 내]남은 총: {0}".format(gun))
#     return gun 
# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun,2) 
# print("남은 총 : {0}".format(gun))




##########퀴즈 6##########3

# height= int(input())
# def std_weight(height,gender):
#     if gender == "male" :
#         weight_male= height * height *22
#         print("키 {0} 남자의 표준 체중은 {1} 입니다",end=""
#               .format(height,weight_male))
#     else:
#         weight_female= height * height*21
#         print("키 {0} 여자의 표준 체중은 {1} 입니다",end=""
#               .format(height,weight_female))
# std_weight(height,"male")
# def std_weight(height,gender):
#     if gender == "male" :
#         return height * height * 22
#     else:
#         return height * height * 21
# height=175
# gender="male"
# weight= round(std_weight(height/100, gender),2)
# print("{0} cm {1}의 표준체중은 {2}다".format(height,gender,weight))





##############문장 다듬기##############################33
# print("python","java",sep=",",end="?")
# print("무엇이 더 재밌을까요?")
# #########sys 아직 모름#############
# import sys 
# print("python", "java",file = sys.stdout)
# print("python", "java",file = sys.stderr)
# ############# 딕셔너리 → 튜플 ljust, rjust, zfill ############3
# scores = {"수학":0,"영어":50,"코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8),str(score).rjust(4),sep=",")
# #########은행 대기순번표 ########
# for num in range(1,21):
#     print("대기번호:" + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 "+answer+"입니다")




# ###############다양한 출력 포맷 ##########
# # 빈자리는 빈공간으로 두고 오른쪽 정렬을 하되, 총 10자리 공간을 확보 
# print("{0: >10}".format(500))
# #양수일 떈  +, 음수일 땐 - 로 표시 
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# #왼쪽 정렬, 빈칸 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리마다 ,를 찍어주기 
# print("{0:,}".format(1000000))
# # 3자리마다 ,를 찍어주기  +,- 부호도 붙이기
# print("{0:+,}".format(1000000000))
# # 3자림다 ,를 찍어주는데 부호도 붙이고 자릿수 확보도 동시에 
# # 돈인 많으면 행복합니까 빈자리는 ^로 채워주기 
# print("{0:^<+30,}".format(1000000000000))
# #소수점 출력
# print("{0:f}".format(5/3))
# #특정 소수점까지만 출력
# print("{0:.2f}".format(5/3))



# ##############파일 입출력#####33
# score_file = open("score.txt","w",encoding="utf8")
# print("수학 : 0", file =score_file)
# print("영어 : 50", file =score_file)
# score_file.close()

# score_file = open ("score.txt","w",encoding="utf8")
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()

# score_file = open ("score.txt","r",encoding="utf8")
# print(score_file.read())
# # score_file.close() 

# score_file = open ("score.txt","r",encoding="utf8")
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open ("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break   
#     print(line, end="")
# score_file.close()

# score_file = open ("score.txt","r",encoding="utf8")
# lines= score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()


##############pickle#########

import pickle 
# profile_file = open("profile.pickle","wb")
# profile = {"이름":"박명수","나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()


