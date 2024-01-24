stk.v.7.0

BEGIN ReportStyle
Name		Boresight Intersection Times

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
	VerticalGridLines		No
	HorizontalGridLines		No
	NumAnnotations		3
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
	ClassName		Sensor
	NameInTitle		No
	ExpandMethod		0
	PropMask		4
	ShowIntervals		No
	NumIntervals		0
	NumLines		1

BEGIN Line
	Name		Line 1
	NumElements		9

BEGIN Element
	Name		Boresight Intersection Times-Start Time
	IsIndepVar		No
	Title		Start Time
	NameInTitle		Yes
	Service		BoreIntersectTimes
	Element		Start Time
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
	Name		Boresight Intersection Times-Stop Time
	IsIndepVar		No
	Title		Stop Time
	NameInTitle		Yes
	Service		BoreIntersectTimes
	Element		Stop Time
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
	Name		Boresight Intersection Times-Duration
	IsIndepVar		No
	Title		Duration
	NameInTitle		Yes
	Service		BoreIntersectTimes
	Element		Duration
	SumAllowedMask		223
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
	Name		Boresight Intersection Times-Inertial Angle
	IsIndepVar		No
	Title		Inertial Angle
	NameInTitle		Yes
	Service		BoreIntersectTimes
	Element		Inertial Angle
	SumAllowedMask		223
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
		ForceUnit		Newtons
		PressureUnit		Pascals
		SpecificImpulseUnit		Seconds
		PRFUnit		Hertz
		BandwidthUnit		Hertz
		SmallVelocityUnit		MetersperSecond
		DataRateUnit		BitsPerSecond
		Percent		UnitValue
		UnitTemperature		UnitKelvin
		MissionModelerDistanceUnit		Meters
		MissionModelerTimeUnit		Seconds
		MissionModelerAltitudeUnit		Meters
		MissionModelerFuelQuantityUnit		Kilograms
		MissionModelerRunwayLengthUnit		Meters
		MissionModelerBearingAngleUnit		Radians
		MissionModelerAngleOfAttackUnit		Radians
		MissionModelerAttitudeAngleUnit		Radians
		MissionModelerGUnit		StandardSeaLevelG
		RadiationDoseUnit		RadsSilicon
		RadiationShieldThicknessUnit		MilsAluminum
		MagneticFieldUnit		Tesla
END Units
END Element

BEGIN Element
	Name		Boresight Intersection Times-Earth Fixed Central Angle
	IsIndepVar		No
	Title		Earth Fixed Central Angle
	NameInTitle		Yes
	Service		BoreIntersectTimes
	Element		Earth Fixed Central Angle
	SumAllowedMask		223
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
		ForceUnit		Newtons
		PressureUnit		Pascals
		SpecificImpulseUnit		Seconds
		PRFUnit		Hertz
		BandwidthUnit		Hertz
		SmallVelocityUnit		MetersperSecond
		DataRateUnit		BitsPerSecond
		Percent		UnitValue
		UnitTemperature		UnitKelvin
		MissionModelerDistanceUnit		Meters
		MissionModelerTimeUnit		Seconds
		MissionModelerAltitudeUnit		Meters
		MissionModelerFuelQuantityUnit		Kilograms
		MissionModelerRunwayLengthUnit		Meters
		MissionModelerBearingAngleUnit		Radians
		MissionModelerAngleOfAttackUnit		Radians
		MissionModelerAttitudeAngleUnit		Radians
		MissionModelerGUnit		StandardSeaLevelG
		RadiationDoseUnit		RadsSilicon
		RadiationShieldThicknessUnit		MilsAluminum
		MagneticFieldUnit		Tesla
END Units
END Element

BEGIN Element
	Name		Boresight Intersection Times-Start Pass Number
	IsIndepVar		No
	Title		Start Pass Number
	NameInTitle		Yes
	Service		BoreIntersectTimes
	Element		Start Pass Number
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

BEGIN Element
	Name		Boresight Intersection Times-Stop Pass Number
	IsIndepVar		No
	Title		Stop Pass Number
	NameInTitle		Yes
	Service		BoreIntersectTimes
	Element		Stop Pass Number
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

BEGIN Element
	Name		Boresight Intersection Times-Start Path Number
	IsIndepVar		No
	Title		Start Path Number
	NameInTitle		Yes
	Service		BoreIntersectTimes
	Element		Start Path Number
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

BEGIN Element
	Name		Boresight Intersection Times-Stop Path Number
	IsIndepVar		No
	Title		Stop Path Number
	NameInTitle		Yes
	Service		BoreIntersectTimes
	Element		Stop Path Number
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
END ReportStyle

