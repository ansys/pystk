stk.v.7.0

BEGIN Planet

Name        Earth

BEGIN PathDescription

		CentralBody                    Earth
		UseCbEphemeris                 Yes

BEGIN               EphemerisData

	EphemerisSource             JplDE

	JplIndex                    2

	JplSpiceId                  399

	ApplyTDTtoTDBCorrectionForDE     No

      OrbitEpoch                  2451545.0000000
      OrbitMeanDist               149597886455.77
      OrbitEcc                    0.016710220000000
      OrbitInc                    23.439340148564
      OrbitRAAN                   359.99997545459
      OrbitPerLong                462.94718797456
      OrbitMeanLong               820.46434797456
      OrbitMeanDistDot            -0.20478832306639
      OrbitEccDot                 -1.0414784394251e-009
      OrbitIncDot                 -3.5013666065859e-007
      OrbitRAANDot                1.7494840125586e-007
      OrbitPerLongDot             9.1275248887196e-006
      OrbitMeanLongDot            0.98560911497641

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

				MarkerColor             #4169e1
				LabelColor              #4169e1
				LineColor               #4169e1
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
				OrbitTime                3.153803573913e+007
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

