class StockSpanner:

    def __init__(self):
        self.dic = {}
        self.pointer = 1
    
    
    def next(self, price: int) -> int:
        if not self.dic:
            self.dic[self.pointer] = price
            return self.pointer
        self.pointer += 1
        self.dic[self.pointer] = price
        i = self.pointer - 1
        while i != 0 and price >= self.dic[i]:
            i -= 1
        return (self.pointer - i)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)