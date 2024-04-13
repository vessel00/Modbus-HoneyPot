import json

def load_part_ssh(file_path):
    try:
        # 读取 config.json 文件的内容并将其存储为一个字典
        with open(file_path, 'r') as archive:
            config_dictionary = json.load(archive)

        # 检查加载的字典中是否存在 'ssh' 部分
        if "ssh" in config_dictionary:
            ssh_section = config_dictionary["ssh"]
            return ssh_section
        else:
            print("'ssh' section not found in the config file.")
            return None

    except FileNotFoundError:
        return None
    
def load_part_modbus(file_path):
    try:
        # 读取 config.json 文件的内容并将其存储为一个字典
        with open(file_path, 'r') as archive:
            config_dictionary = json.load(archive)

        # 检查加载的字典中是否存在 'modbus' 部分
        if "modbus" in config_dictionary:
            modbus_section = config_dictionary["modbus"]
            return modbus_section
        else:
            print("'modbus' section not found in the config file.")
            return None

    except FileNotFoundError:
        return None