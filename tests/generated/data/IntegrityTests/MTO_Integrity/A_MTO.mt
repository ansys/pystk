stk.v.9.0
WrittenBy    STK_v9.0.0

BEGIN MTO

    Name           A_MTO
    Begin GeneralTrackData
        CentralBody    Earth
        SaveTracks     On
        IsStatic       Off
        BlockSize      1
        StoredDataType 21
    End GeneralTrackData

    Begin DefaultTrack
        Id             0
        Name           "TestMTO"
        InterpOrder    1
        GreatArcInterp Off
    End DefaultTrack

    Begin Tracks
    Begin Track
        Id             1
        Name           "Track_No_1"
        InterpOrder    1
        GreatArcInterp Off

        Begin TimeLLAPoints
        0.000000000000e+000 0.000000000000e+000 0.000000000000e+000 1.716000000000e+001
        3.600000000000e+003 3.490658503989e-002 3.490658503989e-002 7.161600000000e+002
        6.620000000000e+003 5.235987755983e-002 5.235987755983e-002 5.150800000000e+002
        1.080000000000e+004 6.981317007977e-002 6.981317007977e-002 9.165600000000e+002
        End Points
    End Track

    Begin Track
        Id             2
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        3.000000000029e-001 1.745329251994e-002 8.726646259972e-003 -4.830900000000e+002
        4.200000000000e+003 6.981317007977e-002 3.490658503989e-002 7.158200000000e+002
        7.200300000000e+003 1.047197551197e-001 9.599310885969e-003 -5.000000000000e+002
        1.140000000000e+004 1.570796326795e-001 3.490658503989e-002 7.900000000000e+002
        End Points
    End Track

    Begin Track
        Id             3
        Name           "Test MTO"
        InterpOrder    4
        GreatArcInterp Off

        Begin TimeLLAPoints
        0.000000000000e+000 7.443464290120e-006 0.000000000000e+000 3.818630001861e+005
        3.600000000000e+003 1.191407124739e-003 1.570796326795e+000 -5.702136496345e+006
        2.520000000000e+004 6.478947937874e-006 0.000000000000e+000 1.381863000162e+006
        2.880000000000e+004 2.978510413129e-003 1.570796326795e+000 -5.702133852165e+006
        End Points
    End Track

    Begin Track
        Id             4
        Name           "TestMTO"
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        2.459000000000e+003 2.967058710900e-001 -3.490670809815e-002 0.000000000000e+000
        6.620000000000e+003 -1.489298215307e+000 2.283076792946e+000 0.000000000000e+000
        9.659000000000e+003 2.967105954109e-001 -3.490504356634e-002 0.000000000000e+000
        1.382000000000e+004 -1.489298863429e+000 2.283185560513e+000 0.000000000000e+000
        End Points
    End Track

    Begin Track
        Id             5
        Name           "TestMTO"
        InterpOrder    6
        GreatArcInterp Off

        Begin TimeLLAPoints
        2.459000000000e+003 1.554849109798e+000 -5.375337273876e-001 7.952357398496e+002
        6.620000000000e+003 1.546875661671e+000 1.397585939180e+000 9.383590172427e+001
        9.659000000000e+003 1.554856379718e+000 -5.373463650370e-001 7.800000000000e+002
        1.382000000000e+004 1.546860719801e+000 1.397828509903e+000 8.000000000000e+001
        End Points
    End Track

    Begin Track
        Id             6
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        0.000000000000e+000 0.000000000000e+000 0.000000000000e+000 1.716000000000e+001
        3.600000000000e+003 3.490658503989e-002 3.490658503989e-002 7.161600000000e+002
        End Points
    End Track

    Begin Track
        Id             7
        InterpOrder    8
        GreatArcInterp Off

        Begin TimeLLAPoints
        3.000000000029e-001 1.745329251994e-002 8.726646259972e-003 -4.830900000000e+002
        4.200000000000e+003 6.981317007977e-002 3.490658503989e-002 7.158200000000e+002
        End Points
    End Track

    Begin Track
        Id             8
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        0.000000000000e+000 7.443464290120e-006 0.000000000000e+000 3.818630001861e+005
        3.600000000000e+003 1.191407124739e-003 1.570796326795e+000 -5.702136496345e+006
        End Points
    End Track

    Begin Track
        Id             9
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        2.459000000000e+003 2.967058710900e-001 -3.490670809815e-002 0.000000000000e+000
        6.620000000000e+003 -1.489298215307e+000 2.283076792946e+000 0.000000000000e+000
        End Points
    End Track

    Begin Track
        Id             10
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        2.459000000000e+003 1.554849109798e+000 -5.375337273876e-001 7.952357398496e+002
        6.620000000000e+003 1.546875661671e+000 1.397585939180e+000 9.383590172427e+001
        End Points
    End Track

    Begin Track
        Id             11
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        0.000000000000e+000 0.000000000000e+000 0.000000000000e+000 0.000000000000e+000
        3.600000000000e+003 3.490658503989e-002 3.490658503989e-002 7.000000000000e+002
        End Points
    End Track

    Begin Track
        Id             12
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        3.000000000029e-001 1.745329251994e-002 8.726646259972e-003 -4.830900000000e+002
        4.200000000000e+003 6.981317007977e-002 3.490658503989e-002 7.158200000000e+002
        End Points
    End Track

    Begin Track
        Id             13
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        0.000000000000e+000 7.443464290120e-006 0.000000000000e+000 3.818630001861e+005
        3.600000000000e+003 1.191407124739e-003 1.570796326795e+000 -5.702136496345e+006
        End Points
    End Track

    Begin Track
        Id             14
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        2.459000000000e+003 2.967058710900e-001 -3.490670809815e-002 0.000000000000e+000
        6.620000000000e+003 -1.489298215307e+000 2.283076792946e+000 0.000000000000e+000
        End Points
    End Track

    Begin Track
        Id             15
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        2.459000000000e+003 1.554849109798e+000 -5.375337273876e-001 7.952357398496e+002
        6.620000000000e+003 1.546875661671e+000 1.397585939180e+000 9.383590172427e+001
        End Points
    End Track

    Begin Track
        Id             16
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        0.000000000000e+000 0.000000000000e+000 0.000000000000e+000 0.000000000000e+000
        3.600000000000e+003 3.490658503989e-002 3.490658503989e-002 7.000000000000e+002
        End Points
    End Track

    Begin Track
        Id             17
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        3.000000000029e-001 1.745329251994e-002 8.726646259972e-003 -5.000000000000e+002
        4.200000000000e+003 6.981317007977e-002 3.490658503989e-002 7.000000000000e+002
        End Points
    End Track

    Begin Track
        Id             18
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        0.000000000000e+000 7.443464290120e-006 0.000000000000e+000 3.818630001861e+005
        3.600000000000e+003 1.191407124739e-003 1.570796326795e+000 -5.702136496345e+006
        End Points
    End Track

    Begin Track
        Id             19
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        2.459000000000e+003 2.967058710900e-001 -3.490670809815e-002 0.000000000000e+000
        6.620000000000e+003 -1.489298215307e+000 2.283076792946e+000 0.000000000000e+000
        End Points
    End Track

    Begin Track
        Id             20
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        2.459000000000e+003 1.554849109798e+000 -5.375337273876e-001 7.800000000000e+002
        6.620000000000e+003 1.546875661671e+000 1.397585939180e+000 8.000000000000e+001
        End Points
    End Track

    End Tracks


BEGIN Extensions
    
    BEGIN Graphics
        Show                  Yes

        Begin DefaultTrackGfx
            Show             Yes
            MarkerColor      #000d10
            MarkerStyle      3
            MarkerFile       C:/AUTO_TEST_RESULTS/STK/v8.1.0/Results/bgilbertpcxp_WinXP/AgUiApplication/Connect_Obj_MTO/DeleteMe/Milt4.bmp
            LabelColor       #000d10
            LineColor        #000d10
            ShowMarker       Yes
            ShowLabel        Yes
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        4
            UseDisplayTime   Yes
            DisplayTimes     -23.000000 -23.000000
            TranslucentTrail No
            UsePreFadeTime   Yes
            PreFadeTime      60.000000
            UsePostFadeTime  Yes
            PostFadeTime     60.000000
            Begin RangeContours
                ShowRangeContours  Yes
                ShowRangeFill      No
                RangeFillStyle     0
                DecimalPlaces      3
                LabelUnits         4
                BEGIN ContourLevel
                    Value      1.000000000000e-003
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  1
                    Numbered   Yes
                    ShowText   No
                    LabelAngle 180
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.000000000000e+000
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      2.400000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  1
                    Numbered   Yes
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      2.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   No
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      3.400000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       135
                    LabelAngle 180
                END ContourLevel
                BEGIN ContourLevel
                    Value      3.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   No
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      4.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   No
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      5.400000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   No
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      6.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   No
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      7.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       135
                    LabelAngle 180
                END ContourLevel
                BEGIN ContourLevel
                    Value      8.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      9.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.050000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.150000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.350000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.450000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 0
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.550000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 1
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.850000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   Yes
                    Text       This is not a lie 135
                    LabelAngle 180
                END ContourLevel
            End RangeContours
        End DefaultTrackGfx

        Begin TrackGfx
            Show             Yes
            MarkerColor      #000d10
            MarkerStyle      3
            MarkerFile       C:/AUTO_TEST_RESULTS/STK/v8.1.0/Results/bgilbertpcxp_WinXP/AgUiApplication/Connect_Obj_MTO/DeleteMe/Milt4.bmp
            LabelColor       #000d10
            LineColor        #000d10
            ShowMarker       Yes
            ShowLabel        Yes
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        4
            UseDisplayTime   Yes
            DisplayTimes     60.000000 60.000000
            TranslucentTrail No
            UsePreFadeTime   Yes
            PreFadeTime      60.000000
            UsePostFadeTime  Yes
            PostFadeTime     60.000000
            Begin RangeContours
                ShowRangeContours  Yes
                ShowRangeFill      No
                RangeFillStyle     0
                DecimalPlaces      3
                LabelUnits         4
                BEGIN ContourLevel
                    Value      1.000000000000e+000
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      2.400000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  1
                    Numbered   Yes
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      2.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   No
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      3.400000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       135
                    LabelAngle 180
                END ContourLevel
                BEGIN ContourLevel
                    Value      3.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   No
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      4.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   No
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      5.400000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   No
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      6.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   No
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      7.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       135
                    LabelAngle 180
                END ContourLevel
                BEGIN ContourLevel
                    Value      8.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      9.500000000000e+001
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.050000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.150000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.350000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   No
                    Text       This is not a lie
                    LabelAngle 135
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.450000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 0
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.550000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   Yes
                    Text       This is not a lie
                    LabelAngle 1
                END ContourLevel
                BEGIN ContourLevel
                    Value      1.850000000000e+002
                    Color      #ff0000
                    LineStyle  0
                    LineWidth  3
                    Numbered   Yes
                    ShowText   Yes
                    Text       This is not a lie 135
                    LabelAngle 180
                END ContourLevel
            End RangeContours
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      34
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     34.000000 34.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      34.000000
            UsePostFadeTime  No
            PostFadeTime     34.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx


        Begin TrackGfx
            Show             Yes
            MarkerColor      #00ff00
            MarkerStyle      1
            LabelColor       #00ff00
            LineColor        #00ff00
            ShowMarker       Yes
            ShowLabel        No
            Font             1
            ShowTrackLine    Yes
            LineWidth        1.000000
            LineStyle        0
            UseDisplayTime   No
            DisplayTimes     3600.000000 3600.000000
            TranslucentTrail No
            UsePreFadeTime   No
            PreFadeTime      0.000000
            UsePostFadeTime  No
            PostFadeTime     0.000000
        End TrackGfx

    END Graphics
    
    BEGIN VO
    END VO

END Extensions
END MTO

