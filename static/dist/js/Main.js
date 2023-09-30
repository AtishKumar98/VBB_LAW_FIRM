const text = document.querySelector('.textual_placements');
const section = document.querySelector('.textual_placements');

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            text.style.transform = 'translateX(0)';
            text.style.opacity = '1';
            // Remove the observer once animation is triggered
            observer.unobserve(section);
        }
    });
}, {
    threshold: 0 // Trigger as soon as the element enters the viewport
});

observer.observe(section);