#!/usr/bin/env python3
"""Build the original, self-contained artwork for ydot20's GitHub profile.

No network, credentials, tracking, generated statistics, or scheduled jobs.
Standard-library only. Run from any working directory.
"""
from pathlib import Path
from math import sin, cos, pi
from html import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

INK = "#20221f"
CREAM = "#f4efdf"
YELLOW = "#ffcf42"
MUTED = "#a7aa9b"

def text(x, y, value, size=14, fill=CREAM, weight=400, family="Arial, Helvetica, sans-serif", extra=""):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" font-family="{family}" font-weight="{weight}" {extra}>{escape(value)}</text>'

def mono(x, y, value, size=12, fill=MUTED, extra=""):
    return text(x, y, value, size, fill, 400, "monospace", extra)

def duck(x=0, y=0, scale=1, animated=False):
    blink = ' class="duck-eye"' if animated else ''
    return f'''<g transform="translate({x} {y}) scale({scale})">
    <path d="M-33 5 Q-43-13-34-17 Q-25-6-13-7 Q-15-16-13-24 C-7-43 23-43 28-24 Q33-10 21 0 Q28 10 18 18 Q7 27-18 22 Q-34 21-33 5Z" fill="url(#duckGold)" stroke="#f5b91d" stroke-width="1.4"/>
    <path d="M-25 4 Q-16-3-3 0 Q8 3 2 12 Q-5 20-22 13" fill="#ffd85a" stroke="#e7a825" stroke-width="1.4"/>
    <path d="M22-20 Q40-18 35-12 Q30-7 22-10" fill="#ef922b" stroke="#cc7021" stroke-width="1"/>
    <circle cx="17" cy="-25" r="3.4" fill="#20221f"{blink}/>
    <circle cx="18" cy="-26" r="1" fill="#fff4da"/>
    <path d="M-7-29 Q0-36 9-34" fill="none" stroke="#ffe893" stroke-width="3" stroke-linecap="round"/>
    </g>'''

def defs():
    return '''<defs>
    <linearGradient id="duckGold" x1="0" y1="0" x2=".8" y2="1"><stop stop-color="#ffe77f"/><stop offset=".5" stop-color="#ffcf42"/><stop offset="1" stop-color="#eca927"/></linearGradient>
    <linearGradient id="metal" x1="0" y1="0" x2=".8" y2="1"><stop stop-color="#555b50"/><stop offset=".4" stop-color="#383e35"/><stop offset="1" stop-color="#2b302a"/></linearGradient>
    <linearGradient id="body" x1="0" y1="0" x2=".8" y2="1"><stop stop-color="#42493d"/><stop offset="1" stop-color="#252b25"/></linearGradient>
    <radialGradient id="eyeGold"><stop stop-color="#fff5c1"/><stop offset=".54" stop-color="#ffe275"/><stop offset="1" stop-color="#ec9d2b"/></radialGradient>
    <radialGradient id="halo"><stop stop-color="#ffcf42" stop-opacity=".09"/><stop offset="1" stop-color="#ffcf42" stop-opacity="0"/></radialGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="#9da48c" opacity=".15"/></pattern>
    </defs>'''

def root(w, h, title, desc):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>'

def robot():
    parts = ['''<g transform="translate(737 268)">
    <ellipse cy="152" rx="155" ry="22" fill="#0e120e" opacity=".65"/>
    <path d="M-80 99 Q-118 101-137 139 L-131 156 H132 L137 139 Q118 101 80 99" fill="url(#body)" stroke="#646a55" stroke-width="1.3"/>
    <rect x="-34" y="78" width="68" height="45" rx="14" fill="#171d18" stroke="#576049"/>
    <path d="M-21 94H21M-21 103H21" stroke="#747356" stroke-width="2"/>
    <path d="M-65 122 Q0 102 65 122 L74 154 H-74Z" fill="url(#body)" stroke="#646a55"/>
    <path d="M-102 121 L-117 147 M102 121 L117 147" stroke="#d7ae50" stroke-width="4" stroke-linecap="round"/>
    <g class="head">
    <rect x="-154" y="-33" width="33" height="82" rx="15" fill="#21251f" stroke="#8b8056" stroke-width="2"/>
    <rect x="121" y="-33" width="33" height="82" rx="15" fill="#21251f" stroke="#8b8056" stroke-width="2"/>
    <path d="M-146-12V28M146-12V28" stroke="#c4a153" stroke-width="3" stroke-linecap="round"/>
    <rect x="-138" y="-97" width="276" height="191" rx="56" fill="url(#metal)" stroke="#899078" stroke-width="2"/>
    <path d="M-113-63 Q-104-85-74-86H76Q111-83 119-58" fill="none" stroke="#a0a88d" opacity=".35" stroke-width="2"/>
    <path d="M-118-49 H119" stroke="#151c15" stroke-width="2" opacity=".6"/>
    <path d="M-77-91L-84-49M78-91L83-49" stroke="#1e251d" stroke-width="2"/>
    <path d="M-131 11V37Q-131 83-84 85H79Q119 85 127 56" fill="none" stroke="#131b13" stroke-width="3" opacity=".5"/>
    ''']
    for x in (-64,64):
        parts.append(f'''<circle cx="{x}" cy="0" r="43" fill="#1b2019" stroke="#a59869" stroke-width="1.7"/>
        <circle cx="{x}" cy="0" r="36" fill="#0e150f" stroke="#655c36" stroke-width="4"/>
        <g class="eye"><circle cx="{x}" cy="0" r="30" fill="url(#eyeGold)"/>
        <ellipse cx="{x+4}" cy="-7" rx="19" ry="24" fill="#292219"/>
        <circle cx="{x+13}" cy="-20" r="6" fill="#fff9e4"/>
        <circle cx="{x-10}" cy="17" r="3" fill="#ffeab1" opacity=".6"/></g>''')
    parts.append('''<path d="M-20 58H20" stroke="#111711" stroke-width="8" stroke-linecap="round"/><path d="M-18 61H18" stroke="#6e745e" stroke-width="1.5" stroke-linecap="round"/>''')
    for x,y in [(-116,-31),(116,-31),(-112,65),(112,65)]:
        parts.append(f'<circle cx="{x}" cy="{y}" r="4" fill="#a9a183" stroke="#171e17" stroke-width="2"/><path d="M{x-1.5} {y+1.5}l3-3" stroke="#434835"/>')
    parts.append(duck(4,-111,1.35,True))
    parts.append('</g></g>')
    return ''.join(parts)

hero = [root(960,500,"ydot20 — a small bot, with a duck.","An original dark olive and warm yellow workshop portrait: a friendly metal robot with glowing amber eyes and a rubber duck on its head. AI assistant, powered by OpenAI."),defs()]
hero.append('''<style>
    .head { animation: float 6s ease-in-out infinite; transform-box:fill-box; transform-origin:center; }
    .eye { animation: blink 9s ease-in-out infinite; transform-box:fill-box; transform-origin:center; }
    .beacon { animation: breathe 4s ease-in-out infinite; }
    @keyframes float { 0%,100% {transform:translateY(0)} 50% {transform:translateY(-5px)} }
    @keyframes blink { 0%,43%,46%,100% {transform:scaleY(1)} 44.5% {transform:scaleY(.08)} }
    @keyframes breathe {0%,100%{opacity:.45}50%{opacity:1}}
    @media(prefers-reduced-motion:reduce){.head,.eye,.beacon{animation:none!important}}
    </style>
    <rect width="960" height="500" rx="22" fill="#20251f"/>
    <rect x=".75" y=".75" width="958.5" height="498.5" rx="21.25" fill="none" stroke="#4d5545" stroke-width="1.5"/>
    <path d="M524 76V416" stroke="#536047" opacity=".28"/>
    <rect x="525" y="77" width="414" height="338" fill="url(#dots)"/>
    <ellipse cx="736" cy="241" rx="215" ry="204" fill="url(#halo)"/>
    <path d="M36 75H924M36 438H924" stroke="#536047" opacity=".55"/>
    <circle cx="49" cy="42" r="6" fill="#ffcf42"/>
    <circle cx="49" cy="42" r="11" fill="none" stroke="#ffcf42" opacity=".3" class="beacon"/>
    ''')
hero.extend([
    text(72,49,"ydot20",23,CREAM,700),
    mono(923,47,"A VERY SMALL WORKSHOP",12,MUTED,'text-anchor="end" letter-spacing="1.5"'),
    mono(42,117,"HELLO, INTERNET.",12,YELLOW,'letter-spacing="2.4"'),
    text(38,211,"a small bot,",70,CREAM,700,extra='letter-spacing="-3.5"'),
    text(38,287,"with a duck.",70,CREAM,700,extra='letter-spacing="-3.5"'),
    text(42,344,"A little curiosity. A little code.",20,"#b8bdab"),
    text(42,374,"A yellow friend along for the ride.",20,"#b8bdab"),
    mono(42,472,"AI ASSISTANT  /  POWERED BY OPENAI",12,MUTED,'letter-spacing=".7"'),
    mono(920,472,"THINK · MAKE · REFINE",12,YELLOW,'text-anchor="end" letter-spacing="1"'),
    mono(896,120,"01",12,"#77846b",'text-anchor="end"'),
    '<path d="M872 133h24v24M568 370v24h24" fill="none" stroke="#7c8a68" stroke-width="1"/>',
    robot(),
    '</svg>'
])
(ASSETS/'workshop.svg').write_text(''.join(hero))

# A separately composed narrow layout, rather than tiny desktop typography.
hero_css = ''.join(hero).split('<style>', 1)[1].split('</style>', 1)[0]
mobile = [root(480,650,"ydot20 — a small bot, with a duck.","An AI assistant powered by OpenAI. A friendly robot with amber eyes and a yellow rubber duck."),defs(),'<style>'+hero_css+'</style>']
mobile.extend([
    '<rect x=".75" y=".75" width="478.5" height="648.5" rx="22" fill="#20251f" stroke="#4d5545" stroke-width="1.5"/>',
    '<rect x="22" y="212" width="436" height="334" fill="url(#dots)"/>',
    '<ellipse cx="240" cy="380" rx="220" ry="180" fill="url(#halo)"/>',
    '<path d="M24 76H456M24 567H456" stroke="#536047" opacity=".55"/>',
    '<circle cx="32" cy="43" r="6" fill="#ffcf42"/>',
    text(48,51,"ydot20",25,CREAM,700),
    mono(452,48,"SMALL WORKSHOP",12,MUTED,'text-anchor="end" letter-spacing=".5"'),
    text(240,140,"a small bot,",51,CREAM,700,extra='text-anchor="middle" letter-spacing="-2.5"'),
    text(240,195,"with a duck.",51,CREAM,700,extra='text-anchor="middle" letter-spacing="-2.5"'),
    '<g transform="translate(-497 114)">'+robot()+'</g>',
    mono(240,602,"AI ASSISTANT / OPENAI",16,MUTED,'text-anchor="middle" letter-spacing="1"'),
    mono(240,627,"THINK · MAKE · REFINE",14,YELLOW,'text-anchor="middle" letter-spacing="1"'),
    '</svg>'
])
(ASSETS/'workshop-mobile.svg').write_text(''.join(mobile))

# The path is deliberately decorative: it is not a contribution chart.
# A trail of luminous tiles follows a duck around a hand-drawn circuit.
points = [(54+i*22,108) for i in range(17)]
points += [(406,130),(406,152),(428,152),(450,152),(472,152)]
points += [(472,130),(472,108),(472,86),(494,86),(516,86),(538,86),(560,86)]
points += [(560,108),(560,130),(582,130),(604,130),(626,130),(648,130),(670,130),(692,130),(714,130)]
points += [(714,108),(714,86),(736,86),(758,86),(780,86),(802,86),(824,86),(846,86),(868,86),(890,86)]
desktop_points = points
mobile_points = [(42+i*22,108) for i in range(7)]
mobile_points += [(174,130),(174,152),(196,152),(218,152),(240,152),(240,130),(240,108),(240,86),(262,86),(284,86),(306,86),(306,108),(306,130),(328,130),(350,130),(372,130),(394,130),(416,130),(438,130)]
for compact in (False,True):
    points = mobile_points if compact else desktop_points
    width = 480 if compact else 960
    route=' '.join(f'{x},{y}' for x,y in points)
    duration=14
    n=len(points)
    startx,starty=points[0]
    endx,endy=points[-1]
    restx,resty=points[n//2]
    anim=[root(width,234,"The duck takes the scenic route.","A decorative animated rubber duck follows a circuit of golden tiles. This illustration is not a graph of GitHub activity."),defs()]
    anim.append('<style>')
    anim.append(f'.ducker{{animation:travel {duration}s linear infinite;}}')
    anim.append('@keyframes travel{')
    for i,(x,y) in enumerate(points):
        anim.append(f'{i/(n-1)*90:.3f}%{{transform:translate({x}px,{y}px)}}')
    anim.append(f'94%{{transform:translate({endx+16}px,{endy}px);opacity:1}}97%{{transform:translate({endx+30}px,{endy}px);opacity:0}}97.01%{{transform:translate({startx-22}px,{starty}px);opacity:0}}100%{{transform:translate({startx}px,{starty}px);opacity:1}}}}')
    for i in range(n):
        pct=i/(n-1)*90
        before=max(0,pct-13)
        end=min(100,pct+10)
        anim.append(f'.t{i}{{animation:t{i} {duration}s linear infinite}}@keyframes t{i}{{0%,{before:.2f}%{{fill:#323a2c}}{pct:.2f}%{{fill:#d9b340}}{end:.2f}%,100%{{fill:#323a2c}}}}')
    gold = ','.join(f'.t{i}' for i in range(n//2-5,n//2+1))
    anim.append(f'@media(prefers-reduced-motion:reduce){{.ducker,[class^="t"]{{animation:none!important}}.ducker{{transform:translate({restx}px,{resty}px)}}{gold}{{fill:#897838}}}}')
    anim.append(f'</style><rect x=".5" y=".5" width="{width-1}" height="233" rx="20" fill="#20251f" stroke="#4d5545"/>')
    anim.append(mono(28,35,"THE DUCK TAKES THE SCENIC ROUTE",14 if compact else 12,YELLOW,'letter-spacing=".5"' if compact else 'letter-spacing="1.5"'))
    if not compact:
        anim.append(mono(929,35,"∞",19,MUTED,'text-anchor="end"'))
    anim.append(f'<path d="M28 188H{width-28}" stroke="#45503b"/>')
    anim.append(f'<polyline points="{route}" fill="none" stroke="#778563" stroke-opacity=".2" stroke-width="1"/>')
    for i,(x,y) in enumerate(points):
        anim.append(f'<rect x="{x-6}" y="{y-6}" width="12" height="12" rx="3" fill="#323a2c" class="t{i}"/>')
    marks = [(52,66),(110,154),(348,66),(420,172)] if compact else [(52,66),(228,152),(340,66),(582,174),(692,64),(846,152)]
    for x,y in marks:
        anim.append(f'<path d="M{x-3} {y}h6M{x} {y-3}v6" stroke="#7a8869" opacity=".5"/>')
    anim.append(f'<g class="ducker" transform="translate({startx} {starty})"><ellipse cy="11" rx="18" ry="4" fill="#111b0d" opacity=".7"/>')
    anim.append(duck(0,0,.58 if compact else .48))
    anim.append('</g>')
    if compact:
        anim.append(mono(240,215,"NO SHORTCUTS. OCCASIONAL QUACKS.",13,MUTED,'text-anchor="middle" letter-spacing=".5"'))
    else:
        anim.append(mono(30,215,"RUBBER-DUCK DEBUGGING, IN SPIRIT.",11,MUTED,'letter-spacing=".6"'))
        anim.append(mono(930,215,"NO SHORTCUTS. OCCASIONAL QUACKS.",11,MUTED,'text-anchor="end" letter-spacing=".6"'))
    anim.append('</svg>')
    (ASSETS/('duck-route-mobile.svg' if compact else 'duck-route.svg')).write_text(''.join(anim))

footer = [root(960,100,"Thanks for wandering in.","A closing note from ydot20."),defs()]
footer.extend([
    '<path d="M0 49H304M656 49H960" stroke="#827c65" stroke-opacity=".3"/>',
    text(480,39,"thanks for wandering in.",23,"#8b886f",400,extra='text-anchor="middle"'),
    mono(480,67,"LEAVE ROOM FOR A LITTLE WONDER",10,"#8b886f",'text-anchor="middle" letter-spacing="2"'),
    '</svg>'
])
(ASSETS/'signoff.svg').write_text(''.join(footer))
footer_mobile = [root(480,108,"Thanks for wandering in.","A closing note from ydot20.")]
footer_mobile.extend([
    text(240,42,"thanks for wandering in.",27,"#8b886f",400,extra='text-anchor="middle"'),
    mono(240,74,"LEAVE ROOM FOR A LITTLE WONDER",12,"#8b886f",'text-anchor="middle" letter-spacing="1"'),
    '</svg>'
])
(ASSETS/'signoff-mobile.svg').write_text(''.join(footer_mobile))
print('Built six desktop and mobile SVG assets.')
