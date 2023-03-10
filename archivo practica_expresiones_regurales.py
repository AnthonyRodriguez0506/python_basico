>>> import rem =  #ModuleNotFoundError: No module named 'rem'
>>> match = re.match('Hello[ \t]*(.*)world', 'Hello')=  #NameError: name 're' is not defined
>>> match.group(1)=  #NameError: name 'match' is not defined
>>> match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')=  #NameError: name 're' is not defined
>>> match.groups()=  #NameError: name 'match' is not defined
>>> re.split('[/:]', '/usr/home/lumberjack')=  #NameError: name 're' is not defined
>>> phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')=  #NameError: name 're' is not defined
>>> mo = phone_num_regex.search('My number is 415-555-4242.')=  #NameError: name 'phone_num_regex' is not defined
>>> print(f'Phone number found: {mo.group()}')=  #SyntaxError: cannot assign to function call
>>> phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')=  #NameError: name 're' is not defined
>>> mo = phone_num_regex.search('My number is 415-555-4242.')=  #NameError: name 'phone_num_regex' is not defined
>>> mo.group(1)=  #NameError: name 'mo' is not defined
>>> mo.group(2)=  #NameError: name 'mo' is not defined
>>> mo.group(0)=  #NameError: name 'mo' is not defined
>>> mo.group()=  #NameError: name 'mo' is not defined
>>> hero_regex = re.compile (r'Batman|Tina Fey')=  #NameError: name 're' is not defined
>>> mo1 = hero_regex.search('Batman and Tina Fey.')=  #NameError: name 'hero_regex' is not defined
>>> mo1.group()= #NameError: name 'mo1' is not defined
>>> mo2 = hero_regex.search('Tina Fey and Batman.')=  #NameError: name 'hero_regex' is not defined
>>> mo2.group()=  #NameError: name 'mo2' is not defined