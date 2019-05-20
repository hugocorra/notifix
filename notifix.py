import sched, time
from win10toast import ToastNotifier

scheduler = sched.scheduler(time.time, time.sleep)
toaster = ToastNotifier()

def notify_postura():
    toaster.show_toast("POSTURA!!!",
                       "Como está sua postura?",
                       icon_path="accerciser.ico",
                       duration=5,
                       threaded=True)



if __name__ == "__main__":
    while True:
        scheduler.enter(5, 1, notify_postura, ())
        scheduler.run()
