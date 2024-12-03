from Menue import BookStore


foop = True
library = BookStore()


while foop == True:
	bng = input(" A. Add books \n B. Sell books \n C. Reduce price (5%) \n D. Increase price (5%)\n E. Display all books \n F. Quit \n ").upper()
	if bng == "A":
		Adding = library.add()
	elif bng == "B":
		Selling = library.sell()
	elif bng == "C":
		reducing == library.reduce

	elif bng == "F":
		Exit = library.qui(foop)
		break







"""from Menue import TAX

nbp = TAX()

Game = True

while Game == True:
    ABP = input("a. add books\nb. sell books\nc. reduce price\nd. increase price\ne.show books\nf. exit menue\nz. other menue")
    if ABP == "a":
        adding = nbp.add()
    elif ABP == "b":
        selling = nbp.sell()
    elif ABP == "c":
        reduction = PGA.reducea()
    elif ABP == "d":
        increase = PGA.increasea()
    elif ABP == "e":
        displaybook = PGA.showbooks()
    elif ABP == "f":
        Game == False 
        break
    elif ABP == "z":
        ABP = input("l. load to file\ns. save to file")
        if ABP == "l":
            load = TAX.load()
        elif ABP == "s":
            save = TAX .save()
        break
"""