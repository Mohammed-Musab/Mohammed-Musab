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

<style>
text {{
    font-family: monospace;
}}

.terminal {{
    fill: #58a6ff;
    font-size: 28px;
}}

.title {{
    fill: #7ee787;
    font-size: 30px;
}}

.small {{
    fill: #8b949e;
    font-size: 18px;
}}
</style>

<rect width="1200" height="450" fill="#0d1117"/>

<rect x="20" y="50" width="1160" height="350"
rx="12"
fill="#161b22"
stroke="#58a6ff"
stroke-width="2"/>

<!-- MacOS buttons -->

<circle cx="55" cy="80" r="7" fill="#ff5f56"/>
<circle cx="80" cy="80" r="7" fill="#ffbd2e"/>
<circle cx="105" cy="80" r="7" fill="#27c93f"/>

<text x="140" y="87"
fill="#8b949e"
font-size="18">
Mohammed-Musab / README.md
</text>

<!-- Neural Network -->

<g>

<circle cx="170" cy="180" r="8" fill="#58a6ff">
    <animate attributeName="r"
             values="8;11;8"
             dur="2s"
             repeatCount="indefinite"/>
</circle>

<circle cx="170" cy="280" r="8" fill="#58a6ff">
    <animate attributeName="r"
             values="8;11;8"
             dur="2.5s"
             repeatCount="indefinite"/>
</circle>

<circle cx="280" cy="140" r="8" fill="#7ee787">
    <animate attributeName="r"
             values="8;11;8"
             dur="1.8s"
             repeatCount="indefinite"/>
</circle>

<circle cx="280" cy="230" r="8" fill="#7ee787">
    <animate attributeName="r"
             values="8;11;8"
             dur="2.2s"
             repeatCount="indefinite"/>
</circle>

<circle cx="280" cy="320" r="8" fill="#7ee787">
    <animate attributeName="r"
             values="8;11;8"
             dur="2.8s"
             repeatCount="indefinite"/>
</circle>

<circle cx="400" cy="180" r="8" fill="#f2cc60">
    <animate attributeName="r"
             values="8;11;8"
             dur="2.1s"
             repeatCount="indefinite"/>
</circle>

<circle cx="400" cy="280" r="8" fill="#f2cc60">
    <animate attributeName="r"
             values="8;11;8"
             dur="2.7s"
             repeatCount="indefinite"/>
</circle>

<line x1="170" y1="180" x2="280" y2="140" stroke="#58a6ff"/>
<line x1="170" y1="180" x2="280" y2="230" stroke="#58a6ff"/>
<line x1="170" y1="180" x2="280" y2="320" stroke="#58a6ff"/>

<line x1="170" y1="280" x2="280" y2="140" stroke="#58a6ff"/>
<line x1="170" y1="280" x2="280" y2="230" stroke="#58a6ff"/>
<line x1="170" y1="280" x2="280" y2="320" stroke="#58a6ff"/>

<line x1="280" y1="140" x2="400" y2="180" stroke="#58a6ff"/>
<line x1="280" y1="230" x2="400" y2="180" stroke="#58a6ff"/>
<line x1="280" y1="320" x2="400" y2="180" stroke="#58a6ff"/>

<line x1="280" y1="140" x2="400" y2="280" stroke="#58a6ff"/>
<line x1="280" y1="230" x2="400" y2="280" stroke="#58a6ff"/>
<line x1="280" y1="320" x2="400" y2="280" stroke="#58a6ff"/>

</g>

<!-- Animated terminal -->

<text x="540" y="140" class="title">

<tspan opacity="1">
# Initializing environment...
<animate attributeName="opacity"
values="1;0;0;0;0;0;0;0;0;0;0"
dur="44s"
repeatCount="indefinite"/>
</tspan>

<tspan opacity="0">
# Loading datasets...
<animate attributeName="opacity"
values="0;1;0;0;0;0;0;0;0;0;0"
dur="44s"
repeatCount="indefinite"/>
</tspan>

<tspan opacity="0">
# Cleaning data...
<animate attributeName="opacity"
values="0;0;1;0;0;0;0;0;0;0;0"
dur="44s"
repeatCount="indefinite"/>
</tspan>

</text>

<text x="540" y="190" class="terminal">
model.fit(
</text>

<text x="590" y="240"
fill="#f2cc60"
font-size="28">
Mohammed_Musab,
</text>

<text x="590" y="290"
fill="#ffffff"
font-size="28">
epochs=∞
</text>

<text x="540" y="340" class="terminal">
)
</text>

<!-- Blinking Cursor -->

<text x="930" y="140"
fill="#58a6ff"
font-size="30">
|
<animate attributeName="opacity"
values="1;0;1"
dur="1s"
repeatCount="indefinite"/>
</text>

<!-- Footer -->

<text x="40" y="430"
class="small">
Status: {status}
</text>

<text x="780" y="430"
class="small">
Updated: {updated}
</text>

</svg>
"""

with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Banner generated.")
