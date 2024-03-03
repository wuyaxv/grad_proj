# 用于记录日志
import logging
from datetime import datetime

# 定义不同级别对应的颜色转义码

COLOR_CODES = {
    'DEBUG': '\033[94m',  # 蓝色
    'INFO': '\033[92m',   # 绿色
    'WARNING': '\033[93m',  # 黄色
    'ERROR': '\033[91m',   # 红色
    'CRITICAL': '\033[95m'  # 紫色
}

RESET_CODE = '\033[0m'  # 重置颜色

def setup_logger(name, description=""):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler=None
    if not description:        # 设置是标准输出还是输出到日志文件
        handler = logging.StreamHandler()
    else:
        handler = logging.FileHandler(
                filename=datetime.now().strftime("%Y-%m-%d_%H-%M-%S-")+description+'.log',
                encoding="UTF-8"
                )
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

def log_message(logger, message, level='info'):
    color_code = COLOR_CODES.get(level.upper(), '')  # 获取对应级别的颜色码
    reset_code = RESET_CODE
    
    if color_code:
        message = f"{color_code}{message}{reset_code}"  # 添加颜色转义码
    
    if level.lower() == 'debug':
        logger.debug(message)
    elif level.lower() == 'info':
        logger.info(message)
    elif level.lower() == 'warning':
        logger.warning(message)
    elif level.lower() == 'error':
        logger.error(message)
    elif level.lower() == 'critical':
        logger.critical(message)
    else:
        print("Invalid log level provided.")

