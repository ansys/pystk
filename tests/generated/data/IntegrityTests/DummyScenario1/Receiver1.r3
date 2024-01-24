VO_V100
	ShowBoresight   No
    Begin GeneralVectorAxes
        ArrowPointSize          3.00
        PersistentLineWidth     2.00
        Scale                   15.848932
    End
    Begin VectorAxes
        Begin CrdnDef
            IsVector Yes
            IsCentralBodyFrame No
            Name "Boresight"
        End
        Begin RefCrdn
            IsVector No
            IsCentralBodyFrame No
            Name "Body"
            Object _Default
        End
        Duration                600.000
        IsShowing               No
        IsPersistent            No
        IsTransparent           No
        DrawFirstArrowOnly      Yes
        UseTrueScale            No
        Label                   Name
        DrawAtCentralBody       No
        ArrowType               3D
        ConnectType             Sweep
        ColorIndex              #ffa500
        IntervalType            AlwaysOn
        AngleUnit               deg
    End
    Begin VectorAxes
        Begin CrdnDef
            IsVector Yes
            IsCentralBodyFrame No
            Name "Sun"
            MagUnit km
        End
        Begin RefCrdn
            IsVector No
            IsCentralBodyFrame No
            Name "Body"
            Object _Default
        End
        Duration                600.000
        IsShowing               No
        IsPersistent            No
        IsTransparent           No
        DrawFirstArrowOnly      Yes
        UseTrueScale            No
        Label                   Name
        DrawAtCentralBody       No
        ArrowType               3D
        ConnectType             Sweep
        ColorIndex              #ffff00
        IntervalType            AlwaysOn
        AngleUnit               deg
    End
    Begin VectorAxes
        Begin CrdnDef
            IsVector Yes
            IsCentralBodyFrame No
            Name "Up"
        End
        Begin RefCrdn
            IsVector No
            IsCentralBodyFrame No
            Name "Body"
            Object _Default
        End
        Duration                600.000
        IsShowing               No
        IsPersistent            No
        IsTransparent           No
        DrawFirstArrowOnly      Yes
        UseTrueScale            No
        Label                   Name
        DrawAtCentralBody       No
        ArrowType               3D
        ConnectType             Sweep
        ColorIndex              #4169e1
        IntervalType            AlwaysOn
        AngleUnit               deg
    End
    Begin VectorAxes
        Begin CrdnDef
            IsVector No
            IsCentralBodyFrame No
            Name "Body"
        End
        Begin RefCrdn
            IsVector No
            IsCentralBodyFrame No
            Name "Body"
        End
        Duration                600.000
        IsShowing               No
        IsPersistent            No
        IsTransparent           No
        DrawFirstArrowOnly      Yes
        UseTrueScale            No
        Label                   Name
        DrawAtCentralBody       No
        ArrowType               3D
        ConnectType             Sweep
        ColorIndex              #00ff00
        IntervalType            AlwaysOn
        AngleUnit               deg
    End
    Begin VectorAngle
        FractionalScale                1.000000
        SupportingDihedralArcLineWidth 1.00
        ArcLineWidth                   2.00
        PixelThreshold                 0.500000
        Begin VectorAngleData
            Name                    "Sun"
            Show                    No
            ShowLabel               Yes
            ShowAngle               Yes
            ShowDihedralAngleSupportingArcs Yes
            ColorIndex              #ba55d3
            IntervalType            AlwaysOn
            Unit                    deg
        End
    End
    Begin Plane
    End
    VolumeSwapDist        -2.5000

    BEGIN VolumesGfx

	Show       Yes

    END VolumesGfx
