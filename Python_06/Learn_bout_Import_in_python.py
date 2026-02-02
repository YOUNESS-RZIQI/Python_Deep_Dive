# 1) First Check the sys.modules
# 2) not found use the finders and the loaders to find the modules and load it to modules then executi it.
# 3) 

            # Import search order

            # sys.modules → check if module is already loaded (cache).

            # Built-in and frozen modules → modules compiled into Python.

            # Path-based search (sys.path), in order:

            # Current directory / script’s directory

            # Directories in PYTHONPATH (if set)

            # Standard library directories

            # Site-packages (pip-installed packages)

            # ✅ So built-ins are checked before sys.path entries (including current dir).


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

