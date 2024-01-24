stk.v.4.0

BEGIN ReportStyle
Name		LLA Position

BEGIN ClassId
	Class		Satellite
END ClassId

BEGIN Header
	StyleType		0
	Title		LLA Position
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
	ViewableDuration		0.000000

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
	PropMask		2
	ShowIntervals		No
	NumIntervals		0
	NumLines		1

BEGIN Line
	Name		Line 1
	NumElements		7

BEGIN Element
	Name		Time
	IsIndepVar		Yes
	IndepVarName		Time
	Title		Time
	NameInTitle		No
	Service		LLAState
	Type		Fixed
	Element		Time
	SumAllowedMask		0
	SummaryOnly		No
	DataType		0
	UnitType		2
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

BEGIN Element
	Name		LLA State-Fixed-Lat
	IsIndepVar		No
	IndepVarName		Time
	Title		Lat
	NameInTitle		No
	Service		LLAState
	Type		Fixed
	Element		Lat
	SumAllowedMask		23
	SummaryOnly		No
	DataType		0
	UnitType		19
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

BEGIN Element
	Name		LLA State-Fixed-Lon
	IsIndepVar		No
	IndepVarName		Time
	Title		Lon
	NameInTitle		No
	Service		LLAState
	Type		Fixed
	Element		Lon
	SumAllowedMask		23
	SummaryOnly		No
	DataType		0
	UnitType		20
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

BEGIN Element
	Name		LLA State-Fixed-Alt
	IsIndepVar		No
	IndepVarName		Time
	Title		Alt
	NameInTitle		No
	Service		LLAState
	Type		Fixed
	Element		Alt
	SumAllowedMask		23
	SummaryOnly		No
	DataType		0
	UnitType		0
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

BEGIN Element
	Name		LLA State-Fixed-Lat Rate
	IsIndepVar		No
	IndepVarName		Time
	Title		Lat Rate
	NameInTitle		No
	Service		LLAState
	Type		Fixed
	Element		Lat Rate
	SumAllowedMask		23
	SummaryOnly		No
	DataType		0
	UnitType		7
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

BEGIN Element
	Name		LLA State-Fixed-Lon Rate
	IsIndepVar		No
	IndepVarName		Time
	Title		Lon Rate
	NameInTitle		No
	Service		LLAState
	Type		Fixed
	Element		Lon Rate
	SumAllowedMask		23
	SummaryOnly		No
	DataType		0
	UnitType		7
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

BEGIN Element
	Name		LLA State-Fixed-Alt Rate
	IsIndepVar		No
	IndepVarName		Time
	Title		Alt Rate
	NameInTitle		No
	Service		LLAState
	Type		Fixed
	Element		Alt Rate
	SumAllowedMask		23
	SummaryOnly		No
	DataType		0
	UnitType		4
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

