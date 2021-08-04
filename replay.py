#Small library to open normal or gzipped json lines file(s)
import json_lines

command = input("Enter Command: ")

#Split up whole command to list elements to store rawpath (as that will be needed to determine how to handle file type in evaluation)
commandsplit = command.split()
rawpath = commandsplit[1]

#If statement to evaluate updateTime passed in command to get ambientTemp for that json object,
#else return error stating ambientTemp not available in json object for that particular updateTime

#Logic to handles gzipped jsonlines file
if rawpath.endswith('jsonl.gz'):
     with json_lines.open(rawpath) as path:
          for obj in path:
               if "ambientTemp" in obj["update"] and commandsplit[2] in obj["updateTime"]:
                    ambientTemp = str(obj["update"]["ambientTemp"])
                    print(ambientTemp)
                    break
          else:
               print("Error:ambientTemp not available in this update")

#Logic to handle normal jsonlines file.
elif rawpath.endswith('jsonl'):
     with json_lines.open(rawpath) as path:
          for obj in path:
               if "ambientTemp" in obj["update"] and commandsplit[2] in obj["updateTime"]:
                    ambientTemp = obj["update"]["ambientTemp"]
                    print(ambientTemp)
                    break
          else:
               print("Error: ambientTemp not available in this update")
