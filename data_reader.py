# 导入必要的库
from torch.utils.data import Dataset  # 导入PyTorch中的Dataset类
from PIL import Image  # 导入PIL库用于图像处理
import os  # 导入os库用于操作系统相关功能

# 定义一个数据集类MyData，继承自Dataset
class MyData(Dataset):
    def __init__(self,root_dir,label_dir): #初始化类，为整个类提供全局变量
        # self指定的变量能给后面的函数（方法）使用，相当于全局变量，相当于这个定义类的属性
        self.root_dir = root_dir  # 保存根目录路径
        self.label_dir = label_dir  # 保存标签目录名称
        self.path = os.path.join(self.root_dir,self.label_dir)  # 拼接路径
        self.img_path = os.listdir(self.path)  # 将所传如的目录下的文件名制作成一个列表

    def __getitem__(self, idx): #获取数据集中的一个数据，根据列表中的位置可访问任意一个

        img_name = self.img_path[idx]  # 从图像路径列表中根据索引idx获取图像名称
        img_item_path = os.path.join(self.root_dir,self.label_dir,img_name) #获取图片路径
        img = Image.open(img_item_path) #打开图片
        label = self.label_dir
        return img,label

    def __len__(self):
        return len(self.img_path)

root_dir = "dataset/train"
ants_label_dir = "ants"
bees_label_dir = "bees"
# 创建数据集对象
ants_dataset = MyData(root_dir,ants_label_dir)
bees_dataset = MyData(root_dir,bees_label_dir)

img,label = ants_dataset[0]
img.show()
img,label = bees_dataset[0]
img.show()

train_dataset = ants_dataset + bees_dataset
print(len(train_dataset))
img,label = train_dataset[0]

img.show()
print(label)
print(len(train_dataset))
