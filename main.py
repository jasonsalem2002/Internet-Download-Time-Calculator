print("|----------------------------------|"
      "|-----Download Time Calculator-----|"
      "|----------------------------------|")

sizeUnit = input("Enter the size unit of the file:\n"
                 "(a) Kilobytes\n"
                 "(b) Megabytes\n"
                 "(c) Gigabytes\n")
size = float(input("Enter the size: "))

if sizeUnit == "b":
    size = size * 1024

if sizeUnit == "c":
    size = size * 1049576

internetSpeedUnit = input("Enter your internet speed unit: \n"
                          "(a) Kbps\n"
                          "(b) Mbps\n")

internetSpeed = float(input("Enter your internet speed: "))

if internetSpeedUnit == "a":
    internetSpeed = internetSpeed / 8

if internetSpeedUnit == "b":
    internetSpeed = internetSpeed * 1000
    internetSpeed = internetSpeed / 8


time = size / internetSpeed

day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minute = time // 60
time %= 60
second = time
print("The download will take: ", day, " days ", hour, " hours ", minute, " minutes ", second, " seconds")
