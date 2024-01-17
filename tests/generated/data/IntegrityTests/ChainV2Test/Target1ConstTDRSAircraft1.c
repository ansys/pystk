stk.v.6.0

BEGIN Chain

Name  Target1ConstTDRSAircraft1
BEGIN Definition

   Type        Chain
   Operator    Or
   Order       1
   Recompute   NofM
   IntervalType    0
   ComputeIntervalStart    0.000000
   ComputeIntervalStop     14400.000000
   UseSaveIntervalFile    No
   UseMinAngle     No
   UseMaxAngle     No
   UseMinLinkTime     No
    Object  Target/ChainTarget1
    Object  Constellation/TDRS
    Object  Aircraft/ChainAircraft1
   SaveMode    0
   UseLoadIntervalFile    No

END Definition

BEGIN Extensions
    
    BEGIN Graphics

BEGIN Attributes

StaticColor					#f08080
AnimationColor					#f08080
AnimationLineWidth					1.000000
StaticLineWidth					3.000000

END Attributes

BEGIN Graphics

    ShowStatic		On
    ShowAnimationHighlight		On
    ShowAnimationLine		On
    ShowLinkDirection		On

END Graphics
    END Graphics
    
    BEGIN Desc
    END Desc

END Extensions

END Chain

