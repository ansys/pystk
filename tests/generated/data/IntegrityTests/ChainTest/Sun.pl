stk.v.6.0

BEGIN Planet

Name        Sun

BEGIN PathDescription

		CentralBody                    Sun
		UseCbEphemeris                 Yes

BEGIN               EphemerisData

	EphemerisSource             JplDE

	JplIndex                    10

	JplSpiceId                  10

	ApplyTDTtoTDBCorrectionForDE     No

END     EphemerisData

END PathDescription

	BEGIN PhysicalData

		GM                   0.000000000000e+000
		Radius               6.960000000000e+008
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
				OrbitTime                0.000000000000e+000
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

BEGIN SubObjects

END SubObjects

END Planet

