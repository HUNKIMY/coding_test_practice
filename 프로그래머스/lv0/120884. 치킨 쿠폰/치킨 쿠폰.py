def solution(chicken):
    raw_coupon = chicken//10
    coupons_coupon = raw_coupon//10
    answer = 0
    while chicken >= 10:
        answer += chicken//10
        chicken = chicken%10 + chicken//10
    print(raw_coupon, coupons_coupon)
    return answer