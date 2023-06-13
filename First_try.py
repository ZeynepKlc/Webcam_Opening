import time
import mainscreen
import threading
import cv2
import traceback


class first_try:

    def __init__(self):
        operation2 = threading.Thread(target=self.window1, name="Operation_2", args=())
        operation2.daemon = True
        operation2.start()

    def window1(self):

        while 1:
            try:
                cv2.imshow("Second Screen", screen2.window)
                time.sleep(1)
                current_thread = threading.current_thread()
                print("Current thread:", current_thread.name)

            except Exception as e:
                error_mes = traceback.format_exc()
                print(f"Error occured\n {error_mes}")
                print("----------------------")

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cv2.destroyAllWindows()


screen2 = mainscreen.windows()
trying = first_try()

