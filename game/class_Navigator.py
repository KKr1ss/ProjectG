class Navigator:
    current_location = ""
    current_label = ""

    def set_navigation_data(self, current_location, current_label):
        self.current_location = current_location
        self.current_label = current_label