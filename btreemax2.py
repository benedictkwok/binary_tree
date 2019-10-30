# Python3 program to find maximum element, maximum sum of the path
# ,and print the maximum path in a Bianry Tree

# class to create a new node
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# Returns maximum value
def findMax(root):

    # Base case
    if not root:
        return False

    # Return maximum of 3 values:
    # 1) Root's data
    # 2) Max in Left Subtree
    # 3) Max in right subtree
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if (lres > res):
        res = lres
    if (rres > res):
        res = rres
    return res
def max_sum_path(root, sum):
    if sum==0:
        return True
    if root is None:
        return 0
    left = max_sum_path(root.left, sum - root.data)
    right = max_sum_path(root.right, sum - root.data)

    if left or right:
        print (root.data, end = " ")

    return  left  or right

def max_sum_top_down(root):
    if not root:
        return 0
    max_sum_left =0 if root.left is None else max_sum_top_down(root.left)
    max_sum_right =0 if root.right is None else max_sum_top_down(root.right)
    return max_sum_left + root.data if max_sum_left > max_sum_right else max_sum_right + root.data
def print_result(root):
    max_sum=max_sum_top_down(root)
    print ("Maximum element is", findMax(root))
    print ("Max sum from leaf to root path is: ", max_sum)
    max_sum_path(root, max_sum)

# Driver Code
if __name__ == '__main__':
    root = newNode(5)
    root.left     = newNode(-7)
    root.right     = newNode(-5)
    root.left.right = newNode(6)
    root.left.right.left=newNode(1)
    root.left.right.right=newNode(11)
    root.right.right=newNode(9)
    root.right.right.left=newNode(12)


    print_result(root)
