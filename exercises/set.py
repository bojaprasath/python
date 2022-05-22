a = set()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
import sys
try:
    a.remove(5)
except:
    print(sys.exc_info())
a.discard(5)

