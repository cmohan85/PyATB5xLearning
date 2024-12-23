class BaseTest:
    def open_browser(self):
        print("Starting the browser")

    def read_from_excel(self):
        print("Read from Excel")

    def close_browser(self):
        print("Close the browser")

class TestCase1(BaseTest):
    def test_positive(self):
        self.open_browser()
        print("This is positive testcase1")
        self.read_from_excel()
        self.close_browser()
    def test_negative(self):
        self.open_browser()
        self.read_from_excel()
        print("This is negative testcase1")
        self.close_browser()

class TestCase2(BaseTest):
    def test_positive(self):
        self.open_browser()
        print("This is positive testcase2")
        self.close_browser()
    def test_negative(self):
        self.open_browser()
        print("This is negative testcase2")
        self.close_browser()