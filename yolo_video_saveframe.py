
from yolo_saveframe import YOLO
from yolo_saveframe import detect_video



if __name__ == '__main__':
    video_path='path2your-video'
    yolo = YOLO()
    #detect_img(yolo)
    detect_video(yolo,video_path)
