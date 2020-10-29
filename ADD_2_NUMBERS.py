'''
Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Example:

5 / 2 = 2
Also, consider if there can be overflow cases. For overflow case, return INT_MAX.

Note: INT_MAX = 2^31 - 1
Solution 1: Recursion

class Solution(object):
    def divide(self, a, b):
        def helper(a, b):
            if a < b: return 0
            multiply = 1 # 1 2 4 8 16...
            sum = b
            while (sum + sum) <= a:
                sum += sum
                multiply += multiply
            return multiply + helper(a - sum, b)
        
        INT_MAX = 2147483647 # 2**31 - 1
        positive = (a >= 0) == (b >= 0) # Positive only if a and b the same sign
        ans = helper(abs(a), abs(b))
        ans = ans if positive else -ans
        return min(ans, INT_MAX)
Complexity:

Time: O(log(N) ^ 2), where N is absolute value of dividend
Solution 2: Non recursion

class Solution(object):
    def divide(self, a, b):
        INT_MAX = 2147483647 # 2**31 - 1
        positive = (a >= 0) == (b >= 0) # Positive only if a and b the same sign
        a, b = abs(a), abs(b)
        ans = 0
        while a >= b:
            multiply = 1 # 1 2 4 8 16...
            sum = b
            while (sum + sum) <= a:
                sum += sum
                multiply += multiply
            ans += multiply
            a -= sum
        ans = ans if positive else -ans
        return min(ans, INT_MAX)
Complexity:

Time: O(log(N) ^ 2), where N is absolute value of dividend
Space: O(1)
'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	
	def divide(self, A, B):
	    # B= divisor, A= dividend
	   INT_MAX = (2**31)-1
	   def helper(A,B):
	       if A<B:
	           return 0
	       multiply = 1
	       sum_B = B
	       while (sum_B+sum_B)<=A:
	           sum_B +=sum_B
	           multiply +=multiply
	       return multiply+helper(A-sum_B,B)
	   is_positive = (A>=0) == (B>=0)
	   ans = helper(abs(A),abs(B))
	   ans = ans if is_positive else -ans
	   return min(ans,INT_MAX)
	
#A = 20, B = 10
#LOG A^2

