import re

def parse_command(command: str):
    parts = re.findall(r'\".*?\"|\S+', command)
    return [part[1:-1] if part.startswith('"') and part.endswith('"') else part for part in parts]