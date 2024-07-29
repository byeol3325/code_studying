def solution(users: list, emoticons: list) -> list:
    # 멤버십 최우선
    # n명 카카오톡 사용자들. 이모티콘 m개 할인 판매
    # 이모티콘 할인율 10%, 20%, 30%, 40%
    # 사람 - [비율, 가격]
    # 
    
    # 할인율 젤 높게 하면서 사람 수 젤 많이
    # 가격 낮은 애를 높이면서 확인
    n, m = len(users), len(emoticons) 
    answer = [0, 0] # num, prices
    
    # 4^7 = 2^14 = 10^3 * 16 = 16000가지
    # 1번 계산 = 100 * 7 * 16000 = 100 * 100 * 1000 = 천만
    
    sales = [10] * m
    def get_answer():
        nonlocal n,m, users, emoticons, sales, answer
        service_num, total_price = 0, 0
        for i in range(n):
            price = 0
            for j in range(m):
                if users[i][0] <= sales[j]:
                    price += emoticons[j] * (100 - sales[j])/100
            
            if price >= users[i][1]:
                service_num += 1
            else:
                total_price += price
        
        if service_num > answer[0]:
            answer = [service_num, total_price]
        elif service_num == answer[0]:
            answer[1] = max(total_price, answer[1])
        return None

    get_answer()
    done = set()
    done.add(tuple(sales))
    
    def backtrack():
        nonlocal users, emoticons, sales
        get_answer()
        for i in range(m):
            for _ in range(3):
                if sales[i] < 40:
                    sales[i] += 10
                    if tuple(sales) not in done:
                        backtrack()
                        done.add(tuple(sales))
                    sales[i] -= 10            
    
    backtrack()
    return answer