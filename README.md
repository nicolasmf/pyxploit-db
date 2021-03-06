# Pyxploit-db

![downloads](https://img.shields.io/pypi/dm/pyxploitdb)
![license](https://img.shields.io/pypi/l/pyxploitdb)

![image](https://cdn.discordapp.com/attachments/972604017261830176/972604672676352000/pyxploitdb.png)

An exploit-db.com python API using advanced search with all possible filters.

For another project, I needed to make some queries to the exploit database, but I couldn't find any complete API that would allow me to get what I wanted, how I wanted. So I decided to create my own API, and making it as complete as possible, with the maximum of parameters so everyone will find what they need and how they need it.

## How to use

`$ python3 -m pip install pyxploitdb`

### Examples

```python
>>> import pyxploitdb
>>> pyxploitdb.search_edb("Gitlab 14.9", platform="ruby", print_=False, nb_results=1)
[Exploit(id_='50888', description='Gitlab 14.9 - Authentication Bypass', 
type_='webapps', platform='Ruby', date_published='2022-04-26', verified=0, 
port=0, tag_if_any=[], author='Greenwolf', link='https://www.exploit-db.com/exploits/50888')]
>>> pyxploitdb.search_edb("CVE-2006-1234")
[Exploit(id_='27423', description='DSCounter 1.2 - \'index.php\' SQL Injection', 
type_='webapps', platform='PHP', date_published='2006-03-14', verified=1, port=0, 
tag_if_any=[], author='Aliaksandr Hartsuyeu', link='https://www.exploit-db.com/exploits/27423')]
```

### With _print=True

![Table Result](https://media.discordapp.net/attachments/842511727324561429/972520026701705237/screenshot_table.png?width=1260&height=135)

***

A full explanation of the functions can be found in the [wiki](https://github.com/nicolasmf/pyxploit-db/wiki) or directly in the code.

***

## TODO

- [x] searchEDB function
- [x] searchCVE function
- [x] Create a package
- [x] Create a wiki
