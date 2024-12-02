from Menue import TAX

PGA = TAX()

Game = True

while Game == True:
    ABP = input("a. add books\nb. sell books\nc. reduce price\nd. increase price\ne.show books\nf. exit menue\nz. other menue")
    if ABP == "a":
        adding = PGA.add()
    elif ABP == "b":
        selling = PGA.sell()
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
