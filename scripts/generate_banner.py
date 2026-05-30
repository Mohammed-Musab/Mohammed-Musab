from datetime import datetime
import random

statuses = [
    "🟢 Building Lazy Data Cleaner",
    "🧠 Studying Machine Learning",
    "📊 Exploring Data Science",
    "🚀 Working on New Features",
    "☕ Converting Coffee into Python",
    "🤖 Training Future AI Projects",
    "🇦🇪 Representing UAE in AI",
]

status = random.choice(statuses)

updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

svg = f'''
<svg width="1200" height="400" xmlns="http://www.w3.org/2000/svg">

<rect width="1200" height="400" fill="#0d1117"/>

<rect x="20" y="70" width="1160" height="280"
fill="#0b1220"
stroke="#1f6feb"
stroke-width="2"/>

<text x="40" y="40"
fill="#8b949e"
font-family="monospace"
font-size="20">
Mohammed-Musab / README.md
</text>

<text x="650" y="130"
fill="#7ee787"
font-family="monospace"
font-size="30">
# Training the model...
</text>

<text x="650" y="180"
fill="#58a6ff"
font-family="monospace"
font-size="34">
model.fit(
</text>

<text x="700" y="230"
fill="#f2cc60"
font-family="monospace"
font-size="34">
Mohammed_Musab,
</text>

<text x="700" y="280"
fill="#ffffff"
font-family="monospace"
font-size="34">
epochs=∞
</text>

<text x="650" y="330"
fill="#58a6ff"
font-family="monospace"
font-size="34">
)
</text>

<circle cx="180" cy="210" r="8" fill="#7ee787"/>
<circle cx="120" cy="150" r="8" fill="#7ee787"/>
<circle cx="120" cy="270" r="8" fill="#7ee787"/>
<circle cx="250" cy="150" r="8" fill="#7ee787"/>
<circle cx="250" cy="270" r="8" fill="#7ee787"/>
<circle cx="330" cy="210" r="8" fill="#7ee787"/>

<line x1="120" y1="150" x2="180" y2="210" stroke="#58a6ff"/>
<line x1="120" y1="270" x2="180" y2="210" stroke="#58a6ff"/>
<line x1="180" y1="210" x2="250" y2="150" stroke="#58a6ff"/>
<line x1="180" y1="210" x2="250" y2="270" stroke="#58a6ff"/>
<line x1="250" y1="150" x2="330" y2="210" stroke="#58a6ff"/>
<line x1="250" y1="270" x2="330" y2="210" stroke="#58a6ff"/>

<text x="40" y="375"
fill="#8b949e"
font-family="monospace"
font-size="18">
Status: {status}
</text>

<text x="700" y="375"
fill="#8b949e"
font-family="monospace"
font-size="18">
Last Updated: {updated}
</text>

</svg>
'''

with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(svg)
