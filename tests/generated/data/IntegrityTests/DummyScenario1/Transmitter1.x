stk.v.10.0
WrittenBy    STK_v10.1.0

BEGIN	Transmitter

Name	Transmitter1
<?xml version = "1.0" standalone = "yes"?>
<VAR name = "STK_Transmitter_Object">
    <SCOPE Class = "CommRadarObject">
        <VAR name = "Version">
            <STRING>&quot;1.0.0 a&quot;</STRING>
        </VAR>
        <VAR name = "ComponentName">
            <STRING>&quot;STK_Transmitter_Object&quot;</STRING>
        </VAR>
        <VAR name = "Description">
            <STRING>&quot;STK Transmitter Object&quot;</STRING>
        </VAR>
        <VAR name = "Type">
            <STRING>&quot;CAgSTKTransmitterObject&quot;</STRING>
        </VAR>
        <VAR name = "UserComment">
            <STRING>&quot;STK Transmitter Object&quot;</STRING>
        </VAR>
        <VAR name = "ReadOnly">
            <BOOL>false</BOOL>
        </VAR>
        <VAR name = "Clonable">
            <BOOL>true</BOOL>
        </VAR>
        <VAR name = "Category">
            <STRING>&quot;&quot;</STRING>
        </VAR>
        <VAR name = "Model">
            <VAR name = "Laser_Transmitter_Model">
                <SCOPE Class = "Transmitter">
                    <VAR name = "Version">
                        <STRING>&quot;1.0.1 a&quot;</STRING>
                    </VAR>
                    <VAR name = "ComponentName">
                        <STRING>&quot;Laser_Transmitter_Model&quot;</STRING>
                    </VAR>
                    <VAR name = "Description">
                        <STRING>&quot;Laser model of a transmitter&quot;</STRING>
                    </VAR>
                    <VAR name = "Type">
                        <STRING>&quot;Laser Transmitter Model&quot;</STRING>
                    </VAR>
                    <VAR name = "UserComment">
                        <STRING>&quot;Laser model of a transmitter&quot;</STRING>
                    </VAR>
                    <VAR name = "ReadOnly">
                        <BOOL>false</BOOL>
                    </VAR>
                    <VAR name = "Clonable">
                        <BOOL>true</BOOL>
                    </VAR>
                    <VAR name = "Category">
                        <STRING>&quot;@Top&quot;</STRING>
                    </VAR>
                    <VAR name = "UseFilter">
                        <BOOL>false</BOOL>
                    </VAR>
                    <VAR name = "Filter">
                        <VAR name = "Butterworth">
                            <SCOPE Class = "Filter">
                                <VAR name = "Version">
                                    <STRING>&quot;1.0.0 a&quot;</STRING>
                                </VAR>
                                <VAR name = "ComponentName">
                                    <STRING>&quot;Butterworth&quot;</STRING>
                                </VAR>
                                <VAR name = "Description">
                                    <STRING>&quot;General form of nth order Butterworth filter with flat passband and stopband regions&quot;</STRING>
                                </VAR>
                                <VAR name = "Type">
                                    <STRING>&quot;Butterworth&quot;</STRING>
                                </VAR>
                                <VAR name = "UserComment">
                                    <STRING>&quot;General form of nth order Butterworth filter with flat passband and stopband regions&quot;</STRING>
                                </VAR>
                                <VAR name = "ReadOnly">
                                    <BOOL>false</BOOL>
                                </VAR>
                                <VAR name = "Clonable">
                                    <BOOL>true</BOOL>
                                </VAR>
                                <VAR name = "Category">
                                    <STRING>&quot;&quot;</STRING>
                                </VAR>
                                <VAR name = "LowerBandwidthLimit">
                                    <QUANTITY Dimension = "BandwidthUnit" Unit = "Hz">
                                        <REAL>-20000000</REAL>
                                    </QUANTITY>
                                </VAR>
                                <VAR name = "UpperBandwidthLimit">
                                    <QUANTITY Dimension = "BandwidthUnit" Unit = "Hz">
                                        <REAL>20000000</REAL>
                                    </QUANTITY>
                                </VAR>
                                <VAR name = "InsertionLoss">
                                    <QUANTITY Dimension = "RatioUnit" Unit = "units">
                                        <REAL>1</REAL>
                                    </QUANTITY>
                                </VAR>
                                <VAR name = "Order">
                                    <INT>4</INT>
                                </VAR>
                                <VAR name = "CutoffFrequency">
                                    <QUANTITY Dimension = "BandwidthUnit" Unit = "Hz">
                                        <REAL>10000000</REAL>
                                    </QUANTITY>
                                </VAR>
                            </SCOPE>
                        </VAR>
                    </VAR>
                    <VAR name = "PostTransmitGainsLosses">
                        <SCOPE>
                            <VAR name = "GainLossList">
                                <LIST />
                            </VAR>
                        </SCOPE>
                    </VAR>
                    <VAR name = "DataRate">
                        <QUANTITY Dimension = "DataRate" Unit = "b*sec^-1">
                            <REAL>16000000</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "Frequency">
                        <QUANTITY Dimension = "FrequencyUnit" Unit = "Hz">
                            <REAL>375000000000000</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "Modulator">
                        <VAR name = "BPSK">
                            <SCOPE Class = "Modulator">
                                <VAR name = "Version">
                                    <STRING>&quot;1.0.1 a&quot;</STRING>
                                </VAR>
                                <VAR name = "ComponentName">
                                    <STRING>&quot;BPSK&quot;</STRING>
                                </VAR>
                                <VAR name = "Description">
                                    <STRING>&quot;Modulator capable of modulating a signal using BPSK modulation&quot;</STRING>
                                </VAR>
                                <VAR name = "Type">
                                    <STRING>&quot;BPSK&quot;</STRING>
                                </VAR>
                                <VAR name = "UserComment">
                                    <STRING>&quot;Modulator capable of modulating a signal using BPSK modulation&quot;</STRING>
                                </VAR>
                                <VAR name = "ReadOnly">
                                    <BOOL>false</BOOL>
                                </VAR>
                                <VAR name = "Clonable">
                                    <BOOL>true</BOOL>
                                </VAR>
                                <VAR name = "Category">
                                    <STRING>&quot;&quot;</STRING>
                                </VAR>
                                <VAR name = "UseSignalPSD">
                                    <BOOL>false</BOOL>
                                </VAR>
                                <VAR name = "NumPSDNulls">
                                    <INT>15</INT>
                                </VAR>
                                <VAR name = "UseCDMASpread">
                                    <BOOL>false</BOOL>
                                </VAR>
                                <VAR name = "ChipsPerBit">
                                    <INT>1</INT>
                                </VAR>
                                <VAR name = "AutoScaleBandwidth">
                                    <BOOL>true</BOOL>
                                </VAR>
                                <VAR name = "SymmetricBandwidth">
                                    <BOOL>true</BOOL>
                                </VAR>
                                <VAR name = "UpperBandwidthLimit">
                                    <QUANTITY Dimension = "BandwidthUnit" Unit = "Hz">
                                        <REAL>16000000</REAL>
                                    </QUANTITY>
                                </VAR>
                                <VAR name = "LowerBandwidthLimit">
                                    <QUANTITY Dimension = "BandwidthUnit" Unit = "Hz">
                                        <REAL>-16000000</REAL>
                                    </QUANTITY>
                                </VAR>
                                <VAR name = "Bandwidth">
                                    <QUANTITY Dimension = "BandwidthUnit" Unit = "Hz">
                                        <REAL>32000000</REAL>
                                    </QUANTITY>
                                </VAR>
                            </SCOPE>
                        </VAR>
                    </VAR>
                    <VAR name = "Power">
                        <QUANTITY Dimension = "PowerUnit" Unit = "W">
                            <REAL>1</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "AntennaControl">
                        <SCOPE>
                            <VAR name = "AntennaReferenceType">
                                <STRING>&quot;Embed&quot;</STRING>
                            </VAR>
                            <VAR name = "Antenna">
                                <VAR name = "Gaussian_Optical">
                                    <SCOPE Class = "Antenna">
                                        <VAR name = "Version">
                                            <STRING>&quot;1.0.0 a&quot;</STRING>
                                        </VAR>
                                        <VAR name = "ComponentName">
                                            <STRING>&quot;Gaussian_Optical&quot;</STRING>
                                        </VAR>
                                        <VAR name = "Description">
                                            <STRING>&quot;Gaussian optical antenna pattern&quot;</STRING>
                                        </VAR>
                                        <VAR name = "Type">
                                            <STRING>&quot;Gaussian Optical&quot;</STRING>
                                        </VAR>
                                        <VAR name = "UserComment">
                                            <STRING>&quot;Gaussian optical antenna pattern&quot;</STRING>
                                        </VAR>
                                        <VAR name = "ReadOnly">
                                            <BOOL>false</BOOL>
                                        </VAR>
                                        <VAR name = "Clonable">
                                            <BOOL>true</BOOL>
                                        </VAR>
                                        <VAR name = "Category">
                                            <STRING>&quot;&quot;</STRING>
                                        </VAR>
                                        <VAR name = "DesignFrequency">
                                            <QUANTITY Dimension = "FrequencyUnit" Unit = "Hz">
                                                <REAL>375000000000000</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "ComputeGain">
                                            <BOOL>false</BOOL>
                                        </VAR>
                                        <VAR name = "MaxGain">
                                            <QUANTITY Dimension = "RatioUnit" Unit = "units">
                                                <REAL>1000000</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "Area">
                                            <QUANTITY Dimension = "Small Area" Unit = "m^2">
                                                <REAL>0.1</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "Efficiency">
                                            <QUANTITY Dimension = "Percent" Unit = "unitValue">
                                                <REAL>0.7</REAL>
                                            </QUANTITY>
                                        </VAR>
                                    </SCOPE>
                                </VAR>
                            </VAR>
                            <VAR name = "UsePolarization">
                                <BOOL>false</BOOL>
                            </VAR>
                            <VAR name = "Polarization">
                                <VAR name = "Linear">
                                    <SCOPE Class = "Polarization">
                                        <VAR name = "ReferenceAxis">
                                            <STRING>&quot;X Axis&quot;</STRING>
                                        </VAR>
                                        <VAR name = "TiltAngle">
                                            <QUANTITY Dimension = "AngleUnit" Unit = "rad">
                                                <REAL>0</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "CrossPolLeakage">
                                            <QUANTITY Dimension = "RatioUnit" Unit = "units">
                                                <REAL>1e-006</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "Type">
                                            <STRING>&quot;Linear&quot;</STRING>
                                        </VAR>
                                    </SCOPE>
                                </VAR>
                            </VAR>
                            <VAR name = "Orientation">
                                <VAR name = "Azimuth Elevation">
                                    <SCOPE Class = "Orientation">
                                        <VAR name = "AzimuthAngle">
                                            <QUANTITY Dimension = "AngleUnit" Unit = "rad">
                                                <REAL>0</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "ElevationAngle">
                                            <QUANTITY Dimension = "AngleUnit" Unit = "rad">
                                                <REAL>1.570796326794897</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "AboutBoresight">
                                            <STRING>&quot;Rotate&quot;</STRING>
                                        </VAR>
                                        <VAR name = "Type">
                                            <STRING>&quot;Azimuth Elevation&quot;</STRING>
                                        </VAR>
                                        <VAR name = "XPositionOffset">
                                            <QUANTITY Dimension = "SmallDistanceUnit" Unit = "m">
                                                <REAL>0</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "YPositionOffset">
                                            <QUANTITY Dimension = "SmallDistanceUnit" Unit = "m">
                                                <REAL>0</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "ZPositionOffset">
                                            <QUANTITY Dimension = "SmallDistanceUnit" Unit = "m">
                                                <REAL>0</REAL>
                                            </QUANTITY>
                                        </VAR>
                                    </SCOPE>
                                </VAR>
                            </VAR>
                        </SCOPE>
                    </VAR>
                </SCOPE>
            </VAR>
        </VAR>
    </SCOPE>
</VAR>
END	Transmitter

BEGIN Extensions
    
    BEGIN Graphics

BEGIN Graphics

	ShowGfx           On
	Relative          Off
	ShowBoresight     On
	BoresightMarker   4
	BoresightColor    #ffffff

END Graphics
    END Graphics
    
    BEGIN ContourGfx
	ShowContours      Off
    END ContourGfx
    
    BEGIN ExternData
    END ExternData
    
    BEGIN ADFFileData
    END ADFFileData
    
    BEGIN AccessConstraints
		LineOfSight   IncludeIntervals 
    END AccessConstraints
    
    BEGIN ObjectCoverage
    END ObjectCoverage
    
    BEGIN Desc
    END Desc
    
    BEGIN Refraction
		RefractionModel	Effective Radius Method

		UseRefractionInAccess		No

		BEGIN ModelData
			RefractionCeiling	5.00000000000000e+003
			MaxTargetAltitude	1.00000000000000e+004
			EffectiveRadius		1.33333333333333e+000

			UseExtrapolation	 Yes


		END ModelData
    END Refraction
    
    BEGIN Contours
	ActiveContourType Antenna Gain

	BEGIN ContourSet Antenna Gain
		Altitude          0.000000e+000
		ShowAtAltitude    Off
		Projected         On
		Relative          On
		ShowLabels        Off
		LineWidth         1.000000
		DecimalDigits     1
		ColorRamp         On
		ColorRampStartColor   #0000ff
		ColorRampEndColor     #ff0000
		BEGIN ContourDefinition
		BEGIN CntrAntAzEl
			BEGIN AzElPattern
				BEGIN AzElPatternDef
					SetResolutionTogether 0
					CoordinateSystem 0
					NumAzPoints      50
					AzimuthRes       7.346939
					MinAzimuth       -180.000000
					MaxAzimuth       180.000000
					NumElPoints      50
					ElevationRes     1.836735
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
		Projected         On
		Relative          On
		ShowLabels        Off
		LineWidth         1.000000
		DecimalDigits     1
		ColorRamp         On
		ColorRampStartColor   #0000ff
		ColorRampEndColor     #ff0000
		BEGIN ContourDefinition
		BEGIN CntrAntAzEl
			BEGIN AzElPattern
				BEGIN AzElPatternDef
					SetResolutionTogether 0
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
		Projected         On
		Relative          On
		ShowLabels        Off
		LineWidth         1.000000
		DecimalDigits     1
		ColorRamp         On
		ColorRampStartColor   #0000ff
		ColorRampEndColor     #ff0000
		BEGIN ContourDefinition
		BEGIN CntrAntLatLon
			SetResolutionTogether   true
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
		Projected         On
		Relative          On
		ShowLabels        Off
		LineWidth         1.000000
		DecimalDigits     1
		ColorRamp         On
		ColorRampStartColor   #0000ff
		ColorRampEndColor     #ff0000
		BEGIN ContourDefinition
		BEGIN CntrAntLatLon
			SetResolutionTogether   true
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
	NumericGainOffset 1.000000
	Frequency 14500000000.000000
	ShowAsWireframe 0
				BEGIN AzElPatternDef
					SetResolutionTogether 0
					CoordinateSystem 0
					NumAzPoints      50
					AzimuthRes       7.346939
					MinAzimuth       -180.000000
					MaxAzimuth       180.000000
					NumElPoints      50
					ElevationRes     1.836735
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
