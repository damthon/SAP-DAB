# API Definitions External Results

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Definitions/External_Results

---



## SetCase

*Source file: `SAP2000_API_Fuctions/Definitions/External_Results/SetCase.htm`*

# SetCase

## Syntax

SapObject.SapModel.LoadCases.ExternalResults.SetCase

## VB6 Procedure

Function SetCase(ByVal Name As String) As Long

## Parameters

Name

The name of an existing or new load case for which user-supplied external analysis results are available for some frame objects. If this is an existing case, that case is modified; otherwise, a new case is added.

## Remarks

This function initializes an external results load case. If this function is called for an existing load case, all items for the case are reset to their default value.

The function returns zero if the load case is successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetFrameExternalResultStations()

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

Initial release in version 16.0



## SetNumberSteps

*Source file: `SAP2000_API_Fuctions/Definitions/External_Results/SetNumberSteps.htm`*

# SetNumberSteps

## Syntax

SapObject.SapModel.LoadCases.ExternalResults.SetNumberSteps

## VB6 Procedure

Function SetNumberSteps (ByVal Name As String, ByVal FirstStep As Long, ByVal LastStep As Long) As Long

## Parameters

Name

The name of an existing external results load case.

FirstStep

The number of the first step for which external results are to be subsequently provided for frame objects in conjunction with this load case. The value may be 0 or 1. A value of zero is typically used for cases that include the initial conditions, such as time-history cases.

LastStep

The number of the last step for which external results are to be subsequently provided for frame objects in conjunction with this load case. The value must be greater than or equal to FirstStep.

## Remarks

In the absence of a call to this function, the default values are FirstStep = 1 and LastStep = 1.

The number of steps available for this load case will be LastStep – FirstStep + 1.

The function returns zero if the number of steps is successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetFrameExternalResultStations()

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

        ret = SapModel.LoadCases.ExternalResults.SetNumberSteps("EXTERNAL", 1, 1)

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

Initial release in version 16.0

