from Preprocess import Preprocess
from tensorflow.keras import preprocessing



# 말뭉치 데이터 가져오기
sent = ['안녕?','하이루~ㅋㅋ','안녕하세요!!','좋은 아침이에요~','반갑습니다.','싸이버거 1개 배달 해주세요','딥치즈버거 1개 배달이요','인크레더블버거 1개 배달 원합니다','딥치즈버거 3개 시키고 싶어요','싸이버거 2개 배달 ㄱㄱ요']


p = Preprocess(userdic = './user_dic.txt')

for i in sent:
    pos = p.pos(i)
    keywords = p.get_keywords(pos, without_tag=False)
    print(i)
    print(keywords)

# w2i = p.get_wordidx_sequence(keywords)
# sequences = [w2i]
#
# MAX_SEQ_LEN = 15    # 임베딩 벡터 크기
# padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')
#
# print(keywords)
# print(sequences)
# print(padded_seqs)
