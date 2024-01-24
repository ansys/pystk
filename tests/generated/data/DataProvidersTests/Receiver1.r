stk.v.6.1

BEGIN Receiver

Name        Receiver1

BEGIN Model

	Type            Simple Receiver
	G/T                     20.000000
	AutoTrackFreq           On
	Frequency               14500000000.000000
	Autoscale               On
	Bandwidth               2000.000000

BEGIN Polarization

	Type                    0

	VertRefAxis             0

END Polarization

	BEGIN RfRain

		RainModel               Off

	END RfRain
	END            Simple Receiver

END Model

BEGIN Extensions
    
    BEGIN Graphics
	Relative          Off
	ShowBoresight     On
	BoresightMarker   4
	BoresightColor    #ffffff
    END Graphics
    
    BEGIN ContourGfx
	ShowContours      On
    END ContourGfx
    
    BEGIN ExternData
    END ExternData
    
    BEGIN AccessConstraints
		LineOfSight   IncludeIntervals 
    END AccessConstraints
    
    BEGIN ObjectCoverage
    END ObjectCoverage
    
    BEGIN Desc
    END Desc
    
    BEGIN Refraction
		RefractionModel	4/3 Earth Radius Method
    END Refraction
    
    BEGIN Contours

	BEGIN ContourSet Antenna Gain
		Altitude          0.000000e+000
		ShowAtAltitude    Off
		Relative          On
		ShowLabels        Off
		LineWidth         1.000000
		ColorRamp         On
		ColorRampStartColor   #ff0000
		ColorRampEndColor     #0000ff
		BEGIN ContourDefinition
		BEGIN CntrAntAzEl
			Frequency 14500000000.000000
			BEGIN AzElPattern
				BEGIN AzElPatternDef
					CoordinateSystem 0
					NumAzPoints      50
					AzimuthRes       0.000000
					MinAzimuth       -180.000000
					MaxAzimuth       180.000000
					NumElPoints      50
					ElevationRes     0.000000
					MinElevation     0.000000
					MaxElevation     90.000000
				END AzElPatternDef
			END AzElPattern
		END CntrAntAzEl
		END ContourDefinition
	END ContourSet
    END Contours
    
    BEGIN Crdn
    END Crdn
    
    BEGIN VO
    END VO
    
    BEGIN 3dVolume

	BEGIN VolumeSet Antenna Beam
	Scale 200000.000000
	Frequency 14500000000.000000
	ShowAsWireframe 0
				BEGIN AzElPatternDef
					CoordinateSystem 0
					NumAzPoints      50
					AzimuthRes       0.000000
					MinAzimuth       -180.000000
					MaxAzimuth       180.000000
					NumElPoints      50
					ElevationRes     0.000000
					MinElevation     0.000000
					MaxElevation     90.000000
				END AzElPatternDef
	END VolumeSet
Begin VolumeGraphics
	ShowContours    Yes
	ShowVolume No
End VolumeGraphics
    END 3dVolume

END Extensions

END Receiver

