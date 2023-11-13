stk.v.7.0

BEGIN Planet

Name        Planet1

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

				MarkerColor             #fff0f5
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
				OrbitTime                0.000000000000e+000
				OrbitDisplay             OneOrbit
				TransformTrajectory      On

			END Graphics
    END Graphics
    
    BEGIN ExternData
    END ExternData
    
    BEGIN AccessConstraints
    END AccessConstraints
    
    BEGIN Desc
    END Desc
    
    BEGIN Crdn
    END Crdn
    
    BEGIN VO
    END VO

END Extensions

END Planet

