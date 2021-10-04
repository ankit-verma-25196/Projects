class Solution:
    def allCount(self,n):
        if n >=11111 and n< 111111:
            div = n//11111
            rem = n%11111
            return div,rem
        elif n >=1111 and n < 11111:
            div = n//1111
            rem = n%1111
            return div,rem
        elif n >=111 and n < 1111:
            div = n//111
            rem = n%111
            return div,rem
        elif n>=11 and n < 111:
            div = n//11
            rem = n%11
            return div,rem
        elif n>=1 and n<=9:
            return n,0
        elif n == 10:
            return 1,0
        
    def minPartitions(self, n: str) -> int:
        n_int = int(n)
        total = 0
        while True:
            print("First n ="+str(n_int))
            count,n_int= self.allCount(n_int)
            total += count
            print("count="+str(count))
            print("Other n ="+str(n_int))
            if n_int == 0:
                break
            
        return total
        
