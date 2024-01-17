stk.v.6.0

BEGIN Target

Name        ChainTarget1

	BEGIN CentroidPosition

		CentralBody            Earth
		DisplayCoords          Geodetic
		EcfLatitude            3.19108280300000e+001
		EcfLongitude           -1.06125000000000e+002
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
                MarkerStyle             14
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
    
    BEGIN ExternData
    END ExternData
    
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
	Inherited          False
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

END Extensions

BEGIN SubObjects

END SubObjects

END Target

