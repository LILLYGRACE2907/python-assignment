class OnlineCourse:
    def start(self):
        print("Online course started")


class OfflineCourse:
    def start(self):
        print("Offline course started")


def start_course(course):
    course.start()


online = OnlineCourse()
offline = OfflineCourse()

start_course(online)
start_course(offline)