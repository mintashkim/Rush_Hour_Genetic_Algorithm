from abc import *
from Car import Car
from Board import Board
import copy

class RushHourSolver:
    @abstractmethod
    def solve(self,objRushHour):
        pass

class SimpleSolver(RushHourSolver):

    def solve(self,objRushHour):
        self.printInfo(objRushHour.objBoard,objRushHour.lstCar)
        carID = objRushHour.dicCar.keys()
        direction = ['U', 'D', 'L', 'R']
        lstSolution = []
        objRoot = TreeNode(None,objRushHour,'','')
        queue = []
        seen = []
        queue.append(objRoot)

        while len(queue) != 0:
            parent = queue.pop(0)
            for car in objRushHour.lstCar:
                for dir in direction:
                    copy = parent.objRushHour.copy()
                    if copy.moveCar(car.strID, dir):
                        if not hash(str(copy.objBoard)) in seen:
                            child = TreeNode(parent, copy, car.strID, dir)
                            queue.append(child)
                            seen.append(hash(str(copy.objBoard)))
                            if copy.checkFinished():
                                queue.clear()
                                while child != objRoot:
                                    lstSolution.append([child.strCarID, child.strDirection])
                                    child = child.getParent()
                                lstSolution.reverse()
                                return lstSolution

    def printInfo(self,objBoard,lstCar):
        strRet = "----------------------------\n"
        strRet = strRet + "Board : \n"
        strRet = strRet + str(objBoard) + "\n"
        strRet = strRet + "Cars : \n"
        for i in range(len(lstCar)):
            strRet = strRet + str(lstCar[i]) + "\n"
        print(strRet)

class TreeNode:

    def __init__(self,objParent,objRushHour,strCarID,strDirection):
        self.objParent = objParent
        self.objRushHour = objRushHour
        self.strCarID = strCarID
        self.strDirection = strDirection

    def getParent(self):
        return self.objParent