#삼각형의 밑변과 높이를 입력 받아 그 삼각형의 넓이를 출력하는 프로그램을 작성하세요

print('삼각형의 넓이 출력')
base_line=float(input('삼각형의 밑변을 입력하세요'))
height=float(input('삼각형의 높이를 입력하세요'))
area=height*base_line*0.5
print('삼각형의 넓이는', area,'입니다')

#화씨 온도를 입력받아 섭씨 온도로 변환하는 프로그램을 작성하세요

print('화씨 섭씨 변환')
fahrenheit=float(input('화씨를 입력하세요'))
celsius=(fahrenheit-32)/1.8
print('화씨온도',fahrenheit, '도 는 섭씨온도', celsius, '도 입니다')

#물체의 질량과 속도를 입력 받아 운동에너지의 값을 구하는 프로그램을 작성하세요.

print('운동에너지 계산')
mass=float(input('물체의 질량을 입력하세요'))
velocity=float(input('속도를 입력하세요'))
kinetic_energy=0.5*mass*velocity**2
print('운동에너지는',kinetic_energy, '입니다')

#출생 연도를 입력받아 그에 맞는 띠를 출력하는 프로그램을 작성하세요.

birth_year=int(input('태어난 해를 입력하세요'))
if birth_year%12==0:
    print('당신은 원숭이띠 입니다')
elif birth_year%12==1:
    print('당신은 닭띠 입니다')
elif birth_year%12==2:
    print('당신은 개띠 입니다')
elif birth_year%12==3:
    print('당신은 돼지띠 입니다')
elif birth_year%12==4:
    print('당신은 쥐띠 입니다')
elif birth_year%12==5:
    print('당신은 소띠 입니다')
elif birth_year%12==6:
    print('당신은 범띠 입니다')
elif birth_year%12==7:
    print('당신은 토끼띠 입니다')
elif birth_year%12==8:
    print('당신은 용띠 입니다')
elif birth_year%12==9:
    print('당신은 뱀띠 입니다')
elif birth_year%12==10:
    print('당신은 말띠 입니다')
elif birth_year%12==11:
    print('당신은 양띠입니다')

#2차 방정식의 각 계수를 입력받아 2차 방정식의 근을 계산하여서 출력하는 프로그램을 작성하세요.

print('이차 방정식의 근 계산')
a=float(input('이차방정식의 이차항의 계수를 쓰시오(0을 제외한)'))
b=float(input('이차방정식의 일차항의 계수를 쓰시오'))
c=float(input('이차방정식의 상수항의 계수를 쓰시오'))
root1= (-b+(b*b-4*a*c)**0.5)
root2= (-b-(b*b-4*a*c)**0.5)
root=-b

if a==0:
    print('이차방정식이 아닙니다')
else:
    if b*b-4*a*c==0:
        print('이차방정식은 중근', root/(2*a),'를 갖습니다')
    else:
        print('이차방정식은 두 근', root1/(2*a), root2/(2*a),'를 갖습니다')
