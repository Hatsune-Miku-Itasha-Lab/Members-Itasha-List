
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
