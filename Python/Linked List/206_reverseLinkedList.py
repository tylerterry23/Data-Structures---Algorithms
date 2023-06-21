"""
LeetCode Problem #206: Reverse Linked List

Problem statement:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
1 > 2 > 3 > 4 > 5
5 > 4 > 3 > 2 > 1

Example 2:
1 > 2
2 > 1

Example 3:
[]
[]

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: 
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# In terms of the follow up question, YES I can implement both iteratively and recursively. Let's do it!

# Iterative Solution
# For this solution we are going to use two pointers to store the prev and current node in order to turn them around
# The key is to remember to keep track where the current node is pointing we will store this as 'nxt'
def reverseListIteratively(head):
    # First we prepare out pointers for the head and the previous which to start will be Null
    prev, curr = None, head

    # as we iterate through curr will become next so we will continue until current is null (while there is curr)
    while curr:

        # Before messing around lets remember where our current node is pointing and store it in `nxt`
        nxt = curr.next

        # now we want the previous node to actually be the next node to turn this thing around so lets change the current nodes next value
        curr.next = prev

        # Everything for the current node is set to be turned around so now its time to move on so our current becomes our previous
        prev = curr

        # we can use the `nxt` we saved earlier and move down the chain making changing the current node 
        curr = nxt

    # once curr == Null that means we made it to the end of the list (prev = last element, curr = null) so we can return our new head which will be prev
    return prev 



# Recursive Solution 
# The approach here is to use the power of recursion to reverse the linked list.
# The idea is to traverse to the end of the list using recursion and as we return from each recursive call,
# we rearrange the pointers of the nodes to reverse the linked list.
# Recursion can be complex to understand, let's break it down step by step:

def reverseListRecursively(head):

    # 1. Empty List Check: If the linked list is empty, there's nothing to reverse, so we return None.
    if not head:
        return None
    
    # 2. Initial New Head: We consider the first node (head) we receive as our `newHead`.
    newHead = head

    # 3. Recursion on Next Node: If there is a node following the current head (i.e., if head.next is not None)...
    if head.next:

        # We make a recursive function call on the next node. 
        # The result of this call will give us the new head of the reversed linked list.
        newHead = self.reverseListRecursively(head.next)

        # We then change the direction of the link between the current node and the next node. 
        # Instead of the current node (head) pointing to the next node, we make the next node (head.next) point to the current node.
        head.next.next = head
        head.next = None  # It's crucial to add this line to prevent a cycle: the current node should not link to the next node anymore.

    # 4. Return New Head: The `newHead` will eventually be the last node in the original list, and the first node in the reversed list.
    # We return `newHead` once the entire list has been reversed.
    return newHead



