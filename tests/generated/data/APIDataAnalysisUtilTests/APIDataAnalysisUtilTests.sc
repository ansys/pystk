stk.v.12.0
WrittenBy    STK_v12.5.0
BEGIN Scenario
    Name		 APIDataAnalysisUtilTests

    BEGIN Epoch

        Epoch		 1 Jul 2020 16:00:00.000000000
        SmartEpoch		
        BEGIN EVENT
            Epoch		 1 Jul 2020 16:00:00.000000000
            EventEpoch		
            BEGIN EVENT
                Type		 EVENT_LINKTO
                Name		 AnalysisStartTime
            END EVENT
            EpochState		 Implicit
        END EVENT


    END Epoch

    BEGIN Interval

        Start		 1 Jul 2020 16:00:00.000000000
        Stop		 2 Jul 2020 16:00:00.000000000
        SmartInterval		
        BEGIN EVENTINTERVAL
            BEGIN Interval
                Start		 1 Jul 2020 16:00:00.000000000
                Stop		 2 Jul 2020 16:00:00.000000000
            END Interval
            IntervalState		 Explicit
        END EVENTINTERVAL

        EpochUsesAnalStart		 No
        AnimStartUsesAnalStart		 Yes
        AnimStopUsesAnalStop		 Yes

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
                StreamingTerrainServerName		 assets.agi.com/stk-terrain/
                StreamingTerrainAzimuthElevationMaskEnabled		 No
                StreamingTerrainObscurationEnabled		 No
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
        Module		 stk_mission_space
        Module		 stk_snopt
    END ScenarioLicenses

    BEGIN QuickReports

        BEGIN Report
            Name		 Percent Satisfied
            Type		 Report
            BaseDir		 Install
            Style		 Percent Satisfied
            AGIViewer		 Yes
            Instance		 CoverageDefinition/World_Coverage/FigureOfMerit/Simple_Coverage
            BEGIN TimeData
                BEGIN Section
                    SectionNumber		 1
                    SectionType		 1
                    ShowIntervals		 No
                    BEGIN IntervalList

                        DateUnitAbrv		 UTCG

                        BEGIN Intervals

"1 Jul 2020 16:00:00.000000000" "1 Jul 2020 16:00:00.000000000"
                        END Intervals

                    END IntervalList

                    TimeType		 Interval
                    SamplingType		 Default
                    TimeBound		 0
                END Section
                BEGIN Section
                    SectionNumber		 2
                    SectionType		 1
                    ShowIntervals		 No
                    BEGIN IntervalList

                        DateUnitAbrv		 UTCG

                        BEGIN Intervals

"1 Jul 2020 16:00:00.000000000" "1 Jul 2020 16:00:00.000000000"
                        END Intervals

                    END IntervalList

                    TimeType		 Interval
                    SamplingType		 Default
                    TimeBound		 0
                END Section
                BEGIN Section
                    SectionNumber		 3
                    SectionType		 1
                    ShowIntervals		 No
                    BEGIN IntervalList

                        DateUnitAbrv		 UTCG

                        BEGIN Intervals

"1 Jul 2020 16:00:00.000000000" "1 Jul 2020 16:00:00.000000000"
                        END Intervals

                    END IntervalList

                    TimeType		 Interval
                    SamplingType		 Default
                    TimeBound		 0
                END Section
            END TimeData
            DisplayOnLoad		 No
            FrameType		 0
            DockCircleID		 0
            DockID		 0
            WindowRectLeft		 2845
            WindowRectTop		 1662
            WindowRectRight		 3044
            WindowRectBottom		 1709
        END Report

        BEGIN Report
            Name		 Grid Stats
            Type		 Report
            BaseDir		 Install
            Style		 Grid Stats
            AGIViewer		 Yes
            Instance		 CoverageDefinition/Country_Coverage/FigureOfMerit/Coverage_Time
            BEGIN TimeData
                BEGIN Section
                    SectionNumber		 1
                    SectionType		 1
                    ShowIntervals		 No
                    BEGIN IntervalList

                        DateUnitAbrv		 UTCG

                        BEGIN Intervals

"1 Jul 2020 16:00:00.000000000" "1 Jul 2020 16:00:00.000000000"
                        END Intervals

                    END IntervalList

                    TimeType		 Interval
                    SamplingType		 Default
                    TimeBound		 0
                END Section
                BEGIN Section
                    SectionNumber		 2
                    SectionType		 1
                    ShowIntervals		 No
                    BEGIN IntervalList

                        DateUnitAbrv		 UTCG

                        BEGIN Intervals

"1 Jul 2020 16:00:00.000000000" "1 Jul 2020 16:00:00.000000000"
                        END Intervals

                    END IntervalList

                    TimeType		 Interval
                    SamplingType		 Default
                    TimeBound		 0
                END Section
                BEGIN Section
                    SectionNumber		 3
                    SectionType		 1
                    ShowIntervals		 No
                    BEGIN IntervalList

                        DateUnitAbrv		 UTCG

                        BEGIN Intervals

"1 Jul 2020 16:00:00.000000000" "1 Jul 2020 16:00:00.000000000"
                        END Intervals

                    END IntervalList

                    TimeType		 Interval
                    SamplingType		 Default
                    TimeBound		 0
                END Section
            END TimeData
            DisplayOnLoad		 No
            FrameType		 0
            DockCircleID		 0
            DockID		 0
            WindowRectLeft		 2845
            WindowRectTop		 127
            WindowRectRight		 5085
            WindowRectBottom		 1188
        END Report
    END QuickReports

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
            LaunchWindowStart		 43981200
            LaunchWindowStop		 44067600
            LaunchMETOffset		 0
            LaunchWindowUseSecEphem		 No 
            LaunchWindowUseScenFolderForSecEphem		 Yes
            LaunchWindowUsePrimEphem		 No 
            LaunchWindowUseScenFolderForPrimEphem		 Yes
            LaunchWindowIntervalPtr		
            BEGIN EVENTINTERVAL
                BEGIN Interval
                    Start		 22 Nov 2021 17:00:00.000000000
                    Stop		 23 Nov 2021 17:00:00.000000000
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
            SpectralBandwidthUnit		 Hertz
            AviatorAltTimeUnit		 Minutes
            AviatorSmallTimeUnit		 Seconds
            AviatorEnergyUnit		 kilowatt-hours
            BitsUnit		 MegaBits
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
            SpectralBandwidthUnit		 Hertz
            AviatorAltTimeUnit		 Minutes
            AviatorSmallTimeUnit		 Seconds
            AviatorEnergyUnit		 kilowatt-hours
            BitsUnit		 MegaBits
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
            SpectralBandwidthUnit		 Hertz
            AviatorAltTimeUnit		 Minutes
            AviatorSmallTimeUnit		 Seconds
            AviatorEnergyUnit		 kilowatt-hours
            BitsUnit		 MegaBits
            MagneticFieldUnit		 nanoTesla
            VoltageUnit		 Volts
        END ConnectReportUnits

        BEGIN ReportFavorites
            BEGIN Class
                Name		 CoverageDefinition
                BEGIN Favorite
                    Type		 Graph
                    BaseDir		 Install
                    Style		 Coverage By Latitude
                END Favorite
            END Class
            BEGIN Class
                Name		 FigureOfMerit
                BEGIN Favorite
                    Type		 Report
                    BaseDir		 Install
                    Style		 Percent Satisfied
                END Favorite
                BEGIN Favorite
                    Type		 Report
                    BaseDir		 Install
                    Style		 Grid Stats
                END Favorite
            END Class
        END ReportFavorites

        BEGIN ADFFileData
        END ADFFileData

        BEGIN GenDb

            BEGIN Database
                DbType		 Satellite
                DefDb		 stkAllTLE.sd
                UseMyDb		 Off
                MaxMatches		 2000
                Use4SOC		 On

                BEGIN FieldDefaults

                    BEGIN Field
                        Name		 "SSC Number"
                        Default		 "*"
                    END Field

                    BEGIN Field
                        Name		 "Common Name"
                        Default		 "*"
                    END Field

                END FieldDefaults

            END Database

            BEGIN Database
                DbType		 City
                DefDb		 stkCityDb.cd
                UseMyDb		 Off
                MaxMatches		 2000
                Use4SOC		 On

                BEGIN FieldDefaults

                    BEGIN Field
                        Name		 "City Name"
                        Default		 "*"
                    END Field

                END FieldDefaults

            END Database

            BEGIN Database
                DbType		 Facility
                DefDb		 stkFacility.fd
                UseMyDb		 Off
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
            Optimize		 No
            UseBasicGlobe		 No
            SaveEphemeris		 Yes
            SaveScenFolder		 No
            BEGIN ExternalFileTypes
                BEGIN Type
                    FileType		 Calculation Scalar
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Celestial Image
                    Include		 No
                END Type
                BEGIN Type
                    FileType		 Cloud
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Component Supporting File
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 EOIR Texture Map File
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 EOP
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 External Vector Data
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Globe
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Globe Data
                    Include		 No
                END Type
                BEGIN Type
                    FileType		 Map
                    Include		 No
                END Type
                BEGIN Type
                    FileType		 Map Image
                    Include		 No
                END Type
                BEGIN Type
                    FileType		 Marker/Label
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Model
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Object Break-up File
                    Include		 No
                END Type
                BEGIN Type
                    FileType		 Planetary Ephemeris
                    Include		 No
                END Type
                BEGIN Type
                    FileType		 Python Script
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Report Style Script
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Report/Graph Style
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Scalar Calculation File
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Terrain
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Volume Grid Intervals File
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 Volumetric File
                    Include		 Yes
                END Type
                BEGIN Type
                    FileType		 WTM
                    Include		 Yes
                END Type
            END ExternalFileTypes
            ReadOnly		 No
            ViewerPassword		 No
            STKPassword		 No
            ExcludeInstallFiles		 No
            BEGIN ExternalFileList
            END ExternalFileList
        END Author

        BEGIN ExportDataFile
            FileType		 Ephemeris
            IntervalType		 Ephemeris
            TimePeriodStart		 0
            TimePeriodStop		 0
            StepType		 Ephemeris
            StepSize		 60
            EphemType		 STK
            UseVehicleCentralBody		 Yes
            CentralBody		 Earth
            SatelliteID		 -200000
            CoordSys		 ICRF
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
                                                <STRING>&quot;{BA37DFAD-00B0-4889-9730-A98955670661}&quot;</STRING>
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
                                                <STRING>&quot;{BF4B3541-791B-4580-AFD0-28E70F920336}&quot;</STRING>
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
                                    <VAR name = "ComputeDeepFade">
                                        <BOOL>false</BOOL>
                                    </VAR>
                                    <VAR name = "FadeOutage">
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
                                                <STRING>&quot;{B027A240-56C8-4673-AF6B-F6C1FAC0403F}&quot;</STRING>
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
                                        <STRING>
                                            <PROP name = "FullName">
                                                <STRING>&quot;&quot;</STRING>
                                            </PROP>&quot;&quot;</STRING>
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
                <VAR name = "ITU-R_P618-12">
                    <SCOPE Class = "LinkEmbedControl">
                        <VAR name = "ReferenceType">
                            <STRING>&quot;Unlinked&quot;</STRING>
                        </VAR>
                        <VAR name = "Component">
                            <VAR name = "ITU-R_P618-12">
                                <SCOPE Class = "RainLossModel">
                                    <VAR name = "Version">
                                        <STRING>&quot;1.0.0 a&quot;</STRING>
                                    </VAR>
                                    <VAR name = "IdentifierInformation">
                                        <SCOPE>
                                            <VAR name = "Identifier">
                                                <STRING>&quot;{30CE4EC6-FF9E-45B7-8359-2B1EDB5FAA30}&quot;</STRING>
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
                                                        <STRING>&quot;{1113D770-D1E5-4DEF-99A3-6B3F4D5CE16A}&quot;</STRING>
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
                                        <STRING>&quot;ITU-R P618-12 rain model&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Type">
                                        <STRING>&quot;ITU-R P618-12&quot;</STRING>
                                    </VAR>
                                    <VAR name = "UserComment">
                                        <STRING>&quot;ITU-R P618-12 rain model&quot;</STRING>
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
                <VAR name = "ITU-R_P676-9">
                    <SCOPE Class = "LinkEmbedControl">
                        <VAR name = "ReferenceType">
                            <STRING>&quot;Unlinked&quot;</STRING>
                        </VAR>
                        <VAR name = "Component">
                            <VAR name = "ITU-R_P676-9">
                                <SCOPE Class = "AtmosphericAbsorptionModel">
                                    <VAR name = "Version">
                                        <STRING>&quot;1.0.1 a&quot;</STRING>
                                    </VAR>
                                    <VAR name = "IdentifierInformation">
                                        <SCOPE>
                                            <VAR name = "Identifier">
                                                <STRING>&quot;{EEC3BB1C-1D9C-4A68-A850-308140DBB60F}&quot;</STRING>
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
                                                        <STRING>&quot;{5DBDF434-D4CA-44F6-8097-A6EBF681200D}&quot;</STRING>
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
                                        <STRING>&quot;ITU-R_P676-9&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Description">
                                        <STRING>&quot;ITU-R P676-9 gaseous absorption model&quot;</STRING>
                                    </VAR>
                                    <VAR name = "Type">
                                        <STRING>&quot;ITU-R P676-9&quot;</STRING>
                                    </VAR>
                                    <VAR name = "UserComment">
                                        <STRING>&quot;ITU-R P676-9 gaseous absorption model&quot;</STRING>
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
                                    <VAR name = "UseApproxMethod">
                                        <BOOL>true</BOOL>
                                    </VAR>
                                    <VAR name = "UseSeasonalRegional">
                                        <BOOL>true</BOOL>
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
                                                <STRING>&quot;{63DCFD85-5867-49A0-8147-12CE7DFC5829}&quot;</STRING>
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
                                                <STRING>&quot;{3608D72A-102C-4005-A192-254D14CE77EC}&quot;</STRING>
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
                                                <STRING>&quot;{8F8FC74F-A565-4A62-8D48-1BF7E7B52DBE}&quot;</STRING>
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
                                        <STRING>&quot;{CCC6D057-69D3-4A64-ABE7-EF769C56A6F6}&quot;</STRING>
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
                                </LIST>
                            </VAR>
                        </SCOPE>
                    </VAR>
                </VAR>
            </SCOPE>
        </VAR>
    </VAR>
</SCOPE>        END RadarCrossSection

        BEGIN RadarClutter
<?xml version = "1.0" standalone = "yes"?>
<SCOPE>
    <VAR name = "ClutterMap">
        <VAR name = "Constant Coefficient">
            <SCOPE Class = "Clutter Map">
                <VAR name = "ClutterCoefficient">
                    <QUANTITY Dimension = "RatioUnit" Unit = "units">
                        <REAL>1</REAL>
                    </QUANTITY>
                </VAR>
                <VAR name = "Type">
                    <STRING>&quot;Constant Coefficient&quot;</STRING>
                </VAR>
                <VAR name = "ComponentName">
                    <STRING>&quot;Constant Coefficient&quot;</STRING>
                </VAR>
            </SCOPE>
        </VAR>
    </VAR>
</SCOPE>        END RadarClutter

        BEGIN Gator
            RPOComponentsLoaded		 False
        END Gator

        BEGIN Crdn
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

                StartTime		 1 Jul 2020 16:00:00.000000000
                EndTime		 2 Jul 2020 16:00:00.000000000
                CurrentTime		 1 Jul 2020 16:00:00.000000000
                Direction		 Forward
                UpdateDelta		 10
                RefreshDelta		 0.010000
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
                AllowAnimUpdate		 On
                AccShowLine		 On
                AccAnimHigh		 On
                AccStatHigh		 On
                AccAnimLineLineWidth		  1.0000000000000000e+00
                ShowPrintButton		 On
                ShowAnimButtons		 On
                ShowAnimModeButtons		 On
                ShowZoomMsrButtons		 On
                ShowMapCbButton		 Off
            END DisplayFlags

            BEGIN WinFonts

                Consolas,12,700,0
                Consolas,14,700,0
                Consolas,16,700,0

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
                TextShadowStyle		 Dark
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
                        CenterLongitude		 -92.89563498754302
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
                                CenterLon		 -92.89563498754302
                                ZoomWidth		 132.2076458752515
                                ZoomHeight		 145.8
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
                            BEGIN Detail
                                Alias		 Coastlines
                                Show		 Yes
                                Color		 #8fbc8f
                            END Detail
                            BEGIN Detail
                                Alias		 Major_Ice_Shelves
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Minor_Ice_Shelves
                                Show		 No
                                Color		 #00ff00
                            END Detail
                        END Detail
                        BEGIN Detail
                            Alias		 RWDB2_International_Borders
                            Show		 No
                            Color		 #8fbc8f
                            BEGIN Detail
                                Alias		 Demarcated_or_Delimited
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Indefinite_or_Disputed
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Lines_of_separation_on_land
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Lines_of_separation_at_sea
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Other_lines_of_separation_at_sea
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Continental_shelf_boundary_in_Persian_Gulf
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Demilitarized_zone_lines_in_Israel
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 No_defined_line
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Selected_claimed_lines
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Old_Panama_Canal_Zone_lines
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Old_North-South_Yemen_lines
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Old_Jordan-Iraq_lines
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Old_Iraq-Saudi_Arabia_Neutral_Zone_lines
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Old_East-West_Germany_and_Berlin_lines
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Old_North-South_Vietnam_boundary
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Old_Vietnam_DMZ_lines
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Old_Oman-Yemen_line_of_separation
                                Show		 No
                                Color		 #00ff00
                            END Detail
                        END Detail
                        BEGIN Detail
                            Alias		 RWDB2_Islands
                            Show		 No
                            Color		 #8fbc8f
                            BEGIN Detail
                                Alias		 Major_islands
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Additional_major_islands
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Moderately_important_islands
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Additional_islands
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Minor_islands
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Very_small_minor_islands
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Reefs
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Shoals
                                Show		 No
                                Color		 #00ff00
                            END Detail
                        END Detail
                        BEGIN Detail
                            Alias		 RWDB2_Lakes
                            Show		 No
                            Color		 #87cefa
                            BEGIN Detail
                                Alias		 Lakes_that_should_appear_on_all_maps
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Major_lakes
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Additional_major_lakes
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Intermediate_lakes
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Minor_lakes
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Additional_minor_lakes
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Swamps
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Intermittent_major_lakes
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Intermittent_minor_lakes
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Major_salt_pans
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Minor_salt_pans
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Glaciers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                        END Detail
                        BEGIN Detail
                            Alias		 RWDB2_Provincial_Borders
                            Show		 No
                            Color		 #8fbc8f
                            BEGIN Detail
                                Alias		 First_order
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Second_order
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Third_order
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Special_boundaries
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Pre-unification_German_administration_lines
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 First_order_boundaries_on_water
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Second_order_boundaries_on_water
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Disputed_lines
                                Show		 No
                                Color		 #00ff00
                            END Detail
                        END Detail
                        BEGIN Detail
                            Alias		 RWDB2_Rivers
                            Show		 No
                            Color		 #87cefa
                            BEGIN Detail
                                Alias		 Major_rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Additional_major_rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Intermediate_rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Additional_intermediate_rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Minor_rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Additional_minor_rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Major_intermittent_rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Intermediate_intermittent_rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Minor_intermittent_rivers
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Major_canals
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Minor_canals
                                Show		 No
                                Color		 #00ff00
                            END Detail
                            BEGIN Detail
                                Alias		 Irrigation_canals
                                Show		 No
                                Color		 #00ff00
                            END Detail
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
                        ShowPrintButton		 On
                        ShowAnimButtons		 On
                        ShowAnimModeButtons		 On
                        ShowZoomMsrButtons		 On
                        ShowMapCbButton		 Off
                    END DisplayFlags

                    BEGIN RecordMovie
                        OutputFormat		 VIDEO
                        SdfSelected		 No
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
                        Bitrate		 10000000
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
                        UmbraLineColor		 #000000
                        UmbraLineStyle		 0
                        UmbraLineWidth		 2
                        FillUmbra		 On
                        UmbraFillColor		 #000000
                        ShowSunlightLine		 Off
                        SunlightLineColor		 #ffff00
                        SunlightLineStyle		 0
                        SunlightLineWidth		 2
                        FillSunlight		 On
                        SunlightFillColor		 #ffffff
                        SunlightMinOpacity		 0
                        SunlightMaxOpacity		 0.2
                        UmbraMaxOpacity		 0.7
                        UmbraMinOpacity		 0.4
                    END LightingData
                END Map

                BEGIN MapStyles

                    UseStyleTime		 No

                    BEGIN Style
                        Name		 DefaultWithBing
                        Time		 43981200
                        UpdateDelta		 10

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
                                BEGIN Detail
                                    Alias		 Coastlines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Major_Ice_Shelves
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_Ice_Shelves
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_International_Borders
                                Show		 No
                                Color		 #8fbc8f
                                BEGIN Detail
                                    Alias		 Demarcated_or_Delimited
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Indefinite_or_Disputed
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Lines_of_separation_on_land
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Lines_of_separation_at_sea
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Other_lines_of_separation_at_sea
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Continental_shelf_boundary_in_Persian_Gulf
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Demilitarized_zone_lines_in_Israel
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 No_defined_line
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Selected_claimed_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Panama_Canal_Zone_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_North-South_Yemen_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Jordan-Iraq_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Iraq-Saudi_Arabia_Neutral_Zone_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_East-West_Germany_and_Berlin_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_North-South_Vietnam_boundary
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Vietnam_DMZ_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Oman-Yemen_line_of_separation
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Islands
                                Show		 No
                                Color		 #8fbc8f
                                BEGIN Detail
                                    Alias		 Major_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_major_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Moderately_important_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Very_small_minor_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Reefs
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Shoals
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Lakes
                                Show		 No
                                Color		 #87cefa
                                BEGIN Detail
                                    Alias		 Lakes_that_should_appear_on_all_maps
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Major_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_major_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Intermediate_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_minor_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Swamps
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Intermittent_major_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Intermittent_minor_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Major_salt_pans
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_salt_pans
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Glaciers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Provincial_Borders
                                Show		 No
                                Color		 #8fbc8f
                                BEGIN Detail
                                    Alias		 First_order
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Second_order
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Third_order
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Special_boundaries
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Pre-unification_German_administration_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 First_order_boundaries_on_water
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Second_order_boundaries_on_water
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Disputed_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Rivers
                                Show		 No
                                Color		 #87cefa
                                BEGIN Detail
                                    Alias		 Major_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_major_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Intermediate_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_intermediate_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_minor_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Major_intermittent_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Intermediate_intermittent_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_intermittent_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Major_canals
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_canals
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Irrigation_canals
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                        END MapList


                        BEGIN MapAnnotations
                        END MapAnnotations

                        BEGIN RecordMovie
                            OutputFormat		 VIDEO
                            SdfSelected		 No
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
                            Bitrate		 10000000
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
                            UmbraLineColor		 #000000
                            UmbraLineStyle		 0
                            UmbraLineWidth		 2
                            FillUmbra		 On
                            UmbraFillColor		 #000000
                            ShowSunlightLine		 Off
                            SunlightLineColor		 #ffff00
                            SunlightLineStyle		 0
                            SunlightLineWidth		 2
                            FillSunlight		 On
                            SunlightFillColor		 #ffffff
                            SunlightMinOpacity		 0
                            SunlightMaxOpacity		 0.2
                            UmbraMaxOpacity		 0.7
                            UmbraMinOpacity		 0.4
                        END LightingData

                        ShowDtedRegions		 Off

                    END Style

                    BEGIN Style
                        Name		 DefaultWithoutBing
                        Time		 43981200
                        UpdateDelta		 10

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
                                BEGIN Detail
                                    Alias		 Coastlines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Major_Ice_Shelves
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_Ice_Shelves
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_International_Borders
                                Show		 No
                                Color		 #8fbc8f
                                BEGIN Detail
                                    Alias		 Demarcated_or_Delimited
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Indefinite_or_Disputed
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Lines_of_separation_on_land
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Lines_of_separation_at_sea
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Other_lines_of_separation_at_sea
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Continental_shelf_boundary_in_Persian_Gulf
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Demilitarized_zone_lines_in_Israel
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 No_defined_line
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Selected_claimed_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Panama_Canal_Zone_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_North-South_Yemen_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Jordan-Iraq_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Iraq-Saudi_Arabia_Neutral_Zone_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_East-West_Germany_and_Berlin_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_North-South_Vietnam_boundary
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Vietnam_DMZ_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Old_Oman-Yemen_line_of_separation
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Islands
                                Show		 No
                                Color		 #8fbc8f
                                BEGIN Detail
                                    Alias		 Major_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_major_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Moderately_important_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Very_small_minor_islands
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Reefs
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Shoals
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Lakes
                                Show		 No
                                Color		 #87cefa
                                BEGIN Detail
                                    Alias		 Lakes_that_should_appear_on_all_maps
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Major_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_major_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Intermediate_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_minor_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Swamps
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Intermittent_major_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Intermittent_minor_lakes
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Major_salt_pans
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_salt_pans
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Glaciers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Provincial_Borders
                                Show		 No
                                Color		 #8fbc8f
                                BEGIN Detail
                                    Alias		 First_order
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Second_order
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Third_order
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Special_boundaries
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Pre-unification_German_administration_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 First_order_boundaries_on_water
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Second_order_boundaries_on_water
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Disputed_lines
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                            BEGIN Detail
                                Alias		 RWDB2_Rivers
                                Show		 No
                                Color		 #87cefa
                                BEGIN Detail
                                    Alias		 Major_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_major_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Intermediate_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_intermediate_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Additional_minor_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Major_intermittent_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Intermediate_intermittent_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_intermittent_rivers
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Major_canals
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Minor_canals
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                                BEGIN Detail
                                    Alias		 Irrigation_canals
                                    Show		 No
                                    Color		 #00ff00
                                END Detail
                            END Detail
                        END MapList


                        BEGIN MapAnnotations
                        END MapAnnotations

                        BEGIN RecordMovie
                            OutputFormat		 VIDEO
                            SdfSelected		 No
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
                            UmbraLineColor		 #000000
                            UmbraLineStyle		 0
                            UmbraLineWidth		 2
                            FillUmbra		 On
                            UmbraFillColor		 #000000
                            ShowSunlightLine		 Off
                            SunlightLineColor		 #ffff00
                            SunlightLineStyle		 0
                            SunlightLineWidth		 2
                            FillSunlight		 On
                            SunlightFillColor		 #ffffff
                            SunlightMinOpacity		 0
                            SunlightMaxOpacity		 0.2
                            UmbraMaxOpacity		 0.7
                            UmbraMinOpacity		 0.4
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

            Canada		
            United_States_of_America		

        END Class

        Class CoverageDefinition

            Country_Coverage		
            World_Coverage		

        END Class

        Class Satellite

            Circ_Sat		
            Repeat_Sat		
            Sun_Sat		

        END Class

        Class Target

            Constraint_Template		

        END Class

    END SubObjects

    BEGIN References
        Instance *
            *		
            CoverageDefinition/Country_Coverage		
            CoverageDefinition/World_Coverage		
        END Instance
        Instance AreaTarget/Canada
            AreaTarget/Canada		
            CoverageDefinition/Country_Coverage		
        END Instance
        Instance AreaTarget/United_States_of_America
            AreaTarget/United_States_of_America		
            CoverageDefinition/Country_Coverage		
        END Instance
        Instance CoverageDefinition/Country_Coverage
            CoverageDefinition/Country_Coverage		
            CoverageDefinition/Country_Coverage/FigureOfMerit/Coverage_Time		
        END Instance
        Instance CoverageDefinition/Country_Coverage/FigureOfMerit/Coverage_Time
        END Instance
        Instance CoverageDefinition/World_Coverage
            CoverageDefinition/World_Coverage		
            CoverageDefinition/World_Coverage/FigureOfMerit/Num_Access_Coverage		
            CoverageDefinition/World_Coverage/FigureOfMerit/Simple_Coverage		
        END Instance
        Instance CoverageDefinition/World_Coverage/FigureOfMerit/Num_Access_Coverage
        END Instance
        Instance CoverageDefinition/World_Coverage/FigureOfMerit/Simple_Coverage
        END Instance
        Instance Satellite/Circ_Sat
            Satellite/Circ_Sat		
            Satellite/Circ_Sat/Sensor/Circ_Sensor		
        END Instance
        Instance Satellite/Circ_Sat/Sensor/Circ_Sensor
            CoverageDefinition/World_Coverage		
            Satellite/Circ_Sat/Sensor/Circ_Sensor		
        END Instance
        Instance Satellite/Repeat_Sat
            Satellite/Repeat_Sat		
            Satellite/Repeat_Sat/Sensor/Repeat_Sensor		
        END Instance
        Instance Satellite/Repeat_Sat/Sensor/Repeat_Sensor
            CoverageDefinition/Country_Coverage		
            CoverageDefinition/World_Coverage		
            Satellite/Repeat_Sat/Sensor/Repeat_Sensor		
        END Instance
        Instance Satellite/Sun_Sat
            Satellite/Sun_Sat		
            Satellite/Sun_Sat/Sensor/Sun_Sensor		
        END Instance
        Instance Satellite/Sun_Sat/Sensor/Sun_Sensor
            CoverageDefinition/World_Coverage		
            Satellite/Sun_Sat/Sensor/Sun_Sensor		
        END Instance
        Instance Target/Constraint_Template
            CoverageDefinition/World_Coverage		
            Target/Constraint_Template		
        END Instance
    END References

END Scenario
