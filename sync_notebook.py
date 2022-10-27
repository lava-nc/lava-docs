import os
import glob
from shutil import copytree as copy_tree
from shutil import ignore_patterns

module_dict = {}

try:
    import lava
    import lava.proc
    module_dict.update({'lava': lava.proc})  # this must be unique path
except ModuleNotFoundError:
    print(f"Failed importing {lava}. It's dependencies will be excluded.")

try:
    import lava.lib.dl.slayer as slayer
    module_dict.update({'slayer': slayer})
except ModuleNotFoundError:
    print(f"Failed importing slayer. It's dependencies will be excluded.")

try:
    import lava.lib.dl.bootstrap as bootstrap
    module_dict.update({'bootstrap': bootstrap})
except ModuleNotFoundError:
    print(f"Failed importing bootstrap. It's dependencies will be excluded.")

try:
    import lava.lib.dl.netx as netx
    module_dict.update({'netx': netx})
except ModuleNotFoundError:
    print(f"Failed importing netx. It's dependencies will be excluded.")

try:
    import lava.lib.optimization as optim
    module_dict.update({'optim': optim})
except ModuleNotFoundError:
    print(f"Failed importing optim. It's dependencies will be excluded.")


tutorial_list = [  # list of all notebooks to sync
    {
        'module': 'lava',
        'dst': 'lava/notebooks/',
        'tutorials': {
            'end_to_end': 'End to end tutorials',
            'in_depth': 'In-depth tutorials',
        },
    },
    {
        'module': 'slayer',
        'dst': 'lava-lib-dl/slayer/notebooks/',
        'tutorials': {
            'oxford': 'Oxford spike train regression',
            'nmnist': 'NMNIST digit classification',
            'pilotnet': 'PilotNet steering angle prediction',
            'neuron_dynamics': 'Dynamics and Neurons',
        },
    },
    {
        'module': 'bootstrap',
        'dst': 'lava-lib-dl/bootstrap/notebooks/',
        'tutorials': {
            'mnist': 'MNIST digit classification',
        },
    },
    {
        'module': 'netx',
        'dst': 'lava-lib-dl/netx/notebooks/',
        'tutorials': {
            'oxford': 'Oxford Inference',
            'pilotnet_snn': 'PilotNet SNN Inference',
            'pilotnet_sdnn': 'PilotNet SDNN Inference',
        },
    },
    {
        'module': 'optim',
        'dst': 'lava/notebooks/',
        'tutorials': {
            '': 'QP solver tutorials',
        },
    },
]


def create_nb_rst(folder_path, rst_name, header, ignore=[]):
    """Create rST file for notebook.

    Parameters
    ----------
    nb_path : str
        notebook path
    rst_name : str
        rST file name
    header : str
        header of the rST file entry
    """
    rst_text = f'''
    .. _{header}:
    {header}
    {"="*len(header)}

    .. toctree::
        :maxdepth: 1
        :glob:

    '''.replace('\n' + ' '*4, '\n')

    nb_paths = glob.glob(folder_path + '/*.ipynb')
    for nb_path in nb_paths:
        _, nb_name = nb_path.rsplit('/', 1)
        if nb_name in ignore:
            print(nb_name, ignore)
            continue
        rst_text += f'    {nb_name}{os.linesep}'


    print('Creating ' + folder_path + '/' + rst_name)
    with open(folder_path + '/' + rst_name, 'wt') as f:
        f.write(rst_text)


if __name__ == '__main__':
    for tutorials in tutorial_list:
        key = tutorials['module']
        if key in module_dict.keys():
            module = module_dict[key]
            module_path = module.__path__[0]
            module_path = module_path.split('src/lava')[0]
            dst = tutorials['dst']
            if 'ignore' in tutorials.keys():
                ignore = tutorials['ignore']
            else:
                ignore = []
            os.makedirs(dst, exist_ok=True)
            for tutorial, header in tutorials['tutorials'].items():
                src_path = glob.glob(
                    f'{module_path}tutorials/**/{tutorial}',
                    recursive=True,
                )
                print(f'src_path is {src_path}')
                dst_path = dst + tutorial

                # filter src path in key
                filter_path = []
                for p in src_path:
                    if key in p:
                        filter_path.append(p)
                src_path = filter_path
                if len(src_path) == 1:
                    src_path = src_path[0]
                    print(f'copying from {src_path} to {dst_path}')
                    copy_tree(src_path, dst_path, ignore=ignore_patterns('data', 'Logs'), dirs_exist_ok=True)
                    create_nb_rst(dst_path, tutorial+'.rst', header, ignore)
                else:
                    if len(src_path) == 0:
                        print(
                            f'search path: '
                            f'{module_path}tutorials/**/{tutorial}'
                        )
                        raise Exception('Module not found! Check your config')
                    else:
                        print(f'{key=}')
                        print(f'{filter_path=}')
                        raise Exception(
                            f'Multiple Moudles found: '
                            f'{src_path}'
                        )
