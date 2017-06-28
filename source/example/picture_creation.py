import tecplot_lib
from tecplot_data_files_creation import tecplot_dir, macros_dir
import os

# директория с изображениями
image_dir = 'images'
# имя файла с данными
sourcefile_name = os.path.join(tecplot_dir, 'example.plt')
# имя, под которым будет сохранени макрос
macro_name = os.path.join(macros_dir, 'picture_creation.mcr')
# имя директории, в которой содержаться .lay файлы с настройками изображения
parse_files_dir = 'tecplot_layout_files_for_parsing'

if __name__ == '__main__':
    # создание экземпляра класса LayoutParser, который позволит считать некоторые настройки изображения,
    # содержащиеся в файле с расширением .lay
    parser = tecplot_lib.LayoutParser(os.path.join(parse_files_dir, 'long_sec_1.lay'))
    # запуск парсинга
    parser.run_parsing()
    # координаты точки, через которую проходит срез
    pos = (0., 0., 0.)
    # нормаль к плоскости среза
    normal = (0, -1, 0)
    # создание экземпляра класса SliceSettings, в котором содержаться настройки среза
    slice_settings = tecplot_lib.SliceSettings(slice_type=tecplot_lib.SliceType.ARBITRARY, position=pos,
                                               normal=normal)
    # создание экземляра класса LevelSettings, в котором содержаться настройки уровней
    level_settings1 = tecplot_lib.LevelSettings(variable_number=19, min_level=0, max_level=90, num_levels=16)
    # задание настроик шрифтов заголовка и подписей для легенды
    legend_header_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=5)
    legend_number_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=5)
    # создание экземпляра класса LegendSettings, в которм содержаться настройки легенды
    legend_settings = tecplot_lib.LegendSettings(xy_position=(100, 90), isvertical=False,
                                                 header_font=legend_header_font, number_font=legend_number_font,
                                                 auto_levelskip=2)
    # задание настроик шрифтов для заголовков и подписей осей
    x_title_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=5)
    x_label_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=2)
    y_title_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=5)
    y_label_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=2)

    # создание экземпляра класса AxisSettings, в котором содержаться настройки для осей
    axis_settings = tecplot_lib.AxisSettings(x_axis_var=parser.x_axis_var, y_axis_var=parser.y_axis_var,
                                             rect=parser.rect,
                                             x_line_pos=0., y_line_pos=0.,
                                             preserve_axis_length=False,
                                             x_title_font=x_title_font, x_label_font=x_label_font,
                                             x_title_offset=5, x_label_offset=2, y_title_font=y_title_font,
                                             y_label_font=y_label_font, y_title_offset=5, y_label_offset=2,
                                             xlim=parser.xlim, ylim=parser.ylim, x_to_y_ratio=parser.x_to_y_ratio)
    # создание экземпляра класса FrameSettings, в котором задаются настройки фрейма
    frame_settings = tecplot_lib.FrameSettings(width=parser.frame_width, height=parser.frame_height, show_border=False)
    # создание экземпляра класса ColormapSettings, в котором содержаться настройки карты цветов
    colormap_settings1 = tecplot_lib.ColormapSettings(color_distribution=tecplot_lib.ColorDistribution.CONTINUOUS,
                                                      color_min=0, color_max=90)
    # создание экземпляра класса ExportSettings, в котором содержаться настройки экспорта в формат png
    export_settings1 = tecplot_lib.ExportSettings(8, os.path.join(image_dir, 'U_long.png'), imagewidth=2000)

    # создание экземпляра класса TicksSettings, в котором содержаться настройки меток на осях
    ticks_settings = tecplot_lib.TicksSettings(x_auto_grid=False, y_auto_grid=True, x_minor_thickness=0.3,
                                               y_minor_thickness=0.3, x_spacing=0.01, x_minor_num_ticks=8)

    # создание экземпляра класса PictureCreator, генерирующего макрос для создания картинок
    picture_creator1 = tecplot_lib.PictureCreator(sourcefile_name,
                                                  macro_name, slice_settings,
                                                  level_settings1, legend_settings, colormap_settings1, axis_settings,
                                                  export_settings1, frame_settings, ticks_settings)
    # создание макроса и его запись в него команд для создания изображения
    picture_creator1.add_to_existing_macro()

    # создание экземляра класса LevelSettings, в котором содержаться настройки уровней
    level_settings2 = tecplot_lib.LevelSettings(variable_number=21, min_level=-30, max_level=0, num_levels=16)
    # создание экземпляра класса ColormapSettings, в котором содержаться настройки карты цветов
    colormap_settings2 = tecplot_lib.ColormapSettings(color_distribution=tecplot_lib.ColorDistribution.CONTINUOUS,
                                                      color_min=-30, color_max=0)
    # создание экземпляра класса ExportSettings, в котором содержаться настройки экспорта в формат png
    export_settings2 = tecplot_lib.ExportSettings(8, os.path.join(image_dir, 'W_long.png'), imagewidth=2000)

    picture_creator2 = tecplot_lib.PictureCreator(sourcefile_name,
                                                  macro_name, slice_settings,
                                                  level_settings2, legend_settings, colormap_settings2, axis_settings,
                                                  export_settings2, frame_settings, ticks_settings)
    # добавление команд для создания второго изображения в уже существующий файл макроса
    picture_creator2.add_to_existing_macro()
    # запуск макроса
    picture_creator2.run_creation()

    # в результате запуска скрипта в папке images появится файлы U_long.png и W_long.png
