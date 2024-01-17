stk.v.7.0
BEGIN Scenario
    Name            Bug_Access_TgtSensor_23617

BEGIN Epoch
    Epoch        1 Jul 2005 12:00:00.00

END Epoch

BEGIN Interval

Start               1 Jul 2005 12:00:00.000000000
Stop                2 Jul 2005 12:00:00.000000000

END Interval

BEGIN EOPFile

    EOPFilename     C:\This\File\Must\Not\Exist\EOP-v1.1.txt

END EOPFile

BEGIN GlobalPrefs

    SatelliteNoOrbWarning    No
    MissileNoOrbWarning      No
    AircraftWGS84Warning     Always
END GlobalPrefs

BEGIN CentralBody

    PrimaryBody     Earth
    UseTerrainCache Yes

END CentralBody

BEGIN Extensions

    BEGIN Graphics

BEGIN Animation

    StartTime          1 Jul 2005 12:00:00.000000000
    EndTime            2 Jul 2005 12:00:00.000000000
    Direction          Forward
    UpdateDelta        30.0000
    RefreshDelta       HighSpeed
    XRealTimeMult      1.0000
    RealTimeOffset     0.0000

END Animation


        BEGIN DisplayFlags
            ShowLabels           On
            ShowPassLabel        Off
            ShowElsetNum         Off
            ShowGndTracks        On
            ShowGndMarkers       On
            ShowOrbitMarkers     On
            ShowPlanetOrbits     Off
            ShowPlanetCBIPos     On
            ShowPlanetCBILabel   On
            ShowPlanetGndPos     On
            ShowPlanetGndLabel   On
            ShowSensors          On
            ShowWayptMarkers     Off
            ShowWayptTurnMarkers Off
            ShowOrbits           On
            ShowDtedRegions      Off
            ShowAreaTgtCentroids On
            ShowToolBar          On
            ShowStatusBar        On
            ShowScrollBars       On
            AllowAnimUpdate      Off
            AccShowLine          On
            AccAnimHigh          On
            AccStatHigh          On
            ShowPrintButton      On
            ShowAnimButtons      On
            ShowAnimModeButtons  On
            ShowZoomMsrButtons   On
            ShowMapCbButton      Off
        END DisplayFlags

BEGIN WinFonts

    System
    MS Sans Serif,22,0,0
    MS Sans Serif,28,0,0

END WinFonts

BEGIN MapData

    Begin TerrainConverterData
           NorthLat        0.00000000000000e+000
           EastLon         0.00000000000000e+000
           SouthLat        0.00000000000000e+000
           WestLon         0.00000000000000e+000
           ColorByRGB      No
           AltsFromMSL     No
           UseColorRamp    Yes
           UseRegionMinMax Yes
           SizeSameAsSrc   Yes
           MinAltHSV       0.00000000000000e+000 7.00000000000000e-001 8.00000000000000e-001 4.00000000000000e-001
           MaxAltHSV       1.00000000000000e+006 0.00000000000000e+000 2.00000000000000e-001 1.00000000000000e+000
           SmoothColors    Yes
           CreateChunkTrn  No
           OutputFormat    PDTTX
    End TerrainConverterData

    BEGIN Map

        MapNum         1
        TrackingMode   LatLon

        BEGIN MapAttributes
            CenterLatitude       0.000000
            CenterLongitude      0.000000
            ProjectionAltitude   63621860.000000
            FieldOfView          35.000000
            OrthoDisplayDistance 20000000.000000
            TransformTrajectory  On
            EquatorialRadius     6378137.000000
            PrimaryBody          Earth
            SecondaryBody        Sun
            BackgroundColor      #000000
            LatLonLines          On
            LatSpacing           30.000000
            LonSpacing           30.000000
            LatLonLineColor      #999999
            LatLonLineStyle      2
            ShowOrthoDistGrid    Off
            OrthoGridXSpacing    5
            OrthoGridYSpacing    5
            OrthoGridColor       #ffffff
            ShowImageExtents     Off
            ImageExtentLineColor #ffffff
            ImageExtentLineStyle 0
            ImageExtentLineWidth 1.000000
            ShowImageNames       Off
            ImageNameFont        0
            Projection           EquidistantCylindrical
            Resolution           VeryLow
            CoordinateSys        ECF
            UseBackgroundImage   On
            BackgroundImageFile  Basic
            UseCloudsFile        Off
            BEGIN ZoomBounds
                -90.000000 -179.999999 90.000000 179.999999
            END ZoomBounds
            Zoomed               No
            SwapMapResolution    Yes
            NoneToVLowSwapDist   2000000.000000
            VLowToLowSwapDist    20000.000000
            LowToMediumSwapDist  10000.000000
            MediumToHighSwapDist 5000.000000
            HighToVHighSwapDist  1000.000000
            VHighToSHighSwapDist 100.000000
            BEGIN Axes
                DisplayAxes no
                CoordSys    CBI
                2aryCB      Sun
                Display+x   yes
                Label+x     yes
                Color+x     #ffffff
                Scale+x     3.000000
                Display-x   yes
                Label-x     yes
                Color-x     #ffffff
                Scale-x     3.000000
                Display+y   yes
                Label+y     yes
                Color+y     #ffffff
                Scale+y     3.000000
                Display-y   yes
                Label-y     yes
                Color-y     #ffffff
                Scale-y     3.000000
                Display+z   yes
                Label+z     yes
                Color+z     #ffffff
                Scale+z     3.000000
                Display-z   yes
                Label-z     yes
                Color-z     #ffffff
                Scale-z     3.000000
            END Axes

        END MapAttributes

        BEGIN Maps
            RWDB2_Coastlines    Yes #8fbc8f
            RWDB2_International_Borders    Yes #8fbc8f
            RWDB2_Islands    Yes #8fbc8f
            RWDB2_Lakes    No #87cefa
            RWDB2_Provincial_Borders    No #8fbc8f
            RWDB2_Rivers    No #87cefa
        END Maps


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN DisplayFlags
            ShowLabels           On
            ShowPassLabel        Off
            ShowElsetNum         Off
            ShowGndTracks        On
            ShowGndMarkers       On
            ShowOrbitMarkers     On
            ShowPlanetOrbits     Off
            ShowPlanetCBIPos     On
            ShowPlanetCBILabel   On
            ShowPlanetGndPos     On
            ShowPlanetGndLabel   On
            ShowSensors          On
            ShowWayptMarkers     Off
            ShowWayptTurnMarkers Off
            ShowOrbits           On
            ShowDtedRegions      Off
            ShowAreaTgtCentroids On
            ShowToolBar          On
            ShowStatusBar        On
            ShowScrollBars       On
            AllowAnimUpdate      Off
            AccShowLine          On
            AccAnimHigh          On
            AccStatHigh          On
            ShowPrintButton      On
            ShowAnimButtons      On
            ShowAnimModeButtons  On
            ShowZoomMsrButtons   On
            ShowMapCbButton      Off
        END DisplayFlags

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\vcoppola\LOCALS~1\Temp
            BaseName         Frame
            Digits           4
            Frame            0
            LastAnimTime     0.000000
            OutputMode       Normal
            HiResAssembly    Assemble
            HRWidth          6000
            HRHeight         4500
            HRDPI            600.000000
            UseSnapInterval  No
            SnapInterval     0.000000
        END SoftVTR


        BEGIN TimeDisplay
            Show             0
            TextColor        #ffffff
            Transparent      0
            BackColor        #4d4d4d
            XPosition        20
            YPosition        -20
        END TimeDisplay

        BEGIN WindowLayout
            VariableAspectRatio  Yes
            MapCenterByMouse     Click
        END WindowLayout

        BEGIN LightingData
            DisplayAltitude              0.000000
            SubsolarPoint                Off
            SubsolarPointColor           #ffff00
            SubsolarPointMarkerStyle     2

            ShowUmbraLine                Off
            UmbraLineColor               #0000ff
            UmbraLineStyle               0
            UmbraLineWidth               2
            FillUmbra                    Off
            UmbraFillColor               #0000ff
            UmbraFillStyle               7

            ShowPenumbraLines            Off
            PenumbraLineColor            #87cefa
            PenumbraLineStyle            0
            PenumbraLineWidth            1
            FillPenumbra                 Off
            PenumbraFillColor            #87cefa
            PenumbraFillStyle            7

            ShowSunlightLine             Off
            SunlightLineColor            #ffff00
            SunlightLineStyle            0
            SunlightLineWidth            2
            FillSunlight                 Off
            SunlightFillColor            #ffff00
            SunlightFillStyle            7

        END LightingData

    END Map

    BEGIN MapStyles

        UseStyleTime        No

        BEGIN Style
        Name                No_Map_Bckgrnd
        Time                0.000000
        UpdateDelta         60.000000

        BEGIN MapAttributes
            CenterLatitude       0.000000
            CenterLongitude      0.000000
            ProjectionAltitude   63621860.000000
            FieldOfView          35.000000
            OrthoDisplayDistance 20000000.000000
            TransformTrajectory  On
            EquatorialRadius     6378137.000000
            PrimaryBody          Earth
            SecondaryBody        Sun
            BackgroundColor      #000000
            LatLonLines          On
            LatSpacing           30.000000
            LonSpacing           30.000000
            LatLonLineColor      #999999
            LatLonLineStyle      2
            ShowOrthoDistGrid    Off
            OrthoGridXSpacing    5
            OrthoGridYSpacing    5
            OrthoGridColor       #ffffff
            ShowImageExtents     Off
            ImageExtentLineColor #ffffff
            ImageExtentLineStyle 0
            ImageExtentLineWidth 1.000000
            ShowImageNames       Off
            ImageNameFont        0
            Projection           EquidistantCylindrical
            Resolution           VeryLow
            CoordinateSys        ECF
            UseBackgroundImage   Off
            UseCloudsFile        Off
            BEGIN ZoomBounds
                -90.000000 -179.999999 90.000000 179.999999
            END ZoomBounds
            Zoomed               No
            SwapMapResolution    Yes
            NoneToVLowSwapDist   2000000.000000
            VLowToLowSwapDist    20000.000000
            LowToMediumSwapDist  10000.000000
            MediumToHighSwapDist 5000.000000
            HighToVHighSwapDist  1000.000000
            VHighToSHighSwapDist 100.000000
            BEGIN Axes
                DisplayAxes no
                CoordSys    CBI
                2aryCB      Sun
                Display+x   yes
                Label+x     yes
                Color+x     #ffffff
                Scale+x     3.000000
                Display-x   yes
                Label-x     yes
                Color-x     #ffffff
                Scale-x     3.000000
                Display+y   yes
                Label+y     yes
                Color+y     #ffffff
                Scale+y     3.000000
                Display-y   yes
                Label-y     yes
                Color-y     #ffffff
                Scale-y     3.000000
                Display+z   yes
                Label+z     yes
                Color+z     #ffffff
                Scale+z     3.000000
                Display-z   yes
                Label-z     yes
                Color-z     #ffffff
                Scale-z     3.000000
            END Axes

        END MapAttributes

        BEGIN Maps
            RWDB2_Coastlines    Yes #00ff00
            RWDB2_International_Borders    Yes #00ff00
            RWDB2_Islands    Yes #00ff00
            RWDB2_Lakes    Yes #87cefa
            RWDB2_Provincial_Borders    Yes #00ff00
            RWDB2_Rivers    No #00ff00
        END Maps


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\vcoppola\LOCALS~1\Temp
            BaseName         Frame
            Digits           4
            Frame            0
            LastAnimTime     0.000000
            OutputMode       Normal
            HiResAssembly    Assemble
            HRWidth          6000
            HRHeight         4500
            HRDPI            600.000000
            UseSnapInterval  No
            SnapInterval     0.000000
        END SoftVTR


        BEGIN TimeDisplay
            Show             0
            TextColor        #00ffff
            Transparent      0
            BackColor        #000000
            XPosition        20
            YPosition        -20
        END TimeDisplay

        BEGIN LightingData
            DisplayAltitude              0.000000
            SubsolarPoint                Off
            SubsolarPointColor           #ffff00
            SubsolarPointMarkerStyle     2

            ShowUmbraLine                Off
            UmbraLineColor               #ffff00
            UmbraLineStyle               0
            UmbraLineWidth               1
            FillUmbra                    Off
            UmbraFillColor               #000000
            UmbraFillStyle               7

            ShowPenumbraLines            Off
            PenumbraLineColor            #ffff00
            PenumbraLineStyle            0
            PenumbraLineWidth            1
            FillPenumbra                 Off
            PenumbraFillColor            #000000
            PenumbraFillStyle            7

            ShowSunlightLine             Off
            SunlightLineColor            #ffff00
            SunlightLineStyle            0
            SunlightLineWidth            1
            FillSunlight                 Off
            SunlightFillColor            #ffff00
            SunlightFillStyle            7

        END LightingData

        ShowDtedRegions     Off

        End Style

        BEGIN Style
        Name                Basic_Map_Bckgrnd
        Time                0.000000
        UpdateDelta         60.000000

        BEGIN MapAttributes
            CenterLatitude       0.000000
            CenterLongitude      0.000000
            ProjectionAltitude   63621860.000000
            FieldOfView          35.000000
            OrthoDisplayDistance 20000000.000000
            TransformTrajectory  On
            EquatorialRadius     6378137.000000
            PrimaryBody          Earth
            SecondaryBody        Sun
            BackgroundColor      #000000
            LatLonLines          On
            LatSpacing           30.000000
            LonSpacing           30.000000
            LatLonLineColor      #999999
            LatLonLineStyle      2
            ShowOrthoDistGrid    Off
            OrthoGridXSpacing    5
            OrthoGridYSpacing    5
            OrthoGridColor       #ffffff
            ShowImageExtents     Off
            ImageExtentLineColor #ffffff
            ImageExtentLineStyle 0
            ImageExtentLineWidth 1.000000
            ShowImageNames       Off
            ImageNameFont        0
            Projection           EquidistantCylindrical
            Resolution           VeryLow
            CoordinateSys        ECF
            UseBackgroundImage   On
            BackgroundImageFile  Basic
            UseCloudsFile        Off
            BEGIN ZoomBounds
                -90.000000 -179.999999 90.000000 179.999999
            END ZoomBounds
            Zoomed               No
            SwapMapResolution    Yes
            NoneToVLowSwapDist   2000000.000000
            VLowToLowSwapDist    20000.000000
            LowToMediumSwapDist  10000.000000
            MediumToHighSwapDist 5000.000000
            HighToVHighSwapDist  1000.000000
            VHighToSHighSwapDist 100.000000
            BEGIN Axes
                DisplayAxes no
                CoordSys    CBI
                2aryCB      Sun
                Display+x   yes
                Label+x     yes
                Color+x     #ffffff
                Scale+x     3.000000
                Display-x   yes
                Label-x     yes
                Color-x     #ffffff
                Scale-x     3.000000
                Display+y   yes
                Label+y     yes
                Color+y     #ffffff
                Scale+y     3.000000
                Display-y   yes
                Label-y     yes
                Color-y     #ffffff
                Scale-y     3.000000
                Display+z   yes
                Label+z     yes
                Color+z     #ffffff
                Scale+z     3.000000
                Display-z   yes
                Label-z     yes
                Color-z     #ffffff
                Scale-z     3.000000
            END Axes

        END MapAttributes

        BEGIN Maps
            RWDB2_Coastlines    Yes #8fbc8f
            RWDB2_International_Borders    Yes #8fbc8f
            RWDB2_Islands    Yes #8fbc8f
            RWDB2_Lakes    No #00ff00
            RWDB2_Provincial_Borders    No #00ff00
            RWDB2_Rivers    No #00ff00
        END Maps


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\vcoppola\LOCALS~1\Temp
            BaseName         Frame
            Digits           4
            Frame            0
            LastAnimTime     0.000000
            OutputMode       Normal
            HiResAssembly    Assemble
            HRWidth          6000
            HRHeight         4500
            HRDPI            600.000000
            UseSnapInterval  No
            SnapInterval     0.000000
        END SoftVTR


        BEGIN TimeDisplay
            Show             0
            TextColor        #00ffff
            Transparent      0
            BackColor        #000000
            XPosition        20
            YPosition        -20
        END TimeDisplay

        BEGIN LightingData
            DisplayAltitude              0.000000
            SubsolarPoint                Off
            SubsolarPointColor           #ffff00
            SubsolarPointMarkerStyle     2

            ShowUmbraLine                Off
            UmbraLineColor               #ffff00
            UmbraLineStyle               0
            UmbraLineWidth               1
            FillUmbra                    Off
            UmbraFillColor               #000000
            UmbraFillStyle               7

            ShowPenumbraLines            Off
            PenumbraLineColor            #ffff00
            PenumbraLineStyle            0
            PenumbraLineWidth            1
            FillPenumbra                 Off
            PenumbraFillColor            #000000
            PenumbraFillStyle            7

            ShowSunlightLine             Off
            SunlightLineColor            #ffff00
            SunlightLineStyle            0
            SunlightLineWidth            1
            FillSunlight                 Off
            SunlightFillColor            #ffff00
            SunlightFillStyle            7

        END LightingData

        ShowDtedRegions     Off

        End Style

        BEGIN Style
        Name                Orthographic_Projection
        Time                0.000000
        UpdateDelta         60.000000

        BEGIN MapAttributes
            CenterLatitude       0.000000
            CenterLongitude      0.000000
            ProjectionAltitude   63621860.000000
            FieldOfView          35.000000
            OrthoDisplayDistance 20000000.000000
            TransformTrajectory  On
            EquatorialRadius     6378137.000000
            PrimaryBody          Earth
            SecondaryBody        Sun
            BackgroundColor      #000000
            LatLonLines          On
            LatSpacing           30.000000
            LonSpacing           30.000000
            LatLonLineColor      #999999
            LatLonLineStyle      2
            ShowOrthoDistGrid    Off
            OrthoGridXSpacing    5
            OrthoGridYSpacing    5
            OrthoGridColor       #ffffff
            ShowImageExtents     Off
            ImageExtentLineColor #ffffff
            ImageExtentLineStyle 0
            ImageExtentLineWidth 1.000000
            ShowImageNames       Off
            ImageNameFont        0
            Projection           Orthographic
            Resolution           VeryLow
            CoordinateSys        ECF
            UseBackgroundImage   Off
            UseCloudsFile        Off
            BEGIN ZoomBounds
                -90.000000 -179.999999 90.000000 179.999999
            END ZoomBounds
            Zoomed               No
            SwapMapResolution    Yes
            NoneToVLowSwapDist   2000000.000000
            VLowToLowSwapDist    20000.000000
            LowToMediumSwapDist  10000.000000
            MediumToHighSwapDist 5000.000000
            HighToVHighSwapDist  1000.000000
            VHighToSHighSwapDist 100.000000
            BEGIN Axes
                DisplayAxes no
                CoordSys    CBI
                2aryCB      Sun
                Display+x   yes
                Label+x     yes
                Color+x     #ffffff
                Scale+x     3.000000
                Display-x   yes
                Label-x     yes
                Color-x     #ffffff
                Scale-x     3.000000
                Display+y   yes
                Label+y     yes
                Color+y     #ffffff
                Scale+y     3.000000
                Display-y   yes
                Label-y     yes
                Color-y     #ffffff
                Scale-y     3.000000
                Display+z   yes
                Label+z     yes
                Color+z     #ffffff
                Scale+z     3.000000
                Display-z   yes
                Label-z     yes
                Color-z     #ffffff
                Scale-z     3.000000
            END Axes

        END MapAttributes

        BEGIN Maps
            RWDB2_Coastlines    Yes #00ff00
            RWDB2_International_Borders    Yes #00ff00
            RWDB2_Islands    Yes #00ff00
            RWDB2_Lakes    Yes #87cefa
            RWDB2_Provincial_Borders    Yes #00ff00
            RWDB2_Rivers    No #00ff00
        END Maps


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\vcoppola\LOCALS~1\Temp
            BaseName         Frame
            Digits           4
            Frame            0
            LastAnimTime     0.000000
            OutputMode       Normal
            HiResAssembly    Assemble
            HRWidth          6000
            HRHeight         4500
            HRDPI            600.000000
            UseSnapInterval  No
            SnapInterval     0.000000
        END SoftVTR


        BEGIN TimeDisplay
            Show             0
            TextColor        #00ffff
            Transparent      0
            BackColor        #000000
            XPosition        20
            YPosition        -20
        END TimeDisplay

        BEGIN LightingData
            DisplayAltitude              0.000000
            SubsolarPoint                Off
            SubsolarPointColor           #ffff00
            SubsolarPointMarkerStyle     2

            ShowUmbraLine                Off
            UmbraLineColor               #ffff00
            UmbraLineStyle               0
            UmbraLineWidth               1
            FillUmbra                    Off
            UmbraFillColor               #000000
            UmbraFillStyle               7

            ShowPenumbraLines            Off
            PenumbraLineColor            #ffff00
            PenumbraLineStyle            0
            PenumbraLineWidth            1
            FillPenumbra                 Off
            PenumbraFillColor            #000000
            PenumbraFillStyle            7

            ShowSunlightLine             Off
            SunlightLineColor            #ffff00
            SunlightLineStyle            0
            SunlightLineWidth            1
            FillSunlight                 Off
            SunlightFillColor            #ffff00
            SunlightFillStyle            7

        END LightingData

        ShowDtedRegions     Off

        End Style

        BEGIN Style
        Name                Zoom_North_America
        Time                0.000000
        UpdateDelta         60.000000

        BEGIN MapAttributes
            CenterLatitude       0.000000
            CenterLongitude      0.000000
            ProjectionAltitude   63621860.000000
            FieldOfView          35.000000
            OrthoDisplayDistance 20000000.000000
            TransformTrajectory  On
            EquatorialRadius     6378137.000000
            PrimaryBody          Earth
            SecondaryBody        Sun
            BackgroundColor      #000000
            LatLonLines          On
            LatSpacing           30.000000
            LonSpacing           30.000000
            LatLonLineColor      #999999
            LatLonLineStyle      2
            ShowOrthoDistGrid    Off
            OrthoGridXSpacing    5
            OrthoGridYSpacing    5
            OrthoGridColor       #ffffff
            ShowImageExtents     Off
            ImageExtentLineColor #ffffff
            ImageExtentLineStyle 0
            ImageExtentLineWidth 1.000000
            ShowImageNames       Off
            ImageNameFont        0
            Projection           EquidistantCylindrical
            Resolution           Low
            CoordinateSys        ECF
            UseBackgroundImage   On
            BackgroundImageFile  Earth_STK42
            UseCloudsFile        Off
            BEGIN ZoomBounds
                15.776278 -171.147540 80.694310 -41.311475
                -90.000000 -179.999999 90.000000 179.999999
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
                CoordSys    CBI
                2aryCB      Sun
                Display+x   yes
                Label+x     yes
                Color+x     #ffffff
                Scale+x     3.000000
                Display-x   yes
                Label-x     yes
                Color-x     #ffffff
                Scale-x     3.000000
                Display+y   yes
                Label+y     yes
                Color+y     #ffffff
                Scale+y     3.000000
                Display-y   yes
                Label-y     yes
                Color-y     #ffffff
                Scale-y     3.000000
                Display+z   yes
                Label+z     yes
                Color+z     #ffffff
                Scale+z     3.000000
                Display-z   yes
                Label-z     yes
                Color-z     #ffffff
                Scale-z     3.000000
            END Axes

        END MapAttributes

        BEGIN Maps
            RWDB2_Coastlines    Yes #00ff00
            RWDB2_International_Borders    Yes #00ff00
            RWDB2_Islands    Yes #00ff00
            RWDB2_Lakes    Yes #87cefa
            RWDB2_Provincial_Borders    Yes #00ff00
            RWDB2_Rivers    No #00ff00
        END Maps


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\vcoppola\LOCALS~1\Temp
            BaseName         Frame
            Digits           4
            Frame            0
            LastAnimTime     0.000000
            OutputMode       Normal
            HiResAssembly    Assemble
            HRWidth          6000
            HRHeight         4500
            HRDPI            600.000000
            UseSnapInterval  No
            SnapInterval     0.000000
        END SoftVTR


        BEGIN TimeDisplay
            Show             0
            TextColor        #00ffff
            Transparent      0
            BackColor        #000000
            XPosition        20
            YPosition        -20
        END TimeDisplay

        BEGIN LightingData
            DisplayAltitude              0.000000
            SubsolarPoint                Off
            SubsolarPointColor           #ffff00
            SubsolarPointMarkerStyle     2

            ShowUmbraLine                Off
            UmbraLineColor               #ffff00
            UmbraLineStyle               0
            UmbraLineWidth               1
            FillUmbra                    Off
            UmbraFillColor               #000000
            UmbraFillStyle               7

            ShowPenumbraLines            Off
            PenumbraLineColor            #ffff00
            PenumbraLineStyle            0
            PenumbraLineWidth            1
            FillPenumbra                 Off
            PenumbraFillColor            #000000
            PenumbraFillStyle            7

            ShowSunlightLine             Off
            SunlightLineColor            #ffff00
            SunlightLineStyle            0
            SunlightLineWidth            1
            FillSunlight                 Off
            SunlightFillColor            #ffff00
            SunlightFillStyle            7

        END LightingData

        ShowDtedRegions     Off

        End Style

    END MapStyles

END MapData

        BEGIN GfxClassPref

        END GfxClassPref


        BEGIN ConnectGraphicsOptions

            AsyncPickReturnUnique          OFF

        END ConnectGraphicsOptions

    END Graphics

    BEGIN Overlays
    END Overlays

    BEGIN Broker
    END Broker

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
		ForceUnit		Newtons
		PressureUnit		Pascals
		SpecificImpulseUnit		Seconds
		PRFUnit		Kilohertz
		BandwidthUnit		Megahertz
		SmallVelocityUnit		CentimetersperSecond
		DataRateUnit		MegaBitsPerSecond
		Percent		Percentage
		UnitTemperature		UnitKelvin
		MissionModelerDistanceUnit		NauticalMiles
		MissionModelerTimeUnit		Hours
		MissionModelerAltitudeUnit		Feet
		MissionModelerFuelQuantityUnit		Pounds
		MissionModelerRunwayLengthUnit		Kilofeet
		MissionModelerBearingAngleUnit		Degrees
		MissionModelerAngleOfAttackUnit		Degrees
		MissionModelerAttitudeAngleUnit		Degrees
		MissionModelerGUnit		StandardSeaLevelG
		RadiationDoseUnit		RadsSilicon
		RadiationShieldThicknessUnit		GramsperSquareCm
		MagneticFieldUnit		nanoTesla
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
		ForceUnit		Newtons
		PressureUnit		Pascals
		SpecificImpulseUnit		Seconds
		PRFUnit		Kilohertz
		BandwidthUnit		Megahertz
		SmallVelocityUnit		CentimetersperSecond
		DataRateUnit		MegaBitsPerSecond
		Percent		Percentage
		UnitTemperature		UnitKelvin
		MissionModelerDistanceUnit		NauticalMiles
		MissionModelerTimeUnit		Hours
		MissionModelerAltitudeUnit		Feet
		MissionModelerFuelQuantityUnit		Pounds
		MissionModelerRunwayLengthUnit		Kilofeet
		MissionModelerBearingAngleUnit		Degrees
		MissionModelerAngleOfAttackUnit		Degrees
		MissionModelerAttitudeAngleUnit		Degrees
		MissionModelerGUnit		StandardSeaLevelG
		RadiationDoseUnit		RadsSilicon
		RadiationShieldThicknessUnit		GramsperSquareCm
		MagneticFieldUnit		nanoTesla
    END ReportUnits

    BEGIN ConnectReportUnits
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
		ForceUnit		Newtons
		PressureUnit		Pascals
		SpecificImpulseUnit		Seconds
		PRFUnit		Kilohertz
		BandwidthUnit		Megahertz
		SmallVelocityUnit		CentimetersperSecond
		DataRateUnit		MegaBitsPerSecond
		Percent		Percentage
		UnitTemperature		UnitKelvin
		MissionModelerDistanceUnit		NauticalMiles
		MissionModelerTimeUnit		Hours
		MissionModelerAltitudeUnit		Feet
		MissionModelerFuelQuantityUnit		Pounds
		MissionModelerRunwayLengthUnit		Kilofeet
		MissionModelerBearingAngleUnit		Degrees
		MissionModelerAngleOfAttackUnit		Degrees
		MissionModelerAttitudeAngleUnit		Degrees
		MissionModelerGUnit		StandardSeaLevelG
		RadiationDoseUnit		RadsSilicon
		RadiationShieldThicknessUnit		GramsperSquareCm
		MagneticFieldUnit		nanoTesla
    END ConnectReportUnits

    BEGIN GenDb

		BEGIN Database
		    DbType       Satellite
		    DefDb        stkSatDb.sd
		    UseMyDb      Off
		    MaxMatches   2000

		END Database

		BEGIN Database
		    DbType       City
		    DefDb        stkCityDb.cd
		    UseMyDb      Off
		    MaxMatches   2000

		END Database

		BEGIN Database
		    DbType       Facility
		    DefDb        stkFacility.fd
		    UseMyDb      Off
		    MaxMatches   2000

		END Database

		BEGIN Database
		    DbType       Star
		    DefDb        stkStarDb.bd
		    UseMyDb      Off
		    MaxMatches   2000

		END Database
    END GenDb

    BEGIN Msgp4Ext
    END Msgp4Ext

    BEGIN VectorTool
    ShowAxes      On
    ShowVector    On
    ShowPoint     On
    ShowSystem    On
    ShowAngle     On
    ShowPlane     On
    ShowAdvanced  Off
    ShowAllCB     Off
    END VectorTool

    BEGIN Author
	Optimize	Yes
	UseBasicGlobe	Yes
	PasswordProtect	No
    END Author

    BEGIN Desc
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
	EarthTemperature    290.000000
	UseCustomModelA    No
	UseCustomModelB    No
	UseCustomModelC    No

	BEGIN RainModel

		RainModelName	Crane1982

	END RainModel


	BEGIN CloudAndFog

		UseCloudFog           Off
		CloudCeiling          3.000000
		CloudThickness        0.500000
		CloudTemperature      273.150000
		CloudLiquidDensity    7.500000
		CloudWaterContent     3750.000000
	END CloudAndFog


	BEGIN TropoScintillation

		ComputeTropoScin          Off
		ComputeDeepFade           Off
		DeepFadePercent           0.100000
		RefractivityGradient      10.000000
	END TropoScintillation

    END RfEnv

    BEGIN RCS
	Inherited          False
	ClutterCoef        0.000000e+000
	BEGIN RCSBAND
		ConstantValue      0.000000e+000
		Swerling      0
		BandData      3.000000e+006 3.000000e+011
	END RCSBAND
    END RCS

    BEGIN Gator
    END Gator

    BEGIN Crdn
    END Crdn

    BEGIN SpiceExt
    END SpiceExt

    BEGIN FlightScenExt
    END FlightScenExt

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
			ReadBufferSize             1500
			QueuePollPeriod            20
			MaxRcvQueueEntries         1000
			MaxRcvIOThreads            4
			sChannelBufferSize         65000

		End Network


		Begin EntityTypeDef


#			order: kind:domain:country:catagory:subCatagory:specific:xtra ( -1 = * )


		End EntityTypeDef


		Begin EntityFilter
			Include                    *:*:*
		End EntityFilter

    END DIS

    BEGIN VO
    END VO

    BEGIN PODS
        MintimebtPasses       1800.000000
        MinObsThinTime        0.000000
        SummaryByFile         False
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
        ReferenceDate         1 Jul 2005 12:00:00.000000000
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
        MaxDegree             36
        MaxOrder              36
        FluxFile              \tables\tables.dat
        JPLFile               \ephem\jplde405.dat
        GeoFile               \gco_files\wgs84.gco
        PODSDirectory         TrkDataDirectory
        TrkDataDirectory      trk_data
        ScratchDirectory      C:\DOCUME~1\vcoppola\LOCALS~1\Temp
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
          SimMeasData		17  12300  0  0.000174532925  0.000174532925  0
          SimMeasData		18  86400  0  0.00034906585  0.000174532925  0
          SimMeasData		51  102  0  23  12  0
          SimMeasData		52  630708  0  0.044  0.066  0
        END SimData
    END PODS

END Extensions

BEGIN SubObjects

Class AreaTarget

	AreaTarget1

END Class

Class Facility

	Facility1
	Facility2
	Facility3
	Facility4
	Facility5

END Class

Class GroundVehicle

	GroundVehicle1

END Class

Class LineTarget

	LineTarget1

END Class

Class Satellite

	Satellite1

END Class

END SubObjects

END Scenario
