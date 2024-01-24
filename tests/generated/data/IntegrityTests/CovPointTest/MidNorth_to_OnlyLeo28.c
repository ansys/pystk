stk.v.8.0

BEGIN Chain

Name  MidNorth_to_OnlyLeo28
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
    Object  Satellite/Leo_28
   SaveMode    1
BEGIN StrandAccesses

  Strand    Facility/MidNorth To Satellite/Leo_28
    Start    0
    Stop     1175.8475518956307
    Start    8515.6758620459768
    Stop     10610.855965238639
    Start    17616.990408502883
    Stop     19861.303036771107
    Start    26820.196127212352
    Stop     29065.326114674783
    Start    36071.040763440658
    Stop     38162.724602883121
    Start    45523.132284190389
    Stop     46999.582726673798
    Start    84483.959061180212
    Stop     85895.96951830115
    Start    93299.243997503552
    Stop     95369.284901814026
    Start    102386.89065410984
    Stop     104625.4639019779
    Start    111585.12652198157
    Stop     113834.12737044346
    Start    120830.34547308846
    Stop     122944.85371729193
    Start    130247.1528230261
    Stop     131816.46942633169
    Start    169312.83375040538
    Stop     170606.75230764854
    Start    178084.48967885619
    Stop     180126.58558410261
    Start    187157.55247880914
    Stop     189389.42626537889
    Start    196350.3102163359
    Stop     198602.2660575984
    Start    205590.62219652729
    Stop     207725.41695061399
    Start    214977.71656277234
    Stop     216627.73583416876
    Start    254152.80547632961
    Stop     255304.90101410859
    Start    262871.53232040873
    Stop     264882.57007651927
    Start    271929.03599673114
    Stop     274153.18305691303
    Start    281115.74617504497
    Stop     283369.80979723478
    Start    290351.72944658506
    Stop     292504.51925082516
    Start    299713.62138561415
    Stop     301434.38000149198
    Start    339009.47911840607
    Stop     339984.47726184886
    Start    347660.50762031676
    Stop     349637.0174851034
    Start    356701.40517702099
    Stop     358916.71652928088
    Start    365881.44909705786
    Stop     368136.83194915752
    Start    375113.54096632538
    Stop     377282.24715638784
    Start    384453.94800782023
    Stop     386237.11608274229
    Start    423896.09997777815
    Stop     424631.87242812122
    Start    432451.57540179149
    Stop     434389.67289658595
    Start    441474.72525642684
    Stop     443679.99521014455
    Start    450647.4485723917
    Stop     452903.38804630557
    Start    459875.9537294386
    Stop     462058.68483812944
    Start    469197.99072286848
    Stop     471036.47473250894
    Start    508874.33353132469
    Stop     509184.97115237219
    Start    517244.92730461591
    Stop     519140.22673188878
    Start    526249.06529810978
    Stop     528442.98332347861
    Start    535413.7667317302
    Stop     537669.5391439565
    Start    544638.8768941348
    Stop     546833.91577639128
    Start    553945.18327778205
    Stop     555832.86241836124
    Start    602040.79699944728
    Stop     603888.32859168947
    Start    611024.48838756303
    Stop     613205.62520625396
    Start    620180.44203564047
    Stop     622435.33741971734
    Start    629402.23287045816
    Stop     631608.01090696361
    Start    638695.06293604919
    Stop     640626.60119809315
    Start    648501.98399210395
    Stop     649138.52392038191
    Start    686839.47520904779
    Stop     688633.54674338689
    Start    695801.0672859624
    Stop     697967.85698754271
    Start    704947.51579736837
    Stop     707200.83236416895
    Start    714165.95647886465
    Stop     716381.0568251533
    Start    723447.24427470146
    Stop     725417.94249811722
    Start    733131.20084482641
    Stop     734041.76521923998
    Start    771641.33049130486
    Stop     773375.35827012826
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
        ShortText    0

        LongText    0

    END Desc
    
    BEGIN VO
    END VO

END Extensions

END Chain

