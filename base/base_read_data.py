import yaml

def readYaml(filepath):
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
        # print(type(data))  # 打印data类型
        # print(data)  # 打印data返回值


        return data