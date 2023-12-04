import time
import jetson_utils
import jetson_inference
import threading
import queue
import csv


class ModelConfig:
    model_path = "/mnt/po/jetson-inference/data/networks/pothole_v1/ssd-mobilenet.onnx"
    label_path = "/mnt/po/jetson-inference/data/networks/pothole_v1/classes.txt"
    threshold = 0.5


class CameraConfig:
    width = 1280
    height = 720
    video_num = '/dev/video4'

def load_model(config):
    argv = ["--model="+config.model_path,
            "--labels="+config.label_path, "--input-blob=input_0",
            "--output-cvg=scores", "--output-bbox=boxes"]
    return jetson_inference.detectNet(argv=argv, threshold=config.threshold)

def load_camera(config):
    return jetson_utils.gstCamera(config.width, config.height, config.video_num)

def load_video(video_path):
    return jetson_utils.videoSource(video_path)

if __name__ == '__main__':
    model_config = ModelConfig
    video_path = '/mnt/test_videos/test1.mp4'
    net = load_model(config = model_config)
    # camera = load_camera(config=camera_config)
    video = load_video(video_path=video_path)
    display = jetson_utils.glDisplay()

    while display.IsOpen():
        img = video.Capture()
        detections = net.Detect(img)
        display.RenderOnce(img)
        display.SetTitle("dddd")