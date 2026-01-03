import secrets #substitute for random
import argparse # for cli arguments parser
from InquirerPy import prompt#for interactive CLI
from InquirerPy.validator import NumberValidator
import string
import sys
import pyperclip as pc

flags = {
    "len" : 12,
    "lowercase": True,
    "uppercase": True,
    "digits": True,
    "punctuations": True,
    "require-all": False,
    "copy": False,
    "count": 1
}

passgen = lambda len, superString: "".join(secrets.choice(superString) for _ in range(len))

def genSuperString(exclude):
    lowercase = string.ascii_lowercase if flags["lowercase"] == True else ""
    uppercase = string.ascii_uppercase if flags["uppercase"] == True else ""
    digits = string.digits if flags["digits"] == True else ""
    punctuations = string.punctuation if flags["punctuations"] == True else ""

    superString = lowercase + uppercase + digits + punctuations
    if exclude != None:
        superString = "".join(set(superString) - set(exclude))

    return superString

copyToClipboard = lambda text: pc.copy(text)

parser = argparse.ArgumentParser(description="Password Generator")

parser.add_argument("--len", type=int, default=12, help="to specify the password length")
parser.add_argument("--remove", nargs="+", choices=["lowercase", "uppercase", "digits", "punctuations"], help="to specify certain charsets not to include in password like digits, uppercase")
parser.add_argument("--exclude", help="exclude specific character. pass excluded characters as \"all-character\"")
parser.add_argument("--require-all", action="store_true", help="ensures at least one occurrence of all characters from the included charsets")
parser.add_argument("--count", type=int, default=1, help="specify the 'count' for multiple password generation")
parser.add_argument("--copy", action="store_true", help="directly copy the generated passwd to clipboard")

args = parser.parse_args()

if len(sys.argv) > 1:
    flags["require-all"] = args.require_all
    flags["copy"] = args.copy
    flags["count"] = args.count
    flags["len"] = args.len
    for i in (args.remove or []):
        flags[i] = False

    superString = genSuperString(args.exclude) 

    passwd = [passgen(flags["len"], superString) for i in range(flags["count"])]
    '''  👆this one liner can be written as 👇
    for i in range(flags["count"]):
        cur_pwd = passgen(flags["len"], superString)
        passwd.append(cur_pwd)
    '''
     
    print("\n".join(passwd))
    
    if flags["count"] == 1 and flags['copy'] == True:
        copyToClipboard(passwd[0])
        print("Password copied to clip")
    
else:

    questions = [
        {
            "type": "number",
            "name": "len",
            "message": "Password length allowed range between 6 to 32: ",
            "validate": NumberValidator(),
            "filter": lambda val: int(val) if val else 12
        },
        {
            "type": "checkbox",
            "name": "include",
            "message": "Choose charaset to include in password:- ",
            "choices": ["lowercase", "uppercase", "digits", "punctuations"]
        },
        {
            "type": "input",
            "name": "exclude",
            "message": "Do you want to exclude certain characters?"
        },
        {
            "type": "confirm",
            "name": "require-all",
            "message": "Ensure at least one character from each selected charset?"
        },
        {
            "type": "number",
            "name": "count",
            "message": "Would you like to generate multiple passwords? If so, enter the count:",
            "validate": NumberValidator(),
            "filter": lambda val: int(val) if val else 1
        },
        {
            "type": "confirm",
            "name": "copy",
            "message": "Copy password to clipboard",
            "default": True,
            "when": lambda result: result["count"] == 1
        }
    ]

    result = prompt(questions)

    for i in ["lowercase", "uppercase", "digits", "punctuations"]:
        if i in result['include']:
            flags[i] = True
        else:
            flags[i] = False
    flags["len"] = result['len']
    flags["copy"] = result['copy']
    flags["count"] = result['count']

    superString = genSuperString(result['exclude'])

    passwd = [passgen(flags["len"], superString) for i in range(flags["count"])]

    print("\n".join(passwd))

    if flags["count"] == 1 and flags['copy'] == True:
        copyToClipboard(passwd[0])
        print("Password copied to clip")