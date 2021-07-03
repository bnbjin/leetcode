import unittest

class TestArray(unittest.TestCase):
    '''
    array 101
    '''

    def test_right_greatest(self):
        '''
        https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
        Replace Elements with Greatest Element on Right Side
        '''

        def replaceElements(arr):
            last_max = -1
            for i in range(len(arr)):
                if last_max != -1 and arr[i] != last_max:
                    arr[i] = last_max
                    continue

                last_max = -1
                for j in range(i + 1, len(arr)):
                    if arr[j] > last_max:
                        last_max = arr[j]

                arr[i] = last_max

            return arr

        result = replaceElements([17,18,5,4,6,1])
        if result != [18,6,6,6,1,-1]:
            self.fail(result)

    def test_height_checker(self):
        '''
        https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/

        bubble sort or selection sort? counting sort!

        counting sort pseudocode:
        ---
        count = array of k+1 zeros
        for x in input do
            count[key(x)] += 1

        total = 0
        for i in 0, 1, ... k do
            count[i], total = total, count[i] + total

        output = array of the same length as input
        for x in input do
            output[count[key(x)]] = x
            count[key(x)] += 1

        return output
        ---
        '''

        def counting_sort_variant(heights):
            k = 100 + 1
            count = k * [0, ]
            for i in heights:
                count[i] += 1

            i = 0
            pos_changed = 0
            for j in heights:
                while count[i] == 0:
                    i += 1

                if i != j:
                    pos_changed += 1

                count[i] -= 1

            return pos_changed

        cases = [
            {'arr': [1,1,4,2,1,3], 'res': 3},
            {'arr': [5,1,2,3,4], 'res': 5},
            {'arr': [1,2,3,4,5], 'res': 0},
        ]

        for c in cases:
            self.assertEqual(counting_sort_variant(c['arr']), c['res'])

    def test_find_max_consecutive_ones(self):
        '''
        https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3230/

        中间夹着可能不止一个0，所以也需要标记是只有一个0，还是有2个或以上的0
        也不知是0还是1开始，奇偶不固定对应。
        '''

        def findMaxConsecutiveOnes(nums):
            prev, curr, max_len = -1, 0, 0

            for n in nums:
                if n == 0:
                    prev, curr = curr, 0
                else:
                    curr += 1

                max_len = max(max_len, prev + 1 + curr)

            return max_len

    def test_third_max_number(self):
        '''
        https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/

        heap sort? nope
        set + iteration find the third big number
        '''

        def find_max_number(nums):
            maximums = set()
            for num in nums:
                maximums.add(num)
                if len(maximums) > 3:
                    maximums.remove(min(maximums))
            if len(maximums) == 3:
                return min(maximums)
            return max(maximums)

    def test_find_Disappeared_Numbers(self):
        '''
        https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/

        先in-place排序，每个元素与他所在的位置的元素交换，时间复杂度为n
        然后迭代排序好了的列表，把列表中与下表对应元素切除，那么剩下的
        '''

        def findDisappearedNumbers(nums):
            for i in range(len(nums)):
                new_index = abs(nums[i])-1
                if nums[new_index] > 0:
                    nums[new_index] *= -1

            i = 0
            for j in range(len(nums)):
                if nums[j] > 0:
                    nums[i] = j+1
                    i += 1

            return nums[:i]

        cases = [
            {'in':[4,3,2,7,8,2,3,1], 'out':[5, 6]},
        ]
        for c in cases:
            self.assertEqual(c['out'], findDisappearedNumbers(c['in']))

    def test_max_profit(self):
        '''
        https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
        动态规划，如何能确定最优的子问题结构呢？子问题边界是什么呢？
        边界是每个local minimum和local maximum
        '''

        def maxProfit(prices):
            i = 0
            profit = 0

            while i < len(prices)-1:
                # 一开始是下坡的话，其实是可以被忽略掉的
                while i < len(prices)-1 and prices[i] >= prices[i+1]:
                    i += 1
                lmin = prices[i]

                while i < len(prices)-1 and prices[i] <= prices[i+1]:
                    i += 1
                lmax = prices[i]

                profit += lmax - lmin

            return profit

        cases = [{'in': [7, 1, 5, 3, 6, 4], 'out': 7}]
        for c in cases:
            self.assertEqual(c['out'], maxProfit(c['in']))
