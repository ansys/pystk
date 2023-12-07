stk.v.11.0
WrittenBy    STK_v11.4.0

BEGIN MTO

    Name		 MTO1
    BEGIN GeneralTrackData
        CentralBody		 Earth
        SaveTracks		 On
        SaveAsBinary		 Off
        IsStatic		 Off
        StaticGeometry		 Off
        BlockSize		 20
        StoredDataType		 21
        Epoch		 20 Jul 2017 16:00:00.000000
    END GeneralTrackData

    BEGIN DefaultTrack
        Id		 0
        InterpOrder		 0
        GreatArcInterp		 Off
    END DefaultTrack

    BEGIN Tracks
        BEGIN Track
            Id		 1
            InterpOrder		 0
            GreatArcInterp		 Off
            NumPts		 1

            BEGIN TimeLLAPoints
                0.0000000000000000e+00 8.7266462599719999e-02 0.0000000000000000e+00 1.0000000000000000e+04
            END Points
        END Track

        BEGIN Track
            Id		 2
            InterpOrder		 0
            GreatArcInterp		 Off
            NumPts		 1

            BEGIN TimeLLAPoints
                3.6000000999999975e+03 1.7453292519940000e-01 -1.7453292519940000e-01 1.0000000000000000e+05
            END Points
        END Track

        BEGIN Track
            Id		 3
            InterpOrder		 0
            GreatArcInterp		 Off
            NumPts		 1

            BEGIN TimeLLAPoints
                7.2000000000000000e+03 2.6179938779910000e-01 -3.4906585039889998e-01 3.0000000000000000e+05
            END Points
        END Track

    END Tracks


    BEGIN Extensions

        BEGIN ADFFileData
        END ADFFileData

        BEGIN Desc
            BEGIN ShortText

            END ShortText
            BEGIN LongText

            END LongText
        END Desc

        BEGIN Crdn
        END Crdn

        BEGIN Graphics
            ShowAll		 Yes
            Show		 Yes

            BEGIN DefaultTrackGfx
                Show		 Yes
                MarkerColor		 #00ff00
                MarkerStyle		 0
                LabelColor		 #00ff00
                LineColor		 #00ff0000
                ShowMarker		 Yes
                ShowLabel		 No
                Font		 1
                ShowTrackLine		 Yes
                LineWidth		 1
                LineStyle		 0
                UseDisplayTime		 No
                DisplayTimes		 3600 3600
                TranslucentTrail		 No
                UsePreFadeTime		 No
                PreFadeTime		 0
                UsePostFadeTime		 No
                PostFadeTime		 0
            END DefaultTrackGfx

            BEGIN TrackGfx
                Show		 Yes
                MarkerColor		 #00ff00
                MarkerStyle		 0
                LabelColor		 #00ff00
                LineColor		 #00ff0000
                ShowMarker		 Yes
                ShowLabel		 No
                Font		 1
                ShowTrackLine		 Yes
                LineWidth		 1
                LineStyle		 0
                UseDisplayTime		 No
                DisplayTimes		 3600 3600
                TranslucentTrail		 No
                UsePreFadeTime		 No
                PreFadeTime		 0
                UsePostFadeTime		 No
                PostFadeTime		 0
            END TrackGfx


            BEGIN TrackGfx
                Show		 Yes
                MarkerColor		 #00ff00
                MarkerStyle		 0
                LabelColor		 #00ff00
                LineColor		 #00ff0000
                ShowMarker		 Yes
                ShowLabel		 No
                Font		 1
                ShowTrackLine		 Yes
                LineWidth		 1
                LineStyle		 0
                UseDisplayTime		 No
                DisplayTimes		 3600 3600
                TranslucentTrail		 No
                UsePreFadeTime		 No
                PreFadeTime		 0
                UsePostFadeTime		 No
                PostFadeTime		 0
            END TrackGfx


            BEGIN TrackGfx
                Show		 Yes
                MarkerColor		 #00ff00
                MarkerStyle		 0
                LabelColor		 #00ff00
                LineColor		 #00ff0000
                ShowMarker		 Yes
                ShowLabel		 No
                Font		 1
                ShowTrackLine		 Yes
                LineWidth		 1
                LineStyle		 0
                UseDisplayTime		 No
                DisplayTimes		 3600 3600
                TranslucentTrail		 No
                UsePreFadeTime		 No
                PreFadeTime		 0
                UsePostFadeTime		 No
                PostFadeTime		 0
            END TrackGfx

        END Graphics

        BEGIN VO
        END VO

    END Extensions
END MTO

