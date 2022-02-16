import sys
import subprocess

code = 'compile("1" + "+1" * 10 ** 6, "string", "exec")'

result = subprocess.run([sys.executable, "-c", code ])

print(result.returncode, result)