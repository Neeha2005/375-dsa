class Solution(object):
    def maxleft(self, height):
        left_max = [0] * len(height)
        left_max[0] = height[0]
        for x in range(1, len(height)):
            left_max[x] = max(height[x], left_max[x - 1])
        return left_max

    def maxright(self, height):
        right_max = [0] * len(height)
        right_max[-1] = height[-1]
        for x in range(len(height) - 2, -1, -1):
            right_max[x] = max(height[x], right_max[x + 1])
        return right_max

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        total_trap = [0] * len(height)
        left = self.maxleft(height)
        right = self.maxright(height)
        for x in range(len(height)):
            total_trap[x] = min(left[x], right[x]) - height[x]
        return sum(total_trap)