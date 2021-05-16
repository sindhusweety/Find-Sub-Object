"""
shortest sub path destination
"""
def recursive(N, A, unique_n, unique):
    if unique_n == N:
        return unique_n
    ck_visited = []
    for i in range(N - unique_n + 1):
        sub_location = A[i:i + unique_n]
        visited = {k: False for k in unique}
        for _l in unique:
            if _l in sub_location:
                visited[_l] = True

        not_visited = [visited[k] for k in visited]
        if False not in not_visited:
            ck_visited = not_visited
    if False not in ck_visited and len(ck_visited):
        return unique_n
    return recursive(N, A, unique_n+1, unique)


def solution(A):
    unique = []
    for i in A:
        if i not in unique:
            unique.append(i)
    unique_n = len(unique)
    return  recursive(len(A), A, unique_n, unique)

print(solution([2, 1, 1, 3, 1]))
