from ultralytics import YOLO

model = YOLO("yolov8m.pt")

#model.predict(source="wick.jpeg", save=True, conf=0.5, save_txt=True)

model.predict(source="wick.mp4", save=False, conf=0.5, save_txt=False, show=True)