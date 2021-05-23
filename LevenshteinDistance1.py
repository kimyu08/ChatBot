from hangul_utils import split_syllable_char, split_syllables, join_jamos

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
    
def read_file(filename):
    with open(filename, mode = 'r', encoding = 'UTF-8') as f:
        data = []
        for line in f:
            data.append(line.rstrip('/n'))
        return data

def Edit_distance(Word, Menu):
    count = 0
    distance_list = []
    total_distance_list = []
    Word_split = split_syllables(Word)
    for num2 in range(0, len(Menu)):
         Menu_split = split_syllables(Menu[num2])
         distance = calc_distance(Word_split, Menu_split)
         distance_list.append(distance)
    for num2 in range(0, len(Menu)):
         Menu_split = split_syllables(Menu[num2])
         distance = calc_distance(Word_split, Menu_split)
         if distance == min(distance_list):
             Word = Menu[num2]
    distance_list = []
    return Word

def split_space(Word):
    Word1 = Word.split(' ')
    Word = Word1[0]
    return Word

def change_string(Word,Edit):
    chWord = Word.split(' ')
    chWord[0] = Edit
    chString = " ".join(chWord)
    return chString



