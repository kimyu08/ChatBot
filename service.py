def service (intent, menu,  menuNum):
    if intent == 0:
        print("안녕하세요 맘스터치입니다~")
    elif intent ==1:
        print("주문해주셔서 감사합니다.")
        print("주문 메뉴: ",",".join(menu))
        print("메뉴 수량: ",",".join(menuNum))
        print("포장 소요시간: 15분")
        print("늦지않게 와주세요~")
    elif intent ==2:
        location = input("배달지역을 입력해주세요: ")
        print("주문해주셔서 감사합니다!!!")
        print("고객님이 주문하신 음식이 약50분 내에 도착할 예정입니다.")
        print("주문 메뉴: ",",".join(menu))
        print("메뉴 수량: ",",".join(menuNum))
        print("배달 주소: ",location)
        print("배달 소요시간: 50분")
