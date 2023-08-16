stk.v.7.0

BEGIN Star

Name        Star1

	BEGIN PathDescription

	Epoch                 2000
		RightAscension        0.000000000000e+000
		Declination           0.000000000000e+000
		ProperMotionRA        0.000000000000e+000
		ProperMotionDec       0.000000000000e+000
		Parallax              0.000000000000e+000

	END PathDescription

	BEGIN PhysicalData

		Magnitude            0.000000000000e+000

	END PhysicalData

	BEGIN IdentityData

		HarvardRevised       0
		HenryDraper          0
		SAOCatalog           0

	END IdentityData

BEGIN Extensions
    
    BEGIN Graphics

          BEGIN Attributes

                MarkerColor             #ff69b4
                MarkerStyle             2
                FontStyle               0

          END Attributes

          BEGIN Graphics

                Inherit                 On
                ShowLabel               On
                ShowMarker              On

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

END Star

