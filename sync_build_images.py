import os
from distutils.file_util import copy_file

sync_images = [  # generated with find lava-lib-dl/ -type f -name *.gif
    'lava-lib-dl/bootstrap/notebooks/mnist/gifs/out3.gif',
    'lava-lib-dl/bootstrap/notebooks/mnist/gifs/out0.gif',
    'lava-lib-dl/bootstrap/notebooks/mnist/gifs/out4.gif',
    'lava-lib-dl/bootstrap/notebooks/mnist/gifs/out2.gif',
    'lava-lib-dl/bootstrap/notebooks/mnist/gifs/out1.gif',
    'lava-lib-dl/bootstrap/notebooks/mnist/gifs/inp3.png',
    'lava-lib-dl/bootstrap/notebooks/mnist/gifs/inp0.png',
    'lava-lib-dl/bootstrap/notebooks/mnist/gifs/inp4.png',
    'lava-lib-dl/bootstrap/notebooks/mnist/gifs/inp2.png',
    'lava-lib-dl/bootstrap/notebooks/mnist/gifs/inp1.png',
    'lava-lib-dl/slayer/notebooks/oxford/input.gif',
    'lava-lib-dl/slayer/notebooks/oxford/output.gif',
    'lava-lib-dl/slayer/notebooks/oxford/target.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/input0.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/inp2.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/out3.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/input1.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/inp0.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/out0.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/out4.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/input3.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/input4.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/out2.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/out1.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/inp3.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/inp4.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/inp1.gif',
    'lava-lib-dl/slayer/notebooks/nmnist/gifs/input2.gif',
]

if __name__ == '__main__':
    if os.path.exists('_build/html'):  # if build dir is not empty
        for src_path in sync_images:
            folder, file = src_path.rsplit('/', 1)
            dst_folder = '_build/html/' + folder
            os.makedirs(dst_folder, exist_ok=True)
            if os.path.isdir(folder):
                copy_file(src_path, dst_folder + '/')
