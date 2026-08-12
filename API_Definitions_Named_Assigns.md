# API Definitions Named Assigns

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Definitions/Named_Assigns

---



## ChangeName {Area Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Area_Modifiers/ChangeName_{Area_Modifiers}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.NamedAssign.ModifierArea.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a defined area stiffness modifier.

NewName

The new name for the area stiffness modifier.

## Remarks

This function changes the name of an existing area stiffness modifier.

The function returns zero if the new name is successfully applied; otherwise it returns a nonzero value.

## VBA Example

Sub ChangeAreaStiffnessModifierName()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'add new stiffness modifier
      ReDim Value(9)
      For i = 0 To 9
         Value(i) = 1
      Next i
      Value(5) = 100
      ret = SapModel.NamedAssign.ModifierArea.SetModifiers("AMOD1", Value)

   'change name of stiffness modifier
      ret = SapModel.NamedAssign.ModifierArea.ChangeName("AMOD1", "MyModifier")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## Count {Area Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Area_Modifiers/Count_{Area_Modifiers}.htm`*

# Count

## Syntax

SapObject.SapModel.NamedAssign.ModifierArea.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None

## Remarks

This function returns the total number of defined area stiffness modifiers in the model.

## VBA Example

Sub CountAreaStiffnessModifiers()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim i As Long
      Dim Value() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'add new stiffness modifier
      ReDim Value(9)
      For i = 0 To 9
         Value(i) = 1
      Next i
      Value(5) = 2
      ret = SapModel.NamedAssign.ModifierArea.SetModifiers("AMOD1", Value)
      Value(5) = 1.5
      ret = SapModel.NamedAssign.ModifierArea.SetModifiers("AMOD2", Value)

   'return number of defined stiffness modifiers
      Count = SapModel.NamedAssign.ModifierArea.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## Delete {Area Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Area_Modifiers/Delete_{Area_Modifiers}.htm`*

# Delete

## Syntax

SapObject.SapModel.NamedAssign.ModifierArea.Delete

## VB6 Procedure

Function Delete(ByVal Name As String) As Long

## Parameters

Name

The name of an existing area stiffness modifier.

## Remarks

The function deletes a specified area stiffness modifier.

The function returns zero if the modifier is successfully deleted; otherwise it returns a nonzero value. It returns an error if the specified modifier can not be deleted; for example, if it is currently used by a staged construction load case.

## VBA Example

Sub DeleteAreaStiffnessModifier()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'add new stiffness modifier
      ReDim Value(9)
      For i = 0 To 9
         Value(i) = 1
      Next i
      Value(5) = 2
      ret = SapModel.NamedAssign.ModifierArea.SetModifiers("AMOD1", Value)
      Value(5) = 1.5
      ret = SapModel.NamedAssign.ModifierArea.SetModifiers("AMOD2", Value)

   'delete stiffness modifier
      ret = SapModel.NamedAssign.ModifierArea.Delete("AMOD1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## GetModifiers {Area Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Area_Modifiers/GetModifiers_{Area_Modifiers}.htm`*

# GetModifiers

## Syntax

SapObject.SapModel.NamedAssign.ModifierArea.GetModifiers

## VB6 Procedure

Function GetModifiers(ByVal Name As String, ByRef Value() As Double) As Long

## Parameters

Name

The name of an existing area stiffness modifier.

Value

This is an array of ten unitless modifiers.

Value(0) = Membrane f11 modifier

Value(1) = Membrane f22 modifier

Value(2) = Membrane f12 modifier

Value(3) = Bending m11 modifier

Value(4) = Bending m22 modifier

Value(5) = Bending m12 modifier

Value(6) = Shear v13 modifier

Value(7) = Shear v23 modifier

Value(8) = Mass modifier

Value(9) = Weight modifier

## Remarks

This function retrieves the modifier assignments for an area stiffness modifier. The default value for all modifier values is one.

The function returns zero if the modifier assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaPropModifierValues()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'define modifiers
      ReDim Value(9)
      For i = 0 To 9
         Value(i) = 1
      Next i
      Value(5) = 2
      ret = SapModel.NamedAssign.ModifierArea.SetModifiers("AMOD1", Value)

   'get modifier values
      ReDim Value(9)
      ret = SapModel.NamedAssign.ModifierArea.GetModifiers("AMOD1", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetModifiers](SetModifiers_{Area_Modifiers}.htm)



## GetNameList {Area Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Area_Modifiers/GetNameList_{Area_Modifiers}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.NamedAssign.ModifierArea.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of area stiffness modifier names retrieved by the program.

MyName

This is a one-dimensional array of area stiffness modifier names. The MyName array is created as a dynamic, zero-based array by the API user:

Dim MyName() as String

The array is dimensioned to (NumberNames - 1) inside the SAP2000 program, filled with the names, and returned to the API user.

## Remarks

This function retrieves the names of all defined area stiffness modifiers.

The function returns zero if the names are successfully retrieved; otherwise it returns nonzero values.

## VBA Example

Sub GetAreaStiffnessModifierNames()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'add new stiffness modifier
      ReDim Value(9)
      For i = 0 To 9
         Value(i) = 1
      Next i
      Value(5) = 2
      ret = SapModel.NamedAssign.ModifierArea.SetModifiers("AMOD1", Value)
      Value(5) = 1.5
      ret = SapModel.NamedAssign.ModifierArea.SetModifiers("AMOD2", Value)

   'get area stiffness modifier names
      ret = SapModel.NamedAssign.ModifierArea.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## SetModifiers {Area Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Area_Modifiers/SetModifiers_{Area_Modifiers}.htm`*

# SetModifiers

## Syntax

SapObject.SapModel.NamedAssign.ModifierArea.SetModifiers

## VB6 Procedure

Function SetModifiers(ByVal Name As String, ByRef Value() As Double) As Long

## Parameters

Name

The name of a new or existing area stiffness modifier.

Value

This is an array of ten unitless modifiers.

Value(0) = Membrane f11 modifier

Value(1) = Membrane f22 modifier

Value(2) = Membrane f12 modifier

Value(3) = Bending m11 modifier

Value(4) = Bending m22 modifier

Value(5) = Bending m12 modifier

Value(6) = Shear v13 modifier

Value(7) = Shear v23 modifier

Value(8) = Mass modifier

Value(9) = Weight modifier

## Remarks

This function defines a named area stiffness modifier. The default value for all modifier values is one.

The function returns zero if the modifier is successfully defined; otherwise it returns a nonzero value.

## VBA Example

Sub DefineAreaStiffnessModifiers()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'define modifiers
      ReDim Value(9)
      For i = 0 To 9
         Value(i) = 1
      Next i
      Value(5) = 2
      ret = SapModel.NamedAssign.ModifierArea.SetModifiers("AMOD1", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[GetModifiers](GetModifiers_{Area_Modifiers}.htm)



## ChangeName {Cable Modifers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Cable_Modifiers/ChangeName_{Cable_Modifers}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.NamedAssign.ModifierCable.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a defined cable property modifier.

NewName

The new name for the cable property modifier.

## Remarks

This function changes the name of an existing cable property modifier.

The function returns zero if the new name is successfully applied; otherwise it returns a nonzero value.

## VBA Example

Sub ChangeCablePropModifierName()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

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

   'add new property modifier
      ReDim Value(2)
      For i = 0 To 2
         Value(i) = 1
      Next i
      Value(1) = 2
      ret = SapModel.NamedAssign.ModifierCable.SetModifiers("CMOD1", Value)

   'change name of property modifier
      ret = SapModel.NamedAssign.ModifierCable.ChangeName("CMOD1", "MyModifier")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## Count {Cable Modifers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Cable_Modifiers/Count_{Cable_Modifers}.htm`*

# Count

## Syntax

SapObject.SapModel.NamedAssign.ModifierCable.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None

## Remarks

This function returns the total number of defined cable property modifiers in the model.

## VBA Example

Sub CountCablePropModifiers()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim i As Long
      Dim Value() As Double

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

   'add new property modifier
      ReDim Value(2)
      For i = 0 To 2
         Value(i) = 1
      Next i
      Value(1) = 2
      ret = SapModel.NamedAssign.ModifierCable.SetModifiers("CMOD1", Value)
      Value(1) = 1.5
      ret = SapModel.NamedAssign.ModifierCable.SetModifiers("CMOD2", Value)

   'return number of defined property modifiers
      Count = SapModel.NamedAssign.ModifierCable.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## Delete {Cable Modifers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Cable_Modifiers/Delete_{Cable_Modifers}.htm`*

# Delete

## Syntax

SapObject.SapModel.NamedAssign.ModifierCable.Delete

## VB6 Procedure

Function Delete(ByVal Name As String) As Long

## Parameters

Name

The name of an existing cable property modifier.

## Remarks

The function deletes a specified cable property modifier.

The function returns zero if the modifier is successfully deleted; otherwise it returns a nonzero value. It returns an error if the specified modifier can not be deleted, for example, if it is currently used by a staged construction load case.

## VBA Example

Sub DeleteCablePropModifier()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

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

   'add new property modifier
      ReDim Value(2)
      For i = 0 To 2
         Value(i) = 1
      Next i
      Value(1) = 2
      ret = SapModel.NamedAssign.ModifierCable.SetModifiers("CMOD1", Value)
      Value(1) = 1.5
      ret = SapModel.NamedAssign.ModifierCable.SetModifiers("CMOD2", Value)

   'delete property modifier
      ret = SapModel.NamedAssign.ModifierCable.Delete("CMOD1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## GetModifiers {Cable Modifers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Cable_Modifiers/GetModifiers_{Cable_Modifers}.htm`*

# GetModifiers

## Syntax

SapObject.SapModel.NamedAssign.ModifierCable.GetModifiers

## VB6 Procedure

Function GetModifiers(ByVal Name As String, ByRef Value() As Double) As Long

## Parameters

Name

The name of an existing cable property modifier.

Value

This is an array of three unitless modifiers.

Value(0) = Cross sectional area modifier

Value(1) = Mass modifier

Value(2) = Weight modifier

## Remarks

This function retrieves the modifier assignments for a cable property modifier. The default value for all modifier values is one.

The function returns zero if the modifier assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetCablePropModifierValues()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

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

   'define modifiers
      ReDim Value(2)
      For i = 0 To 2
         Value(i) = 1
      Next i
      Value(1) = 100
      ret = SapModel.NamedAssign.ModifierCable.SetModifiers("CMOD1", Value)

   'get modifier values
      ReDim Value(2)
      ret = SapModel.NamedAssign.ModifierCable.GetModifiers("CMOD1", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetModifiers](SetModifiers_{Cable_Modifers}.htm)



## GetNameList {Cable Modifers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Cable_Modifiers/GetNameList_{Cable_Modifers}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.NamedAssign.ModifierCable.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of cable property modifier names retrieved by the program.

MyName

This is a one-dimensional array of cable property modifier names. The MyName array is created as a dynamic, zero-based array by the API user:

Dim MyName() as String

The array is dimensioned to (NumberNames - 1) inside the SAP2000 program, filled with the names, and returned to the API user.

## Remarks

This function retrieves the names of all defined cable property modifiers.

The function returns zero if the names are successfully retrieved; otherwise it returns nonzero.

## VBA Example

Sub GetCablePropModifierNames()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add new property modifier
      ReDim Value(2)
      For i = 0 To 2
         Value(i) = 1
      Next i
      Value(1) = 2
      ret = SapModel.NamedAssign.ModifierCable.SetModifiers("CMOD1", Value)
      Value(1) = 1.5
      ret = SapModel.NamedAssign.ModifierCable.SetModifiers("CMOD2", Value)

   'get cable property modifier names
      ret = SapModel.NamedAssign.ModifierCable.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## SetModifiers {Cable Modifers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Cable_Modifiers/SetModifiers_{Cable_Modifers}.htm`*

# SetModifiers

## Syntax

SapObject.SapModel.NamedAssign.ModifierCable.SetModifiers

## VB6 Procedure

Function SetModifiers(ByVal Name As String, ByRef Value() As Double) As Long

## Parameters

Name

The name of a new or existing cable property modifier.

Value

This is an array of three unitless modifiers.

Value(0) = Cross sectional area modifier

Value(1) = Mass modifier

Value(2) = Weight modifier

## Remarks

This function defines a named cable property modifier. The default value for all modifier values is one.

The function returns zero if the modifier is successfully defined; otherwise it returns a nonzero value.

## VBA Example

Sub DefineCablePropModifiers()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

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

   'define modifiers
      ReDim Value(2)
      For i = 0 To 2
         Value(i) = 1
      Next i
      Value(1) = 2
      ret = SapModel.NamedAssign.ModifierCable.SetModifiers("CMOD1", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[GetModifiers](GetModifiers_{Cable_Modifers}.htm)



## ChangeName {Frame Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Modifiers/ChangeName_{Frame_Modifiers}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.NamedAssign.ModifierFrame.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a defined frame property modifier.

NewName

The new name for the frame property modifier.

## Remarks

This function changes the name of an existing frame property modifier.

The function returns zero if the new name is successfully applied; otherwise it returns a nonzero value.

## VBA Example

Sub ChangeFramePropModifierName()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

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

   'add new property modifier
      ReDim Value(7)
      For i = 0 To 7
         Value(i) = 1
      Next i
      Value(5) = 100
      ret = SapModel.NamedAssign.ModifierFrame.SetModifiers("FMOD1", Value)

   'change name of property modifier
      ret = SapModel.NamedAssign.ModifierFrame.ChangeName("FMOD1", "MyModifier")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## Count {Frame Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Modifiers/Count_{Frame_Modifiers}.htm`*

# Count

## Syntax

SapObject.SapModel.NamedAssign.ModifierFrame.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None

## Remarks

This function returns the total number of defined frame property modifiers in the model.

## VBA Example

Sub CountFramePropModifiers()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim i As Long
      Dim Value() As Double

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

   'add new property modifier
      ReDim Value(7)
      For i = 0 To 7
         Value(i) = 1
      Next i
      Value(5) = 100
      ret = SapModel.NamedAssign.ModifierFrame.SetModifiers("FMOD1", Value)
      Value(5) = 10
      ret = SapModel.NamedAssign.ModifierFrame.SetModifiers("FMOD2", Value)

   'return number of defined property modifiers
      Count = SapModel.NamedAssign.ModifierFrame.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## Delete {Frame Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Modifiers/Delete_{Frame_Modifiers}.htm`*

# Delete

## Syntax

SapObject.SapModel.NamedAssign.ModifierFrame.Delete

## VB6 Procedure

Function Delete(ByVal Name As String) As Long

## Parameters

Name

The name of an existing frame property modifier.

## Remarks

The function deletes a specified frame property modifier.

The function returns zero if the modifier is successfully deleted; otherwise it returns a nonzero value. It returns an error if the specified modifier can not be deleted; for example, if it is currently used by a staged construction load case.

## VBA Example

Sub DeleteFramePropModifier()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

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

   'add new property modifier
      ReDim Value(7)
      For i = 0 To 7
         Value(i) = 1
      Next i
      Value(5) = 100
      ret = SapModel.NamedAssign.ModifierFrame.SetModifiers("FMOD1", Value)
      Value(5) = 10
      ret = SapModel.NamedAssign.ModifierFrame.SetModifiers("FMOD2", Value)

   'delete property modifier
      ret = SapModel.NamedAssign.ModifierFrame.Delete("FMOD1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## GetModifiers {Frame Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Modifiers/GetModifiers_{Frame_Modifiers}.htm`*

# GetModifiers

## Syntax

SapObject.SapModel.NamedAssign.ModifierFrame.GetModifiers

## VB6 Procedure

Function GetModifiers(ByVal Name As String, ByRef Value() As Double) As Long

## Parameters

Name

The name of an existing frame property modifier.

Value

This is an array of eight unitless modifiers.

Value(0) = Cross sectional area modifier

Value(1) = Shear area in local 2 direction modifier

Value(2) = Shear area in local 3 direction modifier

Value(3) = Torsional constant modifier

Value(4) = Moment of inertia about local 2 axis modifier

Value(5) = Moment of inertia about local 3 axis modifier

Value(6) = Mass modifier

Value(7) = Weight modifier

## Remarks

This function retrieves the modifier assignments for a frame property modifier. The default value for all modifier values is one.

The function returns zero if the modifier assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePropModifierValues()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

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

   'define modifiers
      ReDim Value(7)
      For i = 0 To 7
         Value(i) = 1
      Next i
      Value(5) = 100
      ret = SapModel.NamedAssign.ModifierFrame.SetModifiers("FMOD1", Value)

   'get modifier values
      ReDim Value(7)
      ret = SapModel.NamedAssign.ModifierFrame.GetModifiers("FMOD1", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetModifiers](SetModifiers_{Frame_Modifiers}.htm)



## GetNameList {Frame Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Modifiers/GetNameList_{Frame_Modifiers}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.NamedAssign.ModifierFrame.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of frame property modifier names retrieved by the program.

MyName

This is a one-dimensional array of frame property modifier names. The MyName array is created as a dynamic, zero-based, array by the API user:

Dim MyName() as String

The array is dimensioned to (NumberNames - 1) inside the SAP2000 program, filled with the names, and returned to the API user.

## Remarks

This function retrieves the names of all defined frame property modifiers.

The function returns zero if the names are successfully retrieved; otherwise it returns nonzero.

## VBA Example

Sub GetFramePropModifierNames()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add new property modifier
      ReDim Value(7)
      For i = 0 To 7
         Value(i) = 1
      Next i
      Value(5) = 100
      ret = SapModel.NamedAssign.ModifierFrame.SetModifiers("FMOD1", Value)
      Value(5) = 10
      ret = SapModel.NamedAssign.ModifierFrame.SetModifiers("FMOD2", Value)

   'get frame property modifier names
      ret = SapModel.NamedAssign.ModifierFrame.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## SetModifiers {Frame Modifiers}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Modifiers/SetModifiers_{Frame_Modifiers}.htm`*

# SetModifiers

## Syntax

SapObject.SapModel.NamedAssign.ModifierFrame.SetModifiers

## VB6 Procedure

Function SetModifiers(ByVal Name As String, ByRef Value() As Double) As Long

## Parameters

Name

The name of a new or existing frame property modifier.

Value

This is an array of eight unitless modifiers.

Value(0) = Cross sectional area modifier

Value(1) = Shear area in local 2 direction modifier

Value(2) = Shear area in local 3 direction modifier

Value(3) = Torsional constant modifier

Value(4) = Moment of inertia about local 2 axis modifier

Value(5) = Moment of inertia about local 3 axis modifier

Value(6) = Mass modifier

Value(7) = Weight modifier

## Remarks

This function defines a named frame property modifier. The default value for all modifier values is one.

The function returns zero if the modifier is successfully defined; otherwise it returns a nonzero value.

## VBA Example

Sub DefineFramePropModifiers()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double

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

   'define modifiers
      ReDim Value(7)
      For i = 0 To 7
         Value(i) = 1
      Next i
      Value(5) = 100
      ret = SapModel.NamedAssign.ModifierFrame.SetModifiers("FMOD1", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[GetModifiers](GetModifiers_{Frame_Modifiers}.htm)



## ChangeName {Frame Releases}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Releases/ChangeName_{Frame_Releases}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.NamedAssign.ReleaseFrame.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a defined frame end release.

NewName

The new name for the frame end release.

## Remarks

This function changes the name of an existing frame end release.

The function returns zero if the new name is successfully applied; otherwise it returns a nonzero value.

## VBA Example

Sub ChangeFrameEndReleaseName()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ii() As Boolean
      Dim jj() As Boolean
      Dim StartValue() As Double
      Dim EndValue() As Double

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

   'add new end release
      ReDim ii(5)
      ReDim jj(5)
      ReDim StartValue(5)
      ReDim EndValue(5)
      ii(0) = True
      StartValue(0) = 10
      ret = SapModel.NamedAssign.ReleaseFrame.SetReleases("FREL1", ii, jj, StartValue, EndValue)

   'change name of end release
      ret = SapModel.NamedAssign.ReleaseFrame.ChangeName("FREL1", "MyRelease")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## Count {Frame Releases}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Releases/Count_{Frame_Releases}.htm`*

# Count

## Syntax

SapObject.SapModel.NamedAssign.ReleaseFrame.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None

## Remarks

This function returns the total number of defined frame end releases in the model.

## VBA Example

Sub CountFrameEndReleases()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim ii() As Boolean
      Dim jj() As Boolean
      Dim StartValue() As Double
      Dim EndValue() As Double

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

   'add new end release
      ReDim ii(5)
      ReDim jj(5)
      ReDim StartValue(5)
      ReDim EndValue(5)
      ii(0) = True
      StartValue(0) = 10
      ret = SapModel.NamedAssign.ReleaseFrame.SetReleases("FREL1", ii, jj, StartValue, EndValue)
      ii(0) = False
      StartValue(0) = 0
      ii(5) = True
      jj(5) = True
      ret = SapModel.NamedAssign.ReleaseFrame.SetReleases("FREL2", ii, jj, StartValue, EndValue)

   'return number of defined end releases
      Count = SapModel.NamedAssign.ReleaseFrame.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## Delete {Frame Releases}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Releases/Delete_{Frame_Releases}.htm`*

# Delete

## Syntax

SapObject.SapModel.NamedAssign.ReleaseFrame.Delete

## VB6 Procedure

Function Delete(ByVal Name As String) As Long

## Parameters

Name

The name of an existing frame end release.

## Remarks

The function deletes a specified frame end release.

The function returns zero if the end release is successfully deleted; otherwise it returns a nonzero value. It returns an error if the specified end release can not be deleted; for example, if it is currently used by a staged construction load case.

## VBA Example

Sub DeleteFrameEndRelease()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ii() As Boolean
      Dim jj() As Boolean
      Dim StartValue() As Double
      Dim EndValue() As Double

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

   'add new end release
      ReDim ii(5)
      ReDim jj(5)
      ReDim StartValue(5)
      ReDim EndValue(5)
      ii(0) = True
      StartValue(0) = 10
      ret = SapModel.NamedAssign.ReleaseFrame.SetReleases("FREL1", ii, jj, StartValue, EndValue)
      ii(0) = False
      StartValue(0) = 0
      ii(5) = True
      jj(5) = True
      ret = SapModel.NamedAssign.ReleaseFrame.SetReleases("FREL2", ii, jj, StartValue, EndValue)

   'delete end release
      ret = SapModel.NamedAssign.ReleaseFrame.Delete("FREL1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## GetNameList {Frame Releases}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Releases/GetNameList_{Frame_Releases}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.NamedAssign.ReleaseFrame.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of frame end release names retrieved by the program.

MyName

This is a one-dimensional array of frame end release names. The MyName array is created as a dynamic, zero-based array by the API user:

Dim MyName() as String

The array is dimensioned to (NumberNames - 1) inside the SAP2000 program, filled with the names, and returned to the API user.

## Remarks

This function retrieves the names of all defined frame end releases.

The function returns zero if the names are successfully retrieved; otherwise it returns nonzero values.

## VBA Example

Sub GetFrameEndReleaseNames()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ii() As Boolean
      Dim jj() As Boolean
      Dim StartValue() As Double
      Dim EndValue() As Double
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add new end release
      ReDim ii(5)
      ReDim jj(5)
      ReDim StartValue(5)
      ReDim EndValue(5)
      ii(0) = True
      StartValue(0) = 10
      ret = SapModel.NamedAssign.ReleaseFrame.SetReleases("FREL1", ii, jj, StartValue, EndValue)
      ii(0) = False
      StartValue(0) = 0
      ii(5) = True
      jj(5) = True
      ret = SapModel.NamedAssign.ReleaseFrame.SetReleases("FREL2", ii, jj, StartValue, EndValue)

   'get frame end release names
      ret = SapModel.NamedAssign.ReleaseFrame.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## GetReleases {Frame Releases}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Releases/GetReleases_{Frame_Releases}.htm`*

# GetReleases

## Syntax

SapObject.SapModel.NamedAssign.ReleaseFrame.GetReleases

## VB6 Procedure

Function GetReleases(ByVal Name As String, ByRef ii() As Boolean, ByRef jj() As Boolean, ByRef StartValue() As Double, ByRef EndValue() As Double) As Long

## Parameters

Name

The name of an existing frame end release.

ii, jj

These are arrays of six booleans indicating the I-End and J-End releases.

ii(0) and jj(0) = U1 release

ii(1) and jj(1) = U2 release

ii(2) and jj(2) = U3 release

ii(3) and jj(3) = R1 release

ii(4) and jj(4) = R2 release

ii(5) and jj(5) = R3 release

StartValue, EndValue

These are arrays of six values indicating the I-End and J-End partial fixity springs.

StartValue(0) and EndValue(0) = U1 partial fixity [F/L]

StartValue(1) and EndValue(1) = U2 partial fixity [F/L]

StartValue(2) and EndValue(2) = U3 partial fixity [F/L]

StartValue(3) and EndValue(3) = R1 partial fixity [FL/rad]

StartValue(4) and EndValue(4) = R2 partial fixity [FL/rad]

StartValue(5) and EndValue(5) = R3 partial fixity [FL/rad]

## Remarks

This function retrieves the release assignments for a frame end release.

The function returns zero if the release assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameEndReleaseValues()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim ii() As Boolean
      Dim jj() As Boolean
      Dim StartValue() As Double
      Dim EndValue() As Double

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

   'define releases
      ReDim ii(5)
      ReDim jj(5)
      ReDim StartValue(5)
      ReDim EndValue(5)
      ii(0) = True
      StartValue(0) = 10
      ret = SapModel.NamedAssign.ReleaseFrame.SetReleases("FREL1", ii, jj, StartValue, EndValue)

   'clear variables
      For i = 0 to 5
         ii(i) = False
         jj(i) = False
         StartValue(i) = 0
         EndValue(i) = 0
      Next i

   'get release values
      ret = SapModel.NamedAssign.ReleaseFrame.GetReleases("FREL1", ii, jj, StartValue, EndValue)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetReleases](SetReleases_{Frame_Releases}.htm)



## SetReleases {Frame Releases}

*Source file: `SAP2000_API_Fuctions/Definitions/Named_Assigns/Frame_Releases/SetReleases_{Frame_Releases}.htm`*

# SetReleases

## Syntax

SapObject.SapModel.NamedAssign.ReleaseFrame.SetReleases

## VB6 Procedure

Function SetReleases(ByVal Name As String, ByRef ii() As Boolean, ByRef jj() As Boolean, ByRef StartValue() As Double, ByRef EndValue() As Double) As Long

## Parameters

Name

The name of a new or existing frame end release.

ii, jj

These are arrays of six booleans indicating the I-End and J-End releases.

ii(0) and jj(0) = U1 release

ii(1) and jj(1) = U2 release

ii(2) and jj(2) = U3 release

ii(3) and jj(3) = R1 release

ii(4) and jj(4) = R2 release

ii(5) and jj(5) = R3 release

StartValue, EndValue

These are arrays of six values indicating the I-End and J-End partial fixity springs.

StartValue(0) and EndValue(0) = U1 partial fixity [F/L]

StartValue(1) and EndValue(1) = U2 partial fixity [F/L]

StartValue(2) and EndValue(2) = U3 partial fixity [F/L]

StartValue(3) and EndValue(3) = R1 partial fixity [FL/rad]

StartValue(4) and EndValue(4) = R2 partial fixity [FL/rad]

StartValue(5) and EndValue(5) = R3 partial fixity [FL/rad]

## Remarks

This function defines a named frame end release.

The function returns zero if the release is successfully defined; otherwise it returns a nonzero value.

## VBA Example

Sub DefineFrameEndReleases()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ii() As Boolean
      Dim jj() As Boolean
      Dim StartValue() As Double
      Dim EndValue() As Double

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

   'define releases
      ReDim ii(5)
      ReDim jj(5)
      ReDim StartValue(5)
      ReDim EndValue(5)
      ii(0) = True
      StartValue(0) = 10
      ret = SapModel.NamedAssign.ReleaseFrame.SetReleases("FREL1", ii, jj, StartValue, EndValue)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[GetReleases](GetReleases_{Frame_Releases}.htm)

