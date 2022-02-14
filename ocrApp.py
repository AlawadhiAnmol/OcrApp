import easyocr
import faulthandler
import sys
faulthandler.enable()

path=sys.argv[1]

# this needs to run only once to load the model into memory
reader = easyocr.Reader(['en'], gpu=False)


results = reader.readtext('/home/anmol/Downloads/b.jpeg', paragraph=True, detail=0)


print(results)