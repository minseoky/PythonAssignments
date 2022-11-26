import random
import closet

def isRain(rain):
    if rain == '비 안옴' :
        print("오늘은 비가 오지 않네요!")
    elif rain == '비':
        print("오늘은 비가 오니 우산을 꼭 챙기세요.")
    elif rain == '비 또는 눈':
        print("오늘은 비 혹은 눈이 오니 우산을 챙기세요.")
    elif rain == '눈':
        print("오늘은 눈이 옵니다.")
    elif rain == '소나기':
        print("오늘은 소나기가 오니 우산을 꼭 챙기세요")

def setStage(temp):#현재 온도 기준으로 stage분류
    currentTemp = int(temp)
    stage = 8 #28도 이상
    if currentTemp < 4: #~4도
        stage = 1
    elif currentTemp < 8: #5~8도
        stage = 2
    elif currentTemp < 11: #9~11도
        stage = 3
    elif currentTemp < 16: #12~16도
        stage = 4
    elif currentTemp < 19: #17~19도
        stage = 5
    elif currentTemp < 22: #20~22도
        stage = 6
    elif currentTemp < 27: #23~27도
        stage = 7
    return stage

def todayTemp(stage):
    closet.Classification() #closet 모듈의 데이터 분류
    if stage == 1: #겨울
        print("날씨가 매우 춥습니다. 아래의 옷을 입어보는건 어떤가요?")
        print(random.choice(closet.top_list_winter))
        print(random.choice(closet.pants_list_winter))
        print(random.choice(closet.outer_list_winter))
    elif stage == 2: #겨울
        print("날씨가 춥습니다. 아래의 옷을 입어보는건 어떤가요?")
        print(random.choice(closet.top_list_winter))
        print(random.choice(closet.pants_list_winter))
        print(random.choice(closet.outer_list_winter))
    elif stage == 3: #겨울
        print("날씨가 조금 춥습니다. 아래의 옷을 입어보는건 어떤가요?")
        print(random.choice(closet.top_list_winter))
        print(random.choice(closet.pants_list_winter))
        print(random.choice(closet.outer_list_winter))
    elif stage == 4: #가을, 봄
        print("날씨가 서늘합니다. 아래의 옷을 입어보는건 어떤가요?")
        print(random.choice(closet.top_list_spring))
        print(random.choice(closet.pants_list_spring))
        print(random.choice(closet.outer_list_spring))
    elif stage == 5: #가을, 봄
        print("날씨가 선선합니다. 아래의 옷을 입어보는건 어떤가요?")
        print(random.choice(closet.top_list_spring))
        print(random.choice(closet.pants_list_spring))
        print(random.choice(closet.outer_list_spring))
    elif stage == 6: #가을, 봄
        print("날씨가 조금 덥습니다. 아래의 옷을 입어보는건 어떤가요?")
        print(random.choice(closet.top_list_spring))
        print(random.choice(closet.pants_list_spring))
        print(random.choice(closet.outer_list_spring))
    elif stage == 7: #여름
        print("날씨가 덥습니다. 아래의 옷을 입어보는건 어떤가요?")
        print(random.choice(closet.top_list_summer))
        print(random.choice(closet.pants_list_summer))
        print(random.choice(closet.outer_list_summer))
    elif stage == 8: #여름 엄청더우니 아우터 추천안함
        print("날씨가 매우 덥습니다. 아래의 옷을 입어보는건 어떤가요?")
        print(random.choice(closet.top_list_summer))
        print(random.choice(closet.pants_list_summer))
