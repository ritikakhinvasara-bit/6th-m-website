import re

file_path = '/Users/ritikakhinvasara/.gemini/antigravity/scratch/landing-page/work.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_gallery = """            <!-- GALLERY GRID -->
            <section class="fade-section staggered-gallery">
                <div class="gallery-row">
                    <div class="gallery-item">
                        <img src="assets/gallery_2.png" alt="Pitch Decks">
                    </div>
                    <div class="gallery-item offset-down">
                        <img src="assets/gallery_5.jpg" alt="Email Design">
                    </div>
                </div>
                <div class="gallery-row">
                    <div class="gallery-item">
                        <img src="assets/gallery_4.jpg" alt="Editorial Reports">
                    </div>
                    <div class="gallery-item offset-down">
                        <img src="assets/gallery_3.png" alt="Social Media Content">
                    </div>
                </div>
                <div class="gallery-row">
                    <div class="gallery-item" style="margin: 0 auto; width: 60%;">
                        <img src="assets/gallery_1.png" alt="Ad Creatives">
                    </div>
                </div>
            </section>"""

# Replace the existing work-gallery section
content = re.sub(
    r'<!-- GALLERY GRID -->\s*<section class="fade-section work-gallery">.*?</section>',
    new_gallery,
    content,
    flags=re.DOTALL
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated work.html")
