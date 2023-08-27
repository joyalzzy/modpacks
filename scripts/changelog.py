#!/home/joyal/mambaforge/bin/python
import os, subprocess, tomllib, sys
import numpy as np
def getdat(f: str):
    try: 
        with open(getroot() + "/" + f, "r" ) as fe:
            tom = tomllib.loads(fe.read())
            # print(tom["update"]["modrinth"]["mod-id"])
            try: 
                return [tom["name"], tom["update"]["modrinth"]["mod-id"]]
            except:
                return [tom["name"], tom["update"]["curseforge"]["project-id"]]

    except Exception as e:
        return [e,""]

def getroot():
    return (subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True).stdout.decode('ascii').strip())

def getdel(f: str):
    try: 
        # print(f)
        tom = tomllib.loads(subprocess.run(["git", "show", f"HEAD~{sys.argv[1]}:" + f], capture_output=True).stdout.decode('ascii').strip())
        try: 
            return [tom["name"], tom["update"]["modrinth"]["mod-id"]]
        except:
            return [tom["name"], tom["update"]["curseforge"]["project-id"]] 
    except Exception as e:
        return [e, ""]
        
os.chdir(getroot())
logs = subprocess.run(["git", "diff", "--name-status",  f"HEAD~{sys.argv[1]}"], capture_output=True).stdout.decode('ascii').strip()
logs = filter(lambda x: '1.20.1/mods' in x, logs.split('\n'))
changes = map(lambda y: [f"added {getdat(y[2 : None])[0]}", f"removed {getdel(y[2: None])[0]}", f"modified {getdel(y[2: None])[0]}"][np.where([y.startswith('A'),y.startswith('D'),y.startswith('M')])[0][0]],logs)
print("\n".join(list(changes)))
