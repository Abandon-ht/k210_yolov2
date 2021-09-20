# k210_yolov2
## Download dataset

```sh
wget https://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar
wget https://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar
wget https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar
tar xf VOCtrainval_11-May-2012.tar
tar xf VOCtrainval_06-Nov-2007.tar
tar xf VOCtest_06-Nov-2007.tar
wget https://pjreddie.com/media/files/voc_label.py
python3 voc_label.py
```
## Make dataset List

```sh
python3 make_voc_list.py train.txt
```

## Make Anchor List

First extract all annotations.

```sh
python3 get_all_annotations.py data/voc_ann.list
```

It will save all annotations to `tmp/all.txt`, Then use kmeans find the anchors:

```sh
python3 make_anchor_list.py tmp/all.txt data/voc_anchors.list
```
## Train VOC detection

```sh
make train MODEL=mobile_yolo MAXEP=50 ILR=0.0005 DATASET=voc CLSNUM=20 IAA=False CLASSIFIER=True BATCH=64
```

You can continue training

```sh
make train MODEL=mobile_yolo MAXEP=50 ILR=0.0005 DATASET=voc CLSNUM=20 IAA=True CLASSIFIER=False BATCH=64 CKPT=log/xxxxx
```

and you can use `tensorboard --logdir log` to look plot

## Freeze Graph

```sh
make freeze MODEL=mobile_yolo CKPT=log/xxxxxxx CLSNUM=20 DATASET=voc
```

now we have Freeze_save.pb

## Inferernce

```sh
make inference CLSNUM=20 IMG=JPEGImages/000007.jpg DATASET=voc
```

## Convert PB to tflite

```sh
python3 pb2tflite.py
```


## Convert tflite to kmodel

```sh
./ncc-linux-x86_64/ncc -i tflite -o k210model Freeze_save.tflite Freeze_save.kmodel --dataset JPEGImages
```
