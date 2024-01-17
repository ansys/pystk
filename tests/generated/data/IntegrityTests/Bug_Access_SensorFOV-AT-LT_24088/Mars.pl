stk.v.7.0

BEGIN Planet

Name        Mars

BEGIN PathDescription

		CentralBody                    Mars
		UseCbEphemeris                 Yes

BEGIN               EphemerisData

	EphemerisSource             JplDE

	JplIndex                    3

	JplSpiceId                  499

	ApplyTDTtoTDBCorrectionForDE     No

      OrbitEpoch                  2451545.0000000
      OrbitMeanDist               227936636175.28
      OrbitEcc                    0.093412330000000
      OrbitInc                    24.677207936585
      OrbitRAAN                   3.3758381193784
      OrbitPerLong                336.33376607352
      OrbitMeanLong               355.74624607352
      OrbitMeanDistDot            -295.75529617248
      OrbitEccDot                 3.2585900068446e-009
      OrbitIncDot                 4.8386831259524e-008
      OrbitRAANDot                -7.4964814191805e-007
      OrbitPerLongDot             1.1805536708463e-005
      OrbitMeanLongDot            0.52403297064432

END     EphemerisData

END PathDescription

	BEGIN PhysicalData

		GM                   0.000000000000e+000
		Radius               0.000000000000e+000
		Magnitude            0.000000000000e+000
		ReferenceDistance    0.000000000000e+000

	END PhysicalData

	BEGIN AutoRename

		AutoRename           Yes

	END AutoRename

BEGIN Extensions
    
    BEGIN Graphics

			BEGIN Attributes

				MarkerColor             #ff0000
				LabelColor              #ff0000
				LineColor               #ff0000
				LineStyle               0
				LineWidth               1.0
				MarkerStyle             2
				FontStyle               0

			END Attributes

			BEGIN Graphics

				Inherit                  On
				ShowLabel                On
				ShowPlanetPoint          On
				ShowSubPlanetPoint       On
				ShowSubPlanetLabel       On
				ShowOrbit                Off
				NumOrbitPoints           360
				OrbitTime                5.935716275514e+007
				OrbitDisplay             OneOrbit
				TransformTrajectory      On

			END Graphics
    END Graphics
    
    BEGIN ExternData
    END ExternData
    
    BEGIN AccessConstraints
		LineOfSight   IncludeIntervals 
    END AccessConstraints
    
    BEGIN Desc
    END Desc
    
    BEGIN Crdn
    END Crdn
    
    BEGIN VO
    END VO

END Extensions

END Planet

