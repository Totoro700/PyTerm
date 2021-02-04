# __main__.py
# Import
# os for file commands and others, time for wait second, platform for os command, multiprocessing for CPU count
import os, time, platform, shutil, socket, getpass, multiprocessing, tkinter, sys, ctypes
import webbrowser as web # Webbrowser for openLink command
import subprocess as sp # Subprocess for ping
import datetime as dt # Datetime for date and time
from time import gmtime, strftime
# webbrowser for openLink command, and datetime for date and time

__cache__ = 0 # Set cache to 0
prompt = '' # Setup prompt variable
__os__ = platform.system() # Get operating system name and store it in a variable (const)

# Print version and title as function
def title():
    print('@------------------------------------------------------------------------------------@')
    print('|                                                                                    |')
    print('|                                  |PyTerm v0.5.1|                                   |')
    print('|                                                                                    |')
    print('@------------------------------------------------------------------------------------@')

def clear(): # Clear screen
    if __os__ == 'Windows': # Windows
        os.system('cls')
    else: # Linux and Mac OS X
        os.system('clear')

def flt(param): # Return float from param
    return float(param)

def ping(host): # Ping a server
    param = '-n' if platform.system().lower() == 'windows' else '-c' # Setup ping parameters
    command = ['ping', param, '4', host] # Ping command
    return sp.call(command) == 0 # Return text

def fileExists(name):
    return os.path.exists(name)

def setupColor(): # Setup text and background color
    try:
        f = open('user_data/settings/color.txt', 'r')
        os.system(f.read())
    except:
        os.system('color 0A')


def cache():
    try:
        if fileExists('user_data'):
            if fileExists('user_data/cache.txt'):
                cache = open('user_data/cache.txt', 'r')
                if '1' in cache.read():
                    __cache__ = 1
                else:
                    cache_ = open('user_data/cache.txt', 'w')
                    cache_.write('1')
                    __cache__ = 0
            else:
                cache = open('user_data/cache.txt', 'x')
                cache.write('1')
                __cache__ = 0
        else:
            os.mkdir('user_data')
            cache = open('user_data/cache.txt', 'x')
            cache.write('1')
            __cache__ = 0
    except:
        print('Error')
    
def promptUpdate(): # Update prompt
    if fileExists('user_data/settings'):
        if fileExists('user_data/settings/prompt.txt'):
            global prompt
            prompt = open('user_data/settings/prompt.txt', 'r').read()
        else:
            f = open('user_data/settings/prompt.txt', 'x')
            f.write('>')
            f.close()
            prompt = '>'
    else:
        os.mkdir('user_data/settings')
        f = open('user_data/settings/prompt.txt', 'x')
        f.write('>')
        f.close()
        prompt = '>'

def fopenLink(link):
    web.open(link)


def init():
    clear()
    print('Loading . . .')
    cache()
    print('Loading color . . .')
    setupColor()
    print('Setting up . . .')
    promptUpdate()
    clear()
    title()

init()

# Main loop
while True:
    print(prompt+' ', end='') # Input prompt without line break ( \n )
    cmd = input() # Collect input
    if cmd == 'help':
        print('changelog                               Shows PyTerm\'s change log')
        print('color                                   Changes the text and the background color')
        print('copy                                    Copies a file')
        print('curDir                                  Displays the current directory')
        print('date                                    Shows the date and time')
        print('del                                     Deletes a file')
        print('delDir                                  Deletes a directory/folder')
        print('dir                                     Displays a list of files and subdirectories in a directory.')
        print('dirRoot                                 Displays a list of files and subdirectories in the root directory.')
        print('diskpart                                Displays or configures Disk Partition properties')
        print('echo                                    Displays messages you enter')
        print('exists                                  Checks if a file or folder exists')
        print('exit                                    Exits the program')
        print('find                                    Finds a specific text in a file')
        print('help                                    Displays this help message')
        print('info                                    Stores info')
        print('info -c                                 Clear stored info')
        print('info -g                                 Get stored info')
        print('ip                                      Displays your computer\'s IP address')
        print('licenes                                 Shows PyTerm\'s license ')
        print('md                                      Creates a directory')
        print('math -a                                 Adds two numbers together')
        print('math -s                                 Subtracts two numbers')
        print('math -m                                 Multiplies two numbers')
        print('math -d                                 Divides two numbers')
        print('mkdir                                   Creates a directory')
        print('mkfil                                   Creates a file')
        print('netstat                                 Displays protocol statistics and current TCP/IP network connections')
        print('notepad                                 [Windows] Opens Windows Notepad')
        print('npm install                             Install npm package')
        print('npm update                              Update npm package')
        print('npm upgrade                             Upgrade npm package')
        print('openBinFil                              Opens a binary file')
        print('openFil                                 Opens a file')
        print('openLink                                Opens a link in your browser')
        print('openWindow                              Opens a window')
        print('ping                                    Pings a server with an IP address')
        print('pip install                             Installs pip package')
        print('pip install -U                          Updates pip package')
        print('print                                   Displays messages you enter')
        print('prompt                                  Changes the prompt')
        print('py                                      [Windows] Opens Python\'s interpreter in cmd in a new window')
        print('pyver                                   Displays Python version')
        print('rename                                  Renames a file')
        print('repo                                    Opens the GitHub repository')
        print('reset                                   Resets to the title screen')
        print('restart                                 Restarts your computer')
        print('shutdown                                Shutdown your computer')
        print('sysinfo                                 Shows your computer\'s infomation')
        print('systeminfo                              Shows information about you computer')
        print('systeminfo                              Shows your computer\'s infomation')
        print('terminate                               Exits the program')
        print('TASKKILL                                Kill or stop a running process or application.')
        print('time                                    Also shows date and time')
        print('title                                   [Windows] Changes the console title')
        print('tree                                    Graphically displays the directory structure of a drive or path\n')
    elif cmd == 'help -a' or cmd == 'help --alt': # Help
        print('changelog                                                       Shows PyTerm\'s change log (../change.log)')
        print('color                                                            Changes the text and the background color')
        print('copy                                                                                         Copies a file')
        print('curDir                                                                      Displays the current directory')
        print('date                                                                               Shows the date and time')
        print('del                                                                                         Deletes a file')
        print('delDir                                                                          Deletes a directory/folder')
        print('dir                                            Displays a list of files and subdirectories in a directory.')
        print('dirRoot                                 Displays a list of files and subdirectories in the root directory.')
        print('diskpart                                                  Displays or configures Disk Partition properties')
        print('echo                                                                           Displays messages you enter')
        print('exists                                                                   Checks if a file or folder exists')
        print('exit                                                                                     Exits the program')
        print('find                                                                       Finds a specific text in a file')
        print('help                                                                            Displays this help message')
        print('info                                                                                           Stores info')
        print('info -c                                                                                  Clear stored info')
        print('info -g                                                                                    Get stored info')
        print('ip                                                                    Displays your computer\'s IP address')
        print('licenes                                                           Shows PyTerm\'s license (../LICENSE.txt)')
        print('math -a                                                                          Adds two numbers together')
        print('math -s                                                                              Subtracts two numbers')
        print('math -m                                                                             Multiplies two numbers')
        print('math -d                                                                                Divides two numbers')
        print('md                                                                                     Creates a directory')
        print('mkdir                                                                                  Creates a directory')
        print('mkfil                                                                                       Creates a file')
        print('netstat                                Displays protocol statistics and current TCP/IP network connections')
        print('notepad                                                                    [Windows] Opens Windows Notepad')
        print('npm install                                                                            Install npm package')
        print('npm update                                                                              Update npm package')
        print('npm upgrade                                                                            Upgrade npm package')
        print('openBinFil                                                                             Opens a binary file')
        print('openFil                                                                                       Opens a file')
        print('openLink                                                                      Opens a link in your browser')
        print('openWindow                                                                                  Opens a window')
        print('systeminfo                                                            Shows information about you computer')
        print('ping                                                                     Pings a server with an IP address')
        print('print                                                                          Displays messages you enter')
        print('prompt                                                                                  Changes the prompt')
        print('pip install                                                                           Installs pip package')
        print('pip install -U                                                                         Updates pip package')
        print('py                                            [Windows] Opens Python\'s interpreter in cmd in a new window')
        print('pyver                                                                              Displays Python version')
        print('rename                                                                                      Renames a file')
        print('reset                                                                           Resets to the title screen')
        print('repo                                                                           Opens the GitHub repository')
        print('restart                                                                             Restarts your computer')
        print('shutdown                                                                            Shutdown your computer')
        print('systeminfo                                                               Shows your computer\'s infomation')
        print('sysinfo                                                                  Shows your computer\'s infomation')
        print('terminate                                                                                Exits the program')
        print('TASKKILL                                                    Kill or stop a running process or application.')
        print('time                                                                              Also shows date and time')
        print('title                                                                  [Windows] Changes the console title')
        print('tree                                       Graphically displays the directory structure of a drive or path\n')
    elif cmd == 'help -h' or cmd == 'help --help' or cmd == 'help /?':
        print('Usage:    help [-a]\n\n\n\n')
        print('Parameters: \n')
        print('    -a  or  --alt      Prints help message another way\n\n')
    elif cmd == 'mkdir' or cmd == 'md': # Make directory
        print('Directory name?')
        try:
            os.mkdir(input())
        except:
            print('Error! Please try again and make sure that it is a valid directory name and it doesn\'t already exists!')
    elif cmd == 'mkfil': # Make file
        print('Full file name? (eg. "text.txt" or "index.html" or "python.py"). This file will be placed next to the program')
        fileName = input()
        try:
            f = open(fileName, 'x')
            print('Successfully created '+fileName)
            f.close()
        except:
            print('Error! Please try again and make sure that it is a valid file name and it doesn\'t already exists!')
    elif cmd == 'openFil': # Open file
        print('Full file name or directory? (eg. "text.txt" or "C:\\Python\\python.py")')
        toOpen = input()
        if fileExists(toOpen):
            f = open(toOpen, 'r')
            print(f.read())
        else:
            print('The file does not exist!')
    elif cmd == 'openBinFil': # Open binary file
        print('WARNING: This command may print a lot of text')
        print('Full binary file name or directory? (eg. "cmd.exe" or "C:\\Python\\python.dll")')
        toOpen = input() # Collect full directory or full file name
        print('Loading . . .')
        time.sleep(3)
        if fileExists(toOpen): # See if file exsits
            f = open(toOpen, 'rb') # Open/read binary file
            print(f.read()) # Display file
        else:
            print('The file does not exist!')
    elif cmd == 'curDir': # Current directory
        print(os.path.dirname(os.path.abspath(__file__)))
    elif cmd == 'del' or cmd == 'delete': # Delete
        print('Full file name or directory to delete? (eg. "text.txt" or "C:\\Trash\\text.txt")')
        toDel = input() # Collect directory or file name
        try: # Try if to delete the file
            if fileExists(toDel): # See if file exsits
                try:
                    os.remove(toDel)
                    print('Successfully deleted '+toDel)
                except:
                    print('Error! Please make sure that the file in not in use by another program!')
            else:
                print('The file does not exist!')
        except: # The user might have typed a folder name or the access is deined
            print('Something went wrong! Make sure it\'s a file, not a folder, with it\'s file extension and this program has access to it!')
    elif cmd == 'info' or cmd == 'info -s' or cmd == 'info --store': # Store data
        print('Info to store?')
        toStore = input() # Collect string to store
        if not fileExists('user_data/info.txt'): # See if the file info.txt exsits
            if fileExists('user_data'):
                f = open('user_data/info.txt', 'x') # Open info.txt or create one
                f.write(toStore+'\n') # Write to it
                f.close() # Close
            else:
                os.mkdir('user_data') # Create folder called user_data
                f = open('user_data/info.txt', 'x') # Open info.txt or create one
                f.write('\n'+toStore) # Write to it
                f.close() # Close
        else:
            f = open('user_data/info.txt', 'a') # Open user_data/info.txt
            f.write('\n'+toStore) # Write
            f.close() # Close
    elif cmd == 'info -o' or cmd == 'info --overwrite': # Overwrite stored info
        print('Info to overwrite?')
        toStore = input() # Collect string to store
        if not fileExists('user_data/info.txt'): # See if the file info.txt exsits
            if fileExists('user_data'):
                if fileExists('user_data/info.txt'):
                    f = open('user_data/info.txt', 'w') # Open info.txt or create one
                    f.write(toStore+'\n') # Write to it
                    f.close() # Close
                else:
                    f = open('user_data/info.txt', 'x') # Open info.txt or create one
                    f.write('')
                    f.write(toStore+'\n') # Write to it
                    f.close() # Close
            else:
                os.mkdir('user_data') # Create folder called user_data
                f = open('user_data/info.txt', 'x') # Open info.txt or create one
                f.write('\n'+toStore) # Write to it
                f.close() # Close
        else:
            f = open('user_data/info.txt', 'w') # Open user_data/info.txt
            f.write('\n'+toStore) # Write
            f.close() # Close
    elif cmd == 'info -g' or cmd == 'info --get': # Get storage data
        try:
            f = open('user_data/info.txt', 'r') # Open
            print(f.read()) # Read
        except:
            print('No info stored')
    elif cmd == 'info -c' or cmd == 'info --clear': # Clear storage data
        f = open('user_data/info.txt', 'w') # Open
        f.write('') # Write blank string to file
        f.close() # Close
    elif cmd == 'info -h' or cmd == 'info --help' or cmd == 'info /?':
        print('Usage:    info [-s] [-g] [-c]\n\n\n\n')
        print('Parameters: \n')
        print('    -s  or  --store            Appends info the before stored info')
        print('    -g  or  --get              Gets all the stored info')
        print('    -o  or  --overwrite        Overwrites all the stored info with the new info')
        print('    -c  or  --clear            Clears stored info\n\n')
    elif cmd == 'time' or cmd == 'date': # Display date and time
        print(dt.datetime.now()) # Print date and time
    elif cmd == 'openLink': # Open link in browser
        print('Link?')
        fopenLink(input()) # Get input and open it in browser
    elif cmd == 'cls' or cmd == 'CLS': # Clear
        print('Loading . . .')
        clear()
    elif cmd == 'exit' or cmd == 'terminate': # Exit program
        break # Exit while loop
    elif cmd == 'exit -f' or cmd == 'exit --force' or cmd == 'terminate -f' or cmd == 'terminate --force':
        exit()
    elif cmd == 'exit /?' or cmd == 'exit -h' or cmd == 'exit --help':
        print('Usage:    exit [-a]\n\n\n\n')
        print('Parameters: \n')
        print('    -f  or  --force     Force exit\n\n')
    elif cmd == 'terminate /?' or cmd == 'terminate -h' or cmd == 'terminate --help':
        print('Usage:    terminate [-a]\n\n\n\n')
        print('Parameters: \n')
        print('    -f  or  --force     Force terminate\n\n')
    elif cmd == 'ping': # Ping server
        print('IP address to ping?')
        ping(input()) # Get input and start ping
    elif cmd == 'ping -s' or cmd == 'ping --self': # Ping self server
        ping(socket.gethostbyname(socket.gethostname())) # Get self server and start ping
    elif cmd == 'systeminfo' or cmd == 'sysinfo':
        print('System information\n')
        print('Full OS name: '+platform.system()+' '+platform.version())
        print('OS name: '+platform.system())
        print('OS version: '+platform.version())
        print('Computer name: '+socket.gethostname())
        print('Username: '+getpass.getuser())
        print('Timezone: '+strftime('%Z', gmtime()))
        print('Logical processors: '+str(multiprocessing.cpu_count()))
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print('IP address: '+ip+'\n')
    elif cmd == 'systeminfo -a' or cmd == 'systeminfo --alt' or cmd == 'sysinfo -a' or cmd == 'sysinfo --alt':
        print('You are on '+platform.system()+' version '+platform.release()+' using the computer name '+socket.gethostname()+' and user '+getpass.getuser()+', in the timezone '+strftime('%Z', gmtime())+', and with '+str(multiprocessing.cpu_count())+' logical processors ')
    elif cmd == 'systeminfo -h' or cmd == 'systeminfo --help' or cmd == 'systeminfo /?' or cmd == 'sysinfo -h' or cmd == 'sysinfo --help' or cmd == 'sysinfo /?':
        print('Usage:    systeminfo [-a]\n\n\n\n')
        print('Parameters: \n')
        print('    -a  or  --alt      Prints systeminfo another way\n\n')
    elif cmd == 'shutdown': # Shutdown computer
        if __os__ == 'nt': # Windows
            os.system('shutdown -s')
        else: # Linux and Mac OS X
            os.system('sudo shutdown now')
    elif cmd == 'restart': # Restart computer
        if __os__ == 'nt': # Windows
            os.system('shutdown -r')
        else: # Linux and Mac OS X
            os.system('sudo shutdown -r')
    elif cmd == 'reset':
        clear() # Clear
        title() # Print start title
    elif cmd == 'echo': # Echo message
        print(input())
    elif cmd == 'copy': # Copy a file
        print('Full file or directory name to copy?')
        toCopy = input() # Get file
        print('Directory path to copy it to?')
        toCopyDir = input() # Get directory path to copy to
        try:
            shutil.copy(toCopy, toCopyDir) # Copy
        except:
            print('Error! Please try again') # Error
    elif cmd == 'find': # Find text in a file
        print('Full file or directory path to find text?')
        toFind = input() # Get file
        if fileExists(toFind):
            print('Text to find?')
            toFindTxt = input() # Get text to find
            try:
                f = open(toFind, 'r') # Open file
                toFindStr = f.read() # Read from file
                print('First appearance of the word '+toFindTxt+' is found at character '+str(toFindStr.find(toFindTxt))) # Print results
            except:
                print('Error! Please try again') # Error
        else:
            print('File does not exist!')
    elif cmd == 'color': # Switch color
        print('Colors:') # Ask color
        print('0 = Black       8 = Gray') # Show colors
        print('1 = Blue        9 = Light Blue')
        print('2 = Green       A = Light Green')
        print('3 = Aqua        B = Light Aqua')
        print('4 = Red         C = Light Red')
        print('5 = Purple      D = Light Purple')
        print('6 = Yellow      E = Light Yellow')
        print('7 = White       F = Bright White')
        print('Background color?')
        bgColor = input() # Get background color
        print('Text color (foreground)?')
        fgColor = input() # Get foreground color
        try: # Try switch color
            os.system('color '+bgColor+fgColor) # Switch color
            if fileExists('user_data'): # Check if folder user_data exists
                if fileExists('user_data/settings/color.txt'): # Check if settings/color.txt in user_data exists
                    f = open('user_data/settings/color.txt', 'w') # Open file
                    f.write('color '+bgColor+fgColor) # Write
                    f.close() # Close
                else:
                    f = open('user_data/settings/color.txt', 'x') # Create file
                    f.write('color '+bgColor+fgColor) # Write
                    f.close() # Close
            else:
                os.mkdir('user_data') # Create folder
                f = open('user_data/settings/color.txt', 'x') # Create file
                f.write('color '+bgColor+fgColor) # Write
                f.close() # Close
        except: # Except
            print('Error! Please try again') # Error
    elif cmd == 'delDir' or cmd == 'rm': # Delete directory
        print('Directory of the folder to delete? Example: C:\\Users\\exampleUser\\Documents\\New_Folder')
        toDelDir = input() # Get directory
        if fileExists(toDelDir): # Check if directory exists
            try:
                os.rmdir(toDelDir) # Remove directory
            except:
                print('Error! Please make sure that directory/folder is not being used by another program!')
        else:
            print('Not a valid directory of a folder!') # Error
    elif cmd == 'rename': # Rename file
        print('Full directory path of the file to rename? Example: C:\\Users\\exampleUser\\Documents\\original_file_name.txt')
        toRename = input() # Get old file name
        print('Full new directory path for the file? Example: C:\\Users\\exampleUser\\Documents\\new_file_name.txt')
        toRenameName = input() # Get new file name
        try:
            os.rename(toRename, toRenameName) # Rename
        except:
            print('Error! Please try again') # Error
    elif cmd == 'dir' or cmd == 'ls': # Directory
        print('Directory?')
        dir = input() # Get directory
        try: # Try code
            print(', '.join(os.listdir(dir))) # Print directory
        except: # Error
            print('Something went wrong! Please try again! Make sure the directory exists!') # Error
    elif cmd == 'dir /' or cmd == 'dir \\': # Root directory
        print(', '.join(os.listdir(dir))) # Print directory
    elif cmd == 'print': # Print
        print(input()) # Get thing to print and print
    elif cmd == 'dirRoot': # Directory of root
        print(', '.join(os.listdir('\\'))) # List
    elif cmd == 'cmd': # Open cmd
        if platform.system() == 'Windows': # Check if os is Windows
            os.system('start cmd') # Open cmd
        else: # Is not Windows
            print('Error! The "cmd" function only works for Windows!')
    elif cmd == 'ip': # Get IP address
        hostname = socket.gethostname() # Get hostname
        ip = socket.gethostbyname(hostname) # Get IP address
        print(ip) # Return/print IP address
    elif cmd == 'openWindow': # Open window with Tkinter
        print('Window name?') # Ask window name
        windowName = input() # Get window name
        window = tkinter.Tk() # Setup variable
        window.title(windowName) # Set title
        window.mainloop() # Open
    elif cmd == 'changePrompt' or cmd == 'prompt': # Change command prompt
        print('New prompt?') # Ask for new prompt
        prompt = input() # Get new prompt
        try: # Test code
            if fileExists('user_data'): # Check if folder user_data exists
                if fileExists('user_data/settings/prompt.txt'): # Check if settings/prompt.txt in user_data exists
                    f = open('user_data/settings/prompt.txt', 'w') # Open file
                    f.write(prompt) # Write
                    f.close() # Close
                else:
                    f = open('user_data/settings/prompt.txt', 'x') # Create file
                    f.write(prompt) # Write
                    f.close() # Close
            else:
                os.mkdir('user_data') # Create folder
                f = open('user_data/settings/prompt.txt', 'x') # Create file
                f.write(prompt) # Write
                f.close() # Close
        except: # Except
            continue # Error
    elif cmd == 'exists': # Check if directory or folder exists
        print('Directory of file or folder?')
        print(fileExists(input()))
    elif cmd == 'repo': # Open PyTerm's repository on GitHub
        fopenLink('https://github.com/Totoro700/PyTerm/')
    elif cmd == 'math -a' or cmd == 'math --add': # Add
        print('Number one -> ', end='') # Get number one
        try:
            numOne = flt(input()) # Try to get input as float
        except:
            print('Error! Please make sure you entered a valid number') # Error
            continue
        print('Number two -> ', end='') # Get number two
        try:
            numTwo = flt(input()) # Try to get input as float
        except:
            print('Error! Please make sure you entered a valid number') # Error
            continue
        print(str(numOne)+' + '+str(numTwo)+' = '+str(numOne + numTwo)) # Calculate and output answer
    elif cmd == 'math -s' or cmd == 'math --subtract': # Subtract
        print('Number one -> ', end='') # Get number one
        try:
            numOne = flt(input()) # Try to get input as float
        except:
            print('Error! Please make sure you entered a valid number') # Error
            continue
        print('Number two -> ', end='') # Get number two
        try:
            numTwo = flt(input()) # Try to get input as float
        except:
            print('Error! Please make sure you entered a valid number') # Error
            continue
        print(str(numOne)+' - '+str(numTwo)+' = '+str(numOne - numTwo)) # Calculate and output answer
    elif cmd == 'math -m' or cmd == 'math --multiply': # Multiply
        print('Number one -> ', end='') # Get number one
        try:
            numOne = flt(input()) # Try to get input as float
        except:
            print('Error! Please make sure you entered a valid number') # Error
            continue
        print('Number two -> ', end='') # Get number two
        try:
            numTwo = flt(input()) # Try to get input as float
        except:
            print('Error! Please make sure you entered a valid number') # Error
            continue
        print(str(numOne)+' * '+str(numTwo)+' = '+str(numOne * numTwo)) # Calculate and output answer
    elif cmd == 'math -d' or cmd == 'math --divide': # Divide
        print('Number one -> ', end='') # Get number one
        try:
            numOne = flt(input()) # Try to get input as float
        except:
            print('Error! Please make sure you entered a valid number') # Error
            continue
        print('Number two -> ', end='') # Get number two
        try:
            numTwo = flt(input()) # Try to get input as float
        except:
            print('Error! Please make sure you entered a valid number') # Error
            continue
        try:
            print(str(numOne)+' / '+str(numTwo)+' = '+str(numOne / numTwo)) # Try to calculate and output answer
        except ZeroDivisionError: # Divisor is zero
            print('Error! Please make sure the divisor isn\'t zero!') # Error
        except: # Error
            print('Error! Please try again!')
    elif cmd == 'math -h' or cmd == 'math --help' or cmd == 'math /?' or cmd == 'math -?' or cmd == 'math': # Math help
        print('\nUsage:    math [-a | -s | -m | -d] \n\n\n\n')
        print('    -a  or  --add        Adds two numbers')
        print('    -s  or  --subtract   Subtracts two numbers')
        print('    -m  or  --multiply   Multiplies two numbers')
        print('    -d  or  --divide     Divides two numbers\n\n')
    elif cmd == 'ver' or cmd == 'version': # Program version
        print('PyTerm v0.5.1')
    elif cmd == 'notepad':  # Open Windows notepad
        if __os__ == 'Windows': # Check if OS is Windows
            sp.Popen('notepad.exe') # subprocess.Popen
        else:
            print('Sorry, notepad is only for Windows!') # Error
    elif cmd == 'py': # Python
        if __os__ == 'Windows':
            os.system('start cmd /c py')
        else:
            print('Sorry, the "py" command is only for Windows!')
    elif cmd == 'license': # Open license
        if fileExists('../LICENSE.txt'): # Check if exists
            print(open('../LICENSE.txt', 'r').read()) # Find, read, and output
        else:
            print('Could not find license!') # Error
    elif cmd == 'os': # OS
        print(platform.system())
    elif cmd == 'osver': # OS version
        print(platform.version())
    elif cmd == 'netstat': # Network status
        print(os.system('netstat'))
    elif cmd == 'diskpart': # Diskpart
        if __os__ == 'Windows': # Check if OS is Windows
            os.system('diskpart') # Open diskpart in cmd
        else:
            print('Error!, diskpart is only for Windows') # Not Windows
    elif cmd == 'TASKKILL': # Force kill a task
        print('Program file name -> ', end='') # Get program name
        toTaskkill = input()
        os.system("taskkill /F /im "+toTaskkill) # Taskkill
    elif cmd == 'runPy': # Run python script
        print('Directory of Python file to run -> ', end='') # Get file
        try:
            if __os__ == 'Windows': # For Windows
                os.system('start cmd /c py '+input())
            elif __os__ == 'Linux': # For Linux
                os.system('start gnome-terminal python '+input())
            elif __os__ == 'Darwin': # For Mac OS
                os.system('start open -a Terminal python '+input())
            else:
                print('OS is not recognized!')
        except:
            print('Error! Please try again!')
    elif cmd == 'move': # Move file
        print('Path/directory to current file to move -> ', end='') # Get current file
        curFil = input()
        if fileExists(curFil): # CHeck if current file exists
            print('Path/directory to new file -> ', end='') # New file
            try:
                os.rename(curFil, input()) # Try move using os.rename
            except:
                print('Error! Make sure both directories are valid and no programs are using the file.') # Error
        else:
            print('That file does not exists! Please try again') # File does not exists
    elif cmd == 'tree': # Tree
        print('Directory (backslash for root) -> ', end='') # Get directory
        os.system('tree '+str(input())) # Output
    elif cmd == 'pyver': # Python version
        print('Python '+platform.python_version())
    elif cmd == 'npm install': # Install package via npm
        print('Package name?')
        pkgName = input() # Get pkg name
        os.system('npm install '+pkgName)
    elif cmd == 'npm upgrade' or cmd == 'npm install -U' or cmd == 'npm update': # Update/upgrade package via npm
        print('Package name?')
        pkgName = input() # Get pkg name
        os.system('npm install '+pkgName)
    elif cmd == 'pip install': # Install package via pip
        print('Package name?')
        pkgName = input() # Get pkg name
        os.system('pip install '+pkgName)
    elif cmd == 'pip install -U' or cmd == 'pip update' or cmd == 'pip upgrade': # Update/upgrade package via pip
        print('Package name?')
        pkgName = input() # Get pkg name
        os.system('pip install -U '+pkgName)
    elif cmd == 'git clone': # Clone Git repository using url
        print('Repository url?')
        repoURL = input('') # Get repository URL
        print('Directory to clone it to?')
        repoPath = input('') # Get directory to clone repo to
        print('Name to clone it as?')
        repoName = input('') # Name to clone the repo as
        try:
            os.system('cd '+repoPath+' & git clone '+repoURL+' '+repoName)
        except:
            print('Error! Please make sure the directory and repository url is valid!')
    elif cmd == 'title': # Change console title
        if __os__ == 'Windows':
            print('New title -> ', end='')
            ctypes.windll.kernel32.SetConsoleTitleW(input())
        else:
            print('This function is only for Windows!')
    elif cmd == '' or cmd == None: # Empty input
        continue # Continue
    else: # Is not a command
        print('Python '+platform.python_version()+' -> PyTerm -> "'+cmd+'" is not a command! Type "help" for some commands to use!') # Error
#   Get Python version  ^                        Get the command name  ^
