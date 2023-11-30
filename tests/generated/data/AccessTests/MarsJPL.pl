stk.v.12.0
WrittenBy    STK_v12.9.0

BEGIN Planet

    Name		 MarsJPL

    BEGIN PathDescription

        CentralBody		 Mars
        UseCbEphemeris		 Yes

        BEGIN EphemerisData

            EphemerisSource		 JplDE

            JplIndex		 3

            JplSpiceId		 10

            ApplyTDTtoTDBCorrectionForDE		 No

        END EphemerisData

    END PathDescription

    BEGIN PhysicalData

        GM		  0.0000000000000000e+00
        Radius		  3.3972000000000000e+06
        Magnitude		  0.0000000000000000e+00
        ReferenceDistance		  0.0000000000000000e+00
        Period		  5.9356394119309999e+07

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

        BEGIN ChainProcessingDelay
            ConstantDelay		  0.0000000000000000e+00
        END ChainProcessingDelay

        BEGIN Graphics

            BEGIN Attributes

                MarkerColor		 #00ff00
                LabelColor		 #00ff00
                LineColor		 #00ff00
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

