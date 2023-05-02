const button = document.querySelectorAll('.offer-button');
const modal = document.querySelector('.modal-w');

modal.style.cssText = `
    display: flex;
    visibility: hidden;
    opacity: 0;
    transition: all .3s ease-in-out;
`;

// close modal
const closeModal = event => {
    const target = event.target;
    if (target === modal || target.closest('.modal-close')) {
        modal.style.opacity = 0;
        setTimeout(() => {
            modal.style.visibility = 'hidden';
        }, 300)
    }

};

// open modal
const openModal = () => {
    modal.style.visibility = 'visible';
    modal.style.opacity = 1;
};


button.forEach(btn => {
    btn.addEventListener('click', openModal);
})

modal.addEventListener('click', closeModal);

// success
const sendButton = document.querySelector('.send-btn')
const sendSuccess = () => {
    document.

    alert("Заявку надіслано успішно!")
}

sendButton.addEventListener('click', sendSuccess);
