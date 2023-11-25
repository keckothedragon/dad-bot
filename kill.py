import constants
def kill():
    with open(constants.killPath, "w+") as f:
        f.write("1")

def unkill():
    with open(constants.killPath, "w+") as f:
        f.write("0")

def isDed():
    try:
        with open(constants.killPath, "r+") as f:
            data = f.read()
            return bool(int(data))
    except (ValueError, FileNotFoundError):
        return False