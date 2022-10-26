import subprocess

p = subprocess.run(['java', '-version'])
print(p)

s = subprocess.Popen(['java','-version']).wait()
print(s)