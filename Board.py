class Board:

    def __init__(self,intYSize,intXSize,lstCar):
        self.intXSize = intXSize
        self.intYSize = intYSize
        self.dicCar = {}
        self.lstBoard = []

        for i in range(intYSize):
            lstRow = []
            for j in range(intXSize):
                lstRow.append('')
            self.lstBoard.append(lstRow)

        for i in range(len(lstCar)):
            self.markCar(lstCar[i])
            self.dicCar[lstCar[i].strID] = lstCar[i]

    def markCar(self,objCar):
        intX = objCar.intX
        intY = objCar.intY

        self.removeCarMark(objCar) # 차 이동하려면 기존 위치 지우고 새로 markCar(self, objCar)
        self.dicCar[objCar.strID] = objCar
        for i in range(objCar.intSize):
            self.lstBoard[intY][intX] = objCar.strID
            if objCar.intOrient == 0:
                intY = intY + 1
            else:
                intX = intX + 1

    def removeCarMark(self,objCar):
        for i in range(self.intYSize):
            for j in range(self.intXSize):
                if self.lstBoard[i][j] == objCar.strID:
                    self.lstBoard[i][j] = ''

    def getSpotInfo(self,intX,intY):
        if intX < 0 or intY < 0 or intX >= self.intXSize or intY >= self.intYSize:
            return None
        return self.lstBoard[intY][intX]

    def __str__(self):
        strRet = "";
        for i in range(self.intYSize):
            for j in range(self.intXSize):
                if self.lstBoard[i][j] == '':
                    strRet = strRet + '_'
                else:
                    strRet = strRet + self.lstBoard[i][j]
            strRet = strRet + '\n'
        return strRet