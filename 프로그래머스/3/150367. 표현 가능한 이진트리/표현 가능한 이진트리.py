import math

def check_binary_tree(bin_num: str):
    depth = math.ceil(math.log2(len(bin_num)+1)) # depth of complete binary tree
    
    if len(bin_num) != 2**depth - 1:
        bin_num = '0' * (2**depth-1 - len(bin_num)) + bin_num
    
    # check top -> bottom
    parents = [2**(depth-1)]
    #print(bin_num, root)
    while True:
        # check to be able to next nodes
        if depth == 1:
            break
        
        # next nodes
        depth -= 1
        nodes = []
        # check nodes 
        for p in parents: 
            #print("break ", p-1, parents)
            
            if bin_num[p-1] == '1':
                nodes.append(p - 2**(depth-1))
                nodes.append(p + 2**(depth-1))
            else: # '0'
                if (bin_num[p-2**(depth-1) -1] == '1') or (bin_num[p+2**(depth-1) -1] == '1'):
                    return 0
                else:
                    nodes.append(p - 2**(depth-1))
                    nodes.append(p + 2**(depth-1))
        
        parents = nodes
        
    return 1
        
def solution(numbers: list) -> list:
    """
    Args
        numbers : 
    
    Returns
        
    """
    results = []
    for number in numbers:
        bin_num = bin(number) # to binary number, 0bXXX
        bin_num = bin_num[2:] # remove '0b', XXX
        
        result = check_binary_tree(bin_num)
        results.append(result)
    
    return results