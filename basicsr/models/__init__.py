import importlib
from copy import deepcopy
from os import path as osp

from utils import get_root_logger, scandir
from utils.registry import MODEL_REGISTRY

__all__ = ['build_model']

# automatically scan and import model modules for registry
# scan all the files under the 'models' folder and collect files ending with
# '_model.py'

# print('*'*20,'model_init_','*'*20)
model_folder = osp.dirname(osp.abspath(__file__))
model_filenames = [osp.splitext(osp.basename(v))[0] for v in scandir(model_folder) if v.endswith('_model.py')]
print(model_filenames )
# import all the model modules
# _model_modules = [importlib.import_module(f'basicsr.models.{file_name}') for file_name in model_filenames]
_model_modules = [importlib.import_module(f'models.{file_name}') for file_name in model_filenames]
# print(_model_modules )


def build_model(opt):
    print("HERE HERE")
    """Build model from options.

    Args:
        opt (dict): Configuration. It must contain:
            model_type (str): Model type.
    """
    opt = deepcopy(opt)

    model = MODEL_REGISTRY.get(opt['model_type'])(opt)
    print('=' * 50)
    # print(model)
    logger = get_root_logger()
    logger.info(f'Model [{model.__class__.__name__}] is created.')
    return model
