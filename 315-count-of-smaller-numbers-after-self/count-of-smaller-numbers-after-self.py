class Solution(object):
    def countSmaller(self, nums):
        n = len(nums)
        counts = [0] * n
        indices = list(range(n))

        def merge_sort(left, right):
            if right - left <= 1:
                return

            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)

            temp = []
            i, j = left, mid
            smaller = 0

            while i < mid and j < right:
                if nums[indices[j]] < nums[indices[i]]:
                    temp.append(indices[j])
                    smaller += 1
                    j += 1
                else:
                    counts[indices[i]] += smaller
                    temp.append(indices[i])
                    i += 1

            while i < mid:
                counts[indices[i]] += smaller
                temp.append(indices[i])
                i += 1

            while j < right:
                temp.append(indices[j])
                j += 1

            indices[left:right] = temp

        merge_sort(0, n)
        return counts
