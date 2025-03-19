import Controller as C

def main():
    controller = C.Controller()
    pathToData = ""
    # Upload the ideal functions data
    nameForData = "ideal"
    controller.uploadData("./data/Advertising.csv", nameForData)
    # Upload the training data
    nameForData = "training"
    controller.uploadData("./data/Advertising.csv", nameForData)
    # Upload the test data
    nameForData = "test"
    controller.uploadData("./data/Advertising.csv", nameForData)

    # Now load the data from the SQL tables into memory
    controller.loadDataToMemory()

    # Run the function to select the ideal function
    controller.selectIdealFunction()

    # Run the function to categorize the test data
    controller.categorizeTestData()

    # Run the function to visualize the data
    controller.visualizeData("scatter")

if __name__ == '__main__':
    main()