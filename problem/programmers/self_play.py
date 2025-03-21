from collections import defaultdict, deque


def solution(cards):
    card_dict = defaultdict(int)
    seen = set()
    queue = deque()
    for i in range(len(cards)):
        if i not in seen:
            seen.add(i)
            queue.append([i, 1])
        while queue:
            box_num, group_count = queue.popleft()
            if cards[box_num] - 1 not in seen:
                seen.add(cards[box_num] - 1)
                queue.append([cards[box_num] - 1, group_count + 1])
            else:
                card_dict[i] = group_count

    return sorted(card_dict.values(), reverse=True)[0] * sorted(card_dict.values(), reverse=True)[1]
