stk.v.9.0
WrittenBy    STK_v9.0.0

BEGIN MTO

    Name           VisTest2_MTO
    Begin GeneralTrackData
        CentralBody    Earth
        SaveTracks     On
        IsStatic       Off
        BlockSize      10
        StoredDataType 21
    End GeneralTrackData

    Begin DefaultTrack
        Id             0
        InterpOrder    0
        GreatArcInterp Off
    End DefaultTrack

    Begin Tracks
    Begin Track
        Id             2
        Name           "Track2"
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        0.000000000000e+000 3.490658503989e-002 -7.504915783576e-001 0.000000000000e+000
        6.000000000000e+002 3.490658503989e-002 -7.155849933177e-001 0.000000000000e+000
        1.200000000000e+003 6.981317007977e-002 -7.155849933177e-001 0.000000000000e+000
        1.800000000000e+003 6.981317007977e-002 -7.504915783576e-001 0.000000000000e+000
        2.400000000000e+003 3.490658503989e-002 -7.504915783576e-001 0.000000000000e+000
        End Points
    End Track

    Begin Track
        Id             3
        Name           "Track3"
        InterpOrder    0
        GreatArcInterp Off

        Begin TimeLLAPoints
        0.000000000000e+000 6.981317007977e-002 -6.981317007977e-001 0.000000000000e+000
        6.000000000000e+002 6.981317007977e-002 -6.632251157578e-001 0.000000000000e+000
        6.000000000000e+002 1.047197551197e-001 -6.632251157578e-001 0.000000000000e+000
        1.200000000000e+003 1.047197551197e-001 -6.981317007977e-001 0.000000000000e+000
        1.800000000000e+003 6.981317007977e-002 -6.981317007977e-001 0.000000000000e+000
        End Points
    End Track

    End Tracks


BEGIN Extensions
    
    BEGIN Graphics
        Show                  Yes

        Begin DefaultTrackGfx
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
        End DefaultTrackGfx

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

