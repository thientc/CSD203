def findmax(S):
    if len(S) == 0:
        raise Exception("List is empty!");
    if len(S) == 1:
        return S[0]
    return max(S[0], findmax(S[1:]))

print(findmax([3,6,2,7,12, 10,1]))