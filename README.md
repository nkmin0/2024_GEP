# 2024_GEP

AI model for 2024 Chungbuk Science Exhibition

> with: [DuvIsaac](https://github.com/DuvIsaac/2024GEP)
> 
> If you want to try it, visit [this link](https://github.com/DuvIsaac/2024GEP)

## AI-Based Grilled Edibility Predictor Model (GEP Model)

This project introduces an AI model that analyzes images to determine the optimal timing to flip meat while grilling.  
Using YOLOv5 for object detection, the model classifies cooking stages based on visual changes and temperature.  
It helps users avoid overcooking by giving real-time feedback on meat doneness.  
Two model structures (GEP1 and GEP2) were tested: full image classification and a hybrid with regression.  
Achieved mAP 0.7+, confirming reliable prediction.  

## Code Overview

### `graph.ipynb`
Notebook for plotting graphs.

- `plot_r`: Used to plot a single graph.
- Functions above `plot_r`: Handle multiple plots and additional features.
- *Ignore everything below that.*

### `Img_extraction.py`
Extracts frames from a video at specific time intervals.

> Check the comments in the code

---

### `split_folder.py`
Splits images **with labels** into `train`, `test`, and `valid` sets based on a specified ratio.

> Check the comments in the code

### `split_files.py`
After splitting into `train`, `test`, and `valid`, this script separates image files and label files into corresponding folders.

### Other Scripts
Just read through them or check the filenames — they should be self-explanatory.

### Note
There’s **no script for generating the `data.yaml` file** — please create it manually.

---

## More Information

- `labels`: Contains all data (images + labels) in one place.
- `dataset`: Contains the split data (`train`, `test`, `valid`) used for model training.

### About `1234` and `123456789` folders

- `1234`: Used in the model submitted for the exhibition. Contains only classes 1 to 4.
- `123456789`: Contains all classes from 1 to 9.

### Class Meaning

| Class | Description            |
|-------|------------------------|
| 1     | Already flipped        |
| 2     | About to flip (1)      |
| 3     | Flipped (1)            |
| 4     | About to flip (2)      |
| 5     | Flipped (2)            |
| 6     | About to flip (3)      |
| 7     | Flipped (3)            |
| 8     | About to flip (4)      |
| 9     | Flipped (4 - Finished) |

---

###  Excluded Data

- `exp02_c3_0055` was excluded due to **blurry/shaky footage**.

