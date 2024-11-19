from Menue import TAX

Game = True

while Game == True:
    ABP = input("a. add books\nb. sell books\nc. reduce price\nd. increase price\ne.show books\nf. exit menue\nz. other menue")
    if ABP == "a":
        adding = TAX.add()
    elif ABP == "b":
        selling = TAX.sell()
    elif ABP == "c":
        reduction = TAX.reducea()
    elif ABP == "d":
        increase = TAX.increasea()
    elif ABP == "e":
        displaybook = TAX.showbooks()
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
