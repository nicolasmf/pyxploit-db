import requests, re
from rich.console import Console
from rich.table import Table

HEADERS = {
    "User-Agent": "pyxploitdb",
    "X-Requested-With": "XMLHttpRequest",
}


def searchEDB(
    title: str = "",
    nb_results: int = 10,
    _type: str = "",
    platform: str = "",
    port: int | str = "",
    content: str = "",
    author: str = "",
    tag: int | str = "",
    tag_verify: bool = True,
    verified: bool = "",
    hasapp: bool = "",
    nomsf: bool = "",
    _print: bool = False,
) -> list:
    """
    Searches exploit-db.com using advanced search, with all possible filters.

    Args:
        title (str, optional): The title or description of the exploit. Defaults to "".
        nb_results (int, optional): The maximum number of results to print/return. Defaults to 10.
        _type (str, optional): The exploit type. Possible types are [dos, local, remote, shellcode, papers, webapps]. Defaults to "".
        platform (str, optional): The platform in which the exploit is written. Defaults to "".
        port (int | str, optional): The exploit target port. Defaults to "".
        content (str, optional): The exploit content. Warning, may increase response time. Defaults to "".
        author (str, optional): The exploit's author. Defaults to "".
        tag (int | str, optional): The exploit's tag. Possible tags are\n
        [WordPress Core, Metasploit Framework (MSF), WordPress Plugin, SQL Injection (SQLi), Cross-Site Scripting (XSS), File Inclusion (LFI/RFI), Cross-Site Request Forgery (CSRF), Denial of Service (DoS), Code Injection, Command Injection, Authentication Bypass / Credentials Bypass (AB/CB), Client Side, Use After Free (UAF), Out Of Bounds, Remote, Local, XML External Entity (XXE), Integer Overflow, Server-Side Request Forgery (SSRF), Race Condition, NULL Pointer Dereference, Malware, Buffer Overflow, Heap Overflow, Type Confusion, Object Injection, Bug Report, Console, Pwn2Own, Traversal, Deserialization].\n
        Defaults to "".
        tag_verify (bool, optional): Make user choose between different tags if the tag string in argument is contained in multiple possible tags or checks if no tags were found with the user input. Defaults to True.
        verified (bool, optional): Search only verified / unverified exploits. Defaults to "".
        hasapp (bool, optional): Search only exploits that have / don't have  a vulnerable application attached. Defaults to "".
        nomsf (bool, optional): Search only exploits that use / don't use Metasploit Framework. Defaults to "".
        _print (bool, optional): Switch to print  a table with results. Defaults to False.

    Returns:
        list: Prints the list of exploits found if _print is True and returns a list of
        exploits' information using this template :
        [id, description, type, platform, date_published, verified, port, tag_if_any, author, link]
    """

    tags = {
        "1": "WordPress Core",
        "3": "Metasploit Framework (MSF)",
        "4": "WordPress Plugin",
        "7": "SQL Injection (SQLi)",
        "8": "Cross-Site Scripting (XSS)",
        "9": "File Inclusion (LFI/RFI)",
        "12": "Cross-Site Request Forgery (CSRF)",
        "13": "Denial of Service (DoS)",
        "14": "Code Injection",
        "15": "Command Injection",
        "16": "Authentication Bypass / Credentials Bypass (AB/CB)",
        "18": "Client Side",
        "19": "Use After Free (UAF)",
        "20": "Out Of Bounds",
        "21": "Remote",
        "22": "Local",
        "23": "XML External Entity (XXE)",
        "24": "Integer Overflow",
        "25": "Server-Side Request Forgery (SSRF)",
        "26": "Race Condition",
        "27": "NULL Pointer Dereference",
        "28": "Malware",
        "31": "Buffer Overflow",
        "34": "Heap Overflow",
        "35": "Type Confusion",
        "36": "Object Injection",
        "37": "Bug Report",
        "38": "Console",
        "39": "Pwn2Own",
        "40": "Traversal",
        "41": "Deserialization",
    }

    if tag != "":
        possible_tags = []

        for i in tags.values():
            if tag.lower() in i.lower():
                possible_tags.append(i)

        if tag_verify:
            if len(possible_tags) > 1:
                print(
                    "Multiple tag possibilities detected. Please choose one from this list :"
                )
                for idx, val in enumerate(possible_tags):
                    print(f"{idx+1}. {val}")
                while True:
                    try:
                        ans = possible_tags[int(input("Answer : ")) - 1]
                    except ValueError:
                        print("Please enter a number.")
                        continue
                    except IndexError:
                        print(
                            f"Please enter a number between 1 and {len(possible_tags)}"
                        )
                        continue
                    break
                tag = [k for k, v in tags.items() if v == ans][0]
            elif len(possible_tags) == 0:
                print(f'No tag found with string "{tag}".')
            else:
                tag = [k for k, v in tags.items() if v == possible_tags[0]][0]
        else:
            tag = [k for k, v in tags.items() if v == possible_tags[0]][0]

    verified, hasapp, nomsf = (
        str(verified).lower(),
        str(hasapp).lower(),
        str(nomsf).lower(),
    )

    url = f"https://www.exploit-db.com/search?q={title}&type={_type}&platform={platform}&port={port}&text={content}&e_author={author}&tag={tag}&verified={verified}&hasapp={hasapp}&nomsf={nomsf}"

    response = requests.get(url, headers=HEADERS)
    data = response.json()["data"]
    res_length = len(data) if (len(data) < nb_results) else nb_results

    if _print:

        table = Table(show_header=True, header_style="bold blue")
        table.add_column("Description")
        table.add_column("Date")
        table.add_column("Link")
        table.add_column("Language", justify="center")
        table.add_column("Verified", justify="center")

        if res_length:
            for i in range(res_length):
                table.add_row(
                    f'[{data[i]["author"]["name"]}] {data[i]["description"][1]}',
                    data[i]["date_published"],
                    f"https://www.exploit-db.com/exploits/{data[i]['id']}",
                    data[i]["platform_id"],
                    "✅" if data[i]["verified"] == 1 else "❌",
                )
            Console().print(table)
        else:
            print("No exploits found.")

    results = []
    for i in range(res_length):
        results.append(
            [
                data[i]["id"],
                data[i]["description"][1],
                data[i]["type_id"],
                data[i]["platform_id"],
                data[i]["date_published"],
                data[i]["verified"],
                data[i]["port"],
                data[i]["tags"],
                data[i]["author"]["name"],
                f"https://www.exploit-db.com/exploits/{response.json()['data'][i]['id']}",
            ]
        )
    return results


def searchCVE(cve: str) -> list:
    """
    Searches exploit-db.com CVE.

    Args:
        cve (str): The CVE to search. The argument can be given in 2 different forms : CVE-1234-1234 or 1234-1234.

    Returns:
        list: A list with the CVE's information using this template :
        [id, description, type, platform, date_published, verified, tag_if_any, author, link]
    """

    # CVE string verification
    CVE_regex = re.compile(r"\d{4}-\d{4,7}")
    if CVE_regex.search(cve) is None:
        print("Please input a valid CVE (YYYY-1234567).")
        return
    else:
        cve = CVE_regex.search(cve).group()

    url = f"https://www.exploit-db.com/search?cve={cve}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()["data"]
    res_length = len(data)

    results = []
    for i in range(res_length):
        results.append(
            [
                data[i]["id"],
                data[i]["description"][1],
                data[i]["type_id"],
                data[i]["platform_id"],
                data[i]["date_published"],
                data[i]["verified"],
                data[i]["port"],
                data[i]["tags"],
                data[i]["author"]["name"],
                f"https://www.exploit-db.com/exploits/{response.json()['data'][i]['id']}",
            ]
        )
    return results
