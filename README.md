# Pyxploit-db

A python package to search the exploit database from exploit-db.com

## Future use

```python
>>> import pyxploitdb
>>> result = pyxploitdb.searchEDB("Gitlab 14.9", platform="ruby", _print=False)
>>> print(result)
[['50888', 'Gitlab 14.9 - Authentication Bypass', 'webapps', 'Ruby', '2022-04-26', 0, 0, [], 'Greenwolf', 'https://www.exploit-db.com/exploits/50888'], ['50889', 'GitLab 14.9 - Stored Cross-Site Scripting (XSS)', 'webapps', 'Ruby', '2022-04-26', 0, 0, [], 'Greenwolf', 'https://www.exploit-db.com/exploits/50889']]
```

![Table Result](images/screenshot_table.png)

## TODO

- [x] searchEDB function
- [ ] searchCVE function
- [ ] Create a package