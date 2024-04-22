import random

target_score = int(input("목표 점수: "))
a_score = 0
b_score = 0
turn = 0

while True:
    if turn % 2 == 0:  
        current_score = 0
        print("A의 차례:")
        while True:
            dice = random.randint(1, 6)
            if dice == 1:
                print("1! 종료")
                current_score = 0
                break
            else:
                current_score += dice
                print(f"획득 점수: {dice}, 현재 차례 점수: {current_score}")
                if a_score + current_score >= target_score:
                    a_score += current_score
                    print(f"A가{a_score}로 게임 승리!")
                    exit(0)
                
                go = input("계속? (y/n): ")
                if go.lower() != 'y':
                    a_score += current_score
                    break
    else:  # B
        current_score = 0
        print("B의 차례:")
        while True:
            dice = random.randint(1, 6)
            if dice == 1:
                print("1! 종료")
                current_score = 0
                break
            else:
                current_score += dice
                print(f"획득 점수: {dice}, 현재 차례 점수: {current_score}")
                if b_score + current_score >= target_score:
                    b_score += current_score
                    print(f"B가 {b_score}로 게임승리!")
                    exit(0)

                go = input("계속? (y/n): ")
                if go.lower() != 'y':
                    b_score += current_score
                    break
    turn += 1

