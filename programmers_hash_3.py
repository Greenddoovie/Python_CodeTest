def solution(clothes) :
    answer = 1
    cloth = {}
    for i in range(0, len(clothes)) :
        category = clothes[i][1]
        if (category in cloth) is True :
            cloth[category] = cloth[category] + 1
        else :
            cloth[category] = 1
    for value in cloth.values() :
        answer *= (value + 1)
    answer -= 1
    return answer

clothes = (['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear'])
print(solution(clothes))