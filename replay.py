# Small library to open normal or gzipped json lines file(s)
import sys

import json_lines


def find_ambient_temp(input):
    # Split up whole command to list elements to store rawpath (as that will be needed to determine how to handle file type in evaluation)
    filepath = input[0]

    # If statement to evaluate updateTime passed in command to get ambientTemp for that json object,
    # else return error stating ambientTemp not available in json object for that particular updateTime

    # Handle gzipped jsonlines file
    if filepath.endswith("jsonl.gz"):
        try:
            with json_lines.open(filepath) as path:
                for obj in path:
                    if obj["updateTime"] == input[1] and "ambientTemp" in obj.get(
                        "update"
                    ):
                        return obj["update"]["ambientTemp"]
                else:
                    raise Exception("updateTime does not exist")
        except Exception as e:
            print(f"An error occured: {e}")
            raise e

    # Handle normal jsonlines file.
    if filepath.endswith("jsonl"):
        try:
            with json_lines.open(filepath) as path:
                for obj in path:
                    if obj["updateTime"] == input[1] and "ambientTemp" in obj.get(
                        "update"
                    ):
                        return obj["update"]["ambientTemp"]
                else:
                    raise Exception("updateTime does not exist")
        except Exception as e:
            print(f"An error occured: {e}")
            raise e


if __name__ == "__main__":
    print(find_ambient_temp(sys.argv[1:]))
