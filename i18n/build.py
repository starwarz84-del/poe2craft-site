import json, sys, re
sys.path.insert(0,'/home/claude/poe2data/i18n'); from en import EN
SITE='/home/claude/poe2data/site/'
LANG_EXPR = "((()=>{try{const q=new URLSearchParams(location.search).get('lang');if(q)return q;return localStorage.getItem('poe2lang')}catch(e){return null}})()||'en')"
RUNTIME = r"""
<script>
/* UI translation: game text comes from data (English or official Korean); remaining Korean UI text is translated here in English mode */
(() => {
  const D = __DICT__;
  const keys = Object.keys(D).sort((a,b)=>b.length-a.length);
  const re = new RegExp(keys.map(k=>k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|'),'g');
  const HAN = /[가-힣]/, ATTRS = ['placeholder','aria-label','title'];
  const origText = new Map(), origAttr = new Map();
  let lang = __LANG__;
  const tr = s => s.replace(re, m => D[m]);
  const skip = el => !el || el.closest('script,style,textarea,.keep-lang');
  function walk(root){
    if(lang!=='en' || !root) return;
    if(root.nodeType===3){ fix(root); return; }
    if(root.nodeType!==1) return;
    const tw=document.createTreeWalker(root, NodeFilter.SHOW_TEXT); let n;
    while((n=tw.nextNode())) fix(n);
    [root, ...root.querySelectorAll('[placeholder],[aria-label],[title]')].forEach(el=>{ if(!el.getAttribute || skip(el)) return;
      ATTRS.forEach(a=>{ const v=el.getAttribute(a); if(v && HAN.test(v)){ const t=tr(v); if(t===v) return; const o=origAttr.get(el)||{}; if(!(a in o)) o[a]=v; origAttr.set(el,o); el.setAttribute(a, t); } }); });
  }
  function fix(n){ const v=n.nodeValue; if(!HAN.test(v) || skip(n.parentElement)) return; const t=tr(v); if(t===v) return; if(!origText.has(n)) origText.set(n, v); n.nodeValue = t; }
  function restore(){ origText.forEach((v,n)=>{ if(n.isConnected) n.nodeValue=v; }); origText.clear(); origAttr.forEach((o,el)=>{ if(el.isConnected) for(const a in o) el.setAttribute(a,o[a]); }); origAttr.clear(); }
  new MutationObserver(ms=>{ if(lang!=='en') return; for(const m of ms){ if(m.type==='characterData') fix(m.target); else m.addedNodes.forEach(walk); } })
    .observe(document.documentElement, {subtree:true, childList:true, characterData:true});
  function setLang(l){ lang=l; document.documentElement.lang = l==='en'?'en':'ko'; if(l==='en') walk(document.body); else restore(); }
  ['kr','en'].forEach(id=>{ const b=document.getElementById('lang-'+id); if(!b) return; b.setAttribute('aria-pressed', String(lang===id)); b.addEventListener('click', ()=>setLang(id)); });
  window.addEventListener('message', e=>{ const d=e.data; if(d && d.type==='poe2-lang' && (d.lang==='en'||d.lang==='kr') && d.lang!==lang){ const b=document.getElementById('lang-'+d.lang); if(b) b.click(); else setLang(d.lang); } });
  setLang(lang);
})();
</script>
"""
EMBED_CSS = ".embed header.top{display:none}\n.embed footer{display:none}\n"
for f,out in [('emulator.html','pub/emulator.html'),('index.html','pub/builder.html')]:
    s=open(SITE+f).read()
    # default language
    if f=='emulator.html':
        s=s.replace("const S = { lang:'kr',", "const S = { lang:"+LANG_EXPR+",",1)
    else:
        s=s.replace("const S = { ", "const S = { lang:"+LANG_EXPR+", ",1) if "lang:'kr'" not in s else s.replace("lang:'kr'", "lang:"+LANG_EXPR,1)
    s=s.replace(".embed header.top > div:first-child{display:none}\n", EMBED_CSS,1)
    rt=RUNTIME.replace('__DICT__', json.dumps(EN, ensure_ascii=False)).replace('__LANG__', LANG_EXPR)
    s=s+rt
    head='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<style>html{color-scheme:dark}body{margin:0;font-family:system-ui,sans-serif;font-size:14px}img{max-width:100%}[hidden]{display:none!important}</style>\n'
    open(SITE+out,'w').write(head+s)
# recipes page is already bilingual; only needs the document head
open(SITE+'pub/recipes.html','w').write(head+open(SITE+'recipes.html').read())
open(SITE+'pub/discover.html','w').write(head+open(SITE+'reverse.html').read())
print('built')
