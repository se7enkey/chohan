"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random 
import sys

NUMBERS = {1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

purse = 1000
while True:  # 메인 게임 루프
    # 배팅하는 부분:
    print('You have', purse, 'won. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ') ### "100"
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:  # elif = else if
            print('You do not have enough to make that bet.')
        else:
            # 유효한 배팅인 경우
            pot = int(pot)  # 정수로 변환한다.
            break  # 베팅값이 유효하다면 이 루프를 빠져나간다.

    # 주사위 굴리기.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    J: 짝수(even) or H: 홀수(odd)?')

    # 플레이어가 cho 또는 han을 선택하게 한다:
    while True:
        bet = input('> ').upper()
        if bet != 'J' and bet != 'H':
            print('Please enter either "J" or "H".')
            continue
        else:
            break

    # 주사위 결과를 보여 준다:
    print('The dealer lifts the cup to reveal:')
    print('  ', NUMBERS[dice1], '-', NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # 플레이어가 이겼는지 판단한다:
    rollIsEven = (dice1 + dice2) % 2 == 0   ### 1 + 2 = 3 : False(odd), 1 + 3 = 4 : True(even)
    if rollIsEven:
        correctBet = 'J'
    else:
        correctBet = 'H'

    playerWon = bet == correctBet

    # 베팅 결과를 표시한다:
    if playerWon:
        print('You won! You take', pot, 'won.')
        purse += pot  # purse = purse + pot  # 플레이어의 지갑에 베팅액을 더한다.
        print('The house collects a', pot // 10, 'won fee.')
        purse = purse - (pot // 10)  # 수수료는 10퍼센트다.
    else:
        purse -= pot  # purse = purse - pot  # 플레이어의 지갑에서 배팅액을 뺀다.
        print('You lost!')

    # 플레이어의 돈이 부족한지 확인한다:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        print('사용해 주셔서 감사합니다.')
        sys.exit()
