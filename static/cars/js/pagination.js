function updatePaginationLinks(currentPage, totalPages) {
  const paginationEl = document.querySelector('.pagination');

  paginationEl.innerHTML = '';

  const prevPageEl = createPaginationLink(currentPage - 1, '&laquo;');
  paginationEl.appendChild(prevPageEl);

  for (let i = 1; i <= totalPages; i++) {
    const pageEl = createPaginationLink(i, i, currentPage === i);
    paginationEl.appendChild(pageEl);
  }

  const nextPageEl = createPaginationLink(currentPage + 1, '&raquo;');
  paginationEl.appendChild(nextPageEl);
}

function createPaginationLink(pageNumber, text, isCurrentPage = false) {
  const linkEl = document.createElement('a');
  linkEl.classList.add('page-link');
  linkEl.href = '?page=' + pageNumber;
  linkEl.innerHTML = text;

  const pageEl = document.createElement('li');
  pageEl.classList.add('page-item');
  if (isCurrentPage) {
    pageEl.classList.add('active');
  }
  pageEl.appendChild(linkEl);

  return pageEl;
}

// Example usage:
const currentPage = 1;
const totalPages = 5;
updatePaginationLinks(currentPage, totalPages);