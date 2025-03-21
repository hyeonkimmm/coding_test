from collections import defaultdict


def solution(topping):
    brother = set(topping)
    brother_topping_dict = defaultdict(int)
    me = set()
    answer = 0
    for topping_item in topping:
        brother_topping_dict[topping_item] += 1

    for topping_item in topping:
        brother_topping_dict[topping_item] -= 1
        if brother_topping_dict[topping_item] == 0:
            brother.remove(topping_item)

        me.add(topping_item)
        if len(me) == len(brother):
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
