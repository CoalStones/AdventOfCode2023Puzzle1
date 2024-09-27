



if __name__ == "__main__":
    coords = open("coords.txt","r")
    array = []
    for xy in coords:
        array.append(xy)
    coords.close()

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    sum = 0
    for x in array:
        one = False
        first = ""
        second = ""
        for y in x:
            # print(y)
            if y in numbers:
                if one == False:
                    first = y
                    one = True
                    # print("Found the first number!")
                else:
                    print("any truers?", end=" ")
                    second = y
                    # print("Found the second number!")
                
        if one == True:
            if second == "":
                second = first
            toAppend = first + second
            print("toAppend " + toAppend + " first: " + first + " second: " + second + " line: " + x)
            sum += int(toAppend)
    print(sum)
