mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]

def traverse(inlist,x,y):
    print(inlist[x][y])
    if x == 0:
        if y < 3:
            traverse(inlist,x+1,y+1)
            traverse(inlist,x,y+1)
    # if x == 0 and

traverse(mat,0,0)