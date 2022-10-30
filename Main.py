row1 = ['😊','😊','😊']
row2 = ['😁','😁','😁']
row3 = ['😅','😅','😅']

map = [row1,row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")
a = input("choose a two digits first  Horizo, second for vertical") #Input always a string 
print(a)

firstDigitHorizonal = int(a[0]) 
secondDigitVertical = int(a[1])

LigneSelected = map[firstDigitHorizonal-1]     #we selected a row 
LigneSelected [secondDigitVertical - 1 ] = "Y" #Selected an element from the row  



print(f"{row1}\n{row2}\n{row3}\n")
