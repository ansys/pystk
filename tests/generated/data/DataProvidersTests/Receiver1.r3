VO_v60
	ShowBoresight   No
    Begin GeneralVectorAxes
        ArrowPointSize          3.00
        PersistentLineWidth     2.00
        Scale                   10000.000000
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
        End
        Duration                600.000
        IsShowing               No
        IsPersistent            No
        IsTransparent           No
        DrawFirstArrowOnly      Yes
        DrawAtCentralBody       No
        ArrowType               3D
        ConnectType             Sweep
        ColorIndex              #00ffff
        IntervalType            AlwaysOn
        AngleUnit               deg
    End
    Begin VectorAxes
        Begin CrdnDef
            IsVector Yes
            IsCentralBodyFrame No
            Name "Sun"
            MagUnit m
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
        End
        Duration                600.000
        IsShowing               No
        IsPersistent            No
        IsTransparent           No
        DrawFirstArrowOnly      Yes
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
        DrawAtCentralBody       No
        ArrowType               3D
        ConnectType             Sweep
        ColorIndex              #fff0f5
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
            ShowLabel               No
            ShowAngle               No
            ColorIndex              #ba55d3
            IntervalType            AlwaysOn
            Unit                    deg
        End
    End
