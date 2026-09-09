(() => {
  let beginner = false;
  try { beginner = localStorage.getItem('mc2202-reading-mode') === 'newbie'; } catch (_) {}
  document.documentElement.classList.add('js');
  document.documentElement.dataset.mode = beginner ? 'newbie' : 'standard';
  document.documentElement.style.colorScheme = beginner ? 'dark' : 'light';
})();
