#!MC 1410
$!VarSet |MFBD| = 'C:\Program Files\Tecplot\Tecplot 360 EX 2016 R2'
$!READDATASET  '"StandardSyntax" "1.0" "FEALoaderVersion" "435" "FILENAME_File" "cfx_res_files\CFX_001.res" "AutoAssignStrandIDs" "Yes"' DATASETREADER = 'ANSYS CFX (FEA)'
$!WRITEDATASET  'tecplot_data_files\example.plt' 
  INCLUDETEXT = NO
  INCLUDEGEOM = NO
  INCLUDEDATASHARELINKAGE = YES
  BINARY = YES
  USEPOINTFORMAT = NO
  PRECISION = 9
  TECPLOTVERSIONTOWRITE = TECPLOTCURRENT
$!RemoveVar |MFBD|
$!Quit