import re

file_path = '/Users/ritikakhinvasara/.gemini/antigravity/scratch/landing-page/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_gallery = """            </div>
        </section>

        <!-- RECENT WORK -->
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
            <div class="gallery-row" style="justify-content: center;">
                <div class="gallery-item" style="width: 50%;">
                    <img src="assets/gallery_1.png" alt="Ad Creatives">
                </div>
            </div>
            <div class="mt-5" style="text-align: center; margin-top: 50px;">
                <a href="work.html" class="btn-pill">VIEW MORE WORK</a>
            </div>
        </section>

        <!-- PRICING -->"""

# Replace the closing of services section to inject this
content = content.replace('            </div>\n        </section>\n\n        <!-- PRICING -->', new_gallery)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
