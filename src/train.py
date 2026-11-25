from ultralytics import YOLO


def main():
    model = YOLO("yolo26s.pt")
    model.train(
        data="configs/drone.yaml",
        epochs=50,
        imgsz=960,
        project="runs",
        name="yolo26s_960_with_cocco",
    )


if __name__ == "__main__":
    main()
