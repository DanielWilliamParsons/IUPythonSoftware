import Controller as C

def main():
    controller = C.Controller()
    pathToData = ""
    nameForData = ""
    controller.uploadData("./data/Advertising.csv", nameForData)
    controller.loadDataToMemory()
    controller.visualizeData("lineChartr")
    controller.selectIdealFunction()
    controller.categorizeTestData()

if __name__ == '__main__':
    main()