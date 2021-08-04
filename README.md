# EnergyHub Coding Sample

[replay.py](./replay.py) is a script to parse information from a file of thermostat data.

## Installation

Install in this order:

```bash
#Install Python (3.8.2 or later)
https://www.python.org/downloads/ (Install based on user OS)

#Install pip (python package manager)

python get-pip.py (Mac)

or

py get-pip.py (Windows)

#Install essential json related library
pip install json-lines
```

## Run Script

While in Energy Coding Assignment root directory
```bash
python replay.py
```

## Sample Command

Returns ambientTemp: 82 based on updateTime passed in command
```bash
#normal json lines file
$ ./replay Enter command: ambientTemp thermostat-data.jsonl 2016-01-09T01:25:00.002797

or

#gzipped json lines file
$ ./replay Enter command: ambientTemp thermostat-data.jsonl.gz 2016-01-09T01:25:00.002797

82
```
### Sample Error Response for unavailable ambientTemp for incorrect updateTime

```bash
$ ./replay Enter command: ambientTemp thermostat-data.jsonl 2016-01-09T01:25:00.111111

Error: ambientTemp not available in this update
```