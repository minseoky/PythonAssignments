clothes_list = list()
top_list = list()
pants_list = list()
outer_list = list()


class Clothes:
    count = 0
    def __init__(self,season,brand,name):
        self.season = season
        self.brand = brand
        self.name = name
        Clothes.count += 1
        clothes_list.append(self)

    def __str__(self):
        return f'{self.name} : {self.season}, {self.brand}'


class Top(Clothes):
    count = 0
    def __init__(self,season,brand,name):
        super().__init__(season,brand,name)
        Top.count += 1
        top_list.append(self)

    def __str__(self):
        return f'상의 - {self.name} : {self.season}, {self.brand}'



class Pants(Clothes):
    count = 0
    def __init__(self,season,brand,name):
        super().__init__(season,brand,name)
        Pants.count += 1
        pants_list.append(self)

    def __str__(self):
        return f'하의 - {self.name} : {self.season}, {self.brand}'


class Outer(Clothes):
    count = 0
    def __init__(self,season,brand,name):
        super().__init__(season,brand,name)
        Outer.count += 1
        outer_list.append(self)

    def __str__(self):
        return f'아우터 - {self.name} : {self.season}, {self.brand}'


def countClothes():
    print("현재 옷장에 " + str(Clothes.count) + "개의 옷이 있습니다.")
    #기타

def myClothes():
    print("내가 가진 옷 목록:")
    print(*clothes_list, sep='\n')

#가을과 봄 옷은 합침.
top_list_spring = list()
pants_list_spring = list()
outer_list_spring = list()
top_list_summer = list()
pants_list_summer = list()
outer_list_summer = list()
top_list_winter = list()
pants_list_winter = list()
outer_list_winter = list()

def Classification():
    for i in top_list:
        if i.season == '봄' or i.season == '가을':
            top_list_spring.append(i)
        elif i.season == '여름':
            top_list_summer.append(i)
        elif i.season == '겨울':
            top_list_winter.append(i)

    for i in pants_list:
        if i.season == '봄' or i.season == '가을':
            pants_list_spring.append(i)
        elif i.season == '여름':
            pants_list_summer.append(i)
        elif i.season == '겨울':
            pants_list_winter.append(i)

    for i in outer_list:
        if i.season == '봄' or i.season == '가을':
            outer_list_spring.append(i)
        elif i.season == '여름':
            outer_list_summer.append(i)
        elif i.season == '겨울':
            outer_list_winter.append(i)



#데이터셋
Top('겨울','무신사스탠다드','베이식 긴팔 티셔츠')
Top('겨울','수아레','하프터틀넥 니트')
Top('겨울','예일','후드')
Top('겨울','디스이즈네버댓','후드')
Top('겨울','커버낫','코튼티셔츠')

Top('가을','드로우핏','레이어드티셔츠')
Top('가을','어커버','롱티셔츠')
Top('가을','지오다노','레이어드 반팔 티셔츠')

Top('여름','커버낫','서퍼맨 반팔 티셔츠')
Top('여름','무신사스탠다드','릴렉스 핏 크루 넥 반팔 티셔츠')

Top('봄','드로우핏','레이어드티셔츠')
Top('봄','어커버','롱티셔츠')
Top('봄','지오다노','레이어드 반팔 티셔츠')

Pants('겨울','브랜슨','와이드핏 트레이닝 스웨트 팬츠')
Pants('겨울','토피','와이드 데님 팬츠')
Pants('겨울','브랜디드','잭 블랙 진스')
Pants('겨울','토르티멘토','와이드 핏 조거팬츠')

Pants('가을','시그니처','더블턱 와이드 슬랙스')
Pants('가을','퍼블릭아이콘','롱 아이드 퍼플팬츠')
Pants('가을','빅 유니온','정글팬츠')

Pants('여름','무신사스탠다드','유틸리티 쇼츠')
Pants('여름','나이키','스우시 반바지 블랙')
Pants('여름','다이클레즈','클래식 벤딩 반바지')

Pants('봄','시그니처','더블턱 와이드 슬랙스')
Pants('봄','퍼블릭아이콘','롱 아이드 퍼플팬츠')
Pants('봄','빅 유니온','정글팬츠')

Outer('겨울','스파오','베이직푸퍼 패딩')
Outer('겨울','예일','웜 업 퀄팅')
Outer('겨울','더폴','오버사이즈 코트')
Outer('겨울','도프제이슨','무스탕 자켓')

Outer('가을','무신사스탠다드','후드 스웨트 집업')
Outer('가을','파르티멘토','필드 자켓 블랙')
Outer('가을','무신사스탠다드','베이직 블레이저')

Outer('여름','트릴리온','온오프 하프 가디건')

Outer('봄','파르티멘토','필드 자켓 블랙')
Outer('봄','무신사스탠다드','베이직 블레이저')

