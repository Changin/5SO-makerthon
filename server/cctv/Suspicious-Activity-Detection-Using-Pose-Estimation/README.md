## :movie_camera: :running: :running: Suspicious-Activity-Detection-Using-Pose-Estimation

![ezgif com-optimize](https://user-images.githubusercontent.com/62059604/105457061-39df5500-5cac-11eb-94a7-0a6c56037175.gif)

## 📝 Description
- This implemantation is based on official **AlphaPose** Pose Estimation Algorithm.
- It is **‘AlphaPose’** & **‘XGBOOST’** based **“Suspicious-Activity-Detection-Using-Pose Estimation”** project.
- Purpose of this project is to make a system which can detect if someone is trying to Climb a house compound wall, Climbing on Fence, Climbing on gate & trying    to do some suspicious activity.
- This model will detect this activities accurately & helps to prevent those kind of activities by giving real time feedback.


## 🎯 Inference demo
![im1_HSP](https://user-images.githubusercontent.com/62059604/105394428-935f6980-5c43-11eb-8123-62c7aad4942d.png)
![img2_HSP](https://user-images.githubusercontent.com/62059604/105394453-9e19fe80-5c43-11eb-9867-40d165b75c1b.png)

## 🏽‍ Download Object Detection Model
- Download the object detection model manually : **yolov3-spp.weights** file from following Drive Link
- https://drive.google.com/file/d/1h2g_wQ270_pckpRCHJb9K78uDf-2PsPd/view?usp=sharing
- Download the weight file and Place it into **" detector/yolo/data/ "** folder.

##  🏽‍ For Pose Tracking, Download the object tracking model
- For pose tracking, download the object tracking model manually: **" JDE-1088x608-uncertainty "** from following Drive Link 
- https://drive.google.com/file/d/1oeK1aj9t7pTi1u70nSIwx0qNVWvEvRrf/view?usp=sharing
- Download the file and Place it into **" detector/tracker/data/ ".** folder.

## 🏽‍ Download Fast.res50.pt file
- Download the **" fast.res50.pth "** file from following Drive Link 
- https://drive.google.com/file/d/1WrvycZnVWwltSa6cjeTznEFOyNAwHEZu/view?usp=sharing
- Download the file and Place it into **" pretrained_models/ ".** folder.

## :desktop_computer:	Installation

### :hammer_and_wrench: Requirements
* Python 3.5+
* Cython
* PyTorch 1.1+
* torchvision 0.3.0+
* Linux
* GCC<6.0, check https://github.com/facebookresearch/maskrcnn-benchmark/issues/25

## :gear: Setup on Colab
1. Install PyTorch :-
```bash
$ !pip3 install torch==1.1.0 torchvision==0.3.0

```

2. Git Clone :-
```bash
$ !git clone https://github.com/akshaykadam771/Suspicious-Activity-Detection-Using-Pose-Estimation.git 

```

3. Install :-
```bash
$ !export PATH=/usr/local/cuda/bin/:$PATH

```
```bash
$ !export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH

```
```bash
$ !pip install cython

```
```bash
$ !sudo apt-get install libyaml-dev

```
```bash
$ !python setup.py build develop --user

```
```bash
$ !python -m pip install Pillow==6.2.1

```
```bash
$ !pip install -U PyYAML

```
## 🎯 Inference 
1. Testing with **Images** ( Put test images in **AlphaPose/examples/demo/** )  :-
```bash
$ !python scripts/demo_inference.py --cfg configs/coco/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/fast_res50_256x192.pth --indir examples/demo/ --save_img

```
2. Output Images & json file will save in bydefault **AlphaPose/examples/res** folder.

3. Testing with **Videos**  :-
```bash
$ !python scripts/demo_inference.py --cfg configs/coco/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/fast_res50_256x192.pth --video examples/video/demo5.mp4 --outdir examples/res --save_video --gpus 0

```
3. If it is giving memory error during **Videos** testing you can add  **--sp**  argument in command which enable Single processing :-
```bash
$ !python scripts/demo_inference.py --cfg configs/coco/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/fast_res50_256x192.pth --video examples/video/demo5.mp4 --outdir examples/res --save_video --gpus 0 --sp

```
## :open_file_folder: Json Dataset for training your own custom ML model :wrench: :nut_and_bolt: :hammer:	

- **Drive Link** :- https://drive.google.com/file/d/1sTJkWBmuE6iBi_mCAs1DJ-KR6MnoZD7-/view?usp=sharing
- This CSV file contaning 17 keypoints (Total 17x2=34 ) of Human body part as columns for each individual person while performing this 2 activities :-                **1) Climbing  2)Standing**
- **Action** :- 0 = Climbing & 1 = Standing
