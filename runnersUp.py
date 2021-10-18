#A.sort(reverse=True)
#i=1
#prev=A[0]#n=5
import os
def getRunnersUp(score_sheet):
    file=open(score_sheet, 'r')
    A=file.readlines()
    n,A=int(A[0]), A[1].split(' ')
    A=list(set(A))
    A.sort(reverse=True)
    print(A[1])
getRunnersUp("sample.txt")


