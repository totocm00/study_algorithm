# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다.
# 예를 들어, "banana"의
# 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string이 매개변수로 주어질 때,
# my_string의 모든 접미사를
# 사전순으로 정렬한
# 문자열 배열을 return 하는 solution 함수
#
# my_string	        result
# "banana"          ["a", "ana", "anana", "banana", "na", "nana"]
# "programmers"     ["ammers", "ers", "grammers", "mers", "mmers",
#                   "ogrammers", "programmers", "rammers", "rogrammers", "rs", "s"]
def solution(my_string):
    # 1. 접미사 만들기
    suffixes = [my_string[i:] for i in range(len(my_string))]
    
    # 2. 사전순 정렬
    suffixes.sort()
    
    return suffixes