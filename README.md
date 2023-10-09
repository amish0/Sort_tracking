# Sort_tracking
The modified version of sort tracking (https://github.com/abewley/sort) compatible with the Yolo Series
## Files
- [sort_cls.py](Sort_cls.py): The main file of the sort tracking with modification. sort will will be initialized with `max_age`, `min_hits`, `iou_threshold` based on arguments. `update` method will with the detections parameters and return the tracking results.
    - arguments:
        - dets - a numpy array of detections in the format [[x1,y1,x2,y2,score, cls],[x1,y1,x2,y2,score, cls],...]
    - returns:
        - Requires: this method must be called once for each frame even with empty detections (use np.empty((0, 7)) for frames without detections).
        - Returns the a similar array, where the last column is the object ID. [[x1,y1,x2,y2,score, cls, ID],[x1,y1,x2,y2,score, cls, ID],...]
- [utils.py](utils.py): conatins the functions `check_file()`: for checking file existence and `check_suffix()`: suffix of the file
- [loadyaml.py](loadyaml.py): contains the function `loadyaml()`: for loading the yaml file
- [tracker.py](tracker.py): main tracking file. It will load the sort_cls.py and use the update method to get the tracking results. please check class `Tracker` and `MuliCameraTracker` for more details.

<details open>
<summary>Install</summary>
Clone repo and install [requirements.txt](requirements.txt)

```bash
git clone https://github.com/amish0/Sort_tracking
cd Sort_tracking
pip install -r requirements.txt
```
</details>

<details open>
<summary>Example</summary>
<details open>
<summary>Sort tracking can be used as a standalone tracker.</summary> Please check the [Sort_cls.py](Sort_cls.py) for more details.

```bash
from Sort_cls import Sort
obj_tracker = Sort(max_age=1, min_hits=3, iou_threshold=0.3)
dets = np.array([[0,0,10,10,0.9,1],[0,0,10,10,0.8,1],[0,0,10,10,0.7,1], ....]) 
# dets = np.empty((0, 7)) # for empty detections
tracking_results = obj_tracker.update(dets)
print(tracking_results)
```
</details>

<details open>
<summary>Tracker class can be used to track the objects in a video.</summary> Please check the [tracker.py](tracker.py) for more details.

```bash
from tracker import Tracker
tracker = Tracker(tracker_type = 'sort')
dets = np.array([[0,0,10,10,0.9,1],[0,0,10,10,0.8,1],[0,0,10,10,0.7,1], ....])
tracking_results = tracker(dets)
print(tracking_results)
```
</details>

<details open>
<summary>MuliCameraTracker class can be used to track the objects in a video.</summary> Please check the [tracker.py](tracker.py) for more details.

```bash
from tracker import MuliCameraTracker
track_id = {0, 1} # set of camera ids
tracker = MuliCameraTracker(tracker_type = 'sort', track_id = track_id )
dets = {0: np.array([[0,0,10,10,0.9,1],[0,0,10,10,0.8,1],[0,0,10,10,0.7,1], ....]), 
        1: np.array([[0,0,10,10,0.9,1],[0,0,10,10,0.8,1],[0,0,10,10,0.7,1], ....])} # dictionary of camera id and detections
tracking_results = tracker(dets) # dictionary of camera id and tracking results
print(tracking_results[0]) # tracking results of camera id 0
```
</details>
</details>

<details open>
<summary>Class Explanation</summary>
- `sort`: The class of the sort tracking. It will be initialized with `max_age`, `min_hits`, `iou_threshold` based on arguments. `update` method will with the detections parameters and return the tracking results. Please check the [sort_cls.py](sort_cls) for more details.
    - arguments:
        - dets - a numpy array of detections in the format [[x1,y1,x2,y2,score, cls],[x1,y1,x2,y2,score, cls],...]
    - returns:
        - Requires: this method must be called once for each frame even with empty detections (use np.empty((0, 7)) for frames without detections).
        - Returns the a similar array, where the last column is the object ID. [[x1,y1,x2,y2,score, cls, ID],[x1,y1,x2,y2,score, cls, ID],...]

- `Tracker`: This class will initialize the tracker with the given tracker_type and tracker parameters from [corresponding yaml](sort.yaml) file. __call__ will take the detections and return the tracking results. Please check the [tracker.py](tracker.py) for more details.
    - arguments:
        - dets - a numpy array of detections in the format [[x1,y1,x2,y2,score, cls],[x1,y1,x2,y2,score, cls],...]
    - returns:
        - Requires: this method must be called once for each frame even with empty detections (use np.empty((0, 7)) for frames without detections).
        - Returns the a similar array, where the last column is the object ID. [[x1,y1,x2,y2,score, cls, ID],[x1,y1,x2,y2,score, cls, ID],...]

- `MuliCameraTracker`:  This class will initialize the tracker with the given tracker_type, and a set of tracker id (each tracker id will be associated with each camera) and tracker parameters from [corresponding yaml](sort.yaml) file. __call__ will take the detections and return the tracking results. Please check the [tracker.py](tracker.py) for more details.
    - arguments:
        - dets - a dictionary of camera id and detections in the format {camera_id: [[x1,y1,x2,y2,score, cls],[x1,y1,x2,y2,score, cls],...], camera_id: [[x1,y1,x2,y2,score, cls],[x1,y1,x2,y2,score, cls],...],...}
        - track_id - a set of camera ids/tracker_id
    - returns:
        - Requires: this method must be called once for each frame even with empty detections (use np.empty((0, 7)) for frames without detections).
        - Returns the a dictionary of camera id and tracking results. {camera_id: [[x1,y1,x2,y2,score, cls, ID],[x1,y1,x2,y2,score, cls, ID],...], camera_id: [[x1,y1,x2,y2,score, cls, ID],[x1,y1,x2,y2,score, cls, ID],...],...}
</details>

<details open>
<summary>References</summary>
SORT: https://github.com/abewley/sort
</details>
