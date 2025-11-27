T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
color_map = {
        "red": 0,
        "orange": 1,
        "yellow": 2,
        "green": 3,
        "blue": 4,
        "purple": 5
    }

for test_case in range(1, T + 1):
        line = input().strip()
        if not line: break
        
        s, t = line.split()
        
        idx1 = color_map[s]
        idx2 = color_map[t]
        
        diff = abs(idx1 - idx2)
        
        result = ''
        
        if diff == 0:
            result = 'E'
        elif diff == 1 or diff == 5:
            result = 'A'
        elif diff == 3:
            result = 'C'
        else:
            result = 'X'
            
        print(result)