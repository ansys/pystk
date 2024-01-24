stk.v.8.0
BEGIN Scenario
    Name            ConstellationTests

BEGIN Epoch
    Epoch        1 Jul 1999 00:00:00.000

END Epoch

BEGIN Interval

Start               1 Jul 1999 00:00:00.000000000
Stop                2 Jul 1999 00:00:00.000000000

END Interval

BEGIN EOPFile

    EOPFilename     EOP-v1.1.txt

END EOPFile

BEGIN GlobalPrefs

    SatelliteNoOrbWarning    No
    MissileNoOrbWarning      No
    AircraftWGS84Warning     Always
END GlobalPrefs

BEGIN CentralBody

    PrimaryBody     Earth
    UseTerrainCache Yes
    TotalCacheSize  402653184

END CentralBody

BEGIN CentralBodyTerrain

END CentralBodyTerrain

BEGIN ScenarioLicenses
    Module    ASTGv8.0
    Module    AgRt3v8.0
    Module    CATv8.0
    Module    MisSysv8.0
    Module    PODSv8.0
    Module    STKExpertv8.0
    Module    STKProfessionalv8.0
    Module    STKv8.0
    Module    TIREM
    Module    USGOVv8.0
END ScenarioLicenses

BEGIN WebData
        EnableWebTerrainData    No
        SaveWebTerrainDataPasswords    No
        BEGIN ConfigServerDataList
            BEGIN ConfigServerData
                Name "globeserver.agi.com"
                Port 80
                DataURL "bin/getGlobeSvrConfig.pl"
            END ConfigServerData
        END ConfigServerDataList
END WebData

BEGIN Extensions
    
    BEGIN Graphics

BEGIN Animation

    StartTime          1 Jul 1999 00:00:00.000000000
    EndTime            1 Jun 2004 16:00:00.000000000
    Direction          Forward
    UpdateDelta        60.0000
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
            UseVarAspectRatio    No
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

        BEGIN MapList
            BEGIN Detail
                Alias RWDB2 Coastlines
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias Coastlines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 International Borders
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Demarcated or Delimited
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Indefinite or Disputed
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Lines of separation or sovereignty on land
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Lines of separation or sovereignty at sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Other lines of separation or sovereignty at sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Continental shelf boundary in Persian Gulf
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 7: Demilitarized zone lines in Israel
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 8: No defined line
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 9: Selected claimed lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 50: Old Panama Canal Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 51: Old N. Yemen-S.Yemen lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 52: Old Jordan-Iraq lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 53: Old Iraq-Saudi Arabia Neutral Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 54: Old East Germany-West Germany and Berlin lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 55: Old N. Vietnam-S. Vietnam boundary
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 56: Old Vietnam DMZ lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 57: Old Kuwait-Saudi Arabia Neutral Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 58: Old Oman-Yemen line of separation
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Islands
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Major islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Additional major islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Moderately important islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Additional islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Very small minor islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 8: Reefs
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 9: Shoals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Lakes
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Lakes that should appear on all maps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Additional major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Intermediate lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Additional minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 7: Swamps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 11: Intermittent major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 12: Intermittent minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 14: Major salt pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 15: Minor salt pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 23: Glaciers
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Provincial Borders
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: First order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Second order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Third order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Special boundaries
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 54: Pre-unification German administration lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 61: First order boundaries in the water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 62: Second order boundaries in the water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 99: Disputed lines
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Rivers
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Major rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Additional major rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Intermediate rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Additional intermediate rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Additional minor rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 10: Major intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 11: Intermediate intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 12: Minor intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 21: Major canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 22: Minor canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 23: Irrigation canals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Coastlines
                Show Yes
                Color #8fbc8f
                BEGIN Detail
                    Alias Coastlines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_International_Borders
                Show Yes
                Color #8fbc8f
                BEGIN Detail
                    Alias Demarcated_or_Delimited
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Indefinite_or_Disputed
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Lines_of_separation_on_land
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Lines_of_separation_at_sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Other_lines_of_separation_at_sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Continental_shelf_boundary_in_Persian_Gulf
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Demilitarized_zone_lines_in_Israel
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias No_defined_line
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Selected_claimed_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Panama_Canal_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_North-South_Yemen_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Jordan-Iraq_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Iraq-Saudi_Arabia_Neutral_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_East-West_Germany_and_Berlin_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_North-South_Vietnam_boundary
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Vietnam_DMZ_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Oman-Yemen_line_of_separation
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Islands
                Show Yes
                Color #8fbc8f
                BEGIN Detail
                    Alias Major_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Moderately_important_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Very_small_minor_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Reefs
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Shoals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Lakes
                Show No
                Color #87cefa
                BEGIN Detail
                    Alias Lakes_that_should_appear_on_all_maps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Swamps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermittent_major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermittent_minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_salt_pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_salt_pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Glaciers
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Provincial_Borders
                Show No
                Color #8fbc8f
                BEGIN Detail
                    Alias First_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Second_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Third_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Special_boundaries
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Pre-unification_German_administration_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias First_order_boundaries_on_water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Second_order_boundaries_on_water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Disputed_lines
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Rivers
                Show No
                Color #87cefa
                BEGIN Detail
                    Alias Major_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_intermediate_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_minor_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Irrigation_canals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
        END MapList


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
            Directory        C:\DOCUME~1\VDUBOV~1\LOCALS~1\Temp
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
            WmvCodec         "Windows Media Video 9"
            Framerate        30
            Bitrate          3000000
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
            UseVarAspectRatio    No
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

        BEGIN MapList
            BEGIN Detail
                Alias RWDB2 Coastlines
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias Coastlines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 International Borders
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Demarcated or Delimited
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Indefinite or Disputed
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Lines of separation or sovereignty on land
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Lines of separation or sovereignty at sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Other lines of separation or sovereignty at sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Continental shelf boundary in Persian Gulf
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 7: Demilitarized zone lines in Israel
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 8: No defined line
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 9: Selected claimed lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 50: Old Panama Canal Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 51: Old N. Yemen-S.Yemen lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 52: Old Jordan-Iraq lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 53: Old Iraq-Saudi Arabia Neutral Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 54: Old East Germany-West Germany and Berlin lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 55: Old N. Vietnam-S. Vietnam boundary
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 56: Old Vietnam DMZ lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 57: Old Kuwait-Saudi Arabia Neutral Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 58: Old Oman-Yemen line of separation
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Islands
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Major islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Additional major islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Moderately important islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Additional islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Very small minor islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 8: Reefs
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 9: Shoals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Lakes
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Lakes that should appear on all maps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Additional major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Intermediate lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Additional minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 7: Swamps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 11: Intermittent major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 12: Intermittent minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 14: Major salt pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 15: Minor salt pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 23: Glaciers
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Provincial Borders
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: First order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Second order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Third order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Special boundaries
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 54: Pre-unification German administration lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 61: First order boundaries in the water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 62: Second order boundaries in the water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 99: Disputed lines
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Rivers
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Major rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Additional major rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Intermediate rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Additional intermediate rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Additional minor rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 10: Major intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 11: Intermediate intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 12: Minor intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 21: Major canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 22: Minor canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 23: Irrigation canals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Coastlines
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias Coastlines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_International_Borders
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias Demarcated_or_Delimited
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Indefinite_or_Disputed
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Lines_of_separation_on_land
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Lines_of_separation_at_sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Other_lines_of_separation_at_sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Continental_shelf_boundary_in_Persian_Gulf
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Demilitarized_zone_lines_in_Israel
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias No_defined_line
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Selected_claimed_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Panama_Canal_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_North-South_Yemen_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Jordan-Iraq_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Iraq-Saudi_Arabia_Neutral_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_East-West_Germany_and_Berlin_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_North-South_Vietnam_boundary
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Vietnam_DMZ_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Oman-Yemen_line_of_separation
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Islands
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias Major_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Moderately_important_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Very_small_minor_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Reefs
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Shoals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Lakes
                Show Yes
                Color #87cefa
                BEGIN Detail
                    Alias Lakes_that_should_appear_on_all_maps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Swamps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermittent_major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermittent_minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_salt_pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_salt_pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Glaciers
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Provincial_Borders
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias First_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Second_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Third_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Special_boundaries
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Pre-unification_German_administration_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias First_order_boundaries_on_water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Second_order_boundaries_on_water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Disputed_lines
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Rivers
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias Major_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_intermediate_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_minor_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Irrigation_canals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
        END MapList


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\MBARTH~1\LOCALS~1\Temp
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
            WmvCodec         "Windows Media Video 9"
            Framerate        30
            Bitrate          3000000
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
            UseVarAspectRatio    No
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

        BEGIN MapList
            BEGIN Detail
                Alias RWDB2 Coastlines
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias Coastlines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 International Borders
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Demarcated or Delimited
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Indefinite or Disputed
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Lines of separation or sovereignty on land
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Lines of separation or sovereignty at sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Other lines of separation or sovereignty at sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Continental shelf boundary in Persian Gulf
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 7: Demilitarized zone lines in Israel
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 8: No defined line
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 9: Selected claimed lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 50: Old Panama Canal Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 51: Old N. Yemen-S.Yemen lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 52: Old Jordan-Iraq lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 53: Old Iraq-Saudi Arabia Neutral Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 54: Old East Germany-West Germany and Berlin lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 55: Old N. Vietnam-S. Vietnam boundary
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 56: Old Vietnam DMZ lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 57: Old Kuwait-Saudi Arabia Neutral Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 58: Old Oman-Yemen line of separation
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Islands
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Major islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Additional major islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Moderately important islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Additional islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Very small minor islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 8: Reefs
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 9: Shoals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Lakes
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Lakes that should appear on all maps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Additional major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Intermediate lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Additional minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 7: Swamps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 11: Intermittent major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 12: Intermittent minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 14: Major salt pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 15: Minor salt pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 23: Glaciers
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Provincial Borders
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: First order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Second order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Third order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Special boundaries
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 54: Pre-unification German administration lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 61: First order boundaries in the water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 62: Second order boundaries in the water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 99: Disputed lines
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Rivers
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Major rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Additional major rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Intermediate rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Additional intermediate rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Additional minor rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 10: Major intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 11: Intermediate intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 12: Minor intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 21: Major canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 22: Minor canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 23: Irrigation canals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Coastlines
                Show Yes
                Color #8fbc8f
                BEGIN Detail
                    Alias Coastlines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_International_Borders
                Show Yes
                Color #8fbc8f
                BEGIN Detail
                    Alias Demarcated_or_Delimited
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Indefinite_or_Disputed
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Lines_of_separation_on_land
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Lines_of_separation_at_sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Other_lines_of_separation_at_sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Continental_shelf_boundary_in_Persian_Gulf
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Demilitarized_zone_lines_in_Israel
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias No_defined_line
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Selected_claimed_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Panama_Canal_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_North-South_Yemen_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Jordan-Iraq_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Iraq-Saudi_Arabia_Neutral_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_East-West_Germany_and_Berlin_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_North-South_Vietnam_boundary
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Vietnam_DMZ_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Oman-Yemen_line_of_separation
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Islands
                Show Yes
                Color #8fbc8f
                BEGIN Detail
                    Alias Major_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Moderately_important_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Very_small_minor_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Reefs
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Shoals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Lakes
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias Lakes_that_should_appear_on_all_maps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Swamps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermittent_major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermittent_minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_salt_pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_salt_pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Glaciers
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Provincial_Borders
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias First_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Second_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Third_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Special_boundaries
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Pre-unification_German_administration_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias First_order_boundaries_on_water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Second_order_boundaries_on_water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Disputed_lines
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Rivers
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias Major_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_intermediate_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_minor_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Irrigation_canals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
        END MapList


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\MBARTH~1\LOCALS~1\Temp
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
            WmvCodec         "Windows Media Video 9"
            Framerate        30
            Bitrate          3000000
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
            UseVarAspectRatio    No
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

        BEGIN MapList
            BEGIN Detail
                Alias RWDB2 Coastlines
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias Coastlines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 International Borders
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Demarcated or Delimited
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Indefinite or Disputed
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Lines of separation or sovereignty on land
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Lines of separation or sovereignty at sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Other lines of separation or sovereignty at sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Continental shelf boundary in Persian Gulf
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 7: Demilitarized zone lines in Israel
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 8: No defined line
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 9: Selected claimed lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 50: Old Panama Canal Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 51: Old N. Yemen-S.Yemen lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 52: Old Jordan-Iraq lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 53: Old Iraq-Saudi Arabia Neutral Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 54: Old East Germany-West Germany and Berlin lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 55: Old N. Vietnam-S. Vietnam boundary
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 56: Old Vietnam DMZ lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 57: Old Kuwait-Saudi Arabia Neutral Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 58: Old Oman-Yemen line of separation
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Islands
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Major islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Additional major islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Moderately important islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Additional islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Very small minor islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 8: Reefs
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 9: Shoals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Lakes
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Lakes that should appear on all maps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Additional major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Intermediate lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Additional minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 7: Swamps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 11: Intermittent major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 12: Intermittent minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 14: Major salt pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 15: Minor salt pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 23: Glaciers
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Provincial Borders
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: First order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Second order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Third order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Special boundaries
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 54: Pre-unification German administration lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 61: First order boundaries in the water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 62: Second order boundaries in the water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 99: Disputed lines
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Rivers
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Major rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Additional major rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Intermediate rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Additional intermediate rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Additional minor rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 10: Major intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 11: Intermediate intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 12: Minor intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 21: Major canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 22: Minor canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 23: Irrigation canals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Coastlines
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias Coastlines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_International_Borders
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias Demarcated_or_Delimited
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Indefinite_or_Disputed
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Lines_of_separation_on_land
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Lines_of_separation_at_sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Other_lines_of_separation_at_sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Continental_shelf_boundary_in_Persian_Gulf
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Demilitarized_zone_lines_in_Israel
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias No_defined_line
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Selected_claimed_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Panama_Canal_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_North-South_Yemen_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Jordan-Iraq_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Iraq-Saudi_Arabia_Neutral_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_East-West_Germany_and_Berlin_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_North-South_Vietnam_boundary
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Vietnam_DMZ_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Oman-Yemen_line_of_separation
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Islands
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias Major_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Moderately_important_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Very_small_minor_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Reefs
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Shoals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Lakes
                Show Yes
                Color #87cefa
                BEGIN Detail
                    Alias Lakes_that_should_appear_on_all_maps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Swamps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermittent_major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermittent_minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_salt_pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_salt_pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Glaciers
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Provincial_Borders
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias First_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Second_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Third_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Special_boundaries
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Pre-unification_German_administration_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias First_order_boundaries_on_water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Second_order_boundaries_on_water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Disputed_lines
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Rivers
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias Major_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_intermediate_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_minor_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Irrigation_canals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
        END MapList


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\MBARTH~1\LOCALS~1\Temp
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
            WmvCodec         "Windows Media Video 9"
            Framerate        30
            Bitrate          3000000
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
            BackgroundImageFile  Basic
            UseCloudsFile        Off
            BEGIN ZoomBounds
                15.776278 -171.147540 80.694310 -41.311475
                -90.000000 -179.999999 90.000000 179.999999
            END ZoomBounds
            UseVarAspectRatio    No
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

        BEGIN MapList
            BEGIN Detail
                Alias RWDB2 Coastlines
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias Coastlines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 International Borders
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Demarcated or Delimited
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Indefinite or Disputed
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Lines of separation or sovereignty on land
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Lines of separation or sovereignty at sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Other lines of separation or sovereignty at sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Continental shelf boundary in Persian Gulf
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 7: Demilitarized zone lines in Israel
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 8: No defined line
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 9: Selected claimed lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 50: Old Panama Canal Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 51: Old N. Yemen-S.Yemen lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 52: Old Jordan-Iraq lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 53: Old Iraq-Saudi Arabia Neutral Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 54: Old East Germany-West Germany and Berlin lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 55: Old N. Vietnam-S. Vietnam boundary
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 56: Old Vietnam DMZ lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 57: Old Kuwait-Saudi Arabia Neutral Zone lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 58: Old Oman-Yemen line of separation
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Islands
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Major islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Additional major islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Moderately important islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Additional islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Very small minor islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 8: Reefs
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 9: Shoals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Lakes
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Lakes that should appear on all maps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Additional major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Intermediate lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Additional minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 7: Swamps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 11: Intermittent major lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 12: Intermittent minor lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 14: Major salt pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 15: Minor salt pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 23: Glaciers
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Provincial Borders
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: First order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Second order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Third order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Special boundaries
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 54: Pre-unification German administration lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 61: First order boundaries in the water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 62: Second order boundaries in the water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 99: Disputed lines
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2 Rivers
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias     Rank 1: Major rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 2: Additional major rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 3: Intermediate rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 4: Additional intermediate rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 5: Minor rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 6: Additional minor rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 10: Major intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 11: Intermediate intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 12: Minor intermittent rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 21: Major canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 22: Minor canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias     Rank 23: Irrigation canals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Coastlines
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias Coastlines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_Ice_Shelves
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_International_Borders
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias Demarcated_or_Delimited
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Indefinite_or_Disputed
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Lines_of_separation_on_land
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Lines_of_separation_at_sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Other_lines_of_separation_at_sea
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Continental_shelf_boundary_in_Persian_Gulf
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Demilitarized_zone_lines_in_Israel
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias No_defined_line
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Selected_claimed_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Panama_Canal_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_North-South_Yemen_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Jordan-Iraq_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Iraq-Saudi_Arabia_Neutral_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_East-West_Germany_and_Berlin_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_North-South_Vietnam_boundary
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Vietnam_DMZ_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Kuwait-Saudi_Arabia_Neutral_Zone_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Old_Oman-Yemen_line_of_separation
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Islands
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias Major_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Moderately_important_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Very_small_minor_islands
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Reefs
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Shoals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Lakes
                Show Yes
                Color #87cefa
                BEGIN Detail
                    Alias Lakes_that_should_appear_on_all_maps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Swamps
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermittent_major_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermittent_minor_lakes
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_salt_pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_salt_pans
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Glaciers
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Provincial_Borders
                Show Yes
                Color #00ff00
                BEGIN Detail
                    Alias First_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Second_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Third_order
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Special_boundaries
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Pre-unification_German_administration_lines
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias First_order_boundaries_on_water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Second_order_boundaries_on_water
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Disputed_lines
                    Show No
                    Color #00ff00
                END Detail
            END Detail
            BEGIN Detail
                Alias RWDB2_Rivers
                Show No
                Color #00ff00
                BEGIN Detail
                    Alias Major_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_major_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_intermediate_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Additional_minor_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Intermediate_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_intermittent_rivers
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Major_canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Minor_canals
                    Show No
                    Color #00ff00
                END Detail
                BEGIN Detail
                    Alias Irrigation_canals
                    Show No
                    Color #00ff00
                END Detail
            END Detail
        END MapList


        BEGIN MapAnnotations
        END MapAnnotations

        BEGIN SoftVTR
            OutputFormat     BMP
            Directory        C:\DOCUME~1\MBARTH~1\LOCALS~1\Temp
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
            WmvCodec         "Windows Media Video 9"
            Framerate        30
            Bitrate          3000000
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
		SolidAngle		Steradians
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
		SolidAngle		Steradians
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
		SolidAngle		Steradians
		RadiationDoseUnit		RadsSilicon
		RadiationShieldThicknessUnit		GramsperSquareCm
		MagneticFieldUnit		nanoTesla
    END ConnectReportUnits
    
    BEGIN GenDb

		BEGIN Database
		    DbType       Satellite
		    DefDb        stkSatDb.sd
		    UseMyDb      Off
		    MyDb         \
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
    ShowAllCB     Off
    END VectorTool
    
    BEGIN Author
	Optimize	Yes
	UseBasicGlobe	Yes
	ReadOnly	No
	ViewerPassword	No
	STKPassword	No
    END Author
    
    BEGIN ExportDataFile
    FileType         Ephemeris
    Directory        C:\dev\v8x\STK\Automation\Tests\NUnitTests\Scenario\
    UseTimePeriod    No
    TimePeriodStart  0.000000e+000
    TimePeriodStop   0.000000e+000
    StepType         Ephemeris
    StepSize         60.000000
    EphemType        STK
    CentralBody      Earth
    SatelliteID      -200000
    CoordSys         J2000
    InterpolateBoundaries  Yes
    EphemFormat      Current
    InterpType       9
    InterpOrder      5
    AttCoordSys      Fixed
    Quaternions      0
    ExportCovar      Yes
    AttitudeFormat   Current
    END ExportDataFile
    
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
	RainOutagePercent    0.100000
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
    
    BEGIN Gator
    END Gator
    
    BEGIN Crdn
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Ceres_Angular_Velocity
			Description	Ceres Angular Velocity
			AbsolutePath	CentralBody/Ceres
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Ceres
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Ceres
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Ceres Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Ceres
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Ceres
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Ceres
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Ceres Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Ceres
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Ceres
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Ceres
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Ceres Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Ceres
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Ceres
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Ceres
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Ceres Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Ceres
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Ceres
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Ceres
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Deimos_Angular_Velocity
			Description	Deimos Angular Velocity
			AbsolutePath	CentralBody/Deimos
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Deimos
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Deimos
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Deimos Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Deimos
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Deimos
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Deimos
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Deimos Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Deimos
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Deimos
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Deimos
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Deimos Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Deimos
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Deimos
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Deimos
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Deimos Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Deimos
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Deimos
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Deimos
					END	AXES
		END	SYSTEM
		BEGIN	AXES
			Type	AXES_TRAJECTORY
			Name	BBR_Axes
			Description	Body-Body Rotating Axes
			AbsolutePath	CentralBody/Earth
				TrajPoint
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				ReferenceSystem
					BEGIN	SYSTEM
						Type	SYSTEM_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Moon
					END	SYSTEM
				TrajAxesType	20
				LabelX	
				LabelY	
				LabelZ	
		END	AXES
		BEGIN	AXES
			Type	AXES_ATEPOCH
			Name	Earth_Aligned_at_Epoch
			Description	Aligned with Earth Fixed at Epoch
			AbsolutePath	CentralBody/Earth
				Epoch	1 Jan 2000 11:58:55.816000000
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
				LabelX	
				LabelY	
				LabelZ	
		END	AXES
		BEGIN	AXES
			Type	AXES_ATEPOCH
			Name	Mean_Ecliptic_of_Epoch
			Description	Mean Ecliptic of Epoch Axes
			AbsolutePath	CentralBody/Earth
				Epoch	1 Jan 2000 11:58:55.816000000
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MeanEclpDate
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
				LabelX	
				LabelY	
				LabelZ	
		END	AXES
		BEGIN	AXES
			Type	AXES_ATEPOCH
			Name	Mean_Ecliptic_of_J2000
			Description	Mean Ecliptic of J2000 Axes
			AbsolutePath	CentralBody/Earth
				Epoch	1 Jan 2000 11:58:55.816000000
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MeanEclpDate
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
				LabelX	
				LabelY	
				LabelZ	
		END	AXES
		BEGIN	AXES
			Type	AXES_ATEPOCH
			Name	Mean_Equinox_True_Equator_of_Epoch
			Description	Mean Equinox True Equator of Epoch Axes
			AbsolutePath	CentralBody/Earth
				Epoch	1 Jan 2000 11:58:55.816000000
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TEMED
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
				LabelX	
				LabelY	
				LabelZ	
		END	AXES
		BEGIN	AXES
			Type	AXES_ATEPOCH
			Name	Mean_of_Epoch
			Description	Mean of Epoch Axes
			AbsolutePath	CentralBody/Earth
				Epoch	1 Jan 2000 11:58:55.816000000
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
				LabelX	
				LabelY	
				LabelZ	
		END	AXES
		BEGIN	AXES
			Type	AXES_ATEPOCH
			Name	True_Ecliptic_of_Epoch
			Description	True Ecliptic of Epoch Axes
			AbsolutePath	CentralBody/Earth
				Epoch	1 Jan 2000 11:58:55.816000000
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TrueEclpDate
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
				LabelX	
				LabelY	
				LabelZ	
		END	AXES
		BEGIN	AXES
			Type	AXES_ATEPOCH
			Name	True_of_Epoch
			Description	True of Epoch Axes
			AbsolutePath	CentralBody/Earth
				Epoch	1 Jan 2000 11:58:55.816000000
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
				LabelX	
				LabelY	
				LabelZ	
		END	AXES
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Callisto_Angular_Velocity
			Description	Callisto Angular Velocity
			AbsolutePath	CentralBody/Earth
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	VECTOR
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Charon_Angular_Velocity
			Description	Charon Angular Velocity
			AbsolutePath	CentralBody/Earth
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	VECTOR
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Earth_Angular_Velocity
			Description	Earth Angular Velocity
			AbsolutePath	CentralBody/Earth
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	VECTOR
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Europa_Angular_Velocity
			Description	Europa Angular Velocity
			AbsolutePath	CentralBody/Earth
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	VECTOR
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Ganymede_Angular_Velocity
			Description	Ganymede Angular Velocity
			AbsolutePath	CentralBody/Earth
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	VECTOR
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Io_Angular_Velocity
			Description	Io Angular Velocity
			AbsolutePath	CentralBody/Earth
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	VECTOR
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Titan_Angular_Velocity
			Description	Titan Angular Velocity
			AbsolutePath	CentralBody/Earth
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	VECTOR
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Triton_Angular_Velocity
			Description	Triton Angular Velocity
			AbsolutePath	CentralBody/Earth
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Earth
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	VECTOR
		BEGIN	VECTOR
			Type	VECTOR_FIXED
			Name	User_Defined
			Description	User Defined Vector Fixed in Coordinate System
			AbsolutePath	CentralBody/Earth
				Dimension	6
				FixedVector
					0.00000000000000e+000
					0.00000000000000e+000
					1.00000000000000e+000
					UiSequence      321
					UiCoordType      4
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	VECTOR
		BEGIN	VECTOR
			Type	VECTOR_FIXED
			Name	X_Vector
			Description	X Axis in Default Coordinate System
			AbsolutePath	CentralBody/Earth
				Dimension	6
				FixedVector
					1.00000000000000e+000
					0.00000000000000e+000
					0.00000000000000e+000
					UiSequence      321
					UiCoordType      4
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Aligned_with_Fixed_at_Epoch
			Description	Earth Centered Aligned with Fixed at Epoch Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Earth_Aligned_at_Epoch
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Triton Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Triton Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Triton Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Triton Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Mean_B1950
			Description	Earth Centered Mean B1950 Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	B1950
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Mean_Ecliptic_of_Date
			Description	Earth Centered Mean Ecliptic of Date Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MeanEclpDate
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Mean_Ecliptic_of_Epoch
			Description	Earth Centered Mean Ecliptic of Epoch Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Mean_Ecliptic_of_Epoch
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Mean_Ecliptic_of_J2000
			Description	Earth Centered Mean Ecliptic of J2000 Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Mean_Ecliptic_of_J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Mean_Equinox_True_Equator_of_Date
			Description	Earth Centered Mean Equinox True Equator of Date Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TEMED
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Mean_Equinox_True_Equator_of_Epoch
			Description	Earth Centered Mean Equinox True Equator of Epoch Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Mean_Equinox_True_Equator_of_Epoch
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Mean_J2000
			Description	Earth Centered Mean J2000 (Default Inertial) Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Mean_of_Date
			Description	Earth Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Mean_of_Epoch
			Description	Earth Centered Mean of Epoch Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Mean_of_Epoch
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	True_Ecliptic_of_Date
			Description	Earth Centered True Ecliptic of Date Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TrueEclpDate
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	True_Ecliptic_of_Epoch
			Description	Earth Centered True Ecliptic of Epoch Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	True_Ecliptic_of_Epoch
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	True_of_Date
			Description	Earth Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	True_of_Epoch
			Description	Earth Centered True of Epoch Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	True_of_Epoch
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	User_Defined
			Description	User Assembled Coordinate System
			AbsolutePath	CentralBody/Earth
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Earth
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Jupiter_Angular_Velocity
			Description	Jupiter Angular Velocity
			AbsolutePath	CentralBody/Jupiter
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Jupiter
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Jupiter
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Jupiter Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Jupiter
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Jupiter
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Jupiter
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Jupiter Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Jupiter
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Jupiter
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Jupiter
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Jupiter Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Jupiter
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Jupiter
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Jupiter
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Jupiter Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Jupiter
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Jupiter
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Jupiter
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Mars_Angular_Velocity
			Description	Mars Angular Velocity
			AbsolutePath	CentralBody/Mars
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Mars
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Mars
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Mars Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Mars
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Mars
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Mars
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Mars Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Mars
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Mars
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Mars
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Mars Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Mars
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Mars
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Mars
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Mars Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Mars
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Mars
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Mars
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Mercury_Angular_Velocity
			Description	Mercury Angular Velocity
			AbsolutePath	CentralBody/Mercury
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Mercury
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Mercury
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Mercury Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Mercury
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Mercury
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Mercury
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Mercury Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Mercury
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Mercury
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Mercury
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Mercury Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Mercury
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Mercury
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Mercury
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Mercury Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Mercury
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Mercury
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Mercury
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Moon_Angular_Velocity
			Description	Moon Angular Velocity
			AbsolutePath	CentralBody/Moon
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Moon
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Moon
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Moon Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Moon
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Moon
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Moon
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Moon Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Moon
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Moon
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Moon
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_J2000
			Description	Moon Centered Mean Earth Equator of J2000 Coordinate System
			AbsolutePath	CentralBody/Moon
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Moon
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Moon Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Moon
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Moon
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Moon
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Moon Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Moon
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Moon
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Moon
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Neptune_Angular_Velocity
			Description	Neptune Angular Velocity
			AbsolutePath	CentralBody/Neptune
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Neptune
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Neptune
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Neptune Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Neptune
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Neptune
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Neptune
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Neptune Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Neptune
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Neptune
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Neptune
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Neptune Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Neptune
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Neptune
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Neptune
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Neptune Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Neptune
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Neptune
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Neptune
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Phobos_Angular_Velocity
			Description	Phobos Angular Velocity
			AbsolutePath	CentralBody/Phobos
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Phobos
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Phobos
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Phobos Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Phobos
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Phobos
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Phobos
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Phobos Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Phobos
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Phobos
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Phobos
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Phobos Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Phobos
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Phobos
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Phobos
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Phobos Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Phobos
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Phobos
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Phobos
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Pluto_Angular_Velocity
			Description	Pluto Angular Velocity
			AbsolutePath	CentralBody/Pluto
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Pluto
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Pluto
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Pluto Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Pluto
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Pluto
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Pluto
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Pluto Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Pluto
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Pluto
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Pluto
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Pluto Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Pluto
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Pluto
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Pluto
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Pluto Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Pluto
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Pluto
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Pluto
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Saturn_Angular_Velocity
			Description	Saturn Angular Velocity
			AbsolutePath	CentralBody/Saturn
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Saturn
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Saturn
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Saturn Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Saturn
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Saturn
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Saturn
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Saturn Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Saturn
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Saturn
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Saturn
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Saturn Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Saturn
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Saturn
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Saturn
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Saturn Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Saturn
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Saturn
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Saturn
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Sun_Angular_Velocity
			Description	Sun Angular Velocity
			AbsolutePath	CentralBody/Sun
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Sun
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Sun
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Sun Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Sun
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Sun
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Sun
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Sun Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Sun
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Sun
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Sun
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_Ecliptic_of_J2000
			Description	Sun Centered Mean Ecliptic of J2000 Coordinate System
			AbsolutePath	CentralBody/Sun
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Sun
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Mean_Ecliptic_of_J2000
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_J2000
			Description	Sun Centered Mean Earth Equator of J2000 Coordinate System
			AbsolutePath	CentralBody/Sun
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Sun
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Earth
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Sun Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Sun
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Sun
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Sun
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Sun Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Sun
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Sun
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Sun
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Uranus_Angular_Velocity
			Description	Uranus Angular Velocity
			AbsolutePath	CentralBody/Uranus
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Uranus
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Uranus
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Uranus Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Uranus
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Uranus
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Uranus
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Uranus Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Uranus
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Uranus
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Uranus
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Uranus Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Uranus
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Uranus
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Uranus
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Uranus Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Uranus
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Uranus
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Uranus
					END	AXES
		END	SYSTEM
		BEGIN	VECTOR
			Type	VECTOR_AXESDERIVATIVE
			Name	Venus_Angular_Velocity
			Description	Venus Angular Velocity
			AbsolutePath	CentralBody/Venus
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Venus
					END	AXES
				ReferenceAxes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Venus
					END	AXES
		END	VECTOR
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Fixed
			Description	Venus Centered Fixed Coordinate System
			AbsolutePath	CentralBody/Venus
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Venus
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Fixed
						AbsolutePath	CentralBody/Venus
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Inertial
			Description	Venus Centered Inertial Coordinate System
			AbsolutePath	CentralBody/Venus
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Venus
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	Inertial
						AbsolutePath	CentralBody/Venus
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_Mean_of_Date
			Description	Venus Centered Mean of Date Coordinate System
			AbsolutePath	CentralBody/Venus
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Venus
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	MOD
						AbsolutePath	CentralBody/Venus
					END	AXES
		END	SYSTEM
		BEGIN	SYSTEM
			Type	SYSTEM_ASSEMBLED
			Name	Centered_True_of_Date
			Description	Venus Centered True of Date Coordinate System
			AbsolutePath	CentralBody/Venus
				Origin
					BEGIN	POINT
						Type	POINT_LINKTO
						Name	Center
						AbsolutePath	CentralBody/Venus
					END	POINT
				Axes
					BEGIN	AXES
						Type	AXES_LINKTO
						Name	TOD
						AbsolutePath	CentralBody/Venus
					END	AXES
		END	SYSTEM
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
        ReferenceDate         1 Jul 1999 00:00:00.000000000
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
        FluxFile              C:\Program@Files\AGI\STK@6.0\PODS\tables\tables.dat
        JPLFile               C:\Program@Files\AGI\STK@6.0\PODS\ephem\jplde405.dat
        GeoFile               C:\Program@Files\AGI\STK@6.0\PODS\gco_files\wgs84.gco
        TideFile              tides\tides.dat
        PODSDirectory         C:\Program@Files\AGI\STK@6.0\PODS
        TrkDataDirectory      C:\Program@Files\AGI\STK@6.0\PODS\trk_data
        ScratchDirectory      C:\DOCUME~1\MBARTH~1\LOCALS~1\Temp
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

Class Aircraft

	Boing737

END Class

Class AreaTarget

	AreaTarget1

END Class

Class Chain

	Chain1

END Class

Class Constellation

	Constellation1

END Class

Class Facility

	Facility1

END Class

Class GroundVehicle

	GroundVehicle1

END Class

Class LineTarget

	LineTarget2

END Class

Class Missile

	Missile1

END Class

Class Place

	Place1

END Class

Class Planet

	JupiterAnalytic
	MarsJPL
	NeptuneFile
	Planet1

END Class

Class Satellite

	CalcScalSat
	Satellite1

END Class

Class Ship

	Ship1

END Class

Class Star

	Star1

END Class

Class Submarine

	SSBN726

END Class

Class Target

	Target1

END Class

END SubObjects

END Scenario
