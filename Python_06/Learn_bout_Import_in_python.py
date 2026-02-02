#  so py do searcj if the module is alredy loaded and excuted by the finders and loaders if not :
# 1- check builtins modules (in built ins in the usr/bin/python3.10 there is no packages)
# 2 - check sys.path;
#    1- current dir
#    2- the stdlib 
#    3- site packages.



# to see the built in modules in python3.10 that lives in the /usr/bin/pyhon3.10
import sys
print(sys.builtin_module_names)


# To list all standard library modules (the ones on disk, not built-ins) in Python 3.10,
import os
import sys

stdlib_path = os.path.dirname(os.__file__)  # path to the standard library
modules = []

for root, dirs, files in os.walk(stdlib_path):
    for file in files:
        if file.endswith(".py") and file != "__init__.py":
            # get module name relative to stdlib_path
            module = os.path.relpath(os.path.join(root, file), stdlib_path)
            modules.append(module.replace(os.sep, ".")[:-3])  # remove ".py"

print(modules)

