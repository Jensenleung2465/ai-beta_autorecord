import core
import bootloader
import yaml
import os
import sqlite3
import uuid
import cli

#<systemvar>
dir = "/" # define the system default path
sysversion = "v1.0.1.0.1" # define the system version
gtimestamp = core.gettime() # get the time from core.py
#</systemvar>

def login() :
    username = input("Username: ")
    password = input("Password: ")
    if core.check_login(username, password) == True : #call check_login() made by ai, then use "if" to check true and false?
        print("Login successful!")
        print("calling the cli...")
        acli(username, password)
    if core.check_login(username, password) == False :
        print("not correct")
        login()

def acli(username, password) :
    with open("config.def.yaml", "r") as file :
        yaml.safe_load(file)
    while True :
        cmd = input(f"{username}@{config['settings']['name']}:{dir} ~$")
        if cmd == "help" :
            cli.help()
        if cmd == "info" :
            cli.info()    
        

def setup() :
    print("Setup your customOS") 
    print("Part 1 -- setup user database")
    core.setup_userdb()
    print("Part2 -- setup administrator user")
    print("Sign up your account: ")
    core.signup_user(input("Your Username( NO [SPACE], ~!@#$%^&*()_+`-=[]',./|: etc... ): "), input("Your Password: "))
    print("Done")
    config['system']['setup'] = 1
    config['system']['sn-code'] = str(uuid.uuid4())
    with open("config.def.yaml", "w") as file: 
        yaml.dump(config, file, default_flow_style=False)

print(f"ai {sysversion}") 
bootloader.boot() #call the bootloader(BL)
with open('config.def.yaml', 'r') as file: 
    config = yaml.safe_load(file)
if config['system']['setup'] == 0 :
    setup()
print("copyright givemetocode.net 2025 info@givemetocode.com")
print("calling ai-beta_d application")
os.system('bash start.sh')