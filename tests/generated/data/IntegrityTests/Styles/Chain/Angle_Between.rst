stk.v.6.1

BEGIN ReportStyle
Name		Angle Between

BEGIN ClassId
	Class		Chain
END ClassId

BEGIN Header
	StyleType		0
	Title		Angle Between Objects
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
	BackgroundColor		#ffffff
	ViewableDuration		0.000000
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
	ClassName		Chain
	NameInTitle		No
	ExpandMethod		0
	PropMask		2562
	ShowIntervals		No
	NumIntervals		0
	NumLines		1

BEGIN Line
	Name		Line 1
	NumElements		4

BEGIN Element
	Name		Time
	IsIndepVar		Yes
	IndepVarName		Time
	Title		Time
	NameInTitle		No
	Service		AngleBetween
	Type		Granularity Determined
	Element		Time
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
	Name		Angle Between-Granularity Determined-Angle
	IsIndepVar		No
	IndepVarName		Time
	Title		Angle
	NameInTitle		No
	Service		AngleBetween
	Type		Granularity Determined
	Element		Angle
	SumAllowedMask		7
	SummaryOnly		No
	DataType		0
	UnitType		3
	LineStyle		0
	LineWidth		0
	LineColor		#000000
	PointStyle		0
	PointSize		0
	PointColor		#000000
	FillPattern		0
	FillColor		#000000
	PropMask		0
	UseScenUnits		No
BEGIN Units
		DistanceUnit		Meters
		TimeUnit		Seconds
		DateFormat		EpochSeconds
		AngleUnit		Degrees
		MassUnit		Kilograms
		PowerUnit		dBW
		FrequencyUnit		Hertz
		SmallDistanceUnit		Meters
		LatitudeUnit		Radians
		LongitudeUnit		Radians
		DurationUnit		Seconds
		Temperature		Kelvin
		SmallTimeUnit		Seconds
		RatioUnit		Decibel
		RcsUnit		Decibel
		DopplerVelocityUnit		MetersperSecond
		SARTimeResProdUnit		Meter-Second
		PowerSpectralDensityUnit		Decibels(WattsperHertz)
		ForceUnit		Newtons
		PressureUnit		Pascals
		SpecificImpulseUnit		Seconds
		PRFUnit		Hertz
		BandwidthUnit		Hertz
		SmallVelocityUnit		MetersperSecond
		DataRateUnit		BitsPerSecond
		Percent		UnitValue
		PowerFluxDensityUnit		Decibels(Wattspermetersquared)
		SpectralDensityUnit		Decibel-Hertz
		FlightAircraftDistanceUnit		Meters
		FlightAircraftTimeUnit		Seconds
		FlightAltitudeUnit		Meters
		FlightFuelQuantityUnit		Kilograms
		FlightRunwayLengthUnit		Meters
		FlightBearingAngleUnit		Radians
		FlightAngleOfAttackUnit		Radians
		FlightAttitudeAngleUnit		Radians
		FlightGUnit		StandardSeaLevelG
		RadiationDoseUnit		RadsSilicon
		RadiationShieldThicknessUnit		MilsAluminum
		MagneticFieldUnit		Tesla
END Units
END Element

BEGIN Element
	Name		Angle Between-Granularity Determined-Range 1
	IsIndepVar		No
	IndepVarName		Time
	Title		Range 1
	NameInTitle		No
	Service		AngleBetween
	Type		Granularity Determined
	Element		Range 1
	SumAllowedMask		7
	SummaryOnly		No
	DataType		0
	UnitType		0
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
	Name		Angle Between-Granularity Determined-Range 2
	IsIndepVar		No
	IndepVarName		Time
	Title		Range 2
	NameInTitle		No
	Service		AngleBetween
	Type		Granularity Determined
	Element		Range 2
	SumAllowedMask		7
	SummaryOnly		No
	DataType		0
	UnitType		0
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

