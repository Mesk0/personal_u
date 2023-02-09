import matplotlib.pyplot as plt

plt.figure(1, figsize=(4,4))
plt.axis('off')

plt.axhspan(0,1,0.2,0.8,ec = "none")
plt.axhspan(0.2,0.8,0,0.2,ec = "none")
plt.axhspan(0.2,0.8,0.8,1,ec = "none")

plt.axhline(0.2,0.2,0.8,linewidth = 2, color = 'black')
plt.axvline(0.2,0.17,0.23,linewidth = 2, color = 'black')
plt.axvline(0.8,0.17,0.23,linewidth = 2, color = 'black')

plt.axvline(0.2,0.8,1,linewidth = 2, color = 'black')
plt.axhline(0.8,0.17,0.23,linewidth = 2, color = 'black')
plt.axhline(1,0.17,0.23,linewidth = 2, color = 'black')

plt.text(0.495,0.22,r"$l$", fontsize = 18,color="black")
plt.text(0.05,0.85,r"$\frac{4-l}{2}$", fontsize = 18,color="black")

plt.show()