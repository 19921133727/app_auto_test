from base.base_action import BaseAction
import yaml

def readYaml(filepath):
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
        print(type(data))  # 打印data类型
        arr = data['test001']
        print(arr)




if __name__ == '__main__':
    readYaml("./text.yaml")