stk.v.8.0

BEGIN ReportStyle
Name		Global Satisfaction Intervals

BEGIN ClassId
	Class		FigureOfMerit
END ClassId

BEGIN Header
	StyleType		0
	Date		Yes
	Name		Yes
	DescShort		No
	DescLong		No
	YLog10		No
	Y2Log10		No
	VerticalGridLines		No
	HorizontalGridLines		No
	AnnotationType		Spaced
	NumAnnotations		3
	NumAngularAnnotations		5
	AnnotationRotation		1
	BackgroundColor		#ffffff
	ViewableDuration		3600.000000
	RealTimeMode		No
	ReadOnlyMode		Yes
	DayLinesStatus		1
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
	NumSections		2
END Header

BEGIN Section
	Name		Section 1
	ClassName		FigureOfMerit
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
	Name		FOM Definition-FOM Properties
	IsIndepVar		No
	Title		FOM Properties
	NameInTitle		Yes
	Service		GenInfo
	Element		FOM Properties
	SumAllowedMask		0
	SummaryOnly		No
	DataType		2
	UnitType		6
	LineStyle		0
	LineWidth		0
	LineColor		#000000
	PointStyle		0
	PointSize		0
	PointColor		#000000
	FillPattern		0
	FillColor		#000000
	PropMask		0
	UseScenUnits		Yes
END Element
END Line
END Section

BEGIN Section
	Name		Section 2
	ClassName		FigureOfMerit
	NameInTitle		No
	ExpandMethod		0
	PropMask		516
	ShowIntervals		No
	NumIntervals		0
	NumLines		1

BEGIN Line
	Name		Line 1
	NumElements		5

BEGIN Element
	Name		Global Total Satisfaction-Interval Number
	IsIndepVar		No
	Title		Interval
	NameInTitle		Yes
	Service		TotalGlobalSat
	Element		Interval Number
	SumAllowedMask		32
	SummaryOnly		No
	DataType		1
	UnitType		6
	LineStyle		0
	LineWidth		0
	LineColor		#000000
	PointStyle		0
	PointSize		0
	PointColor		#000000
	FillPattern		0
	FillColor		#000000
	PropMask		0
	UseScenUnits		Yes
END Element

BEGIN Element
	Name		Global Total Satisfaction-Interval Start
	IsIndepVar		No
	Title		Interval Start
	NameInTitle		Yes
	Service		TotalGlobalSat
	Element		Interval Start
	SumAllowedMask		0
	SummaryOnly		No
	DataType		0
	UnitType		2
	LineStyle		0
	LineWidth		0
	LineColor		#000000
	PointStyle		0
	PointSize		0
	PointColor		#000000
	FillPattern		0
	FillColor		#000000
	PropMask		0
	UseScenUnits		Yes
END Element

BEGIN Element
	Name		Global Total Satisfaction-Interval End
	IsIndepVar		No
	Title		Interval End
	NameInTitle		Yes
	Service		TotalGlobalSat
	Element		Interval End
	SumAllowedMask		0
	SummaryOnly		No
	DataType		0
	UnitType		2
	LineStyle		0
	LineWidth		0
	LineColor		#000000
	PointStyle		0
	PointSize		0
	PointColor		#000000
	FillPattern		0
	FillColor		#000000
	PropMask		0
	UseScenUnits		Yes
END Element

BEGIN Element
	Name		Global Total Satisfaction-Duration
	IsIndepVar		No
	Title		Duration
	NameInTitle		Yes
	Service		TotalGlobalSat
	Element		Duration
	SumAllowedMask		15
	SummaryOnly		No
	DataType		0
	UnitType		1
	LineStyle		0
	LineWidth		0
	LineColor		#000000
	PointStyle		0
	PointSize		0
	PointColor		#000000
	FillPattern		0
	FillColor		#000000
	PropMask		0
	UseScenUnits		Yes
END Element

BEGIN Element
	Name		Global Total Satisfaction-Percent
	IsIndepVar		No
	Title		Percent
	NameInTitle		Yes
	Service		TotalGlobalSat
	Element		Percent
	SumAllowedMask		15
	SummaryOnly		No
	DataType		0
	UnitType		6
	LineStyle		0
	LineWidth		0
	LineColor		#000000
	PointStyle		0
	PointSize		0
	PointColor		#000000
	FillPattern		0
	FillColor		#000000
	PropMask		0
	UseScenUnits		Yes
END Element
END Line
END Section
END ReportStyle

