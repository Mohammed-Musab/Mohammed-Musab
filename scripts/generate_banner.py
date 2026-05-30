from datetime import datetime
import random
import os

statuses = [
    "🟢 Building Lazy Data Cleaner",
    "🧠 Studying Machine Learning",
    "📊 Exploring Data Science",
    "🚀 Working on New Features",
    "☕ Converting Coffee into Python",
    "🤖 Training Future AI Projects",
    "🇦🇪 Representing UAE in AI",
    "📚 Learning Deep Learning",
    "⚡ Improving Open Source Projects",
]

status = random.choice(statuses)

updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

os.makedirs("assets", exist_ok=True)

svg = f"""
<svg width="1200" height="450" xmlns="http://www.w3.org/2000/svg">

<rect width="1200" height="450" fill="#0d1117"/>

<rect x="20" y="50" width="1160" height="350"
rx="12"
fill="#161b22"
stroke="#58a6ff"
stroke-width="2"/>

<text x="40" y="40"
fill="#8b949e"
font-family="monospace"
font-size="20">
Mohammed-Musab / README.md
</text>

<text x="540" y="140"
fill="#7ee787"
font-family="monospace"
font-size="30">
# Training the model...
</text>

<text x="540" y="190"
fill="#58a6ff"
font-family="monospace"
font-size="28">
model.fit(
</text>

<text x="590" y="240"
fill="#f2cc60"
font-family="monospace"
font-size="28">
Mohammed_Musab,
</text>

<text x="590" y="290"
fill="#ffffff"
font-family="monospace"
font-size="28">
epochs=∞
</text>

<text x="540" y="340"
fill="#58a6ff"
font-family="monospace"
font-size="28">
)
</text>

<text x="40" y="430"
fill="#8b949e"
font-family="monospace"
font-size="18">
Status: {status}
</text>

<text x="780" y="430"
fill="#8b949e"
font-family="monospace"
font-size="18">
Updated: {updated}
</text>

</svg>
"""

with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(svg)
