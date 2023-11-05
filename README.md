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

## Installation
<details close>
<summary>Install</summary>
Clone repo and install [requirements.txt](requirements.txt)

```bash
git clone https://github.com/amish0/Sort_tracking
cd Sort_tracking
pip install -r requirements.txt
```
</details>

## Example
<details close>
<summary>Example</summary>
<details close>
<summary>Sort tracking can be used as a standalone tracker.</summary> Please check the [Sort_cls.py](Sort_cls.py) for more details.

```bash

# import Sort
from Sort_cls import Sort

# Create an instance of the tracker
obj_tracker = Sort(max_age=1, min_hits=3, iou_threshold=0.3)

# get detections
dets = np.array([[0,0,10,10,0.9,1],[0,0,10,10,0.8,1],[0,0,10,10,0.7,1], ....]) 

# update tracker
tracking_results = obj_tracker.update(dets)

# print tracking results
print(tracking_results)
```
</details>

<details close>
<summary>Tracker class can be used to track the objects in a video.</summary> Please check the [tracker.py](tracker.py) for more details.

```bash
# import tracker
from tracker import Tracker

# Create an instance of tracker
tracker = Tracker(tracker_type = 'sort')

# detections result from object detector
dets = np.array([[0,0,10,10,0.9,1],[0,0,10,10,0.8,1],[0,0,10,10,0.7,1], ....])

# update tracker
tracking_results = tracker(dets)

# print tracking results
print(tracking_results)
```
</details>

<details close>
<summary>MuliCameraTracker class can be used to track the objects in a video.</summary> Please check the [tracker.py](tracker.py) for more details.

```bash
# import multi camera tracker
from tracker import MuliCameraTracker

# set of tracker id
track_id = {0, 1} # set of camera ids

# Create an instance of tracker
tracker = MuliCameraTracker(tracker_type = 'sort', track_id = track_id )

# detections result from each camera by a object detector
dets = {0: np.array([[0,0,10,10,0.9,1],[0,0,10,10,0.8,1],[0,0,10,10,0.7,1], ....]), 
        1: np.array([[0,0,10,10,0.9,1],[0,0,10,10,0.8,1],[0,0,10,10,0.7,1], ....])}

# update tracker
tracking_results = tracker(dets)

# print tracking results of camera id 0
print(tracking_results[0]) # tracking results of camera id 0
```
</details>
</details>

<details close>
<summary>Class Explanation</summary>

- `sort`: The class of the sort tracking. It will be initialized with `max_age`, `min_hits`, `iou_threshold` based on arguments. `update` method will with the detections parameters and return the tracking results. Please check the [sort.py](tracker/Sort/sort.py) for more details.
    - arguments:
        - dets - a numpy array of detections in the format `[[x1,y1,x2,y2,score, cls],[x1,y1,x2,y2,score, cls],...]`
    - returns:
        - Requires: this method must be called once for each frame even with empty detections (use np.`empty((0, 7))` for frames without detections).
        - Returns the a similar array, where the last column is the object ID. `[[x1,y1,x2,y2,score, cls, ID],[x1,y1,x2,y2,score, cls, ID],...]`

- `Tracker`: This class will initialize the tracker with the given tracker_type and tracker parameters from [corresponding yaml](tracker/Sort/sort.yaml) file. __call__ will take the detections and return the tracking results. Please check the [tracker.py](tracker/tracker.py) for more details.
    - arguments:
        - dets - a numpy array of detections in the format `[[x1,y1,x2,y2,score, cls],[x1,y1,x2,y2,score, cls],...]`
    - returns:
        - Requires: this method must be called once for each frame even with empty detections (use np.`empty((0, 7))` for frames without detections).
        - Returns the a similar array, where the last column is the object ID. `[[x1,y1,x2,y2,score, cls, ID],[x1,y1,x2,y2,score, cls, ID],...]`

- `MuliCameraTracker`:  This class will initialize the tracker with the given tracker_type, and a set of tracker id (each tracker id will be associated with each camera) and tracker parameters from [corresponding yaml](tracker/Sort/sort.yaml) file. __call__ will take the detections and return the tracking results. Please check the [tracker.py](tracker/tracker.py) for more details.
    - arguments:
        - dets - a dictionary of camera id and detections in the format `{camera\_id\_1: [[x1,y1,x2,y2,score, cls],[x1,y1,x2,y2,score, cls],...], camera_id_2: [[x1,y1,x2,y2,score, cls],[x1,y1,x2,y2,score, cls],...],...}`
        - track_id - a set of camera ids/tracker_id to be tracked `{camera\_id\_1, camera\_id\_2, ...}`
    - returns:
        - Requires: this method must be called once for each frame even with empty detections (use np.`empty((0, 7))` for frames without detections).
        - Returns the a dictionary of camera id and tracking results. `{camera\_id\_1: [[x1,y1,x2,y2,score, cls, ID],[x1,y1,x2,y2,score, cls, ID],...], camera\_id\_2: [[x1,y1,x2,y2,score, cls, ID],[x1,y1,x2,y2,score, cls, ID],...],...}$`
</details>

## Use in your own peoject
Below is the gist of how to instantiate and update the tracker. Please check the [tracker/tracker.py](tracker.py) for more details.
```bash

from tracker import Tracker
# Create an instance of tracker
tracker = Tracker(tracker_type = 'sort')
# get detections
...

# update SORT
track_bbs_conf_cls_ids = tracker(detections)

# track_bbs_conf_cls_ids is a np array where each row contains a valid bounding box, score, class and track_id (last column)
...
```

## Build setup
```
# Go to code directory
cd some_root_dir

# create build

python -m build
# or
# python setup.py sdist bdist_wheel
```
It will create build in your dist directory. if dist is not present it will create it.

## Install Packages
 
 if you have not made any build, please follow the command

 ```
 python setup.py install
 ```

 If build has been created, please follow the instruction below
 ```
 cd dist
 pip install package_name*.whl
 ```
 Please replace "package_name*.whl" with .whl file present in dist directory

<details open>
<summary>References</summary>
SORT: https://github.com/abewley/sort
</details>
