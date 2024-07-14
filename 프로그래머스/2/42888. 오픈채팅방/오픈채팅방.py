def read_all_command(record: list):
    """
    ID => 최종 name으로
    dict[ID] = name
    """
    name_dict = {} # [ID] = name
    for line in record:
        line = line.split()
        if line[0] == "Enter":
            name_dict[line[1]] = line[2]
        elif line[0] == "Change":
            name_dict[line[1]] = line[2]
    return name_dict

def print_all_command(record: list, name_dict: dict) -> list:
    result = []
    for line in record:
        line = line.split()
        if line[0] == "Enter":
            line_result = name_dict[line[1]] + "님이 들어왔습니다."
            result.append(line_result)
        elif line[0] == "Leave":
            line_result = name_dict[line[1]] + "님이 나갔습니다."
            result.append(line_result)
    return result

def solution(record):
    """
    Enter ID name
    Leave ID
    Change ID name
    """
    answer = []
    name_dict = read_all_command(record)
    answer = print_all_command(record, name_dict)
    return answer