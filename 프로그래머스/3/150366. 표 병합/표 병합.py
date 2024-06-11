from collections import defaultdict

MERGE_DICT = defaultdict(lambda: None)  # MERGE_NUM: [(r1, c1), (r2, c2) ...]
MERGE_DICT_NUM = defaultdict(lambda: None)  # (r,c): MERGE_NUM
MERGE_NUM = 1

board = [[0] * 51 for i in range(51)]  # 0 means 'blank'

def Rule1(q: list):
    global board, MERGE_DICT, MERGE_DICT_NUM
    r, c, value = int(q[1]), int(q[2]), q[3]

    if MERGE_DICT_NUM[(r, c)] is not None:  # if (r,c) is in merge group
        merge_num = MERGE_DICT_NUM[(r, c)]
        group = MERGE_DICT[merge_num]
        for RC in group:
            board[RC[0]][RC[1]] = value  # change elements of merge group as value
    else:  # if (r,c) is not in merge group
        board[r][c] = value
    return None

def Rule2(q: list):
    global board
    value1, value2 = q[1], q[2]

    for i in range(1, 51):
        for j in range(1, 51):
            if board[i][j] == value1:
                board[i][j] = value2  # change value1 to value2
    return None

def Rule3(q: list):
    """

    Params:
        list q : "MERGE r1 c1 r2 c2"
    """
    global board, MERGE_DICT, MERGE_DICT_NUM, MERGE_NUM
    r1, c1, r2, c2 = int(q[1]), int(q[2]), int(q[3]), int(q[4])

    if r1 == r2 and c1 == c2:  # same cell
        return None
    if MERGE_DICT_NUM[(r1, c1)] and MERGE_DICT_NUM[(r2, c2)] and MERGE_DICT_NUM[(r1, c1)] == MERGE_DICT_NUM[
        (r2, c2)]:  # same merge group
        return None

    # group1(in r1, c1)
    group1 = [(r1, c1)]
    merge_num1 = None
    if MERGE_DICT_NUM[(r1, c1)]:
        merge_num1 = MERGE_DICT_NUM[(r1, c1)]
        group1 = MERGE_DICT[merge_num1]

    # group2(in r2, c2)
    group2 = [(r2, c2)]
    merge_num2 = None
    if MERGE_DICT_NUM[(r2, c2)]:
        merge_num2 = MERGE_DICT_NUM[(r2, c2)]
        group2 = MERGE_DICT[merge_num2]

    if board[r1][c1] != 0: # board[r1][c1] has value
        if merge_num1 == None: # if r1, c1 is no merge group, need to new merge group
            merge_num1 = MERGE_NUM
            MERGE_DICT_NUM[(r1, c1)] = merge_num1
            MERGE_DICT[merge_num1] = [(r1, c1)]
            MERGE_NUM += 1

        for RC in group2:
            MERGE_DICT_NUM[(RC[0], RC[1])] = merge_num1 # change merge_num(merge_num2 -> merge_num1) in group2 elements
            MERGE_DICT[merge_num1].append(RC) # append (r2, c2) group elements in merge group 1
            board[RC[0]][RC[1]] = board[r1][c1] # set (r2, c2) group elements as (r1, c1) value

        if merge_num2 != None: # if r2, c2 is merge group, need to remove merge group of r2, c2
            MERGE_DICT[merge_num2] = None
    else: # board[r1][c1] has no value. (='blank')
        if merge_num2 == None: # if r2, c2 is no merge group, need to new merge group
            merge_num2 = MERGE_NUM
            MERGE_DICT_NUM[(r2, c2)] = merge_num2
            MERGE_DICT[merge_num2] = [(r2, c2)]
            MERGE_NUM += 1

        for RC in group1:
            MERGE_DICT_NUM[(RC[0], RC[1])] = merge_num2  # change merge_num(merge_num2 -> merge_num1) in group2 elements
            MERGE_DICT[merge_num2].append(RC)  # append (r2, c2) group elements in merge group 1
            board[RC[0]][RC[1]] = board[r2][c2]  # set (r2, c2) group elements as (r1, c1) value

        if merge_num1 != None:
            MERGE_DICT[merge_num1] = None
    return None

def Rule4(q: list):
    global board, MERGE_DICT, MERGE_DICT_NUM
    r, c = int(q[1]), int(q[2])

    if MERGE_DICT_NUM[(r, c)] is not None:  # r,c has merge group
        merge_num = MERGE_DICT_NUM[(r, c)]
        group = MERGE_DICT[merge_num]
        for RCs in group:
            if RCs == (r, c):
                pass
            else:
                board[RCs[0]][RCs[1]] = 0
            del MERGE_DICT_NUM[(RCs[0], RCs[1])]
        del MERGE_DICT[merge_num]
    else:  # r,c has no merge group
        pass

    return None

def Rule5(q: list, answer: list) -> list:
    global board
    r, c = int(q[1]), int(q[2])

    if board[r][c] == 0:  # blank
        answer.append("EMPTY")
    else:  # no blank
        answer.append(board[r][c])
    return answer

def show_board():
    global board
    print("============ NOW BOARD ============")
    for i in range(1, 6):
        print(board[i][1:6])
    return None

def show_status(merge_dict = True, merge_dict_num = True):
    global MERGE_DICT, MERGE_DICT_NUM
    if merge_dict == True:
        print("SHOW MERGE_DICT : ", MERGE_DICT)
    if merge_dict_num == True:
        print("SHOW MERGE_DICT_NUM : ", MERGE_DICT_NUM)
    return None

def solution(commands):
    global board
    stop = -1
    answer = []
    for i, q in enumerate(commands):
        q = q.split()
        if q[0] == 'UPDATE':  # Rule1 or Rule2
            if len(q) == 4:  # Rule1
                Rule1(q)
            else:
                Rule2(q)
        elif q[0] == 'MERGE':
            Rule3(q)
        elif q[0] == 'UNMERGE':
            Rule4(q)
        elif q[0] == 'PRINT':
            answer = Rule5(q, answer)

        if stop == i:
            print("STOP NOW ", i, " command.")
            print(q, "STOP")
            break
    #show_board()
    #show_status()

    #print(answer)
    return answer