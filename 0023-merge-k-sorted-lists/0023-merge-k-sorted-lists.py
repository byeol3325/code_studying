# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.k = 0
        self.lists = None

    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        self.k = len(lists)
        if self.k == 0:
            return None
        
        self.lists = lists
        linked_list, end_element = None, None # 결과값

        min_value = float("inf") # 초기값 설정

        while True:
            min_value, min_index = self.find_next_element(min_value) # result에 넣을거 초기 생산
            
            if min_value == float("inf"): # 모든 list 찾아봐도 다음 element가 없음. 끝난 경우
                break
            else:
                if linked_list == None: # 초기값
                    end_element = ListNode(min_value)
                    linked_list = end_element
                else: # ListNode(1, 2) #linked_list.next = 
                    end_element.next = ListNode(min_value)
                    end_element = end_element.next
            self.lists[min_index] = self.lists[min_index].next # 찾은거는 한칸씩 이동

        return linked_list
        
    def find_next_element(self, now_element):
        min_value, min_index = float("inf"), 0
        
        for i in range(self.k):
            if self.lists[i] == None:
                continue

            if now_element == self.lists[i].val:
                return now_element, i
            
            elif min_value > self.lists[i].val:
                min_value = self.lists[i].val
                min_index = i
        
        return min_value, min_index