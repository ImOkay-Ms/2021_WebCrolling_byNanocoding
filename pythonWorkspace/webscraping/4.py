import re 
#정규식 관련 라이브러리
# abcd, book, desk
# ca?e
# care, case ,cafe ,cake 등등 으로 추정가능
# 어떻게 추정가능??

p = re.compile("ca.e")
# . (ca.e) 하나의 문자를 의미 > care, cafe, case
# ^ (^de) 문자열의 시작 > desk, destination
# $ (se$) 문자열의 끝 > case, base | face(X)

def print_match(m):
    if m :
        print("m.group() : ",m.group())
        # print("m.string() : ",m.string())
        # print("m.start() : ",m.start())
        # print("m.end() : ",m.end())
        # print("m.span() : ",m.span())
    else :
        print("매칭되지 않음")

# m = p.match("good care")     #match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") #seach : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

m = p.findall("care cake fine cles") #일치하는 모든 것들을 리스트 형태로 반환
print(m)
