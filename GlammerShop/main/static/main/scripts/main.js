let currentSlideIndexes = [0, 0];
let startX;
let isSwiping = false;
let slideIntervals = [];

function showSlide(sliderIndex, slideIndex) {
    const slider = document.getElementById(`slider${sliderIndex}`);
    const slides = slider.querySelector('.slides');
    const dots = slider.querySelectorAll('.dot');
    const totalSlides = slider.querySelectorAll('.slide').length;

    if (slideIndex >= totalSlides) {
        currentSlideIndexes[sliderIndex - 1] = 0;
    } else if (slideIndex < 0) {
        currentSlideIndexes[sliderIndex - 1] = totalSlides - 1;
    } else {
        currentSlideIndexes[sliderIndex - 1] = slideIndex;
    }

    slides.style.transform = `translateX(-${currentSlideIndexes[sliderIndex - 1] * 100}%)`;

    dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === currentSlideIndexes[sliderIndex - 1]);
    });

    resetSlideInterval(sliderIndex);  // Reset the interval whenever the slide changes
}

function nextSlide(sliderIndex) {
    showSlide(sliderIndex, currentSlideIndexes[sliderIndex - 1] + 1);
}

function prevSlide(sliderIndex) {
    showSlide(sliderIndex, currentSlideIndexes[sliderIndex - 1] - 1);
}

function currentSlide(sliderIndex, slideIndex) {
    showSlide(sliderIndex, slideIndex);
}

function handleTouchStart(event) {
    startX = event.touches[0].clientX;
    isSwiping = true;
}

function handleTouchMove(event) {
    if (!isSwiping) return;
    const currentX = event.touches[0].clientX;
    const diffX = startX - currentX;
    const sliderElement = event.target.closest('.slider');

    if (!sliderElement) return; // Check if sliderElement is found

    const sliderId = sliderElement.id;

    if (diffX > 50) {
        if (sliderId === 'slider1') {
            nextSlide(1);
        } else if (sliderId === 'slider2') {
            nextSlide(2);
        }
        isSwiping = false;
    } else if (diffX < -50) {
        if (sliderId === 'slider1') {
            prevSlide(1);
        } else if (sliderId === 'slider2') {
            prevSlide(2);
        }
        isSwiping = false;
    }
}

function handleTouchEnd() {
    isSwiping = false;
}

function resetSlideInterval(sliderIndex) {
    if (slideIntervals[sliderIndex - 1]) {
        clearInterval(slideIntervals[sliderIndex - 1]);
    }
    slideIntervals[sliderIndex - 1] = setInterval(() => nextSlide(sliderIndex), 15000);
}

// Автоматическое перелистывание каждые 15 секунд для каждого слайдера
resetSlideInterval(1);
resetSlideInterval(2);

// Инициализация слайдера
showSlide(1, currentSlideIndexes[0]);
showSlide(2, currentSlideIndexes[1]);

const slider1 = document.getElementById('slider1');
slider1.addEventListener('touchstart', handleTouchStart, { passive: true });
slider1.addEventListener('touchmove', handleTouchMove, { passive: true });
slider1.addEventListener('touchend', handleTouchEnd);

const slider2 = document.getElementById('slider2');
slider2.addEventListener('touchstart', handleTouchStart, { passive: true });
slider2.addEventListener('touchmove', handleTouchMove, { passive: true });
slider2.addEventListener('touchend', handleTouchEnd);
