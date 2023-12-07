stk.v.6.1
BEGIN Scenario
    Name            Scenario1

BEGIN Epoch
    Epoch        1 Jun 2004 12:00:00.00

END Epoch

BEGIN Interval

Start               1 Jun 2004 12:00:00.000000000
Stop                2 Jun 2004 12:00:00.000000000

END Interval

BEGIN EOPFile

    EOPFilename     EOP-v1.1.txt

END EOPFile

BEGIN GlobalPrefs

    SatelliteNoOrbWarning    No
    MissileNoOrbWarning      No
END GlobalPrefs

BEGIN CentralBody

    PrimaryBody     Earth
    UseTerrainCache       Yes
    ConvertTerrainCacheToInternal       Yes

END CentralBody

BEGIN RealData

    RealDataSceneID          1
    RealDataSceneSrc         0
    RealDataOnAnimateOnly    Yes
    UseOpenGLReadIfPossible  No
    TargetAudience28Modem    0
    TargetAudience56Modem    0
    TargetAudienceSingleISDN 0
    TargetAudienceDualISDN   0
    TargetAudienceLanLow     0
    TargetAudienceLanHigh    1
    VideoQuality             Normal
    RealDataIPAddress  ""
    RealDataStreamName "realSTK.rm"
    RealDataPort             4040
    RealDataUsername         ""
    RealDataTitle            "Real STK"
    RealDataAuthor           ""
    RealDataCopyright        ""
    RealDataWebURL           "http://www.stk.com"

END RealData

BEGIN Extensions
    
    BEGIN Graphics

BEGIN Animation

    StartTime          1 Jun 2004 12:00:00.000000000
    EndTime            2 Jun 2004 12:00:00.000000000
    Direction          Forward
    UpdateDelta        60.000
    RefreshDelta       HighSpeed
    XRealTimeMult      1.000
    RealTimeOffset     0.000

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
           CreateChunkTrn  Yes
           OutputFormat    TXM
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
            Resolution           Medium
            CoordinateSys        ECF
            UseBackgroundImage   On
            BackgroundImageFile  Basic
            UseCloudsFile        Off
            BEGIN ZoomBounds
                24.136364 1.838824 43.363636 37.797961
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
            RWDB2 Coastlines    No #00ff00
            Coastlines    No #00ff00
            Major_Ice_Shelves    No #00ff00
            Minor_Ice_Shelves    No #00ff00
            RWDB2 International Borders    No #00ff00
                Rank 1: Demarcated or Delimited    No #00ff00
                Rank 2: Indefinite or Disputed    No #00ff00
                Rank 3: Lines of separation or sovereignty on land    No #00ff00
                Rank 4: Lines of separation or sovereignty at sea    No #00ff00
                Rank 5: Other lines of separation or sovereignty at sea    No #00ff00
                Rank 6: Continental shelf boundary in Persian Gulf    No #00ff00
                Rank 7: Demilitarized zone lines in Israel    No #00ff00
                Rank 8: No defined line    No #00ff00
                Rank 9: Selected claimed lines    No #00ff00
                Rank 50: Old Panama Canal Zone lines    No #00ff00
                Rank 51: Old N. Yemen-S.Yemen lines    No #00ff00
                Rank 52: Old Jordan-Iraq lines    No #00ff00
                Rank 53: Old Iraq-Saudi Arabia Neutral Zone lines    No #00ff00
                Rank 54: Old East Germany-West Germany and Berlin lines    No #00ff00
                Rank 55: Old N. Vietnam-S. Vietnam boundary    No #00ff00
                Rank 56: Old Vietnam DMZ lines    No #00ff00
                Rank 57: Old Kuwait-Saudi Arabia Neutral Zone lines    No #00ff00
                Rank 58: Old Oman-Yemen line of separation    No #00ff00
            RWDB2 Islands    No #00ff00
                Rank 1: Major islands    No #00ff00
                Rank 2: Additional major islands    No #00ff00
                Rank 3: Moderately important islands    No #00ff00
                Rank 4: Additional islands    No #00ff00
                Rank 5: Minor islands    No #00ff00
                Rank 6: Very small minor islands    No #00ff00
                Rank 8: Reefs    No #00ff00
                Rank 9: Shoals    No #00ff00
            RWDB2 Lakes    No #00ff00
                Rank 1: Lakes that should appear on all maps    No #00ff00
                Rank 2: Major lakes    No #00ff00
                Rank 3: Additional major lakes    No #00ff00
                Rank 4: Intermediate lakes    No #00ff00
                Rank 5: Minor lakes    No #00ff00
                Rank 6: Additional minor lakes    No #00ff00
                Rank 7: Swamps    No #00ff00
                Rank 11: Intermittent major lakes    No #00ff00
                Rank 12: Intermittent minor lakes    No #00ff00
                Rank 14: Major salt pans    No #00ff00
                Rank 15: Minor salt pans    No #00ff00
                Rank 23: Glaciers    No #00ff00
            RWDB2 Provincial Borders    No #00ff00
                Rank 1: First order    No #00ff00
                Rank 2: Second order    No #00ff00
                Rank 3: Third order    No #00ff00
                Rank 4: Special boundaries    No #00ff00
                Rank 54: Pre-unification German administration lines    No #00ff00
                Rank 61: First order boundaries in the water    No #00ff00
                Rank 62: Second order boundaries in the water    No #00ff00
                Rank 99: Disputed lines    No #00ff00
            RWDB2 Rivers    No #00ff00
                Rank 1: Major rivers    No #00ff00
                Rank 2: Additional major rivers    No #00ff00
                Rank 3: Intermediate rivers    No #00ff00
                Rank 4: Additional intermediate rivers    No #00ff00
                Rank 5: Minor rivers    No #00ff00
                Rank 6: Additional minor rivers    No #00ff00
                Rank 10: Major intermittent rivers    No #00ff00
                Rank 11: Intermediate intermittent rivers    No #00ff00
                Rank 12: Minor intermittent rivers    No #00ff00
                Rank 21: Major canals    No #00ff00
                Rank 22: Minor canals    No #00ff00
                Rank 23: Irrigation canals    No #00ff00
            RWDB2_Coastlines    Yes #0c0000
            Coastlines    No #00ff00
            Major_Ice_Shelves    No #00ff00
            Minor_Ice_Shelves    No #00ff00
            RWDB2_International_Borders    Yes #0c0000
            Demarcated_or_Delimited    No #00ff00
            Indefinite_or_Disputed    No #00ff00
            Lines_of_separation_on_land    No #00ff00
            Lines_of_separation_at_sea    No #00ff00
            Other_lines_of_separation_at_sea    No #00ff00
            Continental_shelf_boundary_in_Persian_Gulf    No #00ff00
            Demilitarized_zone_lines_in_Israel    No #00ff00
            No_defined_line    No #00ff00
            Selected_claimed_lines    No #00ff00
            Old_Panama_Canal_Zone_lines    No #00ff00
            Old_North-South_Yemen_lines    No #00ff00
            Old_Jordan-Iraq_lines    No #00ff00
            Old_Iraq-Saudi_Arabia_Neutral_Zone_lines    No #00ff00
            Old_East-West_Germany_and_Berlin_lines    No #00ff00
            Old_North-South_Vietnam_boundary    No #00ff00
            Old_Vietnam_DMZ_lines    No #00ff00
            Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines    No #00ff00
            Old_Oman-Yemen_line_of_separation    No #00ff00
            RWDB2_Islands    Yes #0c0000
            Major_islands    No #00ff00
            Additional_major_islands    No #00ff00
            Moderately_important_islands    No #00ff00
            Additional_islands    No #00ff00
            Minor_islands    No #00ff00
            Very_small_minor_islands    No #00ff00
            Reefs    No #00ff00
            Shoals    No #00ff00
            RWDB2_Lakes    No #090000
            Lakes_that_should_appear_on_all_maps    No #00ff00
            Major_lakes    No #00ff00
            Additional_major_lakes    No #00ff00
            Intermediate_lakes    No #00ff00
            Minor_lakes    No #00ff00
            Additional_minor_lakes    No #00ff00
            Swamps    No #00ff00
            Intermittent_major_lakes    No #00ff00
            Intermittent_minor_lakes    No #00ff00
            Major_salt_pans    No #00ff00
            Minor_salt_pans    No #00ff00
            Glaciers    No #00ff00
            RWDB2_Provincial_Borders    No #0c0000
            First_order    No #00ff00
            Second_order    No #00ff00
            Third_order    No #00ff00
            Special_boundaries    No #00ff00
            Pre-unification_German_administration_lines    No #00ff00
            First_order_boundaries_on_water    No #00ff00
            Second_order_boundaries_on_water    No #00ff00
            Disputed_lines    No #00ff00
            RWDB2_Rivers    No #090000
            Major_rivers    No #00ff00
            Additional_major_rivers    No #00ff00
            Intermediate_rivers    No #00ff00
            Additional_intermediate_rivers    No #00ff00
            Minor_rivers    No #00ff00
            Additional_minor_rivers    No #00ff00
            Major_intermittent_rivers    No #00ff00
            Intermediate_intermittent_rivers    No #00ff00
            Minor_intermittent_rivers    No #00ff00
            Major_canals    No #00ff00
            Minor_canals    No #00ff00
            Irrigation_canals    No #00ff00
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
            Directory        C:\DOCUME~1\sdupont\LOCALS~1\Temp
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
            RWDB2 Coastlines    No #00ff00
            Coastlines    No #00ff00
            Major_Ice_Shelves    No #00ff00
            Minor_Ice_Shelves    No #00ff00
            RWDB2 International Borders    No #00ff00
                Rank 1: Demarcated or Delimited    No #00ff00
                Rank 2: Indefinite or Disputed    No #00ff00
                Rank 3: Lines of separation or sovereignty on land    No #00ff00
                Rank 4: Lines of separation or sovereignty at sea    No #00ff00
                Rank 5: Other lines of separation or sovereignty at sea    No #00ff00
                Rank 6: Continental shelf boundary in Persian Gulf    No #00ff00
                Rank 7: Demilitarized zone lines in Israel    No #00ff00
                Rank 8: No defined line    No #00ff00
                Rank 9: Selected claimed lines    No #00ff00
                Rank 50: Old Panama Canal Zone lines    No #00ff00
                Rank 51: Old N. Yemen-S.Yemen lines    No #00ff00
                Rank 52: Old Jordan-Iraq lines    No #00ff00
                Rank 53: Old Iraq-Saudi Arabia Neutral Zone lines    No #00ff00
                Rank 54: Old East Germany-West Germany and Berlin lines    No #00ff00
                Rank 55: Old N. Vietnam-S. Vietnam boundary    No #00ff00
                Rank 56: Old Vietnam DMZ lines    No #00ff00
                Rank 57: Old Kuwait-Saudi Arabia Neutral Zone lines    No #00ff00
                Rank 58: Old Oman-Yemen line of separation    No #00ff00
            RWDB2 Islands    No #00ff00
                Rank 1: Major islands    No #00ff00
                Rank 2: Additional major islands    No #00ff00
                Rank 3: Moderately important islands    No #00ff00
                Rank 4: Additional islands    No #00ff00
                Rank 5: Minor islands    No #00ff00
                Rank 6: Very small minor islands    No #00ff00
                Rank 8: Reefs    No #00ff00
                Rank 9: Shoals    No #00ff00
            RWDB2 Lakes    No #00ff00
                Rank 1: Lakes that should appear on all maps    No #00ff00
                Rank 2: Major lakes    No #00ff00
                Rank 3: Additional major lakes    No #00ff00
                Rank 4: Intermediate lakes    No #00ff00
                Rank 5: Minor lakes    No #00ff00
                Rank 6: Additional minor lakes    No #00ff00
                Rank 7: Swamps    No #00ff00
                Rank 11: Intermittent major lakes    No #00ff00
                Rank 12: Intermittent minor lakes    No #00ff00
                Rank 14: Major salt pans    No #00ff00
                Rank 15: Minor salt pans    No #00ff00
                Rank 23: Glaciers    No #00ff00
            RWDB2 Provincial Borders    No #00ff00
                Rank 1: First order    No #00ff00
                Rank 2: Second order    No #00ff00
                Rank 3: Third order    No #00ff00
                Rank 4: Special boundaries    No #00ff00
                Rank 54: Pre-unification German administration lines    No #00ff00
                Rank 61: First order boundaries in the water    No #00ff00
                Rank 62: Second order boundaries in the water    No #00ff00
                Rank 99: Disputed lines    No #00ff00
            RWDB2 Rivers    No #00ff00
                Rank 1: Major rivers    No #00ff00
                Rank 2: Additional major rivers    No #00ff00
                Rank 3: Intermediate rivers    No #00ff00
                Rank 4: Additional intermediate rivers    No #00ff00
                Rank 5: Minor rivers    No #00ff00
                Rank 6: Additional minor rivers    No #00ff00
                Rank 10: Major intermittent rivers    No #00ff00
                Rank 11: Intermediate intermittent rivers    No #00ff00
                Rank 12: Minor intermittent rivers    No #00ff00
                Rank 21: Major canals    No #00ff00
                Rank 22: Minor canals    No #00ff00
                Rank 23: Irrigation canals    No #00ff00
            RWDB2_Coastlines    Yes #000000
            Coastlines    No #00ff00
            Major_Ice_Shelves    No #00ff00
            Minor_Ice_Shelves    No #00ff00
            RWDB2_International_Borders    Yes #000000
            Demarcated_or_Delimited    No #00ff00
            Indefinite_or_Disputed    No #00ff00
            Lines_of_separation_on_land    No #00ff00
            Lines_of_separation_at_sea    No #00ff00
            Other_lines_of_separation_at_sea    No #00ff00
            Continental_shelf_boundary_in_Persian_Gulf    No #00ff00
            Demilitarized_zone_lines_in_Israel    No #00ff00
            No_defined_line    No #00ff00
            Selected_claimed_lines    No #00ff00
            Old_Panama_Canal_Zone_lines    No #00ff00
            Old_North-South_Yemen_lines    No #00ff00
            Old_Jordan-Iraq_lines    No #00ff00
            Old_Iraq-Saudi_Arabia_Neutral_Zone_lines    No #00ff00
            Old_East-West_Germany_and_Berlin_lines    No #00ff00
            Old_North-South_Vietnam_boundary    No #00ff00
            Old_Vietnam_DMZ_lines    No #00ff00
            Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines    No #00ff00
            Old_Oman-Yemen_line_of_separation    No #00ff00
            RWDB2_Islands    Yes #000000
            Major_islands    No #00ff00
            Additional_major_islands    No #00ff00
            Moderately_important_islands    No #00ff00
            Additional_islands    No #00ff00
            Minor_islands    No #00ff00
            Very_small_minor_islands    No #00ff00
            Reefs    No #00ff00
            Shoals    No #00ff00
            RWDB2_Lakes    Yes #090000
            Lakes_that_should_appear_on_all_maps    No #00ff00
            Major_lakes    No #00ff00
            Additional_major_lakes    No #00ff00
            Intermediate_lakes    No #00ff00
            Minor_lakes    No #00ff00
            Additional_minor_lakes    No #00ff00
            Swamps    No #00ff00
            Intermittent_major_lakes    No #00ff00
            Intermittent_minor_lakes    No #00ff00
            Major_salt_pans    No #00ff00
            Minor_salt_pans    No #00ff00
            Glaciers    No #00ff00
            RWDB2_Provincial_Borders    Yes #000000
            First_order    No #00ff00
            Second_order    No #00ff00
            Third_order    No #00ff00
            Special_boundaries    No #00ff00
            Pre-unification_German_administration_lines    No #00ff00
            First_order_boundaries_on_water    No #00ff00
            Second_order_boundaries_on_water    No #00ff00
            Disputed_lines    No #00ff00
            RWDB2_Rivers    No #000000
            Major_rivers    No #00ff00
            Additional_major_rivers    No #00ff00
            Intermediate_rivers    No #00ff00
            Additional_intermediate_rivers    No #00ff00
            Minor_rivers    No #00ff00
            Additional_minor_rivers    No #00ff00
            Major_intermittent_rivers    No #00ff00
            Intermediate_intermittent_rivers    No #00ff00
            Minor_intermittent_rivers    No #00ff00
            Major_canals    No #00ff00
            Minor_canals    No #00ff00
            Irrigation_canals    No #00ff00
        END Maps


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\sdupont\LOCALS~1\Temp
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
            RWDB2 Coastlines    No #00ff00
            Coastlines    No #00ff00
            Major_Ice_Shelves    No #00ff00
            Minor_Ice_Shelves    No #00ff00
            RWDB2 International Borders    No #00ff00
                Rank 1: Demarcated or Delimited    No #00ff00
                Rank 2: Indefinite or Disputed    No #00ff00
                Rank 3: Lines of separation or sovereignty on land    No #00ff00
                Rank 4: Lines of separation or sovereignty at sea    No #00ff00
                Rank 5: Other lines of separation or sovereignty at sea    No #00ff00
                Rank 6: Continental shelf boundary in Persian Gulf    No #00ff00
                Rank 7: Demilitarized zone lines in Israel    No #00ff00
                Rank 8: No defined line    No #00ff00
                Rank 9: Selected claimed lines    No #00ff00
                Rank 50: Old Panama Canal Zone lines    No #00ff00
                Rank 51: Old N. Yemen-S.Yemen lines    No #00ff00
                Rank 52: Old Jordan-Iraq lines    No #00ff00
                Rank 53: Old Iraq-Saudi Arabia Neutral Zone lines    No #00ff00
                Rank 54: Old East Germany-West Germany and Berlin lines    No #00ff00
                Rank 55: Old N. Vietnam-S. Vietnam boundary    No #00ff00
                Rank 56: Old Vietnam DMZ lines    No #00ff00
                Rank 57: Old Kuwait-Saudi Arabia Neutral Zone lines    No #00ff00
                Rank 58: Old Oman-Yemen line of separation    No #00ff00
            RWDB2 Islands    No #00ff00
                Rank 1: Major islands    No #00ff00
                Rank 2: Additional major islands    No #00ff00
                Rank 3: Moderately important islands    No #00ff00
                Rank 4: Additional islands    No #00ff00
                Rank 5: Minor islands    No #00ff00
                Rank 6: Very small minor islands    No #00ff00
                Rank 8: Reefs    No #00ff00
                Rank 9: Shoals    No #00ff00
            RWDB2 Lakes    No #00ff00
                Rank 1: Lakes that should appear on all maps    No #00ff00
                Rank 2: Major lakes    No #00ff00
                Rank 3: Additional major lakes    No #00ff00
                Rank 4: Intermediate lakes    No #00ff00
                Rank 5: Minor lakes    No #00ff00
                Rank 6: Additional minor lakes    No #00ff00
                Rank 7: Swamps    No #00ff00
                Rank 11: Intermittent major lakes    No #00ff00
                Rank 12: Intermittent minor lakes    No #00ff00
                Rank 14: Major salt pans    No #00ff00
                Rank 15: Minor salt pans    No #00ff00
                Rank 23: Glaciers    No #00ff00
            RWDB2 Provincial Borders    No #00ff00
                Rank 1: First order    No #00ff00
                Rank 2: Second order    No #00ff00
                Rank 3: Third order    No #00ff00
                Rank 4: Special boundaries    No #00ff00
                Rank 54: Pre-unification German administration lines    No #00ff00
                Rank 61: First order boundaries in the water    No #00ff00
                Rank 62: Second order boundaries in the water    No #00ff00
                Rank 99: Disputed lines    No #00ff00
            RWDB2 Rivers    No #00ff00
                Rank 1: Major rivers    No #00ff00
                Rank 2: Additional major rivers    No #00ff00
                Rank 3: Intermediate rivers    No #00ff00
                Rank 4: Additional intermediate rivers    No #00ff00
                Rank 5: Minor rivers    No #00ff00
                Rank 6: Additional minor rivers    No #00ff00
                Rank 10: Major intermittent rivers    No #00ff00
                Rank 11: Intermediate intermittent rivers    No #00ff00
                Rank 12: Minor intermittent rivers    No #00ff00
                Rank 21: Major canals    No #00ff00
                Rank 22: Minor canals    No #00ff00
                Rank 23: Irrigation canals    No #00ff00
            RWDB2_Coastlines    Yes #0c0000
            Coastlines    No #00ff00
            Major_Ice_Shelves    No #00ff00
            Minor_Ice_Shelves    No #00ff00
            RWDB2_International_Borders    Yes #0c0000
            Demarcated_or_Delimited    No #00ff00
            Indefinite_or_Disputed    No #00ff00
            Lines_of_separation_on_land    No #00ff00
            Lines_of_separation_at_sea    No #00ff00
            Other_lines_of_separation_at_sea    No #00ff00
            Continental_shelf_boundary_in_Persian_Gulf    No #00ff00
            Demilitarized_zone_lines_in_Israel    No #00ff00
            No_defined_line    No #00ff00
            Selected_claimed_lines    No #00ff00
            Old_Panama_Canal_Zone_lines    No #00ff00
            Old_North-South_Yemen_lines    No #00ff00
            Old_Jordan-Iraq_lines    No #00ff00
            Old_Iraq-Saudi_Arabia_Neutral_Zone_lines    No #00ff00
            Old_East-West_Germany_and_Berlin_lines    No #00ff00
            Old_North-South_Vietnam_boundary    No #00ff00
            Old_Vietnam_DMZ_lines    No #00ff00
            Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines    No #00ff00
            Old_Oman-Yemen_line_of_separation    No #00ff00
            RWDB2_Islands    Yes #0c0000
            Major_islands    No #00ff00
            Additional_major_islands    No #00ff00
            Moderately_important_islands    No #00ff00
            Additional_islands    No #00ff00
            Minor_islands    No #00ff00
            Very_small_minor_islands    No #00ff00
            Reefs    No #00ff00
            Shoals    No #00ff00
            RWDB2_Lakes    No #000000
            Lakes_that_should_appear_on_all_maps    No #00ff00
            Major_lakes    No #00ff00
            Additional_major_lakes    No #00ff00
            Intermediate_lakes    No #00ff00
            Minor_lakes    No #00ff00
            Additional_minor_lakes    No #00ff00
            Swamps    No #00ff00
            Intermittent_major_lakes    No #00ff00
            Intermittent_minor_lakes    No #00ff00
            Major_salt_pans    No #00ff00
            Minor_salt_pans    No #00ff00
            Glaciers    No #00ff00
            RWDB2_Provincial_Borders    No #000000
            First_order    No #00ff00
            Second_order    No #00ff00
            Third_order    No #00ff00
            Special_boundaries    No #00ff00
            Pre-unification_German_administration_lines    No #00ff00
            First_order_boundaries_on_water    No #00ff00
            Second_order_boundaries_on_water    No #00ff00
            Disputed_lines    No #00ff00
            RWDB2_Rivers    No #000000
            Major_rivers    No #00ff00
            Additional_major_rivers    No #00ff00
            Intermediate_rivers    No #00ff00
            Additional_intermediate_rivers    No #00ff00
            Minor_rivers    No #00ff00
            Additional_minor_rivers    No #00ff00
            Major_intermittent_rivers    No #00ff00
            Intermediate_intermittent_rivers    No #00ff00
            Minor_intermittent_rivers    No #00ff00
            Major_canals    No #00ff00
            Minor_canals    No #00ff00
            Irrigation_canals    No #00ff00
        END Maps


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\sdupont\LOCALS~1\Temp
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
            RWDB2 Coastlines    No #00ff00
            Coastlines    No #00ff00
            Major_Ice_Shelves    No #00ff00
            Minor_Ice_Shelves    No #00ff00
            RWDB2 International Borders    No #00ff00
                Rank 1: Demarcated or Delimited    No #00ff00
                Rank 2: Indefinite or Disputed    No #00ff00
                Rank 3: Lines of separation or sovereignty on land    No #00ff00
                Rank 4: Lines of separation or sovereignty at sea    No #00ff00
                Rank 5: Other lines of separation or sovereignty at sea    No #00ff00
                Rank 6: Continental shelf boundary in Persian Gulf    No #00ff00
                Rank 7: Demilitarized zone lines in Israel    No #00ff00
                Rank 8: No defined line    No #00ff00
                Rank 9: Selected claimed lines    No #00ff00
                Rank 50: Old Panama Canal Zone lines    No #00ff00
                Rank 51: Old N. Yemen-S.Yemen lines    No #00ff00
                Rank 52: Old Jordan-Iraq lines    No #00ff00
                Rank 53: Old Iraq-Saudi Arabia Neutral Zone lines    No #00ff00
                Rank 54: Old East Germany-West Germany and Berlin lines    No #00ff00
                Rank 55: Old N. Vietnam-S. Vietnam boundary    No #00ff00
                Rank 56: Old Vietnam DMZ lines    No #00ff00
                Rank 57: Old Kuwait-Saudi Arabia Neutral Zone lines    No #00ff00
                Rank 58: Old Oman-Yemen line of separation    No #00ff00
            RWDB2 Islands    No #00ff00
                Rank 1: Major islands    No #00ff00
                Rank 2: Additional major islands    No #00ff00
                Rank 3: Moderately important islands    No #00ff00
                Rank 4: Additional islands    No #00ff00
                Rank 5: Minor islands    No #00ff00
                Rank 6: Very small minor islands    No #00ff00
                Rank 8: Reefs    No #00ff00
                Rank 9: Shoals    No #00ff00
            RWDB2 Lakes    No #00ff00
                Rank 1: Lakes that should appear on all maps    No #00ff00
                Rank 2: Major lakes    No #00ff00
                Rank 3: Additional major lakes    No #00ff00
                Rank 4: Intermediate lakes    No #00ff00
                Rank 5: Minor lakes    No #00ff00
                Rank 6: Additional minor lakes    No #00ff00
                Rank 7: Swamps    No #00ff00
                Rank 11: Intermittent major lakes    No #00ff00
                Rank 12: Intermittent minor lakes    No #00ff00
                Rank 14: Major salt pans    No #00ff00
                Rank 15: Minor salt pans    No #00ff00
                Rank 23: Glaciers    No #00ff00
            RWDB2 Provincial Borders    No #00ff00
                Rank 1: First order    No #00ff00
                Rank 2: Second order    No #00ff00
                Rank 3: Third order    No #00ff00
                Rank 4: Special boundaries    No #00ff00
                Rank 54: Pre-unification German administration lines    No #00ff00
                Rank 61: First order boundaries in the water    No #00ff00
                Rank 62: Second order boundaries in the water    No #00ff00
                Rank 99: Disputed lines    No #00ff00
            RWDB2 Rivers    No #00ff00
                Rank 1: Major rivers    No #00ff00
                Rank 2: Additional major rivers    No #00ff00
                Rank 3: Intermediate rivers    No #00ff00
                Rank 4: Additional intermediate rivers    No #00ff00
                Rank 5: Minor rivers    No #00ff00
                Rank 6: Additional minor rivers    No #00ff00
                Rank 10: Major intermittent rivers    No #00ff00
                Rank 11: Intermediate intermittent rivers    No #00ff00
                Rank 12: Minor intermittent rivers    No #00ff00
                Rank 21: Major canals    No #00ff00
                Rank 22: Minor canals    No #00ff00
                Rank 23: Irrigation canals    No #00ff00
            RWDB2_Coastlines    Yes #000000
            Coastlines    No #00ff00
            Major_Ice_Shelves    No #00ff00
            Minor_Ice_Shelves    No #00ff00
            RWDB2_International_Borders    Yes #000000
            Demarcated_or_Delimited    No #00ff00
            Indefinite_or_Disputed    No #00ff00
            Lines_of_separation_on_land    No #00ff00
            Lines_of_separation_at_sea    No #00ff00
            Other_lines_of_separation_at_sea    No #00ff00
            Continental_shelf_boundary_in_Persian_Gulf    No #00ff00
            Demilitarized_zone_lines_in_Israel    No #00ff00
            No_defined_line    No #00ff00
            Selected_claimed_lines    No #00ff00
            Old_Panama_Canal_Zone_lines    No #00ff00
            Old_North-South_Yemen_lines    No #00ff00
            Old_Jordan-Iraq_lines    No #00ff00
            Old_Iraq-Saudi_Arabia_Neutral_Zone_lines    No #00ff00
            Old_East-West_Germany_and_Berlin_lines    No #00ff00
            Old_North-South_Vietnam_boundary    No #00ff00
            Old_Vietnam_DMZ_lines    No #00ff00
            Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines    No #00ff00
            Old_Oman-Yemen_line_of_separation    No #00ff00
            RWDB2_Islands    Yes #000000
            Major_islands    No #00ff00
            Additional_major_islands    No #00ff00
            Moderately_important_islands    No #00ff00
            Additional_islands    No #00ff00
            Minor_islands    No #00ff00
            Very_small_minor_islands    No #00ff00
            Reefs    No #00ff00
            Shoals    No #00ff00
            RWDB2_Lakes    Yes #090000
            Lakes_that_should_appear_on_all_maps    No #00ff00
            Major_lakes    No #00ff00
            Additional_major_lakes    No #00ff00
            Intermediate_lakes    No #00ff00
            Minor_lakes    No #00ff00
            Additional_minor_lakes    No #00ff00
            Swamps    No #00ff00
            Intermittent_major_lakes    No #00ff00
            Intermittent_minor_lakes    No #00ff00
            Major_salt_pans    No #00ff00
            Minor_salt_pans    No #00ff00
            Glaciers    No #00ff00
            RWDB2_Provincial_Borders    Yes #000000
            First_order    No #00ff00
            Second_order    No #00ff00
            Third_order    No #00ff00
            Special_boundaries    No #00ff00
            Pre-unification_German_administration_lines    No #00ff00
            First_order_boundaries_on_water    No #00ff00
            Second_order_boundaries_on_water    No #00ff00
            Disputed_lines    No #00ff00
            RWDB2_Rivers    No #000000
            Major_rivers    No #00ff00
            Additional_major_rivers    No #00ff00
            Intermediate_rivers    No #00ff00
            Additional_intermediate_rivers    No #00ff00
            Minor_rivers    No #00ff00
            Additional_minor_rivers    No #00ff00
            Major_intermittent_rivers    No #00ff00
            Intermediate_intermittent_rivers    No #00ff00
            Minor_intermittent_rivers    No #00ff00
            Major_canals    No #00ff00
            Minor_canals    No #00ff00
            Irrigation_canals    No #00ff00
        END Maps


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\sdupont\LOCALS~1\Temp
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
            RWDB2 Coastlines    No #00ff00
            Coastlines    No #00ff00
            Major_Ice_Shelves    No #00ff00
            Minor_Ice_Shelves    No #00ff00
            RWDB2 International Borders    No #00ff00
                Rank 1: Demarcated or Delimited    No #00ff00
                Rank 2: Indefinite or Disputed    No #00ff00
                Rank 3: Lines of separation or sovereignty on land    No #00ff00
                Rank 4: Lines of separation or sovereignty at sea    No #00ff00
                Rank 5: Other lines of separation or sovereignty at sea    No #00ff00
                Rank 6: Continental shelf boundary in Persian Gulf    No #00ff00
                Rank 7: Demilitarized zone lines in Israel    No #00ff00
                Rank 8: No defined line    No #00ff00
                Rank 9: Selected claimed lines    No #00ff00
                Rank 50: Old Panama Canal Zone lines    No #00ff00
                Rank 51: Old N. Yemen-S.Yemen lines    No #00ff00
                Rank 52: Old Jordan-Iraq lines    No #00ff00
                Rank 53: Old Iraq-Saudi Arabia Neutral Zone lines    No #00ff00
                Rank 54: Old East Germany-West Germany and Berlin lines    No #00ff00
                Rank 55: Old N. Vietnam-S. Vietnam boundary    No #00ff00
                Rank 56: Old Vietnam DMZ lines    No #00ff00
                Rank 57: Old Kuwait-Saudi Arabia Neutral Zone lines    No #00ff00
                Rank 58: Old Oman-Yemen line of separation    No #00ff00
            RWDB2 Islands    No #00ff00
                Rank 1: Major islands    No #00ff00
                Rank 2: Additional major islands    No #00ff00
                Rank 3: Moderately important islands    No #00ff00
                Rank 4: Additional islands    No #00ff00
                Rank 5: Minor islands    No #00ff00
                Rank 6: Very small minor islands    No #00ff00
                Rank 8: Reefs    No #00ff00
                Rank 9: Shoals    No #00ff00
            RWDB2 Lakes    No #00ff00
                Rank 1: Lakes that should appear on all maps    No #00ff00
                Rank 2: Major lakes    No #00ff00
                Rank 3: Additional major lakes    No #00ff00
                Rank 4: Intermediate lakes    No #00ff00
                Rank 5: Minor lakes    No #00ff00
                Rank 6: Additional minor lakes    No #00ff00
                Rank 7: Swamps    No #00ff00
                Rank 11: Intermittent major lakes    No #00ff00
                Rank 12: Intermittent minor lakes    No #00ff00
                Rank 14: Major salt pans    No #00ff00
                Rank 15: Minor salt pans    No #00ff00
                Rank 23: Glaciers    No #00ff00
            RWDB2 Provincial Borders    No #00ff00
                Rank 1: First order    No #00ff00
                Rank 2: Second order    No #00ff00
                Rank 3: Third order    No #00ff00
                Rank 4: Special boundaries    No #00ff00
                Rank 54: Pre-unification German administration lines    No #00ff00
                Rank 61: First order boundaries in the water    No #00ff00
                Rank 62: Second order boundaries in the water    No #00ff00
                Rank 99: Disputed lines    No #00ff00
            RWDB2 Rivers    No #00ff00
                Rank 1: Major rivers    No #00ff00
                Rank 2: Additional major rivers    No #00ff00
                Rank 3: Intermediate rivers    No #00ff00
                Rank 4: Additional intermediate rivers    No #00ff00
                Rank 5: Minor rivers    No #00ff00
                Rank 6: Additional minor rivers    No #00ff00
                Rank 10: Major intermittent rivers    No #00ff00
                Rank 11: Intermediate intermittent rivers    No #00ff00
                Rank 12: Minor intermittent rivers    No #00ff00
                Rank 21: Major canals    No #00ff00
                Rank 22: Minor canals    No #00ff00
                Rank 23: Irrigation canals    No #00ff00
            RWDB2_Coastlines    Yes #000000
            Coastlines    No #00ff00
            Major_Ice_Shelves    No #00ff00
            Minor_Ice_Shelves    No #00ff00
            RWDB2_International_Borders    Yes #000000
            Demarcated_or_Delimited    No #00ff00
            Indefinite_or_Disputed    No #00ff00
            Lines_of_separation_on_land    No #00ff00
            Lines_of_separation_at_sea    No #00ff00
            Other_lines_of_separation_at_sea    No #00ff00
            Continental_shelf_boundary_in_Persian_Gulf    No #00ff00
            Demilitarized_zone_lines_in_Israel    No #00ff00
            No_defined_line    No #00ff00
            Selected_claimed_lines    No #00ff00
            Old_Panama_Canal_Zone_lines    No #00ff00
            Old_North-South_Yemen_lines    No #00ff00
            Old_Jordan-Iraq_lines    No #00ff00
            Old_Iraq-Saudi_Arabia_Neutral_Zone_lines    No #00ff00
            Old_East-West_Germany_and_Berlin_lines    No #00ff00
            Old_North-South_Vietnam_boundary    No #00ff00
            Old_Vietnam_DMZ_lines    No #00ff00
            Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines    No #00ff00
            Old_Oman-Yemen_line_of_separation    No #00ff00
            RWDB2_Islands    Yes #000000
            Major_islands    No #00ff00
            Additional_major_islands    No #00ff00
            Moderately_important_islands    No #00ff00
            Additional_islands    No #00ff00
            Minor_islands    No #00ff00
            Very_small_minor_islands    No #00ff00
            Reefs    No #00ff00
            Shoals    No #00ff00
            RWDB2_Lakes    Yes #090000
            Lakes_that_should_appear_on_all_maps    No #00ff00
            Major_lakes    No #00ff00
            Additional_major_lakes    No #00ff00
            Intermediate_lakes    No #00ff00
            Minor_lakes    No #00ff00
            Additional_minor_lakes    No #00ff00
            Swamps    No #00ff00
            Intermittent_major_lakes    No #00ff00
            Intermittent_minor_lakes    No #00ff00
            Major_salt_pans    No #00ff00
            Minor_salt_pans    No #00ff00
            Glaciers    No #00ff00
            RWDB2_Provincial_Borders    Yes #000000
            First_order    No #00ff00
            Second_order    No #00ff00
            Third_order    No #00ff00
            Special_boundaries    No #00ff00
            Pre-unification_German_administration_lines    No #00ff00
            First_order_boundaries_on_water    No #00ff00
            Second_order_boundaries_on_water    No #00ff00
            Disputed_lines    No #00ff00
            RWDB2_Rivers    No #000000
            Major_rivers    No #00ff00
            Additional_major_rivers    No #00ff00
            Intermediate_rivers    No #00ff00
            Additional_intermediate_rivers    No #00ff00
            Minor_rivers    No #00ff00
            Additional_minor_rivers    No #00ff00
            Major_intermittent_rivers    No #00ff00
            Intermediate_intermittent_rivers    No #00ff00
            Minor_intermittent_rivers    No #00ff00
            Major_canals    No #00ff00
            Minor_canals    No #00ff00
            Irrigation_canals    No #00ff00
        END Maps


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\sdupont\LOCALS~1\Temp
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
		PowerSpectralDensityUnit		Decibels(WattsperHertz)
		ForceUnit		Newtons
		PressureUnit		Pascals
		SpecificImpulseUnit		Seconds
		PRFUnit		Kilohertz
		BandwidthUnit		Megahertz
		SmallVelocityUnit		CentimetersperSecond
		DataRateUnit		MegaBitsPerSecond
		Percent		Percentage
		PowerFluxDensityUnit		Decibels(Wattspermetersquared)
		SpectralDensityUnit		Decibel-Hertz
		FlightAircraftDistanceUnit		NauticalMiles
		FlightAircraftTimeUnit		Hours
		FlightAltitudeUnit		Feet
		FlightFuelQuantityUnit		Pounds
		FlightRunwayLengthUnit		Kilofeet
		FlightBearingAngleUnit		Degrees
		FlightAngleOfAttackUnit		Degrees
		FlightAttitudeAngleUnit		Degrees
		FlightGUnit		StandardSeaLevelG
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
		PowerSpectralDensityUnit		Decibels(WattsperHertz)
		ForceUnit		Newtons
		PressureUnit		Pascals
		SpecificImpulseUnit		Seconds
		PRFUnit		Kilohertz
		BandwidthUnit		Megahertz
		SmallVelocityUnit		CentimetersperSecond
		DataRateUnit		MegaBitsPerSecond
		Percent		Percentage
		PowerFluxDensityUnit		Decibels(Wattspermetersquared)
		SpectralDensityUnit		Decibel-Hertz
		FlightAircraftDistanceUnit		NauticalMiles
		FlightAircraftTimeUnit		Hours
		FlightAltitudeUnit		Feet
		FlightFuelQuantityUnit		Pounds
		FlightRunwayLengthUnit		Kilofeet
		FlightBearingAngleUnit		Degrees
		FlightAngleOfAttackUnit		Degrees
		FlightAttitudeAngleUnit		Degrees
		FlightGUnit		StandardSeaLevelG
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
		PowerSpectralDensityUnit		Decibels(WattsperHertz)
		ForceUnit		Newtons
		PressureUnit		Pascals
		SpecificImpulseUnit		Seconds
		PRFUnit		Kilohertz
		BandwidthUnit		Megahertz
		SmallVelocityUnit		CentimetersperSecond
		DataRateUnit		MegaBitsPerSecond
		Percent		Percentage
		PowerFluxDensityUnit		Decibels(Wattspermetersquared)
		SpectralDensityUnit		Decibel-Hertz
		FlightAircraftDistanceUnit		NauticalMiles
		FlightAircraftTimeUnit		Hours
		FlightAltitudeUnit		Feet
		FlightFuelQuantityUnit		Pounds
		FlightRunwayLengthUnit		Kilofeet
		FlightBearingAngleUnit		Degrees
		FlightAngleOfAttackUnit		Degrees
		FlightAttitudeAngleUnit		Degrees
		FlightGUnit		StandardSeaLevelG
		RadiationDoseUnit		RadsSilicon
		RadiationShieldThicknessUnit		GramsperSquareCm
		MagneticFieldUnit		nanoTesla
    END ConnectReportUnits
    
    BEGIN GenDb

		BEGIN Database
		    DbType       Satellite
		    DefDb        stkSatDb.sd
		    UseMyDb      Off
		    MyDb         .\stkSatDb.sd
		    MaxMatches   2000

		END Database

		BEGIN Database
		    DbType       City
		    DefDb        stkCityDb.cd
		    UseMyDb      Off
		    MyDb         \
		    MaxMatches   2000

		END Database

		BEGIN Database
		    DbType       Facility
		    DefDb        stkFacility.fd
		    UseMyDb      Off
		    MyDb         .\stkFacility.fd
		    MaxMatches   2000

		END Database

		BEGIN Database
		    DbType       Star
		    DefDb        stkStarDb.bd
		    UseMyDb      Off
		    MyDb         stkStarDb.bd
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
    END VectorTool
    
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
		CloudTemperature      0.000000
		CloudLiquidDensity    7.500000
		CloudWaterContent     0.500000
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
    
    BEGIN PrRaeClutterDb
        dbName None
    END PrRaeClutterDb
    
    BEGIN Gator
    END Gator
    
    BEGIN Crdn
    END Crdn
    
    BEGIN SpiceExt
		File                     C:\Program Files\AGI\STK 6.0\STKData\Spice\de405_2000-2050.bsp
		File                     C:\Program Files\AGI\STK 6.0\STKData\Spice\Mars_2000-2025.bsp
		File                     C:\Program Files\AGI\STK 6.0\STKData\Spice\OuterMoons_2000-2025.bsp
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
			ReadBufferSize             1000
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
        ReferenceDate         1 Jun 2004 12:00:00.000000000
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
        ScratchDirectory      C:\DOCUME~1\sdupont\LOCALS~1\Temp
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

Class AdvCAT

	AdvCAT1

END Class

Class Aircraft

	a340

END Class

Class Constellation

	gps_const

END Class

Class Facility

	Facility1

END Class

Class Satellite

	gps_2-01
	gps_2-02
	gps_2-03
	gps_2-04
	gps_2-05
	gps_2-06
	gps_2-08
	gps_2-09
	gps_2-10
	gps_2-11
	gps_2-12
	gps_2-14
	gps_2-15
	gps_2-16
	gps_2-17
	gps_2-18
	gps_2-19
	gps_2-20
	gps_2-21
	gps_2-22
	gps_2-23
	gps_2-24
	gps_2-25
	gps_2-26
	gps_2-27
	Satellite1
	Satellite2
	Satellite3

END Class

END SubObjects

END Scenario
