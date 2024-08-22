import os

images_dir = 'docs/images'
# base_lines = [
#     "const imagesPerPage = 20;", 
#     "let currentPage = 1;", 
#     "const totalPages = Math.ceil(images.length / imagesPerPage);", 
#     "function renderImages() {", 
#     "    const imageList = document.getElementById('image-list');", 
#     "    imageList.innerHTML = ''; // 清空当前页面的图片", 
#     "    const startIndex = (currentPage - 1) * imagesPerPage;", 
#     "    const endIndex = startIndex + imagesPerPage;", 
#     "    const currentImages = images.slice(startIndex, endIndex);", 
#     "    currentImages.forEach(image => {", 
#     "        const imgElement = document.createElement('img');", 
#     "        imgElement.src = image;", 
#     "        imageList.appendChild(imgElement);", 
#     "    });", 
#     "    document.getElementById('page-info').textContent = `第 ${currentPage} 页，共 ${totalPages} 页`;", 
#     "    // 设置按钮状态", 
#     "    document.getElementById('prev-btn').disabled = currentPage === 1;", 
#     "    document.getElementById('next-btn').disabled = currentPage === totalPages;", 
#     "}", 
#     "function prevPage() {", 
#     "    if (currentPage > 1) {", 
#     "        currentPage--;", 
#     "        renderImages();", 
#     "    }", 
#     "}", 
#     "function nextPage() {", 
#     "    if (currentPage < totalPages) {", 
#     "        currentPage++;", 
#     "        renderImages();", 
#     "    }", 
#     "}", 
#     "// 初始渲染", 
#     "renderImages();", 
# ]

# with open('docs/'script.js', 'w') as f:
#     f.write('// script.js\n')
#     f.write('const images = [\n')
#     for file_name in os.listdir(images_dir):
#         file_name = os.path.join(file_name, images_dir)
#         f.write(f"'{file_name}', \n")
#     f.write('];\n')
#     file.writelines(base_lines)

print("js file 'docs/script.js' created successfully.")
