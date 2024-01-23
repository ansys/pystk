stk.v.12.0
WrittenBy    STK_v12.9.0

BEGIN Chain

    Name		 Target1ConstTDRSAircraft1
    BEGIN Definition
        Object		 Target/ChainTarget1
        Object		 Constellation/TDRS
        Object		 Aircraft/ChainAircraft1
        Recompute		 No
        LastRequestedToBeComputedInParallel		 No
        IntervalType		 0
        ComputeIntervalStart		 0
        ComputeIntervalStop		 14400
        ComputeIntervalPtr		
        BEGIN EVENTINTERVAL
            BEGIN Interval
                Start		 1 Jan 1997 00:00:00.000000000
                Stop		 1 Jan 1997 04:00:00.000000000
            END Interval
            IntervalState		 Explicit
        END EVENTINTERVAL

        ConstConstraintsByStrands		 Yes
        UseSaveIntervalFile		 No
        UseMinAngle		 No
        UseMaxAngle		 No
        UseMinLinkTime		 No
        LTDelayCriterion		 2
        TimeConvergence		 0.005
        AbsValueConvergence		 1e-14
        RelValueConvergence		 1e-08
        MaxTimeStep		 360
        MinTimeStep		 0.01
        UseLightTimeDelay		 Yes
        DetectEventsUsingSamplesOnly		 No
        UseLoadIntervalFile		 No
        AllowSameInstInStrands		 Yes
        KeepStrandsWithNoIntvls		 No
        ComputeOptimalPath		 No
        OptimalPathSampleTime		  1.0000000000000000e+01
        OptimalPathIncludeAccessEdgeTimesInSamples		 Yes
        OptimalPathNumBestStrandsToStore		 1
        OptimalPathMetric		 Distance
        OptimalPathLinkCompare		 Min
        OptimalPathStrandCompare		 Min
        OptimalPathCalcScalarIgnoreCommonParentLinks		 Yes
        SaveMode		 0

    END Definition

    BEGIN Extensions

        BEGIN ExternData
        END ExternData

        BEGIN ADFFileData
        END ADFFileData

        BEGIN Desc
        END Desc

        BEGIN Crdn
        END Crdn

        BEGIN Graphics

            BEGIN Attributes

                StaticColor		 #f08080
                AnimationColor		 #f08080
                OptStrandsColor		 #00ffff
                AnimationLineWidth		 1
                StaticLineWidth		 3
                OptStrandsLineWidth		 5

            END Attributes

            BEGIN Graphics
                ShowGfx		 On
                Show2dGfx		 On
                ShowStatic		 On
                ShowAnimationHighlight		 On
                ShowAnimationLine		 On
                ShowLinkDirection		 On
                ShowOptStrands		 On
                ShowOnly1stOptStrand		 On
                UseHideAnimGfxIfMoreThanNStrands		 On
                HideAnimGfxIfMoreThanNStrandsNum		 100000
            END Graphics
        END Graphics

        BEGIN VO
        END VO

    END Extensions

END Chain

