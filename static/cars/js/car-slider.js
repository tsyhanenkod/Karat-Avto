document.addEventListener("DOMContentLoaded", function(event) {
  let thumbnails = document.getElementsByClassName('car-gallery-img');
  let activeImages = document.getElementsByClassName('active');
  let buttonRight = document.getElementById('slideRight');
  let buttonLeft = document.getElementById('slideLeft');
  let slider = document.getElementById('slider');
  let touchstartX = 0;
  let touchendX = 0;

  // Add click event listener to thumbnails
  for (let i = 0; i < thumbnails.length; i++) {
    thumbnails[i].addEventListener('click', function() {
      if (activeImages.length > 0) {
        activeImages[0].classList.remove('active');
      }
      this.classList.add('active');
      document.getElementById('featured').src = this.src;
      centerActiveImage();
    });
  }

  // Add click event listeners to slider navigation buttons
  buttonLeft.addEventListener('click', function() {
    slider.scrollLeft -= 180;
  });

  buttonRight.addEventListener('click', function() {
    slider.scrollLeft += 180;
  });

  // Add touch event listeners to slider
  slider.addEventListener('touchstart', function(event) {
    touchstartX = event.changedTouches[0].screenX;
  }, { passive: true });

  slider.addEventListener('touchend', function(event) {
    touchendX = event.changedTouches[0].screenX;
    handleSwipe();
  });

  // Handle swipe direction based on touchstart and touchend positions
  function handleSwipe() {
    if (touchendX < touchstartX) {
      slider.scrollLeft += 180;
    } else if (touchendX > touchstartX) {
      slider.scrollLeft -= 180;
    }
  }

  // Center the active image in the slider
  function centerActiveImage() {
    let activeImage = document.getElementsByClassName('active')[0];
    let gallery = document.querySelector('.car-gallery');
    let galleryWidth = gallery.offsetWidth;
    let activeImagePosition = activeImage.offsetLeft;
    let activeImageWidth = activeImage.offsetWidth;
    let scrollOffset = activeImagePosition - (galleryWidth - activeImageWidth) / 2;
    gallery.scrollLeft = scrollOffset;

    // Прокрутка активного изображения в область видимости
    activeImage.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
  }
});