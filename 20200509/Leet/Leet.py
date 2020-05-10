
class Solution:

    squareDigit = {0:[0], 1:[1, 9], 4:[2, 8], 5:[5], 6:[4, 6], 9:[3, 7]}

    productDigit = {0:{0:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1:[0], 2:[0, 5], 3:[0], 4:[0, 5], 5:[0, 2, 4, 6, 8], 6:[0, 5], 7:[0], 8:[0, 5], 9:[0]},
                            1:{1:[1], 3:[7], 7:[3], 9:[9]},
                            2:{1:[2], 2:[1, 6], 3:[4], 4:[3, 8], 6:[2, 7], 7:[6], 8:[4, 9], 9:[8]},
                            3:{1:[3], 3:[1], 7:[9], 9:[7]},
                            4:{1:[4], 2:[2, 7], 3:[8], 4:[1, 6], 6:[4, 9], 7:[2], 8:[3, 8], 9:[6]},
                            5:{1:[5], 3:[5], 5:[1, 3, 5, 7, 9], 7:[5], 9:[5]},
                            6:{1:[6], 2:[3, 8], 3:[2], 4:[4, 9], 6:[1, 6], 7:[8], 8:[2, 7], 9:[4]},
                            7:{1:[7], 3:[9], 7:[1], 9:[3]},
                            8:{1:[8], 2:[4, 9], 3:[6], 4:[2, 7], 6:[3, 8], 7:[4], 8:[1, 6], 9:[2]},
                            9:{1:[9], 3:[9], 7:[7], 9:[1]},
                            }

    def isPerfectSquare(self, x):
        while not x%25:
            x = int(x/25)

        if not x%10:
            return False

        if x > 10000000000:
            return None

        aa = self.squareDigit.get(x%10, []) 
        for a in aa:
            x1 = int((x - a*a)/10)
            if x1 == 0 and x == a*a:
                return True
            if x1 <= 0:
                break
            bb = self.productDigit.get(x1%10, {}).get((2*a)%10, [])
            if len(bb) > 2:
                print('Fail', x, bb)
            for b in bb:
                x2  = int((x1 - 2*(a+5*b)*b)/10)
                if x2 == 0 and (10*b + a)*(10*b + a) == x:
                    return True
                if x2 <= 0:
                    break
                cc = self.productDigit.get(x2%10, {}).get((2*a)%10, [])
                if len(cc) > 2:
                    print('Fail', x, c)
                for c in cc:
                    x3  = int((x2 - 2*(a + 10*b)*c)/10)
                    if x3 == 0 and (100*c + 10*b + a)*(100*c + 10*b + a) == x:
                        return True
                    if x3 <= 0:
                        break
                    dd = self.productDigit.get(x3%10, {}).get((2*a)%10, [])
                    if len(dd) > 2:
                        print('Fail', x, dd)
                    for d in dd:
                        x4  = int((x3 - 10*c*c - 2*(a + 10*b)*d)/10)
                        if x4 == 0 and (1000*d + 100*c + 10*b + a)*(1000*d + 100*c + 10*b + a) == x:
                            return True
                        if x4 <= 0:
                            break
                        ee = self.productDigit.get(x4%10, {}).get((2*a)%10, [])
                        if len(ee) > 2:
                            print('Fail', x, ee)
                        for e in ee:
                            v = (10000*e + 1000*d + 100*c + 10*b + a)
                            if v*v == x:
                                return True
        return False

    def isPerfectSquare_2(self, num):
        #fastest from discussion page
        if num == 1:
            return True
        left, right = 2, int(num/2)
      
        while left <= right:
            mid = int((left+right)/2)
            mid_sq = mid**2
            if mid_sq == num:
                return True
            elif mid_sq < num:
                left = mid+1
            else:
                right = mid-1
        return False


import random
from datetime import datetime

if __name__ == '__main__':

    start = 1000000000
    end = 10000000000
    tests = []
    for i in range(1000000):
        tests.append(random.randint(start, end))

    t1 = datetime.now()
    for num in tests:
        reslt = Solution().isPerfectSquare(num)

    t2 = datetime.now()
    for num in tests:
        reslt_2 = Solution().isPerfectSquare_2(num)
    t3 = datetime.now()

    print(t1, t2, t3)
    print('my time = ', (t2-t1).seconds)
    print('newton time = ', (t3-t2).seconds)

  #      if not i%1000:
   #         print(i)



