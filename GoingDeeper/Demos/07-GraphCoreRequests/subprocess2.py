import subprocess

result = subprocess.run(["ls"], capture_output=True, text=True)
print("stdout: ", result.stdout.split("\n"))
print("stderr: ", result.stderr)
