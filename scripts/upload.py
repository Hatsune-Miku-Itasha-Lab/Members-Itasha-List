import os

# 指定 images 目录的路径
images_dir = 'images'

# 获取目录中的所有文件名
file_names = os.listdir(images_dir)

# 创建 HTML 文件并写入文件名
with open('test.html', 'w') as f:
    f.write('<html><body>\n')
    f.write('<h1>Image Files</h1>\n')
    f.write('<ul>\n')
    
    # 将每个文件名写入 HTML 列表
    for file_name in file_names:
        f.write(f'<li>{file_name}</li>\n')
    
    f.write('</ul>\n')
    f.write('</body></html>\n')

print("HTML file 'test.html' created successfully.")
