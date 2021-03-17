def  pattern(n):
    asc = ord('A')
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(asc)
            print(ch, end=" ")
            asc = asc +1
        print("\r")
n = 5
pattern(n)