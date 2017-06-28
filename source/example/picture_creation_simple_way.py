import tecplot_lib
from tecplot_data_files_creation import tecplot_dir, macros_dir
import os

# директория с изображениями
image_dir = 'images'
# имя файла с данными
sourcefile_name = os.path.join(tecplot_dir, 'example.plt')
# имя, под которым будет сохранени макрос
macro_name = os.path.join(macros_dir, 'picture_creation_simple_way.mcr')

if __name__ == '__main__':
    # координаты точки, через которую проходит срез
    pos = (0., 0., 0.)
    # нормаль к плоскости среза
    normal = (0, -1, 0)
    # создание экземпляра класса SliceSettings, в котором содержаться настройки среза
    slice_settings = tecplot_lib.SliceSettings(slice_type=tecplot_lib.SliceType.ARBITRARY, position=pos,
                                               normal=normal)
    # создание экземляра класса LevelSettings, в котором содержаться настройки уровней
    level_settings1 = tecplot_lib.LevelSettings(variable_number=19, min_level=0, max_level=90, num_levels=16)
    # создание экземпляра класса LegendSettings, в которм содержаться настройки легенды
    legend_settings = tecplot_lib.LegendSettings(xy_position=(100, 90))

    # создание экземпляра класса AxisSettings, в котором содержаться настройки для осей
    axis_settings = tecplot_lib.AxisSettings(x_axis_var=1, y_axis_var=3)

    # создание экземпляра класса ColormapSettings, в котором содержаться настройки карты цветов
    colormap_settings1 = tecplot_lib.ColormapSettings(color_distribution=tecplot_lib.ColorDistribution.CONTINUOUS,
                                                      color_min=0, color_max=90)
    # создание экземпляра класса ExportSettings, в котором содержаться настройки экспорта в формат png
    export_settings1 = tecplot_lib.ExportSettings(8, os.path.join(image_dir, 'U_long_simple_way.png'), imagewidth=2000)

    # создание экземпляра класса PictureCreator, генерирующего макрос для создания картинок
    picture_creator1 = tecplot_lib.PictureCreator(sourcefile_name, macro_name, slice_settings, level_settings1,
                                                  legend_settings, colormap_settings1, axis_settings, export_settings1)
    # создание макроса и его запись в него команд для создания изображения
    picture_creator1.add_to_existing_macro()

    # изменение настроек уровней легенды и цветов
    picture_creator1.level_settings.variable_number = 21
    picture_creator1.level_settings.min_level = -30
    picture_creator1.level_settings.max_level = 0
    picture_creator1.level_settings.num_levels = 16
    picture_creator1.colormap_settings.kwargs['color_min'] = -30
    picture_creator1.colormap_settings.kwargs['color_max'] = 0
    # имя, под которым будет сохранено изображение
    picture_creator1.export_settings.exportfname = os.path.join(image_dir, 'W_long_simple_way.png')

    picture_creator1.add_to_existing_macro()
    picture_creator1.run_creation()

    # в результате запуска скрипта в папке images появится файлы U_long_simple_way.png и W_long_simple_way.png
