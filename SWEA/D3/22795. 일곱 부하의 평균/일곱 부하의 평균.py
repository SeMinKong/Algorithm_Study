T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    heights = list(map(int, input().split()))
    current_sum = sum(heights)
    max_height = max(heights)

    candidate = max_height + 1
    
    while True:
        if (current_sum + candidate) % 7 == 0:
            print(candidate)
            break

        candidate += 1