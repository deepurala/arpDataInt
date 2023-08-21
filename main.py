import subprocess

program_list = ['circuit.py', 'constructors.py', 'drivers.py', 'finishStatus.py', 'races.py','seasons.py','resultsMapped.py']

for program in program_list:
    subprocess.call(['python', program])
    print("Finished:" + program)