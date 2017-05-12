import tecplot_lib
from tecplot_data_files_creation import tecplot_dir, macros_dir
import os

# директория с изображениями
image_dir = 'images'

if __name__ == '__main__':
    # координаты точки, через которую проходит срез
    pos = (0., 0., 0.)
    # нормаль к плоскости среза
    normal = (0, -1, 0)
    # создание экземпляра класса SliceSettings, в котором содержаться настройки среза
    slice_settings = tecplot_lib.SliceSettings(slice_type=tecplot_lib.SliceType.ARBITRARY, position=pos,
                                               normal=normal)
    # создание экземляра класса LevelSettings, в котором содержаться настройки уровней
    level_settings = tecplot_lib.LevelSettings(variable_number=19, min_level=0, max_level=90, num_levels=16)
    # задание настроик шрифтов заголовка и подписей для легенды
    legend_header_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=5)
    legend_number_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=5)
    # создание экземпляра класса LegendSettings, в которм содержаться настройки легенды
    legend_settings = tecplot_lib.LegendSettings(xy_position=(100, 90), isvertical=False,
                                                 header_font=legend_header_font, number_font=legend_number_font,
                                                 auto_levelskip=2)
    # задание настроик шрифтов для заголовков и подписей осей
    x_title_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=5)
    x_label_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=5)
    y_title_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=5)
    y_label_font = tecplot_lib.Font(font_family='Helvetica', is_bold=True, is_italic=False, height=5)

    # создание экземпляра класса AxisSettings, в котором содержаться настройки для осей
    axis_settings = tecplot_lib.AxisSettings(x_axis_var=1, y_axis_var=3, rect=(10, 10, 95, 80),
                                             x_line_pos=0., y_line_pos=0.,
                                             preserve_axis_length=False,
                                             x_title_font=x_title_font, x_label_font=x_label_font,
                                             x_title_offset=5, y_title_font=y_title_font,
                                             y_label_font=y_label_font, y_title_offset=5, xlim=(0, 0.1),
                                             ylim=(0, 0.045))
    # создание экземпляра класса FrameSettings, в котором задаются настройки фрейма
    frame_settings = tecplot_lib.FrameSettings(width=12, height=7)
    # создание экземпляра класса ColormapSettings, в котором содержаться настройки карты цветов
    colormap_settings = tecplot_lib.ColormapSettings(color_distribution=tecplot_lib.ColorDistribution.CONTINUOUS,
                                                     color_min=0, color_max=90)
    # создание экземпляра класса ExportSettings, в котором содержаться настройки экспорта в формат png
    export_settings = tecplot_lib.ExportSettings(8, os.path.join(image_dir, 'U_long.png'), imagewidth=2000)

    # создание экземпляра класса PictureCreator, енерирующего макрос для создания картинок
    picture_creator = tecplot_lib.PictureCreator(os.path.join(tecplot_dir, 'example.plt'),
                                                 os.path.join(macros_dir, 'picture_creation.mcr'), slice_settings,
                                                 level_settings, legend_settings, colormap_settings, axis_settings,
                                                 export_settings, frame_settings)
    # создание макроса и его запуск
    picture_creator.run_creation()

    # в результате запуска скрипта в папке images появится файл U_long.png
