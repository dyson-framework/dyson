from dyson.errors import DysonError
from dyson.utils.dataloader import DataLoader
from dyson.vars import VariableManager
from dyson.vars import iterate_dict


class Step:
    def __init__(self, step: dict, data_loader: DataLoader, variable_manager: VariableManager, keywords: dict,
                 modules: dict,
                 webdriver):

        self._step = step
        self._data_loader = data_loader
        self._variable_manager = variable_manager
        self._modules = modules
        self._keywords = keywords
        self._webdriver = webdriver

    def run(self):
        if 'name' in self._step.keys():
            print(self._step['name'])
            del self._step['name']

        step_module = next(iter(self._step))
        if step_module in self._keywords:
            """
            We check keywords first.  if they have a keyword that overrides a module, so be it.
            """
            # for the keyword, get the steps within, and execute it.
            self._variable_manager.add_var(self._step)  # add ephemeral variables
            individual_steps = self._data_loader.load_file(self._keywords[step_module])

            if isinstance(individual_steps, list):
                for individual_step in individual_steps:
                    individual_step = iterate_dict(individual_step, variable_manager=self._variable_manager)
                    Step(individual_step,
                         data_loader=self._data_loader,
                         variable_manager=self._variable_manager,
                         keywords=self._keywords,
                         modules=self._modules,
                         webdriver=self._webdriver).run()
            else:
                raise DysonError("Keywords must be a list")

            self._variable_manager.clear_additional_vars()
        elif step_module in self._modules:
            """
            Run the specified Module
            """
            return step_module, self._step[step_module], \
                   self._modules[step_module]().run(webdriver=self._webdriver, params=self._step[step_module])
        else:
            raise DysonError("No such module or keyword \"%s\" exists" % step_module)
