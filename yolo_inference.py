from ultralytics import YOLO

model = YOLO('models/last.pt')


model.track('input_video.mp4',conf=0.2,save=True)