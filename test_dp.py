import math
import unittest
import bisect
from collections import defaultdict

class TestDynamicProgramming(unittest.TestCase):
    '''
    dynamic programming
    https://leetcode.com/tag/dynamic-programming/
    '''

    def test_maxSubArray(self):
        # https://leetcode.com/problems/maximum-subarray/

        def maxSubArray(nums):
            # Kadane's algorithm

            # Initialize our variables using the first element.
            current_subarray = max_subarray = nums[0]

            # Start with the 2nd element since we already used the first one.
            for num in nums[1:]:
                # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
                current_subarray = max(num, current_subarray + num)
                max_subarray = max(max_subarray, current_subarray)

            return max_subarray

        def max_sub_array_divide_and_conquer(nums):
            # divide and conquer - 递归分成三种情况，结果仅在左边、右边，或穿过中间。

            if len(nums) == 1:
                return nums[0]

            mid = math.floor(len(nums) / 2)



    def test_unique_binary_search_trees(self):
        '''
        https://leetcode.com/problems/unique-binary-search-trees/
        * device and conquer - S(n) = S(n-1) + f(n)
        '''

        pass

    def test_best_time_to_buy_and_sell_stock(self):
        '''
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

        实际上，这不是动态规划问题。

        方法一：
        求出每个位置的增长轻快
        类似求最大子串的算法

        方法二（更优）：
        其实就是最低买入，最高卖出
        '''

        def max_profit(prices) -> int:
            if len(prices) == 0:
                return 0

            prices_aux = [0, ]
            for i in range(1, len(prices)):
                prices_aux.append(prices[i] - prices[i-1])

            cur_profit = 0
            max_profit_ = 0
            for p in prices_aux[1:]:
                if p > cur_profit + p:
                    cur_profit = p
                else:
                    cur_profit = cur_profit + p

                if cur_profit > max_profit_:
                    max_profit_ = cur_profit

            return max_profit_

        cases = [
            {
                'in': [7,1,5,3,6,4],
                'out': 5,
            }, {
                'in': [7,6,4,3,1],
                'out': 0,
            }
        ]

        for case in cases:
            self.assertEqual(case['out'], max_profit(case['in']))

    def test_is_subsequence(self):
        '''
        https://leetcode.com/problems/is-subsequence/
        判断字符串A的字符是否是另一个字符串B的子集

        设计到的解法非常多，一道非常好的题目。
        解法包括：分治，贪婪，双指针，动态规划。

        求集合: 好像不是其中一个方法
        '''

        def is_subsequence_divide_and_conquer(s: str, t: str) -> bool:
            '''
            分治的思路很清晰，把匹配的源串和检验过的目标串切掉，然后递归校验。

            关于贪婪算法的分析没太看懂。。
            '''

            if len(s) == 0:
                return True

            if len(t) == 0:
                return False

            if s[0] == t[0]:
                return is_subsequence_divide_and_conquer(s[1:], t[1:])
            else:
                return is_subsequence_divide_and_conquer(s, t[1:])

        def is_subsequence_double_pointer(s: str, t: str) -> bool:
            i = 0
            j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1

                j += 1

            return i == len(s)

        def is_subsequence_greedy_match_with_hashmap(s: str, t: str) -> bool:
            '''
            贪婪匹配

            先把目标字符串哈希到哈希表中，key是字符，卫星值存放字符出现的索引
            然后对于每个源字符串，迭代查找每一个字符是否在目标字符串中出现，且按顺序：
            1. 与目标字符串每次匹配的位置都必须是当前位置都右边，即目标字符串的匹配位置必须是单调的
            2. （贪婪算法）每次源串字符匹配，找到的目标串字符位置，都是当前位置的最近，且较大的位置。
            '''

            letter_indices_table = defaultdict(list)
            for index, letter in enumerate(t):
                letter_indices_table[letter].append(index)

            curr_match_index = -1
            for letter in s:
                if letter not in letter_indices_table:
                    return False  # no match at all, early exit

                # greedy match with binary search
                indices_list = letter_indices_table[letter]
                match_index = bisect.bisect_right(indices_list, curr_match_index)
                if match_index != len(indices_list):
                    curr_match_index = indices_list[match_index]
                else:
                    return False  # no suitable match found, early exist

            return True

        def is_subsequence_dynamic_programming(s: str, t: str) -> bool:
            '''
            动态规划解法
            思路参照edit distance问题
            创建一个源、目标字符串矩阵：
            逐个元素初始化：
            如果s[row-1] == t[col-1]，则取 e[row][col] = e[row-1][col-1] + 1，否则取max(e[row-1][col], e[row][col-1])
            数字表示目标字符串转换为源字符串需要进行多少次操作（删除、插入、替换） t[0:col] -> s[0:row]

            结果判断：
            当source最后一个字符，即要把源字符串通过操作转换成目标字符串的次数是源字符串的长度时，结果正确
            即目标字符串可以通过删除n次得到源字符串
            否则，源字符串不是目标字符串的子串
            '''
            source_len, target_len = len(s), len(t)

            # the source string is empty
            if source_len == 0:
                return True

            # matrix to store the history of matches/deletions
            dp = [[0] * (target_len + 1) for _ in range(source_len + 1)]

            # DP compute, we fill the matrix column by column, bottom up
            for col in range(1, target_len + 1):
                for row in range(1, source_len + 1):
                    if s[row - 1] == t[col - 1]:
                        # find another match
                        dp[row][col] = dp[row - 1][col - 1] + 1
                    else:
                        # retrieve the maximal result from previous prefixes
                        dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

                # check if we can consume the entire source string,
                #   with the current prefix of the target string.
                if dp[source_len][col] == source_len:
                    return True

            return False


        cases = [
            {
                "s": "abc",
                "t": "ahbgdc",
                "res": True,
            }, {
                "s": "axc",
                "t": "ahbgdc",
                "res": False,
            }, {
                "s": "acb",
                "t": "ahbgdc",
                "res": False,
            }
        ]

        for c in cases:
            self.assertEqual(c['res'], is_subsequence_divide_and_conquer(c['s'], c['t']))
