#!MC 1410
$!VarSet |MFBD| = 'C:\Program Files\Tecplot\Tecplot 360 EX 2016 R2'
$!READDATASET  'tecplot_data_files\example.plt'
$!ALTERDATA
  EQUATION = '{P_stag, Pa} = {Total Pressure}'
  IGNOREDIVIDEBYZERO = NO
  DATATYPE = SINGLE
$!SAVELAYOUT  'tecplot_data_files\example.lay'
  INCLUDEDATA = YES
  INCLUDEPREVIEW = NO
$!RemoveVar |MFBD|
$!Quit