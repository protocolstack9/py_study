from random import *

# # 전체 주석처리 : 여러 라인 선택 후 Ctrl + /
# # Ctrl + s 파일 저장, VSCode 화살표 버튼 실행
# print(5, -10, '풍선', 5 < 10, not (5 < 10))
# print("multiline comment")


# print(randint(1, 45)) # 1 <= x <= 45
# print(randrange(1, 46)) # 1 <= x < 46

# message = "deep dive into ai"
# print(message.count('i'))
# print(message.find('p'))
# print(message.index('e'))
# print(message.replace("deep", "shallow"))

# print("%s %s 스터디 %d 회차" % ("머신러닝", "딥러닝", 5))
# print("{1} {0} 스터디 {2} 회차".format("머신러닝", "딥러닝", 5))
# print("{study0} {study1} 스터디 {count} 회차".format(study0="머신러닝", study1="딥러닝", count="5"))

# # 파이썬 v3.6 이상
# study0 = "머신러닝"
# study1 = "딥러닝"
# count = 5
# print(f"{study0} {study1} 스터디 {count} 회차")

# new_study0 = study0.replace("머신", "메타")
# new_study1 = study1[:study1.index("러닝")]
# print("study {0} and {1}페이크".format(new_study0, new_study1))


# subway = ["강호동", "유재석"]
# subway.insert(1, "조세호")
# print(subway.index("조세호"))

# subway.append("박명수")
# print(subway)

# subway.pop(subway.index("강호동"))
# subway.append("유재석")
# print(subway)


# # 정렬
# num_list = [1, 4, 2, 5, 3]
# num_list.sort()
# print(num_list)

# # 뒤집기
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# # 합치기
# num_list2 = [ 9, 8, 6, 7, 10 ]
# num_list.extend(num_list2)
# print(num_list)


# # Dict
# cabinet = { 3:"유재석", 100:"김태호" }
# # print(cabinet([5])) # fail
# print(cabinet.get(5, "사용가능"))
# print(cabinet.get(3))

# print(5 in cabinet)
# print(3 in cabinet)


with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())