import yaml

import ocr


def get_yaml_data(yaml_file):
    # 打开yaml文件
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    # 将字符串转化为字典或列表
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data


def image2excel(pic_path):
    config = get_yaml_data("config.yml")

    # 使用ocr进行转换
    trans = ocr.OCR()
    path_excel = trans.img_to_excel(
        pic_path,
        image_path=pic_path,
        secret_id=config['secret_id'],
        secret_key=config['secret_key'],
    )
    return path_excel


if __name__ == '__main__':
    _pic_path = 'classTable.png'
    image2excel(_pic_path)
