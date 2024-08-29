stk.v.12.0
WrittenBy    STK_v12.9.0
BEGIN Scenario
    Name		 ChainTests

    BEGIN Epoch

        Epoch		 1 Jul 1999 00:00:00.000000000
        SmartEpoch		
        BEGIN EVENT
            Epoch		 1 Jul 1999 00:00:00.000000000
            EpochState		 Explicit
        END EVENT


    END Epoch

    BEGIN Interval

        Start		 1 Jul 1999 00:00:00.000000000
        Stop		 2 Jul 1999 00:00:00.000000000
        SmartInterval		
        BEGIN EVENTINTERVAL
            BEGIN Interval
                Start		 1 Jul 1999 00:00:00.000000000
                Stop		 2 Jul 1999 00:00:00.000000000
            END Interval
            IntervalState		 Explicit
        END EVENTINTERVAL

        EpochUsesAnalStart		 No
        AnimStartUsesAnalStart		 Yes
        AnimStopUsesAnalStop		 No

    END Interval

    BEGIN EOPFile

        InheritEOPSource		 No
        EOPFilename		 EOP-v1.1.txt

    END EOPFile

    BEGIN GlobalPrefs
        SatelliteNoOrbWarning		 No
        MissilePerigeeWarning		 No
        MissileStopTimeWarning		 No
        AircraftWGS84Warning		 Always
    END GlobalPrefs

    BEGIN CentralBody

        PrimaryBody		 Earth

    END CentralBody

    BEGIN CentralBodyTerrain

        BEGIN CentralBody
            Name		 Earth
            UseTerrainCache		 Yes
            TotalCacheSize		 402653184

            BEGIN StreamingTerrain
                UseCurrentStreamingTerrainServer		 No
                CurrentStreamingTerrainServerName		 https://gcs.agi.com/
                StreamingTerrainServerName		 assets.agi.com/stk-terrain/
                StreamingTerrainAzimuthElevationMaskEnabled		 Yes
                StreamingTerrainObscurationEnabled		 Yes
                StreamingTerrainCoverageGridObscurationEnabled		 No
            END StreamingTerrain
        END CentralBody

    END CentralBodyTerrain

    BEGIN StarCollection

        Name		 Hipparcos 2 Mag 8

    END StarCollection

    BEGIN ScenarioLicenses
        Module		 stk_mission_air
        Module		 stk_mission_level1
        Module		 stk_mission_level2
        Module		 stk_mission_level3
        Module		 stk_mission_space
        Module		 stk_rfchannel_ent
        Module		 stk_snopt
    END ScenarioLicenses

    BEGIN Extensions

        BEGIN ClsApp
            RangeConstraint		 5000
            ApoPeriPad		 30000
            OrbitPathPad		 100000
            TimeDistPad		 30000
            OutOfDate		 2592000
            MaxApoPeriStep		 900
            ApoPeriAngle		 0.7853981633974483
            UseApogeePerigeeFilter		 Yes
            UsePathFilter		 No
            UseTimeFilter		 No
            UseOutOfDate		 Yes
            CreateSats		 No
            MaxSatsToCreate		 500
            UseModelScale		 No
            ModelScale		 0
            UseCrossRefDb		 Yes
            CollisionDB		 stkAllTLE.tce
            CollisionCrossRefDB		 stkAllTLE.sd
            ShowLine		 Yes
            AnimHighlight		 Yes
            StaticHighlight		 Yes
            UseLaunchWindow		 No
            LaunchWindowUseEntireTraj		 Yes
            LaunchWindowTrajMETStart		 0
            LaunchWindowTrajMETStop		 900
            LaunchWindowStart		 0
            LaunchWindowStop		 86400
            LaunchMETOffset		 0
            LaunchWindowUseSecEphem		 No 
            LaunchWindowUseScenFolderForSecEphem		 Yes
            LaunchWindowUsePrimEphem		 No 
            LaunchWindowUseScenFolderForPrimEphem		 Yes
            LaunchWindowIntervalPtr		
            BEGIN EVENTINTERVAL
                BEGIN Interval
                    Start		 1 Jul 1999 00:00:00.000000000
                    Stop		 2 Jul 1999 00:00:00.000000000
                END Interval
                IntervalState		 Explicit
            END EVENTINTERVAL

            LaunchWindowUsePrimMTO		 No 
            GroupLaunches		 No 
            LWTimeConvergence		 0.001
            LWRelValueConvergence		 1e-08
            LWTSRTimeConvergence		 0.0001
            LWTSRRelValueConvergence		 1e-10
            LaunchWindowStep		 300
            MaxTSRStep		  1.8000000000000000e+02
            MaxTSRRelMotion		  2.0000000000000000e+01
            UseLaunchArea		 No 
            LaunchAreaOrientation		 North
            LaunchAreaAzimuth		 0
            LaunchAreaXLimits		 -10000 10000
            LaunchAreaYLimits		 -10000 10000
            LaunchAreaNumXIntrPnts		 1
            LaunchAreaNumYIntrPnts		 1
            LaunchAreaAltReference		 Ellipsoid
            TargetSameStop		 No 
            SkipSurfaceMetric		 No 
            LWAreaTSRRelValueConvergence		 1e-10
            AreaLaunchWindowStep		 300
            AreaMaxTSRStep		  3.0000000000000000e+01
            AreaMaxTSRRelMotion		 1
            ShowLaunchArea		 No 
            ShowBlackoutTracks		 No 
            ShowClearedTracks		 No 
            UseObjectForClearedColor		 No 
            BlackoutColor		 #ff0000
            ClearedColor		 #ffffff
            ShowTracksSegments		 No 
            ShowMinRangeTracks		 No 
            MinRangeTrackTimeStep		 0.5
            UsePrimStepForTracks		 Yes
            GfxTracksTimeStep		 30
            GfxAreaNumXIntrPnts		 1
            GfxAreaNumYIntrPnts		 1
            CreateLaunchMTO		 No 
            CovarianceSigmaScale		 3
            CovarianceMode		 None 
        END ClsApp

        BEGIN Units
            DistanceUnit		 Kilometers
            TimeUnit		 Seconds
            DateFormat		 GregorianUTC
            AngleUnit		 Degrees
            MassUnit		 Kilograms
            PowerUnit		 dBW
            FrequencyUnit		 Gigahertz
            SmallDistanceUnit		 Meters
            LatitudeUnit		 Degrees
            LongitudeUnit		 Degrees
            DurationUnit		 Hr:Min:Sec
            Temperature		 Kelvin
            SmallTimeUnit		 Seconds
            RatioUnit		 Decibel
            RcsUnit		 Decibel
            DopplerVelocityUnit		 MetersperSecond
            SARTimeResProdUnit		 Meter-Second
            ForceUnit		 Newtons
            PressureUnit		 Pascals
            SpecificImpulseUnit		 Seconds
            PRFUnit		 Kilohertz
            BandwidthUnit		 Megahertz
            SmallVelocityUnit		 CentimetersperSecond
            Percent		 Percentage
            AviatorDistanceUnit		 NauticalMiles
            AviatorTimeUnit		 Hours
            AviatorAltitudeUnit		 Feet
            AviatorFuelQuantityUnit		 Pounds
            AviatorRunwayLengthUnit		 Kilofeet
            AviatorBearingAngleUnit		 Degrees
            AviatorAngleOfAttackUnit		 Degrees
            AviatorAttitudeAngleUnit		 Degrees
            AviatorGUnit		 StandardSeaLevelG
            SolidAngle		 Steradians
            AviatorTSFCUnit		 TSFCLbmHrLbf
            AviatorPSFCUnit		 PSFCLbmHrHp
            AviatorForceUnit		 Pounds
            AviatorPowerUnit		 Horsepower
            MicroDistanceUnit		 Microns
            SpectralBandwidthUnit		 Hertz
            AviatorAltTimeUnit		 Minutes
            AviatorSmallTimeUnit		 Seconds
            AviatorEnergyUnit		 kilowatt-hours
            BitsUnit		 MegaBits
            PowerLinearUnit		 Watts
            RatioLinearUnit		 Units
            RcsLinearUnit		 SquareMeters
            MagneticFieldUnit		 nanoTesla
            VoltageUnit		 Volts
        END Units

        BEGIN ReportUnits
            DistanceUnit		 Kilometers
            TimeUnit		 Seconds
            DateFormat		 GregorianUTC
            AngleUnit		 Degrees
            MassUnit		 Kilograms
            PowerUnit		 dBW
            FrequencyUnit		 Gigahertz
            SmallDistanceUnit		 Meters
            LatitudeUnit		 Degrees
            LongitudeUnit		 Degrees
            DurationUnit		 Hr:Min:Sec
            Temperature		 Kelvin
            SmallTimeUnit		 Seconds
            RatioUnit		 Decibel
            RcsUnit		 Decibel
            DopplerVelocityUnit		 MetersperSecond
            SARTimeResProdUnit		 Meter-Second
            ForceUnit		 Newtons
            PressureUnit		 Pascals
            SpecificImpulseUnit		 Seconds
            PRFUnit		 Kilohertz
            BandwidthUnit		 Megahertz
            SmallVelocityUnit		 CentimetersperSecond
            Percent		 Percentage
            AviatorDistanceUnit		 NauticalMiles
            AviatorTimeUnit		 Hours
            AviatorAltitudeUnit		 Feet
            AviatorFuelQuantityUnit		 Pounds
            AviatorRunwayLengthUnit		 Kilofeet
            AviatorBearingAngleUnit		 Degrees
            AviatorAngleOfAttackUnit		 Degrees
            AviatorAttitudeAngleUnit		 Degrees
            AviatorGUnit		 StandardSeaLevelG
            SolidAngle		 Steradians
            AviatorTSFCUnit		 TSFCLbmHrLbf
            AviatorPSFCUnit		 PSFCLbmHrHp
            AviatorForceUnit		 Pounds
            AviatorPowerUnit		 Horsepower
            MicroDistanceUnit		 Microns
            SpectralBandwidthUnit		 Hertz
            AviatorAltTimeUnit		 Minutes
            AviatorSmallTimeUnit		 Seconds
            AviatorEnergyUnit		 kilowatt-hours
            BitsUnit		 MegaBits
            PowerLinearUnit		 Watts
            RatioLinearUnit		 Units
            RcsLinearUnit		 SquareMeters
            MagneticFieldUnit		 nanoTesla
            VoltageUnit		 Volts
        END ReportUnits

        BEGIN ConnectReportUnits
            DistanceUnit		 Kilometers
            TimeUnit		 Seconds
            DateFormat		 GregorianUTC
            AngleUnit		 Degrees
            MassUnit		 Kilograms
            PowerUnit		 dBW
            FrequencyUnit		 Gigahertz
            SmallDistanceUnit		 Meters
            LatitudeUnit		 Degrees
            LongitudeUnit		 Degrees
            DurationUnit		 Hr:Min:Sec
            Temperature		 Kelvin
            SmallTimeUnit		 Seconds
            RatioUnit		 Decibel
            RcsUnit		 Decibel
            DopplerVelocityUnit		 MetersperSecond
            SARTimeResProdUnit		 Meter-Second
            ForceUnit		 Newtons
            PressureUnit		 Pascals
            SpecificImpulseUnit		 Seconds
            PRFUnit		 Kilohertz
            BandwidthUnit		 Megahertz
            SmallVelocityUnit		 CentimetersperSecond
            Percent		 Percentage
            AviatorDistanceUnit		 NauticalMiles
            AviatorTimeUnit		 Hours
            AviatorAltitudeUnit		 Feet
            AviatorFuelQuantityUnit		 Pounds
            AviatorRunwayLengthUnit		 Kilofeet
            AviatorBearingAngleUnit		 Degrees
            AviatorAngleOfAttackUnit		 Degrees
            AviatorAttitudeAngleUnit		 Degrees
            AviatorGUnit		 StandardSeaLevelG
            SolidAngle		 Steradians
            AviatorTSFCUnit		 TSFCLbmHrLbf
            AviatorPSFCUnit		 PSFCLbmHrHp
            AviatorForceUnit		 Pounds
            AviatorPowerUnit		 Horsepower
            MicroDistanceUnit		 Microns
            SpectralBandwidthUnit		 Hertz
            AviatorAltTimeUnit		 Minutes
            AviatorSmallTimeUnit		 Seconds
            AviatorEnergyUnit		 kilowatt-hours
            BitsUnit		 MegaBits
            PowerLinearUnit		 Watts
            RatioLinearUnit		 Units
            RcsLinearUnit		 SquareMeters
            MagneticFieldUnit		 nanoTesla
            VoltageUnit		 Volts
        END ConnectReportUnits

        BEGIN ReportFavorites
        END ReportFavorites

        BEGIN ADFFileData
        END ADFFileData

        BEGIN GenDb

            BEGIN Database
                DbType		 Satellite
                DefDb		 stkSatDb.sd
                UseMyDb		 Off
                MyDb		 \
                MaxMatches		 2000
                Use4SOC		 On

                BEGIN FieldDefaults

                END FieldDefaults

            END Database

            BEGIN Database
                DbType		 City
                DefDb		 stkCityDb.cd
                UseMyDb		 Off
                MyDb		 \
                MaxMatches		 2000
                Use4SOC		 On

                BEGIN FieldDefaults

                END FieldDefaults

            END Database

            BEGIN Database
                DbType		 Facility
                DefDb		 stkFacility.fd
                UseMyDb		 Off
                MyDb		 .\stkFacility.fd
                MaxMatches		 2000
                Use4SOC		 On

                BEGIN FieldDefaults

                END FieldDefaults

            END Database
        END GenDb

        BEGIN SOCDb
            BEGIN Defaults
            END Defaults
        END SOCDb

        BEGIN Msgp4Ext
        END Msgp4Ext

        BEGIN FileLocations
        END FileLocations

        BEGIN Author
            Optimize		 Yes
            UseBasicGlobe		 Yes
            ReadOnly		 No
            ViewerPassword		 No
            STKPassword		 No
            ExcludeInstallFiles		 No
            BEGIN ExternalFileList
            END ExternalFileList
        END Author

        BEGIN ExportDataFile
            FileType		 Ephemeris
            Directory		 C:\dev\v8x\STK\Automation\Tests\NUnitTests\Scenario\
            IntervalType		 Ephemeris
            TimePeriodStart		 0
            TimePeriodStop		 0
            StepType		 Ephemeris
            StepSize		 60
            EphemType		 STK
            UseVehicleCentralBody		 Yes
            CentralBody		 Earth
            SatelliteID		 -200000
            CoordSys		 J2000
            NonSatCoordSys		 Fixed
            InterpolateBoundaries		 Yes
            EphemFormat		 Current
            InterpType		 9
            InterpOrder		 5
            AttCoordSys		 Fixed
            Quaternions		 0
            ExportCovar		 Position
            AttitudeFormat		 Current
            TimePrecision		 6
            CCSDSDateFormat		 YMD
            CCSDSEphFormat		 SciNotation
            CCSDSTimeSystem		 UTC
            CCSDSRefFrame		 ICRF
            UseSatCenterAndFrame		 No
            IncludeCovariance		 No
            IncludeAcceleration		 No
            CCSDSFileFormat		 KVN
        END ExportDataFile

        BEGIN Desc
        END Desc

        BEGIN RfEnv
<?xml version = "1.0" standalone = "yes"?>
<SCOPE>
    <VAR name = "PropagationChannel">
        <SCOPE>
            <VAR name = "UseITU618Section2p5">
                <BOOL>false</BOOL>
            </VAR>
            <VAR name = "UseCloudFogModel">
                <BOOL>false</BOOL>
            </VAR>
            <VAR name = "CloudFogModel">
                <VAR name = "ITU-R_P840-7">
                    <SCOPE Class = "LinkEmbedControl">
                        <VAR name = "ReferenceType">
                            <STRING>&quot;Unlinked&quot;</STRING>
                        </VAR>
                        <VAR name = "Component">
                            <VAR name = "ITU-R_P840-7">
                                <SCOPE Class = "CloudFogLossModel">
                                    <VAR name = "Version">
                                        <STRING>&quot;1.0.0 a&quot;</STRING>
                                    </VAR>
                                    <VAR name = "IdentifierInformation">
                                        <SCOPE>
                                            <VAR name = "Identifier">
                                                <STRING>&quot;{4BD714B8-BA04-47D8-A8D8-9CB30F50E087}&quot;</STRING>
                                            </VAR>
                                            <VAR name = "Version">
                                                <STRING>&quot;1&quot;</STRING>
                                            </VAR>
                                            <VAR name = "SdfInformation">
                                                <SCOPE>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;0.0&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Url">
                                                        <STRING>&quot;&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                            <VAR name = "SourceIdentifierInformation">
                                                <SCOPE>
                                                    <VAR name = "Identifier">
                                                        <STRING>&quot;{E7BA4392-37BE-4446-A5C7-6068165B166A}&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;1&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "SdfInformation">
                                                        <SCOPE>
                                                            <VAR name = "Version">
                                                                <STRING>&quot;0.0&quot;</STRING>
                                                            </VAR>
                                                            <VAR name = "Url">
                                                                <STRING>&quot;&quot;</STRING>
                                                            </VAR>
                                                        </SCOPE>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </SCOPE>
                                    </VAR>
                                    <VAR name = "ComponentName">
                                        <STRING>&quot;ITU-R_P840-7&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Description">
                                        <STRING>&quot;ITU-R P840-7&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Type">
                                        <STRING>&quot;ITU-R P840-7&quot;</STRING>
                                    </VAR>
                                    <VAR name = "UserComment">
                                        <STRING>&quot;ITU-R P840-7&quot;</STRING>
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
                                    <VAR name = "LiquidWaterDensityValueChoice">
                                        <STRING>&quot;Liquid Water Content Density Value&quot;</STRING>
                                    </VAR>
                                    <VAR name = "CloudCeiling">
                                        <QUANTITY Dimension = "DistanceUnit" Unit = "m">
                                            <REAL>3000</REAL>
                                        </QUANTITY>
                                    </VAR>
                                    <VAR name = "CloudLayerThickness">
                                        <QUANTITY Dimension = "DistanceUnit" Unit = "m">
                                            <REAL>500</REAL>
                                        </QUANTITY>
                                    </VAR>
                                    <VAR name = "CloudTemp">
                                        <QUANTITY Dimension = "Temperature" Unit = "K">
                                            <REAL>273.15</REAL>
                                        </QUANTITY>
                                    </VAR>
                                    <VAR name = "CloudLiqWaterDensity">
                                        <QUANTITY Dimension = "SmallDensity" Unit = "kg*m^-3">
                                            <REAL>0.0001</REAL>
                                        </QUANTITY>
                                    </VAR>
                                    <VAR name = "AnnualAveragePercentValue">
                                        <QUANTITY Dimension = "Percent" Unit = "unitValue">
                                            <REAL>0.01</REAL>
                                        </QUANTITY>
                                    </VAR>
                                    <VAR name = "MonthlyAveragePercentValue">
                                        <QUANTITY Dimension = "Percent" Unit = "unitValue">
                                            <REAL>0.01</REAL>
                                        </QUANTITY>
                                    </VAR>
                                    <VAR name = "LiqWaterAverageDataMonth">
                                        <INT>1</INT>
                                    </VAR>
                                    <VAR name = "UseRainHeightAsCloudThickness">
                                        <BOOL>false</BOOL>
                                    </VAR>
                                </SCOPE>
                            </VAR>
                        </VAR>
                    </SCOPE>
                </VAR>
            </VAR>
            <VAR name = "UseTropoScintModel">
                <BOOL>false</BOOL>
            </VAR>
            <VAR name = "TropoScintModel">
                <VAR name = "ITU-R_P618-12">
                    <SCOPE Class = "LinkEmbedControl">
                        <VAR name = "ReferenceType">
                            <STRING>&quot;Unlinked&quot;</STRING>
                        </VAR>
                        <VAR name = "Component">
                            <VAR name = "ITU-R_P618-12">
                                <SCOPE Class = "TropoScintLossModel">
                                    <VAR name = "Version">
                                        <STRING>&quot;1.0.0 a&quot;</STRING>
                                    </VAR>
                                    <VAR name = "IdentifierInformation">
                                        <SCOPE>
                                            <VAR name = "Identifier">
                                                <STRING>&quot;{2502B40B-6762-4093-8DCB-0B10059D7C35}&quot;</STRING>
                                            </VAR>
                                            <VAR name = "Version">
                                                <STRING>&quot;1&quot;</STRING>
                                            </VAR>
                                            <VAR name = "SdfInformation">
                                                <SCOPE>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;0.0&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Url">
                                                        <STRING>&quot;&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                            <VAR name = "SourceIdentifierInformation">
                                                <SCOPE>
                                                    <VAR name = "Identifier">
                                                        <STRING>&quot;{BC27045B-5A54-458E-BF17-702BCFE40CA8}&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;1&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "SdfInformation">
                                                        <SCOPE>
                                                            <VAR name = "Version">
                                                                <STRING>&quot;0.0&quot;</STRING>
                                                            </VAR>
                                                            <VAR name = "Url">
                                                                <STRING>&quot;&quot;</STRING>
                                                            </VAR>
                                                        </SCOPE>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </SCOPE>
                                    </VAR>
                                    <VAR name = "ComponentName">
                                        <STRING>&quot;ITU-R_P618-12&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Description">
                                        <STRING>&quot;ITU-R P618-12&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Type">
                                        <STRING>&quot;ITU-R P618-12&quot;</STRING>
                                    </VAR>
                                    <VAR name = "UserComment">
                                        <STRING>&quot;ITU-R P618-12&quot;</STRING>
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
                                    <VAR name = "FadeDepthAverageTimeChoice">
                                        <STRING>&quot;Fade depth for the average year&quot;</STRING>
                                    </VAR>
                                    <VAR name = "FadeExceeded">
                                        <QUANTITY Dimension = "Percent" Unit = "unitValue">
                                            <REAL>0.001</REAL>
                                        </QUANTITY>
                                    </VAR>
                                    <VAR name = "PercentTimeRefracGrad">
                                        <QUANTITY Dimension = "Percent" Unit = "unitValue">
                                            <REAL>0.1</REAL>
                                        </QUANTITY>
                                    </VAR>
                                    <VAR name = "SurfaceTemperature">
                                        <QUANTITY Dimension = "Temperature" Unit = "K">
                                            <REAL>273.15</REAL>
                                        </QUANTITY>
                                    </VAR>
                                </SCOPE>
                            </VAR>
                        </VAR>
                    </SCOPE>
                </VAR>
            </VAR>
            <VAR name = "UseIonoFadingModel">
                <BOOL>false</BOOL>
            </VAR>
            <VAR name = "IonoFadingModel">
                <VAR name = "ITU-R_P531-13">
                    <SCOPE Class = "LinkEmbedControl">
                        <VAR name = "ReferenceType">
                            <STRING>&quot;Unlinked&quot;</STRING>
                        </VAR>
                        <VAR name = "Component">
                            <VAR name = "ITU-R_P531-13">
                                <SCOPE Class = "IonoFadingLossModel">
                                    <VAR name = "Version">
                                        <STRING>&quot;1.0.0 a&quot;</STRING>
                                    </VAR>
                                    <VAR name = "IdentifierInformation">
                                        <SCOPE>
                                            <VAR name = "Identifier">
                                                <STRING>&quot;{8D88CB9C-54D9-4ACC-B7B4-11BFA2ABE9C6}&quot;</STRING>
                                            </VAR>
                                            <VAR name = "Version">
                                                <STRING>&quot;1&quot;</STRING>
                                            </VAR>
                                            <VAR name = "SdfInformation">
                                                <SCOPE>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;0.0&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Url">
                                                        <STRING>&quot;&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                            <VAR name = "SourceIdentifierInformation">
                                                <SCOPE>
                                                    <VAR name = "Identifier">
                                                        <STRING>&quot;{1699891E-9828-41C7-ADD4-4BE20EFC34A8}&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;1&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "SdfInformation">
                                                        <SCOPE>
                                                            <VAR name = "Version">
                                                                <STRING>&quot;0.0&quot;</STRING>
                                                            </VAR>
                                                            <VAR name = "Url">
                                                                <STRING>&quot;&quot;</STRING>
                                                            </VAR>
                                                        </SCOPE>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </SCOPE>
                                    </VAR>
                                    <VAR name = "ComponentName">
                                        <STRING>&quot;ITU-R_P531-13&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Description">
                                        <STRING>&quot;ITU-R P531-13&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Type">
                                        <STRING>&quot;ITU-R P531-13&quot;</STRING>
                                    </VAR>
                                    <VAR name = "UserComment">
                                        <STRING>&quot;ITU-R P531-13&quot;</STRING>
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
                                    <VAR name = "UseAlternateAPFile">
                                        <BOOL>false</BOOL>
                                    </VAR>
                                    <VAR name = "AlternateAPDataFile">
                                        <STRING>&quot;&quot;</STRING>
                                    </VAR>
                                </SCOPE>
                            </VAR>
                        </VAR>
                    </SCOPE>
                </VAR>
            </VAR>
            <VAR name = "UseRainModel">
                <BOOL>false</BOOL>
            </VAR>
            <VAR name = "RainModel">
                <VAR name = "ITU-R_P618-13">
                    <SCOPE Class = "LinkEmbedControl">
                        <VAR name = "ReferenceType">
                            <STRING>&quot;Unlinked&quot;</STRING>
                        </VAR>
                        <VAR name = "Component">
                            <VAR name = "ITU-R_P618-13">
                                <SCOPE Class = "RainLossModel">
                                    <VAR name = "Version">
                                        <STRING>&quot;1.0.0 a&quot;</STRING>
                                    </VAR>
                                    <VAR name = "IdentifierInformation">
                                        <SCOPE>
                                            <VAR name = "Identifier">
                                                <STRING>&quot;{C102665B-B6CD-4510-91AC-7B7200771F4F}&quot;</STRING>
                                            </VAR>
                                            <VAR name = "Version">
                                                <STRING>&quot;1&quot;</STRING>
                                            </VAR>
                                            <VAR name = "SdfInformation">
                                                <SCOPE>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;0.0&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Url">
                                                        <STRING>&quot;&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                            <VAR name = "SourceIdentifierInformation">
                                                <SCOPE>
                                                    <VAR name = "Identifier">
                                                        <STRING>&quot;{62382EA0-41C0-45F7-AA94-ACC684509D66}&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;1&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "SdfInformation">
                                                        <SCOPE>
                                                            <VAR name = "Version">
                                                                <STRING>&quot;0.0&quot;</STRING>
                                                            </VAR>
                                                            <VAR name = "Url">
                                                                <STRING>&quot;&quot;</STRING>
                                                            </VAR>
                                                        </SCOPE>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </SCOPE>
                                    </VAR>
                                    <VAR name = "ComponentName">
                                        <STRING>&quot;ITU-R_P618-13&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Description">
                                        <STRING>&quot;ITU-R P618-13 rain model&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Type">
                                        <STRING>&quot;ITU-R P618-13&quot;</STRING>
                                    </VAR>
                                    <VAR name = "UserComment">
                                        <STRING>&quot;ITU-R P618-13 rain model&quot;</STRING>
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
                                    <VAR name = "SurfaceTemperature">
                                        <QUANTITY Dimension = "Temperature" Unit = "K">
                                            <REAL>273.15</REAL>
                                        </QUANTITY>
                                    </VAR>
                                    <VAR name = "EnableDepolarizationLoss">
                                        <BOOL>false</BOOL>
                                    </VAR>
                                    <VAR name = "EnableITU1510">
                                        <BOOL>false</BOOL>
                                    </VAR>
                                    <VAR name = "UseAnnualITU1510">
                                        <BOOL>true</BOOL>
                                    </VAR>
                                    <VAR name = "ITU1510Month">
                                        <STRING>&quot;January&quot;</STRING>
                                    </VAR>
                                </SCOPE>
                            </VAR>
                        </VAR>
                    </SCOPE>
                </VAR>
            </VAR>
            <VAR name = "UseAtmosAbsorptionModel">
                <BOOL>false</BOOL>
            </VAR>
            <VAR name = "AtmosAbsorptionModel">
                <VAR name = "Simple_Satcom">
                    <SCOPE Class = "LinkEmbedControl">
                        <VAR name = "ReferenceType">
                            <STRING>&quot;Unlinked&quot;</STRING>
                        </VAR>
                        <VAR name = "Component">
                            <VAR name = "Simple_Satcom">
                                <SCOPE Class = "AtmosphericAbsorptionModel">
                                    <VAR name = "Version">
                                        <STRING>&quot;1.0.1 a&quot;</STRING>
                                    </VAR>
                                    <VAR name = "IdentifierInformation">
                                        <SCOPE>
                                            <VAR name = "Identifier">
                                                <STRING>&quot;{5F7A99F1-697B-4596-A8EC-31491D3CD655}&quot;</STRING>
                                            </VAR>
                                            <VAR name = "Version">
                                                <STRING>&quot;1&quot;</STRING>
                                            </VAR>
                                            <VAR name = "SdfInformation">
                                                <SCOPE>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;0.0&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Url">
                                                        <STRING>&quot;&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                            <VAR name = "SourceIdentifierInformation">
                                                <SCOPE>
                                                    <VAR name = "Identifier">
                                                        <STRING>&quot;{29E14193-BA6A-42C5-83C5-73DF960AFE44}&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;1&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "SdfInformation">
                                                        <SCOPE>
                                                            <VAR name = "Version">
                                                                <STRING>&quot;0.0&quot;</STRING>
                                                            </VAR>
                                                            <VAR name = "Url">
                                                                <STRING>&quot;&quot;</STRING>
                                                            </VAR>
                                                        </SCOPE>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </SCOPE>
                                    </VAR>
                                    <VAR name = "ComponentName">
                                        <STRING>&quot;Simple_Satcom&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Description">
                                        <STRING>&quot;Simple Satcom gaseous absorption model&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Type">
                                        <STRING>&quot;Simple Satcom&quot;</STRING>
                                    </VAR>
                                    <VAR name = "UserComment">
                                        <STRING>&quot;Simple Satcom gaseous absorption model&quot;</STRING>
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
                                    <VAR name = "SurfaceTemperature">
                                        <QUANTITY Dimension = "Temperature" Unit = "K">
                                            <REAL>293.15</REAL>
                                        </QUANTITY>
                                    </VAR>
                                    <VAR name = "WaterVaporConcentration">
                                        <QUANTITY Dimension = "Density" Unit = "g*m^-3">
                                            <REAL>7.5</REAL>
                                        </QUANTITY>
                                    </VAR>
                                </SCOPE>
                            </VAR>
                        </VAR>
                    </SCOPE>
                </VAR>
            </VAR>
            <VAR name = "UseUrbanTerresPropLossModel">
                <BOOL>false</BOOL>
            </VAR>
            <VAR name = "UrbanTerresPropLossModel">
                <VAR name = "Two_Ray">
                    <SCOPE Class = "LinkEmbedControl">
                        <VAR name = "ReferenceType">
                            <STRING>&quot;Unlinked&quot;</STRING>
                        </VAR>
                        <VAR name = "Component">
                            <VAR name = "Two_Ray">
                                <SCOPE Class = "UrbanTerrestrialPropagationLossModel">
                                    <VAR name = "Version">
                                        <STRING>&quot;1.0.0 a&quot;</STRING>
                                    </VAR>
                                    <VAR name = "IdentifierInformation">
                                        <SCOPE>
                                            <VAR name = "Identifier">
                                                <STRING>&quot;{74DF7D55-F075-40E1-AE3B-4B52E8B20633}&quot;</STRING>
                                            </VAR>
                                            <VAR name = "Version">
                                                <STRING>&quot;1&quot;</STRING>
                                            </VAR>
                                            <VAR name = "SdfInformation">
                                                <SCOPE>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;0.0&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Url">
                                                        <STRING>&quot;&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                            <VAR name = "SourceIdentifierInformation">
                                                <SCOPE>
                                                    <VAR name = "Identifier">
                                                        <STRING>&quot;{60FA4C9B-5D74-4743-A449-66CEB6DFC97B}&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;1&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "SdfInformation">
                                                        <SCOPE>
                                                            <VAR name = "Version">
                                                                <STRING>&quot;0.0&quot;</STRING>
                                                            </VAR>
                                                            <VAR name = "Url">
                                                                <STRING>&quot;&quot;</STRING>
                                                            </VAR>
                                                        </SCOPE>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </SCOPE>
                                    </VAR>
                                    <VAR name = "ComponentName">
                                        <STRING>&quot;Two_Ray&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Description">
                                        <STRING>&quot;Two Ray (Fourth Power Law) atmospheric absorption model&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Type">
                                        <STRING>&quot;Two Ray&quot;</STRING>
                                    </VAR>
                                    <VAR name = "UserComment">
                                        <STRING>&quot;Two Ray (Fourth Power Law) atmospheric absorption model&quot;</STRING>
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
                                    <VAR name = "SurfaceTemperature">
                                        <QUANTITY Dimension = "Temperature" Unit = "K">
                                            <REAL>273.15</REAL>
                                        </QUANTITY>
                                    </VAR>
                                    <VAR name = "LossFactor">
                                        <REAL>1</REAL>
                                    </VAR>
                                </SCOPE>
                            </VAR>
                        </VAR>
                    </SCOPE>
                </VAR>
            </VAR>
            <VAR name = "UseCustomA">
                <BOOL>false</BOOL>
            </VAR>
            <VAR name = "UseCustomB">
                <BOOL>false</BOOL>
            </VAR>
            <VAR name = "UseCustomC">
                <BOOL>false</BOOL>
            </VAR>
        </SCOPE>
    </VAR>
    <VAR name = "EarthTemperature">
        <QUANTITY Dimension = "Temperature" Unit = "K">
            <REAL>290</REAL>
        </QUANTITY>
    </VAR>
    <VAR name = "RainOutagePercent">
        <REAL>0.1</REAL>
    </VAR>
    <VAR name = "ActiveCommSystem">
        <LINKTOOBJ>
            <STRING>&quot;None&quot;</STRING>
        </LINKTOOBJ>
    </VAR>
    <VAR name = "MagneticNorthPoleLatitude">
        <QUANTITY Dimension = "AngleUnit" Unit = "rad">
            <REAL>1.387536755335492</REAL>
        </QUANTITY>
    </VAR>
    <VAR name = "MagneticNorthPoleLongitude">
        <QUANTITY Dimension = "AngleUnit" Unit = "rad">
            <REAL>-1.204277183876087</REAL>
        </QUANTITY>
    </VAR>
</SCOPE>        END RfEnv

        BEGIN LaserEnv
<?xml version = "1.0" standalone = "yes"?>
<SCOPE>
    <VAR name = "PropagationChannel">
        <SCOPE>
            <VAR name = "EnableAtmosphericLossModel">
                <BOOL>false</BOOL>
            </VAR>
            <VAR name = "AtmosphericLossModel">
                <VAR name = "Beer-Bouguer-Lambert_Law">
                    <SCOPE Class = "LinkEmbedControl">
                        <VAR name = "ReferenceType">
                            <STRING>&quot;Unlinked&quot;</STRING>
                        </VAR>
                        <VAR name = "Component">
                            <VAR name = "Beer-Bouguer-Lambert_Law">
                                <SCOPE Class = "LaserAtmosphericAbsorptionLossModel">
                                    <VAR name = "Version">
                                        <STRING>&quot;1.0.0 a&quot;</STRING>
                                    </VAR>
                                    <VAR name = "IdentifierInformation">
                                        <SCOPE>
                                            <VAR name = "Identifier">
                                                <STRING>&quot;{15444A80-05DB-4B11-9D29-8B594FA0DF5C}&quot;</STRING>
                                            </VAR>
                                            <VAR name = "Version">
                                                <STRING>&quot;1&quot;</STRING>
                                            </VAR>
                                            <VAR name = "SdfInformation">
                                                <SCOPE>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;0.0&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Url">
                                                        <STRING>&quot;&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                            <VAR name = "SourceIdentifierInformation">
                                                <SCOPE>
                                                    <VAR name = "Identifier">
                                                        <STRING>&quot;{6896684B-630D-472D-8027-385684842E74}&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;1&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "SdfInformation">
                                                        <SCOPE>
                                                            <VAR name = "Version">
                                                                <STRING>&quot;0.0&quot;</STRING>
                                                            </VAR>
                                                            <VAR name = "Url">
                                                                <STRING>&quot;&quot;</STRING>
                                                            </VAR>
                                                        </SCOPE>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </SCOPE>
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
                                        <STRING>&quot;@Top&quot;</STRING>
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
                                </SCOPE>
                            </VAR>
                        </VAR>
                    </SCOPE>
                </VAR>
            </VAR>
            <VAR name = "EnableTropoScintLossModel">
                <BOOL>false</BOOL>
            </VAR>
            <VAR name = "TropoScintLossModel">
                <VAR name = "ITU-R_P1814">
                    <SCOPE Class = "LinkEmbedControl">
                        <VAR name = "ReferenceType">
                            <STRING>&quot;Unlinked&quot;</STRING>
                        </VAR>
                        <VAR name = "Component">
                            <VAR name = "ITU-R_P1814">
                                <SCOPE Class = "LaserTropoScintLossModel">
                                    <VAR name = "Version">
                                        <STRING>&quot;1.0.0 a&quot;</STRING>
                                    </VAR>
                                    <VAR name = "IdentifierInformation">
                                        <SCOPE>
                                            <VAR name = "Identifier">
                                                <STRING>&quot;{6366B078-FD45-41EE-85D8-4BA976DC8AD9}&quot;</STRING>
                                            </VAR>
                                            <VAR name = "Version">
                                                <STRING>&quot;1&quot;</STRING>
                                            </VAR>
                                            <VAR name = "SdfInformation">
                                                <SCOPE>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;0.0&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Url">
                                                        <STRING>&quot;&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                            <VAR name = "SourceIdentifierInformation">
                                                <SCOPE>
                                                    <VAR name = "Identifier">
                                                        <STRING>&quot;{651AF2C8-7D6D-457E-8F99-1FB796A460BF}&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;1&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "SdfInformation">
                                                        <SCOPE>
                                                            <VAR name = "Version">
                                                                <STRING>&quot;0.0&quot;</STRING>
                                                            </VAR>
                                                            <VAR name = "Url">
                                                                <STRING>&quot;&quot;</STRING>
                                                            </VAR>
                                                        </SCOPE>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </SCOPE>
                                    </VAR>
                                    <VAR name = "ComponentName">
                                        <STRING>&quot;ITU-R_P1814&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Description">
                                        <STRING>&quot;ITU-R P1814&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Type">
                                        <STRING>&quot;ITU-R P1814&quot;</STRING>
                                    </VAR>
                                    <VAR name = "UserComment">
                                        <STRING>&quot;ITU-R P1814&quot;</STRING>
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
                                    <VAR name = "AtmosphericTurbulenceModel">
                                        <VAR name = "Constant">
                                            <SCOPE Class = "AtmosphericTurbulenceModel">
                                                <VAR name = "ConstantRefractiveIndexStructureParameter">
                                                    <REAL>1.7e-14</REAL>
                                                </VAR>
                                                <VAR name = "Type">
                                                    <STRING>&quot;Constant&quot;</STRING>
                                                </VAR>
                                            </SCOPE>
                                        </VAR>
                                    </VAR>
                                </SCOPE>
                            </VAR>
                        </VAR>
                    </SCOPE>
                </VAR>
            </VAR>
        </SCOPE>
    </VAR>
</SCOPE>        END LaserEnv

        BEGIN ComponentManager
        END ComponentManager

        BEGIN RadarCrossSection
<?xml version = "1.0" standalone = "yes"?>
<SCOPE>
    <VAR name = "Model">
        <VAR name = "Radar_Cross_Section">
            <SCOPE Class = "LinkEmbedControl">
                <VAR name = "ReferenceType">
                    <STRING>&quot;Unlinked&quot;</STRING>
                </VAR>
                <VAR name = "Component">
                    <VAR name = "Radar_Cross_Section">
                        <SCOPE Class = "RCS">
                            <VAR name = "Version">
                                <STRING>&quot;1.0.0 a&quot;</STRING>
                            </VAR>
                            <VAR name = "IdentifierInformation">
                                <SCOPE>
                                    <VAR name = "Identifier">
                                        <STRING>&quot;{2FA02B6B-E589-42C2-A5CC-84AA3BC0F7A1}&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Version">
                                        <STRING>&quot;1&quot;</STRING>
                                    </VAR>
                                    <VAR name = "SdfInformation">
                                        <SCOPE>
                                            <VAR name = "Version">
                                                <STRING>&quot;0.0&quot;</STRING>
                                            </VAR>
                                            <VAR name = "Url">
                                                <STRING>&quot;&quot;</STRING>
                                            </VAR>
                                        </SCOPE>
                                    </VAR>
                                    <VAR name = "SourceIdentifierInformation">
                                        <SCOPE>
                                            <VAR name = "Identifier">
                                                <STRING>&quot;{EF03E656-5AB7-4F70-A363-4753683F2BD4}&quot;</STRING>
                                            </VAR>
                                            <VAR name = "Version">
                                                <STRING>&quot;1&quot;</STRING>
                                            </VAR>
                                            <VAR name = "SdfInformation">
                                                <SCOPE>
                                                    <VAR name = "Version">
                                                        <STRING>&quot;0.0&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "Url">
                                                        <STRING>&quot;&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </SCOPE>
                                    </VAR>
                                </SCOPE>
                            </VAR>
                            <VAR name = "ComponentName">
                                <STRING>&quot;Radar_Cross_Section&quot;</STRING>
                            </VAR>
                            <VAR name = "Description">
                                <STRING>&quot;Radar Cross Section&quot;</STRING>
                            </VAR>
                            <VAR name = "Type">
                                <STRING>&quot;Radar Cross Section&quot;</STRING>
                            </VAR>
                            <VAR name = "UserComment">
                                <STRING>&quot;Radar Cross Section&quot;</STRING>
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
                            <VAR name = "FrequencyBandList">
                                <LIST>
                                    <SCOPE>
                                        <VAR name = "MinFrequency">
                                            <QUANTITY Dimension = "BandwidthUnit" Unit = "Hz">
                                                <REAL>2997920</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "ComputeTypeStrategy">
                                            <VAR name = "Constant Value">
                                                <SCOPE Class = "RCS Compute Strategy">
                                                    <VAR name = "ConstantValue">
                                                        <QUANTITY Dimension = "RcsUnit" Unit = "sqm">
                                                            <REAL>1</REAL>
                                                        </QUANTITY>
                                                    </VAR>
                                                    <VAR name = "Type">
                                                        <STRING>&quot;Constant Value&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "ComponentName">
                                                        <STRING>&quot;Constant Value&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </VAR>
                                        <VAR name = "SwerlingCase">
                                            <STRING>&quot;0&quot;</STRING>
                                        </VAR>
                                    </SCOPE>
                                    <SCOPE>
                                        <VAR name = "MinFrequency">
                                            <QUANTITY Dimension = "BandwidthUnit" Unit = "Hz">
                                                <REAL>3000000</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "ComputeTypeStrategy">
                                            <VAR name = "Constant Value">
                                                <SCOPE Class = "RCS Compute Strategy">
                                                    <VAR name = "ConstantValue">
                                                        <QUANTITY Dimension = "RcsUnit" Unit = "sqm">
                                                            <REAL>1</REAL>
                                                        </QUANTITY>
                                                    </VAR>
                                                    <VAR name = "Type">
                                                        <STRING>&quot;Constant Value&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "ComponentName">
                                                        <STRING>&quot;Constant Value&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </VAR>
                                        <VAR name = "SwerlingCase">
                                            <STRING>&quot;0&quot;</STRING>
                                        </VAR>
                                    </SCOPE>
                                    <SCOPE>
                                        <VAR name = "MinFrequency">
                                            <QUANTITY Dimension = "BandwidthUnit" Unit = "Hz">
                                                <REAL>300000000000</REAL>
                                            </QUANTITY>
                                        </VAR>
                                        <VAR name = "ComputeTypeStrategy">
                                            <VAR name = "Constant Value">
                                                <SCOPE Class = "RCS Compute Strategy">
                                                    <VAR name = "ConstantValue">
                                                        <QUANTITY Dimension = "RcsUnit" Unit = "sqm">
                                                            <REAL>1</REAL>
                                                        </QUANTITY>
                                                    </VAR>
                                                    <VAR name = "Type">
                                                        <STRING>&quot;Constant Value&quot;</STRING>
                                                    </VAR>
                                                    <VAR name = "ComponentName">
                                                        <STRING>&quot;Constant Value&quot;</STRING>
                                                    </VAR>
                                                </SCOPE>
                                            </VAR>
                                        </VAR>
                                        <VAR name = "SwerlingCase">
                                            <STRING>&quot;0&quot;</STRING>
                                        </VAR>
                                    </SCOPE>
                                </LIST>
                            </VAR>
                        </SCOPE>
                    </VAR>
                </VAR>
            </SCOPE>
        </VAR>
    </VAR>
</SCOPE>        END RadarCrossSection

        BEGIN Gator
            RPOComponentsLoaded		 False
            RPOPythonComponentsLoaded		 False

            BEGIN PASSIVESAFETYUIVALS
                SPHERICALANALYSIS		 On
                CUSTOMINTERVAL		 Off
                SPHERICALRADIUS		  1.0000000000000000e+03
                PERAXR		  1.0000000000000000e+02
                PERAXI		  2.0000000000000000e+03
                PERAXC		  1.0000000000000000e+03
                PROPTIME		  8.6400000000000000e+04
                STEPSIZE		  6.0000000000000000e+01
                STARTTIME		  0.0000000000000000e+00
                STOPTIME		  0.0000000000000000e+00
            END PASSIVESAFETYUIVALS

        END Gator

        BEGIN Crdn
            BEGIN AXES
                Type		 AXES_TRAJECTORY
                Name		 BBR_Axes
                Description		 Body-Body Rotating Axes
                AbsolutePath		 CentralBody/Earth
                TrajPoint		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                ReferenceSystem		
                BEGIN SYSTEM
                    Type		 SYSTEM_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Moon
                END SYSTEM
                TrajAxesType		 20
                LabelX		 
                LabelY		 
                LabelZ		 
            END AXES
            BEGIN AXES
                Type		 AXES_ATEPOCH
                Name		 Earth_Aligned_at_Epoch
                Description		 Aligned with Earth Fixed at Epoch
                AbsolutePath		 CentralBody/Earth
                Epoch		 1 Jan 2000 11:58:55.816000000
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
                LabelX		 
                LabelY		 
                LabelZ		 
            END AXES
            BEGIN AXES
                Type		 AXES_ATEPOCH
                Name		 Mean_Ecliptic_of_Epoch
                Description		 Mean Ecliptic of Epoch Axes
                AbsolutePath		 CentralBody/Earth
                Epoch		 1 Jan 2000 11:58:55.816000000
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MeanEclpDate
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
                LabelX		 
                LabelY		 
                LabelZ		 
            END AXES
            BEGIN AXES
                Type		 AXES_ATEPOCH
                Name		 Mean_Ecliptic_of_J2000
                Description		 Mean Ecliptic of J2000 Axes
                AbsolutePath		 CentralBody/Earth
                Epoch		 1 Jan 2000 11:58:55.816000000
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MeanEclpDate
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
                LabelX		 
                LabelY		 
                LabelZ		 
            END AXES
            BEGIN AXES
                Type		 AXES_ATEPOCH
                Name		 Mean_Equinox_True_Equator_of_Epoch
                Description		 Mean Equinox True Equator of Epoch Axes
                AbsolutePath		 CentralBody/Earth
                Epoch		 1 Jan 2000 11:58:55.816000000
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TEMED
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
                LabelX		 
                LabelY		 
                LabelZ		 
            END AXES
            BEGIN AXES
                Type		 AXES_ATEPOCH
                Name		 Mean_of_Epoch
                Description		 Mean of Epoch Axes
                AbsolutePath		 CentralBody/Earth
                Epoch		 1 Jan 2000 11:58:55.816000000
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
                LabelX		 
                LabelY		 
                LabelZ		 
            END AXES
            BEGIN AXES
                Type		 AXES_ATEPOCH
                Name		 True_Ecliptic_of_Epoch
                Description		 True Ecliptic of Epoch Axes
                AbsolutePath		 CentralBody/Earth
                Epoch		 1 Jan 2000 11:58:55.816000000
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TrueEclpDate
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
                LabelX		 
                LabelY		 
                LabelZ		 
            END AXES
            BEGIN AXES
                Type		 AXES_ATEPOCH
                Name		 True_of_Epoch
                Description		 True of Epoch Axes
                AbsolutePath		 CentralBody/Earth
                Epoch		 1 Jan 2000 11:58:55.816000000
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
                LabelX		 
                LabelY		 
                LabelZ		 
            END AXES
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Aligned_with_Fixed_at_Epoch
                Description		 Earth Centered Aligned with Fixed at Epoch Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Earth_Aligned_at_Epoch
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Fixed
                Description		 Phobos Centered Fixed Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Inertial
                Description		 Phobos Centered Inertial Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_of_Date
                Description		 Phobos Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_True_of_Date
                Description		 Phobos Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Mean_B1950
                Description		 Earth Centered Mean B1950 Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 B1950
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Mean_Ecliptic_of_Date
                Description		 Earth Centered Mean Ecliptic of Date Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MeanEclpDate
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Mean_Ecliptic_of_Epoch
                Description		 Earth Centered Mean Ecliptic of Epoch Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Mean_Ecliptic_of_Epoch
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Mean_Ecliptic_of_J2000
                Description		 Earth Centered Mean Ecliptic of J2000 Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Mean_Ecliptic_of_J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Mean_Equinox_True_Equator_of_Date
                Description		 Earth Centered Mean Equinox True Equator of Date Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TEMED
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Mean_Equinox_True_Equator_of_Epoch
                Description		 Earth Centered Mean Equinox True Equator of Epoch Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Mean_Equinox_True_Equator_of_Epoch
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Mean_J2000
                Description		 Earth Centered Mean J2000 (Default Inertial) Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Mean_of_Date
                Description		 Earth Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Mean_of_Epoch
                Description		 Earth Centered Mean of Epoch Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Mean_of_Epoch
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 True_Ecliptic_of_Date
                Description		 Earth Centered True Ecliptic of Date Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TrueEclpDate
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 True_Ecliptic_of_Epoch
                Description		 Earth Centered True Ecliptic of Epoch Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 True_Ecliptic_of_Epoch
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 True_of_Date
                Description		 Earth Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 True_of_Epoch
                Description		 Earth Centered True of Epoch Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 True_of_Epoch
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 User_Defined
                Description		 User Assembled Coordinate System
                AbsolutePath		 CentralBody/Earth
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Earth
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Callisto_Angular_Velocity
                Description		 Callisto Angular Velocity
                AbsolutePath		 CentralBody/Earth
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Ceres_Angular_Velocity
                Description		 Ceres Angular Velocity
                AbsolutePath		 CentralBody/Earth
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Charon_Angular_Velocity
                Description		 Charon Angular Velocity
                AbsolutePath		 CentralBody/Earth
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Deimos_Angular_Velocity
                Description		 Deimos Angular Velocity
                AbsolutePath		 CentralBody/Earth
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Earth_Angular_Velocity
                Description		 Earth Angular Velocity
                AbsolutePath		 CentralBody/Earth
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Europa_Angular_Velocity
                Description		 Europa Angular Velocity
                AbsolutePath		 CentralBody/Earth
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Ganymede_Angular_Velocity
                Description		 Ganymede Angular Velocity
                AbsolutePath		 CentralBody/Earth
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Io_Angular_Velocity
                Description		 Io Angular Velocity
                AbsolutePath		 CentralBody/Earth
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Phobos_Angular_Velocity
                Description		 Phobos Angular Velocity
                AbsolutePath		 CentralBody/Earth
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Titan_Angular_Velocity
                Description		 Titan Angular Velocity
                AbsolutePath		 CentralBody/Earth
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Triton_Angular_Velocity
                Description		 Triton Angular Velocity
                AbsolutePath		 CentralBody/Earth
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Earth
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_FIXED
                Name		 User_Defined
                Description		 User Defined Vector Fixed in Coordinate System
                AbsolutePath		 CentralBody/Earth
                Dimension		 6
                FixedVector		
                 0.0000000000000000e+00
                 0.0000000000000000e+00
                 1.0000000000000000e+00
                UiSequence		 321
                UiCoordType		 4
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END VECTOR
            BEGIN VECTOR
                Type		 VECTOR_FIXED
                Name		 X_Vector
                Description		 X Axis in Default Coordinate System
                AbsolutePath		 CentralBody/Earth
                Dimension		 6
                FixedVector		
                 1.0000000000000000e+00
                 0.0000000000000000e+00
                 0.0000000000000000e+00
                UiSequence		 321
                UiCoordType		 4
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END VECTOR
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Fixed
                Description		 Jupiter Centered Fixed Coordinate System
                AbsolutePath		 CentralBody/Jupiter
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Jupiter
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Jupiter
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Inertial
                Description		 Jupiter Centered Inertial Coordinate System
                AbsolutePath		 CentralBody/Jupiter
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Jupiter
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Jupiter
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_of_Date
                Description		 Jupiter Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Jupiter
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Jupiter
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Jupiter
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_True_of_Date
                Description		 Jupiter Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Jupiter
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Jupiter
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Jupiter
                END AXES
            END SYSTEM
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Jupiter_Angular_Velocity
                Description		 Jupiter Angular Velocity
                AbsolutePath		 CentralBody/Jupiter
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Jupiter
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Jupiter
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Fixed
                Description		 Mars Centered Fixed Coordinate System
                AbsolutePath		 CentralBody/Mars
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Mars
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Mars
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Inertial
                Description		 Mars Centered Inertial Coordinate System
                AbsolutePath		 CentralBody/Mars
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Mars
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Mars
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_of_Date
                Description		 Mars Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Mars
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Mars
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Mars
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_True_of_Date
                Description		 Mars Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Mars
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Mars
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Mars
                END AXES
            END SYSTEM
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Mars_Angular_Velocity
                Description		 Mars Angular Velocity
                AbsolutePath		 CentralBody/Mars
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Mars
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Mars
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Fixed
                Description		 Mercury Centered Fixed Coordinate System
                AbsolutePath		 CentralBody/Mercury
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Mercury
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Mercury
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Inertial
                Description		 Mercury Centered Inertial Coordinate System
                AbsolutePath		 CentralBody/Mercury
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Mercury
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Mercury
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_of_Date
                Description		 Mercury Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Mercury
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Mercury
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Mercury
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_True_of_Date
                Description		 Mercury Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Mercury
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Mercury
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Mercury
                END AXES
            END SYSTEM
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Mercury_Angular_Velocity
                Description		 Mercury Angular Velocity
                AbsolutePath		 CentralBody/Mercury
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Mercury
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Mercury
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Fixed
                Description		 Moon Centered Fixed Coordinate System
                AbsolutePath		 CentralBody/Moon
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Moon
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Moon
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Inertial
                Description		 Moon Centered Inertial Coordinate System
                AbsolutePath		 CentralBody/Moon
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Moon
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Moon
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_J2000
                Description		 Moon Centered Mean Earth Equator of J2000 Coordinate System
                AbsolutePath		 CentralBody/Moon
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Moon
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_of_Date
                Description		 Moon Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Moon
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Moon
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Moon
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_True_of_Date
                Description		 Moon Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Moon
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Moon
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Moon
                END AXES
            END SYSTEM
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Moon_Angular_Velocity
                Description		 Moon Angular Velocity
                AbsolutePath		 CentralBody/Moon
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Moon
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Moon
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Fixed
                Description		 Neptune Centered Fixed Coordinate System
                AbsolutePath		 CentralBody/Neptune
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Neptune
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Neptune
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Inertial
                Description		 Neptune Centered Inertial Coordinate System
                AbsolutePath		 CentralBody/Neptune
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Neptune
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Neptune
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_of_Date
                Description		 Neptune Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Neptune
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Neptune
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Neptune
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_True_of_Date
                Description		 Neptune Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Neptune
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Neptune
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Neptune
                END AXES
            END SYSTEM
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Neptune_Angular_Velocity
                Description		 Neptune Angular Velocity
                AbsolutePath		 CentralBody/Neptune
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Neptune
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Neptune
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Fixed
                Description		 Pluto Centered Fixed Coordinate System
                AbsolutePath		 CentralBody/Pluto
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Pluto
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Pluto
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Inertial
                Description		 Pluto Centered Inertial Coordinate System
                AbsolutePath		 CentralBody/Pluto
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Pluto
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Pluto
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_of_Date
                Description		 Pluto Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Pluto
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Pluto
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Pluto
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_True_of_Date
                Description		 Pluto Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Pluto
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Pluto
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Pluto
                END AXES
            END SYSTEM
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Pluto_Angular_Velocity
                Description		 Pluto Angular Velocity
                AbsolutePath		 CentralBody/Pluto
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Pluto
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Pluto
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Fixed
                Description		 Saturn Centered Fixed Coordinate System
                AbsolutePath		 CentralBody/Saturn
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Saturn
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Saturn
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Inertial
                Description		 Saturn Centered Inertial Coordinate System
                AbsolutePath		 CentralBody/Saturn
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Saturn
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Saturn
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_of_Date
                Description		 Saturn Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Saturn
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Saturn
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Saturn
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_True_of_Date
                Description		 Saturn Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Saturn
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Saturn
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Saturn
                END AXES
            END SYSTEM
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Saturn_Angular_Velocity
                Description		 Saturn Angular Velocity
                AbsolutePath		 CentralBody/Saturn
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Saturn
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Saturn
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Fixed
                Description		 Sun Centered Fixed Coordinate System
                AbsolutePath		 CentralBody/Sun
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Sun
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Sun
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Inertial
                Description		 Sun Centered Inertial Coordinate System
                AbsolutePath		 CentralBody/Sun
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Sun
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Sun
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_Ecliptic_of_J2000
                Description		 Sun Centered Mean Ecliptic of J2000 Coordinate System
                AbsolutePath		 CentralBody/Sun
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Sun
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Mean_Ecliptic_of_J2000
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_J2000
                Description		 Sun Centered Mean Earth Equator of J2000 Coordinate System
                AbsolutePath		 CentralBody/Sun
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Sun
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Earth
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_of_Date
                Description		 Sun Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Sun
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Sun
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Sun
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_True_of_Date
                Description		 Sun Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Sun
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Sun
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Sun
                END AXES
            END SYSTEM
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Sun_Angular_Velocity
                Description		 Sun Angular Velocity
                AbsolutePath		 CentralBody/Sun
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Sun
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Sun
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Fixed
                Description		 Uranus Centered Fixed Coordinate System
                AbsolutePath		 CentralBody/Uranus
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Uranus
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Uranus
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Inertial
                Description		 Uranus Centered Inertial Coordinate System
                AbsolutePath		 CentralBody/Uranus
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Uranus
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Uranus
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_of_Date
                Description		 Uranus Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Uranus
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Uranus
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Uranus
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_True_of_Date
                Description		 Uranus Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Uranus
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Uranus
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Uranus
                END AXES
            END SYSTEM
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Uranus_Angular_Velocity
                Description		 Uranus Angular Velocity
                AbsolutePath		 CentralBody/Uranus
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Uranus
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Uranus
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Fixed
                Description		 Venus Centered Fixed Coordinate System
                AbsolutePath		 CentralBody/Venus
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Venus
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Venus
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Inertial
                Description		 Venus Centered Inertial Coordinate System
                AbsolutePath		 CentralBody/Venus
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Venus
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Venus
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_Mean_of_Date
                Description		 Venus Centered Mean of Date Coordinate System
                AbsolutePath		 CentralBody/Venus
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Venus
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 MOD
                    AbsolutePath		 CentralBody/Venus
                END AXES
            END SYSTEM
            BEGIN SYSTEM
                Type		 SYSTEM_ASSEMBLED
                Name		 Centered_True_of_Date
                Description		 Venus Centered True of Date Coordinate System
                AbsolutePath		 CentralBody/Venus
                Origin		
                BEGIN POINT
                    Type		 POINT_LINKTO
                    Name		 Center
                    AbsolutePath		 CentralBody/Venus
                END POINT
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 TOD
                    AbsolutePath		 CentralBody/Venus
                END AXES
            END SYSTEM
            BEGIN VECTOR
                Type		 VECTOR_AXESDERIVATIVE
                Name		 Venus_Angular_Velocity
                Description		 Venus Angular Velocity
                AbsolutePath		 CentralBody/Venus
                Axes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Fixed
                    AbsolutePath		 CentralBody/Venus
                END AXES
                ReferenceAxes		
                BEGIN AXES
                    Type		 AXES_LINKTO
                    Name		 Inertial
                    AbsolutePath		 CentralBody/Venus
                END AXES
                DifferentiationTimeStep		  1.0000000000000001e-01
            END VECTOR
        END Crdn

        BEGIN SpiceExt
            OutputErrorMsgsOnLoad		 No
            SpiceFile		 "asteroids.bsp"
            SpiceFile		 "jupiter.bsp"
            SpiceFile		 "mars.bsp"
            SpiceFile		 "neptune.bsp"
            SpiceFile		 "planets.bsp"
            SpiceFile		 "pluto.bsp"
            SpiceFile		 "saturn.bsp"
            SpiceFile		 "uranus.bsp"
        END SpiceExt

        BEGIN FlightScenExt
        END FlightScenExt

        BEGIN Graphics

            BEGIN Animation

                StartTime		 1 Jul 1999 00:00:00.000000000
                EndTime		 1 Jun 2004 16:00:00.000000000
                CurrentTime		 1 Jul 1999 00:00:00.000000000
                Direction		 Forward
                UpdateDelta		 60
                RefreshDelta		 HighSpeed
                XRealTimeMult		 1
                RealTimeOffset		 0
                XRtStartFromPause		                Yes		
                TimeArrayIncrement		 1

            END Animation


            BEGIN DisplayFlags
                ShowLabels		 On
                ShowPassLabel		 Off
                ShowElsetNum		 Off
                ShowGndTracks		 On
                ShowGndMarkers		 On
                ShowOrbitMarkers		 On
                ShowPlanetOrbits		 Off
                ShowPlanetCBIPos		 On
                ShowPlanetCBILabel		 On
                ShowPlanetGndPos		 On
                ShowPlanetGndLabel		 On
                ShowSensors		 On
                ShowWayptMarkers		 Off
                ShowWayptTurnMarkers		 Off
                ShowOrbits		 On
                ShowDtedRegions		 Off
                ShowAreaTgtCentroids		 On
                ShowToolBar		 On
                ShowStatusBar		 On
                ShowScrollBars		 On
                AllowAnimUpdate		 Off
                AccShowLine		 On
                AccAnimHigh		 On
                AccStatHigh		 On
                AccAnimLineLineWidth		  1.0000000000000000e+00
                AccAnimLineLineStyle		 0
                ShowPrintButton		 On
                ShowAnimButtons		 On
                ShowAnimModeButtons		 On
                ShowZoomMsrButtons		 On
                ShowMapCbButton		 Off
            END DisplayFlags

            BEGIN WinFonts

                System
                MS Sans Serif,16,0,0
                MS Sans Serif,20,0,0

            END WinFonts

            BEGIN MapData

                BEGIN TerrainConverterData
                    NorthLat		  0.0000000000000000e+00
                    EastLon		  0.0000000000000000e+00
                    SouthLat		  0.0000000000000000e+00
                    WestLon		  0.0000000000000000e+00
                    ColorByRGB		 No
                    AltsFromMSL		 No
                    UseColorRamp		 Yes
                    UseRegionMinMax		 Yes
                    SizeSameAsSrc		 Yes
                    MinAltHSV		  0.0000000000000000e+00  6.9999999999999996e-01  8.0000000000000004e-01  4.0000000000000002e-01
                    MaxAltHSV		  1.0000000000000000e+06  0.0000000000000000e+00  2.0000000000000001e-01  1.0000000000000000e+00
                    SmoothColors		 Yes
                    CreateChunkTrn		 No
                    OutputFormat		 PDTTX
                END TerrainConverterData

                DisableDefKbdActions		 Off
                TextShadowStyle		 None
                TextShadowColor		 #000000
                BingLevelOfDetailScale		 2
                BEGIN Map
                    MapNum		 1
                    TrackingMode		 LatLon
                    PickEnabled		 On
                    PanEnabled		 On

                    BEGIN MapAttributes
                        PrimaryBody		 Earth
                        SecondaryBody		 Sun
                        CenterLatitude		 0
                        CenterLongitude		 0
                        ProjectionAltitude		 63621860
                        FieldOfView		 35
                        OrthoDisplayDistance		 20000000
                        TransformTrajectory		 On
                        EquatorialRadius		 6378137
                        BackgroundColor		 #000000
                        LatLonLines		 On
                        LatSpacing		 30
                        LonSpacing		 30
                        LatLonLineColor		 #999999
                        LatLonLineStyle		 2
                        ShowOrthoDistGrid		 Off
                        OrthoGridXSpacing		 5
                        OrthoGridYSpacing		 5
                        OrthoGridColor		 #ffffff
                        ShowImageExtents		 Off
                        ImageExtentLineColor		 #ffffff
                        ImageExtentLineStyle		 0
                        ImageExtentLineWidth		 1
                        ShowImageNames		 Off
                        ImageNameFont		 0
                        Projection		 EquidistantCylindrical
                        Resolution		 VeryLow
                        CoordinateSys		 ECF
                        UseBackgroundImage		 On
                        UseBingForBackground		 Off
                        BingType		 Aerial
                        BingLogoHorizAlign		 Right
                        BingLogoVertAlign		 Bottom
                        BackgroundImageFile		 Basic.bmp
                        UseNightLights		 Off
                        NightLightsFactor		 3.5
                        UseCloudsFile		 Off
                        BEGIN ZoomLocations
                            BEGIN ZoomLocation
                                CenterLat		 0
                                CenterLon		 0
                                ZoomWidth		 359.999998
                                ZoomHeight		 180
                            END ZoomLocation
                        END ZoomLocations
                        UseVarAspectRatio		 No
                        SwapMapResolution		 Yes
                        NoneToVLowSwapDist		 2000000
                        VLowToLowSwapDist		 20000
                        LowToMediumSwapDist		 10000
                        MediumToHighSwapDist		 5000
                        HighToVHighSwapDist		 1000
                        VHighToSHighSwapDist		 100
                        BEGIN Axes
                            DisplayAxes		 no
                            CoordSys		 CBI
                            2aryCB		 Sun
                            Display+x		 yes
                            Label+x		 yes
                            Color+x		 #ffffff
                            Scale+x		 3
                            Display-x		 yes
                            Label-x		 yes
                            Color-x		 #ffffff
                            Scale-x		 3
                            Display+y		 yes
                            Label+y		 yes
                            Color+y		 #ffffff
                            Scale+y		 3
                            Display-y		 yes
                            Label-y		 yes
                            Color-y		 #ffffff
                            Scale-y		 3
                            Display+z		 yes
                            Label+z		 yes
                            Color+z		 #ffffff
                            Scale+z		 3
                            Display-z		 yes
                            Label-z		 yes
                            Color-z		 #ffffff
                            Scale-z		 3
                        END Axes

                    END MapAttributes

                    BEGIN MapList
                        BEGIN Detail
                            Alias		 RWDB2_Coastlines
                            Show		 Yes
                            Color		 #8fbc8f
                        END Detail
                        BEGIN Detail
                            Alias		 RWDB2_International_Borders
                            Show		 Yes
                            Color		 #8fbc8f
                        END Detail
                        BEGIN Detail
                            Alias		 RWDB2_Islands
                            Show		 Yes
                            Color		 #8fbc8f
                        END Detail
                        BEGIN Detail
                            Alias		 RWDB2_Lakes
                            Show		 No
                            Color		 #87cefa
                        END Detail
                        BEGIN Detail
                            Alias		 RWDB2_Provincial_Borders
                            Show		 No
                            Color		 #8fbc8f
                        END Detail
                        BEGIN Detail
                            Alias		 RWDB2_Rivers
                            Show		 No
                            Color		 #87cefa
                        END Detail
                    END MapList


                    BEGIN MapAnnotations
                    END MapAnnotations

                    BEGIN DisplayFlags
                        ShowLabels		 On
                        ShowPassLabel		 Off
                        ShowElsetNum		 Off
                        ShowGndTracks		 On
                        ShowGndMarkers		 On
                        ShowOrbitMarkers		 On
                        ShowPlanetOrbits		 Off
                        ShowPlanetCBIPos		 On
                        ShowPlanetCBILabel		 On
                        ShowPlanetGndPos		 On
                        ShowPlanetGndLabel		 On
                        ShowSensors		 On
                        ShowWayptMarkers		 Off
                        ShowWayptTurnMarkers		 Off
                        ShowOrbits		 On
                        ShowDtedRegions		 Off
                        ShowAreaTgtCentroids		 On
                        ShowToolBar		 On
                        ShowStatusBar		 On
                        ShowScrollBars		 On
                        AllowAnimUpdate		 Off
                        AccShowLine		 On
                        AccAnimHigh		 On
                        AccStatHigh		 On
                        AccAnimLineLineWidth		  1.0000000000000000e+00
                        AccAnimLineLineStyle		 0
                        ShowPrintButton		 On
                        ShowAnimButtons		 On
                        ShowAnimModeButtons		 On
                        ShowZoomMsrButtons		 On
                        ShowMapCbButton		 Off
                    END DisplayFlags

                    BEGIN RecordMovie
                        OutputFormat		 BMP
                        SdfSelected		 No
                        Directory		 C:\DOCUME~1\VDUBOV~1\LOCALS~1\Temp
                        BaseName		 Frame
                        Digits		 4
                        Frame		 0
                        LastAnimTime		 0
                        OutputMode		 Normal
                        HiResAssembly		 Assemble
                        HRWidth		 6000
                        HRHeight		 4500
                        HRDPI		 600
                        UseSnapInterval		 No
                        SnapInterval		 0
                        VideoCodec		 "H264"
                        Framerate		 30
                        Bitrate		 3000000
                    END RecordMovie


                    BEGIN TimeDisplay
                        Show		 0
                        TextColor		 #ffffff
                        TextTranslucency		 0
                        ShowBackground		 0
                        BackColor		 #4d4d4d
                        BackTranslucency		 0.4
                        XPosition		 20
                        YPosition		 -20
                    END TimeDisplay

                    BEGIN LightingData
                        DisplayAltitude		 0
                        SubsolarPoint		 Off
                        SubsolarPointColor		 #ffff00
                        SubsolarPointMarkerStyle		 2

                        ShowUmbraLine		 Off
                        UmbraLineColor		 #0000ff
                        UmbraLineStyle		 0
                        UmbraLineWidth		 2
                        FillUmbra		 Off
                        UmbraFillColor		 #0000ff
                        ShowSunlightLine		 Off
                        SunlightLineColor		 #ffff00
                        SunlightLineStyle		 0
                        SunlightLineWidth		 2
                        FillSunlight		 Off
                        SunlightFillColor		 #ffff00
                        SunlightMinOpacity		 0
                        SunlightMaxOpacity		 0.2
                        UmbraMaxOpacity		 0.7
                        UmbraMinOpacity		 0.4
                    END LightingData
                END Map

                BEGIN MapStyles

                    UseStyleTime		 No

                    BEGIN Style
                        Name		 No_Map_Bckgrnd
                        Time		 0
                        UpdateDelta		 60

                        BEGIN MapAttributes
                            PrimaryBody		 Earth
                            SecondaryBody		 Sun
                            CenterLatitude		 0
                            CenterLongitude		 0
                            ProjectionAltitude		 63621860
                            FieldOfView		 35
                            OrthoDisplayDistance		 20000000
                            TransformTrajectory		 On
                            EquatorialRadius		 6378137
                            BackgroundColor		 #000000
                            LatLonLines		 On
                            LatSpacing		 30
                            LonSpacing		 30
                            LatLonLineColor		 #999999
                            LatLonLineStyle		 2
                            ShowOrthoDistGrid		 Off
                            OrthoGridXSpacing		 5
                            OrthoGridYSpacing		 5
                            OrthoGridColor		 #ffffff
                            ShowImageExtents		 Off
                            ImageExtentLineColor		 #ffffff
                            ImageExtentLineStyle		 0
                            ImageExtentLineWidth		 1
                            ShowImageNames		 Off
                            ImageNameFont		 0
                            Projection		 EquidistantCylindrical
                            Resolution		 VeryLow
                            CoordinateSys		 ECF
                            UseBackgroundImage		 Off
                            UseBingForBackground		 Off
                            BingType		 Aerial
                            BingLogoHorizAlign		 Right
                            BingLogoVertAlign		 Bottom
                            UseNightLights		 Off
                            NightLightsFactor		 3.5
                            UseCloudsFile		 Off
                            BEGIN ZoomLocations
                                BEGIN ZoomLocation
                                    CenterLat		 0
                                    CenterLon		 0
                                    ZoomWidth		 359.999998
                                    ZoomHeight		 180
                                END ZoomLocation
                            END ZoomLocations
                            UseVarAspectRatio		 No
                            SwapMapResolution		 Yes
                            NoneToVLowSwapDist		 2000000
                            VLowToLowSwapDist		 20000
                            LowToMediumSwapDist		 10000
                            MediumToHighSwapDist		 5000
                            HighToVHighSwapDist		 1000
                            VHighToSHighSwapDist		 100
                            BEGIN Axes
                                DisplayAxes		 no
                                CoordSys		 CBI
                                2aryCB		 Sun
                                Display+x		 yes
                                Label+x		 yes
                                Color+x		 #ffffff
                                Scale+x		 3
                                Display-x		 yes
                                Label-x		 yes
                                Color-x		 #ffffff
                                Scale-x		 3
                                Display+y		 yes
                                Label+y		 yes
                                Color+y		 #ffffff
                                Scale+y		 3
                                Display-y		 yes
                                Label-y		 yes
                                Color-y		 #ffffff
                                Scale-y		 3
                                Display+z		 yes
                                Label+z		 yes
                                Color+z		 #ffffff
                                Scale+z		 3
                                Display-z		 yes
                                Label-z		 yes
                                Color-z		 #ffffff
                                Scale-z		 3
                            END Axes

                        END MapAttributes

                        BEGIN MapList
                            BEGIN Detail
                                Alias		 RWDB2_Coastlines
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_International_Borders
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Islands
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Lakes
                                Show		 Yes
                                Color		 #87cefa
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Provincial_Borders
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                        END MapList


                        BEGIN MapAnnotations
                        END MapAnnotations

                        BEGIN RecordMovie
                            OutputFormat		 BMP
                            SdfSelected		 No
                            Directory		 C:\DOCUME~1\MBARTH~1\LOCALS~1\Temp
                            BaseName		 Frame
                            Digits		 4
                            Frame		 0
                            LastAnimTime		 0
                            OutputMode		 Normal
                            HiResAssembly		 Assemble
                            HRWidth		 6000
                            HRHeight		 4500
                            HRDPI		 600
                            UseSnapInterval		 No
                            SnapInterval		 0
                            VideoCodec		 "H264"
                            Framerate		 30
                            Bitrate		 3000000
                        END RecordMovie


                        BEGIN TimeDisplay
                            Show		 0
                            TextColor		 #00ffff
                            TextTranslucency		 0
                            ShowBackground		 0
                            BackColor		 #000000
                            BackTranslucency		 0
                            XPosition		 20
                            YPosition		 -20
                        END TimeDisplay

                        BEGIN LightingData
                            DisplayAltitude		 0
                            SubsolarPoint		 Off
                            SubsolarPointColor		 #ffff00
                            SubsolarPointMarkerStyle		 2

                            ShowUmbraLine		 Off
                            UmbraLineColor		 #ffff00
                            UmbraLineStyle		 0
                            UmbraLineWidth		 1
                            FillUmbra		 Off
                            UmbraFillColor		 #000000
                            ShowSunlightLine		 Off
                            SunlightLineColor		 #ffff00
                            SunlightLineStyle		 0
                            SunlightLineWidth		 1
                            FillSunlight		 Off
                            SunlightFillColor		 #ffff00
                            SunlightMinOpacity		 0.1
                            SunlightMaxOpacity		 0.5
                            UmbraMaxOpacity		 0.5
                            UmbraMinOpacity		 0.2
                        END LightingData

                        ShowDtedRegions		 Off

                    END Style

                    BEGIN Style
                        Name		 Basic_Map_Bckgrnd
                        Time		 0
                        UpdateDelta		 60

                        BEGIN MapAttributes
                            PrimaryBody		 Earth
                            SecondaryBody		 Sun
                            CenterLatitude		 0
                            CenterLongitude		 0
                            ProjectionAltitude		 63621860
                            FieldOfView		 35
                            OrthoDisplayDistance		 20000000
                            TransformTrajectory		 On
                            EquatorialRadius		 6378137
                            BackgroundColor		 #000000
                            LatLonLines		 On
                            LatSpacing		 30
                            LonSpacing		 30
                            LatLonLineColor		 #999999
                            LatLonLineStyle		 2
                            ShowOrthoDistGrid		 Off
                            OrthoGridXSpacing		 5
                            OrthoGridYSpacing		 5
                            OrthoGridColor		 #ffffff
                            ShowImageExtents		 Off
                            ImageExtentLineColor		 #ffffff
                            ImageExtentLineStyle		 0
                            ImageExtentLineWidth		 1
                            ShowImageNames		 Off
                            ImageNameFont		 0
                            Projection		 EquidistantCylindrical
                            Resolution		 VeryLow
                            CoordinateSys		 ECF
                            UseBackgroundImage		 On
                            UseBingForBackground		 Off
                            BingType		 Aerial
                            BingLogoHorizAlign		 Right
                            BingLogoVertAlign		 Bottom
                            BackgroundImageFile		 Basic.bmp
                            UseNightLights		 Off
                            NightLightsFactor		 3.5
                            UseCloudsFile		 Off
                            BEGIN ZoomLocations
                                BEGIN ZoomLocation
                                    CenterLat		 0
                                    CenterLon		 0
                                    ZoomWidth		 359.999998
                                    ZoomHeight		 180
                                END ZoomLocation
                            END ZoomLocations
                            UseVarAspectRatio		 No
                            SwapMapResolution		 Yes
                            NoneToVLowSwapDist		 2000000
                            VLowToLowSwapDist		 20000
                            LowToMediumSwapDist		 10000
                            MediumToHighSwapDist		 5000
                            HighToVHighSwapDist		 1000
                            VHighToSHighSwapDist		 100
                            BEGIN Axes
                                DisplayAxes		 no
                                CoordSys		 CBI
                                2aryCB		 Sun
                                Display+x		 yes
                                Label+x		 yes
                                Color+x		 #ffffff
                                Scale+x		 3
                                Display-x		 yes
                                Label-x		 yes
                                Color-x		 #ffffff
                                Scale-x		 3
                                Display+y		 yes
                                Label+y		 yes
                                Color+y		 #ffffff
                                Scale+y		 3
                                Display-y		 yes
                                Label-y		 yes
                                Color-y		 #ffffff
                                Scale-y		 3
                                Display+z		 yes
                                Label+z		 yes
                                Color+z		 #ffffff
                                Scale+z		 3
                                Display-z		 yes
                                Label-z		 yes
                                Color-z		 #ffffff
                                Scale-z		 3
                            END Axes

                        END MapAttributes

                        BEGIN MapList
                            BEGIN Detail
                                Alias		 RWDB2_Coastlines
                                Show		 Yes
                                Color		 #8fbc8f
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_International_Borders
                                Show		 Yes
                                Color		 #8fbc8f
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Islands
                                Show		 Yes
                                Color		 #8fbc8f
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Lakes
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Provincial_Borders
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                        END MapList


                        BEGIN MapAnnotations
                        END MapAnnotations

                        BEGIN RecordMovie
                            OutputFormat		 BMP
                            SdfSelected		 No
                            Directory		 C:\DOCUME~1\MBARTH~1\LOCALS~1\Temp
                            BaseName		 Frame
                            Digits		 4
                            Frame		 0
                            LastAnimTime		 0
                            OutputMode		 Normal
                            HiResAssembly		 Assemble
                            HRWidth		 6000
                            HRHeight		 4500
                            HRDPI		 600
                            UseSnapInterval		 No
                            SnapInterval		 0
                            VideoCodec		 "H264"
                            Framerate		 30
                            Bitrate		 3000000
                        END RecordMovie


                        BEGIN TimeDisplay
                            Show		 0
                            TextColor		 #00ffff
                            TextTranslucency		 0
                            ShowBackground		 0
                            BackColor		 #000000
                            BackTranslucency		 0
                            XPosition		 20
                            YPosition		 -20
                        END TimeDisplay

                        BEGIN LightingData
                            DisplayAltitude		 0
                            SubsolarPoint		 Off
                            SubsolarPointColor		 #ffff00
                            SubsolarPointMarkerStyle		 2

                            ShowUmbraLine		 Off
                            UmbraLineColor		 #ffff00
                            UmbraLineStyle		 0
                            UmbraLineWidth		 1
                            FillUmbra		 Off
                            UmbraFillColor		 #000000
                            ShowSunlightLine		 Off
                            SunlightLineColor		 #ffff00
                            SunlightLineStyle		 0
                            SunlightLineWidth		 1
                            FillSunlight		 Off
                            SunlightFillColor		 #ffff00
                            SunlightMinOpacity		 0.1
                            SunlightMaxOpacity		 0.5
                            UmbraMaxOpacity		 0.5
                            UmbraMinOpacity		 0.2
                        END LightingData

                        ShowDtedRegions		 Off

                    END Style

                    BEGIN Style
                        Name		 Orthographic_Projection
                        Time		 0
                        UpdateDelta		 60

                        BEGIN MapAttributes
                            PrimaryBody		 Earth
                            SecondaryBody		 Sun
                            CenterLatitude		 0
                            CenterLongitude		 0
                            ProjectionAltitude		 63621860
                            FieldOfView		 35
                            OrthoDisplayDistance		 20000000
                            TransformTrajectory		 On
                            EquatorialRadius		 6378137
                            BackgroundColor		 #000000
                            LatLonLines		 On
                            LatSpacing		 30
                            LonSpacing		 30
                            LatLonLineColor		 #999999
                            LatLonLineStyle		 2
                            ShowOrthoDistGrid		 Off
                            OrthoGridXSpacing		 5
                            OrthoGridYSpacing		 5
                            OrthoGridColor		 #ffffff
                            ShowImageExtents		 Off
                            ImageExtentLineColor		 #ffffff
                            ImageExtentLineStyle		 0
                            ImageExtentLineWidth		 1
                            ShowImageNames		 Off
                            ImageNameFont		 0
                            Projection		 Orthographic
                            Resolution		 VeryLow
                            CoordinateSys		 ECF
                            UseBackgroundImage		 Off
                            UseBingForBackground		 Off
                            BingType		 Aerial
                            BingLogoHorizAlign		 Right
                            BingLogoVertAlign		 Bottom
                            UseNightLights		 Off
                            NightLightsFactor		 3.5
                            UseCloudsFile		 Off
                            BEGIN ZoomLocations
                                BEGIN ZoomLocation
                                    CenterLat		 0
                                    CenterLon		 0
                                    ZoomWidth		 359.99999
                                    ZoomHeight		 180
                                END ZoomLocation
                            END ZoomLocations
                            UseVarAspectRatio		 No
                            SwapMapResolution		 Yes
                            NoneToVLowSwapDist		 2000000
                            VLowToLowSwapDist		 20000
                            LowToMediumSwapDist		 10000
                            MediumToHighSwapDist		 5000
                            HighToVHighSwapDist		 1000
                            VHighToSHighSwapDist		 100
                            BEGIN Axes
                                DisplayAxes		 no
                                CoordSys		 CBI
                                2aryCB		 Sun
                                Display+x		 yes
                                Label+x		 yes
                                Color+x		 #ffffff
                                Scale+x		 3
                                Display-x		 yes
                                Label-x		 yes
                                Color-x		 #ffffff
                                Scale-x		 3
                                Display+y		 yes
                                Label+y		 yes
                                Color+y		 #ffffff
                                Scale+y		 3
                                Display-y		 yes
                                Label-y		 yes
                                Color-y		 #ffffff
                                Scale-y		 3
                                Display+z		 yes
                                Label+z		 yes
                                Color+z		 #ffffff
                                Scale+z		 3
                                Display-z		 yes
                                Label-z		 yes
                                Color-z		 #ffffff
                                Scale-z		 3
                            END Axes

                        END MapAttributes

                        BEGIN MapList
                            BEGIN Detail
                                Alias		 RWDB2_Coastlines
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_International_Borders
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Islands
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Lakes
                                Show		 Yes
                                Color		 #87cefa
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Provincial_Borders
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                        END MapList


                        BEGIN MapAnnotations
                        END MapAnnotations

                        BEGIN RecordMovie
                            OutputFormat		 BMP
                            SdfSelected		 No
                            Directory		 C:\DOCUME~1\MBARTH~1\LOCALS~1\Temp
                            BaseName		 Frame
                            Digits		 4
                            Frame		 0
                            LastAnimTime		 0
                            OutputMode		 Normal
                            HiResAssembly		 Assemble
                            HRWidth		 6000
                            HRHeight		 4500
                            HRDPI		 600
                            UseSnapInterval		 No
                            SnapInterval		 0
                            VideoCodec		 "H264"
                            Framerate		 30
                            Bitrate		 3000000
                        END RecordMovie


                        BEGIN TimeDisplay
                            Show		 0
                            TextColor		 #00ffff
                            TextTranslucency		 0
                            ShowBackground		 0
                            BackColor		 #000000
                            BackTranslucency		 0
                            XPosition		 20
                            YPosition		 -20
                        END TimeDisplay

                        BEGIN LightingData
                            DisplayAltitude		 0
                            SubsolarPoint		 Off
                            SubsolarPointColor		 #ffff00
                            SubsolarPointMarkerStyle		 2

                            ShowUmbraLine		 Off
                            UmbraLineColor		 #ffff00
                            UmbraLineStyle		 0
                            UmbraLineWidth		 1
                            FillUmbra		 Off
                            UmbraFillColor		 #000000
                            ShowSunlightLine		 Off
                            SunlightLineColor		 #ffff00
                            SunlightLineStyle		 0
                            SunlightLineWidth		 1
                            FillSunlight		 Off
                            SunlightFillColor		 #ffff00
                            SunlightMinOpacity		 0.1
                            SunlightMaxOpacity		 0.5
                            UmbraMaxOpacity		 0.5
                            UmbraMinOpacity		 0.2
                        END LightingData

                        ShowDtedRegions		 Off

                    END Style

                    BEGIN Style
                        Name		 Zoom_North_America
                        Time		 0
                        UpdateDelta		 60

                        BEGIN MapAttributes
                            PrimaryBody		 Earth
                            SecondaryBody		 Sun
                            CenterLatitude		 0
                            CenterLongitude		 0
                            ProjectionAltitude		 63621860
                            FieldOfView		 35
                            OrthoDisplayDistance		 20000000
                            TransformTrajectory		 On
                            EquatorialRadius		 6378137
                            BackgroundColor		 #000000
                            LatLonLines		 On
                            LatSpacing		 30
                            LonSpacing		 30
                            LatLonLineColor		 #999999
                            LatLonLineStyle		 2
                            ShowOrthoDistGrid		 Off
                            OrthoGridXSpacing		 5
                            OrthoGridYSpacing		 5
                            OrthoGridColor		 #ffffff
                            ShowImageExtents		 Off
                            ImageExtentLineColor		 #ffffff
                            ImageExtentLineStyle		 0
                            ImageExtentLineWidth		 1
                            ShowImageNames		 Off
                            ImageNameFont		 0
                            Projection		 EquidistantCylindrical
                            Resolution		 Low
                            CoordinateSys		 ECF
                            UseBackgroundImage		 On
                            UseBingForBackground		 Off
                            BingType		 Aerial
                            BingLogoHorizAlign		 Right
                            BingLogoVertAlign		 Bottom
                            BackgroundImageFile		 Basic.bmp
                            UseNightLights		 Off
                            NightLightsFactor		 3.5
                            UseCloudsFile		 Off
                            BEGIN ZoomLocations
                                BEGIN ZoomLocation
                                    CenterLat		 0
                                    CenterLon		 0
                                    ZoomWidth		 359.999998
                                    ZoomHeight		 180
                                END ZoomLocation
                                BEGIN ZoomLocation
                                    CenterLat		 48.235294
                                    CenterLon		 -106.2295075
                                    ZoomWidth		 129.836065
                                    ZoomHeight		 64.918032
                                END ZoomLocation
                            END ZoomLocations
                            UseVarAspectRatio		 No
                            SwapMapResolution		 Yes
                            NoneToVLowSwapDist		 2000000
                            VLowToLowSwapDist		 20000
                            LowToMediumSwapDist		 10000
                            MediumToHighSwapDist		 5000
                            HighToVHighSwapDist		 1000
                            VHighToSHighSwapDist		 100
                            BEGIN Axes
                                DisplayAxes		 no
                                CoordSys		 CBI
                                2aryCB		 Sun
                                Display+x		 yes
                                Label+x		 yes
                                Color+x		 #ffffff
                                Scale+x		 3
                                Display-x		 yes
                                Label-x		 yes
                                Color-x		 #ffffff
                                Scale-x		 3
                                Display+y		 yes
                                Label+y		 yes
                                Color+y		 #ffffff
                                Scale+y		 3
                                Display-y		 yes
                                Label-y		 yes
                                Color-y		 #ffffff
                                Scale-y		 3
                                Display+z		 yes
                                Label+z		 yes
                                Color+z		 #ffffff
                                Scale+z		 3
                                Display-z		 yes
                                Label-z		 yes
                                Color-z		 #ffffff
                                Scale-z		 3
                            END Axes

                        END MapAttributes

                        BEGIN MapList
                            BEGIN Detail
                                Alias		 RWDB2_Coastlines
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_International_Borders
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Islands
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Lakes
                                Show		 Yes
                                Color		 #87cefa
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Provincial_Borders
                                Show		 Yes
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                        END MapList


                        BEGIN MapAnnotations
                        END MapAnnotations

                        BEGIN RecordMovie
                            OutputFormat		 BMP
                            SdfSelected		 No
                            Directory		 C:\DOCUME~1\MBARTH~1\LOCALS~1\Temp
                            BaseName		 Frame
                            Digits		 4
                            Frame		 0
                            LastAnimTime		 0
                            OutputMode		 Normal
                            HiResAssembly		 Assemble
                            HRWidth		 6000
                            HRHeight		 4500
                            HRDPI		 600
                            UseSnapInterval		 No
                            SnapInterval		 0
                            VideoCodec		 "H264"
                            Framerate		 30
                            Bitrate		 3000000
                        END RecordMovie


                        BEGIN TimeDisplay
                            Show		 0
                            TextColor		 #00ffff
                            TextTranslucency		 0
                            ShowBackground		 0
                            BackColor		 #000000
                            BackTranslucency		 0
                            XPosition		 20
                            YPosition		 -20
                        END TimeDisplay

                        BEGIN LightingData
                            DisplayAltitude		 0
                            SubsolarPoint		 Off
                            SubsolarPointColor		 #ffff00
                            SubsolarPointMarkerStyle		 2

                            ShowUmbraLine		 Off
                            UmbraLineColor		 #ffff00
                            UmbraLineStyle		 0
                            UmbraLineWidth		 1
                            FillUmbra		 Off
                            UmbraFillColor		 #000000
                            ShowSunlightLine		 Off
                            SunlightLineColor		 #ffff00
                            SunlightLineStyle		 0
                            SunlightLineWidth		 1
                            FillSunlight		 Off
                            SunlightFillColor		 #ffff00
                            SunlightMinOpacity		 0.1
                            SunlightMaxOpacity		 0.5
                            UmbraMaxOpacity		 0.5
                            UmbraMinOpacity		 0.2
                        END LightingData

                        ShowDtedRegions		 Off

                    END Style

                END MapStyles

            END MapData

            BEGIN GfxClassPref

            END GfxClassPref


            BEGIN ConnectGraphicsOptions

                AsyncPickReturnUnique		 OFF

            END ConnectGraphicsOptions

        END Graphics

        BEGIN Overlays
        END Overlays

        BEGIN VO
        END VO

    END Extensions

    BEGIN SubObjects

        Class AreaTarget

            AreaTarget1		

        END Class

        Class Chain

            Chain1		

        END Class

        Class Constellation

            SatRcvrs		
            SatXmtrs		

        END Class

        Class Facility

            Facility1		

        END Class

        Class Place

            Place1		
            Place2		

        END Class

        Class Satellite

            Satellite1		
            Satellite2		
            Satellite3		
            Satellite4		
            TemplateSatellite1		

        END Class

        Class SatelliteCollection

            SatelliteCollection1		

        END Class

    END SubObjects

    BEGIN References
        Instance *
            *		
            Chain/Chain1		
            Constellation/SatRcvrs		
            Constellation/SatXmtrs		
        END Instance
        Instance AreaTarget/AreaTarget1
            AreaTarget/AreaTarget1		
        END Instance
        Instance Chain/Chain1
            Chain/Chain1		
        END Instance
        Instance Constellation/SatRcvrs
        END Instance
        Instance Constellation/SatXmtrs
        END Instance
        Instance Facility/Facility1
            Facility/Facility1		
            Facility/Facility1/Sensor/Sensor1		
        END Instance
        Instance Facility/Facility1/Sensor/Sensor1
            Facility/Facility1/Sensor/Sensor1		
        END Instance
        Instance Place/Place1
            Place/Place1		
            Place/Place1/Transmitter/Transmitter1		
        END Instance
        Instance Place/Place1/Transmitter/Transmitter1
            Place/Place1/Transmitter/Transmitter1		
        END Instance
        Instance Place/Place2
            Place/Place2		
            Place/Place2/Receiver/Receiver1		
        END Instance
        Instance Place/Place2/Receiver/Receiver1
            Place/Place2/Receiver/Receiver1		
        END Instance
        Instance Satellite/Satellite1
            Satellite/Satellite1		
            Satellite/Satellite1/Sensor/Sensor2		
        END Instance
        Instance Satellite/Satellite1/Sensor/Sensor2
            Satellite/Satellite1/Sensor/Sensor2		
        END Instance
        Instance Satellite/Satellite2
            Satellite/Satellite2		
            Satellite/Satellite2/Receiver/Receiver2		
            Satellite/Satellite2/Transmitter/Transmitter2		
        END Instance
        Instance Satellite/Satellite2/Receiver/Receiver2
            Constellation/SatRcvrs		
            Satellite/Satellite2/Receiver/Receiver2		
        END Instance
        Instance Satellite/Satellite2/Transmitter/Transmitter2
            Constellation/SatXmtrs		
            Satellite/Satellite2/Transmitter/Transmitter2		
        END Instance
        Instance Satellite/Satellite3
            Satellite/Satellite3		
            Satellite/Satellite3/Receiver/Receiver3		
            Satellite/Satellite3/Transmitter/Transmitter3		
        END Instance
        Instance Satellite/Satellite3/Receiver/Receiver3
            Constellation/SatRcvrs		
            Satellite/Satellite3/Receiver/Receiver3		
        END Instance
        Instance Satellite/Satellite3/Transmitter/Transmitter3
            Constellation/SatXmtrs		
            Satellite/Satellite3/Transmitter/Transmitter3		
        END Instance
        Instance Satellite/Satellite4
            Satellite/Satellite4		
            Satellite/Satellite4/Receiver/Receiver4		
            Satellite/Satellite4/Transmitter/Transmitter4		
        END Instance
        Instance Satellite/Satellite4/Receiver/Receiver4
            Constellation/SatRcvrs		
            Satellite/Satellite4/Receiver/Receiver4		
        END Instance
        Instance Satellite/Satellite4/Transmitter/Transmitter4
            Constellation/SatXmtrs		
            Satellite/Satellite4/Transmitter/Transmitter4		
        END Instance
        Instance Satellite/TemplateSatellite1
            Satellite/TemplateSatellite1		
            Satellite/TemplateSatellite1/Receiver/TemplateReceiver		
            Satellite/TemplateSatellite1/Transmitter/TemplateTransmitter		
            SatelliteCollection/SatelliteCollection1		
        END Instance
        Instance Satellite/TemplateSatellite1/Receiver/TemplateReceiver
            Satellite/TemplateSatellite1/Receiver/TemplateReceiver		
            SatelliteCollection/SatelliteCollection1		
        END Instance
        Instance Satellite/TemplateSatellite1/Transmitter/TemplateTransmitter
            Satellite/TemplateSatellite1/Transmitter/TemplateTransmitter		
            SatelliteCollection/SatelliteCollection1		
        END Instance
        Instance SatelliteCollection/SatelliteCollection1
            SatelliteCollection/SatelliteCollection1		
            SatelliteCollection/SatelliteCollection1/Subset/AllReceivers		
            SatelliteCollection/SatelliteCollection1/Subset/AllSatellites		
            SatelliteCollection/SatelliteCollection1/Subset/AllTransmitters		
            SatelliteCollection/SatelliteCollection1/Subset/Plane_1		
            SatelliteCollection/SatelliteCollection1/Subset/Plane_2		
            SatelliteCollection/SatelliteCollection1/Subset/Shell_1		
        END Instance
        Instance SatelliteCollection/SatelliteCollection1/Subset/AllReceivers
            SatelliteCollection/SatelliteCollection1		
        END Instance
        Instance SatelliteCollection/SatelliteCollection1/Subset/AllSatellites
            SatelliteCollection/SatelliteCollection1		
        END Instance
        Instance SatelliteCollection/SatelliteCollection1/Subset/AllTransmitters
            SatelliteCollection/SatelliteCollection1		
        END Instance
        Instance SatelliteCollection/SatelliteCollection1/Subset/Plane_1
            SatelliteCollection/SatelliteCollection1		
        END Instance
        Instance SatelliteCollection/SatelliteCollection1/Subset/Plane_2
            SatelliteCollection/SatelliteCollection1		
        END Instance
        Instance SatelliteCollection/SatelliteCollection1/Subset/Shell_1
            SatelliteCollection/SatelliteCollection1		
        END Instance
    END References

END Scenario
