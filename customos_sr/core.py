#import some application for "system core"
import pytz
from datetime import datetime
import yaml
import requests
import sqlite3

#<systemvar>
dir = "/" # define the system defpath
sysversion = "v1.0.1.0.1" # define the system version
# you can remove the gtimestamp = core.gettime or gtimestamp = gettime (i don't know 1/2 why you can answer me in jensen@givemetocode.com thanks / :) \ )
#</systemvar>

#copy from newfile.py old
def create_utc_offset_map():
    utc_offset_map = {}
    for tz in pytz.all_timezones:
        timezone = pytz.timezone(tz)
        offset = timezone.utcoffset(datetime.now()).total_seconds() / 3600
        utc_offset_map[f"UTC{int(offset):+d}"] = tz
    return utc_offset_map

def gettime() :
	utc_offset_map = create_utc_offset_map()
	with open('config.def.yaml', 'r+') as file: 
		config = yaml.safe_load(file)
	# Get the timezone from the config or use UTC+8 if it's None (SO, the first boot timezone is UTC+8)
	timezone_str = config['settings']['timezone'] if config['settings']['timezone'] else 'UTC+8'
	timezone_name = utc_offset_map.get(timezone_str, 'Asia/Singapore')  # Default to Asia/Singapore for unknown timezone
	timezone = pytz.timezone(timezone_name)
	now = datetime.now(timezone)
	date_time = now.strftime("%m/%d/%Y_%H:%M:%S")
	gtimestamp = date_time
	return date_time

def writelog(logstring) :
    file = open("boot.log", "a")
    file.write(logstring)
    file.close()



#<ai>
def setup_userdb():
    """Initialize the SQLite database with a users table"""
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist with role column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user'
        )
    ''')
    
    # Insert default root user if no users exist
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    
    if count == 0: #</ai>
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', 
                      ('root', 'givemetocodeisthebest', 'root'))
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', 
                      ('dev_root', 'root', 'administrator'))
    #<ai>
    conn.commit()
    conn.close()

def signup_user(username, password, role='user'):
    """Register a new user with specified role"""
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', 
                      (username, password, role))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

def check_login(username, password):
    """Check if the provided username and password are valid"""
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()
    
    # Check if user exists and return user info including role
    cursor.execute('SELECT username, role FROM users WHERE username=? AND password=?', (username, password))
    result = cursor.fetchone()
    conn.close()
    #print(result) #used for debug
    return result is not None

#</ai>

def curl(url) :
    curl = requests.get(url)
    return curl.json