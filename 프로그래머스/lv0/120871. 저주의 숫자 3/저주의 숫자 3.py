def solution(n):
    result = 0
    while n:
        while True:
            result += 1
            if result % 3 ==0 or '3' in str(result):
                pass
            else:
                break
        n -= 1
    return result