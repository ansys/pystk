stk.v.7.0

BEGIN Facility

Name        Facility4

	BEGIN CentroidPosition

		CentralBody            Earth
		DisplayCoords          Geodetic
		EcfLatitude            5.97018653042689e+001
		EcfLongitude           -1.06604746656675e+002
		EcfAltitude            0.00000000000000e+000
		HeightAboveGround      0.00000000000000e+000
		DisplayAltRef          Ellipsoid
		UseTerrainInfo         Off
		NumAzRaysInMask        360
		TerrainNormalMode      UseCbShape

	END CentroidPosition

BEGIN Extensions
    
    BEGIN Graphics

            BEGIN Attributes

                MarkerColor             #f08080
                LabelColor              #f08080
                LineStyle               0
                MarkerStyle             9
                FontStyle               0

            END Attributes

            BEGIN Graphics

                Inherit                 On
                ShowLabel               On
                ShowAzElMask            Off
                ShowAzElFill            Off
                AzElFillStyle           7
                MinDisplayAlt           0.000
                MaxDisplayAlt           10000000.000
                NumAzElMaskSteps        1
                ShowAzElAtRangeMask       Off
                ShowAzElAtRangeFill       Off
                AzElAtRangeFillStyle      7
                MinDisplayRange           0.000
                MaxDisplayRange           10000000.000
                NumAzElAtRangeMaskSteps   1

            BEGIN RangeContourData
                    Show                 Off
                    ShowRangeFill        Off
                    RangeFillStyle       7
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
		StartTime                1 Jul 2005 12:00:00.000000000
		StopTime                 2 Jul 2005 12:00:00.000000000
		RangeConstraint         500000000.00000
		MinElevationAng         0.34907
		Duration                0.00000
		ExclHalfAng             0.08727
		MaxPVtoScenario         10
		CenterFrequency         14000000000.00000
		BandWidth               20000000.00000
		PowerFlux/EIRP          140.00000
		PowerThreshold          -32.00000
		TransmitOn              1
		ReceiveOn               0
		PVDataBase              STKData\Databases\Satellite\stkAllActive.tce
		RFIDataBase             STKData\Databases\Satellite\stkAllActive.rfi
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
		StartTime                1 Jul 2005 12:00:00.000000000
		StopTime                 2 Jul 2005 12:00:00.000000000
		RangeConstraint         500000000.00000
		MinElevationAng         0.34907
		Duration                0.00000
		ExclHalfAng             0.08727
		MaxPVtoScenario         10
		CenterFrequency         14000000000.00000
		BandWidth               20000000.00000
		PowerFlux/EIRP          140.00000
		PowerThreshold          -32.00000
		TransmitOn              1
		ReceiveOn               0
		PVDataBase              STKData\Databases\Satellite\stkAllActive.tce
		RFIDataBase             STKData\Databases\Satellite\stkAllActive.rfi
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
		LineOfSight   IncludeIntervals 
    END AccessConstraints
    
    BEGIN ObjectCoverage
    END ObjectCoverage
    
    BEGIN Desc
    END Desc
    
    BEGIN Atmosphere
	Inherit          Yes

	BEGIN Absorption

		AbsorptionModel	Simple Satcom

		BEGIN ModelData
			SWVC		    7.500000
			Temperature		293.150000

		END ModelData

	END Absorption

	RainOverride          No
	IsoHeight         2000.000000
	RainRate          1.000000
	RainModelSurfaceTemp		293.150000
    END Atmosphere
    
    BEGIN RCS
	Inherited          True
	ClutterCoef        0.000000e+000
	BEGIN RCSBAND
		ConstantValue      0.000000e+000
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

