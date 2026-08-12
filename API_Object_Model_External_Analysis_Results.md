# API Object Model External Analysis Results

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Object_Model/External_Analysis_Results

---



## DeleteAllFrameForces

*Source file: `SAP2000_API_Fuctions/Object_Model/External_Analysis_Results/DeleteAllFrameForces.htm`*

# DeleteAllFrameForces

## Syntax

SapObject.SapModel.ExternalAnalysisResults.DeleteAllFrameForces

## VB6 Procedure

Function DeleteAllFrameForces () As Long

## Remarks

This function deletes all the external results previously provided for all frame objects. The function returns zero if the results are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAllFrameExternalResultForces ()

     'dimension variables

        Dim SapObject As Sap2000v16.SapObject

        Dim SapModel As cSapModel

        Dim ret As Long

        Dim ObjSta() As Double = New Double() {0.0, 124.0}

        Dim LoadCase() As String = New String() {"EXTERNAL"}

        Dim P() As Double = New Double() {5.0, 5.0}

        Dim V2() As Double = New Double() {-5.0, 5.0}

        Dim V3() As Double = Nothing

        Dim T() As Double = Nothing

        Dim M2() As Double = Nothing

        Dim M3() As Double = New Double() {100.0, 100.0}

        'create Sap2000 object

        SapObject = New Sap2000v16.SapObject

        'start Sap2000 application

        SapObject.ApplicationStart()

        'create SapModel object

        SapModel = SapObject.SapModel

        'initialize model

        ret = SapModel.InitializeNewModel

        'create model from template

        ret = SapModel.File.New2DFrame(e2DFrameType.PortalFrame, 3, 124, 3, 200)

        'create load case for external results

        ret = SapModel.LoadCases.ExternalResults.SetCase("EXTERNAL")

        'set cases and stations for frame external results

        ret = SapModel.ExternalAnalysisResults.PresetFrameCases("1", 1, LoadCase)

        ret = SapModel.ExternalAnalysisResults.SetFrameStations("1", ObjSta)

        'set frame external result forces at case first step

        ret = SapModel.ExternalAnalysisResults.SetFrameForce("1", "EXTERNAL", 0, P, V2, V3, T, M2, M3)

        'delete all frame external results

ret = SapModel.ExternalAnalysisResults.DeleteAllFrames()

        'close Sap2000

        SapObject.ApplicationExit(False)

        SapModel = Nothing

        SapObject = Nothing

    End Sub

## Release Notes

Initial release in version 16.00.



## DeleteFrameForces

*Source file: `SAP2000_API_Fuctions/Object_Model/External_Analysis_Results/DeleteFrameForces.htm`*

# DeleteFrameForces

## Syntax

SapObject.SapModel.ExternalAnalysisResults.DeleteFrameForces

## VB6 Procedure

Function DeleteFrameForces (Name As String) As Long

## Parameters

Name

The name of an existing frame object.

## Remarks

This function deletes all the external results previously provided for a given frame object. This function returns zero if the external results are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameExternalResults ()

      'dimension variables

        Dim SapObject As Sap2000v16.SapObject

        Dim SapModel As cSapModel

        Dim ret As Long

        Dim ObjSta() As Double = New Double() {0.0, 124.0}

        Dim LoadCase() As String = New String() {"EXTERNAL"}

        Dim P() As Double = New Double() {5.0, 5.0}

        Dim V2() As Double = New Double() {-5.0, 5.0}

        Dim V3() As Double = Nothing

        Dim T() As Double = Nothing

        Dim M2() As Double = Nothing

        Dim M3() As Double = New Double() {100.0, 100.0}

        'create Sap2000 object

        SapObject = New Sap2000v16.SapObject

        'start Sap2000 application

        SapObject.ApplicationStart()

        'create SapModel object

        SapModel = SapObject.SapModel

        'initialize model

        ret = SapModel.InitializeNewModel

        'create model from template

        ret = SapModel.File.New2DFrame(e2DFrameType.PortalFrame, 3, 124, 3, 200)

        'create load case for external results

        ret = SapModel.LoadCases.ExternalResults.SetCase("EXTERNAL")

        'set cases and stations for frame external results

        ret = SapModel.ExternalAnalysisResults.PresetFrameCases("1", 1, LoadCase)

        ret = SapModel.ExternalAnalysisResults.SetFrameStations("1", ObjSta)

        'set frame external result forces at case first step

        ret = SapModel.ExternalAnalysisResults.SetFrameForce("1", "EXTERNAL", 0, P, V2, V3, T, M2, M3)

        ret = SapModel.ExternalAnalysisResults.DeleteFrameForces("1")

        'close Sap2000

        SapObject.ApplicationExit(False)

        SapModel = Nothing

        SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.00.



## PresetFrameCases

*Source file: `SAP2000_API_Fuctions/Object_Model/External_Analysis_Results/FrameCases.htm`*

# PresetFrameCases

## Syntax

SapObject.SapModel.ExternalAnalysisResults.PresetFrameCases

## VB6 Procedure

Function PresetFrameCases(Name As String, ByVal Count As Long, ByRef casname() As String) As Long

## Parameters

Name

The name of an existing frame object.

Count

The length of the subsequent array.

casename

An array listing the names of previously defined external result load cases for which user-supplied external analysis results are available for the frame object.

## Remarks

Calling this function is optional, but it can speed up subsequent assignment of external analysis results which are available for more than one load case.

The first time this function is called for a particular frame object, it sets the list of names of external result load cases for which results relevant to the object are available. Subsequent calls to this function for the same object reset the results for load cases already in the list, and add load cases not already in.

This function returns zero if the stations are successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub PresetFrameExternalCases()

    'dimension variables

         Dim SapObject as cOAPI

        Dim SapModel As cSapModel

        Dim ret As Long

        Dim ObjSta() As Double = New Double() {0.0, 124.0}

        Dim LoadCase() As String = New String() {"EXTERNAL"}

        Dim P() As Double = New Double() {5.0, 5.0}

        Dim V2() As Double = New Double() {-5.0, 5.0}

        Dim V3() As Double = Nothing

        Dim T() As Double = Nothing

        Dim M2() As Double = Nothing

        Dim M3() As Double = New Double() {100.0, 100.0}

        'create Sap2000 object

        SapObject = New Sap2000v16.SapObject

        'start Sap2000 application

        SapObject.ApplicationStart()

        'create SapModel object

        SapModel = SapObject.SapModel

        'initialize model

        ret = SapModel.InitializeNewModel

        'create model from template

        ret = SapModel.File.New2DFrame(e2DFrameType.PortalFrame, 3, 124, 3, 200)

        'create load case for external results

        ret = SapModel.LoadCases.ExternalResults.SetCase("EXTERNAL")

        'set cases and stations for frame external results

        ret = SapModel.ExternalAnalysisResults.PresetFrameCases("1", 1, LoadCase)

        ret = SapModel.ExternalAnalysisResults.SetFrameStations("1", ObjSta)

        'set frame external result forces at case first step

        ret = SapModel.ExternalAnalysisResults.SetFrameForce("1", "EXTERNAL", 0, P, V2, V3, T, M2, M3)

        'close Sap2000

        SapObject.ApplicationExit(False)

        SapModel = Nothing

       SapObject = Nothing

    End Sub

## Release Notes

Initial release in version 16.00.



## GetFrameForces

*Source file: `SAP2000_API_Fuctions/Object_Model/External_Analysis_Results/GetFrameForces.htm`*

# GetFrameForces

## Syntax

SapObject.SapModel.ExternalAnalysisResults.GetFrameForce

## VB6 Procedure

Function GetFrameForce(ByVal Name As String, ByVal InitialCase As String, \_

                                       ByVal NumStep As Long, ByRef NumberStations As Long, \_

                                       ByRef P() As Double, ByRef V2() As Double, \_

                                       ByRef V3() As Double, ByRef T() As Double, \_

                                       ByRef M2() As Double, ByRef M3() As Double) As Long

## Parameters

Name

The name of an existing frame object.

InitialCase

The name of an existing external results load case for which external results relevant to the object may have been previously provided.

NumStep

The zero based index of a load case step: 0 for the first step, 1 for the second, and so on.

NumberStations

The number of frame stations on the object at which external result forces are reported.

P, V2, V3

One dimensional arrays that include the axial force, shear force in the local 2 direction, and shear force in the local 3 direction, respectively, for each frame station. [F]

T, M2, M3

One dimensional arrays that include the torsion, moment about the local 2axis, and moment about the local 3-axis, respectively, for each frame station. [FL]

## Remarks

This function reports the external result forces for a given step of a given external results load case on a given object.

The function returns zero if the external result forces are successfully recovered, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameExternalResultForces ()

'dimension variables

        Dim SapObject As Sap2000v16.SapObject

        Dim SapModel As cSapModel

        Dim ret As Long

        Dim ObjSta() As Double = New Double() {0.0, 124.0}

        Dim LoadCase() As String = New String() {"EXTERNAL"}

        Dim P() As Double = New Double() {5.0, 5.0}

        Dim V2() As Double = New Double() {-5.0, 5.0}

        Dim V3() As Double = Nothing

        Dim T() As Double = Nothing

        Dim M2() As Double = Nothing

        Dim M3() As Double = New Double() {100.0, 100.0}

        Dim numberStations As Long

        'create Sap2000 object

        SapObject = New Sap2000v16.SapObject

        'start Sap2000 application

        SapObject.ApplicationStart()

        'create SapModel object

        SapModel = SapObject.SapModel

        'initialize model

        ret = SapModel.InitializeNewModel()

        'create model from template

        ret = SapModel.File.New2DFrame(e2DFrameType.PortalFrame, 3, 124, 3, 200)

        'create load case for external results

        ret = SapModel.LoadCases.ExternalResults.SetCase("EXTERNAL")

        ret = SapModel.LoadCases.ExternalResults.SetNumberSteps("EXTERNAL", 1)

        'set cases and stations for frame external results

        ret = SapModel.ExternalAnalysisResults.PresetFrameCases("1", 1, LoadCase)

        ret = SapModel.ExternalAnalysisResults.SetFrameStations("1", ObjSta)

        'set frame external result forces at case first step

        ret = SapModel.ExternalAnalysisResults.SetFrameForce("1", "EXTERNAL", 0, P, V2, V3, T, M2, M3)

ret = SapModel.ExternalAnalysisResults.GetFrameForce("1", "EXTERNAL", 0, numberStations, P, V2, V3, T, M2, M3)

        'close Sap2000

 SapObject.ApplicationExit(False)

 SapModel = Nothing

       SapObject = Nothing

    End Sub

## Release Notes

Initial release in version 16.00.



## GetFrameStations

*Source file: `SAP2000_API_Fuctions/Object_Model/External_Analysis_Results/GetFrameStations.htm`*

# GetFrameStations

## Syntax

SapObject.SapModel.ExternalAnalysisResults.GetFrameStations

## VB6 Procedure

Function GetFrameStations(Name As String, ByRef nStations As Long, ByRef ObjSta() As Double) As Long

## Parameters

Name

The name of an existing frame object.

nStation

Number of the stations of an existing frame object.

ObjSta

This is an array that includes the distance measured from the I-end of the object to the result location.

## Remarks

This function gets the frame stations on a frame object for which user-supplied external analysis results are available.

The function returns zero if the stations are successfully get, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameExternalResultStations()

        'dimension variables

        Dim SapObject As Sap2000v16.SapObject

        Dim SapModel As cSapModel

        Dim ret As Long

        Dim ObjSta() As Double = New Double() {0.0, 124.0}

        Dim nStations As Long

        Dim Sta() As Double

        Dim LoadCase() As String = New String() {"EXTERNAL"}

        Dim P() As Double = New Double() {5.0, 5.0}

        Dim V2() As Double = New Double() {-5.0, 5.0}

        Dim V3() As Double = Nothing

        Dim T() As Double = Nothing

        Dim M2() As Double = Nothing

        Dim M3() As Double = New Double() {100.0, 100.0}

        'create Sap2000 object

        SapObject = New Sap2000v16.SapObject

        'start Sap2000 application

        SapObject.ApplicationStart()

        'create SapModel object

        SapModel = SapObject.SapModel

        'initialize model

        ret = SapModel.InitializeNewModel

        'create model from template

        ret = SapModel.File.New2DFrame(e2DFrameType.PortalFrame, 3, 124, 3, 200)

        'create load case for external results

        ret = SapModel.LoadCases.ExternalResults.SetCase("EXTERNAL")

        'set cases and stations for frame external results

        ret = SapModel.ExternalAnalysisResults.PresetFrameCases("1", 1, LoadCase)

        ret = SapModel.ExternalAnalysisResults.SetFrameStations("1", ObjSta)

        ret = SapModel.ExternalAnalysisResults.GetFrameStations("1", nStations, Sta)

        'set frame external result forces at case first step

        ret = SapModel.ExternalAnalysisResults.SetFrameForce("1", "EXTERNAL", 0, P, V2, V3, T, M2, M3)

        'close Sap2000

        SapObject.ApplicationExit(False)

        SapModel = Nothing

        SapObject = Nothing

    End Sub

## Release Notes

Initial release in version 16.00.



## SetFrameStations

*Source file: `SAP2000_API_Fuctions/Object_Model/External_Analysis_Results/SeFrameStations.htm`*

# SetFrameStations

## Syntax

SapObject.SapModel.ExternalAnalysisResults.SetFrameStations

## VB6 Procedure

Function SetFrameStations(Name As String, ByRef ObjSta() As Double) As Long

## Parameters

Name

The name of an existing frame object.

ObjSta

This is an array that includes the distance measured from the I-end of the object to the result location.

## Remarks

This function sets the frame stations on a frame object for which user-supplied external analysis results are available.

The function returns zero if the stations are successfully set, otherwise it returns a nonzero value.

## VBA Example

SubSetFrameExternalResultStations()

        'dimension variables

        Dim SapObject As Sap2000v16.SapObject

        Dim SapModel As cSapModel

        Dim ret As Long

        Dim ObjSta() As Double = New Double() {0.0, 124.0}

        Dim LoadCase() As String = New String() {"EXTERNAL"}

        Dim P() As Double = New Double() {5.0, 5.0}

        Dim V2() As Double = New Double() {-5.0, 5.0}

        Dim V3() As Double = Nothing

        Dim T() As Double = Nothing

        Dim M2() As Double = Nothing

        Dim M3() As Double = New Double() {100.0, 100.0}

        'create Sap2000 object

        SapObject = New Sap2000v16.SapObject

        'start Sap2000 application

        SapObject.ApplicationStart()

        'create SapModel object

        SapModel = SapObject.SapModel

        'initialize model

        ret = SapModel.InitializeNewModel

        'create model from template

        ret = SapModel.File.New2DFrame(e2DFrameType.PortalFrame, 3, 124, 3, 200)

        'create load case for external results

        ret = SapModel.LoadCases.ExternalResults.SetCase("EXTERNAL")

        'set cases and stations for frame external results

        ret = SapModel.ExternalAnalysisResults.PresetFrameCases("1", 1, LoadCase)

        ret = SapModel.ExternalAnalysisResults.SetFrameStations("1", ObjSta)

        'set frame external result forces at case first step

        ret = SapModel.ExternalAnalysisResults.SetFrameForce("1", "EXTERNAL", 0, P, V2, V3, T, M2, M3)

        'close Sap2000

        SapObject.ApplicationExit(False)

        SapModel = Nothing

        SapObject = Nothing

    End Sub

## Release Notes

Initial release in version 16.00.



## SetFrameForceMultiple

*Source file: `SAP2000_API_Fuctions/Object_Model/External_Analysis_Results/SetFrameForceMultiple.htm`*

# SetFrameForceMultiple

## Syntax

SapObject.SapModel.ExternalAnalysisResults.SetFrameForceMultiple

## VB6 Procedure

Function SetFrameForceMultiple(ByVal NumberFrameNames As Long, ByVal FrameName() As String, ByVal NumberLoadCases As Long, ByVal LoadCase() As String, ByVal FirstStep() As Long, ByVal LastStep() As Long, ByRef P() As Double, ByRef M2() As Double, ByRef M3() As Double) As Long

## Parameters

NumberFrameNames

The number of input frames

FrameName

An array of existing frame objects

NumberLoadCases

The number of input load cases

LoadCase

An array of existing external results load cases for which user-supplied external analysis results relevant to the frame objects are available.

FirstStep

An array of the first step values for each load case. This should be of length NumberLoadCases.

LastStep

An array of the last step values for each load case. This should be of length NumberLoadCases.

P

An array of the axial forces for each frame station. [F]

V2

An array of the shear forces in the local 2 direction for each frame station. [F]

V3

An array of the shear forces in the local 3 direction for each frame station. [F]

T

An array of the torsion for each frame station. [F]

M2

An array of the moment about the local 2-axis for each frame station. [F]

M3

An array of the moment about the local 3-axis for each frame station. [F]

## Remarks

This function sets the external result forces for all input frames and load cases.

The P, V2, V3, T, M2, M3 arrays should be of length:

(Sum of all steps for all input Load Cases) \* (Sum of all stations for all input Frames)

As an example, consider setting results for two Frames, each with two defined Stations, for two Load Cases, each Load Case containing three steps, eg First Step = 1, Last step = 3.

The values of this array will be iterated over in the following order:

The P[0] value will be the axial force for FrameName[0], LoadCase[0], FirstStep[0], 1st Station

The P[1] value will be the axial force for FrameName[0], LoadCase[0], FirstStep[0], 2nd Station

The P[2] value will be the axial force for FrameName[0], LoadCase[0], FirstStep[0]+1, 1st Station

The P[3] value will be the axial force for FrameName[0], LoadCase[0], FirstStep[0]+1, 2nd Station

The P[4] value will be the axial force for FrameName[0], LoadCase[0], LastStep[0], 1st Station

The P[5] value will be the axial force for FrameName[0], LoadCase[0], LastStep[0], 2nd Station

The P[6] value will be the axial force for FrameName[0], LoadCase[1], FirstStep[1], 1st Station

The P[7] value will be the axial force for FrameName[0], LoadCase[1], FirstStep[1], 2nd Station

The P[8] value will be the axial force for FrameName[0], LoadCase[1], FirstStep[1]+1, 1st Station

The P[9] value will be the axial force for FrameName[0], LoadCase[1], FirstStep[1]+1, 2nd Station

The P[10] value will be the axial force for FrameName[0], LoadCase[1], LastStep[1], 1st Station

The P[11] value will be the axial force for FrameName[0], LoadCase[1],  LastStep[1], 2nd Station

The P[12] value will be the axial force for FrameName[1], LoadCase[0], FirstStep[0], 1st Station

And so on…

The number of stations must be previously declared using SetFrameStations

Enter 0 for any unneeded values in these arrays

The function returns zero if the forces are successfully set, otherwise it returns a nonzero value.

## VBA Example

## Release Notes

Initial Release in version 16.0.0.



## SetFrameForce

*Source file: `SAP2000_API_Fuctions/Object_Model/External_Analysis_Results/SetFrameForces.htm`*

# SetFrameForce

## Syntax

SapObject.SapModel.ExternalAnalysisResults.SetFrameForce

## VB6 Procedure

Function SetFrameForce(ByVal Name As String, ByVal InitialCase As String, ByVal StepNum As Long, ByRef P() As Double, ByRef V2() As Double, ByRef V3() As Double, ByRef T() As Double, ByRef M2() As Double, ByRef M3() As Double) As Long

## Parameters

Name

The name of an existing frame object.

InitialCase

The name of an existing external results load case for which user-supplied external analysis results relevant to the object are available.

StepNum

The zero based index of a load case step: 0 for the first step, 1 for the second, and so on.

P, V2, V3

These are one dimensional arrays that include the axial force, shear force in the local 2 direction, and shear force in the local 3 direction, respectively, for each frame station.[F] These arrays are each expected to contain a number of values equal to the  previously declared number of stations at which external results are available for the object – see SapObject.SapModel.ExternalAnalysisResults.SetFrameStations() for that declaration.

If any of these arrays is empty, the function substitutes zero values for the missing values.

T, M2, M3

These are one dimensional arrays that include the torsion, moment about the local 2axis, and moment about the local 3-axis, respectively, for each frame station. [FL] Again, these arrays are each expected to contain a number of values equal to the  previously declared number of stations at which external results are provided for the object. If any of these arrays is empty, the function substitutes zero values for the missing values.

## Remarks

This function sets the external result forces for a given step of a given external results load case on a frame object.

The function returns zero if the forces are successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetFrameExternalResultForces ()

    'dimension variables

        Dim SapObject As Sap2000v16.SapObject

        Dim SapModel As cSapModel

        Dim ret As Long

        Dim ObjSta() As Double = New Double() {0.0, 124.0}

        Dim LoadCase() As String = New String() {"EXTERNAL"}

        Dim P() As Double = New Double() {5.0, 5.0}

        Dim V2() As Double = New Double() {-5.0, 5.0}

        Dim V3() As Double = Nothing

        Dim T() As Double = Nothing

        Dim M2() As Double = Nothing

        Dim M3() As Double = New Double() {100.0, 100.0}

        'create Sap2000 object

        SapObject = New Sap2000v16.SapObject

        'start Sap2000 application

        SapObject.ApplicationStart()

        'create SapModel object

        SapModel = SapObject.SapModel

        'initialize model

        ret = SapModel.InitializeNewModel

        'create model from template

        ret = SapModel.File.New2DFrame(e2DFrameType.PortalFrame, 3, 124, 3, 200)

        'create load case for external results

        ret = SapModel.LoadCases.ExternalResults.SetCase("EXTERNAL")

        'set cases and stations for frame external results

        ret = SapModel.ExternalAnalysisResults.PresetFrameCases("1", 1, LoadCase)

        ret = SapModel.ExternalAnalysisResults.SetFrameStations("1", ObjSta)

        'set frame external result forces at case first step

        ret = SapModel.ExternalAnalysisResults.SetFrameForce("1", "EXTERNAL", 0, P, V2, V3, T, M2, M3)

        'close Sap2000

        SapObject.ApplicationExit(False)

        SapModel = Nothing

        SapObject = Nothing

    End Sub

## Release Notes

Initial release in version 16.00.

