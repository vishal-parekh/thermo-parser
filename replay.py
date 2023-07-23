# Small library to open normal and gzipped json lines files
import sys

import json_lines


def find_ambient_temp(input):
    # Store file path in var to open file
    filepath = input[0]

    # Parsing logic to handle jsonlines file
    try:
        with json_lines.open(filepath) as path:
            for obj in path:
                if obj["updateTime"] == input[1] and "ambientTemp" in obj.get("update"):
                    return obj["update"]["ambientTemp"]
            else:
                raise Exception(
                    "ambientTemp does not exist. updateTime is incorrect or invalid."
                )
    except Exception as e:
        print(f"An error occured: {e}")
        raise e


if __name__ == "__main__":
    print(find_ambient_temp(sys.argv[1:]))
