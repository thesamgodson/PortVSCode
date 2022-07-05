from pathlib import Path
from json import dump as dumpthis
from json import load as loadthis
from pathtub import add_to_path
from pathtub import remove_from_path

def namegen():
    print("""
 _____           ___      _______  _____          _      
|  __ \         | \ \    / / ____|/ ____|        | |     
| |__) |__  _ __| |\ \  / / (___ | |     ___   __| | ___ 
|  ___/ _ \|  __| __\ \/ / \___ \| |    / _ \ / _  |/ _ \ 
| |  | (_) | |  | |_ \  /  ____) | |___| (_) | (_| |  __/
|_|   \___/|_|   \__| \/  |_____/ \_____\___/ \____|\___|
Done by Sam Godson, Contact - Mail : contact.samgodson@gmail.com
                Github : @thesamgodson
""")

def vscode_json():#this is so that vscode can identify the location of the .exe files
    disk_name=str(Path(__file__).parent)# To get the cwd parent folder name
    rem_settings_path=r"\CODE\data\user-data\User\settings.json"# r is used to get the raw format
    settings_path=disk_name+rem_settings_path
    java_path=disk_name+r'\compilers\jdk-17\bin'
    gcpp_path=disk_name+r'\compilers\MinGW\bin\g++.exe'
    python_path=disk_name+r'\compilers\Python39\python.exe'
    with open(settings_path, "r") as jsonFile:
        data = loadthis(jsonFile)
    data["C_Cpp.default.compilerPath"]=gcpp_path
    data["java.home"]=java_path
    inter_path_python="& "+disk_name.replace("\\","/")+'/compilers/Python39/python.exe'
    # The following is the command which runs in terminal each time it needs to execute,
    data["code-runner.executorMap"]["python"]=inter_path_python
    data["python.defaultInterpreterPath"]=python_path
    #print(disk_name,settings_path,java_path,gcpp_path,python_path,inter_path_python)#To check if this works.
    with open(settings_path, "w") as jsonFile:
        dumpthis(data, jsonFile,indent=4)# indent = 4 is used to format the file, else it's dreadful to look at
    return disk_name


def addpath(disk_name:str):#This is to add to path to environment variables
    # We'll add python first
    python_interpreter_path=disk_name+r"\compilers\Python39\ "#There can be a trailing space while adding to the path actually
    python_script_path=disk_name+r'\compilers\Python39\Scripts'#That was a feature honestly.
    py=add_to_path(str(python_interpreter_path).rstrip(),'user')
    ps=add_to_path(str(python_script_path),'user')
    # Now JDK
    java_path=disk_name+r'\compilers\jdk-17\bin'
    jp=add_to_path(str(java_path),'user')
    # Now MinGW
    mingw_path=disk_name+r'\compilers\MinGW\bin'
    mw=add_to_path(str(mingw_path),'user')
    print("Added - Python:",py,", PyScript:",ps,", Java:",jp,", MinGW:",mw)


def cleaner(disk_name:str):
    # First we'll clean python
    python_interpreter_path=disk_name+r"\compilers\Python39\ "
    python_script_path=disk_name+r'\compilers\Python39\Scripts'
    py=remove_from_path(str(python_interpreter_path).rstrip(),'user')#Rstrip cause i didn't want to leave it with double //
    ps=remove_from_path(str(python_script_path),'user')
    # Now jdk
    java_path=disk_name+r'\compilers\jdk-17\bin'
    jp=remove_from_path(str(java_path),'user')
    # Now MinGW or gcc/g++ compilers
    mingw_path=disk_name+r'\compilers\MinGW\bin'
    mw=remove_from_path(str(mingw_path),'user')
    print("Removed - Python:",py,", PyScript:",ps,", Java:",jp,", MinGW:",mw)


if __name__=="__main__":
    namegen()#This'll generate the figlet styled name
    diskpath=vscode_json()
    add_response=input("If you want to add to path, press Y/y for Yes and N/n for No: ").lower()
    if add_response=="y":
        addpath(diskpath)
    clean_response=input("\nIf you want to clean the environment variables, run this as administrator. Press Y/y for Yes and N/n for No: ").lower()
    if clean_response=="y":
        cleaner(diskpath)