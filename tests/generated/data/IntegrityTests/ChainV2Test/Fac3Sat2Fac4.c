stk.v.6.0

BEGIN Chain

Name  Fac3Sat2Fac4
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
    Object  Facility/ChainFac3
    Object  Satellite/ChainSat2
    Object  Facility/ChainFac4
   SaveMode    0
   UseLoadIntervalFile    No

END Definition

BEGIN Extensions
    
    BEGIN Graphics

BEGIN Attributes

StaticColor					#00ffff
AnimationColor					#00ffff
AnimationLineWidth					1.000000
StaticLineWidth					4.000000

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

