import tecplot_lib
from tecplot_data_files_creation import macros_dir, tecplot_dir
import os

# директория содержащая файлы с извлеченными данными
ext_data_dir = 'extracted_data'

if __name__ == '__main__':
    # создание точек, которые будут узлами полилиний
    point1 = tecplot_lib.Point(0.005, -0.0005, 0.000)
    point2 = tecplot_lib.Point(0.005, -0.0005, 0.0399)
    point3 = tecplot_lib.Point(0.095, -0.0005, 0.000)
    point4 = tecplot_lib.Point(0.095, -0.0005, 0.021)
    # полилиния, построенная по узлам, находящимся в точках point1 и point2, и содержащая 200 точек
    pl1 = tecplot_lib.PolyLine([point1, point2], 200)
    # полилиния, построенная по узлам, находящимся в точках point3 и point4, и содержащая 200 точек
    pl2 = tecplot_lib.PolyLine([point3, point4], 200)
    # список полилиний, по которым будут извелакться данные из файла example.plt
    # количество таких списков во входных параметрах к инициализатору класса tecplot_lib.LineDataExtractor должно
    # быть равно количеству файлов, содержащихся в директории с данными TecPlot
    pl_set = [pl1, pl2]
    # создание экземпляра класса tecplot_lib.LineDataExtractor
    data_extractor = tecplot_lib.LineDataExtractor(tecplot_dir, ext_data_dir, [pl_set],
                                                   os.path.join(macros_dir, 'data_extraction.mcr'))
    # создание и запуск макроса для извлечения данных
    data_extractor.run_extraction()
    #  результате выполнения скрипта в папке  extracted_data появятся два файла example_line_0.dat и example_line_0.dat
