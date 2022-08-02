s = 'aabbaccc'

'''
aabbaccc -> 1개단위 압축 2a2ba3c =>7
ababcdcdababcdcd -> 8개단위 압축 2ababcdcd => 9 
'''

answer = len(s) # 8

#1개 단위(step) 부터 압축 단위를 늘려가며 확인
# 1부터 n/2까지의 모든 수를 단위로 하여 문자열을 압축하는 방법을 모두 확인, 가장 짧게 압축되는 길이를 출력
for step in range(1, len(s) // 2 + 1):
    compressed = ""
    prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
    count = 1
    # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
    for j in range(step, len(s), step):
        # 이전 상태와 동일하다면 압축 횟수(count) 증가
        compare = s[j:j + step]
        if prev == compare:
            count += 1
        # 다른 문자열이 나왔다면 (더 이상 압축하지 못하는 경우라면)
        else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = s[j:j +step] # 다시 상태 초기화
            count = 1
    # 남아있는 문자열에 대해서 처리
    compressed += str(count) + prev if count >= 2 else prev
    #만들어지는 압축 문자열이 가장 짧은 것이 정답
    answer = min(answer, len(compressed))

print(answer)
'''
구현: 반복문 돌려서 하나하나 비교하기~~~~~!
'''