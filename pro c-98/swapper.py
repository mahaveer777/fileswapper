def swapFileData():
    file1 = "pg1.txt"
    file2 ="pg2.txt"


    with open(file1, 'r') as a:
        c = a.read()
    with open(file2, 'r') as b:
        d = b.read()
    with open(file1, 'w') as a:
        a.write(d)
    with open(file2, 'w') as b:
        b.write(c)
swapFileData()