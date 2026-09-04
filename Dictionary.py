def findShortestSubArray(self, nums):
        freq = {}
        first = {}
        last = {}

        degree = 0

        for i, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1

            if num not in first:
                first[num] = i

            last[num] = i

            degree = max(degree, freq[num])

        ans = len(nums)

        for num in freq:
            if freq[num] == degree:
                length = last[num] - first[num] + 1
                ans = min(ans, length)

        return ans