stk.v.7.0

BEGIN Ship

Name		Ship1

BEGIN VehiclePath
	CentralBody				Earth
	StoreEphemeris				Yes
	SmoothInterp				No

    BEGIN GreatArc

        Method              DetTimeAccFromVel

        TimeOfFirstWaypoint 1 Jul 1999 00:00:00.000

        ArcGranularity      5.729577951308e-001
        AltRef              WGS84
        AltInterpMethod     EllipsoidHeight
        NumberOfWaypoints   0

        BEGIN Waypoints


        END Waypoints

    END GreatArc

END VehiclePath

BEGIN MassProperties

	Mass           1.000000000000e+003
	InertiaXX      4.500000000000e+003
	InertiaYX      0.000000000000e+000
	InertiaYY      4.500000000000e+003
	InertiaZX      0.000000000000e+000
	InertiaZY      0.000000000000e+000
	InertiaZZ      4.500000000000e+003

END MassProperties

BEGIN Attitude

     	ScenarioEpoch		 1 Jul 1999 00:00:00.000

      BEGIN Profile
          Name			 AircraftAtt
          StartTime			 0.000000000000e+000
          BEGIN Aircraft
             	Azimuth		 0.000000000000e+000
          END Aircraft
      END Profile

END Attitude

BEGIN Swath

    SwathType           ElevAngle
    ElevationAngle      0.000000000000e+000
    HalfAngle           0.000000000000e+000
    Distance            0.000000000000e+000
    RepType             NoSwath

END Swath

BEGIN Eclipse

    Sunlight                Off
    SunlightColor           #ffff00
    SunlightLineStyle       0
    SunlightLineWidth       3
    SunlightMarkerStyle     19

    Penumbra                Off
    PenumbraColor           #87cefa
    PenumbraLineStyle       0
    PenumbraLineWidth       3
    PenumbraMarkerStyle     19

    Umbra                   Off
    UmbraColor              #0000ff
    UmbraLineStyle          0
    UmbraLineWidth          3
    UmbraMarkerStyle        19

    SunlightPenumbraLine    Off
    PenumbraUmbraLine       Off

END Eclipse

BEGIN RealTimeDef

	HistoryDuration     1.800000000000e+003
	LookAheadDuration   1.800000000000e+003

END RealTimeDef


BEGIN LineOfSightModel

	ModelType     CbShape
	HeightAboveSurface   0.000000000000e+000

END LineOfSightModel


BEGIN Extensions
    
    BEGIN Graphics

        BEGIN GenericGraphics
            ShowPassLabel        Off
            ShowPathLabel        Off
            TransformTrajectory  On
            MaxGfxGndTrkTimeStep 6.000000000000e+002
            MaxGfxOrbitTimeStep  6.000000000000e+002
            ShowGlintPoint       Off
            ShowGlintColor       #ffffff
            ShowGlintStyle       2
        END GenericGraphics

        BEGIN AttributeData

            AttributeType    Basic
            IntvlHideShowAll Off

            BEGIN DefaultAttributes
                Show                 On
                Inherit              On
                ShowLabel            On
                ShowGndTrack         On
                ShowGndMarker        On
                ShowOrbit            On
                ShowOrbitMarker      On
                ShowElsetNum         Off
                MarkerColor          #ffa500
                GroundTrackColor     #ffa500
                SwathColor           #ffa500
                LabelColor           #ffa500
                LineStyle            0
                LineWidth            1.000000
                MarkerStyle          19
                FontStyle            0
            END DefaultAttributes

            BEGIN CustomIntervalList
                BEGIN DefaultAttributes
                    Show                 On
                    Inherit              On
                    ShowLabel            On
                    ShowGndTrack         On
                    ShowGndMarker        On
                    ShowOrbit            On
                    ShowOrbitMarker      On
                    ShowElsetNum         Off
                    MarkerColor          #ffa500
                    GroundTrackColor     #ffa500
                    SwathColor           #ffa500
                    LabelColor           #ffa500
                    LineStyle            0
                    LineWidth            1.000000
                    MarkerStyle          19
                    FontStyle            0
                END DefaultAttributes
            END CustomIntervalList

            BEGIN AccessIntervalsAttributes
                BEGIN AttrDuringAccess
                    Show                 On
                    Inherit              On
                    ShowLabel            On
                    ShowGndTrack         On
                    ShowGndMarker        On
                    ShowOrbit            On
                    ShowOrbitMarker      On
                    ShowElsetNum         Off
                    MarkerColor          #ffa500
                    GroundTrackColor     #ffa500
                    SwathColor           #ffa500
                    LabelColor           #ffa500
                    LineStyle            0
                    LineWidth            1.000000
                    MarkerStyle          4
                    FontStyle            0
                END AttrDuringAccess
                BEGIN AttrDuringNoAccess
                    Show                 Off
                    Inherit              On
                    ShowLabel            On
                    ShowGndTrack         On
                    ShowGndMarker        On
                    ShowOrbit            On
                    ShowOrbitMarker      On
                    ShowElsetNum         Off
                    MarkerColor          #ffa500
                    GroundTrackColor     #ffa500
                    SwathColor           #ffa500
                    LabelColor           #ffa500
                    LineStyle            0
                    LineWidth            1.000000
                    MarkerStyle          4
                    FontStyle            0
                END AttrDuringNoAccess
            END AccessIntervalsAttributes

            BEGIN RealTimeAttributes
                BEGIN HistoryAttr
                    Show                 On
                    Inherit              On
                    ShowLabel            On
                    ShowGndTrack         On
                    ShowGndMarker        On
                    ShowOrbit            On
                    ShowOrbitMarker      On
                    ShowElsetNum         Off
                    MarkerColor          #ffa500
                    GroundTrackColor     #ffa500
                    SwathColor           #ffa500
                    LabelColor           #ffa500
                    LineStyle            0
                    LineWidth            1.000000
                    MarkerStyle          4
                    FontStyle            0
                END HistoryAttr
                BEGIN SplineAttr
                    Show                 On
                    Inherit              On
                    ShowLabel            On
                    ShowGndTrack         On
                    ShowGndMarker        On
                    ShowOrbit            On
                    ShowOrbitMarker      On
                    ShowElsetNum         Off
                    MarkerColor          #ffff00
                    GroundTrackColor     #ffff00
                    SwathColor           #ffff00
                    LabelColor           #ffff00
                    LineStyle            0
                    LineWidth            1.000000
                    MarkerStyle          4
                    FontStyle            0
                END SplineAttr
                BEGIN LookAheadAttr
                    Show                 On
                    Inherit              On
                    ShowLabel            On
                    ShowGndTrack         On
                    ShowGndMarker        On
                    ShowOrbit            On
                    ShowOrbitMarker      On
                    ShowElsetNum         Off
                    MarkerColor          #ffffff
                    GroundTrackColor     #ffffff
                    SwathColor           #ffffff
                    LabelColor           #ffffff
                    LineStyle            0
                    LineWidth            1.000000
                    MarkerStyle          4
                    FontStyle            0
                END LookAheadAttr
                BEGIN DropOutAttr
                    Show                 On
                    Inherit              On
                    ShowLabel            On
                    ShowGndTrack         On
                    ShowGndMarker        On
                    ShowOrbit            On
                    ShowOrbitMarker      On
                    ShowElsetNum         Off
                    MarkerColor          #ff0000
                    GroundTrackColor     #ff0000
                    SwathColor           #ff0000
                    LabelColor           #ff0000
                    LineStyle            0
                    LineWidth            1.000000
                    MarkerStyle          4
                    FontStyle            0
                END DropOutAttr
            END RealTimeAttributes
        END AttributeData

        BEGIN LeadTrailData
                GtLeadingType             AllData
                GtTrailingType            AllData
                OrbitLeadingType          AllData
                OrbitTrailingType         OnePass
        END LeadTrailData
            BEGIN SaaData
               ShowSaa            Off
               ShowSaaFill        Off
               SaaFillStyle       7
               TrackSaa           On
               SaaAltitude        500000.000000
            END SaaData
            BEGIN WaypointData
                ShowWayptMarkers           On
                ShowWayptTurnMarkers       On
                ShowWayptMarkersExtEphem   Off
                NewWayptMarkerShow         On
                NewWayptShowLabel          Off
                NewWayptMarkerStyle        3
                WayptShowLabel             Off
                WayptMarkerStyle           3
            END WaypointData
        BEGIN EllipseSetGxData
            BEGIN DefEllipseSetGx
                ShowStatic     On
                ShowDynamic    On
                UseLastDynPos  Off
                HoldLastDynPos Off
                ShowName       Off
                ShowMarker     On
                MarkerStyle    0
                LineStyle      0
                LineWidth      1.000000
            END DefEllipseSetGx
        END EllipseSetGxData
    END Graphics
    
    BEGIN LaserCAT
		Mode                     TargetObject
		StartTime                1 Jun 2004 12:00:00.000000000
		StopTime                 2 Jun 2004 12:00:00.000000000
		RangeConstraint         500000000.00000
		MinElevationAng         0.34907
		Duration                0.00000
		ExclHalfAng             0.08727
		MaxPVtoScenario         10
		CenterFrequency         14000000000.00000
		BandWidth               20000000.00000
		PowerFlux/EIRP          140.00000
		PowerThreshold          -32.00000
		TransmitOn              1
		ReceiveOn               0
		PVDataBase              STKData\Databases\Satellite\stkAllActive.tce
		RFIDataBase             STKData\Databases\Satellite\stkAllActive.rfi
		LaserDispersionAngle    0.00000
		KOCTimeStep             1.00000
		UseOutOfDate            Yes
		NearEarthOutOfDate       10.00000
		DeepSpaceOutOfDate       40.00000
		ModelIntrackUncert      Yes
		UseTrajectoryFilter     No
		UsePotVictimList        No
    END LaserCAT
    
    BEGIN ExternData
    END ExternData
    
    BEGIN RFI
		Mode                     TargetObject
		StartTime                1 Jun 2004 12:00:00.000000000
		StopTime                 2 Jun 2004 12:00:00.000000000
		RangeConstraint         500000000.00000
		MinElevationAng         0.34907
		Duration                0.00000
		ExclHalfAng             0.08727
		MaxPVtoScenario         10
		CenterFrequency         14000000000.00000
		BandWidth               20000000.00000
		PowerFlux/EIRP          140.00000
		PowerThreshold          -32.00000
		TransmitOn              1
		ReceiveOn               0
		PVDataBase              STKData\Databases\Satellite\stkAllActive.tce
		RFIDataBase             STKData\Databases\Satellite\stkAllActive.rfi
		LaserDispersionAngle    0.00000
		KOCTimeStep             1.00000
		UseOutOfDate            Yes
		NearEarthOutOfDate       10.00000
		DeepSpaceOutOfDate       40.00000
		ModelIntrackUncert      Yes
		UseTrajectoryFilter     No
		UsePotVictimList        No
    END RFI
    
    BEGIN AccessConstraints
		LineOfSight   IncludeIntervals 
    END AccessConstraints
    
    BEGIN ObjectCoverage
    END ObjectCoverage
    
    BEGIN Desc
    END Desc
    
    BEGIN Atmosphere
	Inherit          Yes

	BEGIN Absorption

		AbsorptionModel	Simple Satcom

		BEGIN ModelData
			SWVC		    7.500000
			Temperature		293.150000

		END ModelData

	END Absorption

	RainOverride          No
	IsoHeight         2000.000000
	RainRate          1.000000
	RainModelSurfaceTemp		293.150000
    END Atmosphere
    
    BEGIN Ellipse
        TimesTrackVehStartTime Yes
    END Ellipse
    
    BEGIN Crdn
    END Crdn
    
    BEGIN VO
    END VO

END Extensions

BEGIN SubObjects

END SubObjects

END Ship

