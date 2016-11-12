import glob
import os
import importlib

from dyson.errors import DysonError
from dyson.utils.module import DysonModule
from dyson.vars import merge_dict


def load_modules(mod_path=None):
    all_modules = dict()

    # each path, local dir last to override any.
    modules_paths = (
        os.path.abspath(os.path.join(os.path.dirname(__file__), "core")),
        os.path.abspath(os.path.join(os.path.dirname(__file__), "extras")),
        os.path.abspath("/etc/dyson/modules"),
        os.path.abspath(os.path.join(os.path.dirname(os.path.curdir), "modules"))
    )

    if mod_path is not None:
        # load specific modules from a path.
        all_modules = merge_dict(load_modules(), _load_modules_from(mod_path))
    else:
        for module_path in modules_paths:
            all_modules = merge_dict(all_modules, _load_modules_from(module_path))

    return all_modules


def _load_modules_from(module_path):
    all_modules_from_path = dict()

    if os.path.exists(module_path) and os.path.isdir(module_path):
        for filename in glob.iglob("%s/**" % module_path, recursive=True):
            # FIXME (maybe?) for now, we only support python modules
            if os.path.isfile(filename) and os.path.basename(filename).endswith(".py") \
                    and not os.path.basename(filename).startswith("__"):
                module = None
                # module = importlib.import_module(os.path.basename(filename))
                dirs = os.path.abspath(os.path.dirname(filename)).split(os.path.sep)
                dirs = list(filter(None, dirs))

                for i in range(len(dirs)):
                    i = 0
                    module_path = '.'.join(dirs)
                    try:
                        module = importlib.import_module(module_path)
                        break
                    except ImportError:
                        del dirs[i]

                if module and module_path:
                    try:
                        module_to_load = os.path.basename(os.path.splitext(filename)[0])
                        if module_to_load.find("_") != -1:
                            # using a _ in the module name.
                            split = module_to_load.split("_")
                            module_nicename = ""
                            for s in split:
                                module_nicename += s.capitalize()
                        else:
                            module_nicename = module_to_load.replace("_", "").capitalize()

                        theclass = "%sModule" % module_nicename
                        mod = getattr(__import__("%s.%s" % (module_path, module_to_load), fromlist=[theclass]),
                                      theclass)

                        if issubclass(mod, DysonModule):
                            all_modules_from_path[module_to_load] = mod
                    except ImportError:
                        raise DysonError("Couldn't find class %s" % theclass)

    return all_modules_from_path
