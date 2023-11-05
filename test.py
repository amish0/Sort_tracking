from tracker.tracker import Tracker
import numpy as np
object_tracker = Tracker('sort')
print("test case started")
print("test case 1")
test = object_tracker([[0.1, 0.2, 0.3, 0.4, 0.5, 0], [0.2, 0.3, 0.4, 0.5, 0.6, 1]])
for *xyxy, conf, cls, ID in test:
    print("xyxy: ", xyxy)
    print("conf: ", conf)
    print("cls: ", cls)
    print("ID: ", ID)
    print("\n")
print("test case ended")
