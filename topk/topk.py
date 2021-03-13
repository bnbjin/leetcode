from collections import Counter
import random


class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k: int):
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            """
            根据pivot_index，把比pivot_index的频次大的数挪到右边，频次较小的挪到左边
            一开始把pivot的值挪到最后是为什么？应该是为了保护pivot的数值，和方便后面挪回来吧
            中间的循环就是从最左边开始，与pivot的频次比较，较小的就把当前迭代的位置元素和store_index的元素交换,store_index往右挪
            因为交换过来的数值，肯定是要比pivot的频次小的，
            迭代完毕后，store_index会坐落在所有比pivot小的元素数，也即store_index左边所有元素都是比pivot要小的
            而sotre_index所指向的那个元素肯定是 >= pivot元素的。有等于，是可能是pviot它自己。
            store_index一开始从最左开始，最后会停留在把大小数挪到两边后，pivot应该所在的位置
            最后与[right], [store_index]交换数值这个也就是把pivot对应的数值挪到它应该所在的位置
            """

            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place.

            一开始随机随机一个pivot，然后partition，得到一个数值已经根据pivot分区的数列，算是一个初始化的过程。
            然后根据pivot和已经分区的数列，判断当前pivot，是相等还是较大、小，类似quicksort的思路，往里递归找到最终对应的pivot的位置。
            即可找到topk
            """
            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
                # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]

if __name__ == '__main__':
    s = Solution()

    q = [1, 2, 7, 0, 2, 6, 8, 7, 2, 1, 0, 0, 5]
    result = s.topKFrequent(q, 2)
    print(result)
