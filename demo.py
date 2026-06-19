import os, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
os.makedirs("figures",exist_ok=True); os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(1); snps=200
pops=[]; lab=[]
for i,freqshift in enumerate([0.2,0.5,0.8]):
    af=np.clip(rng.normal(freqshift,0.15,snps),0.02,0.98)
    g=rng.binomial(2,af,(80,snps)); pops.append(g); lab+= [i]*80
X=np.vstack(pops).astype(float); lab=np.array(lab)
emb=PCA(2).fit_transform(X)
plt.figure(figsize=(6,5))
for k,c in enumerate(["#e41a1c","#377eb8","#4daf4a"]):
    plt.scatter(emb[lab==k,0],emb[lab==k,1],s=14,c=c,label=f"population {k+1}")
plt.xlabel("PC1"); plt.ylabel("PC2"); plt.title("Population structure via PCA (demo data)"); plt.legend()
plt.tight_layout(); plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("3 populations separated on PC1/PC2\n"); print("ok")