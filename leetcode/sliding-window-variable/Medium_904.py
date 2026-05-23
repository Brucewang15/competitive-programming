class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        max_fruits = 0
        start = end = 0
        picked = {}

        for end in range(len(fruits)):
            picked[fruits[end]] = picked.get(fruits[end], 0) + 1
            if len(picked) > 2:
                max_fruits = max(max_fruits, end - start)
                while len(picked) > 2:
                    picked[fruits[start]] -= 1
                    if picked[fruits[start]] == 0:
                        picked.pop(fruits[start])
                    start += 1
        return max(max_fruits, end - start)


        # max_fruits = 0

        # for i in range(len(fruits)):

        #     picked = set()
        #     picked_fruits = 0
        #     for k in range(i, len(fruits), 1):
        #         if len(picked) > 2:
        #             break
        #         picked.add(fruits[k])
        #         picked_fruits += 1
        #     max_fruits = max(max_fruits, picked_fruits)
        # return max_fruits