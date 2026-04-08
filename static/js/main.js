const elements = document.querySelectorAll('.fade-in');

window.addEventListener('scroll', () => {
    elements.forEach(el => {
        const position = el.getBoundingClientRect().top;
        const screenHeight = window.innerHeight;

        if (position < screenHeight - 100) {
            el.classList.add('show');
        }
    });
});
const cursor = document.getElementById("cursor");

document.addEventListener("mousemove", e => {
    cursor.style.left = e.clientX + "px";
    cursor.style.top = e.clientY + "px";
});
// PARALLAX EFFECT
const videos = document.querySelectorAll('.bg-video');

window.addEventListener('scroll', () => {
    let scrollY = window.scrollY;

    videos.forEach(video => {
        video.style.transform = `translateY(${scrollY * 0.2}px)`;
    });
});
const texts = document.querySelectorAll('.reveal-text');

window.addEventListener('scroll', () => {
    texts.forEach(el => {
        const pos = el.getBoundingClientRect().top;
        if (pos < window.innerHeight - 100) {
            el.classList.add('show');
        }
    });
});