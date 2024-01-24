stk.v.8.0

BEGIN Chain

Name  ConstAssetChain
BEGIN Definition

   Type        Chain
   Operator    Or
   Order       1
   Recompute   No
   IntervalType    0
   ComputeIntervalStart    0.000000
   ComputeIntervalStop     86400.000000
   UseSaveIntervalFile    No
   UseMinAngle     No
   UseMaxAngle     No
   UseMinLinkTime     No
   LTDelayCriterion    2.000000
   TimeConvergence     0.005000
   AbsValueConvergence 1.000000e-014
   RelValueConvergence 1.000000e-008
   MaxTimeStep         360.000000
   MinTimeStep         1.000000e-002
   UseLightTimeDelay   No
    DetectEventsUsingSamplesOnly No
    Object  Facility/MidNorth
    Object  Constellation/AssetConst
   SaveMode    0
   UseLoadIntervalFile    No

END Definition

BEGIN Extensions
    
    BEGIN Graphics

BEGIN Attributes

StaticColor					#0000ff
AnimationColor					#ffff00
AnimationLineWidth					2.000000
StaticLineWidth					3.000000

END Attributes

BEGIN Graphics

    ShowStatic		Off
    ShowAnimationHighlight		On
    ShowAnimationLine		On
    ShowLinkDirection		Off

END Graphics
    END Graphics
    
    BEGIN Desc
        ShortText    0

        LongText    0

    END Desc
    
    BEGIN VO
    END VO

END Extensions

END Chain

