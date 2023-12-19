stk.v.8.0

BEGIN Chain

Name  Chain1
BEGIN Definition

   Type        Chain
   Operator    Or
   Order       1
   Recompute   Yes
   IntervalType    0
   ComputeIntervalStart    0.000000
   ComputeIntervalStop     86400.000000
   UseSaveIntervalFile    No
   UseMinAngle     No
   UseMaxAngle     No
   UseMinLinkTime     No
   LTDelayCriterion    2.000000
   SaveMode    1
BEGIN StrandAccesses

END StrandAccesses

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
    END Desc
    
    BEGIN VO
    END VO

END Extensions

END Chain

