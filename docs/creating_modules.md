Creating Modules
================

There are two locations that custom modules may reside.

- Inside of your project root - a directory called `modules/`
- Inside of specific tests - a directory called `modules/`

## Create your first module

Inside of your project root, create a directory called `modules/`.

Inside the `modules/` directory, create a file named `my_module.py`

**my_module.py**

```python
from dyson.utils.module import DysonModule


class MyModuleModule(DysonModule):
    def run(self, webdriver, params):
        print("We're inside my module, and I passed \"%s\"" % params))
```

Inside of one of your test steps, you may now call your module.

```yaml
- my_module: hi there!
```

By executing this step, you will see `We're inside my module, and I passed "hi there!"`

You also have access to the base WebDriver API through the `webdriver` parameter.

See the [goto module](https://github.com/Dynamictivity/dyson-modules-core/blob/master/actions/goto.py) 
for the most basic definition of a functional module.

## Module Specifications

There are a few rules to follow when creating a module.

- The module must be in python
- The module file must end in `.py` (having a shebang in the file is not enough)
- The module must have a class that ends in `Module`
- The module must be a subclass of [`DysonModule`](https://github.com/Dynamictivity/dyson/tree/master/lib/dyson/utils/module.py)
- The module must implement the abstract method `run(self, webdriver, params)`

We also recommend the following conventions

- Only use `self.fail()` when a validation of some sort has failed, hence should fail tests.
- Always use `return ...` as your last statement as the result could be
used by the [store](https://github.com/dynamictivity/dyson/tree/master/docs/storing_variables.md) directive
- Always `raise DysonError("The Error Message")` when some constraint is not satisifed.
This could be an argument to the module for example.  See the [goto module](https://github.com/Dynamictivity/dyson-modules-core/blob/master/actions/goto.py#L10)
for an example of this.
