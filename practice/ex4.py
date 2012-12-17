
# -*- coding: cp936 -*
"""
作者：边雪冬
技术支持：冒泡
Email：bxd602@163.com
转载注明出处
"""
mine = []
show = []

for i in xrange(10):
    mine.append([0] * 10)
    show.append(['#'] * 10)

import random,string

for i in xrange(10):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if mine[x][y] == 0:
            print x, y
            mine[x][y] = 1
            break
if True:
    for i in xrange(10):
        for j in xrange(10):
            print mine[i][j],
        print


def getX(self):
    print('X='),
    xRet = raw_input()
    while xRet=='' or (False == isNumber(xRet)) or 0>int(xRet):
        print 'Input Error,Input again(0-9):'
        print('X='),
        xRet = raw_input()
    return int(xRet)
        
        
def getY(self):
    print('Y='),
    yRet = raw_input()
    while yRet=='' or (False == isNumber(yRet)) or 0>int(yRet):
        print 'Input Error,Input again(0-9):'
        print('Y='),
        yRet = raw_input()
    return int(yRet)

def isNumber(strVal):
    nums = string.digits
    for i in strVal:
        if i not in nums:
            return False
    return True

def open_blk(x, y):
    n = 0
    for i in xrange(x - 1, x + 2):
        for j in xrange(y - 1, y + 2):
            if i < 0 or i > 9 or j < 0 or j > 9:
                continue
            if mine[i][j] == 1:
                n += 1
    show[x][y] = str(n)
    if n != 0:
        return
    for i in xrange(x - 1, x + 2):
        for j in xrange(y - 1, y + 2):
            if i < 0 or i > 9 or j < 0 or j > 9:
                continue
            if show[i][j] == '#':
                open_blk(i, j)

print 'start'
while True:
    end = True
    for i in xrange(10):
        for j in xrange(10):
            if show[i][j] == '#' and mine[i][j] == 0:
                end = False
    if end:
        break
    for i in xrange(10):
        print ' '.join(show[i])
    if mine[getX(x)][getY(y)] == 1:
        print 'you lost'
        break
    open_blk(x, y)
