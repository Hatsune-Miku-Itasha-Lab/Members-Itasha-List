// script.js
const images = [
    {
        url: `images/曉风殘刖_斯巴鲁_傲虎_樱未来_0_0.jpeg`,
        name: `曉风殘刖_斯巴鲁_傲虎_樱未来_0_0`
    }, 
    {
        url: `images/花甲粉_大众_cc_雪未来_2017_0.jpeg`,
        name: `花甲粉_大众_cc_雪未来_2017_0`
    }, 
]; 

for (let i = 1; i <= 298; i++) {
    images.push({
        url: `images/image${i}.jpg`,
        name: `图片 ${i}`  // 你可以根据实际需要设置图片的名字
    });
}

const imagesPerPage = 20;
let currentPage = 1;
const totalPages = Math.ceil(images.length / imagesPerPage);

function renderImages() {
    const imageList = document.getElementById('image-list');
    imageList.innerHTML = ''; 

    const startIndex = (currentPage - 1) * imagesPerPage;
    const endIndex = startIndex + imagesPerPage;
    const currentImages = images.slice(startIndex, endIndex);

    currentImages.forEach(image => {
        const imageItem = document.createElement('div');
        imageItem.className = 'image-item';

        const imgElement = document.createElement('img');
        imgElement.src = image.url;
        imageItem.appendChild(imgElement);

        const imageName = document.createElement('div');
        imageName.className = 'image-name';
        imageName.textContent = image.name;
        imageItem.appendChild(imageName);

        imageList.appendChild(imageItem);
    });

    document.getElementById('page-info').textContent = `第 ${currentPage} 页，共 ${totalPages} 页`;

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

renderImages();
