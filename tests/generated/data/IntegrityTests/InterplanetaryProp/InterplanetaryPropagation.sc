stk.v.9.0
WrittenBy    STK_v9.0.0
BEGIN Scenario
    Name            InterplanetaryPropagation

BEGIN Epoch
    Epoch        1 Jul 2007 12:00:00.000000000

END Epoch

BEGIN Interval

Start                   1 Jul 2007 12:00:00.000000000
Stop                    2 Jul 2007 12:00:00.000000000
EpochUsesAnalStart      Yes
AnimStartUsesAnalStart  Yes
AnimStopUsesAnalStop    No

END Interval

BEGIN EOPFile

    EOPFilename     EOP-v1.1.txt

END EOPFile

BEGIN GlobalPrefs

    SatelliteNoOrbWarning    No
    MissilePerigeeWarning    No
    MissileStopTimeWarning   No
    AircraftWGS84Warning     Always
    Use1PtSGP4Prop                No
    Validate1PtSGP4Prop           No
    Suppress1PtSGP4InterpWarning  No
END GlobalPrefs

BEGIN CentralBody

    PrimaryBody     Earth
    UseTerrainCache Yes
    TotalCacheSize  402653184

END CentralBody

BEGIN CentralBodyTerrain

END CentralBodyTerrain

BEGIN ScenarioLicenses
    Module    ASTGv9.0
    Module    CATv9.0
    Module    DISv9.0
    Module    MexServv9.0
    Module    PODSv9.0
    Module    RdrAdvEnv9.0
    Module    STKExpertv9.0
    Module    STKv9.0
    Module    TIREM
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

    StartTime          1 Jul 2007 12:00:00.000000000
    EndTime            2 Jul 2007 00:00:00.000000000
    CurrentTime        1 Jul 2007 12:00:00.000000000
    Direction          Forward
    UpdateDelta        60.000000
    RefreshDelta       HighSpeed
    XRealTimeMult      1.000000
    RealTimeOffset     0.000000
    XRtStartFromPause  Yes

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

    DisableDefKbdActions     Off
    TextShadowStyle          None
    TextShadowColor          #000000

    BEGIN MapStyles

        UseStyleTime        No

        BEGIN Style
        Name                No_Map_Bckgrnd
        Time                -61603201.000000
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
        Time                -61603201.000000
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
        Time                -61603201.000000
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
        Time                -61603201.000000
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
    
    BEGIN ClsApp
		RangeConstraint         5000.000
		ApoPeriPad              30000.000
		OrbitPathPad            30000.000
		TimeDistPad             30000.000
		OutOfDate               2592000.000
		UseApogeePerigeeFilter  Yes
		UsePathFilter           Yes
		UseTimeFilter           Yes
		UseOutOfDate            Yes
		CreateSats              No
		MaxSatsToCreate         500
		UseModelScale           No
		ModelScale              4.000
		UseLaunchWindow         Yes
		LaunchWindowStart       0.000
		LaunchWindowStop        0.000
		ShowLine                Yes
		AnimHighlight           Yes
		StaticHighlight         Yes
		UseCrossRefDb           Yes
		CollisionDB                     Databases\Satellite\stkAllTLE.tce
		CollisionCrossRefDB             Databases\Satellite\stkAllTLE.sd
    END ClsApp
    
    BEGIN LaserCAT
		Mode                     TargetObject
		StartTime                1 Jul 2007 12:00:00.000000000
		StopTime                 1 Jul 2007 16:00:00.000000000
		RangeConstraint         500000000.00000
		MinElevationAng         0.34907
		Duration                0.00000
		ExclHalfAng             0.08727
		MaxPVtoScenario         10
		CenterFrequency         14000000000.00000
		BandWidth               20000000.00000
		Linear_PowerFlux/EIRP   1.0000000000000e+014
		Linear_PowerThreshold   6.3095734448019e-004
		TransmitOn              1
		ReceiveOn               0
		PVDataBase              Databases\Satellite\stkAllComm.tce
		RFIDataBase             Databases\Satellite\stkAllComm.rfi
		LaserDispersionAngle    0.00000
		KOCTimeStep             1.00000
		UseOutOfDate            Yes
		NearEarthOutOfDate       10.00000
		DeepSpaceOutOfDate       40.00000
		ModelIntrackUncert      Yes
		UseTrajectoryFilter     No
		UsePotVictimList        No
    END LaserCAT
    
    BEGIN RFI
		Mode                     TargetObject
		StartTime                1 Jul 2007 12:00:00.000000000
		StopTime                 1 Jul 2007 16:00:00.000000000
		RangeConstraint         500000000.00000
		MinElevationAng         0.34907
		Duration                0.00000
		ExclHalfAng             0.08727
		MaxPVtoScenario         10
		CenterFrequency         14000000000.00000
		BandWidth               20000000.00000
		Linear_PowerFlux/EIRP   1.0000000000000e+014
		Linear_PowerThreshold   6.3095734448019e-004
		TransmitOn              1
		ReceiveOn               0
		PVDataBase              Databases\Satellite\stkAllComm.tce
		RFIDataBase             Databases\Satellite\stkAllComm.rfi
		LaserDispersionAngle    0.00000
		KOCTimeStep             1.00000
		UseOutOfDate            Yes
		NearEarthOutOfDate       10.00000
		DeepSpaceOutOfDate       40.00000
		ModelIntrackUncert      Yes
		UseTrajectoryFilter     No
		UsePotVictimList        No
    END RFI
    
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
		MissionModelerTSFCUnit		TSFCLbmHrLbf
		MissionModelerPSFCUnit		PSFCLbmHrHp
		MissionModelerForceUnit		Pounds
		MissionModelerPowerUnit		Horsepower
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
		MissionModelerTSFCUnit		TSFCLbmHrLbf
		MissionModelerPSFCUnit		PSFCLbmHrHp
		MissionModelerForceUnit		Pounds
		MissionModelerPowerUnit		Horsepower
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
		MissionModelerTSFCUnit		TSFCLbmHrLbf
		MissionModelerPSFCUnit		PSFCLbmHrHp
		MissionModelerForceUnit		Pounds
		MissionModelerPowerUnit		Horsepower
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
    
    BEGIN FileLocations
    END FileLocations
    
    BEGIN Author
	Optimize	Yes
	UseBasicGlobe	Yes
	ReadOnly	No
	ViewerPassword	No
	STKPassword	No
    END Author
    
    BEGIN ExportDataFile
    FileType         Ephemeris
    Directory        C:\Documents and Settings\vcoppola\My Documents\STK 8.0
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
    ExportCovar      Position
    AttitudeFormat   Current
    TimePrecision      6
    CCSDSDateFormat    YMD
    CCSDSEphFormat     SciNotation
    CCSDSRefFrame      EME2000
    END ExportDataFile
    
    BEGIN Desc
    END Desc
    
    BEGIN RfEnv
<!-- STKv4.0 Format="XML" -->
<STKOBJECT>
<OBJECT Class = "RFEnvironment" Name = "STK_RF_Environment">
    <OBJECT Class = "link" Name = "ActiveCommSystem">
        <OBJECT Class = "string" Name = ""> &quot;None&quot; </OBJECT>
    </OBJECT>
    <OBJECT Class = "string" Name = "Description"> &quot;STK RF Environment&quot; </OBJECT>
    <OBJECT Class = "double" Name = "EarthTemperature"> 290 K </OBJECT>
    <OBJECT Class = "link" Name = "PropagationChannel">
        <OBJECT Class = "PropagationChannel" Name = "RF_Propagation_Channel">
            <OBJECT Class = "link" Name = "AtmosAbsorptionModel">
                <OBJECT Class = "AtmosphericAbsorptionModel" Name = "Simple_Satcom">
                    <OBJECT Class = "string" Name = "Description"> &quot;Simple Satcom&quot; </OBJECT>
                    <OBJECT Class = "bool" Name = "ReadOnly"> False </OBJECT>
                    <OBJECT Class = "double" Name = "SurfaceTemperature"> 293.15 K </OBJECT>
                    <OBJECT Class = "string" Name = "Type"> &quot;CAgCRRFPropModelAtmosAbsorptionSimpleSatcom&quot; </OBJECT>
                    <OBJECT Class = "string" Name = "UserComment"> &quot;Simple Satcom&quot; </OBJECT>
                    <OBJECT Class = "string" Name = "Version"> &quot;1.0.0 a&quot; </OBJECT>
                    <OBJECT Class = "double" Name = "WaterVaporConcentration"> 7.5 g*m^-3 </OBJECT>
                </OBJECT>
            </OBJECT>
            <OBJECT Class = "link" Name = "CloudFogModel">
                <OBJECT Class = "CloudFogLossModel" Name = "ITU_840-3">
                    <OBJECT Class = "double" Name = "CloudCeiling"> 3000 m </OBJECT>
                    <OBJECT Class = "double" Name = "CloudLayerThickness"> 500 m </OBJECT>
                    <OBJECT Class = "double" Name = "CloudLiqWaterDensity"> 7.5 g*m^-3 </OBJECT>
                    <OBJECT Class = "double" Name = "CloudTemp"> 273.15 K </OBJECT>
                    <OBJECT Class = "double" Name = "CloudWaterContent"> 3750 g*m^-2 </OBJECT>
                    <OBJECT Class = "string" Name = "Description"> &quot;ITU 840-3&quot; </OBJECT>
                    <OBJECT Class = "bool" Name = "ReadOnly"> False </OBJECT>
                    <OBJECT Class = "string" Name = "Type"> &quot;CAgCRRFPropModelCloudFogLossITU840_3&quot; </OBJECT>
                    <OBJECT Class = "string" Name = "UserComment"> &quot;ITU 840-3&quot; </OBJECT>
                    <OBJECT Class = "string" Name = "Version"> &quot;1.0.0 a&quot; </OBJECT>
                </OBJECT>
            </OBJECT>
            <OBJECT Class = "string" Name = "Description"> &quot;RF Propagation Channel&quot; </OBJECT>
            <OBJECT Class = "link" Name = "RainModel">
                <OBJECT Class = "RainLossModel" Name = "ITU-R_P618-8">
                    <OBJECT Class = "string" Name = "Description"> &quot;ITU-R P618-8&quot; </OBJECT>
                    <OBJECT Class = "bool" Name = "ReadOnly"> False </OBJECT>
                    <OBJECT Class = "double" Name = "SurfaceTemperature"> 273.15 K </OBJECT>
                    <OBJECT Class = "string" Name = "Type"> &quot;CAgCRRFPropModelRainLossITU618_8&quot; </OBJECT>
                    <OBJECT Class = "string" Name = "UserComment"> &quot;ITU-R P618-8&quot; </OBJECT>
                    <OBJECT Class = "string" Name = "Version"> &quot;1.0.0 a&quot; </OBJECT>
                </OBJECT>
            </OBJECT>
            <OBJECT Class = "bool" Name = "ReadOnly"> False </OBJECT>
            <OBJECT Class = "link" Name = "TropoScintModel">
                <OBJECT Class = "TropoScintLossModel" Name = "ITU_618-8_Scintillation">
                    <OBJECT Class = "bool" Name = "ComputeDeepFade"> False </OBJECT>
                    <OBJECT Class = "string" Name = "Description"> &quot;ITU 618-8 Scintillation&quot; </OBJECT>
                    <OBJECT Class = "double" Name = "FadeOutage"> 0.001 unitValue </OBJECT>
                    <OBJECT Class = "double" Name = "PercentTimeRefracGrad"> 0.1 unitValue </OBJECT>
                    <OBJECT Class = "bool" Name = "ReadOnly"> False </OBJECT>
                    <OBJECT Class = "string" Name = "Type"> &quot;CAgCRRFPropModelTropoScintLossITU618_8&quot; </OBJECT>
                    <OBJECT Class = "string" Name = "UserComment"> &quot;ITU 618-8 Scintillation&quot; </OBJECT>
                    <OBJECT Class = "string" Name = "Version"> &quot;1.0.0 a&quot; </OBJECT>
                </OBJECT>
            </OBJECT>
            <OBJECT Class = "string" Name = "Type"> &quot;CAgCRRFPropagationChannel&quot; </OBJECT>
            <OBJECT Class = "bool" Name = "UseAtmosAbsorptionModel"> False </OBJECT>
            <OBJECT Class = "bool" Name = "UseCloudFogModel"> False </OBJECT>
            <OBJECT Class = "bool" Name = "UseCustomA"> False </OBJECT>
            <OBJECT Class = "bool" Name = "UseCustomB"> False </OBJECT>
            <OBJECT Class = "bool" Name = "UseCustomC"> False </OBJECT>
            <OBJECT Class = "bool" Name = "UseRainModel"> False </OBJECT>
            <OBJECT Class = "string" Name = "UserComment"> &quot;RF Propagation Channel&quot; </OBJECT>
            <OBJECT Class = "bool" Name = "UseTropoScintModel"> False </OBJECT>
            <OBJECT Class = "string" Name = "Version"> &quot;1.0.0 a&quot; </OBJECT>
        </OBJECT>
    </OBJECT>
    <OBJECT Class = "string" Name = "RainOutagePercent"> &quot;0.100&quot; </OBJECT>
    <OBJECT Class = "bool" Name = "ReadOnly"> False </OBJECT>
    <OBJECT Class = "string" Name = "Type"> &quot;CAgSTKRFEnvironment&quot; </OBJECT>
    <OBJECT Class = "string" Name = "UserComment"> &quot;STK RF Environment&quot; </OBJECT>
    <OBJECT Class = "string" Name = "Version"> &quot;1.0.0 a&quot; </OBJECT>
</OBJECT>
</STKOBJECT>
    END RfEnv
    
    BEGIN CommRad
    END CommRad
    
    BEGIN RCS
	Inherited          False
	LinearClutterCoef        1.000000e+000
	BEGIN RCSBAND
		LinearConstantValue      1.000000e+000
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
        ReferenceDate         13 Apr 2007 04:00:00.000000000
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
        TideFile              tides\tides.dat
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

Class Satellite

	AstgEuropa
	AstgJupiterVOP
	AstgMars
	AstgMoon
	AstgSun
	HpopEuropa
	HpopJupiterVOP
	HpopMars
	HpopMoon
	HpopSun
	LopEarth

END Class

END SubObjects

BEGIN References
    Instance *
        *
    END Instance
    Instance Satellite/AstgEuropa
        Satellite/AstgEuropa
    END Instance
    Instance Satellite/AstgJupiterVOP
        Satellite/AstgJupiterVOP
    END Instance
    Instance Satellite/AstgMars
        Satellite/AstgMars
    END Instance
    Instance Satellite/AstgMoon
        Satellite/AstgMoon
    END Instance
    Instance Satellite/AstgSun
        Satellite/AstgSun
    END Instance
    Instance Satellite/HpopEuropa
        Satellite/HpopEuropa
    END Instance
    Instance Satellite/HpopJupiterVOP
        Satellite/HpopJupiterVOP
    END Instance
    Instance Satellite/HpopMars
        Satellite/HpopMars
    END Instance
    Instance Satellite/HpopMoon
        Satellite/HpopMoon
    END Instance
    Instance Satellite/HpopSun
        Satellite/HpopSun
    END Instance
    Instance Satellite/LopEarth
        Satellite/LopEarth
    END Instance
END References

END Scenario
