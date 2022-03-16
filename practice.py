print(5)
print(-10)
print(1000)
print(5+3)
print(2*5)
print(3*(3+1))
print("풍선")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print('ㅋ'*9)
# 참/거짓
print(5>10)
print(5<10)
print(True)
print(not True)
print(not (5>10))
# 변수
animal = "강아지"
name = "연탄이"
age =4
hobby = "산책"
is_adult = age >=3

print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "살이며, " +hobby+ "을 좋아해요")
# + 대신에 , 로도 문장을 합칠수있다.
# ,로 대신할경우 str()을 쓰면 안된다.
print(name,"는", age, "살이며 " ,hobby, "을 좋아해요")
print(name + "는 어른일까요?" +str(is_adult))

# 퀴즈 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station

# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력

# 출력문장 : XX 행 열차가 들어오고 있습니다.

station = "사당"
print(station, "행 열차가 들어오고 있습니다.")

station = "신도림"
print(station, "행 열차가 들어오고 있습니다.")

station = "인천공항"
print(station, "행 열차가 들어오고 있습니다.")

# 연산자
print(2**3) #2^3
print(5%3) # 나머지 구하기

print(5//3) # 몫 구하기

#boolean
print(5 > 3) # 참,거짓
print(4>=7)
print(3==3) #같다
print(3+3 == 6)

print(1 != 3) # 같지않다.

#비교연산자
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 < 5))
print((3 > 0) | (3 < 5))

#숫자 처리 함수
print(abs(-5)) #절대값
print(pow(4, 2)) # 4^2
print(max(5, 12)) # 최대값
print(min(5, 12)) # 최소값
print(round(3.14)) # 반올림

 # math를 import한다.
from math import*
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근 구하기 

#랜덤함수
from random import*

print(random()) # 0.0부터 1.0까지의 랜덤 수
print(random() * 10) #0.0부터 10.0미만의 랜던 수
print(int(random() * 10)) # 0부터 10까지의 랜덤 수
print(int(random() * 10) + 1) # 1부터 10까지의 랜덤 수

#로또 값 출력
print(int(random() * 45) + 1) # 1부터 45까지의 랜덤 수

print(randrange(1, 46)) # 1 부터 46미만의 랜덤 수
print(randint(1, 45)) # 1부터 45이하의 랜덤 수

'''퀴즈
당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터리를 하는데 3번은 온라인으로 하고 1번은 오프라인으로
하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을
작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날ㅉ는 다름을 감안하여 최소 일수인 28일 이내로정함
조건3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

출력문 : 오프라인 스터디 모임 날짜는 매월 xx 일로 선정되었습니다.
'''
from random import*

date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 ",date,"일로 선정되었습니다.")

#문자열
string = """
이렇게 따옴표를 6개 만들면
띄어쓰기, 줄 바꿈 모두 가능함.
"""
print(string)

#슬라이싱 (필요한 정보만 잘라서 사용 index는 0부터 시작)
jumin = "970219-1110610"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # index 값이 0 부터 2미만
print("월 : " + jumin[2:4]) # index 값이 2 부터 4미만
print("일 : " + jumin[4:6]) # index 값이 4 부터 6미만
print("생년월일 : " + jumin[:6]) # index 값이 처음부터 6미만
print("주민번호 뒷자리 : " + jumin[7:])# index 값이 7 부터 끝까지
print("주민번호 7자리(뒤에서부터)" + jumin[-7:])

#문자열 처리 함수

python = "python is Amazing"
print(python.lower()) #전부 소문자로 출력
print(python.upper()) #전부 대문자로 출력
print(python[0].isupper()) #index 값이 대문자인지 참,거짓으로 알려줌
print(len(python)) # 총 길이를 알려준다.
print(python.replace("python", "java")) # 앞 글자를 뒤 글자로 바꿔준다.

index = python.index("n") # python 이라는 변수에서 "n" 이라는 글자가 몇번째 index에 있는 알려준다.
print(index)
index = python.index("n", index + 1) # python 이라는 변수에서 "n" 이라는 글자 +1 index 부터 다음 "n"의 index 값을 알려준다.
print(index)

print(python.find("java")) # 찾는 문자가 없으면 -1이라는 값을 반환한다.
# print(python.index("java")) # 찾는 문자가 없으면 에러가 뜬다.
print(python.count("n")) # python 이라는 변수에 "n" 이 몇개나 들어있는지 알려준다.



# 문자열 포멧 
# d = int, s = String, c = char// s로 int,String,char 모두 가능함
# 방법 1
print("나는 %d살 입니다." % 20) # %d 에 %20이 들어간다.
print("나는 %s을 좋아해요." % "프로그래밍") # %s 에 %"프로그래밍"이 들어간다.
print("Apple은 %c로 시작해요." % 'A') # %c 에 %'A'가 들어간다.
print("나는 %s색을 좋아하고 숫자 %s를 싫어합니다." % ("보라색" , 10)) # 혼용 가능

#방법2
print("나는 {}을 좋아합니다." .format("언어")) # {}안에 .format()함수가 들어간다.
print("나는 {}과 {}을 좋아합니다." .format("언어" , 5)) # 다중입력도 가능하다.
print("나는 {0}과 {1}을 좋아합니다." .format("언어" , 5)) # index를 줄수도있다
print("나는 {1}과 {0}을 좋아합니다." .format("언어" , 5)) # index 값을 바꿀수도있다.

#방법 3
print("나는 {age}살 이며 {color}색을 좋아합니다." .format(age = 26 , color = "빨간색")) # 변수처럼 사용도 가능하다.
