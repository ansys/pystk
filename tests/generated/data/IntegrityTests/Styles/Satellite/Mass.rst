stk.v.4.0

BEGIN ReportStyle
Name		Mass

BEGIN ClassId
	Class		Satellite
END ClassId

BEGIN Header
	StyleType		0
	Date		Yes
	Name		Yes
	DescShort		No
	DescLong		No
	YLog10		No
	Y2Log10		No
	Ticks		No
	GridLines		No
	NumAnnotations		3
	AnnotationRotation		1
	NumTick		12
	NumGridX		12
	NumGridY		12
	BackgroundColor		7
	ViewableDuration		3600.000000
	LegendStatus		1

BEGIN PostProcessor
	Destination	0
	Use	0
	Destination	1
	Use	0
	Destination	2
	Use	0
	Destination	3
	Use	0
END PostProcessor
	NumSections		1
END Header

BEGIN Section
	Name		Section 1
	ClassName		Satellite
	NameInTitle		No
	ExpandMethod		0
	PropMask		1
	ShowIntervals		No
	NumIntervals		0
	NumLines		1

BEGIN Line
	Name		Line 1
	NumElements		1

BEGIN Element
	Name		Mass-Mass
	IsIndepVar		No
	Title		Mass
	NameInTitle		Yes
	Service		MassData
	Element		Mass
	SumAllowedMask		0
	SummaryOnly		No
	DataType		0
	UnitType		8
	LineStyle		0
	LineWidth		0
	LineColor		0
	PointStyle		0
	PointSize		0
	PointColor		0
	FillPattern		0
	FillColor		0
	UseScenUnits		Yes
END Element
END Line
END Section
END ReportStyle

