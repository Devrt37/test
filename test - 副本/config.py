"""银行卡卡号识别系统 — 全局配置参数"""


class PipelineConfig:
    """所有可调参数集中管理"""

    # --- 模板 ---
    TEMPLATE_WIDTH = 40
    TEMPLATE_HEIGHT = 60
    TEMPLATE_FONT_SIZE = 42

    # --- 预处理 ---
    BLUR_KSIZE = (3, 3)
    ADAPTIVE_BLOCK = 11
    ADAPTIVE_C = 2
    MORPH_CLOSE_KSIZE = (2, 2)
    MORPH_OPEN_KSIZE = (2, 2)

    # --- 卡号区域检测 ---
    MORPH_DETECT_KSIZE = (55, 7)       # 水平核，融合数字组
    MIN_CONTOUR_AREA = 500
    MIN_ASPECT_RATIO = 2.0             # 文字块宽高比下限
    MAX_ASPECT_RATIO = 20.0            # 文字块宽高比上限
    MIN_FILL_RATIO = 0.2               # 轮廓填充率下限
    ROI_PAD = 5                        # ROI 扩展像素

    # --- 字符分割 ---
    PROJ_SMOOTH_SIGMA = 2.0            # 投影曲线高斯平滑
    PROJ_THRESH_FACTOR = 0.15          # 谷值阈值 = 均值 × 此系数
    MIN_GAP_WIDTH = 2                  # 字符间最小间隙（像素）
    MIN_DIGIT_WIDTH = 5
    MAX_DIGIT_WIDTH = 80
    MIN_DIGIT_HEIGHT = 15
    MAX_DIGIT_HEIGHT = 90
    DIGIT_PAD_RATIO = 0.1              # 字符居中时边框比例
    MIN_DIGITS = 13
    MAX_DIGITS = 19

    # --- 识别 ---
    MATCH_THRESHOLD = 0.40             # 模板匹配置信度阈值
    TESSERACT_PSM = 7                  # 单行文本模式
    TESSERACT_WHITELIST = "0123456789"
