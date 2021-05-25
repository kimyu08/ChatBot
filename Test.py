from Preprocess import Preprocess
from IntentModel import IntentModel
import tensorflow as tf
import pandas as pd
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing
from LevenshteinDistance1 import *
from service import *
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

menulist = ["싸이버거","딥치즈버거","통새우버거","화이트갈릭버거","인크레더블버거"]

p = Preprocess(word2index_dic='./chatbot_dict.bin',
               userdic='./user_dic.txt')

intent = IntentModel(model_name='./intent_model.h5', proprocess=p)
##query = ['싸이버거 1개 배달해주세요','하이루','딥치즈버거 1개 포장하러 갈게요']

menu = []
menuNum = []
query = input("안녕하세요 맘스터입니다~ 무엇을 도와드릴까요?? : ")
# 오타변환.
Equery = typo_correction(query)
predict = intent.predict_class(Equery)
predict_label = intent.labels[predict]
pos = p.pos(Equery)
for i in pos:
    if i[0] in menulist:
        menu.append(i[0])
    if i[1] == "SN":
        menuNum.append(i[0])
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)
print("----------------------------------------------")
service(predict,menu,menuNum)


# for i in query:
# # space_query = split_space(query)
# # edit = Edit_distance(space_query,menulist)
# # change_query = change_string(query, edit)

#     predict = intent.predict_class(i)
#     predict_label = intent.labels[predict]
#     pos = p.pos(i)
#     print(i)
#     print(pos)
#     # print(change_query)
#     print("의도 예측 클래스 : ", predict)
#     print("의도 예측 레이블 : ", predict_label)
#     print()

    

## 정해야할점.
## 메뉴에 대한 오타처리를 어떻게 할건지? > 쓰이버거 1개 딉추지버거 2개 배달해주세요
## 입력값 어떻게 받을지. > 띄어쓰기를 명확하게 받을 것인지.
## 입력값에서 수량 체크 어떻게 할건지. > 싸이버거랑 딥치즈버거 1개씩 주세요.?(이런거 안됨.)
## 입력에서 무조건 메뉴에 수량이 연속적으로 등장 가정. > 싸이버거 1개 딥치즈버거 1개 보내주세요.(전처리에서 햄버거(고유명사) 다음 수사를 수량으로 취급 )
## 예측값.. 보여주기.. 어떻게? p.176
## 답변출력 어떻게 해줄 것인지.  
##의도 0.인사
##     안녕하세요~? 맘스터치입니다.
##1,2 인경우 
## 메뉴명: ~ 수량: ~ 배달(포장)소요시간:50(15)
##                                                                  

## 입력값: 띄어쓰기 필수, 메뉴에대한 오타만 허용, 메뉴에 대한 수량은 무조건 연속적으로 등장
## 

##   1. 메뉴 오타 수정.
##   2. 전처리.
##   3. 의도분석.
##   4. 의도에 맞는 답변 출력.