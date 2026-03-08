(function() {
  'use strict';

  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var navLinks = document.querySelector('.nav-links');

  if (toggle && navLinks) {
    toggle.addEventListener('click', function() {
      navLinks.classList.toggle('open');
      toggle.setAttribute('aria-expanded',
        navLinks.classList.contains('open'));
    });
  }

  // Close mobile nav on link click
  if (navLinks) {
    navLinks.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function() {
        navLinks.classList.remove('open');
        if (toggle) toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Shrink header on scroll
  var header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }
})();
