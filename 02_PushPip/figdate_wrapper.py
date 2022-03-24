import tempfile
import subprocess
import venv
import sys
import os

if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as tmpdir:
        venv_builder = venv.EnvBuilder(with_pip=True)
        venv_builder.create(tmpdir)

        scripts = os.path.join(tmpdir, 'Scripts') 
        pip = os.path.join(scripts, 'pip')
        python = os.path.join(scripts, 'python')
        subprocess.run([pip, 'install', 'pyfiglet', '-q', '--disable-pip-version-check']);
 
        command = [python, '-m', 'figdate']
        for arg in sys.argv[1:]:
            command.append(arg)
        subprocess.run(command)
