stk.v.12.0
WrittenBy    STK_v12.7.0

BEGIN Planet

    Name		 MarsJPL

    BEGIN PathDescription

        CentralBody		 Sun
        UseCbEphemeris		 Yes

        BEGIN EphemerisData

            EphemerisSource		 JplDE

            JplIndex		 10

            JplSpiceId		 10

            ApplyTDTtoTDBCorrectionForDE		 Yes

        END EphemerisData

    END PathDescription

    BEGIN PhysicalData

        GM		  1.3271220000000000e+20
        Radius		  6.9550800000000000e+08
        Magnitude		  0.0000000000000000e+00
        ReferenceDistance		  0.0000000000000000e+00

    END PhysicalData

    BEGIN AutoRename

        AutoRename		 Yes

    END AutoRename

    BEGIN Extensions

        BEGIN ExternData
        END ExternData

        BEGIN ADFFileData
        END ADFFileData

        BEGIN AccessConstraints
            LineOfSight IncludeIntervals

            UsePreferredMaxStep No
            PreferredMaxStep 360
        END AccessConstraints

        BEGIN Desc
        END Desc

        BEGIN Crdn
        END Crdn

        BEGIN Graphics

            BEGIN Attributes

                MarkerColor		 #ffffff
                LabelColor		 #ffffff
                LineColor		 #ffffff
                LineStyle		 0
                LineWidth		 1
                MarkerStyle		 2
                FontStyle		 0

            END Attributes

            BEGIN Graphics

                Show		 On
                Inherit		 On
                ShowLabel		 On
                ShowPlanetPoint		 On
                ShowSubPlanetPoint		 On
                ShowSubPlanetLabel		 On
                ShowOrbit		 Off
                NumOrbitPoints		 360
                OrbitTime		  0.0000000000000000e+00
                OrbitDisplay		                OneOrbit		
                TransformTrajectory		 On

            END Graphics
        END Graphics

        BEGIN VO
        END VO

    END Extensions

END Planet

