from Preprocess import Preprocess
from IntentModel import IntentModel
import tensorflow as tf
import pandas as pd
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing
from LevenshteinDistance1 import *

menulist = ["싸이버거","딥치즈버거","통새우버거","화이트갈릭버거","인크레더블버거"]

p = Preprocess(word2index_dic='./chatbot_dict.bin',
               userdic='./user_dic.txt')

intent = IntentModel(model_name='./intent_model.h5', proprocess=p)
query = ['싸이버거 1개 배달해주세요','하이루','딥치즈버거 1개 포장하러 갈게요']

for i in query:
# space_query = split_space(query)
# edit = Edit_distance(space_query,menulist)
# change_query = change_string(query, edit)

    predict = intent.predict_class(i)
    predict_label = intent.labels[predict]

    print(i)
    # print(change_query)
    print("의도 예측 클래스 : ", predict)
    print("의도 예측 레이블 : ", predict_label)
    print()

