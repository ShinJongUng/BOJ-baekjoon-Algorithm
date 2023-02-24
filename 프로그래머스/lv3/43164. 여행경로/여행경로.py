from collections import defaultdict
def solution(tickets):
    ticket_dict = defaultdict(list)
    ans_len = 1 + len(tickets)
    for u, v in tickets:
        if u not in ticket_dict:
            ticket_dict[u] = [v]
        else:
            ticket_dict[u].append(v)
    
    for i in ticket_dict.keys():
        ticket_dict[i].sort()

    answer = []
    def DFS(s):
        while ticket_dict[s]:
            DFS(ticket_dict[s].pop(0))
        if not ticket_dict[s]:
            answer.append(s)
            return
    DFS('ICN')
    return list(reversed(answer))
                    