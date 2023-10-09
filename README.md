# Sort_tracking
The modified version of sort tracking (https://github.com/abewley/sort) compatible with the Yolo Series
## Directory structure
- sort_cls.py: The main file of the sort tracking with modification. sort will will be initialized with.max_age, min_hits, iou_threshold based on arguments. `update` method will with the detections parameters and return the tracking results.
    - arguments:
        - dets - a numpy array of detections in the format [[x1,y1,x2,y2,score, cls],[x1,y1,x2,y2,score, cls],...]
    - returns:
        - Requires: this method must be called once for each frame even with empty detections (use np.empty((0, 7)) for frames without detections).
        - Returns the a similar array, where the last column is the object ID. [[x1,y1,x2,y2,score, cls, ID],[x1,y1,x2,y2,score, cls, ID],...]
