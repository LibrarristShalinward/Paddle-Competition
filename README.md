# while True: 卷
# &emsp; Y.O.L.O!
<br><br><br>



## 项目介绍：
&emsp; 本仓库为“while True: 卷”队完成飞桨论文复现挑战赛（第四期）中论文#12所使用的仓库

### 论文标题：
#12 YOLOv4: Optimal Speed and Accuracy of Object Detection :star::star::star::star:

### 论文摘要：
There are a huge number of features which are said to improve Convolutional Neural Network (CNN) accuracy. Practical testing of combinations of such features on large datasets, and theoretical justification of the result, is required. Some features operate on certain models exclusively and for certain problems exclusively, or only for small-scale datasets; while some features, such as batch-normalization and residual-connections, are applicable to the majority of models, tasks, and datasets. We assume that such universal features include Weighted-Residual-Connections (WRC), Cross-Stage-Partial-connections (CSP), Cross mini-Batch Normalization (CmBN), Self-adversarial-training (SAT) and Mish-activation. We use new features: WRC, CSP, CmBN, SAT, Mish activation, Mosaic data augmentation, CmBN, DropBlock regularization, and CIoU loss, and combine some of them to achieve state-of-the-art results: 43.5% AP (65.7% AP50) for the MS COCO dataset at a realtime speed of ∼65 FPS on Tesla V100. Source code is at https://github.com/AlexeyAB/darknet.

### 论文内容概述：
基于CNN通用特征的YOLO优化
