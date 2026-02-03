Step	   Action	          Location
1	     Check cache	    sys.modules
2	     Find module	    sys.meta_path finders
3	     Search paths	    sys.path
4	     Create spec	    ModuleSpec object
5	     Create module	    Module object
6	     Execute code	    Run module code
7	     Cache module	    Store in sys.modules as object
8	     Return	          Return to caller (the sys.module object)



The way to not full in the circular imports is to import in the runtime not in the compil time.
thi is a way and there is also the injections , or to creat separated modules in separated packages.