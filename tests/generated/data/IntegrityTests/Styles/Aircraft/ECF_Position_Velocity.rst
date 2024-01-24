stk.v.4.0

BEGIN ReportStyle
Name		ECF Position Velocity

BEGIN ClassId
	Class		Aircraft
END ClassId

BEGIN Header
	StyleType		0
	Title		ECF Position & Velocity
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
	ClassName		Aircraft
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
	Service		CartPos
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
	Name		Cartesian Position-Fixed-x
	IsIndepVar		No
	IndepVarName		Time
	Title		x
	NameInTitle		No
	Service		CartPos
	Type		Fixed
	Element		x
	SumAllowedMask		0
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
	Name		Cartesian Position-Fixed-y
	IsIndepVar		No
	IndepVarName		Time
	Title		y
	NameInTitle		No
	Service		CartPos
	Type		Fixed
	Element		y
	SumAllowedMask		0
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
	Name		Cartesian Position-Fixed-z
	IsIndepVar		No
	IndepVarName		Time
	Title		z
	NameInTitle		No
	Service		CartPos
	Type		Fixed
	Element		z
	SumAllowedMask		0
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
	Name		Cartesian Velocity-Fixed-x
	IsIndepVar		No
	IndepVarName		Time
	Title		vx
	NameInTitle		No
	Service		CartVel
	Type		Fixed
	Element		x
	SumAllowedMask		0
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

BEGIN Element
	Name		Cartesian Velocity-Fixed-y
	IsIndepVar		No
	IndepVarName		Time
	Title		vy
	NameInTitle		No
	Service		CartVel
	Type		Fixed
	Element		y
	SumAllowedMask		0
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

BEGIN Element
	Name		Cartesian Velocity-Fixed-z
	IsIndepVar		No
	IndepVarName		Time
	Title		vz
	NameInTitle		No
	Service		CartVel
	Type		Fixed
	Element		z
	SumAllowedMask		0
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

