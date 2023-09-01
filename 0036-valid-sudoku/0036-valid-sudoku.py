class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                element = b[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        print(res)
        return len(res) == len(set(res))
        '''def isvalid(num,i,j):
            cnt=0
            for k in range(9):
                if b[i][k]==num:
                    cnt+=1
                if b[k][j]==num:
                    cnt+=1
            if cnt>2:
                return False
            cnt=0
            if i<3 and j<3:
                for x in range(3):
                    for y in range(3):
                        if b[x][y]==num:
                            cnt+=1
            elif i<3 and j in range(3,6):
                for x in range(3):
                    for y in range(3,6):
                        if b[x][y]==num:
                            cnt+=1
            elif i<3 and j in range(6,9):
                for x in range(3):
                    for y in range(6,9):
                        if b[x][y]==num:
                            cnt+=1
            elif i in range(3,6) and j<3:
                for x in range(3,6):
                    for y in range(3):
                        if b[x][y]==num:
                            cnt+=1
            elif i in range(3,6) and j in range(3,6):
                for x in range(3,6):
                    for y in range(3,6):
                        if b[x][y]==num:
                            cnt+=1
            elif i in range(3,6) and j in range(6,9):
                for x in range(3,6):
                    for y in range(6,9):
                        if b[x][y]==num:
                            cnt+=1
            elif i in range(6,9) and j<3:
                for x in range(6,9):
                    for y in range(3):
                        if b[x][y]==num:
                            cnt+=1
            elif i in range(6,9) and j in range(3,6):
                for x in range(6,9):
                    for y in range(3,6):
                        if b[x][y]==num:
                            cnt+=1
            elif i in range(6,9) and j in range(6,9):
                for x in range(6,9):
                    for y in range(6,9):
                        if b[x][y]==num:
                            cnt+=1
            if cnt>1:
                return False
            return True
        for i in range(9):
            for j in range(9):
                for num in range(1,10):
                    if b[i][j].isdigit():
                        if not isvalid(b[i][j],i,j):
                            return False
        return True
            '''