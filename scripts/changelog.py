#!/usr/bin/python 
data = ""
with open("./index.toml", "r") as f:
    data = f.read()
print(data.split("\n\n"))

