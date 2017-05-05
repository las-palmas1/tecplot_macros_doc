import tecplot_lib
from tecplot_data_files_creation import tecplot_dir, macros_dir
import os

layouts_dir = 'tecplot_layouts_dir'

if __name__ == '__main__':
    # строка, содержащая команду, открывающую айл данных TecPlot
    open_file = tecplot_lib.get_open_data_file_command(os.path.join(tecplot_dir, 'example.plt'))
    # строка, содержащая команду, создающую новую переменную
    alter_data = tecplot_lib.get_alterdata_command(equation='{P_stag, Pa} = {Total Pressure}')
    # строка, содержащая команду, сохранающую текущий файл данных TecPlot в формате .lay
    save_layout = tecplot_lib.get_save_layout_command(os.path.join(layouts_dir, 'example.lay'))
    # строка, содержащая весь макрос
    macro = tecplot_lib.wrap_macro(open_file + alter_data + save_layout)
    # создание файла .mcr
    tecplot_lib.create_macro_file(macro, os.path.join(macros_dir, 'alter_data_creation.mcr'))
    # апуск макроса
    tecplot_lib.execute_macro(os.path.join(macros_dir, 'alter_data_creation.mcr'))
    # результате выполнения скрипта в папке tecplot_layouts_dir появится файл example.lay
