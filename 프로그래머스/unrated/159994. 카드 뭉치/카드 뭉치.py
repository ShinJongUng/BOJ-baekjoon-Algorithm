from collections import deque
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    idx1, idx2 = 0, 0
    while goal:
        n = goal.pop()
        if cards1:
            if cards1[-1] == n:
                cards1.pop()
                idx1 += 1
                continue
        if cards2:
            if cards2[-1] == n:
                cards2.pop()
                idx2 += 1
                continue
        if n in cards1 and not idx1:
            cards1.pop()
            goal.append(n)
            continue
        if n in cards2 and not idx2:
            cards2.pop()
            goal.append(n)
            continue
        return "No"
    return "Yes"
            