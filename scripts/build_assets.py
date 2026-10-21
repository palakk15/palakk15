"""Regenerate the self-contained SVGs using only the Python standard library."""
from pathlib import Path
from html import escape
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
CSS = '''text{white-space:pre;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,"DejaVu Sans Mono",monospace}
@keyframes reveal{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
@keyframes appear{from{opacity:0}to{opacity:1}}
@keyframes blink{50%{opacity:0}}
@keyframes rain{from{transform:translateY(-38px)}to{transform:translateY(48px)}}
@keyframes pulse{50%{opacity:.72}}
.type{animation:reveal .8s steps(32,end) both}.row{animation:appear .5s both}
.cursor{animation:blink 1.1s step-end infinite}.portrait{animation:pulse 7s ease-in-out 3s infinite}
@media(prefers-reduced-motion:reduce){*{animation:none!important;clip-path:none!important;opacity:1!important}}
'''

def text(x,y,value,size=16,color='#c9d1d9',extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" {extra}>{escape(value)}</text>'

def rect(x,y,w,h,fill='#161b22',extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" {extra}/>'

def write(name,w,h,body,title):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><style>{CSS}</style>'+rect(0,0,w,h,'#0d1117','rx="16"')+body+'</svg>'
    ET.fromstring(svg)
    assert len(svg.encode()) < 150_000
    (ASSETS/name).write_text(svg,encoding='utf-8')

def hero():
    body=rect(1,1,998,558,'#0d1117','rx="16" stroke="#30363d"')+rect(2,2,996,42,'#161b22','rx="15"')
    for x,c in [(25,'#ff5f57'),(47,'#febc2e'),(69,'#28c840')]:
        body+=f'<circle cx="{x}" cy="23" r="6" fill="{c}"/>'
    body+=text(100,29,'palak@github: ~',13,'#8b949e')+text(30,86,'ENGINEER. BUILDER. ALWAYS CURIOUS.',13,'#bc8cff')
    lines=[('$ whoami','#3fb950'),('palak boob','#c9d1d9'),('software engineer / agentic AI focus','#58a6ff'),('$ cat education.txt','#3fb950'),('B.Tech Computer Engineering','#58a6ff'),('Honors, Data Science · DJSCE','#58a6ff'),('2024–2028 · CGPA 9.4','#8b949e'),('$ ls ./proof','#3fb950'),('internship  TWWIOS Technologies','#58a6ff'),('ideathons   1st SynkF · 3rd Oscillation','#58a6ff'),('projects    VeilAI · InfraSetu','#58a6ff'),('            ReserveX · AnvayaX','#58a6ff'),('$ status','#3fb950'),('exploring agents that plan, call tools','#c9d1d9'),('and recover when a step fails.','#c9d1d9')]
    for i,(s,c) in enumerate(lines):
        body+=text(30,122+i*26,s,15,c,f'class="type" style="animation-delay:{i*.45}s"')
    body+=rect(30,520,9,16,'#3fb950','class="cursor"')+'<path d="M470 75V526" stroke="#30363d"/>'
    body+='<g class="portrait" xml:space="preserve">'
    for i,line in enumerate((ASSETS/'ascii-portrait.txt').read_text().splitlines()):
        body+=text(480,102+i*8.8,line,8.5,'#58a6ff',f'class="row" style="animation-delay:{i*.04}s"')
    body+='</g>'+text(740,535,'human behind the code',12,'#8b949e','text-anchor="middle"')
    write('hero.svg',1000,560,body,'Palak Boob: software engineer exploring agentic AI, with an animated ASCII portrait')

def headings():
    names={'about':'About me','carryover':'Why my backend work carries over to agents','experience':'Experience','projects':'Projects','achievements':'Achievements','exploring':"What I’m exploring in agentic AI",'stack':'Tech stack','education':'Education & leadership','activity':'Activity'}
    for key,title in names.items():
        body=text(18,31,title,20,'#c9d1d9','class="type"')+rect(18,45,560,2,'#58a6ff','class="type"')
        write(f'section-{key}.svg',620,60,body,title)

def divider():
    body=''
    for i in range(65):
        body+=f'<g style="opacity:{.25+(i%4)*.1};animation:rain {3+i%5}s linear -{i%7}s infinite">'+text(i*16,5,'0 1' if i%2 else '1 0',10,'#3fb950')+'</g>'
    write('divider-matrix.svg',1000,48,body,'Subtle animated binary divider')

def metrics():
    cards=[('VeilAI','172','automated tests','12-stage privacy pipeline','#58a6ff'),('InfraSetu','40%','less manual tracking','Audit trails · 8 dashboards','#3fb950'),('ReserveX','50+','venues supported','Booking access · 3 roles','#bc8cff'),('AnvayaX','3','forecast models','GFS · IFS · AIFS','#f2cc60')]
    for i,(name,number,label,detail,color) in enumerate(cards):
        body=rect(1,1,478,228,'#0d1117','rx="15" stroke="#30363d"')
        body+=text(22,35,f'0{i+1} / {name}',17,color)+text(22,95,number,46,color,'class="row"')+text(22,124,label,16)+text(22,207,detail,14,'#8b949e')
        if i==1:
            body+=rect(22,148,430,18,'#21262d','rx="4"')+rect(22,148,172,18,color,'rx="4" class="type"')+text(22,184,'40% reduction · supplied project result',12,'#8b949e')
        else:
            count={0:12,2:3,3:3}[i]
            for k in range(count):
                body+=rect(22+k*(430/count),149,430/count-6,17,color,f'rx="3" class="row" style="animation-delay:{k*.09}s"')
            body+=text(22,184,{0:'12 stages',2:'3 user roles',3:'3 named model sources'}[i],12,'#8b949e')
        write(f'project-{name.lower()}.svg',480,230,body,f'{name}: {number} {label}. {detail}')
    body=text(24,34,'THE ENGINEERING LOOP I’M EXPLORING',16,'#bc8cff')
    for i,s in enumerate(['Plan','Call tools','Validate','Recover','Review']):
        x=24+i*194
        body+=rect(x,65,168,54,'#161b22','rx="8" stroke="#30363d"')+text(x+84,98,s,16,'#58a6ff','text-anchor="middle"')
        if i<4: body+=text(x+176,98,'→',20,'#3fb950')
    body+=text(24,151,'Scoped permissions · audit trails · tests and evals',15,'#8b949e')
    write('agent-flow.svg',1000,180,body,'Agent engineering exploration: plan, call tools, validate, recover, review')

if __name__ == '__main__':
    hero(); headings(); divider(); metrics()
    print('Built and XML-validated all profile SVGs.')
