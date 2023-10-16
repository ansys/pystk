'#########################################################################################
' EXAMPLE VBS BASED SCRIPT "DIRECTION PROVIDER" PROVIDED BY THE USER
' PLEASE ADD YOUR MODEL IN THE USER "DIRECTION PROVIDER" MODEL AREA BELOW.
' DO NOT CHANGE ANYTHING ELSE IN THE SCRIPT
' If you change the file name then the function names below
' must be edited to match the file name
'#########################################################################################

Dim VB_NullDirectionProvider_globalVar
Dim VB_NullDirectionProvider_Inputs
Dim VB_NullDirectionProvider_Outputs
Dim gScanAzStepSize, gScanElStepSize, gScanMinAz, gScanMaxAz, gScanMinEl, gScanMaxEl, gScanAz, gScanEl, degToRad, radToDeg

degToRad = 0.01745329252
radToDeg = 57.29577951308
gScanAzStepSize = degToRad*4
gScanElStepSize = degToRad*4
gScanMinAz = -30*degToRad
gScanMaxAz = 30*degToRad
gScanMinEl = -30*degToRad
gScanMaxEl = 30*degToRad

gScanAz = gScanMinAz
gScanEl = gScanMinEl

'==========================================================================
' VB_NullDirectionProvider() fctn
'==========================================================================
Function VB_NullDirectionProvider ( argArray )

	Dim retVal

	If IsEmpty(argArray(0)) Then

		' do compute

		retVal = VB_NullDirectionProvider_compute( argArray )

	ElseIf argArray(0) = "register" Then

		VB_NullDirectionProvider_globalVar = -1

		retVal = VB_NullDirectionProvider_register()

	ElseIf argArray(0) = "compute" Then

		' do compute

		retVal = VB_NullDirectionProvider_compute( argArray )

	Else

		' bad call

		retVal = Empty

	End If

	VB_NullDirectionProvider = retVal

End Function

Function VB_NullDirectionProvider_register()

    Dim ac
	ReDim descripStr(3), argStr(18)

    ac = 0
	descripStr(0)="ArgumentType = Output"
	descripStr(1)="Name = IsDynamic"
	descripStr(2)="ArgumentName = IsDynamic"
	argStr(ac) = descripStr

    ac = ac + 1
	descripStr(0)="ArgumentType = Output"
	descripStr(1)="Name = NumDirections"
	descripStr(2)="ArgumentName = NumDirections"
	argStr(ac) = descripStr
	
    ac = ac + 1
    descripStr(0)="ArgumentType = Output"
    descripStr(1)="Name = Azimuths"
    descripStr(2)="ArgumentName = Azimuths"
    argStr(ac) = descripStr
    
    ac = ac + 1
    descripStr(0)="ArgumentType = Output"
    descripStr(1)="Name = Elevations"
    descripStr(2)="ArgumentName = Elevations"
    argStr(ac) = descripStr
	
	
	ReDim descripStr(4)

    ac = ac + 1
	descripStr(0)="ArgumentType = Input"
	descripStr(1)="Name = ObjectPath"
	descripStr(2)="ArgumentName = ObjectPath"
	descripStr(3)="Type = Value"
	argStr(ac) = descripStr

    ac = ac + 1
	descripStr(0)="ArgumentType = Input"
	descripStr(1)="Name = EpochSec"
	descripStr(2)="ArgumentName = EpochSec"
	descripStr(3)="Type = Value"
	argStr(ac) = descripStr

    ac = ac + 1
	descripStr(0)="ArgumentType = Input"
	descripStr(1)="Name = PosLLA"
	descripStr(2)="ArgumentName = PosLLA"
	descripStr(3)="Type = Value"
	argStr(ac) = descripStr

   ac = ac + 1
	descripStr(0)="ArgumentType = Input"
	descripStr(1)="Name = PosCBF"
	descripStr(2)="ArgumentName = PosCBF"
	descripStr(3)="Type = Value"
	argStr(ac) = descripStr
	
    ac = ac + 1
	descripStr(0)="ArgumentType = Input"
	descripStr(1)="Name = NumberOfMembers"
	descripStr(2)="ArgumentName = NumberOfMembers"
	descripStr(3)="Type = Value"
	argStr(ac) = descripStr

    ac = ac + 1
	descripStr(0)="ArgumentType = Input"
	descripStr(1)="Name = MemberPositionFormat"
	descripStr(2)="ArgumentName = MemberPositionFormat"
	descripStr(3)="Type = Value"
	argStr(ac) = descripStr
	
    ac = ac + 1
	descripStr(0)="ArgumentType = Input"
	descripStr(1)="Name = MemberPositions"
	descripStr(2)="ArgumentName = MemberPositions"
	descripStr(3)="Type = Value"
	argStr(ac) = descripStr
	
	ac = ac + 1
	descripStr(0)="ArgumentType = Input"
	descripStr(1)="Name = MemberFrequencies"
	descripStr(2)="ArgumentName = MemberFrequencies"
	descripStr(3)="Type = Value"
	argStr(ac) = descripStr

	ac = ac + 1
	descripStr(0)="ArgumentType = Input"
	descripStr(1)="Name = MemberPwrs"
	descripStr(2)="ArgumentName = MemberPwrs"
	descripStr(3)="Type = Value"
	argStr(ac) = descripStr
	
	ac = ac + 1
	descripStr(0)="ArgumentType = Input"
	descripStr(1)="Name = MemberCategories"
	descripStr(2)="ArgumentName = MemberCategories"
	descripStr(3)="Type = Value"
	argStr(ac) = descripStr
	
	
    'MsgBox  ac
	VB_NullDirectionProvider_register = argStr

End Function


Function VB_NullDirectionProvider_compute( inputData )

	' NOTE: inputData(0) is the call Mode, which is either Empty or 'compute'

	Dim outStr

	outStr = ""

	If VB_NullDirectionProvider_globalVar < 0 Then

		Set VB_NullDirectionProvider_Inputs = g_GetPluginArrayInterface("VB_NullDirectionProvider_Inputs")

		outStr = VB_NullDirectionProvider_Inputs.Describe()
		
		'displayDialog outStr , 800

		Set VB_NullDirectionProvider_Outputs = g_GetPluginArrayInterface("VB_NullDirectionProvider_Outputs")

		outStr = VB_NullDirectionProvider_Outputs.Describe()
		
		'displayDialog outStr , 800

		VB_NullDirectionProvider_globalVar = 1

		'MsgBox inputData(VB_NullDirectionProvider_Inputs.EpochSec)

	End If
	Redim returnValue(4)  ' Size should be equivalent to number of outputs being returned
	
	' Dim input parameters
    Dim ObjectPath, EpochSec, PosLLA, PosCBF, NumberOfMembers, MemberPositionFormat, MemberPositions, MemberFrequencies, MemberPwrs, MemberCategories
	
    ' Initialize Input values
	ObjectPath           = inputData(VB_NullDirectionProvider_Inputs.ObjectPath)
	EpochSec             = inputData(VB_NullDirectionProvider_Inputs.EpochSec)
	PosLLA               = inputData(VB_NullDirectionProvider_Inputs.PosLLA)
	PosCBF               = inputData(VB_NullDirectionProvider_Inputs.PosCBF)
	NumberOfMembers      = inputData(VB_NullDirectionProvider_Inputs.NumberOfMembers)
	MemberPositionFormat = inputData(VB_NullDirectionProvider_Inputs.MemberPositionFormat)
	MemberPositions      = inputData(VB_NullDirectionProvider_Inputs.MemberPositions)
	MemberFrequencies    = inputData(VB_NullDirectionProvider_Inputs.MemberFrequencies)
	MemberPwrs           = inputData(VB_NullDirectionProvider_Inputs.MemberPwrs)
	MemberCategories     = inputData(VB_NullDirectionProvider_Inputs.MemberCategories)
	
    ' Dim STK expected output parameters
	Dim IsDynamic, NumDirections
	Dim Azs(100, 1), Els(100, 1)
	Azs(1, 0) = 0
	Els(1, 0) = 0
 	
	
	'############################################################################################
	' USER PLUGIN DIRECTION PROVIDER MODEL AREA.
	' PLEASE REPLACE THE CODE BELOW WITH YOUR DIRECTION PROVIDER COMPUTATION MODEL
	'
	' This sample demonstrates how to dynamically return directions.
	'
	' All input and out paramters have been mapped to variables described below.
	'############################################################################################
	' NOTE: the outputs that are returned MUST be in the same order as registered
	' If IsDynamic is set to 0 (false), this script will only be called once and the same outputs 
	' will be used for every timestep.  Setting IsDynamic to 1 (true), this script will be called 
	' at every timestep.
	'
	' All directions specified as Azimuth and Elevation angles (see STK help) in degrees and 
	' relative to the entity's body coordinate system.
	'
	' Script input variables available to user:
	'		ObjectPath - Path of the object, i.e. objects fully qualified name.   string
	'		EpochSec   - Current simulation epoch seconds.                        double  
	'		PosLLA	   - Position the object in LLA.                              string
	'		PosCBF	   - Position the object in CBF.                              string
	'		NumberOfMembers - Number of members. Used to define size of input 
	'                         field arrays.                                       int
    '       MemberPositionFormat - Defines if memberPositions array will be 
	'                              relative position in Theta/Phi/Range (rad/rad/m)
	'                              or X/Y/Z (m/m/m)                               int  
	'		MemberPositions      - Member positions in format specified by
	'                              MemberPositionFormat.                          double(3)
    '       MemberFrequencies    -     double
    '       MemberPwrs      -     double
	'
	' Script outputs which must be filled in by the user:
	'       IsDynamic            - Indicates if script is time-dynamic (see above).   int
	'       NumDirections       - 
	'		Directions - Azimuth/Elevation(s) in antenna's coordinate system (rad/rad)

	

    ' Dim temporaries used for this particular example
	
    ' Initialize Output values
	' NOTE: Your doppler resolution will be limited to FreqStepSize, so be sure to 
	'       set NumPSDPts to achieve adequate doppler resolution.
	IsDynamic        = 1 

	'objPosLat = PosLLA(0)
	'objPosLon = PosLLA(1)
	'objPosAlt = PosLLA(2)


	' If any object is in radar range, use track mode determine who to track
	NumDirections = 0
	For i = 0 To NumberOfMembers - 1
	   If MemberCategories(i) <> 1 Then  ' If it's not an aircraft...treat it as a jammer and null it
	      Azs(0,NumDirections) = MemberPositions(3*i)
	      Els(0,NumDirections) = MemberPositions(3*i+1)
		  NumDirections = NumDirections+1 
	   End If
	 Next  
    
	'NumDirections = 1
	'Azs(0,0) = -45*degToRad 
	'Els(0,0) = 0*degToRad

 	' MODEL END
	
	
	' #####################################################
	returnValue(VB_NullDirectionProvider_Outputs.IsDynamic)      = IsDynamic
    returnValue(VB_NullDirectionProvider_Outputs.NumDirections)  = NumDirections
	returnValue(VB_NullDirectionProvider_Outputs.Azimuths)       = Azs
	returnValue(VB_NullDirectionProvider_Outputs.Elevations)     = Els

	'############################################################################################
	' END OF USER MODEL AREA	
	'############################################################################################

	VB_NullDirectionProvider_compute = returnValue

End Function
