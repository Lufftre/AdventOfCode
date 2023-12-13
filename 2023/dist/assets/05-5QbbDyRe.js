import"./modulepreload-polyfill-9p4a8sJU.js";const p=`seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4`;document.querySelector("#input").innerHTML=p;const f=String(p),[d,...g]=f.split(`
`),i=d.split(" ").slice(1).map(n=>parseInt(n)),c=[];let l;for(const n of g){if(n=="")continue;if(n.includes("map")){l=c.length,c.push([]);continue}const[e,s,t]=n.split(" ").map(o=>parseInt(o));c[l].push([e,s,t])}function S(n){const e=[];for(const s of n){let t=s;const o=[t];for(const m of c){for(const[u,a,h]of m)if(t>=a&&t<a+h){t=u+(t-a);break}o.push(t)}e.push(o)}return e}const w=S(i),y=Math.min(...w.map(n=>n[n.length-1]));console.log(y);let r;for(let n=0;n<i.length;n+=2){const e=i[n],s=i[n+1];console.log(e,s);for(let t=e;t<e+s;t++){const o=seedToLocation(t);r=o>r?r:o}}console.log(r);
