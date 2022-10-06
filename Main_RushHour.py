from RushHour import RushHour
from RushHourSolver import SimpleSolver

if __name__ == "__main__":
    strSettingFile = 'Setting-Easiest.csv'
    # strSettingFile = 'Setting-Easy.csv'
    # strSettingFile = 'Setting-Intermediate.csv'
    # strSettingFile = 'Setting-Hard.csv'
    # strSettingFile = 'Setting-Hidden.csv'
    objSimpleSolver = SimpleSolver()
    objGame = RushHour(strSettingFile=strSettingFile,objSolver=objSimpleSolver)
    objGame.play()

