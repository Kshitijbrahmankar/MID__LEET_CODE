class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1

        x = list(str(abs(x)))

        left = 0
        right = len(x)-1

        while left < right:
            x[left] , x[right] = x[right] , x[left]
            left += 1
            right -=1

        result = sign * int("" .join(x))

        if result < -2**31 or result > 2**31 -1:
            return 0
        return result


        # sign = -1 if x < 0 else 1

        # x = list(str(abs(x)))

        # left = 0
        # right = len(x)-1

        # while left < right:
        #     x[left] , x[right] = x[right] , x[left]
        #     left += 1
        #     right -= 1 
            
        #     result = sign * int("" .join(x))


        #     if result < -2**31 or result > 2**31 -1:
        #         return 0
        #     return result