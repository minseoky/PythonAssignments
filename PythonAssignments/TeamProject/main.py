import requests
import json
import urllib3 #경고 무시를 위한 모듈

import closet
import mod
from pandas import json_normalize #dataframe화를 위한 판다스 모듈

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #경고 무시

#입력부---------------------------------------------------------------------------
mydate = input("오늘 날짜를 입력해 주세요(ex:20220101):") #최근 3일까지 가능
mytime = input("현재 시각을 입력해 주세요(ex:1100):") #0200, 0500, 0800, 1100, 1400, 1700, 2000, 2300시 가능
#-------------------------------------------------------------------------------
APIKEY = 'UrSIGfvuu4vQAYuh11KQRI8aBtZQ2r95EmZ950i2m9Q%2BFzL%2Fmpq77ws6k%2BwrNjah2osSOgl63Udr4D7bX7cY8A%3D%3D'

#nx=62&ny=122 경기도 용인시 수지구 좌표이고,
#numOfRows는 1~12는 현재 시간, 13~24는 다음시간< 이런식
url = 'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey=' + APIKEY + '&pageNo=1&numOfRows=12&dataType=JSON&base_date=' + mydate + '&base_time=' + mytime + '&nx=62&ny=122'

response = requests.get(url, verify=False) #https관련 보안 이슈로 인해 verify = False 인자 넣어줌
contents = response.text #api를 통해 불러온 데이터 저장


data = json.loads(contents) #json형식으로 저장된 데이터 load
stat = data['response']['body']['items']['item'] #데이터 파싱: api의 json데이터 상에 우리가 필요한 item은 response 안의 body 안의 items안에 있음.

df = json_normalize(stat) #Pandas를 활용한 dataframe화
#print(df) #데이터프레임 출력 (주석 지우면 데이터프레임 나타남)
#모든 데이터셋은 str 자료형임
current_temp = df.iloc[0]['fcstValue'] #현재 온도(1시간 단위)

current_wspeed = df.iloc[4]['fcstValue'] #현재 풍속

current_sky = df.iloc[5]['fcstValue'] #맑음(1), 구름많음(3), 흐림(4)
if(current_sky == '1'):
    current_sky = '맑음'
elif(current_sky == '3'):
    current_sky = '구름 많음'
elif(current_sky == '4'):
    current_sky = '흐림'
else:
    current_sky = '자료추출오류'

current_rain = df.iloc[6]['fcstValue'] #없음(0), 비(1), 비/눈(2), 눈(3), 소나기(4)
if(current_rain == '0'):
    current_rain = '비 안옴'
elif(current_rain == '1'):
    current_rain = '비'
elif(current_rain == '2'):
    current_rain = '비 또는 눈'
elif(current_rain == '3'):
    current_rain = '눈'
elif(current_rain == '4'):
    current_rain = '소나기'
else:
    current_sky = '자료추출오류'

current_probrain = df.iloc[7]['fcstValue'] #강수확률 (%)

current_nowrain = df.iloc[9]['fcstValue'] #현재 강수량
if(current_nowrain == '강수없음'):
    current_nowrain = '0'

current_humid = df.iloc[10]['fcstValue'] #현재 습도

current_snow = df.iloc[11]['fcstValue'] #현재 적설량
if(current_snow == '적설없음'):
    current_snow = '0'



#사용자 출력부--------------------------------------------------


print("--" + mydate + " 오늘의 날씨 (" + mytime + "기준)--")
print("  현재 온도 : " + current_temp + "℃")
print("  현재 풍속 : " + current_wspeed + "m/s")
print("  현재 날씨 : " + current_sky + "," + current_rain)
print("  강수 확률 : " + current_probrain + "%")
print("  강 수 량 : " + current_nowrain + "mm")
print("  현재 습도 : " + current_humid + "%")
print("  적 설 량 : " + current_snow + "mm")
print("-------------------------------")
option = input("1:옷장의 옷 보기, 2:옷 개수 출력, 3:오늘의 옷 추천 \n입력하세요:")
if option == '1':
    closet.myClothes()
elif option == '2':
    closet.countClothes()
elif option == '3':
    mod.isRain(current_rain)
    mod.todayTemp(mod.setStage(current_temp))
else:
    print("입력 오류")
#------------------------------------------------------------

