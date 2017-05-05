import tecplot_lib
from data_extraction import ext_data_dir
import matplotlib.pyplot as plt
import os

# директория, содержащая файлы с графиками
plots_dir = 'plots'

if __name__ == '__main__':
    # создание экземпляра класса LineDataLoader
    data_loader = tecplot_lib.LineDataLoader(ext_data_dir)
    # вызов метода load класса LineDataLoader, который в поле frames создат список объектов
    # класса pandas.DataFrame, в которых будут содержаться данные из считанных файлов
    data_loader.load()
    # экземпляр класса pandas.DataFrame, содержащий данные из первой полилинии
    pl1_fr = data_loader.frames[0]
    # экземпляр класса pandas.DataFrame, содержащий данные из второй полилинии
    pl2_fr = data_loader.frames[1]

    # создание графика распределения скорости на входе и на выходе в канал
    plt.figure(figsize=(8, 6))
    plt.plot(pl1_fr['U'], pl1_fr['Z'], color='red', lw=1.5, label='inlet')
    plt.plot(pl2_fr['U'], pl2_fr['Z'], color='blue', lw=1.5, label='outlet')
    plt.grid()
    plt.xlabel('Velocity, m/s', fontsize=16)
    plt.ylabel('Z, m', fontsize=16)
    plt.legend(fontsize=16)
    plt.ylim(0, 0.040)
    plt.xlim(30, 90)
    plt.title('Velocity profile', fontsize=16)
    plt.savefig(os.path.join(plots_dir, 'velocity_profile.png'))
    # в результате выполнения скрипта в папке plots появится файл velocity_profile.png

