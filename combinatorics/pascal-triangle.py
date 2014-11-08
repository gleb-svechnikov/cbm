def triangle(rows):
    for rownum in range (rows):
        newValue=1
        PrintingList = list()
        PrintingList.append(int(1))
        for iteration in range (rownum):
            newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
            PrintingList.append(int(newValue))
        print(PrintingList)

rows = input("Сколько срочек трекгольника Паскаля вывести? ")
triangle(int(rows))
