import importlib

a = importlib.import_module("sys")

print(getattr(a, "__version__", "unknown"))
