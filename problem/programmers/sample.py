from collections import deque


def solution(cap, n, deliveries, pickups):
    answer = 0
    max_idx = n - 1
    home_deque = [i for i in range(max_idx, -1, -1)]
    while home_deque:
        # 남아있는 배달 및 픽업 용량 초기화
        deliver_cap = cap
        pickup_cap = cap

        copy_home_deque = deque(home_deque)
        # 배달 및 픽업이 필요한 가장 먼 지점을 찾기
        for idx in home_deque:
            if deliveries[idx] == 0 and pickups[idx] == 0:
                copy_home_deque.popleft()
            else:
                break
        else:
            break  # 더 이상 배달 및 픽업이 필요하지 않음

        home_deque = deque(copy_home_deque)
        # 왕복 거리 추가 (가장 먼 지점의 왕복)
        answer += (home_deque[0] + 1) * 2

        for idx in home_deque:
            if deliveries[idx] >= 0 and deliver_cap > 0:
                deliver_amount = min(deliver_cap, deliveries[idx])
                deliveries[idx] -= deliver_amount
                deliver_cap -= deliver_amount

            if pickups[idx] >= 0 and pickup_cap > 0:
                pickup_amount = min(pickup_cap, pickups[idx])
                pickups[idx] -= pickup_amount
                pickup_cap -= pickup_amount

            if deliveries[idx] == 0 and pickups[idx] == 0:
                copy_home_deque.popleft()

            if deliver_cap == 0 and pickup_cap == 0:
                home_deque = deque(copy_home_deque)
                break

    return answer

