import re

with open("style.css", "r") as f:
    css = f.read()

# Replace .hero-visuals CSS
new_css = re.sub(
    r'\.hero-visuals \{[\s\S]*?\}\n\.hero-visual-left img, \.hero-visual-right img \{[\s\S]*?\}\n\.hero-visual-left \{[\s\S]*?\}\n\.hero-visual-right \{[\s\S]*?\}',
    r'''.hero-visuals {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 500px;
    position: relative;
    width: 100%;
}

.hero-slideshow {
    position: relative;
    width: 100%;
    max-width: 800px;
    height: 100%;
}

.hero-slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    gap: 40px;
    opacity: 0;
    transition: opacity 1s ease-in-out;
    pointer-events: none;
}

.hero-slide.active {
    opacity: 1;
    pointer-events: auto;
    position: relative;
}

.hero-gallery-left, .hero-gallery-right {
    position: relative;
    width: 45%;
}

.hero-staggered-img {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    object-position: center;
    border-radius: 12px;
}''',
    css
)

with open("style.css", "w") as f:
    f.write(new_css)
