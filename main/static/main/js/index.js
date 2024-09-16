const swiper = new Swiper('.swiper', {
  // Необязательные параметры
  // direction: 'vertical',
  loop: true,
  effect: 'coverflow',
  coverflowEffect: {
      // depth: 200,
      slideShadows: false,
      rotate: 1,
      modifier: 4,
  },

  slidesPerView: 3,

  // Если нам нужна разбивка на страницы
  pagination: {
    el: '.swiper-pagination',
  },

  // Навигационные стрелки
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

 });