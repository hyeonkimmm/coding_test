from collections import deque


def solution(board):
    seen = set()
    len_x = len(board[0])
    len_y = len(board)

    start = None
    for j in range(len_y):
        for i in range(len_x):
            if board[j][i] == "R":
                start = (i, j, 0)
                break
        if start:
            break

    q = deque([start])
    seen.add((start[0], start[1]))

    def is_stop(nx, ny):
        if nx < 0 or nx >= len_x or ny < 0 or ny >= len_y or board[ny][nx] == "D":
            return True
        return False

    while q:
        x, y, cnt = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x
            ny = y
            while True:
                nx += dx
                ny += dy
                if is_stop(nx, ny):
                    nx -= dx
                    ny -= dy
                    break
            if board[ny][nx] == "G":
                return cnt + 1
            if (nx, ny) not in seen:
                seen.add((nx, ny))
                q.append([nx, ny, cnt + 1])

    return -1


if __name__ == "__main__":
    input_board = [".D.R", "....", ".G..", "...D"]
    print(solution(input_board))
