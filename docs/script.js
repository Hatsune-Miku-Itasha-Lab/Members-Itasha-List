// script.js
const images = []; // 这里可以放入300张图片的URL地址，例如：'image1.jpg', 'image2.jpg', ...

// 生成模拟数据
for (let i = 1; i <= 300; i++) {
    images.push(`image${i}.jpg`);
}

const imagesPerPage = 20;
let currentPage = 1;
const totalPages = Math.ceil(images.length / imagesPerPage);

function renderImages() {
    const imageList = document.getElementById('image-list');
    imageList.innerHTML = ''; // 清空当前页面的图片

    const startIndex = (currentPage - 1) * imagesPerPage;
    const endIndex = startIndex + imagesPerPage;
    const currentImages = images.slice(startIndex, endIndex);

    currentImages.forEach(image => {
        const imgElement = document.createElement('img');
        imgElement.src = image;
        imageList.appendChild(imgElement);
    });

    document.getElementById('page-info').textContent = `第 ${currentPage} 页，共 ${totalPages} 页`;

    // 设置按钮状态
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

// 初始渲染
renderImages();
