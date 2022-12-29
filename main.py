"""password locker"""

import sys
import pyperclip

print("Hello World!")


passwords = {
    "email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
    "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
    "luggage": "12345"
}

if len(sys.argv) < 2:
    print("Usage: python main.py [account] - copy account password")
    sys.exit()


account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print("Password for " + account + "Copied to clipboard")
else:
    print("Account: " + account + " variance not detected!")





