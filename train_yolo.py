from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

results = model.predict(
    source="data/images/test",
    save=True,
    imgsz=640,
    device="cpu",
    classes=[7]  
)