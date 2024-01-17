stk.v.6.0

BEGIN Facility

Name        ChainFac3

	BEGIN CentroidPosition

		CentralBody            Earth
		DisplayCoords          Geodetic
		EcfLatitude            2.38853503200000e+001
		EcfLongitude           -1.11375000000000e+002
		EcfAltitude            0.00000000000000e+000
		UseTerrainInfo         Off
		HeightAdjustment       0.00000000000000e+000
		NumAzRaysInMask        360
		TerrainNormalMode      UseCbShape

	END CentroidPosition

BEGIN Extensions
    
    BEGIN Graphics

            BEGIN Attributes

                MarkerColor             #ffffff
                LabelColor              #ffffff
                LineStyle               0
                MarkerStyle             9
                FontStyle               0

            END Attributes

            BEGIN Graphics

                Inherit                 On
                ShowLabel               On
                ShowAzElMask            Off
                MinDisplayAlt           0.000
                MaxDisplayAlt           10000.000
                NumAzElMaskSteps        1
                ShowAzElAtRangeMask       Off
                MinDisplayRange           0.000
                MaxDisplayRange           10000000.000
                NumAzElAtRangeMaskSteps   1

            END Graphics

            BEGIN LblNotes


            END LblNotes

    END Graphics
    
    BEGIN LaserCAT
		Mode                     TargetObject
		StartTime                1 Jan 1997 00:00:00.000000000
		StopTime                 1 Jan 1997 04:00:00.000000000
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
		PVDataBase              STKData/Databases/Satellite/stkAllActive.tce
		RFIDataBase             STKData/Databases/Satellite/stkAllActive.rfi
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
		StartTime                1 Jan 1997 00:00:00.000000000
		StopTime                 1 Jan 1997 04:00:00.000000000
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
		PVDataBase              STKData/Databases/Satellite/stkAllActive.tce
		RFIDataBase             STKData/Databases/Satellite/stkAllActive.rfi
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
	IsoHeight         0.000000
	RainRate          0.000000
	RainModelSurfaceTemp		0.000000
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

