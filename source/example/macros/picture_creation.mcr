#!MC 1410
$!VarSet |MFBD| = 'C:\Program Files\Tecplot\Tecplot 360 EX 2016 R2'
$!READDATASET  'tecplot_data_files\example.plt'
$!SLICELAYERS SHOW = YES
$!SLICEATTRIBUTES 1  SLICESURFACE = ARBITRARY
$!SLICEATTRIBUTES 1  PRIMARYPOSITION{X = 0.0 Y = 0.0 Z = 0.0}
$!SLICEATTRIBUTES 1 NORMAl {X = 0 Y = -1 Z = 0}
$!SETCONTOURVAR
  VAR = 19
  CONTOURGROUP = 1
$!CONTOURLEVELS NEW
  CONTOURGROUP = 1
  RAWDATA
16
0.0
6.0
12.0
18.0
24.0
30.0
36.0
42.0
48.0
54.0
60.0
66.0
72.0
78.0
84.0
90.0
$!GLOBALCONTOUR 1  LEGEND{ISVERTICAL = NO}
$!GLOBALCONTOUR 1  LABELS{AUTOLEVELSKIP = 2}
$!GLOBALCONTOUR 1  LEGEND{ROWSPACING = 1.2}
$!GLOBALCONTOUR 1
LEGEND
{
SHOW = YES
XYPOS
{
X = 100
Y = 90
}
}
$!GLOBALCONTOUR 1  LEGEND{HEADERTEXTSHAPE{FONTFAMILY = 'Helvetica'}}
$!GLOBALCONTOUR 1  LEGEND{HEADERTEXTSHAPE{HEIGHT = 5}}
$!GLOBALCONTOUR 1  LEGEND{HEADERTEXTSHAPE{ISITALIC = NO}}
$!GLOBALCONTOUR 1  LEGEND{HEADERTEXTSHAPE{ISBOLD = YES}}
$!GLOBALCONTOUR 1  LEGEND{NUMBERTEXTSHAPE{FONTFAMILY = 'Helvetica'}}
$!GLOBALCONTOUR 1  LEGEND{NUMBERTEXTSHAPE{HEIGHT = 5}}
$!GLOBALCONTOUR 1  LEGEND{NUMBERTEXTSHAPE{ISITALIC = NO}}
$!GLOBALCONTOUR 1  LEGEND{NUMBERTEXTSHAPE{ISBOLD = YES}}
$!GLOBALCONTOUR 1  COLORMAPNAME = 'Modern'
$!GLOBALCONTOUR 1  COLORMAPFILTER{COLORMAPDISTRIBUTION = CONTINUOUS}
$!GLOBALCONTOUR 1  COLORMAPFILTER{CONTINUOUSCOLOR{CMIN = 0}}
$!GLOBALCONTOUR 1  COLORMAPFILTER{CONTINUOUSCOLOR{CMAX = 90}}
$!CREATESLICEZONES
$!FIELDLAYERS SHOWCONTOUR = YES
$!PLOTTYPE = CARTESIAN2D
$!TWODAXIS XDETAIL{VARNUM = 1}
$!TWODAXIS YDETAIL{VARNUM = 3}
$!TWODAXIS
  PRESERVEAXISSCALE = TRUE
  XDETAIL
    {
    RANGEMIN = -0.0030406946326921526
    RANGEMAX = 0.10091868649126987
    }
  YDETAIL
    {
    RANGEMIN = -0.0035628683697661663
    RANGEMAX = 0.05013466738300066
    }
$!TWODAXIS
  DEPXTOYRATIO = 1.0
  GRIDAREA
  {
    EXTENTS
    {
      X1 = 12.287
      Y1 = 16.983
      X2 = 90.614
      Y2 = 75.18
    }
  }
$!TWODAXIS XDETAIL{AXISLINE{AXISALIGNMENT = WITHVIEWPORT}}
$!TWODAXIS XDETAIL{AXISLINE{POSITION = 0.0}}
$!TWODAXIS YDETAIL{AXISLINE{AXISALIGNMENT = WITHVIEWPORT}}
$!TWODAXIS YDETAIL{AXISLINE{POSITION = 0.0}}
$!TWODAXIS XDETAIL{TITLE{TEXTSHAPE{FONTFAMILY = 'Helvetica'}}}
$!TWODAXIS XDETAIL{TITLE{TEXTSHAPE{HEIGHT =5}}}
$!TWODAXIS XDETAIL{TITLE{TEXTSHAPE{ISITALIC = NO}}}
$!TWODAXIS XDETAIL{TITLE{TEXTSHAPE{ISBOLD = YES}}}
$!TWODAXIS XDETAIL{TITLE{OFFSET = 5}}
$!TWODAXIS XDETAIL{TICKLABEL{TEXTSHAPE{FONTFAMILY = 'Helvetica'}}}
$!TWODAXIS XDETAIL{TICKLABEL{TEXTSHAPE{HEIGHT =2}}}
$!TWODAXIS XDETAIL{TICKLABEL{TEXTSHAPE{ISITALIC = NO}}}
$!TWODAXIS XDETAIL{TICKLABEL{TEXTSHAPE{ISBOLD = YES}}}
$!TWODAXIS XDETAIL{TICKLABEL{OFFSET = 2}}
$!TWODAXIS YDETAIL{TITLE{TEXTSHAPE{FONTFAMILY = 'Helvetica'}}}
$!TWODAXIS YDETAIL{TITLE{TEXTSHAPE{HEIGHT =5}}}
$!TWODAXIS YDETAIL{TITLE{TEXTSHAPE{ISITALIC = NO}}}
$!TWODAXIS YDETAIL{TITLE{TEXTSHAPE{ISBOLD = YES}}}
$!TWODAXIS YDETAIL{TITLE{OFFSET = 5}}
$!TWODAXIS YDETAIL{TICKLABEL{TEXTSHAPE{FONTFAMILY = 'Helvetica'}}}
$!TWODAXIS YDETAIL{TICKLABEL{TEXTSHAPE{HEIGHT =2}}}
$!TWODAXIS YDETAIL{TICKLABEL{TEXTSHAPE{ISITALIC = NO}}}
$!TWODAXIS YDETAIL{TICKLABEL{TEXTSHAPE{ISBOLD = YES}}}
$!TWODAXIS YDETAIL{TICKLABEL{OFFSET = 2}}
$!TWODAXIS XDETAIL{AUTOGRID = FALSE}
$!TWODAXIS XDETAIL{TICKS{MINORLINETHICKNESS = 0.3}}
$!TWODAXIS YDETAIL{AUTOGRID = TRUE}
$!TWODAXIS YDETAIL{TICKS{MINORLINETHICKNESS = 0.3}}
$!TWODAXIS XDETAIL{GRSPACING = 0.01}
$!TWODAXIS XDETAIL{TICKS{NUMMINORTICKS = 8}}
$!ACTIVEFIELDMAPS = [8]
$!FRAMELAYOUT HEIGHT = 6.2567
$!FRAMELAYOUT WIDTH = 9.0
$!FRAMELAYOUT SHOWBORDER = FALSE
$!EXPORTSETUP EXPORTFNAME = 'images\U_long.png'
$!EXPORTSETUP IMAGEWIDTH = 2000
$!EXPORT
  EXPORTREGION = CURRENTFRAME
$!DELETEZONES [8]
$!PLOTTYPE = CARTESIAN3D
$!READDATASET  'tecplot_data_files\example.plt'
$!SLICELAYERS SHOW = YES
$!SLICEATTRIBUTES 1  SLICESURFACE = ARBITRARY
$!SLICEATTRIBUTES 1  PRIMARYPOSITION{X = 0.0 Y = 0.0 Z = 0.0}
$!SLICEATTRIBUTES 1 NORMAl {X = 0 Y = -1 Z = 0}
$!SETCONTOURVAR
  VAR = 21
  CONTOURGROUP = 1
$!CONTOURLEVELS NEW
  CONTOURGROUP = 1
  RAWDATA
16
-30.0
-28.0
-26.0
-24.0
-22.0
-20.0
-18.0
-16.0
-14.0
-12.0
-10.0
-8.0
-6.0
-4.0
-2.0
0.0
$!GLOBALCONTOUR 1  LEGEND{ISVERTICAL = NO}
$!GLOBALCONTOUR 1  LABELS{AUTOLEVELSKIP = 2}
$!GLOBALCONTOUR 1  LEGEND{ROWSPACING = 1.2}
$!GLOBALCONTOUR 1
LEGEND
{
SHOW = YES
XYPOS
{
X = 100
Y = 90
}
}
$!GLOBALCONTOUR 1  LEGEND{HEADERTEXTSHAPE{FONTFAMILY = 'Helvetica'}}
$!GLOBALCONTOUR 1  LEGEND{HEADERTEXTSHAPE{HEIGHT = 5}}
$!GLOBALCONTOUR 1  LEGEND{HEADERTEXTSHAPE{ISITALIC = NO}}
$!GLOBALCONTOUR 1  LEGEND{HEADERTEXTSHAPE{ISBOLD = YES}}
$!GLOBALCONTOUR 1  LEGEND{NUMBERTEXTSHAPE{FONTFAMILY = 'Helvetica'}}
$!GLOBALCONTOUR 1  LEGEND{NUMBERTEXTSHAPE{HEIGHT = 5}}
$!GLOBALCONTOUR 1  LEGEND{NUMBERTEXTSHAPE{ISITALIC = NO}}
$!GLOBALCONTOUR 1  LEGEND{NUMBERTEXTSHAPE{ISBOLD = YES}}
$!GLOBALCONTOUR 1  COLORMAPNAME = 'Modern'
$!GLOBALCONTOUR 1  COLORMAPFILTER{COLORMAPDISTRIBUTION = CONTINUOUS}
$!GLOBALCONTOUR 1  COLORMAPFILTER{CONTINUOUSCOLOR{CMIN = -30}}
$!GLOBALCONTOUR 1  COLORMAPFILTER{CONTINUOUSCOLOR{CMAX = 0}}
$!CREATESLICEZONES
$!FIELDLAYERS SHOWCONTOUR = YES
$!PLOTTYPE = CARTESIAN2D
$!TWODAXIS XDETAIL{VARNUM = 1}
$!TWODAXIS YDETAIL{VARNUM = 3}
$!TWODAXIS
  PRESERVEAXISSCALE = TRUE
  XDETAIL
    {
    RANGEMIN = -0.0030406946326921526
    RANGEMAX = 0.10091868649126987
    }
  YDETAIL
    {
    RANGEMIN = -0.0035628683697661663
    RANGEMAX = 0.05013466738300066
    }
$!TWODAXIS
  DEPXTOYRATIO = 1.0
  GRIDAREA
  {
    EXTENTS
    {
      X1 = 12.287
      Y1 = 16.983
      X2 = 90.614
      Y2 = 75.18
    }
  }
$!TWODAXIS XDETAIL{AXISLINE{AXISALIGNMENT = WITHVIEWPORT}}
$!TWODAXIS XDETAIL{AXISLINE{POSITION = 0.0}}
$!TWODAXIS YDETAIL{AXISLINE{AXISALIGNMENT = WITHVIEWPORT}}
$!TWODAXIS YDETAIL{AXISLINE{POSITION = 0.0}}
$!TWODAXIS XDETAIL{TITLE{TEXTSHAPE{FONTFAMILY = 'Helvetica'}}}
$!TWODAXIS XDETAIL{TITLE{TEXTSHAPE{HEIGHT =5}}}
$!TWODAXIS XDETAIL{TITLE{TEXTSHAPE{ISITALIC = NO}}}
$!TWODAXIS XDETAIL{TITLE{TEXTSHAPE{ISBOLD = YES}}}
$!TWODAXIS XDETAIL{TITLE{OFFSET = 5}}
$!TWODAXIS XDETAIL{TICKLABEL{TEXTSHAPE{FONTFAMILY = 'Helvetica'}}}
$!TWODAXIS XDETAIL{TICKLABEL{TEXTSHAPE{HEIGHT =2}}}
$!TWODAXIS XDETAIL{TICKLABEL{TEXTSHAPE{ISITALIC = NO}}}
$!TWODAXIS XDETAIL{TICKLABEL{TEXTSHAPE{ISBOLD = YES}}}
$!TWODAXIS XDETAIL{TICKLABEL{OFFSET = 2}}
$!TWODAXIS YDETAIL{TITLE{TEXTSHAPE{FONTFAMILY = 'Helvetica'}}}
$!TWODAXIS YDETAIL{TITLE{TEXTSHAPE{HEIGHT =5}}}
$!TWODAXIS YDETAIL{TITLE{TEXTSHAPE{ISITALIC = NO}}}
$!TWODAXIS YDETAIL{TITLE{TEXTSHAPE{ISBOLD = YES}}}
$!TWODAXIS YDETAIL{TITLE{OFFSET = 5}}
$!TWODAXIS YDETAIL{TICKLABEL{TEXTSHAPE{FONTFAMILY = 'Helvetica'}}}
$!TWODAXIS YDETAIL{TICKLABEL{TEXTSHAPE{HEIGHT =2}}}
$!TWODAXIS YDETAIL{TICKLABEL{TEXTSHAPE{ISITALIC = NO}}}
$!TWODAXIS YDETAIL{TICKLABEL{TEXTSHAPE{ISBOLD = YES}}}
$!TWODAXIS YDETAIL{TICKLABEL{OFFSET = 2}}
$!TWODAXIS XDETAIL{AUTOGRID = FALSE}
$!TWODAXIS XDETAIL{TICKS{MINORLINETHICKNESS = 0.3}}
$!TWODAXIS YDETAIL{AUTOGRID = TRUE}
$!TWODAXIS YDETAIL{TICKS{MINORLINETHICKNESS = 0.3}}
$!TWODAXIS XDETAIL{GRSPACING = 0.01}
$!TWODAXIS XDETAIL{TICKS{NUMMINORTICKS = 8}}
$!ACTIVEFIELDMAPS = [8]
$!FRAMELAYOUT HEIGHT = 6.2567
$!FRAMELAYOUT WIDTH = 9.0
$!FRAMELAYOUT SHOWBORDER = FALSE
$!EXPORTSETUP EXPORTFNAME = 'images\W_long.png'
$!EXPORTSETUP IMAGEWIDTH = 2000
$!EXPORT
  EXPORTREGION = CURRENTFRAME
$!DELETEZONES [8]
$!PLOTTYPE = CARTESIAN3D
$!RemoveVar |MFBD|
$!Quit
