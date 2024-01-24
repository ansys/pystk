stk.v.4.0

BEGIN ReportStyle
Name		Pass Data

BEGIN ClassId
	Class		Satellite
END ClassId

BEGIN Header
	StyleType		0
	Title		Pass Information
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
	NameInTitle		Yes
	ExpandMethod		0
	PropMask		4
	ShowIntervals		No
	NumIntervals		0
	NumLines		2

BEGIN Line
	Name		Line 1
	NumElements		6

BEGIN Element
	Name		Pass Number
	IsIndepVar		Yes
	IndepVarName		Pass Number
	Title		Pass
	NameInTitle		No
	Service		Passes
	Element		Pass Number
	SumAllowedMask		0
	SummaryOnly		No
	DataType		1
	UnitType		6
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
	Name		Passes-Start Time
	IsIndepVar		No
	IndepVarName		Pass Number
	Title		Start Time
	NameInTitle		No
	Service		Passes
	Element		Start Time
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
	Name		Passes-Apogee
	IsIndepVar		No
	IndepVarName		Pass Number
	Title		Apogee
	NameInTitle		No
	Service		Passes
	Element		Apogee
	SumAllowedMask		0
	SummaryOnly		No
	DataType		3
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
	Name		Passes-Time of Apogee
	IsIndepVar		No
	IndepVarName		Pass Number
	Title		Time of Apogee
	NameInTitle		No
	Service		Passes
	Element		Time of Apogee
	SumAllowedMask		0
	SummaryOnly		No
	DataType		3
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
	Name		Passes-Period
	IsIndepVar		No
	IndepVarName		Pass Number
	Title		Period
	NameInTitle		No
	Service		Passes
	Element		Period
	SumAllowedMask		0
	SummaryOnly		No
	DataType		3
	UnitType		1
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
	Name		Passes-Lon Ascen Node
	IsIndepVar		No
	IndepVarName		Pass Number
	Title		Lon Ascen Node
	NameInTitle		No
	Service		Passes
	Element		Lon Ascen Node
	SumAllowedMask		0
	SummaryOnly		No
	DataType		3
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
		AngleUnit		Degrees
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
END Units
END Element
END Line

BEGIN Line
	Name		Line 2
	NumElements		5

BEGIN Element
	Name		Passes-End Time
	IsIndepVar		No
	IndepVarName		Pass Number
	Title		End Time
	NameInTitle		No
	Service		Passes
	Element		End Time
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
	Name		Passes-Perigee
	IsIndepVar		No
	IndepVarName		Pass Number
	Title		Perigee
	NameInTitle		No
	Service		Passes
	Element		Perigee
	SumAllowedMask		0
	SummaryOnly		No
	DataType		3
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
	Name		Passes-Time of Perigee
	IsIndepVar		No
	IndepVarName		Pass Number
	Title		Time of Perigee
	NameInTitle		No
	Service		Passes
	Element		Time of Perigee
	SumAllowedMask		0
	SummaryOnly		No
	DataType		3
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
	Name		Passes-Right Ascen
	IsIndepVar		No
	IndepVarName		Pass Number
	Title		Right Ascen
	NameInTitle		No
	Service		Passes
	Element		Right Ascen
	SumAllowedMask		0
	SummaryOnly		No
	DataType		3
	UnitType		3
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
		PowerDensityUnit		Decibels
END Units
END Element

BEGIN Element
	Name		Passes-Lon Descen Node
	IsIndepVar		No
	IndepVarName		Pass Number
	Title		Lon Descen Node
	NameInTitle		No
	Service		Passes
	Element		Lon Descen Node
	SumAllowedMask		0
	SummaryOnly		No
	DataType		3
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
		AngleUnit		Degrees
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
END Units
END Element
END Line
END Section
END ReportStyle

