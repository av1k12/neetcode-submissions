class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardcount = 9

        print("rows checks")
        counts = {}
        for i in range(boardcount):
            for z in board[i]:
                if z != ".":
                    if z in counts:
                        counts[z] = counts.get(z) + 1
                        return False
                    else:
                        counts[z] = 1
            print(counts)
            counts.clear()


        print("column check")
        for i in range(boardcount):
            for z in range(boardcount):
                curVal = board[z][i]
                #print(curVal)
                if curVal != ".":
                    if curVal in counts:
                        counts[curVal] = counts.get(curVal) + 1
                        return False
                    else:
                        counts[curVal] = 1
            print(counts)
            counts.clear()

        print("box check")
        for i in range(boardcount): #this is for the nine boxes
            box_row_start = (i // 3) * 3
            box_col_start = (i % 3) * 3 ###### understand ts more
            #we'll check row by row
            for z in range(3):
                for x in range(3):
                    curVal = board[box_row_start + z][box_col_start + x]
                    
                    if curVal != ".":
                        if curVal in counts:
                            return False
                        else:
                            counts[curVal] = 1
            print(counts)
            counts.clear()
            
        return True

