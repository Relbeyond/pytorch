import os

root_dir = "dataset\\train"
target_dir = "ants_image"

img_path = os.listdir(os.path.join(root_dir, target_dir))   #将dataset\\train\\ants_image文件夹下所有文件名转化为列表存储在img_path中
label = target_dir.split('_')[0]                            #将target_dir中所存储的"ants_image"用_分开，取第0个元素  label = ants

out_dir = "ants_label"                                      #输出文件夹名

for img in img_path:                                        #img就是由低位到高位取出img_path列表里每一个数据
    file_name = img.split('.jpg')[0]                        #将img中的.jpg用空格分开，取第0个元素，即取文件名 如123.jpg取123
    file_path = os.path.join(root_dir,out_dir, "{}.txt".format(file_name))   #将root_dir,out_dir,file_name拼接起来，生成文件名，即dataset\\train\\ants_label\\123.txt
    with open(file_path, 'w') as f:                         #打开dataset\\train\\ants_label\\123.txt文件 ，如果不存在则创建
        f.write(label)                                      #将label所存储的ants写入文件中