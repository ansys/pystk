stk.v.4.1.1
BEGIN Scenario
    Name            AreaTgtWeird

BEGIN Epoch
    Epoch        1 Nov 1997 00:00:00.00

END Epoch

BEGIN Interval

Start               1 Nov 1997 00:00:00.000000000
Stop                1 Nov 1997 08:00:00.000000000

END Interval

BEGIN CentralBody

    PrimaryBody     Earth

END CentralBody

BEGIN Extensions
    
    BEGIN Graphics

BEGIN Animation

    StartTime          1 Nov 1997 00:00:00.000000000
    EndTime            1 Nov 1997 02:00:00.000000000
    Direction          Forward
    UpdateDelta        30.00
    RefreshDelta       0.1
    XRealTimeMult      1.0
    RealTimeOffset     0.0

END Animation


        BEGIN DisplayFlags
            ShowLabels          On
            ShowPassLabel       Off
            ShowElsetNum        Off
            ShowGndTracks       On
            ShowGndMarkers      On
            ShowOrbitMarkers    On
            ShowPlanetOrbits    Off
            ShowPlanetCBIPos    On
            ShowPlanetCBILabel  On
            ShowPlanetGndPos    On
            ShowPlanetGndLabel  On
            ShowSensors         On
            ShowTurnMarkers     Off
            ShowOrbits          On
            ShowDtedRegions     Off
            ShowToolBar         On
            ShowStatusBar       On
            ShowScrollBars      On
            AllowAnimUpdate     Off
            AccShowLine         On
            AccAnimHigh         On
            AccStatHigh         On
            ShowPrintButton     On
            ShowAnimButtons     On
            ShowAnimModeButtons On
            ShowZoomMsrButtons  On
            ShowMapCbButton     Off
        END DisplayFlags

BEGIN MapData

    BEGIN Map

        MapNum         1

        BEGIN MapAttributes
            CenterLatitude       0.000000
            CenterLongitude      0.000000
            ProjectionAltitude   60000.000000
            FieldOfView          35.000000
            OrthoDisplayDistance 20000000.000000
            TransformTrajectory  On
            EquatorialRadius     6378137.000000
            PrimaryBody          Earth
            BackgroundColor      0
            LatLonLines          On
            LatSpacing           20.000000
            LonSpacing           20.000000
            LatLonLineColor      7
            LatLonLineStyle      2
            ShowOrthoDistGrid    Off
            OrthoGridXSpacing    5
            OrthoGridYSpacing    5
            OrthoGridColor       7
            ShowImageExtents     Off
            ImageExtentLineColor 7
            ImageExtentLineStyle 0
            ImageExtentLineWidth 1.000000
            ShowImageNames       Off
            ImageNameFont        0
            Projection           EquidistantCylindrical
            Resolution           Medium
            SubSolarPoint        Off
            SolarTerminator      Off
            CoordinateSys        ECF
            BEGIN ZoomBounds
                -28.610526 16.871053 7.768421 89.628947
                -90.000000 -180.000000 90.000000 180.000000
            END ZoomBounds
            Zoomed               Yes
            SwapMapResolution    Yes
            NoneToVLowSwapDist   2000000.000000
            VLowToLowSwapDist    20000.000000
            LowToMediumSwapDist  10000.000000
            MediumToHighSwapDist 5000.000000
            HighToVHighSwapDist  1000.000000
            VHighToSHighSwapDist 100.000000
            BEGIN Axes
                DisplayAxes no
                CoordSys    BBR
                Display+x   yes
                Label+x     yes
                Color+x     7
                Scale+x     2.000000
                Display-x   yes
                Label-x     yes
                Color-x     7
                Scale-x     2.000000
                Display+y   yes
                Label+y     yes
                Color+y     7
                Scale+y     2.000000
                Display-y   yes
                Label-y     yes
                Color-y     7
                Scale-y     2.000000
                Display+z   yes
                Label+z     yes
                Color+z     7
                Scale+z     2.000000
                Display-z   yes
                Label-z     yes
                Color-z     7
                Scale-z     2.000000
            END Axes

        END MapAttributes

        BEGIN Maps
            RWDB2_Coastlines    Yes 1
            Coastlines    No 1
            Major_Ice_Shelves    No 1
            Minor_Ice_Shelves    No 1
            RWDB2_International_Borders    Yes 1
            Demarcated_or_Delimited    No 1
            Indefinite_or_Disputed    No 1
            Lines_of_separation_on_land    No 1
            Lines_of_separation_at_sea    No 1
            Other_lines_of_separation_at_sea    No 1
            Continental_shelf_boundary_in_Persian_Gulf    No 1
            Demilitarized_zone_lines_in_Israel    No 1
            No_defined_line    No 1
            Selected_claimed_lines    No 1
            Old_Panama_Canal_Zone_lines    No 1
            Old_North-South_Yemen_lines    No 1
            Old_Jordan-Iraq_lines    No 1
            Old_Iraq-Saudi_Arabia_Neutral_Zone_lines    No 1
            Old_East-West_Germany_and_Berlin_lines    No 1
            Old_North-South_Vietnam_boundary    No 1
            Old_Vietnam_DMZ_lines    No 1
            Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines    No 1
            Old_Oman-Yemen_line_of_separation    No 1
            RWDB2_Islands    Yes 1
            Major_islands    No 1
            Additional_major_islands    No 1
            Moderately_important_islands    No 1
            Additional_islands    No 1
            Minor_islands    No 1
            Very_small_minor_islands    No 1
            Reefs    No 1
            Shoals    No 1
            RWDB2_Lakes    Yes 1
            Lakes_that_should_appear_on_all_maps    No 1
            Major_lakes    No 1
            Additional_major_lakes    No 1
            Intermediate_lakes    No 1
            Minor_lakes    No 1
            Additional_minor_lakes    No 1
            Swamps    No 1
            Intermittent_major_lakes    No 1
            Intermittent_minor_lakes    No 1
            Major_salt_pans    No 1
            Minor_salt_pans    No 1
            Glaciers    No 1
            RWDB2_Provincial_Borders    No 1
            First_order    No 1
            Second_order    No 1
            Third_order    No 1
            Special_boundaries    No 1
            Pre-unification_German_administration_lines    No 1
            First_order_boundaries_on_water    No 1
            Second_order_boundaries_on_water    No 1
            Disputed_lines    No 1
            RWDB2_Rivers    No 1
            Major_rivers    No 1
            Additional_major_rivers    No 1
            Intermediate_rivers    No 1
            Additional_intermediate_rivers    No 1
            Minor_rivers    No 1
            Additional_minor_rivers    No 1
            Major_intermittent_rivers    No 1
            Intermediate_intermittent_rivers    No 1
            Minor_intermittent_rivers    No 1
            Major_canals    No 1
            Minor_canals    No 1
            Irrigation_canals    No 1
        END Maps

        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN DisplayFlags
            ShowLabels          On
            ShowPassLabel       Off
            ShowElsetNum        Off
            ShowGndTracks       On
            ShowGndMarkers      On
            ShowOrbitMarkers    On
            ShowPlanetOrbits    Off
            ShowPlanetCBIPos    On
            ShowPlanetCBILabel  On
            ShowPlanetGndPos    On
            ShowPlanetGndLabel  On
            ShowSensors         On
            ShowTurnMarkers     Off
            ShowOrbits          On
            ShowDtedRegions     Off
            ShowToolBar         On
            ShowStatusBar       On
            ShowScrollBars      On
            AllowAnimUpdate     Off
            AccShowLine         On
            AccAnimHigh         On
            AccStatHigh         On
            ShowPrintButton     On
            ShowAnimButtons     On
            ShowAnimModeButtons On
            ShowZoomMsrButtons  On
            ShowMapCbButton     Off
        END DisplayFlags

        BEGIN SoftVTR
            OutputFormat     RGB
            Directory        /tmp
            BaseName         Frame
            Digits           4
            Frame            0
            LastAnimTime     0.000000
            OutputMode       Normal
            HiResAssembly    Assemble
            HRWidth          6000
            HRHeight         4500
            HRDPI            600.000000
            SnapInterval     0.000000
        END SoftVTR


        BEGIN TimeDisplay
            Show             0
            TextColor        1
            Transparent      0
            BackColor        0
            XPosition        20
            YPosition        -20
        END TimeDisplay

        BEGIN WindowLayout
            VariableAspectRatio  Yes
            MapTop               358
            MapBottom            905
            MapLeft              182
            MapRight             1160
            MapCenterByMouse     Click
        END WindowLayout

    END Map
        UseStyleTime   No

END MapData
    END Graphics
    
    BEGIN ChainGraphics
    END ChainGraphics
    
    BEGIN Sun

        SubsolarPoint                Off
        SubsolarPointColor           4
        SubsolarPointLineWidth       1
        SubsolarPointMarkerStyle     2

        PenumbraUmbra                Off
        PenumbraUmbraColor           4
        PenumbraUmbraLineStyle       0
        PenumbraUmbraLineWidth       1

        SunlightPenumbra             Off
        SunlightPenumbraColor        4
        SunlightPenumbraLineStyle    0
        SunlightPenumbraLineWidth    1

        DisplayAltitude               0.000000

        DarknessToPenumbraFill       Off
        DarknessToPenumbraColor      0
        DarknessToPenumbraFillStyle  7
        DarknessToSunlightFill       Off
        DarknessToSunlightColor      0
        DarknessToSunlightFillStyle  7
        UmbraToSunlightFill          Off
        UmbraToSunlightColor         0
        UmbraToSunlightFillStyle     7
    END Sun
    
    BEGIN Units
		DistanceUnit		Kilometers
		TimeUnit		Seconds
		DateFormat		GregorianUTC
		AngleUnit		Degrees
		MassUnit		Kilograms
		PowerUnit		dBW
		FrequencyUnit		Gigahertz
		SmallDistanceUnit		Meters
		LatitudeUnit		Degrees
		LongitudeUnit		Degrees
		DurationUnit		Hr:Min:Sec
		Temperature		Kelvin
		SmallTimeUnit		Seconds
		RatioUnit		Decibel
		RcsUnit		Decibel
		DopplerVelocityUnit		MetersperSecond
		SARTimeResProdUnit		Meter-Second
		PowerDensityUnit		Decibels
		ForceUnit		Newtons
		PRFUnit		Kilohertz
		BandwidthUnit		Megahertz
		SmallVelocityUnit		CentimetersperSecond
    END Units
    
    BEGIN ReportUnits
		DistanceUnit		Kilometers
		TimeUnit		Seconds
		DateFormat		GregorianUTC
		AngleUnit		Degrees
		MassUnit		Kilograms
		PowerUnit		dBW
		FrequencyUnit		Gigahertz
		SmallDistanceUnit		Meters
		LatitudeUnit		Degrees
		LongitudeUnit		Degrees
		DurationUnit		Hr:Min:Sec
		Temperature		Kelvin
		SmallTimeUnit		Seconds
		RatioUnit		Decibel
		RcsUnit		Decibel
		DopplerVelocityUnit		MetersperSecond
		SARTimeResProdUnit		Meter-Second
		PowerDensityUnit		Decibels
		ForceUnit		Newtons
		PRFUnit		Kilohertz
		BandwidthUnit		Megahertz
		SmallVelocityUnit		CentimetersperSecond
    END ReportUnits
    
    BEGIN GenDb

		BEGIN Database
		    DbType       Satellite
		    DefDb        stkSatDb.sd
		    DefDbDir     /net/stk/group/STKData/Databases/Satellite
		    UseMyDb      Off
		    MaxMatches   2000

		END Database

		BEGIN Database
		    DbType       City
		    DefDb        stkCityDb.cd
		    DefDbDir     /net/stk/group/STKData/Databases/City
		    UseMyDb      Off
		    MaxMatches   2000

		END Database

		BEGIN Database
		    DbType       Facility
		    DefDb        stkFacility.fd
		    DefDbDir     /net/stk/group/STKData/Databases/Facility
		    UseMyDb      Off
		    MaxMatches   2000

		END Database

		BEGIN Database
		    DbType       Star
		    DefDb        stkStarDb.bd
		    DefDbDir     /net/stk/group/STKData/Databases/Star
		    UseMyDb      Off
		    MaxMatches   2000

		END Database
    END GenDb
    
    BEGIN Report
    END Report
    
    BEGIN Msgp4Ext
    END Msgp4Ext
    
    BEGIN DynData
    END DynData
    
    BEGIN Desc
        ShortText    28
Area Target Test Senarion #4
        LongText    157
This Scenario has a number of Area Targets
for testing Area-to-Vehicle , Vehicle-to-
Area and sensor  access.

NOTE: Scenario has two custom sensor patterns

    END Desc
    
    BEGIN RfEnv
	UseGasAbsorbModel    No

	BEGIN Absorption

		AbsorptionModel	Simple Satcom

		BEGIN ModelData
			SWVC		    7.500000
			Temperature		293.150000

		END ModelData

	END Absorption

	UseRainModel         No
    END RfEnv
    
    BEGIN RCS
	Inherited          False
	ClutterCoef        0.000000e+00
	BEGIN RCSBAND
		ConstantValue      0.000000e+00
		Swerling      0
		BandData      3.000000e+06 3.000000e+11
	END RCSBAND
    END RCS
    
    BEGIN PrRaeClutterDb
    END PrRaeClutterDb
    
    BEGIN Crdn
    END Crdn
    
    BEGIN DIS

		Begin General

			Verbose                    Off
			Processing                 Off
			Statistics                 Off
			ExerciseID                 -1
			ForceID                    -1

		End General


		Begin Output

			Version                    5
			ExerciseID                 1
			forceID                    1
			HeartbeatTimer             5.000000
			DistanceThresh             1.000000
			OrientThresh               3.000000

		End Output


		Begin Time

			Mode                       rtPDUTimestamp

		End Time


		Begin PDUInfo


		End PDUInfo


		Begin Parameters

			ParmData  COLORFRIENDLY        blue
			ParmData  COLORNEUTRAL         white
			ParmData  COLOROPFORCE         red
			ParmData  MAXDRELSETS          1000

		End Parameters


		Begin Network

			NetIF                      Default
			Mode                       Broadcast
			McastIP                    224.0.0.1
			Port                       3000
			rChannelBufferSize         65000
			ReadBufferSize             500
			QueuePollPeriod            20
			MaxRcvQueueEntries         500
			MaxRcvIOThreads            4
			sChannelBufferSize         65000

		End Network


		Begin EntityTypeDef


#			order: kind:domain:country:catagory:subCatagory:specific:xtra ( -1 = * )


		End EntityTypeDef


		Begin EntityFilter


		End EntityFilter

    END DIS
    
    BEGIN PODS
        MintimebtPasses       1800
        GlobalConvCrit        2
        GlobalMinIter         1
        GlobalMaxIter         9
        ArcEdSigMult          3.500000
        ArcIRMS               200.000000
        ArcConvCrit           2
        ArcMinIter            4
        ArcMaxIter            9
        ArcMax1globalIter     19
        IterationCntl         Automatic
        IntegrationStepSize   60.000000
        ReferenceDate         1 Nov 1997 00:00:00.00
        RefDateControl        Fixed
        ODTimesControl        Fixed
        UseGM                 False
        EstimateGM            False
        GMValue               398600.441800000
        GMSigma               0.000000000
        SemiMajorAxis         6378137.000000
        InvFlatCoef           298.257223491
        SunPert               True
        MoonPert              True
        MarsPert              False
        VenusPert             False
        MercuryPert           False
        PlutoPert             False
        UranusPert            False
        SaturnPert            False
        JupiterPert           False
        NeptunePert           False
        MaxDegree             12
        MaxOrder              12
        FluxFile              /net/stk/group/PODS/tables/tables.dat
        JPLFile               /net/stk/group/PODS/ephem/jplde403.dat
        GeoFile               /net/stk/group/PODS/gco_files/wgs84.gco
        PODSDirectory         /net/stk/group/PODS
        TrkDataDirectory      /net/stk/group/PODS/trk_data
        ScratchDirectory      /tmp
        CleanupFlag           True
        PODSMessages          True
        TDMaxObs              1000
        TDMaxPB               168
        TDMaxMB               1000
        TDMaxDR               300
        VOMaxObs              1000
        VOIntSteps            31
        BDMaxSD               20
        BDMaxDR               2
        BEGIN SimData
          TruthTrop           On
          DeviatedTrop        On
          TruthDelay          Off
          DeviatedDelay       Off
          AddBias             Off
          AddNoise            Off
          AddTime             Off
          TimeBias            0.000000
          TimeStep            60.000000
        END SimData
    END PODS
    
    BEGIN AsyncIPC
    END AsyncIPC

END Extensions

BEGIN SubObjects

Class Aircraft

	GA3
	GA5

END Class

Class AreaTarget

	AreaTg1
	AreaTg2
	AreaTg3
	AreaTg4
	AreaTg5
	AreaTg6
	AreaTg7

END Class

Class Satellite

	Veh1

END Class

END SubObjects

END Scenario
