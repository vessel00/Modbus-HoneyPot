import os
import sys


ACTUAL_PATH = os.getcwd()  # 当前路径，也是配置文件路径
CONFIG_FILE = os.path.join(ACTUAL_PATH, "../../../", "config.json")
CONFIG_FILE = os.path.normpath(CONFIG_FILE)

def get_path_from_config_converted(label):
    # 获取源代码路径
    src_path = os.path.normpath(os.path.join(ACTUAL_PATH, '..'))
    sys.path.append(src_path)
    from configuration.load_config import load_part_modbus
    modbus_dict = load_part_modbus(CONFIG_FILE)
    
    if label in modbus_dict:
        path_from_config = modbus_dict[label]

        # 检查是否为整数类型
        if isinstance(path_from_config, int):
            converted_path = path_from_config
        # 检查是否为路径
        elif '/' in path_from_config:
            initial_path = ACTUAL_PATH.split("src/")[0]
            converted_path = str(initial_path) + path_from_config
        # 默认为字符串类型
        else: 
            converted_path = path_from_config
    else:
        raise KeyError(f"'{label}' 在配置中未找到.")
    
    return converted_path