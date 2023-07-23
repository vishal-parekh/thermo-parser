# EnergyHub Coding Sample

[replay.py](./replay.py) is a script to parse information from a json lines file consisting of thermostat data.

## Install Dependencies
### Install Python (3.11.4 or later)
- [Official Python Download Link](https://www.python.org/downloads/)

### Install Poetry
- [How to install Poetry](https://python-poetry.org/docs/#installation)

```bash
#Install Dependencies from pyproject.toml
poetry install
```

## Commands to run for normal or gzipped json lines file type:

### In root of thermo-parser directory:
```bash
#Return ambientTemp from json lines files using updateTime
$ python replay.py thermostat-data.jsonl 2016-01-09T01:25:00.002797

and 

#Return ambientTemp from gzipped json lines files using updateTime
$ python replay.py thermostat-data.jsonl.gz 2016-01-09T01:25:00.002797

Expected output: 74
```
### Error Response for non-existent ambientTemp:

```bash
$ python replay.py thermostat-data.jsonl 2016-01-09T01:25:00.111111

An error occured: updateTime does not exist
Traceback (most recent call last):
  File "//src/thermo-parser/replay.py", line 46, in <module>
    print(find_ambient_temp(sys.argv[1:]))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/src/thermo-parser/replay.py", line 42, in find_ambient_temp
    raise e
  File "/src/thermo-parser/replay.py", line 39, in find_ambient_temp
    raise Exception("updateTime does not exist")
Exception: updateTime does not exist
```