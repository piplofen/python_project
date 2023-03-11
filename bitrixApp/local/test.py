import re
from uuid import getnode as mac

print (':'.join(re.findall('..', '%012x' % mac())))