# -*- coding: euc-kr -*-
import random
import time

# ����ڰ� �ð� ���� �Է��� �Ϸ��ߴ��� Ȯ���ϴ� �Լ�
def is_input_valid(seconds):
    start = time.time()
    user_input = input()
    end = time.time()
    elapsed_time = end - start

    if elapsed_time <= seconds:
        return user_input
    else:
        print("�ð� �ʰ�! �Է� �ð��� {}�ʸ� �ʰ��߽��ϴ�.".format(seconds))
        return None

# ��ǻ�Ͱ� ������ ���������� ���ڿ��� ��ȯ�ϴ� �Լ�
def get_computer_choice():
    choice = random.choice(["����", "����", "��"])
    return choice

# ���������� ���� ���� �Լ�
def play_game():
    while True:
        # ����������
        print("û������ ���������� ������ �����մϴ�!")
        print("����, ����, ���� �Է����ּ���: ")

        user_choice = input().strip().lower()
        
        # ��ȿ�� �Է����� Ȯ��
        if user_choice not in ['����', '����', '��']:
            print("�߸��� �Է��Դϴ�. �ٽ� �Է����ּ���.")
            continue
        
        computer_choice = get_computer_choice()
        
        print("���� [{}]�� �½��ϴ� :".format(computer_choice[0:2]))  # ����� ���� ǥ��

        # ���������� ��� �Է� �ð� ���� ����
        player_result = is_input_valid(3)

        if player_result is None:
            # ����� �Է� �ð� �ʰ�
            print("�ð� �ʰ��� ���ӿ��� �й��߽��ϴ�.")
            return

        # ��� Ȯ��
        if (user_choice == "����" and computer_choice == "��" and player_result == "����") or \
           (user_choice == "����" and computer_choice == "����" and player_result == "����") or \
           (user_choice == "��" and computer_choice == "����" and player_result == "����"):
            print("���ӿ��� �¸��ϼ̽��ϴ�!")
        elif (user_choice == "����" and computer_choice == "����" and player_result == "�̰��") or \
             (user_choice == "����" and computer_choice == "��" and player_result == "�̰��") or \
             (user_choice == "��" and computer_choice == "����" and player_result == "�̰��"):
            print("���ӿ��� �¸��ϼ̽��ϴ�!")
        elif (user_choice == "����" and computer_choice == "����" and player_result == "����") or \
             (user_choice == "����" and computer_choice == "����" and player_result == "����") or \
             (user_choice == "��" and computer_choice == "��" and player_result == "����"):
            print("���ӿ��� �¸��ϼ̽��ϴ�!")
        else:
            print("���ӿ��� �й��ϼ̽��ϴ�!")
        
        break

# ���� ����
while True:
    play_game()

    # ������ ������� ����
    play_again = input("������ ���� �����Ϸ��� 1, �����Ϸ��� 2�� �Է��ϼ���: ").strip()
    if play_again != '1':
        break

print("���� ����!")