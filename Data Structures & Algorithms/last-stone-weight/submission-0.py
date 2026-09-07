class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        stones = sorted(stones, reverse = True)

        count = 0
        while stones:
            print(stones)
            if len(stones) == 1:
                return stones[0]

            bigger, big = stones[0], stones[1]

            del stones[0]
            del stones[0]

            if bigger > big:
                stones.append(bigger - big)
                stones = sorted(stones, reverse = True)
        return 0