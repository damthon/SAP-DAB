# API Definitions Generalized Displacement

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Definitions/Generalized_Displacement

---



## Add {Generalized Displacement}

*Source file: `SAP2000_API_Fuctions/Definitions/Generalized_Displacement/Add_{Generalized_Displacement}.htm`*

# Add

## Syntax

SapObject.SapModel.GDispl.Add

## VB6 Procedure

Function Add(ByVal Name As String, ByVal MyType As Long) As Long

## Parameters

Name

The name of a new generalized displacement.

MyType

This is 1 or 2 indicating the generalized displacement type.

1 = Translational

2 = Rotational

## Remarks

This function adds a new generalized displacement with the specified name and type.

The function returns zero if the generalized displacement is successfully added, otherwise it returns a nonzero value.

The new generalized displacement must have a different name from all other generalized displacements. If the name is not unique, an error will be returned.

## VBA Example

Sub AddNewGDispl()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add generalized displacement
      ret = SapModel.GDispl.Add("GD1", 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetPoint](SetPoint.htm)



## ChangeName {Generalized Displacement}

*Source file: `SAP2000_API_Fuctions/Definitions/Generalized_Displacement/ChangeName_{Generalized_Displacement}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.GDispl.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a defined generalized displacement.

NewName

The new name for the generalized displacement.

## Remarks

The function returns zero if the new name is successfully applied, otherwise it returns a nonzero value.

The new generalized displacement name must be different from all other generalized displacement names. If the name is not unique, an error will be returned.

## VBA Example

Sub ChangeGDisplName()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add generalized displacement
      ret = SapModel.GDispl.Add("GD1", 1)

   'change generalized displacement name
      ret = SapModel.GDispl.ChangeName("GD1", "MyGD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## CountPoint

*Source file: `SAP2000_API_Fuctions/Definitions/Generalized_Displacement/CountPoint.htm`*

# CountPoint

## Syntax

SapObject.SapModel.GDispl.CountPoint

## VB6 Procedure

Function CountPoint(ByVal Name As String, ByRef Count As Long) As Long

## Parameters

Name

The name of an existing generalized displacement.

Count

The number of point objects included in the specified generalized displacement.

## Remarks

This function retrieves the total number of point objects included in a specified generalized displacement.

The function returns zero if the count is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub CountGDisplPoints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim SF() As Double
      Dim Count As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add generalized displacement
      ret = SapModel.GDispl.Add("GD1", 1)

   'add points to generalized displacement
      ReDim SF(5)
      SF(0) = 0.5
      ret = SapModel.GDispl.SetPoint("GD1", "3", SF)
      ret = SapModel.GDispl.SetPoint("GD1", "7", SF)

   'get number of points in generalized displacement
      ret = SapModel.GDispl.CountPoint("GD1", Count)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetPoint](GetPoint.htm)

[SetPoint](SetPoint.htm)



## Count {Generalized Displacement}

*Source file: `SAP2000_API_Fuctions/Definitions/Generalized_Displacement/Count_{Generalized_Displacement}.htm`*

# Count

## Syntax

SapObject.SapModel.GDispl.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None

## Remarks

This function returns the total number of generalized displacements defined in the model.

## VBA Example

Sub CountGDispls()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add generalized displacement
      ret = SapModel.GDispl.Add("GD1", 1)

   'return number of generalized displacements
      Count = SapModel.GDispl.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## DeletePoint

*Source file: `SAP2000_API_Fuctions/Definitions/Generalized_Displacement/DeletePoint.htm`*

# DeletePoint

## Syntax

SapObject.SapModel.GDispl.DeletePoint

## VB6 Procedure

Function DeletePoint(ByVal Name As String, ByVal PointName As String) As Long

## Parameters

Name

The name of an existing generalized displacement.

PointName

The name of a point object included in the generalized displacement that is to be deleted.

## Remarks

This function deletes one point object from a generalized displacement definition.

The function returns zero if the point is successfully deleted from the generalized displacement definition, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteGDisplPoint()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim SF() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add generalized displacement
      ret = SapModel.GDispl.Add("GD1", 1)

   'add points to generalized displacement
      ReDim SF(5)
      SF(0) = 0.5
      ret = SapModel.GDispl.SetPoint("GD1", "3", SF)
      ret = SapModel.GDispl.SetPoint("GD1", "7", SF)

   'delete point from generalized displacement
      ret = SapModel.GDispl.DeletePoint("GD1", "3")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetPoint](GetPoint.htm)

[SetPoint](SetPoint.htm)



## Delete {Generalized Displacement}

*Source file: `SAP2000_API_Fuctions/Definitions/Generalized_Displacement/Delete_{Generalized_Displacement}.htm`*

# Delete

## Syntax

SapObject.SapModel.GDispl.Delete

## VB6 Procedure

Function Delete(ByVal Name As String) As Long

## Parameters

Name

The name of an existing generalized displacement.

## Remarks

This function deletes the specified generalized displacement.

The function returns zero if the generalized displacement is successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteGDispl()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add generalized displacement
      ret = SapModel.GDispl.Add("GD1", 1)

   'delete generalized displacement
      ret = SapModel.GDispl.Delete("GD1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[Add](Add_{Generalized_Displacement}.htm)



## GetNameList {Generalized Displacement}

*Source file: `SAP2000_API_Fuctions/Definitions/Generalized_Displacement/GetNameList_{Generalized_Displacement}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.GDispl.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of generalized displacement names retrieved by the program.

MyName

This is a one-dimensional array of generalized displacement names. The MyName array is created as a dynamic, zero-based, array by the API user:

Dim MyName() as String

The array is dimensioned to (NumberNames – 1) inside the Sap2000 program, filled with the names, and returned to the API user.

## Remarks

This function retrieves the names of all defined generalized displacements.

The function returns zero if the names are successfully retrieved, otherwise it returns nonzero.

## VBA Example

Sub GetGDisplNames()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberNames As Long
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add generalized displacements
      ret = SapModel.GDispl.Add("GD1", 1)
      ret = SapModel.GDispl.Add("GD2", 2)

   'get generalized displacement names
      ret = SapModel.GDispl.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetPoint

*Source file: `SAP2000_API_Fuctions/Definitions/Generalized_Displacement/GetPoint.htm`*

# GetPoint

## Syntax

SapObject.SapModel.GDispl.GetPoint

## VB6 Procedure

Function GetPoint(ByVal Name As String, ByRef NumberItems As Long, ByRef PointName() As String, ByRef U1() As Double, ByRef U2() As Double, ByRef U3() As Double, ByRef R1() As Double, ByRef R2() As Double, ByRef R3() As Double) As Long

## Parameters

Name

The name of an existing generalized displacement.

NumberItems

The number of point objects included in the generalized displacement definition.

PointName

This is an array that includes the name of the point objects included in the generalized displacement definition.

U1, U2, U3, R1, R2, R3

These are arrays that include the unitless scale factors for each of the displacement degrees of freedom of the associated point objects that are included in the generalized displacement definition.

## Remarks

This function retrieves the point objects and their scale factors from a generalized displacement definition.

The function returns zero if the data is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetGDisplPointData()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim PointName() As String
      Dim U1() As Double
      Dim U2() As Double
      Dim U3() As Double
      Dim R1() As Double
      Dim R2() As Double
      Dim R3() As Double
      Dim SF() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add generalized displacement
      ret = SapModel.GDispl.Add("GD1", 1)

   'add points to generalized displacement
      ReDim SF(5)
      SF(0) = 0.5
      ret = SapModel.GDispl.SetPoint("GD1", "3", SF)
      ret = SapModel.GDispl.SetPoint("GD1", "7", SF)

   'get point data from generalized displacement
      ret = SapModel.GDispl.GetPoint("GD1", NumberItems, PointName, U1, U2, U3, R1, R2, R3)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetPoint](SetPoint.htm)



## GetTypeOAPI {Generalized Displacement}

*Source file: `SAP2000_API_Fuctions/Definitions/Generalized_Displacement/GetType_{Generalized_Displacement}.htm`*

# GetTypeOAPI

## Syntax

SapObject.SapModel.GDispl.GetTypeOAPI

## VB6 Procedure

Function GetTypeOAPI(ByVal Name As String, ByRef MyType As Long) As Long

## Parameters

Name

The name of an existing generalized displacement.

MyType

This is 1 or 2, indicating the generalized displacement type.

1 = Translational

2 = Rotational

## Remarks

This function retrieves the generalized displacement type.

The function returns zero if the type is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetGDisplType()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyType As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add generalized displacement
      ret = SapModel.GDispl.Add("GD1", 2)

   'get generalized displacement type
      ret = SapModel.GDispl.GetTypeOAPI("GD1", MyType)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Change function name to GetTypeOAPI in v17.0.0.

## See Also

[SetTypeOAPI](SetType_{Generalized_Displacement}.htm)



## SetPoint

*Source file: `SAP2000_API_Fuctions/Definitions/Generalized_Displacement/SetPoint.htm`*

# SetPoint

## Syntax

SapObject.SapModel.GDispl.SetPoint

## VB6 Procedure

Function SetPoint(ByVal Name As String, ByVal PointName As String, ByRef SF() As Double) As Long

## Parameters

Name

The name of an existing generalized displacement.

PointName

The name of a point object to be included in the generalized displacement definition.

SF

This is an array of six unitless scale factors for the point object displacement degrees of freedom.

SF(0) = U1 scale factor

SF(1) = U2 scale factor

SF(2) = U3 scale factor

SF(3) = R1 scale factor

SF(4) = R2 scale factor

SF(5) = R3 scale factor

## Remarks

This function adds a point object and its scale factors to a generalized displacement definition, or, if the point object already exists in the generalized displacement definition, it modifies the scale factors.

The function returns zero if the data is successfully added or modified, otherwise it returns a nonzero value.

## VBA Example

Sub SetGDisplPointData()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim SF() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add generalized displacement
      ret = SapModel.GDispl.Add("GD1", 1)

   'add point to generalized displacement
      ReDim SF(5)
      SF(0) = 0.5
      ret = SapModel.GDispl.SetPoint("GD1", "3", SF)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetPoint](GetPoint.htm)



## SetTypeOAPI {Generalized Displacement}

*Source file: `SAP2000_API_Fuctions/Definitions/Generalized_Displacement/SetType_{Generalized_Displacement}.htm`*

# SetTypeOAPI

## Syntax

SapObject.SapModel.GDispl.SetTypeOAPI

## VB6 Procedure

Function SetTypeOAPI(ByVal Name As String, ByVal MyType As Long) As Long

## Parameters

Name

The name of an existing generalized displacement.

MyType

This is 1 or 2, indicating the generalized displacement type.

1 = Translational

2 = Rotational

## Remarks

This function sets the generalized displacement type.

The function returns zero if the type is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetGDisplType()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add generalized displacement
         ret = SapModel.GDispl.Add("GD1", 2)

   'modify generalized displacement type
      ret = SapModel.GDispl.SetTypeOAPI("GD1", 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed function name to SetTypeOAPI in v17.0.0.

## See Also

[GetTypeOAPI](GetType_{Generalized_Displacement}.htm)

