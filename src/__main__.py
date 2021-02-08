# __main__.py
# Import
# os for file commands and others, time for wait second, platform for os command, multiprocessing for CPU count
import os, time, platform, shutil, socket, getpass, multiprocessing, tkinter, sys, ctypes
import webbrowser as web # Webbrowser for openLink command
import subprocess as sp # Subprocess for ping
import datetime as dt # Datetime for date and time
from time import gmtime, strftime

__cache__ = 0 # Set cache to 0
prompt = '' # Setup prompt variable
__os__ = platform.system() # Get operating system name and store it in a variable (const)

def p(msg, end='\n'): # Alternative to print
    print(msg, end)

# Print version and title as function
def title():
    p('@------------------------------------------------------------------------------------@')
    p('|                                                                                    |')
    p('|                                  |PyTerm v0.5.1|                                   |')
    p('|                                                                                    |')
    p('@------------------------------------------------------------------------------------@')

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
    try: # Try read files
        f = open('user_data/settings/color.txt', 'r') # Open files
        os.system(f.read()) # Read
    except: # Does not exist/ or some other error
        os.system('color 0A') # Default color, black green


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
                    cache.close()
            else:
                cache = open('user_data/cache.txt', 'x')
                cache.write('1')
                __cache__ = 0
                cache = close()
        else:
            os.mkdir('user_data')
            cache = open('user_data/cache.txt', 'x')
            cache.write('1')
            __cache__ = 0
            cache.close()
    except:
        p('Error')
    
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
    p('Loading . . .')
    cache()
    p('Loading color . . .')
    setupColor()
    p('Setting up . . .')
    promptUpdate()
    clear()
    title()

init()

# Main loop
while True:
    p(prompt+' ', end='') # Input prompt without line break ( \n )
    cmd = input() # Collect input
    if cmd == 'help':
        p('changelog                               Shows PyTerm\'s change log')
        p('color                                   Changes the text and the background color')
        p('copy                                    Copies a file')
        p('curDir                                  Displays the current directory')
        p('date                                    Shows the date and time')
        p('del                                     Deletes a file')
        p('delDir                                  Deletes a directory/folder')
        p('dir                                     Displays a list of files and subdirectories in a directory.')
        p('dirRoot                                 Displays a list of files and subdirectories in the root directory.')
        p('diskpart                                Displays or configures Disk Partition properties')
        p('echo                                    Displays messages you enter')
        p('exists                                  Checks if a file or folder exists')
        p('exit                                    Exits the program')
        p('find                                    Finds a specific text in a file')
        p('help                                    Displays this help message')
        p('info                                    Stores info')
        p('info -c                                 Clear stored info')
        p('info -g                                 Get stored info')
        p('ip                                      Displays your computer\'s IP address')
        p('licenes                                 Shows PyTerm\'s license ')
        p('md                                      Creates a directory')
        p('math -a                                 Adds two numbers together')
        p('math -s                                 Subtracts two numbers')
        p('math -m                                 Multiplies two numbers')
        p('math -d                                 Divides two numbers')
        p('mkdir                                   Creates a directory')
        p('mkfil                                   Creates a file')
        p('netstat                                 Displays protocol statistics and current TCP/IP network connections')
        p('notepad                                 [Windows] Opens Windows Notepad')
        p('npm install                             Install npm package')
        p('npm update                              Update npm package')
        p('npm upgrade                             Upgrade npm package')
        p('openLink                                Opens a link in your browser')
        p('openWindow                              Opens a window')
        p('ping                                    Pings a server with an IP address')
        p('pip install                             Installs pip package')
        p('pip install -U                          Updates pip package')
        p('print                                   Displays messages you enter')
        p('prompt                                  Changes the prompt')
        p('py                                      [Windows] Opens Python\'s interpreter in cmd in a new window')
        p('pyver                                   Displays Python version')
        p('readBinFil                              Reads a binary file')
        p('readFil                                 Reads a file')
        p('rename                                  Renames a file')
        p('repo                                    Opens the GitHub repository')
        p('reset                                   Resets to the title screen')
        p('restart                                 Restarts your computer')
        p('shutdown                                Shutdown your computer')
        p('sysinfo                                 Shows your computer\'s infomation')
        p('systeminfo                              Shows your computer\'s infomation')
        p('terminate                               Exits the program')
        p('TASKKILL                                Kill or stop a running process or application.')
        p('time                                    Also shows date and time')
        p('title                                   [Windows] Changes the console title')
        p('tree                                    Graphically displays the directory structure of a drive or path')
        p('\nRead the docs for more commands\n')
    elif cmd == 'help -a' or cmd == 'help --alt': # Help
        p('changelog                                                       Shows PyTerm\'s change log (../change.log)')
        p('color                                                            Changes the text and the background color')
        p('copy                                                                                         Copies a file')
        p('curDir                                                                      Displays the current directory')
        p('date                                                                               Shows the date and time')
        p('del                                                                                         Deletes a file')
        p('delDir                                                                          Deletes a directory/folder')
        p('dir                                            Displays a list of files and subdirectories in a directory.')
        p('dirRoot                                 Displays a list of files and subdirectories in the root directory.')
        p('diskpart                                                  Displays or configures Disk Partition properties')
        p('echo                                                                           Displays messages you enter')
        p('exists                                                                   Checks if a file or folder exists')
        p('exit                                                                                     Exits the program')
        p('find                                                                       Finds a specific text in a file')
        p('help                                                                            Displays this help message')
        p('info                                                                                           Stores info')
        p('info -c                                                                                  Clear stored info')
        p('info -g                                                                                    Get stored info')
        p('ip                                                                    Displays your computer\'s IP address')
        p('licenes                                                           Shows PyTerm\'s license (../LICENSE.txt)')
        p('math -a                                                                          Adds two numbers together')
        p('math -s                                                                              Subtracts two numbers')
        p('math -m                                                                             Multiplies two numbers')
        p('math -d                                                                                Divides two numbers')
        p('md                                                                                     Creates a directory')
        p('mkdir                                                                                  Creates a directory')
        p('mkfil                                                                                       Creates a file')
        p('netstat                                Displays protocol statistics and current TCP/IP network connections')
        p('notepad                                                                    [Windows] Opens Windows Notepad')
        p('npm install                                                                            Install npm package')
        p('npm update                                                                              Update npm package')
        p('npm upgrade                                                                            Upgrade npm package')
        p('openLink                                                                      Opens a link in your browser')
        p('openWindow                                                                                  Opens a window')
        p('systeminfo                                                            Shows information about you computer')
        p('ping                                                                     Pings a server with an IP address')
        p('print                                                                          Displays messages you enter')
        p('prompt                                                                                  Changes the prompt')
        p('pip install                                                                           Installs pip package')
        p('pip install -U                                                                         Updates pip package')
        p('py                                            [Windows] Opens Python\'s interpreter in cmd in a new window')
        p('pyver                                                                              Displays Python version')
        p('readFil                                                                                       Reads a file')
        p('readBinFil                                                                             Reads a binary file')
        p('rename                                                                                      Renames a file')
        p('reset                                                                           Resets to the title screen')
        p('repo                                                                           Opens the GitHub repository')
        p('restart                                                                             Restarts your computer')
        p('shutdown                                                                            Shutdown your computer')
        p('systeminfo                                                               Shows your computer\'s infomation')
        p('terminate                                                                                Exits the program')
        p('TASKKILL                                                    Kill or stop a running process or application.')
        p('time                                                                              Also shows date and time')
        p('title                                                                  [Windows] Changes the console title')
        p('tree                                       Graphically displays the directory structure of a drive or path')
        p('\nRead the docs for more commands\n')
    elif cmd == 'help -h' or cmd == 'help --help' or cmd == 'help /?':
        p('Usage:    help [-a]\n\n\n\n')
        p('Parameters: \n')
        p('    -a  or  --alt      Prints help message another way\n\n')
    elif cmd == 'mkdir' or cmd == 'md': # Make directory
        p('Directory name?')
        try:
            os.mkdir(input())
        except:
            p('Error! Please try again and make sure that it is a valid directory name and it doesn\'t already exists!')
    elif cmd == 'mkfil': # Make file
        p('Full file name? (eg. "text.txt" or "index.html" or "python.py"). This file will be placed next to the program')
        fileName = input()
        try:
            f = open(fileName, 'x') # Try to open file
            p('Successfully created '+fileName)
            f.close() # Close file
        except:
            p('Error! Please try again and make sure that it is a valid file name and it doesn\'t already exists!')
    elif cmd == 'readFil': # Read file
        p('Full file name or directory? (eg. "text.txt" or "C:\\Python\\python.py")')
        toOpen = input() # Get file name
        if fileExists(toOpen):
            f = open(toOpen, 'r') # Open file
            p(f.read()) # Read file
        else:
            p('The file does not exist!') # File does not exist
    elif cmd == 'readBinFil': # Read binary file
        p('WARNING: This command may output a lot of text')
        p('Full binary file name or directory? (eg. "cmd.exe" or "C:\\Python\\python.dll")')
        toOpen = input() # Collect full directory or full file name
        p('Loading . . .')
        time.sleep(3)
        if fileExists(toOpen): # See if file exsits
            f = open(toOpen, 'rb') # Open/read binary file
            p(f.read()) # Display file
        else:
            p('The file does not exist!')
    elif cmd == 'curDir': # Current directory
        p(os.path.dirname(os.path.abspath(__file__)))
    elif cmd == 'del' or cmd == 'delete': # Delete
        p('Full file name or directory to delete? (eg. "text.txt" or "C:\\Trash\\text.txt")')
        toDel = input() # Collect directory or file name
        try: # Try if to delete the file
            if fileExists(toDel): # See if file exsits
                try:
                    os.remove(toDel)
                    p('Successfully deleted '+toDel)
                except:
                    p('Error! Please make sure that the file in not in use by another program!')
            else:
                p('The file does not exist!')
        except: # The user might have typed a folder name or the access is deined
            p('Something went wrong! Make sure it\'s a file, not a folder, with it\'s file extension and this program has access to it!')
    elif cmd == 'info' or cmd == 'info -s' or cmd == 'info --store': # Store data
        p('Info to store?')
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
        p('Info to overwrite?')
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
            p(f.read()) # Read
        except:
            p('No info stored')
    elif cmd == 'info -c' or cmd == 'info --clear': # Clear storage data
        f = open('user_data/info.txt', 'w') # Open
        f.write('') # Write blank string to file
        f.close() # Close
    elif cmd == 'info -h' or cmd == 'info --help' or cmd == 'info /?':
        p('Usage:    info [-s] [-g] [-c]\n\n\n\n')
        p('Parameters: \n')
        p('    -s  or  --store            Appends info the before stored info')
        p('    -g  or  --get              Gets all the stored info')
        p('    -o  or  --overwrite        Overwrites all the stored info with the new info')
        p('    -c  or  --clear            Clears stored info\n\n')
    elif cmd == 'time' or cmd == 'date': # Display date and time
        p(dt.datetime.now()) # Print date and time
    elif cmd == 'openLink': # Open link in browser
        p('Link?')
        fopenLink(input()) # Get input and open it in browser
    elif cmd == 'cls' or cmd == 'CLS': # Clear
        p('Loading . . .')
        clear()
    elif cmd == 'exit' or cmd == 'terminate': # Exit program
        break # Exit while loop
    elif cmd == 'exit -f' or cmd == 'exit --force' or cmd == 'terminate -f' or cmd == 'terminate --force':
        exit()
    elif cmd == 'exit /?' or cmd == 'exit -h' or cmd == 'exit --help':
        p('Usage:    exit [-a]\n\n\n\n')
        p('Parameters: \n')
        p('    -f  or  --force     Force exit\n\n')
    elif cmd == 'terminate /?' or cmd == 'terminate -h' or cmd == 'terminate --help':
        p('Usage:    terminate [-a]\n\n\n\n')
        p('Parameters: \n')
        p('    -f  or  --force     Force terminate\n\n')
    elif cmd == 'ping': # Ping server
        p('IP address to ping?')
        ping(input()) # Get input and start ping
    elif cmd == 'ping -s' or cmd == 'ping --self': # Ping self server
        ping(socket.gethostbyname(socket.gethostname())) # Get self server and start ping
    elif cmd == 'systeminfo' or cmd == 'sysinfo':
        p('System information\n')
        p('Full OS name: '+platform.system()+' '+platform.version())
        p('OS name: '+platform.system())
        p('OS version: '+platform.version())
        p('Computer name: '+socket.gethostname())
        p('Username: '+getpass.getuser())
        p('Timezone: '+strftime('%Z', gmtime()))
        p('Logical processors: '+str(multiprocessing.cpu_count()))
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        p('IP address: '+ip+'\n')
    elif cmd == 'systeminfo -a' or cmd == 'systeminfo --alt' or cmd == 'sysinfo -a' or cmd == 'sysinfo --alt':
        p('You are on '+platform.system()+' version '+platform.release()+' using the computer name '+socket.gethostname()+' and user '+getpass.getuser()+', in the timezone '+strftime('%Z', gmtime())+', and with '+str(multiprocessing.cpu_count())+' logical processors ')
    elif cmd == 'systeminfo -h' or cmd == 'systeminfo --help' or cmd == 'systeminfo /?' or cmd == 'sysinfo -h' or cmd == 'sysinfo --help' or cmd == 'sysinfo /?':
        p('Usage:    systeminfo [-a]\n\n\n\n')
        p('Parameters: \n')
        p('    -a  or  --alt      Prints systeminfo another way\n\n')
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
    elif cmd == 'reset': # Reset text
        clear() # Clear text
        title() # Print start title
    elif cmd == 'echo': # Echo message
        p(input())
    elif cmd == 'copy': # Copy a file
        p('Full file or directory name to copy?')
        toCopy = input() # Get file
        p('Directory path to copy it to?')
        toCopyDir = input() # Get directory path to copy to
        try:
            shutil.copy(toCopy, toCopyDir) # Copy
        except:
            p('Error! Please try again') 
    elif cmd == 'find': # Find text in a file
        p('Full file or directory path to find text?')
        toFind = input() # Get file
        if fileExists(toFind):
            p('Text to find?')
            toFindTxt = input() # Get text to find
            try:
                f = open(toFind, 'r') # Open file
                toFindStr = f.read() # Read from file
                p('First appearance of the word '+toFindTxt+' is found at character '+str(toFindStr.find(toFindTxt))) # Print results
            except:
                p('Error! Please try again') 
        else:
            p('File does not exist!')
    elif cmd == 'color': # Switch color
        p('Colors:') # Ask color
        p('0 = Black       8 = Gray') # Show colors
        p('1 = Blue        9 = Light Blue')
        p('2 = Green       A = Light Green')
        p('3 = Aqua        B = Light Aqua')
        p('4 = Red         C = Light Red')
        p('5 = Purple      D = Light Purple')
        p('6 = Yellow      E = Light Yellow')
        p('7 = White       F = Bright White')
        p('Background color?')
        bgColor = input() # Get background color
        p('Text color (foreground)?')
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
            p('Error! Please try again') 
    elif cmd == 'delDir' or cmd == 'rm': # Delete directory
        p('Directory of the folder to delete? Example: C:\\Users\\exampleUser\\Documents\\New_Folder')
        toDelDir = input() # Get directory
        if fileExists(toDelDir): # Check if directory exists
            try:
                os.rmdir(toDelDir) # Remove directory
            except:
                p('Error! Please make sure that directory/folder is not being used by another program!')
        else:
            p('Not a valid directory of a folder!') 
    elif cmd == 'rename': # Rename file
        p('Full directory path of the file to rename? Example: C:\\Users\\exampleUser\\Documents\\original_file_name.txt')
        toRename = input() # Get old file name
        p('Full new directory path for the file? Example: C:\\Users\\exampleUser\\Documents\\new_file_name.txt')
        toRenameName = input() # Get new file name
        try:
            os.rename(toRename, toRenameName) # Rename
        except:
            p('Error! Please try again') 
    elif cmd == 'dir' or cmd == 'ls': # Directory
        p('Directory?')
        dir = input() # Get directory
        try: # Try code
            p(', '.join(os.listdir(dir))) # Print directory
        except: 
            p('Something went wrong! Please try again! Make sure the directory exists!') 
    elif cmd == 'dir /' or cmd == 'dir \\': # Root directory
        p(', '.join(os.listdir(dir))) # Print directory
    elif cmd == 'print': # Print
        p(input()) # Get thing to print and print
    elif cmd == 'dirRoot': # Directory of root
        p(', '.join(os.listdir('\\'))) # List
    elif cmd == 'cmd': # Open cmd
        if platform.system() == 'Windows': # Check if os is Windows
            os.system('start cmd') # Open cmd
        else: # Is not Windows
            p('Error! The "cmd" function only works for Windows!')
    elif cmd == 'ip': # Get IP address
        hostname = socket.gethostname() # Get hostname
        ip = socket.gethostbyname(hostname) # Get IP address
        p(ip) # Return/print IP address
    elif cmd == 'openWindow': # Open window with Tkinter
        p('Window name?') # Ask window name
        windowName = input() # Get window name
        window = tkinter.Tk() # Setup variable
        window.title(windowName) # Set title
        window.mainloop() # Open
    elif cmd == 'changePrompt' or cmd == 'prompt': # Change command prompt
        p('New prompt?') # Ask for new prompt
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
            continue 
    elif cmd == 'exists': # Check if directory or folder exists
        p('Directory of file or folder?')
        p(fileExists(input()))
    elif cmd == 'repo': # Open PyTerm's repository on GitHub
        fopenLink('https://github.com/Totoro700/PyTerm/')
    elif cmd == 'math -a' or cmd == 'math --add': # Add
        p('Number one -> ', end='') # Get number one
        try:
            numOne = flt(input()) # Try to get input as float
        except:
            p('Error! Please make sure you entered a valid number') 
            continue
        p('Number two -> ', end='') # Get number two
        try:
            numTwo = flt(input()) # Try to get input as float
        except:
            p('Error! Please make sure you entered a valid number') 
            continue
        p(str(numOne)+' + '+str(numTwo)+' = '+str(numOne + numTwo)) # Calculate and output answer
    elif cmd == 'math -s' or cmd == 'math --subtract': # Subtract
        p('Number one -> ', end='') # Get number one
        try:
            numOne = flt(input()) # Try to get input as float
        except:
            p('Error! Please make sure you entered a valid number') 
            continue
        p('Number two -> ', end='') # Get number two
        try:
            numTwo = flt(input()) # Try to get input as float
        except:
            p('Error! Please make sure you entered a valid number') 
            continue
        p(str(numOne)+' - '+str(numTwo)+' = '+str(numOne - numTwo)) # Calculate and output answer
    elif cmd == 'math -m' or cmd == 'math --multiply': # Multiply
        p('Number one -> ', end='') # Get number one
        try:
            numOne = flt(input()) # Try to get input as float
        except:
            p('Error! Please make sure you entered a valid number') 
            continue
        p('Number two -> ', end='') # Get number two
        try:
            numTwo = flt(input()) # Try to get input as float
        except:
            p('Error! Please make sure you entered a valid number') 
            continue
        p(str(numOne)+' * '+str(numTwo)+' = '+str(numOne * numTwo)) # Calculate and output answer
    elif cmd == 'math -d' or cmd == 'math --divide': # Divide
        p('Number one -> ', end='') # Get number one
        try:
            numOne = flt(input()) # Try to get input as float
        except:
            p('Error! Please make sure you entered a valid number') 
            continue
        p('Number two -> ', end='') # Get number two
        try:
            numTwo = flt(input()) # Try to get input as float
        except:
            p('Error! Please make sure you entered a valid number') 
            continue
        try:
            p(str(numOne)+' / '+str(numTwo)+' = '+str(numOne / numTwo)) # Try to calculate and output answer
        except ZeroDivisionError: # Divisor is zero
            p('Error! Please make sure the divisor isn\'t zero!') 
        except: 
            p('Error! Please try again!')
    elif cmd == 'math -h' or cmd == 'math --help' or cmd == 'math /?' or cmd == 'math -?' or cmd == 'math': # Math help
        p('\nUsage:    math [-a | -s | -m | -d] \n\n\n\n')
        p('    -a  or  --add        Adds two numbers')
        p('    -s  or  --subtract   Subtracts two numbers')
        p('    -m  or  --multiply   Multiplies two numbers')
        p('    -d  or  --divide     Divides two numbers\n\n')
    elif cmd == 'ver' or cmd == 'version': # Program version
        p('PyTerm v0.5.1')
    elif cmd == 'notepad':  # Open Windows notepad
        if __os__ == 'Windows': # Check if OS is Windows
            sp.Popen('notepad.exe') # subprocess.Popen
        else:
            p('Sorry, notepad is only for Windows!') 
    elif cmd == 'py': # Python
        if __os__ == 'Windows':
            os.system('start cmd /c py')
        else:
            p('Sorry, the "py" command is only for Windows!')
    elif cmd == 'license': # Open license
        if fileExists('../LICENSE.txt'): # Check if exists
            p(open('../LICENSE.txt', 'r').read()) # Find, read, and output
        else:
            p('Could not find license!') 
    elif cmd == 'os': # OS
        p(platform.system())
    elif cmd == 'osver': # OS version
        p(platform.version())
    elif cmd == 'netstat': # Network status
        p(os.system('netstat'))
    elif cmd == 'diskpart': # Diskpart
        if __os__ == 'Windows': # Check if OS is Windows
            os.system('diskpart') # Open diskpart in cmd
        else:
            p('Error!, diskpart is only for Windows') # Not Windows
    elif cmd == 'TASKKILL': # Force kill a task
        p('Program file name -> ', end='') # Get program name
        toTaskkill = input()
        os.system("taskkill /F /im "+toTaskkill) # Taskkill
    elif cmd == 'runPy': # Run python script
        p('Directory of Python file to run -> ', end='') # Get file
        try:
            if __os__ == 'Windows': # For Windows
                os.system('start cmd /c py '+input())
            elif __os__ == 'Linux': # For Linux
                os.system('start gnome-terminal python '+input())
            elif __os__ == 'Darwin': # For Mac OS
                os.system('start open -a Terminal python '+input())
            else:
                p('OS is not recognized!')
        except:
            p('Error! Please try again!')
    elif cmd == 'move': # Move file
        p('Path/directory to current file to move -> ', end='') # Get current file
        curFil = input()
        if fileExists(curFil): # CHeck if current file exists
            p('Path/directory to new file -> ', end='') # New file
            try:
                os.rename(curFil, input()) # Try move using os.rename
            except:
                p('Error! Make sure both directories are valid and no programs are using the file.') 
        else:
            p('That file does not exists! Please try again') # File does not exists
    elif cmd == 'tree': # Tree
        p('Directory (backslash for root) -> ', end='') # Get directory
        os.system('tree '+str(input())) # Output
    elif cmd == 'pyver': # Python version
        p('Python '+platform.python_version())
    elif cmd == 'npm install': # Install package via npm
        p('Package name?')
        pkgName = input() # Get pkg name
        os.system('npm install '+pkgName)
    elif cmd == 'npm upgrade' or cmd == 'npm install -U' or cmd == 'npm update': # Update/upgrade package via npm
        p('Package name?')
        pkgName = input() # Get pkg name
        os.system('npm install '+pkgName)
    elif cmd == 'pip install': # Install package via pip
        p('Package name?')
        pkgName = input() # Get pkg name
        os.system('pip install '+pkgName)
    elif cmd == 'pip install -U' or cmd == 'pip update' or cmd == 'pip upgrade': # Update/upgrade package via pip
        p('Package name?')
        pkgName = input() # Get pkg name
        os.system('pip install -U '+pkgName)
    elif cmd == 'git clone': # Clone Git repository using url
        p('Repository url?')
        repoURL = input('') # Get repository URL
        p('Directory to clone it to?')
        repoPath = input('') # Get directory to clone repo to
        p('Name to clone it as?')
        repoName = input('') # Name to clone the repo as
        try:
            os.system('cd '+repoPath+' & git clone '+repoURL+' '+repoName)
        except:
            p('Error! Please make sure the directory and repository url is valid!')
    elif cmd == 'title': # Change console title
        if __os__ == 'Windows': # Check if OS is Windows
            p('New title -> ', end='') # Get new title
            ctypes.windll.kernel32.SetConsoleTitleW(input()) # Set title
        else: # Not Windows
            p('This function is only for Windows!')
    elif cmd == 'msgbox':
        if __os__ == 'Windows': 
            p('Title -> ', end='')
            title = input()
            p('Message -> ', end='')
            try:
                ctypes.windll.user32.MessageBoxW(0, input(), title, 0)
            except:
                p('Something went wrong! This may be an issue of your Windows computer, it may be to old for this feature')
        else:
            p('This function is only for Windows!')
    elif cmd == 'openFil': # Open a file
        p('Path to file -> ', end='') # Get filename
        fileName = input()
        if fileExists(fileName): # Check if file exists
            try:
                sp(['open', fileName], check=True) # Open file
            except:
                p('Error! Something went wrong! Please try again!')
        else:
            p('That file does not exist! Please try again with another file')
    elif cmd == '' or cmd == None: # Empty input
        continue # Continue
    else: # Is not a command
        p('Python '+platform.python_version()+' -> PyTerm -> "'+cmd+'" is not a command! Type "help" for some commands to use!') 
#   Get Python version  ^                        Get the command name  ^
