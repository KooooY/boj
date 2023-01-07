def solution(routes):
    answer = 1
    routes.sort(key=lambda x:(x[0], x[1]))
    camera = routes[0][1]

    for r_idx in range(1, len(routes)):
        if routes[r_idx][0] > camera:
            answer += 1
            camera = routes[r_idx][1]
        else:
            if routes[r_idx][1] < camera:
                camera = routes[r_idx][1]
                
    return answer