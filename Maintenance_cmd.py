import Maintenance_main
from Maintenance_main import Sens
from pygame import mixer
from datetime import datetime
import time
import os

try:
    print('Салам, ИНЖЕНЕГРЫ!!!\nБудьте внимательны при настройке!\n\nДля выхода нажмите CTRL+C\n')
    try:
        iram = (input('Input path to IRAM\n') + '\\TEK\\DAT_SENS\\')
        dur = float(input('Введите время срабатывания по отсутствию данных (мин)\n'))
        #os.system('cls')
        #os.system('mode con: cols=45 lines=3')
        snd = 'D:\\IRAM\\KRAMS_DAT\\WAV\\srok1M.wav'
    except ValueError:
        print('Ошибка ввода\n')
    cl_list = ["CL311", "CL312", "CT25K1", "CT25K2"]
    lt_list = ["LT311", "LT312", "LT313", "LT314", "LT315", "LT316"]
    while True:
        for c in range(0, 4):
            lc = cl_list[c]
            try:
                try:
                    Sens(iram, lc, "", snd, dur).cl()
                    print(Maintenance_main.status_cl)
                    #os.system("cls")
                except FileNotFoundError:
                    print(lc + ' Не найден файл с данными!!!\n' )
                    log = open(iram + "maintenance.log", "a+")
                    log.write(str(datetime.now()) + " " + lc + ' Не найден файл с данными!!!\n' )
                    log.close()
                    mixer.music.load(snd)
                    mixer.music.play(0)
                    time.sleep(3)
                    #os.system("cls")
            except PermissionError:
                print('Ошибка чтения файла ' + lc )
                log = open(iram + "maintenance.log", "a+")
                log.write(str(datetime.now()) + " " + lc + ' Ошибка чтения файла\n' )
                log.close()
                pass
        for t in range(0, 6):
            ll = lt_list[t]
            try:
                try:
                    Sens(iram, "", ll, snd, dur).lt()
                    print(Maintenance_main.status_lt)
                    #os.system("cls")
                except FileNotFoundError:
                    print(ll + ' Не найден файл с данными!!!\n' )
                    log = open(iram + "maintenance.log", "a+")
                    log.write(str(datetime.now()) + " " + ll + ' Не найден файл с данными!!!\n' )
                    log.close()
                    mixer.music.load(snd)
                    mixer.music.play(0)
                    time.sleep(3)
                    #os.system("cls")
            except PermissionError:
                print('Ошибка чтения файла ' + ll)
                log = open(iram + "maintenance.log", "a+")
                log.write(str(datetime.now()) + " " + ll + ' Ошибка чтения файла!!!\n' )
                log.close()
                pass
except KeyboardInterrupt:
        print('\n\nДавай, до свидания....')
        time.sleep(2)
