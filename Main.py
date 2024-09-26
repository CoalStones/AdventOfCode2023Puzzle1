



if __name__ == "__main__":
    coords = open("coords.txt","r")
    array = []
    for xy in coords:
        array.append(xy)
        
    coordinateArray = []
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    first = ""
    second = ""
    for x in array:
        one = False
        for y in x:
            print(y)
            if y in numbers:
                if one == False:
                    first = y
                    one = True
                    print("Found the first number!")
                else:
                    second = y
                    print("Found the second number!")
                
                toAppend = first + second
                coordinateArray.append(toAppend)
    print(coordinateArray)
