from hangul_utils import split_syllables, join_jamos
import re

menu_list = ['싸이버거','딥치즈버거','통새우버거','화이트갈릭버거','인크레더블버거', '에그불고기버거']
split_menu_list = [split_syllables(menu) for menu in menu_list]
def calc_distance(a, b):
    ''' 레벤슈타인 거리 계산하기 '''
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

def typo_correction(text):
    split_word = []
    distance = []
    correction_text = ""
    if "." in text:
        r_text = text.replace(".", " ")
        text = re.sub('[^0-9ㄱ-ㅎㅏ-ㅣ가-힣\s]', '', r_text)
        split_text = text.split()
    else:
        text = re.sub('[^0-9ㄱ-ㅎㅏ-ㅣ가-힣\s]', '', text)
        split_text = text.split()

    for word in split_text:
        split_word.append(split_syllables(word))
    for word in range(0,len(split_text)):
        for menu in range(0,len(split_menu_list)):
            dis_value = calc_distance(split_word[word], split_menu_list[menu])
            distance.append(dis_value)
        for menu in range(0,len(split_menu_list)):
            dis_value = calc_distance(split_word[word], split_menu_list[menu])
            if min(distance) == dis_value and dis_value <= 4:
                split_word[word] = split_menu_list[menu]
        distance = []
    for word in split_word:
        join = join_jamos(word)
        correction_text += join
        correction_text += " "
    return correction_text
