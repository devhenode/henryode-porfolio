const navigation = [...document.querySelectorAll('nav a')];
const sections = navigation.map(link => document.querySelector(link.getAttribute('href'))).filter(Boolean);
function updateNavigation() {
  let current = sections[0];
  for (const section of sections) if (section.getBoundingClientRect().top <= 160) current = section;
  if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 20) current = sections.at(-1);
  for (const link of navigation) {
    const active = link.hash === '#' + current.id;
    link.classList.toggle('active', active);
    if (active) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current');
  }
}
window.addEventListener('scroll', updateNavigation, { passive: true });
updateNavigation();
