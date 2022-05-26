from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyxploitdb",
    version="2.0",
    description="An exploit-db.com python API using advanced search with all possible filters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicolasmf/pyxploit-db",
    author="Nicolas MF",
    author_email="nikolamf@hotmail.com",
    license="MIT",
    keywords="api exploitdb exploit exploit-db",
    packages=find_packages(),
    install_requires=["rich"],
    project_urls={"Documentation": "https://github.com/nicolasmf/pyxploit-db/wiki"},
)
