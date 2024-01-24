stk.v.6.0

BEGIN Chain

Name  AngBtwn
BEGIN Definition

   Type        Chain
   Operator    Or
   Order       1
   Recompute   Yes
   IntervalType    0
   ComputeIntervalStart    0.000000
   ComputeIntervalStop     86400.000000
   UseSaveIntervalFile    No
   UseMinAngle     Yes
   MinAngle    0.698132
   UseMaxAngle     Yes
   MaxAngle    1.047198
   UseMinLinkTime     No
    Object  Planet/Sun
    Object  Satellite/FirstSat
    Object  Satellite/LastSat
   SaveMode    1
BEGIN StrandAccesses

END StrandAccesses

   UseLoadIntervalFile    No

END Definition

BEGIN Extensions
    
    BEGIN Graphics

BEGIN Attributes

StaticColor					#ffff00
AnimationColor					#ffff00
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

