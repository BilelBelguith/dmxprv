 #import erppeek
import configparser
import argparse

parser = argparse.ArgumentParser(description='create new database')
parser.add_argument('-d', '--dbname', dest='database', nargs='+', help='database name')
parser.add_argument('-u', '--host', dest='hostname', nargs='+', help='Url odoo')
parser.add_argument('-m', '--masterpass', dest='masterpass', nargs='+', help='Master password')
parser.add_argument('-l', '--login', dest='login', nargs='+', help='login')
parser.add_argument('-p', '--pass', dest='password', nargs='+', help='user password')

args = parser.parse_args()


DATABASE = args.database[0]
SERVER = args.hostname[0]
ADMIN_PASSWORD = args.masterpass[0]
USER_PASS = args.login[0]
USER_LOGIN = args.password[0]

def installNewDatabase(input):
    client = erppeek.Client(server=SERVER)
    if not DATABASE in client.db.list():
        print("The database does not exist yet, creating one!")
        client.create_database(ADMIN_PASSWORD, DATABASE, login=USER_LOGIN, user_password=USER_PASS)

 
        listModules= input.split(",")
        if (listModules!=[]):
            installModules(listModules)
    else:
        print("The database " + DATABASE + " already exists.")
 
        listModules= input.split(",")
        if (listModules!=[]):
            installModules(listModules)

def installModules(ListModules):
    client = erppeek.Client(SERVER, DATABASE, USER_LOGIN, USER_PASS)
    for i in range(len(ListModules)):
        print('%s'%ListModules[i])
        modules = client.modules('%s'%ListModules[i] ,installed=False)
        print(type(modules))
        if '%s'%ListModules[i] in modules['uninstalled']:
            client.install('%s'%ListModules[i])


input = input("""what are the modules that you want to install
 """)
installNewDatabase(input)
