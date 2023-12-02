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
import threading
import queue
import csv
from datetime import date
def export_to_excel(q):
    now = time.localtime()
    while True:
        if not q.empty():
            data = q.get()
            with open('detections.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                # writer.writerows(str(float(data.Confidence)))
                # writer.writerows("%04d/%02d/%02d %02d:%02d:%02d" % (
	            #     now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
                writer.writerow([str(float(data.Confidence)),"%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)])
                # print(str(float(data.Confidence)))



# net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
net = jetson_inference.detectNet(argv=["--model=/home/snslab/po/jetson-inference/data/networks/pothole_v1/ssd-mobilenet.onnx", "--labels=/home/snslab/po/jetson-inference/data/networks/pothole_v1/classes.txt","--input-blob=input_0", "--output-cvg=scores", "--output-bbox=boxes"], threshold=0.5)
# net = jetson_inference.segNet("fcn-resnet18-cityscapes-1024x512")
# net = jetson_inference.detectNet("data/networks/mycustom/ssd-mobilenet.onnx", threshold=0.5)
# net = jetson_inference.detectNet("/home/snslab/po/jetson-inference//python/training/detection/ssd/models/ssd-inception-v2/ssd-mobilenet.onnx", threshold=0.5)
camera = jetson_utils.gstCamera(1280,720,'/dev/video4')
# load the object detection model
data_queue = queue.Queue()

excel_thread = threading.Thread(target=export_to_excel, args=(data_queue,))
excel_thread.start()
display = jetson_utils.glDisplay()

while display.IsOpen():
	img,width, height = camera.CaptureRGBA()
	detections = net.Detect(img,width,height)
	for data in detections:
		for data in detections:
			data_queue.put(data)
			# exit()
	display.RenderOnce(img,width,height)
	display.SetTitle("dddd")

