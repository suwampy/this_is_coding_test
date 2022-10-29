# 국, 영, 수 점수
# 1. 국어 점수가 감소하는 순서
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서
# 4. 모든 점수가 같으면 일므이 사전 순으로 증가하는 순서
n = int(input())
students = [] #학생 정보를 담을 리스트
for i in range(n):
    students.append(input().split())


students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(students[0])
