# mode 'w' will always overwrite the previous file
with open('newfile.txt', mode='w') as file:
    file.writelines(["\nThis is a new file. Create by a python script.", "\nThis is another line"])

try:
    with open('newfile.txt', mode='a') as file:
        file.writelines(["\nNew Line", "\nThis is another new line"])
except FileNotFoundError as e:
    print("ERROR:", e)