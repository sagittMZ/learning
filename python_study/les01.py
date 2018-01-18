# test1
import os
import sys
import shutil
import psutil # сторонний
# test1
print("Python :)") 
print("Привет, чудила") 
name = input("Type your name:")Ы
answer = ''
while answer !='q':
    answer = input("Work? Y/N/q: ")
    if answer == "Y":
       #print("$")
       #pass
        print("u r really strange persone")
        print("1 - список файлов")
        print("2 - информация о системе")
        print("3 - список процессов")
        print("4 - дублирование файлов в текущей директории")
        do = int(input("choose # of action: "))
        if do == 1:
            print(os.listdir())
        elif do == 2:
            print("about sys: ")
            print("количество процессоров: ", psutil.cpu_count())
            print("платформа: ", sys.platform)
            print("кодировка файлов файловой системы: ", sys.getfilesystemencoding())
            print("текущая директорая: ", os.getcwd())
            print("текущий пользователь: ", os.getlogin())
            file_list = os.listdir()
            i=0
            while i<len(file_list):
                newfile = file_list[i]+ '.copy'
                shutil.copy(file_list[i], newfile)
                i+=1
        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("--Дублирование файлов директории--")
        else:
            pass
    elif answer == "N":
        print("stay away")
    else:
        print("whaaat?!")