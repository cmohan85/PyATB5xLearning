from abc import ABC, abstractmethod

class ExcelReader(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass


class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass
    @abstractmethod
    def stopBrowser(self):
        pass


class TC1(Browser):
    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("readFromExcel is Ready")

    def runTc(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()

tc_obj = TC1()
tc_obj.runTc()

