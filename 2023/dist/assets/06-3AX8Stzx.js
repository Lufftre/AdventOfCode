import"./modulepreload-polyfill-9p4a8sJU.js";const o=`Time:        42     89     91     89
Distance:   308   1170   1291   1467`;document.querySelector("#input").innerHTML=o;const c=String(o),[l,m]=c.split(`
`).map(t=>t.split(":")[1].split(/\s+/).slice(1).map(e=>parseInt(e)));let p=1;for(let t=0;t<l.length;t++){const e=l[t],r=m[t],s=[];for(let n=0;n<e;n++)n*(e-n)>r&&s.push(n);p*=s.length}console.log(p);const[i,d]=c.split(`
`).map(t=>t.replaceAll(/\s+/g,"").split(":")[1]).map(t=>parseInt(t)),a=[];for(let t=0;t<i;t++)t*(i-t)>d&&a.push(t);const g=a.length;console.log(g);
