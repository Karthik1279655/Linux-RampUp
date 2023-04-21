from datetime import datetime
string = input()


def string_search():
    file = open('device_log.txt', 'r')  # f = open('filename', 'mode')
    data = file.read()
    if string in data:
        print('string exist')
    else:
        print('string does not exist')
    file.close()



def read_line():
    file = open('device_log.txt', 'r')
    lines = file.readlines()
    for line in lines:
        if string in line:
            print(line)
    file.close()

def key_appeared():
    file = open('device_log.txt', 'r')
    data = file.read()
    occured = data.count(string)
    print("The number of times the string occured is :",occured)
    file.close()

def time_difference():
    string2 = input()
    file = open('device_log.txt', 'r')
    lines = file.readlines()
    for line in lines:
        if string in line:
            a = line[0:18]
            break
    for line in lines:
        if string2 in line:
            b = line[0:18]
            break
    diff1 = datetime.strptime(a, "%m-%d %H:%M:%S.%f")
    diff2 = datetime.strptime(b, "%m-%d %H:%M:%S.%f")
    d = diff2 - diff1
    print(d)

while True:
    print("Select the choice :")
    print("1.Searching the given string")
    print("2.Printing the given input")
    print("3.Printing the number of times the string appears")
    print("4.calculate the time between ON and OFF for a given keyword")
    print("5.exit")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        string_search()

    elif choice == 2:
        read_line()

    elif choice == 3:
        key_appeared()

    elif choice == 4:
        time_difference()

    elif choice == 5:
        break

    else:
        print("invalid choice")


