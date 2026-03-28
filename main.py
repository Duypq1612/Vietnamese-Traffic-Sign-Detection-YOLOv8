from ultralytics import YOLO
import cv2

#1. Load model
print("Đang tải best.pt...")
model = YOLO("D:\SignTrafficRecognition\YOLO_output\checkpoints/best.pt") 

source_file = 'D:\SignTrafficRecognition\dataset/video_2.mp4' 

# 3. Inference
print(f"Đang phân tích {source_file}...")
results = model.predict(
    source=source_file, 
    show=True,       # Mở cửa sổ hiển thị kết quả trực tiếp
    save=True,       # Lưu lại ảnh/video đã vẽ khung vào ổ cứng
    conf=0.4,        # Độ tự tin: Chỉ vẽ khung khi AI chắc chắn trên 40%
    line_width=2     # Độ dày của khung vuông (pixel)
)

print("Kiểm tra thư mục runs/detect/predict ")