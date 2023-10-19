import importlib

class DepManager:
    def __init__(self):
        self.pkgs = {}

    def __getattr__(self, pkg:str):
        if '_' in pkg:
            module = '.'.join(pkg.split('_')[:-1])
            name = pkg.split('_')[-1]
            self.import_from(module, name)
            try:
                # return True, "ok", 
                return self.pkgs[name] #, self.pkgs[module].__version
            except KeyError:
                # return False, str([module,name]) + " not installed", 
                return None #, None
        else:
            self._add_deps(pkg)
            try:
                # return True, "ok", 
                return self.pkgs[pkg] #, self.pkgs[pkg].__version__
            except KeyError:
                # return False, str(pkg) + " not installed", 
                return None #, None

    def _add_deps(self, pkg:str):
        try:
            pkg_val = importlib.import_module(pkg)
            self.pkgs[pkg] = pkg_val
            setattr(self, pkg, pkg_val)
        except:
            pass

    def import_from(self,pkg:str, name:str):
        try:
            module = __import__(pkg, fromlist=[name])
            self.pkgs[name] = module
        except:
            pass
