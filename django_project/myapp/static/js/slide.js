const slides = document.querySelectorAll('.slideshow img');
const dotsContainer = document.querySelector('.slider-dots');
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

let currentIndex = 0;

function initSlider() {
  slides[currentIndex].classList.add('active');

  slides.forEach((_, index) => {
    const dot = document.createElement('div');
    dot.classList.add('slider-dot');
    if (index === currentIndex) dot.classList.add('active');
    dot.addEventListener('click', () => goToSlide(index));
    dotsContainer.appendChild(dot);
  });
}

function goToSlide(index) {
  slides[currentIndex].classList.remove('active');
  currentIndex = index;
  if (currentIndex < 0) currentIndex = slides.length - 1;
  else if (currentIndex >= slides.length) currentIndex = 0;
  slides[currentIndex].classList.add('active');
  document.querySelectorAll('.slider-dot').forEach((dot, i) => {
    dot.classList.toggle('active', i === currentIndex);
  });
}

initSlider();

prevButton.addEventListener('click', () => goToSlide(currentIndex - 1));
nextButton.addEventListener('click', () => goToSlide(currentIndex + 1));