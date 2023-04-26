def solution(a, b):
    
    for i in range(min(a, b), 0, -1):
        if a%i == b%i ==0:
            a, b = a//i, b//i
            break
    while True:
        if b == 1:
            return 1
        elif b % 2 == 0:
            b = b//2
        elif b%5 ==0:
            b = b//5
            
        else:
            return 2
    