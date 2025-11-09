from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(source="data/immages/test", save=True, imgsz=640, device="cpu")