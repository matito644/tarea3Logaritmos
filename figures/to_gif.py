import imageio
frames = []
for t in range(2,23, 2):
    image = imageio.v2.imread(f'./figures/Figura_k-{t}.png')
    frames.append(image)

imageio.mimsave('./wena.gif', # output gif
                frames,          # array of input frames
                duration = 444)         # optional: frames per second