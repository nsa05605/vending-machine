select = 999
a = 0
b = 0
c = 0
A = 0
B = 0
C = 0

while True:
    print("현재 음료 재고 :", "사이다 "+str(10 - a)+"개", "환타 "+str(10 - b)+"개", "파워에이드 "+str(10 - c)+"개")
    print("1. 사  이  다")
    print("2. 환      타")
    print("3. 파워에이드")
    print("0. 종료")
    select = int(input("메뉴 선택 : "))
    if select == 1:
        if a < 9:
            print("선택하신 메뉴는 사이다입니다.\n\n")
            a = a + 1
        elif a == 9:
            print("선택하신 메뉴는 사이다입니다.\n")
            print("이제 사이다가 품절되었습니다.\n\n")
            a = a + 1
        elif a == 10:
            print("사이다는 더 이상 고를 수 없습니다.\n\n")
            a = a            
    elif select == 2:
        if b < 9:
            print("선택하신 메뉴는 환타입니다.\n\n")
            b = b + 1
        elif b == 9:
            print("선택하신 메뉴는 환타입니다.\n")
            print("이제 환타가 품절되었습니다.\n\n")
            b = b + 1
        elif b == 10:
            print("환타는 더 이상 고를 수 없습니다.\n\n")
            b = b  
    elif select == 3:
        if c < 9:
            print("선택하신 메뉴는 파워에이드입니다.\n\n")
            c = c + 1
        elif c == 9:
            print("선택하신 메뉴는 파워에이드입니다.\n")
            print("이제 파워에이드가 품절되었습니다.\n\n")
            c = c + 1
        elif c == 10:
            print("파워에이드는 더 이상 고를 수 없습니다.\n\n")
            c = c
    elif select < 0 or select > 3:
        print("잘못 선택하였습니다. 다시 선택하여 주십시오.\n\n")
    elif select == 0:
        print("선택이 종료되었습니다. \n")
        print("선택한 사이다의 개수 :", a - A)
        print("선택한 환  타의 개수 :", b - B)
        print("선택한 파워에이드의의 개수 :", c - C, "\n")

        answer = int(input("선택하신 메뉴가 맞습니까? 맞으면 1, 틀리면 2를 눌러주세요 : "))
        if answer == 1:
            m = ((a - A) * 500 + (b - B) * 700 + (c - C) * 1000)
            print(" ")
            print("총 주문 금액 :", m)
        elif answer == 2:
            a = 0
            b = 0
            c = 0
            continue
        elif answer > 2 or answer < 1:
            print("잘못 눌렀습니다. 다시 눌러주세요.")
            answer2 = int(input("선택하신 메뉴가 맞습니까? 맞으면 1, 틀리면 2를 눌러주세요 : "))
            if answer2 == 1:
                m = ((a - A) * 500 + (b - B) * 700 + (c - C) * 1000)
                print(" ")
                print("총 주문 금액 :", m)
            elif answer2 == 2:
                a = 0
                b = 0
                c = 0
                continue
            elif answer > 2 or answer < 1: 
                print("두 번 잘못 입력하였습니다. 처음으로 돌아갑니다.")
                a = 0
                b = 0
                c = 0
                continue
        pay = int(input("결제 방식을 선택해주세요 현금은 1, 카드는 2를 눌러주세요 : "))
        if pay == 2:
            print("카드을 넣어주세요.")
        elif pay > 2 or pay < 1:
                print("잘못 눌렀습니다. 다시 눌러주세요.")
        elif pay == 1:
                mon = int(input("돈을 넣어주세요 "))
                print("%d원을 넣으셨습니다." % mon)
                change = mon - m
                if change >= 0:
                    print("거스름돈 %d원을 받으세요." % change)
                else:
                    mon2 = int(input("투입하신 금액이 부족합니다. 돈을 더 넣어주세요 : "))
                    change2 = mon - m
                    while change2 < 0:
                        change2 = change2 + mon2
                        if change2 < 0:
                            mon2 = int(input("투입하신 금액이 부족합니다. 돈을 더 넣어주세요. "))
                            continue
                        else:
                            print("거스름돈 %d원을 받으세요." % change2)
                            break
                        
        reciept = int(input("영수증을 드릴까요? 받으면 1, 아니면 2를 눌러주세요 : "))
        if reciept == 1:
            print(" ")
            print("영수증이 출력됩니다. \n")
        elif reciept > 2 or reciept < 1:
            print("잘못 눌렀습니다. 다시 눌러주세요.")
        elif reciept == 2:
            print(" ")
        print("주문하신 음료가 나옵니다. \n")
        print("각 음료의 남은 개수")
        if a == 10:
            print("사  이  다 : ", "품절")
        else:
            print("사  이  다 : ", 10 - a)
        if b == 10:
            print("환      타 : ", "품절")
        else:
            print("환      타 : ", 10 - b)
        if c == 10:
            print("파워에이드 : ", "품절")
        else:
            print("파워에이드 : ", 10 - c, "\n")
        re_order = int(input("다시 주문하시겠습니까? 다시 주문하면 1, 주문 종료하면 2를 눌러주세요 : "))
        if re_order == 1:
            print("처음으로 돌아갑니다\n")
            A = a
            B = b
            C = c
            continue
        if re_order == 2:
            print("이용해주셔서 감사합니다.")
            break
        if re_order > 2 or re_order < 1:
            print("잘못 입력하셨습니다. 이용해주셔서 감사합니다.")
            break
