__author__ = 'zhengyiwang'
class Solution(object):
    def isValidSerialization(self, preorder):
        preorder = preorder.split(",")
        stack = []
        for a in preorder:
            #push into stack if is number
            if a != "#":
                stack.append(a)
            else:
                if not self.handle_none(stack):
                    return False
        #in the end, the tree should only have a null left in the stack
        if len(stack) == 1 and stack[0] == "#":

            return True
        return False

    def handle_none(self, stack):
        if len(stack) == 0 or stack[-1] != "#":
            stack.append("#")
        else:
            #pop the previous # too and change the peek number to #
            #which means change a small child tree into null
            stack.pop()

            if len(stack) == 0:
                return False
            stack.pop()
            self.handle_none(stack)
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))