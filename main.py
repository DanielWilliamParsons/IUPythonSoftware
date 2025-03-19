import Controller as C

def main():
    controller = C.Controller()
    pathToData = ""
    nameForData = ""
    controller.uploadData("./data/Advertising.csv", nameForData)
    controller.visualizeData("lineChartr")
    controller.selectIdealFunction()
    controller.runEvaluation

if __name__ == '__main__':
    main()