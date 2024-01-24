stk.v.6.0

BEGIN Chain

Name  ChainToReport
BEGIN Definition

   Type        Chain
   Operator    Or
   Order       1
   Recompute   NofM
   IntervalType    0
   ComputeIntervalStart    0.000000
   ComputeIntervalStop     86400.000000
   UseSaveIntervalFile    No
   UseMinAngle     No
   UseMaxAngle     No
   UseMinLinkTime     No
    Object  Constellation/GroundConstellation
    Object  Constellation/LEOConstellation
   SaveMode    0
   UseLoadIntervalFile    No

END Definition

BEGIN Extensions
    
    BEGIN Graphics

BEGIN Attributes

StaticColor					#0000ff
AnimationColor					#0000ff
AnimationLineWidth					1.000000
StaticLineWidth					3.000000

END Attributes

BEGIN Graphics

    ShowStatic		Off
    ShowAnimationHighlight		Off
    ShowAnimationLine		On
    ShowLinkDirection		Off

END Graphics
    END Graphics
    
    BEGIN Desc
    END Desc

END Extensions

END Chain

