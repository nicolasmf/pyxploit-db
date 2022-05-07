# Pyxploit-db

An exploit-db.com python API using advanced search with all possible filters.

For another project, I needed to make some queries to the exploit database, but I couldn't find any complete API that would allow me to get what I wanted, how I wanted. So I decided to create my own API, and making it as complete as possible, with the maximum of parameters so everyone will find what they need and how they need it.

## Future use

```python
>>> import pyxploitdb
>>> result = pyxploitdb.searchEDB("Gitlab 14.9", platform="ruby", _print=False)
>>> print(result)
[['50888', 'Gitlab 14.9 - Authentication Bypass', 'webapps', 'Ruby', '2022-04-26', 0, 0, [],
'Greenwolf', 'https://www.exploit-db.com/exploits/50888'], 
['50889', 'GitLab 14.9 - Stored Cross-Site Scripting (XSS)', 'webapps', 'Ruby',
'2022-04-26', 0, 0, [], 'Greenwolf', 'https://www.exploit-db.com/exploits/50889']]
```

### With _print=True

![Table Result](images/screenshot_table.png)

The full explanation of the functions can be found in the wiki or directly in the code.

## TODO (WIP)

- [x] searchEDB function
- [ ] searchCVE function
- [ ] Create a wiki
- [ ] Create a package
