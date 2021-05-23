from hangul_utils import split_syllables, join_jamos
from konlpy.tag import Mecab
import re
# 레벤슈타인 거리 구하기
keyStroke = {'ㄱ':'r', 'ㄴ':'s', 'ㄷ':'e', 'ㄹ':'f', 'ㅁ':'a', 'ㅂ':'q', 'ㅅ':'t', 'ㅇ':'d', 'ㅈ':'w', 
'ㅊ':'c', 'ㅋ':'z','ㅌ':'x','ㅍ':'v', 'ㅎ':'g','ㄲ':'R','ㄸ':'E','ㅆ':'T','ㅃ':'Q','ㅉ':'W',
'ㅏ':'k', 'ㅑ':'i', 'ㅓ':'j', 'ㅕ':'u', 'ㅗ':'h', 'ㅛ':'y', 'ㅜ':'n', 'ㅠ':'b', 'ㅡ':'m', 'ㅣ':'l', 
'ㅐ':'o', 'ㅔ':'p', 'ㅒ':'O', 'ㅖ':'P', 'ㅘ':'hk', 'ㅢ':'ml', 'ㅙ':'ho', 'ㅞ':'np', 'ㅚ':'hl', 'ㅝ':'nj', 'ㅟ':'nl'}
m = Mecab(dicpath='C:/mecab/mecab-ko-dic')
menu_list = ['싸이버거','딥치즈버거','통새우버거','화이트갈릭버거','인크레더블버거', '에그불고기버거']
keyStroke_menu_list = ['Tkdlqjrj', 'elqclwmqjrj', 'xhdtodnqjrj', 'ghkdlxmrkfflrqjrj', 'dlszmfpejqmfqjrj', 'dprmqnfrhrlqjrj']    

def get_key(val):
    for key, value in keyStroke.items():
        if val == value:
            return key

def calc_distance(a, b):
    if a == b: return 0 # 같으면 0을 반환
    a_len = len(a) # a 길이
    b_len = len(b) # b 길이
    if a == "": return b_len
    if b == "": return a_len
    # 2차원 표 (a_len+1, b_len+1) 준비하기 --- (※1)
    matrix = [[] for i in range(a_len+1)]
    for i in range(a_len+1): # 0으로 초기화
        matrix[i] = [0 for j in range(b_len+1)]
    # 0일 때 초깃값을 설정
    for i in range(a_len+1):
        matrix[i][0] = i
    for j in range(b_len+1):
        matrix[0][j] = j
    # 표 채우기 --- (※2)
    for i in range(1, a_len+1):
        ac = a[i-1]
        for j in range(1, b_len+1):
            bc = b[j-1]
            cost = 0 if (ac == bc) else 1
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # 문자 삽입
                matrix[i][j-1] + 1,     # 문자 제거
                matrix[i-1][j-1] + cost # 문자 변경
            ])
    return matrix[a_len][b_len]

def typo_correction(sentence):
    correction_text = ""
    Stroke_text = ""
    Stroke_text_list = []
    distance = []
    # !.,? 등의 필요없는 문자 제거
    if "." in sentence:
        r_text = sentence.replace(".", " ")
        text = re.sub('[^0-9ㄱ-ㅎㅏ-ㅣ가-힣\s]', '', r_text)
        split_text = text.split()
    else:
        text = re.sub('[^0-9ㄱ-ㅎㅏ-ㅣ가-힣\s]', '', sentence)
        split_text = text.split()
    # 자모 분리후 힌글자씩 영어로 바꾸는 과정
    for word in split_text:
        for i in split_syllables(word):
            if i in keyStroke:
                Stroke_text += keyStroke[i]
            else:
                Stroke_text += i
        Stroke_text_list.append(Stroke_text)
        Stroke_text = ""
    # 편집거리 구하기
    for menu in range(0,len(keyStroke_menu_list)):
        for word in range(0,len(Stroke_text_list)):
            distance.append(calc_distance(Stroke_text_list[word], keyStroke_menu_list[menu]))
        for word in range(0,len(Stroke_text_list)):
            dis_value = calc_distance(Stroke_text_list[word], keyStroke_menu_list[menu])
            if dis_value == min(distance) and dis_value <= 5:
                Stroke_text_list[word] = keyStroke_menu_list[menu]
        distance = []
    # 영어를 한글로 변환후 자모 합치기
    for word in Stroke_text_list:
        for w_piece in word:
            if get_key(w_piece) == None:
                Stroke_text += w_piece
            else:
                Stroke_text += get_key(w_piece)
        Stroke_text += " "
    correction_text = join_jamos(Stroke_text)

    return correction_text

