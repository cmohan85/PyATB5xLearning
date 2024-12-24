class OldBrowser:
    def start_browser(self):
        print("IE browser is starting")

    def stop_browser(self):
        print("IE browser is Closing")

class Chrom(OldBrowser):

    def start_browser(self):
        super().start_browser() # TO start Parent browser also
        print("better chrome browser is starting")

    def stop_browser(self):
        super().stop_browser()
        print("better chrome browser is stopping")


obj_ref = Chrom()
obj_ref.start_browser()
obj_ref.stop_browser()