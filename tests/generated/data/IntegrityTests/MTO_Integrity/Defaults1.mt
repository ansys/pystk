stk.v.9.0
WrittenBy    STK_v9.0.0

BEGIN MTO

    Name           Defaults1
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
    END Graphics
    
    BEGIN VO
    END VO

END Extensions
END MTO

