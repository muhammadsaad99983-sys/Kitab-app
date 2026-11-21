let B=[],tab='home',mk='سب مکاتب',fs=20;
const $=s=>document.querySelector(s),V=$('#view');
const fav=()=>{try{return JSON.parse(localStorage.fav||'[]')}catch(e){return[]}};
fetch('books.json').then(r=>r.json()).then(d=>{B=d;chips();render()});
function chips(){const m=['سب مکاتب',...new Set(B.map(b=>b.maktab))];
$('#chips').innerHTML=m.map(x=>`<button class="chip ${x==mk?'on':''}" onclick="mk='${x}';chips();render()">${x}</button>`).join('')}
function render(){const q=$('#q').value.trim();let l=B;
if(tab=='fav')l=l.filter(b=>fav().includes(b.id));
if(mk!='سب مکاتب')l=l.filter(b=>b.maktab==mk);
if(q)l=l.filter(b=>(b.title+b.author).includes(q));
if(tab=='about'){V.innerHTML='<div class="empty">یہ ایپ آپ کی منتخب کتب پڑھنے کے لیے ہے۔<br><button class="chip" onclick="document.body.classList.toggle(\'night\')">🌙 رات / دن موڈ</button></div>';return}
V.innerHTML=l.length?`<div class="grid">${l.map(b=>`<div class="card" onclick="openBook(${b.id})"><div class="cover" style="background-color:${b.color}">${b.title}</div><div class="meta"><b>${b.author}</b><span class="tag">${b.category}</span> <span class="tag">${b.maktab}</span></div></div>`).join('')}</div>`:'<div class="empty">کوئی کتاب نہیں ملی</div>'}
function openBook(id){const b=B.find(x=>x.id==id),f=fav().includes(id);
V.innerHTML=`<div class="reader"><div class="bar"><button onclick="render()">← واپس</button><button onclick="fs+=2;openBook(${id})">A+</button><button onclick="fs-=2;openBook(${id})">A−</button><button onclick="tg(${id})">${f?'❤️':'🤍'}</button></div><h2>${b.title}</h2><div style="font-size:${fs}px">${b.chapters.map(c=>`<h3>${c.title}</h3><p>${c.text}</p>`).join('')}</div></div>`;scrollTo(0,0)}
function tg(id){let f=fav();f=f.includes(id)?f.filter(x=>x!=id):[...f,id];try{localStorage.fav=JSON.stringify(f)}catch(e){}openBook(id)}
$('#q').oninput=render;
document.querySelectorAll('nav button').forEach(n=>n.onclick=()=>{tab=n.dataset.t;document.querySelectorAll('nav button').forEach(x=>x.classList.toggle('on',x==n));render()});
