matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]

# 아래애 코드를 작성하시오.
matrix_len = 0
for each in matrix:
    matrix_len += 1

print(matrix_len)



for number in matrix:
    temporary_len = 0
    for each in number:
        temporary_len += 1
    if temporary_len <= 4:
        print(f'{number}리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')



for x, each in enumerate(matrix):
    for y in range(0,len(each)):
        print(f'matrix의 {x},{y} 번째 요소의 값은 {each[y]} 입니다. ')
