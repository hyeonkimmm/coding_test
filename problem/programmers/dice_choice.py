# https://school.programmers.co.kr/learn/courses/30/lessons/258709
from itertools import combinations, product


def calculate_win_prob(dice_comb_a, dice_comb_b):
    win_count = 0
    for a_result in product(*dice_comb_a):
        for b_result in product(*dice_comb_b):
            if sum(a_result) > sum(b_result):
                win_count += 1
    return win_count


def solution(dice):
    n = len(dice)
    max_win_prob = 0
    best_comb = []

    # 모든 가능한 조합에 대해 반복
    for comb in combinations(range(n), n // 2):
        # A의 주사위 조합
        dice_comb_a = [dice[i] for i in comb]
        # B의 주사위 조합 (남은 주사위)
        dice_comb_b = [dice[i] for i in range(n) if i not in comb]

        # 승리 확률 계산
        win_prob = calculate_win_prob(dice_comb_a, dice_comb_b)

        # 최대 승리 확률 업데이트
        if win_prob > max_win_prob:
            max_win_prob = win_prob
            best_comb = comb

    return sorted([x + 1 for x in best_comb])

input_dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]

print(solution(input_dice))