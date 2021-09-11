# ObfuscateProtect
A tool for quickly obfuscating sensitive, violent, or extremist text to protect the researcher or analyst viewing the content - while keeping it in a unique form so that patterns can still be observed.

## Instalation 
```shell
python -m pip install git+https://github.com/CartographerLabs/ObfuscateProtect.git
```

## Usage 
Simple Python usage to view the conversion name in the verbose log output:
```python
from ObfuscateProtect.ObfuscateProtect import ObfuscateProtect
obfuscator = ObfuscateProtect()
obfuscator.obfuscate("string", verbose=True)
```
Output:
```bash
Plain text 'string' obfuscated to '0a77d64c35ea4a2ea658b2e8fc5d8c26', using mode 'uuid'.
```
More complex, using a list of names:
```python
from ObfuscateProtect.ObfuscateProtect import ObfuscateProtect

list_of_bad_username = ["John","Steve","Chloe","Ishaan"]

obfuscator = ObfuscateProtect()

good_usernames = []
for username in list_of_bad_username:
    good_usernames.append(obfuscator.obfuscate(username, mode=2))

print(good_usernames)
```
Output:
```bash
['GREEN-BOWL', 'VIOLET-FRUIT', 'BLUE-PLANET', 'PURPLE-UNCLE']
```

### Modes
Currently this tooling supports two modes, of which can be provided to the ```obfuscate``` function via the ```mode``` paramiter. Mode 1 obfuscates all text to a UUID, while mode 2 will obfuscate all text to a color-word name paring. 
