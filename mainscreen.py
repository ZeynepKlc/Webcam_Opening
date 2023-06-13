import threading
import cv2


class windows:

    def __init__(self):
        self.window = None
        self.video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        operation1 = threading.Thread(target=self.video_showing, name="Operation_1", args=())
        operation1.daemon = True
        operation1.start()

    def video_showing(self):
        while 1:

            ret, self.window = self.video.read()

            cv2.imshow("First Screen", self.window)
            current_thread = threading.current_thread()
            print("Current thread:", current_thread.name)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.video.release()
        cv2.destroyAllWindows()