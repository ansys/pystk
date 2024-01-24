stk.v.6.0

BEGIN Transmitter

Name        FOMTest

BEGIN Model

	Type            Simple Source Transmitter
	Frequency                1.4500000000e+010
	EIRP                    3.000000e+001
	DataRate                1.600000e+007
	AutoScaleBW             1
	RFBandwidth              1.0000000000e+003
	cdmaSelect              0
	cdmaSpreadGain          0.000000e+000
	Modulation              BPSK

BEGIN Polarization

	Type                    0

	VertRefAxis             0

END Polarization
	END            Simple Source Transmitter

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
    
    BEGIN Contours

	BEGIN ContourSet Antenna Gain
		Altitude          0.000000e+000
		ShowAtAltitude    Off
		Relative          On
		ShowLabels        Off
		LineWidth         1.000000
		ColorRamp         Off
		ColorRampStartColor   #0000ff
		ColorRampEndColor     #ff0000
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

	BEGIN ContourSet EIRP
		Altitude          0.000000e+000
		ShowAtAltitude    Off
		Relative          Off
		ShowLabels        Off
		LineWidth         1.000000
		ColorRamp         Off
		ColorRampStartColor   #ffffff
		ColorRampEndColor     #4169e1
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

	BEGIN ContourSet Flux Density
		Altitude          0.000000e+000
		ShowAtAltitude    Off
		Relative          Off
		ShowLabels        Off
		LineWidth         1.000000
		ColorRamp         Off
		ColorRampStartColor   #87cefa
		ColorRampEndColor     #00ced1
		BEGIN ContourDefinition
		BEGIN CntrAntLatLon
			Resolution	9.000000  9.000000
			ElevationAngleConstraint	90.000000
			BEGIN LatLonSphGrid
				Centroid	0.000000	0.000000
				ConeAngle	0.000000
				NumPts		50	20
				Altitude	0.000000
			END LatLonSphGrid
		END CntrAntLatLon
		END ContourDefinition
	END ContourSet

	BEGIN ContourSet RIP
		Altitude          0.000000e+000
		ShowAtAltitude    Off
		Relative          Off
		ShowLabels        Off
		LineWidth         1.000000
		ColorRamp         Off
		ColorRampStartColor   #6b8e23
		ColorRampEndColor     #8fbc8f
		BEGIN ContourDefinition
		BEGIN CntrAntLatLon
			Resolution	9.000000  9.000000
			ElevationAngleConstraint	90.000000
			BEGIN LatLonSphGrid
				Centroid	0.000000	0.000000
				ConeAngle	0.000000
				NumPts		50	20
				Altitude	0.000000
			END LatLonSphGrid
		END CntrAntLatLon
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
	ShowContours    No
	ShowVolume No
End VolumeGraphics
    END 3dVolume

END Extensions

END Transmitter

