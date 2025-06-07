# =========================== Detect Cycle in Linked List ===========================

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


# =========================== Count Nodes in Loop ===========================

class Solution:
    def countNodesInLoop(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                count = 1
                fast = fast.next
                while slow != fast:
                    fast = fast.next
                    count += 1
                return count
        return 0


# =========================== Binary Tree Level Order Traversal ===========================

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        ans = []

        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            ans.append(level)

        return ans


# =========================== Height of Binary Tree ===========================

class Solution:
    def findHeight(self, root):
        if root is None:
            return 0
        lh = self.findHeight(root.left)
        rh = self.findHeight(root.right)
        return 1 + max(lh, rh)

    def maxDepth(self, root):  # LeetCode format
        return self.findHeight(root)


# =========================== Zigzag Level Order Traversal ===========================

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = [root]
        ans = []

        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            ans.append(level)

        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i] = ans[i][::-1]

        return ans


# =========================== Sort Linked List ===========================

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next

        arr.sort()

        temp = head
        ind = 0
        while temp:
            temp.val = arr[ind]
            ind += 1
            temp = temp.next

        return head


# =========================== Palindrome Linked List ===========================

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        return arr == arr[::-1]


# =========================== Convert Array to BST - Placeholder ===========================
# Note: You had marked this section but didn't include the code.
# Here's a basic template for converting sorted array to BST.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
