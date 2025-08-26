# 어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다.
# 예를 들어, "banana"의 모든 접두사는
# "b", "ba", "ban", "bana", "banan", "banana"입니다.
# 문자열 my_string과 is_prefix가 주어질 때,
# is_prefix가 my_string의 접두사라면 1을,
# 아니면 0을 return 하는 solution 함수
#
# my_string	is_prefix	     result 
# "banana"	"ban"	         1
# "banana"	"nan"	         0
# "banana"	"abcd"	       0
# "banana"	"bananan"	     0

def solution(my_string, is_prefix):
	  return 1 if my_string.startswith(is_prefix) else 0