import secrets #substitute for random
import argparse # for cli arguments parser
import InquirerPy #for interactive CLI
import string
import sys

flags = {
    "lowercase": True,
    "uppercase": True,
    "digits": True,
    "punctuations": True,
    "require-all": False,
    "copy": False,
    "count": 1
}

parser = argparse.ArgumentParser(description="Password Generator")

parser.add_argument("--len", type=int, default=12)
parser.add_argument("--remove", nargs="+", choices=["lowercase", "uppercase", "digits", "punctuations"], help="Remove certain charsets from passwd like digits, uppercase")
parser.add_argument("--require-all", action="store_true", help="ensures at least one occurrence of all characters from the charsets that are not excluded")
parser.add_argument("--count", type=int, default=1, help="generate 'count' numbers of passwd at a time")
parser.add_argument("--copy", action="store_true", help="directly copy the generated passwd to clipboard")
parser.add_argument("--exclude", help="exclude specific character. pass excluded characters as \"all-character\"")

args = parser.parse_args()

if len(sys.argv) > 1:
    flags["require-all"] = args.require_all
    flags["copy"] = args.copy
    flags["count"] = args.count
    for i in (args.remove or []):
        flags[i] = False

    lowercase = string.ascii_lowercase if flags["lowercase"] == True else ""
    uppercase = string.ascii_uppercase if flags["uppercase"] == True else ""
    digits = string.digits if flags["digits"] == True else ""
    punctuations = string.punctuation if flags["punctuations"] == True else ""

    superString = lowercase + uppercase + digits + punctuations
    if args.exclude != None:
        superString = "".join(set(superString) - set(args.exclude))

    passwd = "".join(secrets.choice(superString) for _ in range(args.len))

else:
    '''
    pending logic using inquirerPy
    ask user for len of passwd, default 12
    ask user for charsets to include, default include all (lowercase, uppercase, digits and punctuations)
    ask user count of passwd per generation
    ask user does he/she wants to copy passwd directly to clipboard. Only ask if count == 1 
    '''
    pass

print(passwd)