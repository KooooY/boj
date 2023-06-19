def solution(n, computers):
    answer = 0
    visited = set()
    
    for i in range(n):
        if i not in visited:
            Q = [i]
            visited.add(i)
            answer += 1
            while Q:
                cur = Q.pop()
                for j in range(n):
                    if j != cur and j not in visited and computers[cur][j]:
                        Q.append(j)
                        visited.add(j)
            
    return answer