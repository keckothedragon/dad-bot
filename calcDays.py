import constants
from datetime import date, timedelta

def calcDaysSinceTimeStamp():
    try:
        with open(constants.doomsdayPath, "r+") as f:
            data = f.read()
            timestampDay = date(year=int(data[:4]), month=int(data[5:7]), day=int(data[8:]))
    except (IndexError, FileNotFoundError, ValueError) as e:
        print(e)
        return 0
    return (date.today() - timestampDay).days

def writeTimeStampNow():
    with open(constants.doomsdayPath, "w+") as f:
        f.write(str(date.today() - timedelta()))

def main():
    writeTimeStampNow()

if __name__ == '__main__':
    main()