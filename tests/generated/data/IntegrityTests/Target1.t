stk.v.7.0

BEGIN Target

Name        Target1

	BEGIN CentroidPosition

		CentralBody            Earth
		DisplayCoords          Geodetic
		EcfLatitude            0.00000000000000e+000
		EcfLongitude           0.00000000000000e+000
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

                MarkerColor             #00ff00
                LabelColor              #00ff00
                LineStyle               0
                MarkerStyle             14
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
            BEGIN ContourLevel
                Value      1.000000000000e+005
                Color      #ff6a6a
                LineStyle  0
                LineWidth  1
                Numbered   On
                ShowText   Off
                LabelAngle 0
            END ContourLevel
            BEGIN ContourLevel
                Value      2.000000000000e+005
                Color      #9b30ff
                LineStyle  0
                LineWidth  1
                Numbered   On
                ShowText   Off
                LabelAngle 0
            END ContourLevel
            BEGIN ContourLevel
                Value      3.000000000000e+005
                Color      #ffa500
                LineStyle  0
                LineWidth  1
                Numbered   On
                ShowText   Off
                LabelAngle 0
            END ContourLevel
            BEGIN ContourLevel
                Value      4.000000000000e+005
                Color      #f08080
                LineStyle  0
                LineWidth  1
                Numbered   On
                ShowText   Off
                LabelAngle 0
            END ContourLevel
            BEGIN ContourLevel
                Value      5.000000000000e+005
                Color      #f0ffff
                LineStyle  0
                LineWidth  1
                Numbered   On
                ShowText   Off
                LabelAngle 0
            END ContourLevel

            END RangeContourData

            END Graphics
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

