<p align="center"><img src="https://assets.tryhackme.com/img/THMlogo.png" width="350" title="TryHackMe Logo"></p>
<p align="center">API Py</p>


 
Maintained Python wrapper for TryHackMe public API  
This fork is unofficial and not associated with TryHackMe, but i would love to.

## Installation
```sh
pip install thmapi
```

## Usage
```python
from thmapi import THM

creds = {
    'username': '<USERNAME>', 'password': '<PASSWORD', 
    # username and password are no longer supported please instead use
    'session': '<connect.sid cookie>'
}

thm = THM(credentials=creds) # Logging in is optional

thm.get_stats() # {'publicRooms': 203, 'totalUsers': 88017, 'cloneableRooms': 967}
```
## API documentation
For the API documentation please visit the [TryHackMe-API-Doc](https://github.com/GnarLito/TryHackMe-API-Doc)


## Contributing
You're welcome to create Issues/Pull Requests with features you'd want to see

## License
[MIT LICENSE](https://github.com/szymex73/py-thmapi/blob/master/LICENSE)
