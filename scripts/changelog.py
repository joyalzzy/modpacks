#!/home/joyal/mambaforge/bin/python
import os, subprocess, tomllib, sys
import numpy as np
def getdat(f: str):
    try: 
        with open(getroot() + "/" + f, "r" ) as fe:
            tom = tomllib.loads(fe.read())
            # print(tom["update"]["modrinth"]["mod-id"])
            return [tom["name"], tom["update"]["modrinth"]["mod-id"] if tom["update"]["modrinth"]["mod-id"] else tom["update"]["curseforge"]["project-id"]]
    except Exception as e:
        print(e)
        return ["",""]

def getroot():
    return (subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True).stdout.decode('ascii').strip())

def getdel(f: str):
    try: 
        tom = tomllib.loads(subprocess.run(["git", "show", f"HEAD~{sys.argv[1]}:" + f], capture_output=True).stdout.decode('ascii').strip())
        return [tom["name"], tom["update"]["modrinth"]["mod-id"] if tom["update"]["modrinth"]["mod-id"] else tom["update"]["curseforge"]["project-id"]] 
    except:
        return ["idk", "idk"]
        
os.chdir(getroot())
logs = subprocess.run(["git", "diff", "--name-status",  f"HEAD~{sys.argv[1]}"], capture_output=True).stdout.decode('ascii').strip()
logs = filter(lambda x: '1.20.1/mods' in x and not x.startswith('M'), logs.split('\n'))
changes = map(lambda x: [f"added {getdat(x[2 : None])[0]}", f"removed {getdel(x[2: None])[0]}"][np.where([str(x).startswith('A'), str(x).startswith('D')])[0][0]],logs)
print("\n".join(list(changes)))
