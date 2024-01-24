stk.v.6.0

BEGIN Radar

Name        CovDefTest

	BEGIN System


BEGIN RadarAntenna

	Type                    PencilBeam

	BEGIN Boresight

		RotationType		0
		qx		0.000000e+000
		qy		7.071068e-001
		qz		0.000000e+000
		qs		7.071068e-001
		RelOffsetX		0.000000e+000
		RelOffsetY		0.000000e+000
		RelOffsetZ		0.000000e+000

	END Boresight

	BEGIN PencilBeam

		MainLobeGain        4.000000e+001
		SideLobeGain        -3.000000e+000
	END PencilBeam

END RadarAntenna


		Monostatic		Yes
		PeakPower		4.000000e+001
		Wavelength		1.000000e-001
		FreqMode		0

	END System

	BEGIN SearchTrack

		Enabled		Yes
		Mode		0
		SubMode		0
		PRF		1.000000e+003
		UnambigRng		1.498962e+005
		UnambigVel		2.500000e+001
		PulseWidthMode		0
		PulseWidth		1.000000e-007
		DutyFactor		1.000000e-004
		MLCFilter		No
		MLCFilterBW		0.000000e+000
		SLCFilter		No
		SLCFilterBW		0.000000e+000
		IntGainMode		0
		IntGainGoalVal		1.600000e+001 1 1.000000e+000 512
		IntGainFlag		0
		IntGainVal		1.000000e+000
		IntGainExp		1.000000e+000
		Pfa		1.000000e-006
		IsCFAR		No
		RefCells		6

	END SearchTrack

	BEGIN SAR

		Enabled		No
		SARMode		0
		IntegrationTime		1.000000e+000
		AzimuthResolution		1.000000e+001
		PRFMode		0
		PRF		1.000000e+003
		UnambigRng		1.498962e+005
		AzBroadFactor		1.200000e+000
		RngBroadFactor		1.200000e+000
		IFBandwidth		1.000000e+008
		RangeResMode		0
		RangeResolution		1.000000e+001
		Bandwidth		1.798755e+007
		PCRMode		0
		PulseCompRatio		1.000000e+003
		Pulsewidth		5.559402e-005
		SceneDepth		4.632835e+004
		RangeChirp		3.235519e+011
		MultNoiseRatio		-2.000000e+001

	END SAR

	BEGIN SystemTemperature

		ConstantTemp      290.000000
		NoiseFigure       1.000000
		WaveguideTemp     290.000000
		WaveguideLoss     0.000000
		ConstantAntTemp     0.000000

	END SystemTemperature

	BEGIN RfRain

		RainModel               Off

	END RfRain

BEGIN Extensions
    
    BEGIN Graphics

	BEGIN Graphics

		ShowRdr		Yes
		ShowXmtTgt		Yes
		ShowXmtRdr		Yes
		ShowContour		Yes
		UseSinglePulse		Yes
		SNR		1.300000e+001
		LineWidth		1.000000e+000
		LineColor		#9b30ff
		LineStyle		1
		XmtTgtWidth		1.000000e+000
		XmtTgtColor		#9b30ff
		XmtTgtStyle		2
		XmtRdrWidth		1.000000e+000
		XmtRdrColor		#9b30ff
		XmtRdrStyle		2
		ShowRdrTgtGrp		No
		RdrTgtGrpMarker		0
		RdrTgtGrpColor		#000000
		ShowXmtTgtGrp		No
		XmtTgtGrpMarker		0
		XmtTgtGrpColor		#000000
		ShowXmtRdrGrp		No
		XmtRdrGrpMarker		0
		XmtRdrGrpColor		#000000

	BEGIN Antenna

	Relative          Off
	ShowBoresight     On
	BoresightMarker   4
	BoresightColor    #ffffff

	END Antenna


	END Graphics
    END Graphics
    
    BEGIN ContourGfx
	ShowContours      On
    END ContourGfx
    
    BEGIN ExternData
    END ExternData
    
    BEGIN AccessConstraints
		LineOfSight   IncludeIntervals 
		RadarAccess   IncludeIntervals 
		RdrXmtTgtAccess   IncludeIntervals 
    END AccessConstraints
    
    BEGIN ObjectCoverage
    END ObjectCoverage
    
    BEGIN Desc
    END Desc
    
    BEGIN Refraction
		RefractionModel	4/3 Earth Radius Method
    END Refraction
    
    BEGIN Contours
	ActiveContourType Antenna Gain

	BEGIN ContourSet Antenna Gain
		Altitude          0.000000e+000
		ShowAtAltitude    Off
		Relative          Off
		ShowLabels        Off
		LineWidth         1.000000
		ColorRamp         Off
		ColorRampStartColor   #7fff00
		ColorRampEndColor     #ff6a6a
		BEGIN ContourDefinition
		BEGIN CntrAntAzEl
			Frequency 2997925000.000000
			BEGIN AzElPattern
				BEGIN AzElPatternDef
					CoordinateSystem 0
					NumAzPoints      50
					AzimuthRes       0.000000
					MinAzimuth       -180.000000
					MaxAzimuth       180.000000
					NumElPoints      30
					ElevationRes     0.000000
					MinElevation     0.000000
					MaxElevation     10.000000
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
		ColorRampStartColor   #9b30ff
		ColorRampEndColor     #ffa500
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
					NumElPoints      30
					ElevationRes     0.000000
					MinElevation     0.000000
					MaxElevation     10.000000
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
		ColorRampStartColor   #f08080
		ColorRampEndColor     #f0ffff
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
		ColorRampStartColor   #4d4d4d
		ColorRampEndColor     #00ff00
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
	ActiveVolumeType  Antenna Beam

	BEGIN VolumeSet Antenna Beam
	Scale 200000.000000
	Frequency 2997924580.000000
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

END Radar

