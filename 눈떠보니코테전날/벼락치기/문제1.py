# replace() 대체어
# lstrip() 앞의 공백 없애줌 
# rstrip() 뒤의 공백 없애줌
# strip() 앞뒤 공백 없애줌 
# ord() 문자 -> 숫자
# chr() 숫자 -> 문자
# (''.join(배열)) => 배열에 있는 것들 문자열로 출력해줌

text = [
    ' +--+-+- ',
    ' +---+-+ ',
    ' +--+-+-' ,
    ' +-+-+-+ '
]
list = []
for i in text:
    list.append(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)))

print(''.join(list))

# print(''.join(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)) for i in text))