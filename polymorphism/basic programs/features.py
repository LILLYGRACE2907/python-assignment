class Android:
    def show_features(self):
        print("Android: Customizable and supports many apps")


class iPhone:
    def show_features(self):
        print("iPhone: iOS and strong security")


class WindowsPhone:
    def show_features(self):
        print("Windows Phone: Windows-based interface")


phones = [Android(), iPhone(), WindowsPhone()]

for phone in phones:
    phone.show_features()