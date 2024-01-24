stk.v.4.0

BEGIN ReportStyle
Name		Pattern Intersection

BEGIN ClassId
	Class		Sensor
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
	ClassName		Sensor
	NameInTitle		No
	ExpandMethod		0
	PropMask		1024
	ShowIntervals		No
	NumIntervals		0
	NumLines		1

BEGIN Line
	Name		Line 1
	NumElements		2

BEGIN Element
	Name		Pattern Intersection-Latitude
	IsIndepVar		No
	Title		Latitude
	NameInTitle		Yes
	Service		PatternIntersectPts
	Element		Latitude
	SumAllowedMask		0
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
	UseScenUnits		No
BEGIN Units
		DistanceUnit		Meters
		TimeUnit		Seconds
		DateFormat		EpochSeconds
		AngleUnit		Radians
		MassUnit		Kilograms
		PowerUnit		dBW
		FrequencyUnit		Hertz
		SmallDistanceUnit		Meters
		LatitudeUnit		Degrees
		LongitudeUnit		Radians
		DurationUnit		Seconds
		Temperature		Kelvin
		SmallTimeUnit		Seconds
		RatioUnit		Decibel
		RcsUnit		Decibel
		DopplerVelocityUnit		MetersperSecond
		SARTimeResProdUnit		Meter-Second
		PowerDensityUnit		Decibels
		ForceUnit		Newtons
END Units
END Element

BEGIN Element
	Name		Pattern Intersection-Longitude
	IsIndepVar		No
	Title		Longitude
	NameInTitle		Yes
	Service		PatternIntersectPts
	Element		Longitude
	SumAllowedMask		0
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
	UseScenUnits		No
BEGIN Units
		DistanceUnit		Meters
		TimeUnit		Seconds
		DateFormat		EpochSeconds
		AngleUnit		Radians
		MassUnit		Kilograms
		PowerUnit		dBW
		FrequencyUnit		Hertz
		SmallDistanceUnit		Meters
		LatitudeUnit		Radians
		LongitudeUnit		Degrees
		DurationUnit		Seconds
		Temperature		Kelvin
		SmallTimeUnit		Seconds
		RatioUnit		Decibel
		RcsUnit		Decibel
		DopplerVelocityUnit		MetersperSecond
		SARTimeResProdUnit		Meter-Second
		PowerDensityUnit		Decibels
		ForceUnit		Newtons
END Units
END Element
END Line
END Section
END ReportStyle

