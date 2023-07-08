import imageio
frames = []
for t in range(1,6):
    image = imageio.v2.imread(f'./figures/Figura_k-{t}.png')
    frames.append(image)

imageio.mimsave('./wena.gif', # output gif
                frames,          # array of input frames
                duration = 555)         # optional: frames per second