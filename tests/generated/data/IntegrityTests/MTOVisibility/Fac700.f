stk.v.9.0
WrittenBy    STK_v9.0.0

BEGIN Facility

Name        Fac700

	BEGIN CentroidPosition

		CentralBody            Earth
		DisplayCoords          Geodetic
		EcfLatitude            5.80000000000000e+001
		EcfLongitude           0.00000000000000e+000
		EcfAltitude            7.50000000000000e+002
		HeightAboveGround      0.00000000000000e+000
		DisplayAltRef          Ellipsoid
		UseTerrainInfo         Off
		NumAzRaysInMask        360
		TerrainNormalMode      UseCbShape

	END CentroidPosition

BEGIN Extensions
    
    BEGIN Graphics

            BEGIN Attributes

                MarkerColor             #ff0000
                LabelColor              #ff0000
                LineStyle               0
                MarkerStyle             9
                FontStyle               0

            END Attributes

            BEGIN Graphics

                Inherit                 On
                IsDynamic               Off
                ShowLabel               On
                ShowAzElMask            Off
                ShowAzElFill            Off
                AzElFillStyle           7
                UseAzElColor               Off
                AzElColor               #ffffff
                MinDisplayAlt           1000.000
                MaxDisplayAlt           10000000.000
                NumAzElMaskSteps        1
                ShowAzElAtRangeMask       Off
                ShowAzElAtRangeFill       Off
                AzElAtRangeFillStyle      7
                UseAzElAtRangeColor          Off
                AzElAtRangeColor          #ffffff
                MinDisplayRange           0.000
                MaxDisplayRange           10000000.000
                NumAzElAtRangeMaskSteps   1

            BEGIN RangeContourData
                    Show                 Off
                    ShowRangeFill        Off
                    RangeFillStyle       7
                    LabelUnits           4
                    NumDecimalDigits     3
            BEGIN ContourLevel
                Value      1.000000000000e+005
                Color      #4169e1
                LineStyle  0
                LineWidth  1
                Numbered   On
                ShowText   Off
                LabelAngle 180
            END ContourLevel
            BEGIN ContourLevel
                Value      2.000000000000e+005
                Color      #87cefa
                LineStyle  0
                LineWidth  1
                Numbered   On
                ShowText   Off
                LabelAngle 180
            END ContourLevel
            BEGIN ContourLevel
                Value      3.000000000000e+005
                Color      #00ced1
                LineStyle  0
                LineWidth  1
                Numbered   On
                ShowText   Off
                LabelAngle 180
            END ContourLevel
            BEGIN ContourLevel
                Value      4.000000000000e+005
                Color      #6b8e23
                LineStyle  0
                LineWidth  1
                Numbered   On
                ShowText   Off
                LabelAngle 180
            END ContourLevel
            BEGIN ContourLevel
                Value      5.000000000000e+005
                Color      #8fbc8f
                LineStyle  0
                LineWidth  1
                Numbered   On
                ShowText   Off
                LabelAngle 180
            END ContourLevel

            END RangeContourData

            END Graphics
    END Graphics
    
    BEGIN LaserCAT
		Mode                     TargetObject
		StartTime                1 Jul 2007 12:00:00.000000000
		StopTime                 2 Jul 2007 12:00:00.000000000
		RangeConstraint         500000000.00000
		MinElevationAng         0.34907
		Duration                0.00000
		ExclHalfAng             0.08727
		MaxPVtoScenario         10
		CenterFrequency         14000000000.00000
		BandWidth               20000000.00000
		Linear_PowerFlux/EIRP   1.0000000000000e+014
		Linear_PowerThreshold   6.3095734448019e-004
		TransmitOn              1
		ReceiveOn               0
		PVDataBase              STKData\Databases\Satellite\stkSatDb.tce
		RFIDataBase             STKData\Databases\Satellite\stkAllComm.rfi
		LaserDispersionAngle    0.00000
		KOCTimeStep             1.00000
		UseOutOfDate            Yes
		NearEarthOutOfDate       10.00000
		DeepSpaceOutOfDate       40.00000
		ModelIntrackUncert      Yes
		UseTrajectoryFilter     No
		UsePotVictimList        No
    END LaserCAT
    
    BEGIN ExternData
    END ExternData
    
    BEGIN RFI
		Mode                     TargetObject
		StartTime                1 Jul 2007 12:00:00.000000000
		StopTime                 2 Jul 2007 12:00:00.000000000
		RangeConstraint         500000000.00000
		MinElevationAng         0.34907
		Duration                0.00000
		ExclHalfAng             0.08727
		MaxPVtoScenario         10
		CenterFrequency         14000000000.00000
		BandWidth               20000000.00000
		Linear_PowerFlux/EIRP   1.0000000000000e+014
		Linear_PowerThreshold   6.3095734448019e-004
		TransmitOn              1
		ReceiveOn               0
		PVDataBase              STKData\Databases\Satellite\stkAllComm.tce
		RFIDataBase             STKData\Databases\Satellite\stkAllComm.rfi
		LaserDispersionAngle    0.00000
		KOCTimeStep             1.00000
		UseOutOfDate            Yes
		NearEarthOutOfDate       10.00000
		DeepSpaceOutOfDate       40.00000
		ModelIntrackUncert      Yes
		UseTrajectoryFilter     No
		UsePotVictimList        No
    END RFI
    
    BEGIN AccessConstraints
    END AccessConstraints
    
    BEGIN ObjectCoverage
    END ObjectCoverage
    
    BEGIN Desc
    END Desc
    
    BEGIN Atmosphere
<!-- STKv4.0 Format="XML" -->
<STKOBJECT>
<OBJECT Class = "AtmosphereExtension" Name = "Atmosphere_Extension">
    <OBJECT Class = "link" Name = "AtmosAbsorptionModel">
        <OBJECT Class = "AtmosphericAbsorptionModel" Name = "Simple_Satcom">
            <OBJECT Class = "string" Name = "Description"> &quot;Simple Satcom&quot; </OBJECT>
            <OBJECT Class = "bool" Name = "ReadOnly"> False </OBJECT>
            <OBJECT Class = "double" Name = "SurfaceTemperature"> 293.15 K </OBJECT>
            <OBJECT Class = "string" Name = "Type"> &quot;CAgCRRFPropModelAtmosAbsorptionSimpleSatcom&quot; </OBJECT>
            <OBJECT Class = "string" Name = "UserComment"> &quot;Simple Satcom&quot; </OBJECT>
            <OBJECT Class = "string" Name = "Version"> &quot;1.0.0 a&quot; </OBJECT>
            <OBJECT Class = "double" Name = "WaterVaporConcentration"> 7.5 g*m^-3 </OBJECT>
        </OBJECT>
    </OBJECT>
    <OBJECT Class = "string" Name = "Description"> &quot;Atmosphere Extension&quot; </OBJECT>
    <OBJECT Class = "bool" Name = "InheritAtmosAbsorptionModel"> True </OBJECT>
    <OBJECT Class = "double" Name = "RainOverrideIsoHeight"> 2000 m </OBJECT>
    <OBJECT Class = "double" Name = "RainOverrideRate"> 1 mm*hr^-1 </OBJECT>
    <OBJECT Class = "double" Name = "RainOverrideSurfaceTemp"> 293.15 K </OBJECT>
    <OBJECT Class = "bool" Name = "RainOverride"> False </OBJECT>
    <OBJECT Class = "bool" Name = "ReadOnly"> False </OBJECT>
    <OBJECT Class = "string" Name = "Type"> &quot;CAgSTKAtmosphereExt&quot; </OBJECT>
    <OBJECT Class = "string" Name = "UserComment"> &quot;Atmosphere Extension&quot; </OBJECT>
    <OBJECT Class = "string" Name = "Version"> &quot;1.0.0 a&quot; </OBJECT>
</OBJECT>
</STKOBJECT>
    END Atmosphere
    
    BEGIN RCS
	Inherited          True
	LinearClutterCoef        1.000000e+000
	BEGIN RCSBAND
		LinearConstantValue      1.000000e+000
		Swerling      0
		BandData      3.000000e+006 3.000000e+011
	END RCSBAND
    END RCS
    
    BEGIN DisplayTm
		DisplayGT	AlwaysOff
		DisplayType	AlwaysOn
    END DisplayTm
    
    BEGIN Identification
    END Identification
    
    BEGIN Crdn
    END Crdn
    
    BEGIN VO
    END VO
    
    BEGIN PODS
        FacilityID       0
        ElAngCutoff      1.000000e+001
        LocEstimate      No
        UseTransponderDelay      No
        TransponderDelay     0.000000000000e+000
    END PODS

END Extensions

BEGIN SubObjects

END SubObjects

END Facility

