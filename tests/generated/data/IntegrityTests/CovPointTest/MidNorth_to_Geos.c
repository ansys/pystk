stk.v.8.0

BEGIN Chain

Name  MidNorth_to_Geos
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
   TimeConvergence     0.005000
   AbsValueConvergence 1.000000e-014
   RelValueConvergence 1.000000e-008
   MaxTimeStep         360.000000
   MinTimeStep         1.000000e-002
   UseLightTimeDelay   Yes
    DetectEventsUsingSamplesOnly No
    Object  Facility/MidNorth
    Object  Constellation/Geos_AnyOf
   SaveMode    1
BEGIN StrandAccesses

  Strand    Facility/MidNorth To Satellite/Geo_m100
    Start    0
    Stop     777600
  Strand    Facility/MidNorth To Satellite/SuperGeo_80
    Start    75248.792315002938
    Stop     191836.89142659711
    Start    332337.20254341682
    Stop     448925.78017948515
    Start    589425.80807188177
    Stop     706014.4535931783
END StrandAccesses

   UseLoadIntervalFile    No

END Definition

BEGIN Extensions
    
    BEGIN Graphics

BEGIN Attributes

StaticColor					#0000ff
AnimationColor					#00ff00
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

