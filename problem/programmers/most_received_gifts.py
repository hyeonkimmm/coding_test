# https://school.programmers.co.kr/learn/courses/30/lessons/258712
from collections import defaultdict
import itertools

gift_score = defaultdict(int)
gift_log = dict()
gift_result = defaultdict(int)


def select_upcoming_gift_receiver(friend_a, friend_b):
    global gift_result
    friend_a_score = gift_score[friend_a]
    friend_b_score = gift_score[friend_b]

    gift_count_a_to_b = gift_log[friend_a][friend_b]
    gift_count_b_to_a = gift_log[friend_b][friend_a]

    if gift_count_a_to_b > gift_count_b_to_a:
        gift_result[friend_a] += 1
    elif gift_count_a_to_b < gift_count_b_to_a:
        gift_result[friend_b] += 1
    else:
        if friend_a_score > friend_b_score:
            gift_result[friend_a] += 1
        elif friend_a_score < friend_b_score:
            gift_result[friend_b] += 1


def solution(friends, gifts):
    global gift_score, gift_log
    for friend in friends:
        gift_log[friend] = defaultdict(int)

    for gift in gifts:
        giver, receiver = gift.split()
        gift_score[giver] += 1
        gift_score[receiver] -= 1
        gift_log[giver][receiver] += 1

    for friend_a, friend_b in itertools.combinations(friends, 2):
        select_upcoming_gift_receiver(friend_a, friend_b)

    if not gift_result:
        return 0

    max_value = max(gift_result.values())
    return max_value


input_friends = ["a", "b", "c"]
input_gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]


print(solution(input_friends, input_gifts))
