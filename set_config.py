import configparser
from tkinter import TRUE

Config = configparser.ConfigParser()
Config.read('data/config.ini')

section = 'Client'
k = "sla_strict"
val = 'Yes'


try:
    config = Config[section]
except:
    Config[section] = {}

Config[section][k] = val

with open('data/config.ini', 'w+')as f:
    Config.write(f)