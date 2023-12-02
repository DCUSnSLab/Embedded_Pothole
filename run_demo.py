import argparse
import ctypes
import sys
import copy
import numpy as np
import csv
import time
from datetime import date
import os
import shutil
import jetson_utils
import jetson_inference

# net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
net = jetson_inference.detectNet(argv=["--model=/home/snslab/po/jetson-inference/data/networks/mycustom/ssd-mobilenet.onnx", "--labels=/home/snslab/po/jetson-inference/data/networks/mycustom/classes.txt","--input-blob=input_0", "--output-cvg=scores", "--output-bbox=boxes"], threshold=0.5)
# net = jetson_inference.segNet("fcn-resnet18-cityscapes-1024x512")
# net = jetson_inference.detectNet("data/networks/mycustom/ssd-mobilenet.onnx", threshold=0.5)
# net = jetson_inference.detectNet("/home/snslab/po/jetson-inference//python/training/detection/ssd/models/ssd-inception-v2/ssd-mobilenet.onnx", threshold=0.5)
camera = jetson_utils.gstCamera(1280,720,'/dev/video4')
# load the object detection model

display = jetson_utils.glDisplay()

while display.IsOpen():
	img,width, height = camera.CaptureRGBA()
	detections = net.Detect(img,width,height)
	display.RenderOnce(img,width,height)
	display.SetTitle("dddd")
