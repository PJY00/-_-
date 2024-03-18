# -*- coding: euc-kr -*-
import random
import time

# 사용자가 시간 내에 입력을 완료했는지 확인하는 함수
def is_input_valid(seconds):
    start = time.time()
    user_input = input()
    end = time.time()
    elapsed_time = end - start

    if elapsed_time <= seconds:
        return user_input
    else:
        print("시간 초과! 입력 시간이 {}초를 초과했습니다.".format(seconds))
        return None

# 컴퓨터가 선택한 가위바위보 문자열을 반환하는 함수
def get_computer_choice():
    choice = random.choice(["가위", "바위", "보"])
    return choice

# 가위바위보 게임 진행 함수
def play_game():
    while True:
        # 가위바위보
        print("청개구리 가위바위보 게임을 시작합니다!")
        print("가위, 바위, 보를 입력해주세요: ")

        user_choice = input().strip().lower()
        
        # 유효한 입력인지 확인
        if user_choice not in ['가위', '바위', '보']:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            continue
        
        computer_choice = get_computer_choice()
        
        print("상대는 [{}]을 냈습니다 :".format(computer_choice[0:2]))  # 상대의 선택 표시

        # 가위바위보 결과 입력 시간 제한 설정
        player_result = is_input_valid(3)

        if player_result is None:
            # 사용자 입력 시간 초과
            print("시간 초과로 게임에서 패배했습니다.")
            return

        # 결과 확인
        if (user_choice == "가위" and computer_choice == "보" and player_result == "졌다") or \
           (user_choice == "바위" and computer_choice == "가위" and player_result == "졌다") or \
           (user_choice == "보" and computer_choice == "바위" and player_result == "졌다"):
            print("게임에서 승리하셨습니다!")
        elif (user_choice == "가위" and computer_choice == "바위" and player_result == "이겼다") or \
             (user_choice == "바위" and computer_choice == "보" and player_result == "이겼다") or \
             (user_choice == "보" and computer_choice == "가위" and player_result == "이겼다"):
            print("게임에서 승리하셨습니다!")
        elif (user_choice == "가위" and computer_choice == "가위" and player_result == "개굴") or \
             (user_choice == "바위" and computer_choice == "바위" and player_result == "개굴") or \
             (user_choice == "보" and computer_choice == "보" and player_result == "개굴"):
            print("게임에서 승리하셨습니다!")
        else:
            print("게임에서 패배하셨습니다!")
        
        break

# 게임 실행
while True:
    play_game()

    # 게임을 계속할지 묻기
    play_again = input("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요: ").strip()
    if play_again != '1':
        break

print("게임 종료!")