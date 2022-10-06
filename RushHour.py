from Car import Car
from Board import Board
from RushHourSolver import SimpleSolver
import csv
import time

class RushHour:

    def __init__(self,objRushHour=None,strSettingFile=None,objSolver=None):
        if strSettingFile is not None:
            objFile = open(strSettingFile,newline='')
            objReader = csv.reader(objFile,delimiter=',')
            self.lstCar = []
            self.dicCar = {}
            for lstRow in objReader:
                if lstRow[0] == 'intXSize':
                    self.intXSize = int(lstRow[1])
                elif lstRow[0] == 'intYSize':
                    self.intYSize = int(lstRow[1])
                else:
                    objCar = Car(int(lstRow[1]),int(lstRow[2]),lstRow[0],int(lstRow[3]),int(lstRow[4]))
                    self.lstCar.append(objCar)
                    self.dicCar[objCar.strID] = objCar
            self.objBoard = Board(self.intYSize,self.intXSize,self.lstCar)
            self.intTurn = 0
            self.objSolver = objSolver
        elif objRushHour is not None:
            self.lstCar = []
            self.dicCar = {}
            for i in range(len(objRushHour.lstCar)):
                objSourceCar = objRushHour.lstCar[i]
                objCar = Car(objSourceCar.intY,objSourceCar.intX,objSourceCar.strID,\
                             objSourceCar.intSize,objSourceCar.intOrient)
                self.lstCar.append(objCar)
                self.dicCar[objCar.strID] = objCar
            self.intXSize = objRushHour.intXSize
            self.intYSize = objRushHour.intYSize
            self.objBoard = Board(objRushHour.intYSize,objRushHour.intXSize,self.lstCar)
            self.intTurn = objRushHour.intTurn
            self.objSolver = objRushHour.objSolver

    def copy(self):
        return RushHour(objRushHour=self)

    def __str__(self):
        strRet = "----------------------------\n"
        strRet = strRet + "Turn : "+str(self.intTurn)+"\n"
        strRet = strRet + "Board : \n"
        strRet = strRet + str(self.objBoard) + "\n"
        strRet = strRet + "Cars : \n"
        for i in range(len(self.lstCar)):
            strRet = strRet + str(self.lstCar[i]) + "\n"
        return strRet

    def moveCar(self,strCarID,strDirection):
        objCar = self.dicCar[strCarID]
        if strDirection == 'U':
            return objCar.moveUp(self.objBoard)
        if strDirection == 'D':
            return objCar.moveDown(self.objBoard)
        if strDirection == 'L':
            return objCar.moveLeft(self.objBoard)
        if strDirection == 'R':
            return objCar.moveRight(self.objBoard)

    def play(self):
        dblStartTime = time.time()
        lstSolution = self.objSolver.solve(self)
        dblEndTime = time.time()
        for i in range(len(lstSolution)):
            self.moveCar(lstSolution[i][0],lstSolution[i][1])
            self.intTurn = self.intTurn + 1
            print("----------------------------\n")
            print("Turn : "+str(self.intTurn))
            print("Action : "+str(lstSolution[i]))
            print(str(self.objBoard))
        print("----------------------------\n")
        print("Final Turn : "+str(self.intTurn))
        print("Final Finish Check : " + str(self.checkFinished()))
        print("Elapsed Time for Solver : "+str(dblEndTime-dblStartTime))

    def checkFinished(self):
        objXCar = self.dicCar['X']
        if objXCar.intX == 4 and objXCar.intY == 2:
            return True
        else:
            return False