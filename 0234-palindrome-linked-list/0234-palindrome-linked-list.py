# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True


        # used to reverse the linked list
        def reverse_ll(node):
            prev = None
            while node:
                next_node = node.next 
                node.next = prev
                prev = node
                node = next_node

            return prev         

        
        # now let's find middle of LL
        def find_middle(node):
            slow,fast = node, node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next 
            return slow

        middle = find_middle(head)

        # reverse the second half of LL

        sec_half = reverse_ll(middle)

        # compare both first half and second half
        first_half = head
        while sec_half:
            if first_half.val != sec_half.val:
                return False
            first_half = first_half.next
            sec_half = sec_half.next

        return True





























        # if head is None:
        #     return True

        # values = []
        # current = head 

        # while current is not None:
        #     values.append(current.val)
        #     current = current.next

        # left, right = 0, len(values) -1
        # while left < right:
        #     if values[left] != values[right]:
        #         return False
        #     left +=1
        #     right -=1

        # return True

    


#     Time Complexity (TC):

# The first loop that traverses the linked list to collect the values has a time complexity of 
# O(n) because it iterates through each node once.
# The second loop that compares the values from both ends of the list has a time complexity of 
# O(n/2) since it iterates until the left and right pointers meet in the middle.
# Therefore, the overall time complexity is O(n+n/2)=O(n).

# Space Complexity (SC):

# The space complexity is primarily determined by the additional space used to store the values of the linked list nodes in the values list.
# The values list stores all n node values, so it consumes O(n) space.
# Apart from the values list, the space complexity is constant, as we are using a fixed number of variables.
# Therefore, the overall space complexity is O(n).
# So, the time complexity of the solution is O(n) and the space complexity is also O(n).