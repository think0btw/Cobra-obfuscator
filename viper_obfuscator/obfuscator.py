#obfuscator
import marshal
import base64
from pathlib import Path

filtre = [
    100,
    100.0,
    100 + 0j,
    True,
    "100",
    b"100",
    bytearray(b"100"),
    [100],
    (100,),
    {100},
    frozenset([100]),
    {"valeur": 100},
    None,
    slice(100)
]

filesPath = Path("mon_code.py")
print ("Enter the files PATH:")
filesPath =input(filesPath)

if filesPath.suffix == ".py":
    with open(filesPath, "wb") as f :
        marshal.dump(filtre,f)