stk.v.7.0

BEGIN Planet

Name        JupiterAnalytic

BEGIN PathDescription

		CentralBody                    Jupiter
		UseCbEphemeris                 No

BEGIN               EphemerisData

	EphemerisSource             Analytic

	JplIndex                    4

	JplSpiceId                  10

	ApplyTDTtoTDBCorrectionForDE     No

      OrbitEpoch                  2451545.0000000
      OrbitMeanDist               778412023132.79
      OrbitEcc                    0.048392660000000
      OrbitInc                    23.233623374326
      OrbitRAAN                   3.2543705406445
      OrbitPerLong                15.019944513791
      OrbitMeanLong               34.670474513792
      OrbitMeanDistDot            2487.6456756167
      OrbitEccDot                 -3.5263518138261e-009
      OrbitIncDot                 -2.0487362090228e-007
      OrbitRAANDot                -1.4970986778464e-007
      OrbitPerLongDot             6.3732432049364e-006
      OrbitMeanLongDot            0.083086747568249

END     EphemerisData

END PathDescription

	BEGIN PhysicalData

		GM                   0.000000000000e+000
		Radius               7.139800000000e+007
		Magnitude            0.000000000000e+000
		ReferenceDistance    0.000000000000e+000

	END PhysicalData

	BEGIN AutoRename

		AutoRename           Yes

	END AutoRename

BEGIN Extensions
    
    BEGIN Graphics

			BEGIN Attributes

				MarkerColor             #ff00ff
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
				OrbitTime                3.745746331842e+008
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

