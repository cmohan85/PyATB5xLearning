class ExcelReader:
    @staticmethod
    def read_from_excel():
        print("Reading from excel")

class MYSQLDBConnection:
    @staticmethod
    def readyMYSQLFile():
        print("Reading from MySQL")

class TC1:
    def testccase(self):
        MYSQLDBConnection.readyMYSQLFile()
        ExcelReader.read_from_excel()

tc_obj = TC1()
tc_obj.testccase()