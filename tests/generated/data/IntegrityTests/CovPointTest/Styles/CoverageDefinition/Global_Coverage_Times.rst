stk.v.8.0

BEGIN ReportStyle
Name		Global Coverage Times

BEGIN ClassId
	Class		CoverageDefinition
END ClassId

BEGIN Header
	StyleType		0
	Title		Periods of Global Coverage
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
	NumSections		1
END Header

BEGIN Section
	Name		Section 1
	ClassName		CoverageDefinition
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
	Name		Global Coverage-Global Coverage Number
	IsIndepVar		No
	Title		Number
	NameInTitle		Yes
	Service		GlobalCov
	Element		Global Coverage Number
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
	Name		Global Coverage-Global Coverage Start
	IsIndepVar		No
	Title		Coverage Start
	NameInTitle		Yes
	Service		GlobalCov
	Element		Global Coverage Start
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
	Name		Global Coverage-Global Coverage End
	IsIndepVar		No
	Title		Coverage End
	NameInTitle		Yes
	Service		GlobalCov
	Element		Global Coverage End
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
	Name		Global Coverage-Duration
	IsIndepVar		No
	Title		Duration
	NameInTitle		Yes
	Service		GlobalCov
	Element		Duration
	Format		%.3f
	SumAllowedMask		15
	SummaryOnly		No
	SumRequestMask		11
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
	Name		Global Coverage-Percent
	IsIndepVar		No
	Title		Percent
	NameInTitle		Yes
	Service		GlobalCov
	Element		Percent
	Format		%.6f
	SumAllowedMask		15
	SummaryOnly		No
	SumRequestMask		8
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

