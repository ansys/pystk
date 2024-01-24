stk.v.10.0
WrittenBy    STK_v10.1.0

BEGIN	Receiver

Name	Receiver1
<?xml version = "1.0" standalone = "yes"?>
<VAR name = "STK_Receiver_Object">
    <SCOPE Class = "CommRadarObject">
        <VAR name = "Version">
            <STRING>&quot;1.0.0 a&quot;</STRING>
        </VAR>
        <VAR name = "ComponentName">
            <STRING>&quot;STK_Receiver_Object&quot;</STRING>
        </VAR>
        <VAR name = "Description">
            <STRING>&quot;STK Receiver Object&quot;</STRING>
        </VAR>
        <VAR name = "Type">
            <STRING>&quot;CAgSTKReceiverObject&quot;</STRING>
        </VAR>
        <VAR name = "UserComment">
            <STRING>&quot;STK Receiver Object&quot;</STRING>
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
            <VAR name = "Laser_Receiver_Model">
                <SCOPE Class = "Receiver">
                    <VAR name = "Version">
                        <STRING>&quot;1.0.0 a&quot;</STRING>
                    </VAR>
                    <VAR name = "ComponentName">
                        <STRING>&quot;Laser_Receiver_Model&quot;</STRING>
                    </VAR>
                    <VAR name = "Description">
                        <STRING>&quot;Laser model of a receiver&quot;</STRING>
                    </VAR>
                    <VAR name = "Type">
                        <STRING>&quot;Laser Receiver Model&quot;</STRING>
                    </VAR>
                    <VAR name = "UserComment">
                        <STRING>&quot;Laser model of a receiver&quot;</STRING>
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
                    <VAR name = "AutoSelectDemodulator">
                        <BOOL>true</BOOL>
                    </VAR>
                    <VAR name = "Demodulator">
                        <VAR name = "BPSK">
                            <SCOPE Class = "Demodulator">
                                <VAR name = "Version">
                                    <STRING>&quot;1.0.0 a&quot;</STRING>
                                </VAR>
                                <VAR name = "ComponentName">
                                    <STRING>&quot;BPSK&quot;</STRING>
                                </VAR>
                                <VAR name = "Description">
                                    <STRING>&quot;Demodulator capable of demodulating a BPSK modulated signal.&quot;</STRING>
                                </VAR>
                                <VAR name = "Type">
                                    <STRING>&quot;BPSK&quot;</STRING>
                                </VAR>
                                <VAR name = "UserComment">
                                    <STRING>&quot;Demodulator capable of demodulating a BPSK modulated signal.&quot;</STRING>
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
                            </SCOPE>
                        </VAR>
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
                    <VAR name = "Bandwidth">
                        <QUANTITY Dimension = "BandwidthUnit" Unit = "Hz">
                            <REAL>2000</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "AutoScaleBandwidth">
                        <BOOL>true</BOOL>
                    </VAR>
                    <VAR name = "PreReceiveGainsLosses">
                        <SCOPE>
                            <VAR name = "GainLossList">
                                <LIST />
                            </VAR>
                        </SCOPE>
                    </VAR>
                    <VAR name = "PreDemodGainsLosses">
                        <SCOPE>
                            <VAR name = "GainLossList">
                                <LIST />
                            </VAR>
                        </SCOPE>
                    </VAR>
                    <VAR name = "EnableLinkMargin">
                        <BOOL>false</BOOL>
                    </VAR>
                    <VAR name = "LinkMarginType">
                        <STRING>&quot;Eb/No&quot;</STRING>
                    </VAR>
                    <VAR name = "LinkMarginThreshold">
                        <QUANTITY Dimension = "RatioUnit" Unit = "units">
                            <REAL>1</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "EnablePropagationLossModel">
                        <BOOL>false</BOOL>
                    </VAR>
                    <VAR name = "PropagationLossModel">
                        <VAR name = "Beer-Bouguer-Lambert_Law">
                            <SCOPE Class = "ConcentricSpheresPropagationLossModel">
                                <VAR name = "Version">
                                    <STRING>&quot;1.0.0 a&quot;</STRING>
                                </VAR>
                                <VAR name = "ComponentName">
                                    <STRING>&quot;Beer-Bouguer-Lambert_Law&quot;</STRING>
                                </VAR>
                                <VAR name = "Description">
                                    <STRING>&quot;Model atmospheric loss for laser receivers using the Beer-Bouguer-Lambert Law&quot;</STRING>
                                </VAR>
                                <VAR name = "Type">
                                    <STRING>&quot;Beer-Bouguer-Lambert Law&quot;</STRING>
                                </VAR>
                                <VAR name = "UserComment">
                                    <STRING>&quot;Model atmospheric loss for laser receivers using the Beer-Bouguer-Lambert Law&quot;</STRING>
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
                                <VAR name = "LayerList">
                                    <LIST>
                                        <SCOPE>
                                            <VAR name = "LayerNum">
                                                <INT>1</INT>
                                            </VAR>
                                            <VAR name = "LayerTop">
                                                <QUANTITY Dimension = "DistanceUnit" Unit = "m">
                                                    <REAL>100000</REAL>
                                                </QUANTITY>
                                            </VAR>
                                            <VAR name = "ExtinctionCoefficient">
                                                <QUANTITY Dimension = "UnitlessPerSmallDistance" Unit = "m^-1">
                                                    <REAL>0</REAL>
                                                </QUANTITY>
                                            </VAR>
                                        </SCOPE>
                                    </LIST>
                                </VAR>
                                <VAR name = "EnableEvenlySpacedHeights">
                                    <BOOL>true</BOOL>
                                </VAR>
                                <VAR name = "MaxLayerHeight">
                                    <QUANTITY Dimension = "DistanceUnit" Unit = "m">
                                        <REAL>100000</REAL>
                                    </QUANTITY>
                                </VAR>
                                <VAR name = "MinLayerHeight">
                                    <QUANTITY Dimension = "DistanceUnit" Unit = "m">
                                        <REAL>0</REAL>
                                    </QUANTITY>
                                </VAR>
                            </SCOPE>
                        </VAR>
                    </VAR>
                    <VAR name = "Frequency">
                        <QUANTITY Dimension = "FrequencyUnit" Unit = "Hz">
                            <REAL>375000000000000</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "FrequencyAutoTracking">
                        <BOOL>true</BOOL>
                    </VAR>
                    <VAR name = "ComputeSystemNoiseTemp">
                        <STRING>&quot;Constant&quot;</STRING>
                    </VAR>
                    <VAR name = "ConstantSystemNoiseTemp">
                        <QUANTITY Dimension = "Temperature" Unit = "K">
                            <REAL>290</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "ANT2LNALineLoss">
                        <QUANTITY Dimension = "RatioUnit" Unit = "units">
                            <REAL>1</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "ANT2LNALineTemperature">
                        <QUANTITY Dimension = "Temperature" Unit = "K">
                            <REAL>290</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "LNA2RcvrLineLoss">
                        <QUANTITY Dimension = "RatioUnit" Unit = "units">
                            <REAL>1</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "LNA2RcvrLineTemperature">
                        <QUANTITY Dimension = "Temperature" Unit = "K">
                            <REAL>290</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "LNAGain">
                        <QUANTITY Dimension = "RatioUnit" Unit = "units">
                            <REAL>1</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "LNANoiseFigure">
                        <QUANTITY Dimension = "RatioUnit" Unit = "units">
                            <REAL>1.258925411794167</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "LNATemperature">
                        <QUANTITY Dimension = "Temperature" Unit = "K">
                            <REAL>290</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "DetectorGain">
                        <QUANTITY Dimension = "RatioUnit" Unit = "units">
                            <REAL>1000000</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "DetectorEfficiency">
                        <QUANTITY Dimension = "Percent" Unit = "unitValue">
                            <REAL>0.9</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "DetectorDarkCurrent">
                        <REAL>1e-016</REAL>
                    </VAR>
                    <VAR name = "DetectorNoiseFigure">
                        <QUANTITY Dimension = "RatioUnit" Unit = "units">
                            <REAL>0.1</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "DetectorNoiseTemperature">
                        <QUANTITY Dimension = "Temperature" Unit = "K">
                            <REAL>10</REAL>
                        </QUANTITY>
                    </VAR>
                    <VAR name = "DetectorLoadImpedance">
                        <REAL>100000000</REAL>
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
                    <VAR name = "AntennaNoiseTemperature">
                        <QUANTITY Dimension = "Temperature" Unit = "K">
                            <REAL>290</REAL>
                        </QUANTITY>
                    </VAR>
                </SCOPE>
            </VAR>
        </VAR>
    </SCOPE>
</VAR>
END	Receiver

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
