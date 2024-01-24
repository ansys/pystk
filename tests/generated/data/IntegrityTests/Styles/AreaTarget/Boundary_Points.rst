stk.v.4.3

BEGIN ReportStyle
Name		Boundary Points

BEGIN ClassId
	Class		AreaTarget
END ClassId

BEGIN Header
	StyleType		0
	Title		Boundary Points
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
	RealTimeMode		No
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
	ClassName		AreaTarget
	NameInTitle		No
	ExpandMethod		0
	PropMask		1
	ShowIntervals		No
	NumIntervals		0
	NumLines		1

BEGIN Line
	Name		Line 1
	NumElements		2

BEGIN Element
	Name		Boundary Points-Geodetic-Lat
	IsIndepVar		No
	IndepVarName		Point Number
	Title		Geodetic-Lat
	NameInTitle		Yes
	Service		BoundaryPointsDP
	Element		Geodetic-Lat
	Format		%.6f
	SumAllowedMask		7
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
		PressureUnit		Pascals
		SpecificImpulseUnit		Seconds
		PRFUnit		Hertz
		BandwidthUnit		Hertz
		SmallVelocityUnit		MetersperSecond
		RadiationDoseUnit		RadsSilicon
		RadiationShieldThicknessUnit		MilsAluminum
		MagneticFieldUnit		Tesla
END Units
END Element

BEGIN Element
	Name		Boundary Points-Geodetic-Lon
	IsIndepVar		No
	IndepVarName		Point Number
	Title		Geodetic-Lon
	NameInTitle		Yes
	Service		BoundaryPointsDP
	Element		Geodetic-Lon
	Format		%.6f
	SumAllowedMask		7
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
		PressureUnit		Pascals
		SpecificImpulseUnit		Seconds
		PRFUnit		Hertz
		BandwidthUnit		Hertz
		SmallVelocityUnit		MetersperSecond
		RadiationDoseUnit		RadsSilicon
		RadiationShieldThicknessUnit		MilsAluminum
		MagneticFieldUnit		Tesla
END Units
END Element
END Line
END Section
END ReportStyle

