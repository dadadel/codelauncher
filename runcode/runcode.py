import subprocess
import sys
import os


class RunCCode(object):
    
    def __init__(self, code=None):
        self.code = code
        self.compiler = "gcc"
        if not os.path.exists('running'):
            os.mkdir('running')
    
    def _compile_c_code(self, filename, prog="./running/a.out"):
        cmd = [self.compiler, filename, "-Wall", "-o", prog]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result

    def _run_c_prog(self, cmd="./running/a.out"):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result
    
    def run_c_code(self, code=None):
        filename = "./running/test.c"
        if not code:
            code = self.code
        result_run = "No run done"
        with open(filename, "w") as f:
            f.write(code)
        res = self._compile_c_code(filename)
        result_compilation = self.stdout + self.stderr
        if res == 0:
            self._run_c_prog()
            result_run = self.stdout + self.stderr
        return result_compilation, result_run


class RunCppCode(object):

    def __init__(self, code=None):
        self.code = code
        self.compiler = "g++"
        if not os.path.exists('running'):
            os.mkdir('running')

    def _compile_cpp_code(self, filename, prog="./running/a.out"):
        cmd = [self.compiler, filename, "-Wall", "-o", prog]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result

    def _run_cpp_prog(self, cmd="./running/a.out"):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result

    def run_cpp_code(self, code=None):
        filename = "./running/test.cpp"
        if not code:
            code = self.code
        result_run = "No run done"
        with open(filename, "w") as f:
            f.write(code)
        res = self._compile_cpp_code(filename)
        result_compilation = self.stdout + self.stderr
        if res == 0:
            self._run_cpp_prog()
            result_run = self.stdout + self.stderr
        return result_compilation, result_run

class RunPyCode(object):
    
    def __init__(self, code=None):
        self.code = code
        if not os.path.exists('running'):
            os.mkdir('running')

    def _run_py_prog(self, cmd="a.py"):
        cmd = [sys.executable, cmd]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result
    
    def run_py_code(self, code=None):
        filename = "./running/a.py"
        if not code:
            code = self.code
        with open(filename, "w") as f:
            f.write(code)
        self._run_py_prog(filename)
        return self.stderr, self.stdout
