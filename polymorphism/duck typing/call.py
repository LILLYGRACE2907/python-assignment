class AndroidPhone:
    def call(self):
        print("Calling from Android phone")


class iPhone:
    def call(self):
        print("Calling from iPhone")


def make_call(phone):
    phone.call()


android = AndroidPhone()
iphone = iPhone()

make_call(android)
make_call(iphone)