from First_try import screen2
import threading
import cv2
import time


class second_try:

    def __init__(self):

        operation3 = threading.Thread(target=self.window2, name="Operation_3", args=())
        operation3.start()

    def window2(self):

        while 1:

            try:
                cv2.imshow("Third Screen", screen2.window)
                time.sleep(3)
                current_thread = threading.current_thread()
                print("Current thread:", current_thread.name)

            except:
                print("Resize error! !")

            if cv2.waitKey(2) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()


screen3 = second_try()
