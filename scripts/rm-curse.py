#!/home/joyal/mambaforge/bin/python
import os,sys, tomllib

args = sys.argv
os.chdir(args[1])

def findcurse():
    for f in os.listdir("./mods"):
        if not f.endswith(".toml"):
            break
        with open("./mods/" + f, "r") as fe:
            t = tomllib.loads(fe.read())
#            print(t["update"])
            try: 
                if not t["update"]["curseforge"]:
                    break
            except:
                print(t.get("name"))

findcurse()

