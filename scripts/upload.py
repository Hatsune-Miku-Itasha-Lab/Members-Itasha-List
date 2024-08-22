import os

# 配置目录和文件
image_dir = 'docs/images'
output_dir = 'docs'
html_file = os.path.join(output_dir, 'index.html')
css_file = os.path.join(output_dir, 'styles.css')
js_file = os.path.join(output_dir, 'script.js')

# 获取所有图片文件
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpeg')]

# 解析文件名并生成HTML
html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>葱痛研车友名录</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <img src="logo.jpg" alt="Logo" id="logo">
        <img src="teaser.png" alt="Teaser" id="teaser">
    </header>
    <div class="filters">
        <!-- 筛选控件 -->
    </div>
    <div id="image-list">
'''

for image_file in image_files:
    # 提取文件名去掉扩展名
    file_name = os.path.splitext(image_file)[0]
    # 解析文件名
    cn, brand, type_, miku, year, remark = file_name.split('_')
    
    # 替换为0的元素为空白
    cn = cn if cn != '0' else ''
    brand = brand if brand != '0' else ''
    type_ = type_ if type_ != '0' else ''
    miku = miku if miku != '0' else ''
    year = year if year != '0' else ''
    remark = remark if remark != '0' else ''
    
    # 生成HTML内容
    html_content += f'''
        <div class="image-item">
            <img src="images/{image_file}" alt="{cn}">
            <div class="image-details">{cn} {brand} {type} {miku} {year} {remark}</div>
        </div>
    '''

html_content += '''
    </div>
    <div class="pagination">
        <button id="prev-btn" onclick="prevPage()">上一页</button>
        <span id="page-info"></span>
        <input type="number" id="page-input" min="1" max="totalPages" placeholder="页码">
        <button onclick="goToPage()">跳转</button>
        <button id="next-btn" onclick="nextPage()">下一页</button>
    </div>
    <script src="script.js"></script>
</body>
</html>
'''

# 写入HTML文件
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

# 生成CSS内容
css_content = '''
body {
    font-family: Arial, sans-serif;
}

#logo, #teaser {
    width: 100%;
    display: block;
    margin: 0 auto;
}

.image-item {
    margin-bottom: 20px;
    text-align: center;
}

.image-item img {
    max-width: 100%;
    height: auto;
}

.image-details {
    margin-top: 10px;
    font-size: 1.2rem;
    color: #333;
    white-space: pre-wrap;
}

.filters {
    margin-bottom: 20px;
    text-align: center;
}

.filters label {
    margin-right: 10px;
}

.filters select {
    margin-right: 20px;
    padding: 5px;
}

.pagination {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
}

.pagination input {
    width: 60px;
    padding: 5px;
    text-align: center;
}

.pagination button {
    padding: 10px 20px;
    background-color: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
}

.pagination button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
}

.pagination span {
    line-height: 35px;
}
'''

# 写入CSS文件
with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 生成JS内容
js_content = '''
const imagesPerPage = 20;
let currentPage = 1;
let totalPages = Math.ceil(document.querySelectorAll('.image-item').length / imagesPerPage);

function renderImages() {
    const imageList = document.getElementById('image-list');
    const items = imageList.querySelectorAll('.image-item');
    
    items.forEach((item, index) => {
        if (index >= (currentPage - 1) * imagesPerPage && index < currentPage * imagesPerPage) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });

    document.getElementById('page-info').textContent = `第 ${currentPage} 页，共 ${totalPages} 页`;
    document.getElementById('page-input').value = currentPage;

    document.getElementById('prev-btn').disabled = currentPage === 1;
    document.getElementById('next-btn').disabled = currentPage === totalPages;
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        renderImages();
    }
}

function nextPage() {
    if (currentPage < totalPages) {
        currentPage++;
        renderImages();
    }
}

function goToPage() {
    const pageInput = document.getElementById('page-input');
    let page = parseInt(pageInput.value);

    if (!isNaN(page) && page >= 1 && page <= totalPages) {
        currentPage = page;
        renderImages();
    } else {
        alert("请输入有效的页码！");
        pageInput.value = currentPage;
    }
}

// 初始化渲染
renderImages();
'''

# 写入JS文件
with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("HTML, CSS, and JS files have been generated successfully.")
