import cv2
import pytesseract
import os

# Tesseract 配置
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

# ====================== 主程序 ======================
image_path = "card.png"  # 你的银行卡图片
img = cv2.imread(image_path)

# 【超级精准】直接截取你这张卡卡号所在区域（根据你这张图）
h, w = img.shape[:2]
y1 = int(h * 0.70)
y2 = int(h * 0.82)
x1 = 0
x2 = int(w * 0.95)
roi = img[y1:y2, x1:x2]

# 超强预处理（专门对付银行卡）
gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 3)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# 识别（只认数字！）
config = r'--psm 12 --oem 3 -c tessedit_char_whitelist=0123456789'
result = pytesseract.image_to_string(thresh, config=config)
digits = ''.join(c for c in result if c.isdigit())

# 输出
print("\n===== 银行卡号识别结果 =====")
print("完整卡号：", digits)
print("格式化：", " ".join([digits[i:i+4] for i in range(0, len(digits), 4)]))
print("===========================\n")