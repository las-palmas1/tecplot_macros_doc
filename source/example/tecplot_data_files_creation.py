import tecplot_lib
import os

# имя директории с файлами .res
cfx_dir = 'cfx_res_files'
# имя директории с файлами данных TecPlot
tecplot_dir = 'tecplot_data_files'
# имя директории с файлами максросов
macros_dir = 'macros'

if __name__ == '__main__':
    # строка, содержащая команду на языке TecPlot, открывающую файл .res
    open_cfx = tecplot_lib.get_open_data_file_command(os.path.join(cfx_dir, 'CFX_001.res'), tecplot_lib.LoaderType.CFX)
    # строка, содержащая команду, сохраняющую текущий файл
    save_as_plt = tecplot_lib.get_write_data_set_command(os.path.join(tecplot_dir, 'example.plt'))
    # строка, содержащий макрос из двух вышеполученных команд
    macros = tecplot_lib.wrap_macro(open_cfx + save_as_plt)
    # создание файла с макросом
    tecplot_lib.create_macro_file(macros, os.path.join(macros_dir, 'tecplot_data_files_creation.mcr'))
    # запуск макроса
    tecplot_lib.execute_macro(os.path.join(macros_dir, 'tecplot_data_files_creation.mcr'))
    # результате выполнения скрипта в папке tecplot_data_files появится файл example.plt
