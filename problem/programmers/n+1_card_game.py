# https://school.programmers.co.kr/learn/courses/30/lessons/258707?language=python3
from collections import deque


def solution(coin, cards):
    n = len(cards)
    initial = set(cards[:n//3])
    remain = deque(cards[n//3:])
    possible = set()
    game_round = 1

    def remove_pair(source: set, target: set):
        for card in list(source):
            if n+1-card in target:
                source.remove(card)
                target.remove(n+1-card)
                return True
        return False

    def add_possible():
        if remain:
            possible.add(remain.popleft())
            possible.add(remain.popleft())

    while remain:
        add_possible()
        if remove_pair(initial, initial):
            game_round += 1
        elif coin >= 1 and remove_pair(initial, possible):
            coin -= 1
            game_round += 1
        elif coin >= 2 and remove_pair(possible, possible):
            coin -= 2
            game_round += 1
        else:
            break

    return game_round


if __name__ == "__main__":
    print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))  # Expected output: 5
    print(solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]))  # Expected output: 2
    print(solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]))  # Expected output: 4
    print(solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))  # Expected output: 1
