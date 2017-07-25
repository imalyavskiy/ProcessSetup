# -*- coding: utf-8 -*-
import subprocess
import os
import sys

def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

if len(sys.argv) < 2:
    print("ОШИБКА: Недостаточно аргументов.")
    print("\tАргумент должен быть один.")
    print("\tАргумент должен быть исполняемым файлом.")
    exit()

executable = which(sys.argv[1])

if executable is None:
    print("ОШИБКА: Файл \"{0}\" не является исполняемым.".format(sys.argv[1]))
    exit()

pipe = subprocess.PIPE
fpath, fname = os.path.split(executable)

environ = os.environ
environ["SOME_VAR"] = "Hello World!"

output = subprocess.Popen(executable,
                          shell=True,
                          stdin=pipe,
                          stdout=pipe,
                          stderr=subprocess.STDOUT,
                          cwd=fpath,
                          env=environ).stdout.read()

decoded_output = output.decode('utf8', 'ignore')
print(decoded_output)
