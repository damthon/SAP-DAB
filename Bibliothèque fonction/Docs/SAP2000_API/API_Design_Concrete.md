# API Design Concrete

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Design/Concrete

---



## GetOverwrite {Concrete AASHTO 07}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_07/GetOverwrite_{Concrete_AASHTO_07}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_Concrete\_07.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 11, inclusive, indicating the overwrite item considered.

1 = Live load reduction factor

2 = Unbraced length ratio, Major

3 = Unbraced length ratio, Minor

4 = Effective length factor, K Major

5 = Effective length factor, K Minor

6 = Moment coefficient, Cm Major

7 = Moment coefficient, Cm Minor

8 = Nonsway moment factor, Db Major

9 = Nonsway moment factor, Db Minor

10 = Sway moment factor, Ds Major

11 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Live load reduction factor

Value >= 0; 0 means use program determined value.

2 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

4 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

6 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

8 = Nonsway moment factor, Db Major

Value >= 0; 0 means use program determined value.

9 = Nonsway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

10 = Sway moment factor, Ds Major

  Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Minor

  Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemAASHTO\_Concrete\_07()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO Concrete 07")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.AASHTO\_Concrete\_07.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.1.0.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_AASHTO_07}.htm)



## GetPreference {Concrete AASHTO 07}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_07/GetPreference_{Concrete_AASHTO_07}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_Concrete\_07.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 7, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic Zone

5 = Pattern live load factor

6 = Utilization factor limit

7 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and divisible by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic Zone

  0 = Zone 0

  1 = Zone 1

  2 = Zone 2

  3 = Zone 3

  4 = Zone 4

5 = Pattern live load factor

Value >= 0

6 = Utilization factor limit

Value > 0

7 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItem AASHTO\_Concrete\_07()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO Concrete 07")

   'get preference item
      ret = SapModel.DesignConcrete.AASHTO\_Concrete\_07.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.1.0.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_AASHTO_07}.htm)



## SetOverwrite {Concrete AASHTO 07}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_07/SetOverwrite_{Concrete_AASHTO_07}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_Concrete\_07.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 11, inclusive, indicating the overwrite item considered.

1 = Live load reduction factor

2 = Unbraced length ratio, Major

3 = Unbraced length ratio, Minor

4 = Effective length factor, K Major

5 = Effective length factor, K Minor

6 = Moment coefficient, Cm Major

7 = Moment coefficient, Cm Minor

8 = Nonsway moment factor, Db Major

9 = Nonsway moment factor, Db Minor

10 = Sway moment factor, Ds Major

11 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Live load reduction factor

Value >= 0; 0 means use program determined value.

2 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

4 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

6 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

8 = Nonsway moment factor, Db Major

Value >= 0; 0 means use program determined value.

9 = Nonsway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

10 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItem AASHTO\_Concrete\_07 ()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO Concrete 07")

   'set overwrite item
      ret = SapModel.DesignConcrete.AASHTO\_Concrete\_07.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.1.0.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_AASHTO_07}.htm)



## SetPreference {Concrete AASHTO 07}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_07/SetPreference_{Concrete_AASHTO_07}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_Concrete\_07.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 7, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic Zone

5 = Pattern live load factor

6 = Utilization factor limit

7 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and divisible by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic Zone

 0 = Zone 0

 1 = Zone 1

 2 = Zone 2

 3 = Zone 3

 4 = Zone 4

5 = Pattern live load factor

Value >= 0

6 = Utilization factor limit

Value > 0

7 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItem AASHTO\_Concrete\_07()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO Concrete 07")

   'set preference item
      ret = SapModel.DesignConcrete.AASHTO\_Concrete\_07.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.1.0.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_AASHTO_07}.htm)



## GetOverwrite {Concrete AASHTO_LRFD_2012}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_LRFD_2012/GetOverwrite_{Concrete_AASHTO_LRFD_2012}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_LRFD\_2012.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 11, inclusive, indicating the overwrite item considered.

1 = Live load reduction factor

2 = Unbraced length ratio, Major

3 = Unbraced length ratio, Minor

4 = Effective length factor, K Major

5 = Effective length factor, K Minor

6 = Moment coefficient, Cm Major

7 = Moment coefficient, Cm Minor

8 = Nonsway moment factor, Db Major

9 = Nonsway moment factor, Db Minor

10 = Sway moment factor, Ds Major

11 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Live load reduction factor

Value >= 0; 0 means use program determined value.

2 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

4 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

6 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

8 = Nonsway moment factor, Db Major

Value >= 0; 0 means use program determined value.

9 = Nonsway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

10 = Sway moment factor, Ds Major

  Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Minor

  Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemAASHTO\_Concrete\_LRFD\_2012()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO LRFD 2012")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.AASHTO\_LRFD\_2012.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 17.3.0.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_AASHTO_LRFD_2012}.htm)



## GetPreference {Concrete AASHTO_LRFD_2012}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_LRFD_2012/GetPreference_{Concrete_AASHTO_LRFD_2012}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_LRFD\_2012.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 7, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic Zone

5 = Pattern live load factor

6 = Utilization factor limit

7 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and divisible by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic Zone

  0 = Zone 0

  1 = Zone 1

  2 = Zone 2

  3 = Zone 3

  4 = Zone 4

5 = Pattern live load factor

Value >= 0

6 = Utilization factor limit

Value > 0

7 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItem AASHTO\_LRFD\_2012()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO LRFD 2012")

   'get preference item
      ret = SapModel.DesignConcrete.AASHTO\_LRFD\_2012.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 17.3.0.

## See Also

[SetPreference](SetPreference_{Concrete_AASHTO_LRFD_2012}.htm)



## SetOverwrite {Concrete AASHTO_LRFD_2012}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_LRFD_2012/SetOverwrite_{Concrete_AASHTO_LRFD_2012}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_LRFD\_2012.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 11, inclusive, indicating the overwrite item considered.

1 = Live load reduction factor

2 = Unbraced length ratio, Major

3 = Unbraced length ratio, Minor

4 = Effective length factor, K Major

5 = Effective length factor, K Minor

6 = Moment coefficient, Cm Major

7 = Moment coefficient, Cm Minor

8 = Nonsway moment factor, Db Major

9 = Nonsway moment factor, Db Minor

10 = Sway moment factor, Ds Major

11 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Live load reduction factor

Value >= 0; 0 means use program determined value.

2 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

4 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

6 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

8 = Nonsway moment factor, Db Major

Value >= 0; 0 means use program determined value.

9 = Nonsway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

10 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItem AASHTO\_LRFD\_2012 ()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO LRFD 2012")

   'set overwrite item
      ret = SapModel.DesignConcrete.AASHTO\_LRFD\_2012.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 17.3.0.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_AASHTO_LRFD_2012}.htm)



## SetPreference {Concrete AASHTO_LRFD_2012}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_LRFD_2012/SetPreference_{Concrete_AASHTO_LRFD_2012}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_LRFD\_2012.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 7, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic Zone

5 = Pattern live load factor

6 = Utilization factor limit

7 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and divisible by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic Zone

 0 = Zone 0

 1 = Zone 1

 2 = Zone 2

 3 = Zone 3

 4 = Zone 4

5 = Pattern live load factor

Value >= 0

6 = Utilization factor limit

Value > 0

7 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItem AASHTO\_LRFD\_2012()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO LRFD 2012")

   'set preference item
      ret = SapModel.DesignConcrete.AASHTO\_LRFD\_2012.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 17.3.0.

## See Also

[GetPreference](GetPreference_{Concrete_AASHTO_LRFD_2012}.htm)



## GetOverwrite {Concrete AASHTO_LRFD_2014}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_LRFD_2014/GetOverwrite_{Concrete_AASHTO_LRFD_2014}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_LRFD\_2014.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 11, inclusive, indicating the overwrite item considered.

1 = Live load reduction factor

2 = Unbraced length ratio, Major

3 = Unbraced length ratio, Minor

4 = Effective length factor, K Major

5 = Effective length factor, K Minor

6 = Moment coefficient, Cm Major

7 = Moment coefficient, Cm Minor

8 = Nonsway moment factor, Db Major

9 = Nonsway moment factor, Db Minor

10 = Sway moment factor, Ds Major

11 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Live load reduction factor

Value >= 0; 0 means use program determined value.

2 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

4 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

6 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

8 = Nonsway moment factor, Db Major

Value >= 0; 0 means use program determined value.

9 = Nonsway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

10 = Sway moment factor, Ds Major

  Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Minor

  Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemAASHTO\_Concrete\_LRFD\_2014()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO LRFD 2014")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.AASHTO\_LRFD\_2014.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 17.3.0.

## See Also

SetOverwrite



## GetPreference {Concrete AASHTO_LRFD_2014}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_LRFD_2014/GetPreference_{Concrete_AASHTO_LRFD_2014}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_LRFD\_2014.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 7, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic Zone

5 = Pattern live load factor

6 = Utilization factor limit

7 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and divisible by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic Zone

  0 = Zone 0

  1 = Zone 1

  2 = Zone 2

  3 = Zone 3

  4 = Zone 4

5 = Pattern live load factor

Value >= 0

6 = Utilization factor limit

Value > 0

7 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItem AASHTO\_LRFD\_2014()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO LRFD 2014")

   'get preference item
      ret = SapModel.DesignConcrete.AASHTO\_LRFD\_2014.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 17.3.0.

## See Also

[SetPreference](SetPreference_{Concrete_AASHTO_LRFD_2014}.htm)



## SetOverwrite {Concrete AASHTO_LRFD_2014}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_LRFD_2014/SetOverwrite_{Concrete_AASHTO_LRFD_2014}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_LRFD\_2014.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 11, inclusive, indicating the overwrite item considered.

1 = Live load reduction factor

2 = Unbraced length ratio, Major

3 = Unbraced length ratio, Minor

4 = Effective length factor, K Major

5 = Effective length factor, K Minor

6 = Moment coefficient, Cm Major

7 = Moment coefficient, Cm Minor

8 = Nonsway moment factor, Db Major

9 = Nonsway moment factor, Db Minor

10 = Sway moment factor, Ds Major

11 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Live load reduction factor

Value >= 0; 0 means use program determined value.

2 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

4 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

6 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

8 = Nonsway moment factor, Db Major

Value >= 0; 0 means use program determined value.

9 = Nonsway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

10 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItem AASHTO\_LRFD\_2014 ()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO LRFD 2014")

   'set overwrite item
      ret = SapModel.DesignConcrete.AASHTO\_LRFD\_2014.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 17.3.0.

## See Also

GetOverwrite



## SetPreference {Concrete AASHTO_LRFD_2014}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AASHTO_LRFD_2014/SetPreference_{Concrete_AASHTO_LRFD_2014}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.AASHTO\_LRFD\_2014.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 7, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic Zone

5 = Pattern live load factor

6 = Utilization factor limit

7 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and divisible by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic Zone

 0 = Zone 0

 1 = Zone 1

 2 = Zone 2

 3 = Zone 3

 4 = Zone 4

5 = Pattern live load factor

Value >= 0

6 = Utilization factor limit

Value > 0

7 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItem AASHTO\_LRFD\_2014()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AASHTO LRFD 2014")

   'set preference item
      ret = SapModel.DesignConcrete.AASHTO\_LRFD\_2014.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 17.3.0.

## See Also

[GetPreference](GetPreference_{Concrete_AASHTO_LRFD_2014}.htm)



## GetOverwrite {Concrete ACI 318-02}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-02/GetOverwrite_{Concrete_ACI_318-02}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.ACI\_318\_02.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway intermediate

3 = Sway ordinary

4 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemACI\_318\_02()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI 318-02")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.ACI\_318\_02.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_ACI_318-02}.htm)



## GetPreference {Concrete ACI 318-02}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-02/GetPreference_{Concrete_ACI_318-02}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.ACI\_318\_02.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 13, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic design category

5 = Phi tension controlled

6 = Phi compression controlled tied

7 = Phi compression controlled spiral

8 = Phi shear and/or torsion

9 = Phi shear seismic

10 = Phi joint shear

11 = Pattern live load factor

12 = Utilization factor limit

13 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

5 = Phi tension controlled

Value > 0

6 = Phi compression controlled tied

Value > 0

7 = Phi compression controlled spiral

Value > 0

8 = Phi shear and/or torsion

Value > 0

9 = Phi shear seismic

Value > 0

10 = Phi joint shear

Value > 0

11 = Pattern live load factor

Value >= 0

12 = Utilization factor limit

Value > 0

13 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemACI\_318\_02()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI 318-02")

   'get preference item
      ret = SapModel.DesignConcrete.ACI\_318\_02.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_ACI_318-02}.htm)



## SetOverwrite {Concrete ACI 318-02}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-02/SetOverwrite_{Concrete_ACI_318-02}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.ACI\_318\_02.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway intermediate

3 = Sway ordinary

4 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemACI\_318\_02()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI 318-02")

   'set overwrite item
      ret = SapModel.DesignConcrete.ACI\_318\_02.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_ACI_318-02}.htm)



## SetPreference {Concrete ACI 318-02}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-02/SetPreference_{Concrete_ACI_318-02}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.ACI\_318\_02.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 13, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic design category

5 = Phi tension controlled

6 = Phi compression controlled tied

7 = Phi compression controlled spiral

8 = Phi shear and/or torsion

9 = Phi shear seismic

10 = Phi joint shear

11 = Pattern live load factor

12 = Utilization factor limit

13 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

5 = Phi tension controlled

Value > 0

6 = Phi compression controlled tied

Value > 0

7 = Phi compression controlled spiral

Value > 0

8 = Phi shear and/or torsion

 Value > 0

9 = Phi shear seismic

Value > 0

10 = Phi joint shear

Value > 0

11 = Pattern live load factor

Value >= 0

12 = Utilization factor limit

Value > 0

13 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemACI\_318\_02()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI 318-02")

   'set preference item
      ret = SapModel.DesignConcrete.ACI\_318\_02.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_ACI_318-02}.htm)



## GetOverwrite {Concrete ACI 318-05 IBC 2003}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-05_IBC_2003/GetOverwrite_{Concrete_ACI_318-05_IBC_2003}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.ACI318\_05\_IBC2003.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Nonsway moment factor, Dns Major

10 = Nonsway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway Intermediate

3 = Sway Ordinary

4 = Nonsway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Nonsway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Nonsway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemACI318\_05\_IBC2003()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI318-05/IBC2003")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.ACI318\_05\_IBC2003.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_ACI_318-05_IBC_2003}.htm)



## GetPreference {Concrete ACI 318-05 IBC 2003}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-05_IBC_2003/GetPreference_{Concrete_ACI_318-05_IBC_2003}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.ACI318\_05\_IBC2003.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 13, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic design category

5 = Phi tension controlled

6 = Phi compression controlled tied

7 = Phi compression controlled spiral

8 = Phi shear and/or torsion

9 = Phi shear seismic

10 = Phi joint shear

11 = Pattern live load factor

12 = Utilization factor limit

13 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and divisible by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

5 = Phi tension controlled

Value > 0

6 = Phi compression controlled tied

Value > 0

7 = Phi compression controlled spiral

Value > 0

8 = Phi shear and/or torsion

Value > 0

9 = Phi shear seismic

Value > 0

10 = Phi joint shear

Value > 0

11 = Pattern live load factor

Value >= 0

12 = Utilization factor limit

Value > 0

13 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemACI318\_05\_IBC2003()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI318-05/IBC2003")

   'get preference item
      ret = SapModel.DesignConcrete.ACI318\_05\_IBC2003.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_ACI_318-05_IBC_2003}.htm)



## SetOverwrite {Concrete ACI 318-05 IBC 2003}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-05_IBC_2003/SetOverwrite_{Concrete_ACI_318-05_IBC_2003}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.ACI318\_05\_IBC2003.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway Intermediate

3 = Sway Ordinary

4 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects=  2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemACI318\_05\_IBC2003()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI318-05/IBC2003")

   'set overwrite item
      ret = SapModel.DesignConcrete.ACI318\_05\_IBC2003.SetOverwrite("8", 1, 4)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_ACI_318-05_IBC_2003}.htm)



## SetPreference {Concrete ACI 318-05 IBC 2003}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-05_IBC_2003/SetPreference_{Concrete_ACI_318-05_IBC_2003}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.ACI318\_05\_IBC2003.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 13, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic design category

5 = Phi tension controlled

6 = Phi compression controlled tied

7 = Phi compression controlled spiral

8 = Phi shear and/or torsion

9 = Phi shear seismic

10 = Phi joint shear

11 = Pattern live load factor

12 = Utilization factor limit

13 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and divisible by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

5 = Phi tension controlled

Value > 0

6 = Phi compression controlled tied

Value > 0

7 = Phi compression controlled spiral

Value > 0

8 = Phi shear and/or torsion

Value > 0

9 = Phi shear seismic

Value > 0

10 = Phi joint shear

Value > 0

11 = Pattern live load factor

Value >= 0

12 = Utilization factor limit

Value > 0

13 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemACI318\_05\_IBC2003()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI318-05/IBC2003")

   'set preference item
      ret = SapModel.DesignConcrete.ACI318\_05\_IBC2003.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_ACI_318-05_IBC_2003}.htm)



## GetOverwrite {Concrete ACI 318-08 IBC 2009}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-08_IBC_2009/GetOverwrite_{Concrete_ACI_318-08_IBC_2009}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.ACI318\_08\_IBC2009.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 15, inclusive, indicating the overwrite item considered.

1 = Framing type (beam and column)

2 = Live load reduction factor (beam and column)

3 = Unbraced length ratio, Major (beam and column)

4 = Unbraced length ratio, Minor (beam and column)

5 = Effective length factor, K Major (column only)

6 = Effective length factor, K Minor (column only)

7 = Moment coefficient, Cm Major (column only)

8 = Moment coefficient, Cm Minor (column only)

9 = Non-sway moment factor, Dns Major (column only)

10 = Non-sway moment factor, Dns Minor (column only)

11 = Sway moment factor, Ds Major (column only)

12 = Sway moment factor, Ds Minor (column only)

13 = Tangent of the angle of concrete compressive strut (beam only)

14 = Consider torsion (beam only)

15 = Concrete cover for closed stirrups (beam only)

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway Intermediate

3 = Sway Ordinary

4 = Nonsway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Nonsway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Nonsway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

13 = Tangent of the angle of concrete compressive strut

Value >= 0; 0 means use program determined value.

14 = Consider torsion

0 = No

Any other value = Yes

15 = Concrete cover for closed stirrups

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemACI318\_08\_IBC2009()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI318-08/IBC2009")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.ACI318\_08\_IBC2009.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.2.0.

Added items 13~15 in version 23.4.0

## See Also

[SetOverwrite](mk:@MSITStore:W:/Released/SAP2000 V15/15.0.0 Server/CSi_OAPI_Documentation.chm::/SAP2000_API_Fuctions/Design/Concrete/ACI_318-05_IBC_2003/SetOverwrite_%7bConcrete_ACI_318-05_IBC_2003%7d.htm)



## GetPreference {Concrete ACI 318-08 IBC 2009}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-08_IBC_2009/GetPreference_{Concrete_ACI_318-08_IBC_2009}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.ACI318\_08\_IBC2009.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 18, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic design category

5 = Phi tension controlled

6 = Phi compression controlled tied

7 = Phi compression controlled spiral

8 = Phi shear and/or torsion

9 = Phi shear seismic

10 = Phi joint shear

11 = Pattern live load factor

12 = Utilization factor limit

13 = Multi-response case design

14 = System Rho

15 = System Sds

16 = Tangent of the angle of concrete compressive strut

17 = Consider torsion

18 = Design for B/C capacity ratio

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

5 = Phi tension controlled

Value > 0

6 = Phi compression controlled tied

Value > 0

7 = Phi compression controlled spiral

Value > 0

8 = Phi shear and/or torsion

Value > 0

9 = Phi shear seismic

Value > 0

10 = Phi joint shear

Value > 0

11 = Pattern live load factor

Value >= 0

12 = Utilization factor limit

Value > 0

13 = Multi-response case design

1 = Envelopes

2 = Step-by step

3= Last step

4 = Envelopes - All

5 = Step-by step - All

14 = System Rho

Value > 0

15 = System Sds

Value > 0

16 = Tangent of the angle of concrete compressive strut

Value >= 0

17 = Consider torsion

0 = No

Any other value = Yes

18 = Design for B/C capacity ratio

0 = No

Any other value = Yes

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemACI318\_08\_IBC2009()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI318-08/IBC2009")

   'get preference item
      ret = SapModel.DesignConcrete.ACI318\_08\_IBC2009.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.2.0.

Added items 14~18 in version 23.4.0

## See Also

[SetPreference](mk:@MSITStore:W:/Released/SAP2000 V15/15.0.0 Server/CSi_OAPI_Documentation.chm::/SAP2000_API_Fuctions/Design/Concrete/ACI_318-05_IBC_2003/SetPreference_%7bConcrete_ACI_318-05_IBC_2003%7d.htm)



## SetOverwrite {Concrete ACI 318-08 IBC 2009}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-08_IBC_2009/SetOverwrite_{Concrete_ACI_318-08_IBC_2009}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.ACI318\_08\_IBC2009.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 15, inclusive, indicating the overwrite item considered.

1 = Framing type (beam and column)

2 = Live load reduction factor (beam and column)

3 = Unbraced length ratio, Major (beam and column)

4 = Unbraced length ratio, Minor (beam and column)

5 = Effective length factor, K Major (column only)

6 = Effective length factor, K Minor (column only)

7 = Moment coefficient, Cm Major (column only)

8 = Moment coefficient, Cm Minor (column only)

9 = Non-sway moment factor, Dns Major (column only)

10 = Non-sway moment factor, Dns Minor (column only)

11 = Sway moment factor, Ds Major (column only)

12 = Sway moment factor, Ds Minor (column only)

13 = Tangent of the angle of concrete compressive strut (beam only)

14 = Consider torsion (beam only)

15 = Concrete cover for closed stirrups (beam only)

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway Intermediate

3 = Sway Ordinary

4 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

13 = Tangent of the angle of concrete compressive strut

Value >= 0; 0 means use program determined value.

14 = Consider torsion

0 = No

Any other value = Yes

15 = Concrete cover for closed stirrups

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects=  2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemACI318\_08\_IBC2009()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI318-08/IBC2009")

   'set overwrite item
      ret = SapModel.DesignConcrete.ACI318\_08\_IBC2009.SetOverwrite("8", 1, 4)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.2.0.

Added items 13~15 in version 23.4.0

## See Also

[GetOverwrite](mk:@MSITStore:W:/Released/SAP2000 V15/15.0.0 Server/CSi_OAPI_Documentation.chm::/SAP2000_API_Fuctions/Design/Concrete/ACI_318-05_IBC_2003/GetOverwrite_%7bConcrete_ACI_318-05_IBC_2003%7d.htm)



## SetPreference {Concrete ACI 318-08 IBC 2009}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-08_IBC_2009/SetPreference__{Concrete_ACI_318-08_IBC_2009}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.ACI318\_08\_IBC2009.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 18, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Seismic design category

5 = Phi tension controlled

6 = Phi compression controlled tied

7 = Phi compression controlled spiral

8 = Phi shear and/or torsion

9 = Phi shear seismic

10 = Phi joint shear

11 = Pattern live load factor

12 = Utilization factor limit

13 = Multi-response case design

14 = System Rho

15 = System Sds

16 = Tangent of the angle of concrete compressive strut

17 = Consider torsion

18 = Design for B/C capacity ratio

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

5 = Phi tension controlled

Value > 0

6 = Phi compression controlled tied

Value > 0

7 = Phi compression controlled spiral

Value > 0

8 = Phi shear and/or torsion

Value > 0

9 = Phi shear seismic

Value > 0

10 = Phi joint shear

Value > 0

11 = Pattern live load factor

Value >= 0

12 = Utilization factor limit

Value > 0

13 = Multi-response case design

1 = Envelopes

2 = Step-by step

3= Last step

4 = Envelopes - All

5 = Step-by step - All

14 = System Rho

Value > 0

15 = System Sds

Value > 0

16 = Tangent of the angle of concrete compressive strut

Value >= 0

17 = Consider torsion

0 = No

Any other value = Yes

18 = Design for B/C capacity ratio

0 = No

Any other value = Yes

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemACI318\_08\_IBC2009()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI318-08/IBC2009")

   'set preference item
      ret = SapModel.DesignConcrete.ACI318\_08\_IBC2009.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.2.0.

Added items 14~18 in version 23.4.0

## See Also

[GetPreference](mk:@MSITStore:W:/Released/SAP2000 V15/15.0.0 Server/CSi_OAPI_Documentation.chm::/SAP2000_API_Fuctions/Design/Concrete/ACI_318-05_IBC_2003/GetPreference_%7bConcrete_ACI_318-05_IBC_2003%7d.htm)



## GetOverwrite {Concrete ACI 318-99}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-99/GetOverwrite_{Concrete_ACI_318-99}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.ACI\_318\_99.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = No-nsway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway intermediate

3 = Sway ordinary

4 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemACI\_318\_99()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI 318-99")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.ACI\_318\_99.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_ACI_318-99}.htm)



## GetPreference {Concrete ACI 318-99}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-99/GetPreference_{Concrete_ACI_318-99}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.ACI\_318\_99.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi bending torsion

5 = Phi compression controlled tied

6 = Phi compression controlled spiral

7 = Phi shear

8 = Pattern live load factor

9 = Utilization factor limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi bending torsion

Value > 0

5 = Phi compression controlled tied

Value > 0

6 = Phi compression controlled spiral

Value > 0

7 = Phi shear

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Utilization factor limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemACI\_318\_99()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI 318-99")

   'get preference item
      ret = SapModel.DesignConcrete.ACI\_318\_99.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_ACI_318-99}.htm)



## SetOverwrite {Concrete ACI 318-99}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-99/SetOverwrite_{Concrete_ACI_318-99}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.ACI\_318\_99.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway intermediate

3 = Sway ordinary

4 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemACI\_318\_99()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI 318-99")

   'set overwrite item
      ret = SapModel.DesignConcrete.ACI\_318\_99.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_ACI_318-99}.htm)



## SetPreference {Concrete ACI 318-99}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_318-99/SetPreference_{Concrete_ACI_318-99}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.ACI\_318\_99.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi bending torsion

5 = Phi compression controlled tied

6 = Phi compression controlled spiral

7 = Phi shear

8 = Pattern live load factor

9 = Utilization factor limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi bending torsion

Value > 0

5 = Phi compression controlled tied

Value > 0

6 = Phi compression controlled spiral

Value > 0

7 = Phi shear

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Utilization factor limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemACI\_318\_99()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'createSapModelobject
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI 318-99")

   'set preference item
      ret = SapModel.DesignConcrete.ACI\_318\_99.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_ACI_318-99}.htm)



## GetOverwrite {ACI 350-2020}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_350_2020/GetOverwrite_{ACI_350-2020}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcreteShell.ACI350\_20.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete shell design procedure.

Item

This is an integer between 1 and 11, inclusive, indicating the overwrite item considered.

1 = Number rebar layer

2 = Concrete cover to center of top rebar layer in direction 1

3 = Concrete cover to center of top rebar layer in direction 2

4 = Concrete cover to center of bottom rebar layer in direction 1

5 = Concrete cover to center of bottom rebar layer in direction 2

6 = Longitudinal bar size

7 = Environmental exposure conditions

8 = Environmental durability factor for axial forces

9 = Environmental durability factor for moments

10 = Environmental durability factor for shear

11 = Consider shear design

Value

The value of the considered overwrite item.

1 = Number rebar layer

0 = Program Default

1 = 1 layer

2 = 2 layers

2 = Concrete cover to center of top rebar layer in direction 1

Value >= 0; 0 means value taken from shell section definition.

3 = Concrete cover to center of top rebar layer in direction 2

Value >= 0; 0 means value taken from shell section definition.

4 = Concrete cover to center of bottom rebar layer in direction 1

Value >= 0; 0 means value taken from shell section definition.

5 = Concrete cover to center of bottom rebar layer in direction 2

Value >= 0; 0 value taken from shell section definition.

6 = Longitudinal bar size

      1 = #2

      2 = #3

      3 = #4

      4 = #5

      5 = #6

      6 = #7

      7 = #8

      8 = #9

      9 = #10

      10 = #11

      11 = #14

      12 = #18

      13 = 10M

      14 = 15M

      15 = 20M

      16 = 25M

      17 = 30M

      18 = 35M

      19 = 45M

      20 = 55M

      21 = 6d

      22 = 8d

      23 = 10d

      24 = 12d

      25 = 14d

      26 = 16d

      27 = 20d

      28 = 25d

      29 = 26d

      30 = 28d

      31 = N12

      32 = N16

      33 = N20

      34 = N24

      35 = N28

      36 = N32

      37 = N36

7 = Environmental exposure conditions

0 = Program Default

1 = Normal

2 = Extreme

8 = Environmental durability factor for axial forces

Value >= 0; 0 means use program determined value.

9 = Environmental durability factor for moments

Value >= 0; 0 means use program determined value

10 = Environmental durability factor for shear

Value >= 0; 0 means use program determined value

11 = Consider shear design

 0 = No

Any other value = Yes

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcretShellDesignOverwriteItemACI350\_20()

   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model

      ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

   'create a wall model from template

      ret = SapModel.File.NewWall(6, 4, 6, 4)

   'set concrete shell design code
      ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

   'set concrete shell design overwrite

      ret = SapModel.DesignConcreteShell.ACI350\_20.SetOverwrite("1", 4, 1.345)

   'get overwrite item
      ret = SapModel.DesignConcreteShell.ACI350\_20.GetOverwrite("1", 4, value, progdet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0.

## See Also

[SetOverwrite](SetPreference_{ACI_350-2020}.htm)



## GetPreference {ACI 350-2020}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_350_2020/GetPreference_{ACI_350-2020}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcreteShell.ACI350\_20.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 6, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Consider environmental durability

3 = Consider shear design

4 = Shear design method

5 = Cotangent of the angle of concrete compressive strut

6 = Add tensile force due to shear

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3= Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Consider environmental durability

0 = No

Any other value = Yes

3 = Consider shear design

0 = No

Any other value = Yes

4 = Shear design method

1 = Method 1 – considers increasing longitudinal reinforcement to increase concrete shear capacity up to the allowable limit. If insufficient, shear reinforcement will be added

2 = Method 2 – determines required shear reinforcement without considering to increase longitudinal reinforcement

5 = Cotangent of the angle of concrete compressive strut

Value > 0

6 = Add tensile force due to shear

0 = No

Any other value = Yes

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteShellDesignPreferenceItemACI350\_20()

   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model

      ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

   'create a wall model from template

      ret = SapModel.File.NewWall(6, 4, 6, 4)

   'set concrete shell design code
      ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

   'set concrete shell design preference

      ret = SapModel.DesignConcreteShell.ACI350\_20.SetPreference(5, 0.7)

   'get preference item
      ret = SapModel.DesignConcreteShell.ACI350\_20.GetPreference(5, Value)

   'close Sap2000
      SapObject.ApplicationExit(False)
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0.

## See Also

[SetPreference](SetPreference_{ACI_350-2020}.htm)



## SetOverwrite {ACI 350-2020}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_350_2020/SetOverwrite_{ACI_350-2020}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcreteShell.ACI350\_20.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 11, inclusive, indicating the overwrite item considered.

1 = Number rebar layer

2 = Concrete cover to center of top rebar layer in direction 1

3 = Concrete cover to center of top rebar layer in direction 2

4 = Concrete cover to center of bottom rebar layer in direction 1

5 = Concrete cover to center of bottom rebar layer in direction 2

6 = Longitudinal bar size

7 = Environmental exposure conditions

8 = Environmental durability factor for axial forces

9 = Environmental durability factor for moments

10 = Environmental durability factor for shear

11 = Consider shear design

Value

The value of the considered overwrite item.

1 = Number rebar layer

0 = Program Default

1 = 1 layer

2 = 2 layers

2 = Concrete cover to center of top rebar layer in direction 1

Value >= 0; 0 means value taken from shell section definition.

3 = Concrete cover to center of top rebar layer in direction 2

Value >= 0; 0 means value taken from shell section definition.

4 = Concrete cover to center of bottom rebar layer in direction 1

Value >= 0; 0 means value taken from shell section definition.

5 = Concrete cover to center of bottom rebar layer in direction 2

Value >= 0; 0 value taken from shell section definition.

6 = Longitudinal bar size

      1 = #2

      2 = #3

      3 = #4

      4 = #5

      5 = #6

      6 = #7

      7 = #8

      8 = #9

      9 = #10

      10 = #11

      11 = #14

      12 = #18

      13 = 10M

      14 = 15M

      15 = 20M

      16 = 25M

      17 = 30M

      18 = 35M

      19 = 45M

      20 = 55M

      21 = 6d

      22 = 8d

      23 = 10d

      24 = 12d

      25 = 14d

      26 = 16d

      27 = 20d

      28 = 25d

      29 = 26d

      30 = 28d

      31 = N12

      32 = N16

      33 = N20

      34 = N24

      35 = N28

      36 = N32

      37 = N36

7 = Environmental exposure conditions

0 = Program Default

1 = Normal

2 = Extreme

8 = Environmental durability factor for axial forces

Value >= 0; 0 means use program determined value.

9 = Environmental durability factor for moments

Value >= 0; 0 means use program determined value

10 = Environmental durability factor for shear

Value >= 0; 0 means use program determined value

11 = Consider shear design

 0 = No

Any other value = Yes

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects=  2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteShellDesignOverwriteItemACI350\_20()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim value As Double

      Dim progdet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model

      ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

   'create a wall model from template

      ret = SapModel.File.NewWall(6, 4, 6, 4)

   'set concrete shell design code
      ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

   'set concrete shell design overwrite

      ret = SapModel.DesignConcreteShell.ACI350\_20.SetOverwrite("1", 4, 1.345)

   'get overwrite item
      ret = SapModel.DesignConcreteShell.ACI350\_20.GetOverwrite("1", 4, value, progdet)

   'close Sap2000
      SapObject.ApplicationExit(False)
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0.

## See Also

[GetOverwrite](GetOverwrite_{ACI_350-2020}.htm)



## SetPreference {ACI 350-2020}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ACI_350_2020/SetPreference_{ACI_350-2020}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.ACI350\_20.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 6, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Consider environmental durability

3 = Consider shear design

4 = Shear design method

5 = Cotangent of the angle of concrete compressive strut

6 = Add tensile force due to shear

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3= Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Consider environmental durability

0 = No

Any other value = Yes

3 = Consider shear design

0 = No

Any other value = Yes

4 = Shear design method

1 = Method 1 – considers increasing longitudinal reinforcement to increase concrete shear capacity up to the allowable limit. If insufficient, shear reinforcement will be added

2 = Method 2 – determines required shear reinforcement without considering to increase longitudinal reinforcement

5 = Cotangent of the angle of concrete compressive strut

Value > 0

6 = Add tensile force due to shear

0 = No

Any other value = Yes

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteShellDesignPreferenceItemACI350\_20()
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

      ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

   'create a wall model from template

      ret = SapModel.File.NewWall(6, 4, 6, 4)

   'set concrete shell design code
      ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

   'set concrete shell design preference

      ret = SapModel.DesignConcreteShell.ACI350\_20.SetPreference(5, 0.7)

   'get preference item
      ret = SapModel.DesignConcreteShell.ACI350\_20.GetPreference(5, Value)

   'close Sap2000
      SapObject.ApplicationExit(False)
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0.

## See Also

[GetPreference](GetPreference_{ACI_350-2020}.htm)



## GetOverwrite {Concrete AS 3600-09}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AS_3600-09/GetOverwrite_{Concrete_AS_3600-09}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.AS\_3600\_09.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design
procedure.

Item

This is an integer between 1 and 15, inclusive, indicating
the overwrite item considered.

1 = Framing type (beam
and column)

2 = Live load reduction
factor (beam and column)

3 = Unbraced length ratio,
Major (beam and column)

4 = Unbraced length ratio,
Minor (beam and column)

5 = Effective length factor,
K Major (column only)

6 = Effective length factor,
K Minor (column only)

7 = Moment coefficient,
km Major (column only)

8 = Moment coefficient,
km Minor (column only)

9 = Nonsway moment factor,
Db Major (column only)

10 = Nonsway moment factor,
Db Minor (column only)

11 = Sway moment factor,
Ds Major (column only)

12 = Sway moment factor,
Ds Minor (column only)

13
= Tangent of the angle of concrete compressive strut (beam only)

14 = Consider torsion (beam
only)

15 = Concrete cover for
closed stirrups (beam only)

Value

The value of the considered
overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Sway special

2 = Sway intermediate

3 = Sway ordinary

4 = Nonsway

2 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

3 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value.

4 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value.

5 = Effective length factor,
K Major

Value >= 0; 0 means
use program determined value.

6 = Effective length factor,
K Minor

Value >= 0; 0 means
use program determined value.

7 = Moment coefficient,
km Major

Value >= 0; 0 means
use program determined value.

8 = Moment coefficient,
km Minor

Value >= 0; 0 means
use program determined value.

9 = Nonsway moment factor,
Db Major

Value >= 0; 0 means
use program determined value.

10 = Nonsway moment factor,
Db Minor

  Value >=
0; 0 means use program determined value.

11 = Sway moment factor,
Ds Major

  Value >=
0; 0 means use program determined value.

12 = Sway moment factor,
Ds Minor

  Value >=
0; 0 means use program determined value.

13 = Tangent of the angle
of concrete compressive strut

Value >= 0; 0 means
use program determined value.

14 = Consider torsion

0 = No

Any other value = Yes

15 = Concrete cover for
closed stirrups

Value >=
0; 0 means use program determined value.

ProgDet

If this item is True then the specified value is program
determined.

## Remarks

This function retrieves the value of a concrete design
overwrite item.

The function returns zero if the item is successfully
retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemAS\_3600\_09()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AS
3600-09")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.AS\_3600\_09.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

Added items 13~15 in version 23.4.0

## See Also

[SetOverwrite](SetOverwrite_{Concrete_AS_3600-09}.htm)



## GetPreference {Concrete AS 3600-09}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AS_3600-09/GetPreference_{Concrete_AS_3600-09}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.AS\_3600\_09.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 13, inclusive, indicating
the preference item considered.

1 = Number of interaction
curves

2 = Number of interaction
points

3
= Consider minimum eccentricity

4
= Phi tension controlled

5 = Phi compression controlled

6 = Phi shear and/or torsion

7 = Phi shear seismic

8 = Phi joint shear

9 = Pattern live load
factor

10 = Utilization factor
limit

11 = Multi-response case
design

12
= Consider torsion

13 = Design for B/C capacity
ratio

Value

The value of the considered preference item.

1 = Number of interaction
curves

Value >= 4 and divisible
by 4

2 = Number of interaction
points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi tension controlled

Value > 0

5 = Phi compression controlled

Value > 0

6 = Phi shear and/or torsion

Value > 0

7 = Phi shear seismic

Value > 0

8 = Phi joint shear

Value
> 0

9 = Pattern live load
factor

Value >= 0

10 = Utilization factor
limit

  Value >
0

 11 = Multi-response
case design

1 = Envelopes

2 = Step-by step

3= Last step

4 = Envelopes - All

5 = Step-by step - All

12 = Consider torsion

0 = No

Any other value
= Yes

13 = Design for B/C capacity ratio

0 = No

Any other value
= Yes

## Remarks

This function retrieves the value of a concrete design
preference item.

The function returns zero if the item is successfully
retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemAS\_3600\_09()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AS
3600-09")

   'get preference item
      ret = SapModel.DesignConcrete.AS\_3600\_09.GetPreference(2,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

Added items 12~13 in version 23.4.0

## See Also

[SetPreference](SetPreference_{Concrete_AS_3600-09}.htm)



## SetOverwrite {Concrete AS 3600-09}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AS_3600-09/SetOverwrite_{Concrete_AS_3600-09}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.AS\_3600\_09.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 15, inclusive, indicating
the overwrite item considered.

1 = Framing type (beam
and column)

2 = Live load reduction
factor (beam and column)

3 = Unbraced length ratio,
Major (beam and column)

4 = Unbraced length ratio,
Minor (beam and column)

5 = Effective length factor,
K Major (column only)

6 = Effective length factor,
K Minor (column only)

7 = Moment coefficient,
km Major (column only)

8 = Moment coefficient,
km Minor (column only)

9 = Nonsway moment factor,
Db Major (column only)

10 = Nonsway moment factor,
Db Minor (column only)

11 = Sway moment factor,
Ds Major (column only)

12 = Sway moment factor,
Ds Minor (column only)

13
= Tangent of the angle of concrete compressive strut (beam only)

14 = Consider torsion (beam
only)

15 = Concrete cover for
closed stirrups (beam only)

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Sway special

2 = Sway intermediate

3 = Sway ordinary

4 = Nonsway

2 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

3 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value.

4 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value.

5 = Effective length factor,
K Major

Value >= 0; 0 means
use program determined value.

6 = Effective length factor,
K Minor

Value >= 0; 0 means
use program determined value.

7 = Moment coefficient,
km Major

Value >= 0; 0 means
use program determined value.

8 = Moment coefficient,
km Minor

Value >= 0; 0 means
use program determined value.

9 = Nonsway moment factor,
Db Major

Value >= 0; 0 means
use program determined value.

10 = Nonsway moment factor,
Db Minor

  Value >=
0; 0 means use program determined value.

11 = Sway moment factor,
Ds Major

  Value >=
0; 0 means use program determined value.

12 = Sway moment factor,
Ds Minor

  Value >=
0; 0 means use program determined value.

13
= Tangent of the angle of concrete compressive strut

Value >= 0; 0 means
use program determined value.

14 = Consider torsion

0 = No

Any other value = Yes

15 = Concrete cover for
closed stirrups

Value >=
0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType
enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item
is Object, the assignment is made to the frame object specified by the
Name item.

If this item
is Group, the assignment is made to all frame objects in the group specified
by the Name item.

If this item
is SelectedObjects, assignment is made to all selected frame objects and
the Name item is ignored.

## Remarks

This function
sets the value of a concrete design overwrite item.

The function
returns zero if the item is successfully set, otherwise it returns a nonzero
value.

## VBA Example

Sub SetConcreteDesignOverwriteItemAS\_3600\_09()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AS
3600-09")

   'set overwrite item
      ret = SapModel.DesignConcrete.AS\_3600\_09.SetOverwrite("8",
1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

Added items 13~15 in version 23.4.0

## See Also

[GetOverwrite](GetOverwrite_{Concrete_AS_3600-09}.htm)



## SetPreference {Concrete AS 3600-09}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/AS_3600-09/SetPreference_{Concrete_AS_3600-09}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.AS\_3600\_09.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 13, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi tension controlled

5 = Phi compression controlled

6 = Phi shear and/or torsion

7 = Phi shear seismic

8 = Phi joint shear

9 = Pattern live load factor

10 = Utilization factor limit

11 = Time history design

12 = Consider torsion

13 = Design for B/C capacity ratio

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and divisible by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi tension controlled

Value > 0

5 = Phi compression controlled

Value > 0

6 = Phi shear and/or torsion

Value > 0

7 = Phi shear seismic

Value > 0

8 = Phi joint shear

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Utilization factor limit

  Value > 0

11 = Multi-response case design

        1 = Envelopes

        2 = Step-by step

        3= Last step

        4 = Envelopes - All

        5 = Step-by step - All

12 = Consider torsion

0 = No

Any other value = Yes

13 = Design for B/C capacity ratio

0 = No

Any other value = Yes

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemAS\_3600\_09()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AS 3600-00")

   'set preference item
      ret = SapModel.DesignConcrete.AS\_3600\_09.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.01.

Added items 12~13 in version 23.4.0

## See Also

[GetPreference](mk:@MSITStore:W:/Released/SAP2000 V15/15.0.0 Server/CSi_OAPI_Documentation.chm::/SAP2000_API_Fuctions/Design/Concrete/Australian_AS_3600-01/GetPreference_%7bConcrete_Australian_AS_3600-01%7d.htm)



## GetOverwrite {Concrete Australian AS 3600-01}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Australian_as_3600-01/GetOverwrite_{Concrete_Australian_AS_3600-01}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.AS\_3600\_01.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, km Major

8 = Moment coefficient, km Minor

9 = Nonsway moment factor, Db Major

10 = Nonsway moment factor, Db Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway intermediate

3 = Sway ordinary

4 = Nonsway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, km Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, km Minor

Value >= 0; 0 means use program determined value.

9 = Nonsway moment factor, Db Major

Value >= 0; 0 means use program determined value.

10 = Nonsway moment factor, Db Minor

  Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

  Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

  Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemAS\_3600\_01()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AS 3600-01")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.AS\_3600\_01.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.0.0.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_Australian_AS_3600-01}.htm)



## GetPreference {Concrete Australian AS 3600-01}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Australian_as_3600-01/GetPreference_{Concrete_Australian_AS_3600-01}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.AS\_3600\_01.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi tension controlled

5 = Phi compression controlled

6 = Phi shear and/or torsion

7 = Phi shear seismic

8 = Phi joint shear

9 = Pattern live load factor

10 = Utilization factor limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and divisible by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi tension controlled

Value > 0

5 = Phi compression controlled

Value > 0

6 = Phi shear and/or torsion

Value > 0

7 = Phi shear seismic

Value > 0

8 = Phi joint shear

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Utilization factor limit

  Value > 0

11 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemAS\_3600\_01()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AS 3600-01")

   'get preference item
      ret = SapModel.DesignConcrete.AS\_3600\_01.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.0.0.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_Australian_AS_3600-01}.htm)



## SetOverwrite {Concrete Australian AS 3600-01}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Australian_as_3600-01/SetOverwrite_{Concrete_Australian_AS_3600-01}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.AS\_3600\_01.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, km Major

8 = Moment coefficient, km Minor

9 = Nonsway moment factor, Db Major

10 = Nonsway moment factor, Db Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway intermediate

3 = Sway ordinary

4 = Nonsway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, km Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, km Minor

Value >= 0; 0 means use program determined value.

9 = Nonsway moment factor, Db Major

Value >= 0; 0 means use program determined value.

10 = Nonsway moment factor, Db Minor

  Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

  Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

        Value >= 0; 0 means use program determined value

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemAS\_3600\_01()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AS 3600-01")

   'set overwrite item
      ret = SapModel.DesignConcrete.AS\_3600\_01.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.0.0.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Australian_AS_3600-01}.htm)



## SetPreference {Concrete Australian AS 3600-01}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Australian_as_3600-01/SetPreference_{Concrete_Australian_AS_3600-01}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.AS\_3600\_01.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi tension controlled

5 = Phi compression controlled

6 = Phi shear and/or torsion

7 = Phi shear seismic

8 = Phi joint shear

9 = Pattern live load factor

10 = Utilization factor limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and divisible by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi tension controlled

Value > 0

5 = Phi compression controlled

Value > 0

6 = Phi shear and/or torsion

Value > 0

7 = Phi shear seismic

Value > 0

8 = Phi joint shear

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Utilization factor limit

  Value > 0

11 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemAS\_3600\_01()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("AS 3600-01")

   'set preference item
      ret = SapModel.DesignConcrete.AS\_3600\_01.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.0.0.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_Australian_AS_3600-01}.htm)



## GetOverwrite {Concrete BS8110-89}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/BS8110_89/GetOverwrite_{Concrete_BS8110-89}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.BS8110\_89.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, Beta Major

6 = Effective length factor, Beta Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemBS8110\_89()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("BS8110 89")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.BS8110\_89.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_BS8110-89}.htm)



## GetPreference {Concrete BS8110-89}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/BS8110_89/GetPreference_{Concrete_BS8110-89}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.BS8110\_89.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 6, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Pattern live load factor

5 = Utilization factor limit

6 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Pattern live load factor

Value >= 0

5 = Utilization factor limit

Value > 0

6 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemBS8110\_89()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("BS8110 89")

   'get preference item
      ret = SapModel.DesignConcrete.BS8110\_89.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_BS8110-89}.htm)



## SetOverwrite {Concrete BS8110-89}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/BS8110_89/SetOverwrite_{Concrete_BS8110-89}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.BS8110\_89.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, Beta Major

6 = Effective length factor, Beta Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemBS8110\_89()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("BS8110 89")

   'set overwrite item
      ret = SapModel.DesignConcrete.BS8110\_89.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_BS8110-89}.htm)



## SetPreference {Concrete BS8110-89}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/BS8110_89/SetPreference_{Concrete_BS8110-89}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.BS8110\_89.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 6, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Pattern live load factor

5 = Utilization factor limit

6 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Pattern live load factor

Value >= 0

5 = Utilization factor limit

Value > 0

6 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemBS8110\_89()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("BS8110 89")

   'set preference item
      ret = SapModel.DesignConcrete.BS8110\_89.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_BS8110-89}.htm)



## GetOverwrite {Concrete BS8110 97}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/BS8110_97/GetOverwrite_{Concrete_BS8110_97}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.BS8110\_97.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, Beta Major

6 = Effective length factor, Beta Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemBS8110\_97()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("BS8110 97")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.BS8110\_97.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_BS8110_97}.htm)



## GetPreference {Concrete BS8110 97}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/BS8110_97/GetPreference_{Concrete_BS8110_97}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.BS8110\_97.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Gamma steel

5 = Gamma concrete

6 = Gamma concrete shear

7 = Pattern live load factor

8 = Utilization factor limit

9 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and desvisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Gamma steel

Value > 0

5 = Gamma concrete

Value > 0

6 = Gamma concrete shear

Value > 0

7 = Pattern live load factor

Value >= 0

8 = Utilization factor limit

Value > 0

9 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemBS8110\_97()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("BS8110 97")

   'get preference item
      ret = SapModel.DesignConcrete.BS8110\_97.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_BS8110_97}.htm)



## SetOverwrite {Concrete BS8110 97}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/BS8110_97/SetOverwrite_{Concrete_BS8110_97}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.BS8110\_97.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, Beta Major

6 = Effective length factor, Beta Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemBS8110\_97()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("BS8110 97")

   'set overwrite item
      ret = SapModel.DesignConcrete.BS8110\_97.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_BS8110_97}.htm)



## SetPreference {Concrete BS8110 97}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/BS8110_97/SetPreference_{Concrete_BS8110_97}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete. BS8110\_97.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Gamma steel

5 = Gamma concrete

6 = Gamma concrete shear

7 = Pattern live load factor

8 = Utilization factor limit

9 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Gamma steel

Value > 0

5 = Gamma concrete

Value > 0

6 = Gamma concrete shear

Value > 0

7 = Pattern live load factor

Value >= 0

8 = Utilization factor limit

Value > 0

9 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemBS8110\_97()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("BS8110 97")

   'set preference item
      ret = SapModel.DesignConcrete.BS8110\_97.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_BS8110_97}.htm)



## GetOverwrite {Concrete CSA A23304}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/CSA_A23304/GetOverwrite_{Concrete_CSA_A23304}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.CSA\_A23\_3\_04.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Db Major

10 = Non-sway moment factor, Db Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

13 = Force modification factor, Rd

14 = Force modification factor, Ro

15 = Maximum aggregate size

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ductile

2 = Moderate

3 = Conventional

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Db Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

13 = Force modification factor, Rd

Value >= 0; 0 means use program determined value.

14 = Force modification factor, Ro

Value >= 0; 0 means use program determined value.

15 = Maximum aggregate size

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemCSA\_A23\_3\_04()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("CSA A23.3-04")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.CSA\_A23\_3\_04.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_CSA_A23304}.htm)



## GetPreference {Concrete CSA A23304}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/CSA_A23304/GetPreference_{Concrete_CSA_A23304}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.CSA\_A23\_3\_04.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 8, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi steel

5 = Phi concrete

6 = Pattern live load factor

7 = Utilization factor limit

8 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi steel

Value > 0

5 = Phi concrete

Value > 0

6 = Pattern live load factor

Value >= 0

7 = Utilization factor limit

Value > 0

8 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemCSA\_A23\_3\_04()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("CSA A23.3-04")

   'get preference item
      ret = SapModel.DesignConcrete.CSA\_A23\_3\_04.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_CSA_A23304}.htm)



## SetOverwrite {Concrete CSA A23304}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/CSA_A23304/SetOverwrite_{Concrete_CSA_A23304}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.CSA\_A23\_3\_04.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Db Major

10 = Non-sway moment factor, Db Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

13 = Force modification factor, Rd

14 = Force modification factor, Ro

15 = Maximum aggregate size

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ductile

2 = Moderate

3 = Conventional

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Db Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

13 = Force modification factor, Rd

Value >= 0; 0 means use program determined value.

14 = Force modification factor, Ro

Value >= 0; 0 means use program determined value.

15 = Maximum aggregate size

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemCSA\_A23\_3\_04()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("CSA A23.3-04")

   'set overwrite item
      ret = SapModel.DesignConcrete.CSA\_A23\_3\_04.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_CSA_A23304}.htm)



## SetPreference {Concrete CSA A23304}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/CSA_A23304/SetPreference_{Concrete_CSA_A23304}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.CSA\_A23\_3\_04.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 8, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi steel

5 = Phi concrete

6 = Pattern live load factor

7 = Utilization factor limit

8 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi steel

Value > 0

5 = Phi concrete

Value > 0

6 = Pattern live load factor

Value >= 0

7 = Utilization factor limit

Value > 0

8 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemCSA\_A23\_3\_04()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("CSA A23.3-04")

   'set preference item
      ret = SapModel.DesignConcrete.CSA\_A23\_3\_04.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_CSA_A23304}.htm)



## GetOverwrite {Concrete CSA A23394}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/CSA_A23394/GetOverwrite_{Concrete_CSA_A23394}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.CSA\_A23\_3\_94.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Db Major

10 = Non-sway moment factor, Db Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ductile

2 = Nominal

3 = Ordinary

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Db Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemCSA\_A23\_3\_94()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("CSA-A23.3-94")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.CSA\_A23\_3\_94.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_CSA_A23394}.htm)



## GetPreference {Concrete CSA A23394}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/CSA_A23394/GetPreference_{Concrete_CSA_A23394}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.CSA\_A23\_3\_94.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 8, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi steel

5 = Phi concrete

6 = Pattern live load factor

7 = Utilization factor limit

8 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi steel

Value > 0

5 = Phi concrete

Value > 0

6 = Pattern live load factor

Value >= 0

7 = Utilization factor limit

Value > 0

8 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemCSA\_A23\_3\_94()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("CSA-A23.3-94")

   'get preference item
      ret = SapModel.DesignConcrete.CSA\_A23\_3\_94.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_CSA_A23394}.htm)



## SetOverwrite {Concrete CSA A23394}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/CSA_A23394/SetOverwrite_{Concrete_CSA_A23394}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.CSA\_A23\_3\_94.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, DbMajor

10 = Non-sway moment factor, DbMinor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ductile

2 = Nominal

3 = Ordinary

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Db Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemCSA\_A23\_3\_94()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'createSap2000 object
      Set SapObject= New Sap2000v16.SapObject

   'startSap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel= SapObject.SapModel

   'initialize model
      ret= SapModel.InitializeNewModel

   'create new concrete frame section property
      ret= SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret= SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret= SapModel.DesignConcrete.SetCode("CSA-A23.3-94")

   'set overwrite item
      ret= SapModel.DesignConcrete.CSA\_A23\_3\_94.SetOverwrite("8", 1, 2)

   'closeSap2000
      SapObject.ApplicationExit False
      Set SapModel= Nothing
      Set SapObject= Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_CSA_A23394}.htm)



## SetPreference {Concrete CSA A23394}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/CSA_A23394/SetPreference_{Concrete_CSA_A23394}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.CSA\_A23\_3\_94.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 8, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi steel

5 = Phi concrete

6 = Pattern live load factor

7 = Utilization factor limit

8 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi steel

Value > 0

5 = Phi concrete

Value > 0

6 = Pattern live load factor

Value >= 0

7 = Utilization factor limit

Value > 0

8 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemCSA\_A23\_3\_94()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("CSA-A23.3-94")

   'set preference item
      ret = SapModel.DesignConcrete.CSA\_A23\_3\_94.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_CSA_A23394}.htm)



## GetOverwrite {Concrete Chinese 2010}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Chinese_2010/GetOverwrite_{Concrete_Chinese_2010}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Chinese\_2010.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 18, inclusive, indicating the overwrite item considered.

1 = Seismic design grade

2 = Dual system SMF

3 = MMF

4 = SMF

5 = AFMF

6 = Column location

7 = Transfer beam of column

8 = Corner column seismic modification

9 = Beam gravity neg moment red factor

10 = Unbraced length ratio, Major

11 = Unbraced length ratio, Minor

12 = Effective length factor, K Major

13 = Effective length factor, K Minor

14 = Torsion modification factor

15 = Torsion design factor, Zeta

16 = Concrete cover for closed stirrup

17 = Effective length factor for gravity, K Major

18 = Effective length factor for gravity, K Minor

Value

The value of the considered overwrite item.

1 = Seismic design grade

0 = As specified in preferences

1 = Seismic Super I

2 = Seismic Class I

3 = Seismic Class II

4 = Seismic Class III

5 = Seismic Class IV

6 = NonSeismic

2 = Dual system SMF

Value >= 0; 0 means use program determined value.

3 = MMF

Value >= 0; 0 means use program determined value.

4 = SMF

Value >= 0; 0 means use program determined value.

5 = AFMF

Value >= 0; 0 means use program determined value.

6 = Column Location

1 = Center Column

2 = Side Column

3 = Corner Column

4 = End Column

5 = Individual Column

7 = Transfer beam or column

0 = Program Determined

1 = No

2 = Yes

8 = Corner column seismic modification

0 = Program Determined

1 = No

2 = Yes

9 = Beam gravity neg moment red factor

Value >= 0; 0 means use program determined value.

10 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

11 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

12 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

13 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

14 = Torsion modification factor

Value >= 0; 0 means use program determined value.

15 = Torsion design factor, Zeta

Value >= 0; 0 means use program determined value.

16 = Concrete cover for closed stirrup

Value >= 0; 0 means use program determined value.

17 = Effective length factor for gravity, K Major

        Value >= 0; 0 means use program default value.

18 = Effective length factor for gravity, K Minor

        Value >= 0; 0 means use program default value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemChinese\_2010()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Chinese 2010")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.Chinese\_2010.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.2.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_Chinese_2010}.htm)



## GetPreference {Concrete Chinese 2010}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Chinese_2010/GetPreference_{Concrete_Chinese_2010}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Chinese\_2010.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Importance factor gamma 0

4 = Column design procedure

5 = Seismic design grade

6 = Pattern live load factor

7 = Utilization factor limit

8 = Multi-response case design

9 = Structural system

10 = Is tall building?

11 = Seismic field type

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Importance factor gamma 0

Value > 0

4 = Column design procedure

1 = Appendix F

2 = Simplified

5 = Seismic design grade

1 = Super I

2 = Grade I

3 = Grade II

4 = Grade III

5 = Grade IV

6 = Nonseismic

6 = Pattern live load factor

Value >= 0

7 = Utilization factor limit

Value > 0

8 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

9 = Structural system

      1 = Frame only

      2 = Shearwall only

      3 = Frame-shearwall

      4 = Braced frame only

      5 = Frame-braced frame

10 =  Is tall building?

        0 = No

        1 = Yes

11 =  Seismic field type

        1 = I

        2 = II

        3 = III

        4 = IV

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemChinese\_2010()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Chinese 2010")

   'get preference item
      ret = SapModel.DesignConcrete.Chinese\_2010.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.2.

## See Also

[SetPreference](SetPreference_{Concrete_Chinese_2010}.htm)



## SetOverwrite {Concrete Chinese 2010}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Chinese_2010/SetOverwrite_{Concrete_Chinese_2010}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Chinese\_2010.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 18, inclusive, indicating the overwrite item considered.

1 = Seismic design grade

2 = Dual system SMF

3 = MMF

4 = SMF

5 = AFMF

6 = Column location

7 = Transfer beam of column

8 = Corner column seismic modification

9 = Beam gravity neg moment red factor

10 = Unbraced length ratio, Major

11 = Unbraced length ratio, Minor

12 = Effective length factor, K Major

13 = Effective length factor, K Minor

14 = Torsion modification factor

15 = Torsion design factor, Zeta

16 = Concrete cover for closed stirrup

17 = Effective length factor for gravity, K Major

18 = Effective length factor for gravity, K Minor

Value

The value of the considered overwrite item.

1 = Seismic design grade

0 = As specified in preferences

1 = Seismic Super I

2 = Seismic Class I

3 = Seismic Class II

4 = Seismic Class III

5 = Seismic Class IV

6 = NonSeismic

2 = Dual system SMF

Value >= 0; 0 means use program determined value.

3 = MMF

Value >= 0; 0 means use program determined value.

4 = SMF

Value >= 0; 0 means use program determined value.

5 = AFMF

Value >= 0; 0 means use program determined value.

6 = Column Location

1 = Center Column

2 = Side Column

3 = Corner Column

4 = End Column

5 = Individual Column

7 = Transfer beam or column

0 = Program Determined

1 = No

2 = Yes

8 = Corner column seismic modification

0 = Program Determined

1 = No

2 = Yes

9 = Beam gravity neg moment red factor

Value >= 0; 0 means use program determined value.

10 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

11 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

12 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

13 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

14 = Torsion modification factor

Value >= 0; 0 means use program determined value.

15 = Torsion design factor, Zeta

Value >= 0; 0 means use program determined value.

16 = Concrete cover for closed stirrup

Value >= 0; 0 means use program determined value.

17 = Effective length factor for gravity, K Major

        Value >= 0; 0 means use program default value.

18 = Effective length factor for gravity, K Minor

        Value >= 0; 0 means use program default value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemChinese\_2010()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'createSap2000 object
      Set SapObject= New Sap2000v16.SapObject

   'startSap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel= SapObject.SapModel

   'initialize model
      ret= SapModel.InitializeNewModel

   'create new concrete frame section property
      ret= SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret= SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret= SapModel.DesignConcrete.SetCode("Chinese 2010")

   'set overwrite item
      ret= SapModel.DesignConcrete.Chinese\_2010.SetOverwrite("8", 1, 2)

   'closeSap2000
      SapObject.ApplicationExit False
      Set SapModel= Nothing
      Set SapObject= Nothing
End Sub

## Release Notes

Initial release in version 15.0.2.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Chinese_2010}.htm)



## SetPreference {Concrete Chinese 2010}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Chinese_2010/SetPreference_{Concrete_Chinese_2010}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Chinese\_2010.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Importance factor gamma 0

4 = Column design procedure

5 = Seismic design grade

6 = Pattern live load factor

7 = Utilization factor limit

8 = Multi-response case design

9 = Structural system

10 = Is tall building?

11 = Seismic field type

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Importance factor gamma 0

Value > 0

4 = Column design procedure

1 = Appendix F

2 = Simplified

5 = Seismic design grade

1 = Super I

2 = Grade I

3 = Grade II

4 = Grade III

5 = Grade IV

6 = Nonseismic

6 = Pattern live load factor

Value >= 0

7 = Utilization factor limit

Value > 0

8 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

9 = Structural system

      1 = Frame only

      2 = Shearwall only

      3 = Frame-shearwall

      4 = Braced frame only

      5 = Frame-braced frame

10 =  Is tall building?

        0 = No

        1 = Yes

11 =  Seismic field type

        1 = I

        2 = II

        3 = III

        4 = IV

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemChinese\_2010()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Chinese 2010")

   'set preference item
      ret = SapModel.DesignConcrete.Chinese\_2010.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.2.

## See Also

[GetPreference](GetPreference_{Concrete_Chinese_2010}.htm)



## DeleteResults {Concrete Shell}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/DeleteResults_{Concrete_Shell}.htm`*

# DeleteResults {Concrete Shell}

## Syntax

SapObject.SapModel.DesignConcreteShell.DeleteResults

## VB6 Procedure

Function DeleteResults() As Long

## Parameters

None

## Remarks

This function deletes all concrete shell design results.

The function returns zero if the results are successfully deleted; otherwise it returns a nonzero value.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub DeleteConcreteShellDesignResults()

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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fluid", eLoadPatternType.EarthHydrostatic)

'add point load

Dim LoadValue() As Double

ReDim LoadValue(5)

LoadValue(1) = 10

ret = SapModel.PointObj.SetLoadForce("14", "DEAD", LoadValue)

'add combo

ret = SapModel.RespCombo.Add("COMB1", 1)

ret = SapModel.RespCombo.Add("COMB2", 1)

ret = SapModel.RespCombo.Add("COMB3", 1)

ret = SapModel.RespCombo.Add("COMB4", 1)

'add load case to combo

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.1)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.2)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.3)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.4)

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

Dim RequestName As String

Dim GroupList() As String

Dim ComboList() As String

Dim AutoCombo As Boolean

Dim AutoComboCaseList() As String

Dim NewName As String

Dim NumberRequest As Integer

Dim RequestList() As String

Dim NumberGroup As Integer

Dim NumberCombo As Integer

RequestName = "R1"

ReDim RequestList(1)

RequestList(0) = ""

RequestList(1) = ""

ReDim GroupList(1)

ReDim ComboList(1)

ReDim AutoComboCaseList(2)

GroupList(1) = "GROUP1"

ComboList(1) = "COMB1"

AutoCombo = True

AutoComboCaseList(1) = "DEAD"

AutoComboCaseList(2) = "Fluid"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

NewName = "R11"

ret = SapModel.DesignConcreteShell.DesignRequest.ChangeName(RequestName, NewName)

RequestName = "R2"

GroupList(1) = "GROUP2"

ComboList(1) = "COMB2"

AutoCombo = False

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

RequestName = "R123"

ReDim GroupList(3)

ReDim ComboList(3)

GroupList(1) = "GROUP1"

GroupList(2) = "GROUP2"

GroupList(3) = "GROUP3"

ComboList(1) = "COMB1"

ComboList(2) = "COMB2"

ComboList(3) = "COMB3"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetRequestList(NumberRequest, RequestList)

RequestName = "R123"

ReDim GroupList(0)

ReDim ComboList(0)

ret = SapModel.DesignConcreteShell.DesignRequest.GetGroupList(RequestName, NumberGroup, GroupList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetComboList(RequestName, NumberCombo, ComboList)

ReDim GroupList(2)

GroupList(1) = "GROUP3"

GroupList(2) = "GROUP4"

ret = SapModel.DesignConcreteShell.DesignRequest.SetGroup(RequestName, GroupList)

ReDim ComboList(2)

ComboList(1) = "COMB3"

ComboList(2) = "COMB4"

ret = SapModel.DesignConcreteShell.DesignRequest.SetCombo(RequestName, ComboList)

Dim AutoComboCaseList1() As String

ReDim AutoComboCaseList1(2)

AutoComboCaseList1(1) = "DEAD"

AutoComboCaseList1(2) = "Fluid"

RequestName = "R2"

ret = SapModel.DesignConcreteShell.DesignRequest.SetAutoCombo(RequestName, AutoComboCaseList1)

Dim value As Double

Dim progdet As Boolean

ret = SapModel.DesignConcreteShell.ACI350\_20.SetPreference(5, 0.7)

ret = SapModel.DesignConcreteShell.ACI350\_20.GetPreference(5, value)

ret = SapModel.DesignConcreteShell.ACI350\_20.SetOverwrite("1", 4, 1.345)

ret = SapModel.DesignConcreteShell.ACI350\_20.GetOverwrite("1", 4, value, progdet)

ret = SapModel.DesignConcreteShell.ResetOverwrites

'save model

ret = SapModel.File.Save("C:\CSiAPIexample\x.sdb")

'run model (this will create the analysis model)

ret = SapModel.Analyze.RunAnalysis

'design concrete shell elements

ret = SapModel.DesignConcreteShell.StartDesign

'delete concrete shell design results

ret = SapModel.DesignConcreteShell.DeleteResults

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0.

## See Also



## DeleteResults {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/DeleteResults_{Concrete}.htm`*

# DeleteResults

## Syntax

SapObject.SapModel.DesignConcrete.DeleteResults

## VB6 Procedure

Function DeleteResults() As Long

## Parameters

None

## Remarks

This function deletes all concrete frame design results.

The function returns zero if the results are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteConcreteDesignResults()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'delete concrete design results
      ret = SapModel.DesignConcrete.DeleteResults

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## GetOverwrite {Concrete Eurocode 2-2023}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/EuroCode_2_2023/GetOverwrite_{Concrete_Eurocode_2-2023}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Eurocode\_2\_2023.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 42, inclusive, indicating the overwrite item considered.

1 = Framing type (beam and column)

2 = Live load reduction factor (beam and column)

3 = Unbraced length ratio, Major (beam and column)

4 = Unbraced length ratio, Minor (beam and column)

5 = Effective length factor, Beta Major (column only)

6 = Effective length factor, Beta Minor (column only)

7 = Moment coefficient, Cm Major (not used)

8 = Moment coefficient, Cm Minor (not used)

9 = Nonsway moment factor, Dns Major (not used)

10 = Nonsway moment factor, Dns Minor (not used)

11 = Sway moment factor, Ds Major (not used)

12 = Sway moment factor, Ds Minor (not used)

13 = Correction factor depending on axial load in Nominal Curvature method, Kr Major (beam and column)

14 = Correction factor depending on axial load in Nominal Curvature method, Kr Major (columns only)

15 = Correction factor depending on axial load in Nominal Curvature method, Kr Minor (columns only)

16 = Factor accounting for creep in Nominal Curvature method, Kr Minor (columns only)

17 = Factor accounting for creep in Nominal Curvature method, KPhi Minor (columns only)

18 = Coefficient depending on the distribution of first-order moment in both Nominal Stiffness and Nominal Curvature methods, c\_1/r Major (beam and column)

19 = Coefficient depending on the distribution of first-order moment in both Nominal Stiffness and Nominal Curvature methods, c\_1/r Minor (beam and column)

20 = Factor for contribution of reinforcement, Ks Major (beam and column)

21 = Factor for contribution of reinforcement, Ks Minor (beam and column)

22 = Factor for effects of cracking, creep etc, Kc Major (beam and column)

23 = Factor for effects of cracking, creep etc, Kc Minor (beam and column)

24 = Effective creep coefficient, Phi\_ef (beam and column)

25 = Crack width factor, kw

26 = Coefficient of concrete compressive stress limit, k1

27 = Coefficient of steel tensile stress limit, k3

28 = Exposure class for crack control

29 = Crack width limit

30 = Age at cracking of concrete (days)

31 = Type of cement

32 = Load duration (short or long term)

33 = Longitudinal rebar size top (beam only)

34 = Longitudinal rebar size bottom (beam only)

35 = Is longitudinal rebar ribbed?

36 = Is member braced against sidesway? Braced major? (columns only)

37 = Is member braced against sidesway? Braced minor? (columns only)

38 = Consider minimum eccentricity? (columns only)

39 = Ignore beneficial Pu for beam design? (beams only)

40 = Consider torsion?

41 = Shear compression strut angle's tangent, Tan(theta)

42 = Maximum aggregate size

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Determined

1 = DC High

2 = DC Medium

3 = DC Low

4 = Secondary

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major – only applies to column design

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor – only applies to column design

Value >= 0; 0 means use program determined value.

14 = Correction factor depending on axial load in Nominal Curvature method, Kr  Major

Value >= 0; 0 means use program determined value.

15 = Correction factor depending on axial load in Nominal Curvature method, Kr Minor

Value >= 0; 0 means use program determined value.

16 = Factor accounting for creep in Nominal Curvature method, KPhi Major

Value >= 0; 0 means use program determined value.

17 = Factor accounting for creep in Nominal Curvature method, KPhi Minor

Value >= 0; 0 means use program determined value.

18 = Coefficient depending on the distribution of first-order moment in both Nominal Stiffness and Nominal Curvature methods, c\_1/r Major

Value >= 0; 0 means use program determined value.

19 = Coefficient depending on the distribution of first-order moment in both Nominal Stiffness and Nominal Curvature methods, c\_1/r Minor

Value >= 0; 0 means use program determined value.

24 = Effective creep coefficient, Phi\_ef

Value >= 0; 0 means use program determined value.

25 = Crack width factor, kw

Value >= 0; 0 means use program determined value.

26 = Coefficient of concrete compressive stress limit, k1

Value >=0; 0 means use program determined value.

27 = Coefficient of steel tensile stress limit, k3

Value >= 0; 0 means use program determined value.

28 = Exposure class for crack control

0 = Program Determined

1 = X0

2 = XC1

3 = XC2

4 = XC3

5 = XC4

6 = XD1

7 = XD2

8 = XD3

9 = XS1

10 = XS2

11 = XS3

12 = XF1

13 = XF2

14 = XF3

15 = XF4

29 = Crack width limit

Value >= 0; 0 means use program determined value.

30 = Age at cracking of concrete, days

Value >= 0; 0 means use program determined value.

31 = Type of cement

0 = Program Determined

1 = Class R

2 = Class N

3 = Class S

32 = Loading duration

0 = Program Determined

1 = Short term

2 = Long term

33 = Longitudinal rebar size top

       Value is the index in the list of the rebar defined in the Reinforcing Bar Sizes form.

34 = Longitudinal rebar size bottom

       Value is the index in the list of the rebar defined in the Reinforcing Bar Sizes form.

35 = Is longitudinal rebar ribbed?

0 = No

Any other value = Yes

36 = Is braced against sidesway?  Braced major?

0 = Program Determined

1 = No

2 = Yes

37 = Is braced against sidesway?  Braced minor?

0 = Program Determined

1 = No

2 = Yes

38 = Consider minimum eccentricity?

0 = No

Any other value = Yes

39 = Ignore beneficial Pu for beam design?

0 = No

Any other value = Yes

40 = Consider torsion?

0 = No

Any other value = Yes

41 = Shear compression strut angle's tangent, Tan(theta)

Value >= 0; 0 means use program determined value.

42 = Maximum aggregate size

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemEurocode\_2\_2023()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Eurocode 2-2023")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.Eurocode\_2\_2023.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 27.0.0

## See Also

[SetOverwrite](SetOverwrite{Concrete_Eurocode_2-2023}.htm)



## GetPreference {Concrete Eurocode 2-2023}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/EuroCode_2_2023/GetPreference{Concrete_Eurocode_2-2023}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Eurocode\_2\_2023.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 28, inclusive, indicating the preference item considered.

1 = Country

2 = Combos equation

3 = Second order method

4 = Number of interaction curves

5 = Number of interaction points

6 = Consider minimum eccentricity

7 = Theta0

8 = Gamma steel

9 = Gamma concrete

14 = Pattern live load factor

15 = Utilization factor limit

16 = Multi-response case design

17 = Reliability Class

18 = Gamma concrete modulus

20 = Consider Torsion

21 = Longitudinal rebar size top

22 = Longitudinal rebar size bottom

23 = Is longitudinal rebar ribbed?

24 = Gamma shear

25 = kTC

26 = kTT

27 = Framing Type

28 = Ignore Beneficial Pu for Beam Design?

Value

The value of the considered preference item.

1 = Country

      1 = CEN Default

      2 = United Kingdom

      3 = Slovenia

      5 = Norway

      6 = Singapore

      7 = Sweden

      8 = Finland

      9 = Denmark

    10 = Portugal

    11 = Germany

    12 = Poland

    13 = Ireland

2 = Combos equation

      1 = Eq. 6.10

      2 = Max of Eqs. 6.10a and 6.10b

3 = Second order method

      1 = Nominal stiffness

      2 = Nominal curvature

      3 = None

4 = Number of interaction curves

Value >= 4 and divisible by 4

5 = Number of interaction points

Value >= 5 and odd

6 = Consider minimum eccentricity

0 = No

Any other value = Yes

7 = Theta0

Value > 0

8 = Gamma steel

Value > 0

9 = Gamma concrete

Value > 0

10 = AlphaCC

  Value > 0

11 = AlphaCT

  Value > 0

12 = AlphaLCC

  Value > 0

13 = AlphaLCT

  Value > 0

14 = Pattern live load factor

  Value >= 0

15 = Utilization factor limit

  Value > 0

16 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

17 = Reliability Class

 1 = Class 1

 2 = Class 2

  3 = Class 3

                        18 = GammacE

                             Value > 0

19 = Alphae (not used)

                             Value > 0

20 = Consider torsion

0 = No

Any other value = Yes

21 = Longitudinal rebar size top

      Value is the index in the list of the rebar defined in the Reinforcing Bar Sizes form

22 = Longitudinal rebar size bottom

      Value is the index in the list of the rebar defined in the Reinforcing Bar Sizes form

23 = Is longitudinal rebar ribbed?

0 = No

Any other value = Yes

24 = Gamma shear

  Value > 0

25 = kTC

  Value > 0

26 = kTT

  Value > 0

27 = Design for B/C capacity ratio

0 = No

Any other value = Yes

28 = Ignore Beneficial Pu for Beam Design?

0 = No

Any other value = Yes

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemEurocode\_2\_2023()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Eurocode 2-2023")

   'get preference item
      ret = SapModel.DesignConcrete.Eurocode\_2\_2023.GetPreference(5, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 27.0.0

## See Also

[SetPreference](SetPreference_{Concrete_Eurocode_2-2023}.htm)



## SetOverwrite{Concrete Eurocode 2-2023}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/EuroCode_2_2023/SetOverwrite{Concrete_Eurocode_2-2023}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Eurocode\_2\_2023.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 42, inclusive, indicating the overwrite item considered.

1 = Framing type (beam and column)

2 = Live load reduction factor (beam and column)

3 = Unbraced length ratio, Major (beam and column)

4 = Unbraced length ratio, Minor (beam and column)

5 = Effective length factor, Beta Major (columns only)

6 = Effective length factor, Beta Minor (columns only)

14 = Correction factor depending on axial load in Nominal Curvature method, Kr Major (columns only)

15 = Correction factor depending on axial load in Nominal Curvature method, Kr Minor (columns only)

16 = Factor accounting for creep in Nominal Curvature method, Kr Minor (columns only)

17 = Factor accounting for creep in Nominal Curvature method, KPhi Minor (columns only)

18 = Coefficient depending on the distribution of first-order moment in both Nominal Stiffness and Nominal Curvature methods, c\_1/r Major (columns only)

19 = Coefficient depending on the distribution of first-order moment in both Nominal Stiffness and Nominal Curvature methods, c\_1/r Minor (columns only)

24 = Effective creep coefficient, Phi\_ef (beam and column)

25 = Crack width factor, kw

26 = Coefficient of concrete compressive stress limit, k1

27 = Coefficient of steel tensile stress limit, k3

28 = Exposure class for crack control

29 = Crack width limit

30 = Age at cracking of concrete (days)

31 = Type of cement

32 = Load duration (short or long term)

33 = Longitudinal rebar size top (beams only)

34 = Longitudinal rebar size bottom (beams only)

35 = Is longitudinal rebar ribbed?

36 = Is member braced against sidesway? Braced major? (columns only)

37 = Is member braced against sidesway? Braced minor? (columns only)

38 = Consider minimum eccentricity? (columns only)

39 = Ignore beneficial Pu for beam design? (beams only)

40 = Consider torsion?

41 = Shear compression strut angle's tangent, Tan(theta)

42 = Maximum aggregate size

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Determined

1 = DC High

2 = DC Medium

3 = DC Low

4 = Secondary

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major – only applies to column design

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor – only applies to column design

Value >= 0; 0 means use program determined value.

14 = Correction factor depending on axial load in Nominal Curvature method, Kr  Major

Value >= 0; 0 means use program determined value.

15 = Correction factor depending on axial load in Nominal Curvature method, Kr Minor

Value >= 0; 0 means use program determined value.

16 = Factor accounting for creep in Nominal Curvature method, KPhi Major

Value >= 0; 0 means use program determined value.

17 = Factor accounting for creep in Nominal Curvature method, KPhi Minor

Value >= 0; 0 means use program determined value.

18 = Coefficient depending on the distribution of first-order moment in both Nominal Stiffness and Nominal Curvature methods, c\_1/r Major

Value >= 0; 0 means use program determined value.

19 = Coefficient depending on the distribution of first-order moment in both Nominal Stiffness and Nominal Curvature methods, c\_1/r Minor

Value >= 0; 0 means use program determined value.

24 = Effective creep coefficient, Phi\_ef

Value >= 0; 0 means use program determined value.

25 = Crack width factor, kw

Value >= 0; 0 means use program determined value.

26 = Coefficient of concrete compressive stress limit, k1

Value >=0; 0 means use program determined value.

27 = Coefficient of steel tensile stress limit, k3

Value >= 0; 0 means use program determined value.

28 = Exposure class for crack control

0 = Program Determined

1 = X0

2 = XC1

3 = XC2

4 = XC3

5 = XC4

6 = XD1

7 = XD2

8 = XD3

9 = XS1

10 = XS2

11 = XS3

12 = XF1

13 = XF2

14 = XF3

15 = XF4

29 = Crack width limit

Value >= 0; 0 means use program determined value.

30 = Age at cracking of concrete, days

Value >= 0; 0 means use program determined value.

31 = Type of cement

0 = Program Determined

1 = Class R

2 = Class N

3 = Class S

32 = Loading duration

0 = Program Determined

1 = Short term

2 = Long term

33 = Longitudinal rebar size top

       Value is the index in the list of the rebar defined in the Reinforcing Bar Sizes form.

34 = Longitudinal rebar size bottom

       Value is the index in the list of the rebar defined in the Reinforcing Bar Sizes form.

35 = Is longitudinal rebar ribbed?

0 = No

Any other value = Yes

36 = Is braced against sidesway?  Braced major?

0 = Program Determined

1 = No

2 = Yes

37 = Is braced against sidesway?  Braced minor?

0 = Program Determined

1 = No

2 = Yes

38 = Consider minimum eccentricity?

0 = No

Any other value = Yes

39 = Ignore beneficial Pu for beam design?

0 = No

Any other value = Yes

40 = Consider torsion?

0 = No

Any other value = Yes

41 = Shear compression strut angle's tangent, Tan(theta)

      Value >= 0; 0 means use program determined value.

42 = Maximum aggregate size

       Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemEurocode\_2\_2023()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Eurocode 2-2023")

   'set overwrite item
      ret = SapModel.DesignConcrete.Eurocode\_2\_2023.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 27.0.0

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Eurocode_2-2023}.htm)



## SetPreference {Concrete Eurocode 2-2023}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/EuroCode_2_2023/SetPreference_{Concrete_Eurocode_2-2023}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Eurocode\_2\_2023.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 28, inclusive, indicating the preference item considered.

1 = Country

2 = Combos equation

3 = Second order method

4 = Number of interaction curves

5 = Number of interaction points

6 = Consider minimum eccentricity

7 = Theta0

8 = Gamma steel

9 = Gamma concrete

14 = Pattern live load factor

15 = Utilization factor limit

16 = Multi-response case design

17 = Reliability Class

18 = Gamma concrete modulus

20 = Consider Torsion

21 = Longitudinal rebar size top

22 = Longitudinal rebar size bottom

23 = Is longitudinal rebar ribbed?

24 = Gamma shear

25 = kTC

26 = kTT

27 = Framing type

28 = Ignore Beneficial Pu for Beam Design?

Value

The value of the considered preference item.

1 = Country

      1 = CEN Default

      2 = United Kingdom

      3 = Slovenia

      5 = Norway

      6 = Singapore

      7 = Sweden

      8 = Finland

      9 = Denmark

    10 = Portugal

    11 = Germany

    12 = Poland

    13 = Ireland

2 = Combos equation

      1 = Eq. 6.10

      2 = Max of Eqs. 6.10a and 6.10b

3 = Second order method

      1 = Nominal stiffness

      2 = Nominal curvature

      3 = None

4 = Number of interaction curves

Value >= 4 and divisible by 4

5 = Number of interaction points

Value >= 5 and odd

6 = Consider minimum eccentricity

0 = No

Any other value = Yes

7 = Theta0

Value > 0

8 = Gamma steel

Value > 0

9 = Gamma concrete

Value > 0

14 = Pattern live load factor

  Value >= 0

15 = Utilization factor limit

  Value > 0

16 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

17 = Reliability Class

 1 = Class 1

 2 = Class 2

 3 = Class 3

                       18 = GammacE

                             Value > 0

20 = Consider torsion

0 = No

Any other value = Yes

21 = Longitudinal rebar size top

      Value is the index in the list of the rebar defined in the Reinforcing Bar Sizes form

22 = Longitudinal rebar size bottom

      Value is the index in the list of the rebar defined in the Reinforcing Bar Sizes form

23 = Is longitudinal rebar ribbed?

0 = No

Any other value = Yes

24 = Gamma shear

  Value > 0

25 = kTC

  Value > 0

26 = kTT

  Value > 0

27 = Framing type

  0 = Program Determined

  1 = DC High

  2 = DC Medium

  3 = DC Low

  4 = Secondary

28 = Ignore Beneficial Pu for Beam Design?

0 = No

Any other value = Yes

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemEurocode\_2\_2023()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True,"R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Eurocode 2-2023")

   'set preference item
      ret = SapModel.DesignConcrete.Eurocode\_2\_2023.SetPreference(5, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 27.0.0

## See Also

[GetPreference](GetPreference{Concrete_Eurocode_2-2023}.htm)



## GetOverwrite {Concrete Eurocode 2-2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2-2004/GetOverwrite_{Concrete_Eurocode_2-2004}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Eurocode\_2\_2004.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design
procedure.

Item

This is an integer between 1 and 37, inclusive, indicating
the overwrite item considered.

1 = Framing type (beam
and column)

2 = Live load reduction
factor (beam and column)

3 = Unbraced length ratio,
Major (beam and column)

4 = Unbraced length ratio,
Minor (beam and column)

5 = Effective length factor,
Beta Major (column only)

6 = Effective length factor,
Beta Minor (column only)

7 = Moment coefficient,
Cm Major (not used)

8 = Moment coefficient,
Cm Minor (not used)

9 = Nonsway moment factor,
Dns Major (not used)

10 = Nonsway moment factor,
Dns Minor (not used)

11 = Sway moment factor,
Ds Major (not used)

12 = Sway moment factor,
Ds Minor (not used)

13 = Correction factor
depending on axial load in Nominal Curvature method, Kr Major (beam and
column)

14 = Correction factor
depending on axial load in Nominal Curvature method, KPhi Major (beam
and column)

15 = Shear compressive
strut angle, TanTheta (beam only)

16 = Factor accounting
for creep in Nominal Curvature method, Kr Minor (beam and column)

17 = Factor accounting
for creep in Nominal Curvature method, KPhi Minor (beam and column)

18 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Major (beam and column)

19 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Minor (beam and column)

20 = Factor for contribution
of reinforcement, Ks Major (beam and column)

21 = Factor for contribution
of reinforcement, Ks Minor (beam and column)

22 = Factor for effects
of cracking, creep etc, Kc Major (beam and column)

23 = Factor for effects
of cracking, creep etc, Kc Minor (beam and column)

24 = Effective creep
coefficient, Phief (beam and column)

25 = Consider torsion (beam only)

26 = Coefficient of concrete
compressive stress limit, k1

27 = Coefficient of steel
tensile stress limit, k3

28 = Exposure class for
crack control

29 = Limiting crack width

30 = Age at cracking of
concrete, days

31 = Type of cement

32 = Load duration

33 = Longitudinal rebar
size top (beam only)

34 = Longitudinal rebar
size bottom (beam only)

35 = Is longitudinal rebar
ribbed?

36 = Is braced about major?

37 = Is braced about minor?

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Determined

1 = DC High

2 = DC Medium

3 = DC Low

4 = Secondary

2 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

3 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value.

4 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value.

5 = Effective length factor,
Beta Major – only applies to column design

Value >= 0; 0 means
use program determined value.

6 = Effective length factor,
Beta Minor – only applies to column design

Value >= 0; 0 means
use program determined value.

7 = Moment coefficient,
Cm Major – not used

Value >= 0; 0 means
use program determined value.

8 = Moment coefficient,
Cm Minor – not used

Value >= 0; 0 means
use program determined value.

9 = Nonsway moment factor,
Dns Major – not used

Value >= 0; 0 means
use program determined value.

10 = Nonsway moment factor,
Dns Minor – not used

  Value >=
0; 0 means use program determined value.

11 = Sway moment factor,
Ds Major – not used

  Value >=
0; 0 means use program determined value.

12 = Sway moment factor,
Ds Minor – not used

  Value >=
0; 0 means use program determined value.

13
= Correction factor depending on axial load in Nominal Curvature method,
Kr Major

Value >= 0; 0 means
use program determined value.

14 = Correction factor
depending on axial load in Nominal Curvature method, KPhi Major

Value >= 0; 0 means
use program determined value.

15 = Shear compressive
strut angle, TanTheta

Value >= 0; 0 means
use program determined value.

16 = Factor accounting
for creep in Nominal Curvature method, Kr Minor

Value >= 0; 0 means
use program determined value.

17 = Factor accounting
for creep in Nominal Curvature method, KPhi Minor

Value >= 0; 0 means
use program determined value.

18 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Major

Value >= 0; 0 means
use program determined value.

19 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Minor

Value >= 0; 0 means
use program determined value.

20 = Factor for contribution
of reinforcement, Ks Major

Value >= 0; 0 means
use program determined value.

21 = Factor for contribution
of reinforcement, Ks Minor

Value >= 0; 0 means
use program determined value.

22 = Factor for effects
of cracking, creep etc, Kc Major

Value >= 0; 0 means
use program determined value.

23 = Factor for effects
of cracking, creep etc, Kc Minor

Value >= 0; 0 means
use program determined value.

24 = Effective creep
coefficient, Phief

Value >= 0; 0 means
use program determined value.

25 = Consider torsion

0 = No

Any other value = Yes

26 = Coefficient of concrete
compressive stress limit, k1

Value >=0; 0 means use
program determined value.

27 = Coefficient of steel
tensile stress limit, k3

Value >= 0; 0 means
use program determined value.

28 = Exposure class for
crack control

0 = Program Determined

1 = X0

2 = XC1

3 = XC2

4 = XC3

5 = XC4

6 = XD1

7 = XD2

8 = XS1

9 = XS2

10 = XS3

29 = Limiting crack width

Value >= 0; 0 means
use program determined value.

30 = Age at cracking of
concrete, days

Value >= 0; 0 means
use program determined value.

31 = Type of cement

0 = Program Determined

1 = Class R

2 = Class N

3 = Class S

32 = Loading duration

0 = Program Determined

1 = Short term

2 = Long term

33
= Longitudinal rebar size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

34 = Longitudinal rebar
size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

35 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

36 = Is braced about major?

0
= Program Determined

1 = No

2 = Yes

37 = Is braced about minor?

0
= Program Determined

1 = No

2 = Yes

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a concrete design
overwrite item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemEurocode\_2\_2004()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Eurocode
2-2004")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.Eurocode\_2\_2004.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.0.0.

Added items 16 – 24 in v21.1.0

Changed Description for items 1 and 5 through 12 in
v23.4.0.

Added item 25 in v23.4.0

Added items 26 through 35 in v24.2.0

Added items 36 and 37 in v25.1.0

## See Also

[SetOverwrite](SetOverwrite{Concrete_Eurocode_2-2004}.htm)



## GetOverwrite {Concrete Shell Design Eurocode 2-2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2-2004/GetOverwrite_{Concrete_Shell_Design_Eurocode_2-2004}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcreteShell.Eurocode\_2\_2004.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete shell design procedure.

Item

This is an integer between 1 and 5, inclusive, indicating the overwrite item considered.

1 = Number rebar layer

2 = Concrete cover to center of top rebar layer in direction 1

3 = Concrete cover to center of top rebar layer in direction 2

4 = Concrete cover to center of bottom rebar layer in direction 1

5 = Concrete cover to center of bottom rebar layer in direction 2

Value

The value of the considered overwrite item.

1 = Number rebar layer

0 = Program Default

1 = 1 layer

2 = 2 layers

2 = Concrete cover to center of top rebar layer in direction 1

Value >= 0; 0 means value taken from shell section definition.

3 = Concrete cover to center of top rebar layer in direction 2

Value >= 0; 0 means value taken from shell section definition.

4 = Concrete cover to center of bottom rebar layer in direction 1

Value >= 0; 0 means value taken from shell section definition.

5 = Concrete cover to center of bottom rebar layer in direction 2

Value >= 0; 0 value taken from shell section definition.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcretShellDesignOverwriteItemEurocode\_2\_2004()

   'dimension variables
Dim SapObject as cOAPI
Dim SapModel As cSapModel
Dim ret As Long
Dim Value As Double
Dim ProgDet As Boolean

'create Sap2000 object
Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

'start Sap2000 application
SapObject.ApplicationStart

'create SapModel object
Set SapModel = SapObject.SapModel

'initialize model

      ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

   'create a wall model from template

      ret = SapModel.File.NewWall(6, 4, 6, 4)

'set concrete shell design code
ret = SapModel.DesignConcreteShell.SetCode("Eurocode 2 2004")

   'set concrete shell design overwrite

      ret = SapModel.DesignConcreteShell.Eurocode\_2\_2004.SetOverwrite("1", 4, 1.345)

'get overwrite item
ret = SapModel.DesignConcreteShell.Eurocode\_2\_2004.GetOverwrite("1", 4, value, progdet)

'close Sap2000
SapObject.ApplicationExit False
Set SapModel = Nothing
Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.2.0.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_Shell_Design_Eurocode_2004}.htm)



## GetPreference {Concrete Shell Design Eurocode 2-2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2-2004/GetPreference_{Concrete_Shell_Design_Eurocode_2-2004}.htm`*

# GetPreference (Concrete Shell Design)

## Syntax

SapObject.SapModel.DesignConcreteShell.Eurocode\_2\_2004.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Country

2 = Gamma steel

3 = Gamma concrete

4 = AlphaCC

5 = AlphaCT

6 = Crack condition

7 = Shear design method

8 = Cotangent of the angle of concrete compressive strut

9 = Add tensile force due to shear

**Value**

The value of the considered preference item.

1 = Country

      1 = CEN Default

      2 = United Kingdom

      3 = Slovenia

      5 = Norway

      6 = Singapore

      7 = Sweden

      8 = Finland

      9 = Denmark

    10 = Portugal

    11 = Germany

    12 = Poland

    13 = Ireland

2 = Gamma steel

Value > 0

3 = Gamma concrete

Value > 0

4 = AlphaCC

  Value > 0

5 = AlphaCT

  Value > 0

6 = Crack condition

      1 = Program Determined - the program will perform the calculation according to EN 1992-2:2005 Annex LL (107) to check whether the shell elements are uncracked or cracked

2 = Cracked – the program will assume that the shell elements are cracked without performing the calculation according to EN 1992-2:2005 Annex LL (107)

7 = Shear design method

      1 = Method 1 – considers increasing longitudinal reinforcement to increase concrete shear capacity up to the allowable limit. If insufficient, shear reinforcement will be added

2 = Method 2 – determines required shear reinforcement without considering to increase longitudinal reinforcement

8 = Cotangent of the angle of concrete compressive strut

1 <= Value <= 3.0 for Germany

1 <= Value <= 2.0 for Poland

1 <= Value <= 2.5 for other countries

9 = Add tensile force due to shear

      0 = No

      Any Other Value = Yes

## Remarks

This function retrieves the value of a concrete shell design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteShellDesignPreferenceItemEurocode\_2\_2004()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create blank model
       ret = SapModel.File.NewBlank()

   'set concrete design code
      ret = SapModel.DesignConcreteShell.SetCode("Eurocode 2-2004")

   'get preference item
      ret = SapModel.DesignConcreteShell.Eurocode\_2\_2004.GetPreference(3, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.0.0.

Added items 5 through 8 in v24.1.0.

Added item 9 in version 25.2.0.

## See Also

[SetPreference (Concrete Shell EC-2)](GetPreference_{Concrete_Shell_Design_Eurocode_2-2004}.htm)



## GetPreference {Concrete Eurocode 2-2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2-2004/GetPreference{Concrete_Eurocode_2-2004}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Eurocode\_2\_2004.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 23, inclusive, indicating
the preference item considered.

1 = Country

2 = Combos equation

3 = Second order method

4 = Number of interaction
curves

5 = Number of interaction
points

6
= Consider minimum eccentricity

7
= Theta0

8
= Gamma steel

9 = Gamma concrete

10 = AlphaCC

11 = AlphaCT

12 = AlphaLCC

13 = AlphaLCT

14 = Pattern live load
factor

15 = Utilization factor
limit

16 = Multi-response case design

17 = Reliability Class

18 = GammacE

19 = Alphae (not used)

20 = Consider Torsion

21 = Longitudinal rebar
size top

22 = Longitudinal rebar
size bottom

23 = Is longitudinal rebar
ribbed?

Value

The value of the considered preference item.

1 = Country

      1
= CEN Default

      2
= United Kingdom

      3
= Slovenia

      5
= Norway

      6
= Singapore

      7
= Sweden

      8
= Finland

      9
= Denmark

    10
= Portugal

    11
= Germany

    12
= Poland

    13
= Ireland

2 = Combos equation

      1
= Eq. 6.10

      2
= Max of Eqs. 6.10a and 6.10b

3 = Second order method

      1
= Nominal stiffness

      2
= Nominal curvature

      3
= None

4 = Number of interaction
curves

Value >= 4 and divisible
by 4

5 = Number of interaction
points

Value >= 5 and odd

6 = Consider minimum eccentricity

0 = No

Any other value = Yes

7
= Theta0

Value
> 0

8
= Gamma steel

Value
> 0

9
= Gamma concrete

Value > 0

10 = AlphaCC

  Value >
0

11 = AlphaCT

  Value >
0

12 = AlphaLCC

  Value >
0

13 = AlphaLCT

  Value >
0

14 = Pattern live load
factor

  Value >=
0

15 = Utilization factor
limit

  Value >
0

16 = Multi-response case
design

  1 = Envelopes

  2 = Step-by-step

  3 = Last
step

  4 = Envelopes
-- All

  5 = Step-by-step
-- All

17
= Reliability Class

 1 = Class 1

 2 = Class 2

  3 = Class
3

                       18
= GammacE

                             Value
> 0

19 = Alphae (not used)

                             Value
> 0

20 = Consider torsion

0 = No

Any
other value = Yes

21 = Longitudinal rebar
size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

22 = Longitudinal rebar
size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

23 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

## Remarks

This function retrieves the value of a concrete design
preference item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemEurocode\_2\_2004()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Eurocode
2-2004")

   'get preference item
      ret = SapModel.DesignConcrete.Eurocode\_2\_2004.GetPreference(5,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.0.0.

Added Norway as a Country
parameter in version 14.1.0.

Added Reliability Class parameter and added Sweden,
Finland, and Denmark as Country parameters in version 14.2.2.

Added Portugal and Germany as Country parameters in
SAP2000 Version 15.0.0.

Changed Time history design item to Multi-response case
design and added additional values in version 15.0.1.

Added items 18 – 19 in v21.1.0

Added item 20 in v23.4.0.

Changed item 19 to Not Used in v24.2.0

Added items 21 – 23 in v24.2.0

## See Also

[SetPreference](SetPreference_{Concrete_Eurocode_2-2004}.htm)



## SetOverwrite {Concrete Shell Design Eurocode 2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2-2004/SetOverwrite_{Concrete_Shell_Design_Eurocode_2004}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcreteShell.Eurocode\_2\_2004.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object with a concrete shell design procedure.

Item

This is an integer between 1 and 5, inclusive, indicating the overwrite item considered.

1 = Number rebar layer

2 = Concrete cover to center of top rebar layer in direction 1

3 = Concrete cover to center of top rebar layer in direction 2

4 = Concrete cover to center of bottom rebar layer in direction 1

5 = Concrete cover to center of bottom rebar layer in direction 2

Value

The value of the considered overwrite item.

1 = Number rebar layer

0 = Program Default

1 = 1 layer

2 = 2 layers

2 = Concrete cover to center of top rebar layer in direction 1

Value >= 0; 0 means value taken from shell section definition.

3 = Concrete cover to center of top rebar layer in direction 2

Value >= 0; 0 means value taken from shell section definition.

4 = Concrete cover to center of bottom rebar layer in direction 1

Value >= 0; 0 means value taken from shell section definition.

5 = Concrete cover to center of bottom rebar layer in direction 2

Value >= 0; 0 value taken from shell section definition

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteShellDesignOverwriteItemEurocode\_2\_2004()
'dimension variables
Dim SapObject as cOAPI
Dim SapModel As cSapModel
Dim ret As Long

      Dim value As Double

      Dim progdet As Boolean

'create Sap2000 object
Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

'start Sap2000 application
SapObject.ApplicationStart

'create SapModel object
Set SapModel = SapObject.SapModel

'initialize model

      ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

   'create a wall model from template

      ret = SapModel.File.NewWall(6, 4, 6, 4)

'set concrete shell design code
ret = SapModel.DesignConcreteShell.SetCode("Eurocode 2 2004")

   'set concrete shell design overwrite

      ret = SapModel.DesignConcreteShell.Eurocode\_2\_2004.SetOverwrite("1", 4, 1.345)

'get overwrite item
ret = SapModel.DesignConcreteShell.Eurocode\_2\_2004.GetOverwrite("1", 4, value, progdet)

'close Sap2000
SapObject.ApplicationExit(False)
Set SapModel = Nothing
Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.2.0.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Shell_Design_Eurocode_2-2004}.htm)



## SetOverwrite{Concrete Eurocode 2-2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2-2004/SetOverwrite{Concrete_Eurocode_2-2004}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Eurocode\_2\_2004.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 37, inclusive, indicating
the overwrite item considered.

1 = Framing type (beam
and column)

2 = Live load reduction
factor (beam and column)

3 = Unbraced length ratio,
Major (beam and column)

4 = Unbraced length ratio,
Minor (beam and column)

5 = Effective length factor,
Beta Major (column only)

6 = Effective length factor,
Beta Minor (column only)

7 = Moment coefficient,
Cm Major (not used)

8 = Moment coefficient,
Cm Minor (not used)

9 = Nonsway moment factor,
Dns Major (not used)

10 = Nonsway moment factor,
Dns Minor (not used)

11 = Sway moment factor,
Ds Major (not used)

12 = Sway moment factor,
Ds Minor (not used)

13 = Correction factor
depending on axial load in Nominal Curvature method, Kr Major (beam and
column)

14 = Correction factor
depending on axial load in Nominal Curvature method, KPhi Major (beam
and column)

15 = Shear compressive
strut angle, TanTheta (beam only)

16 = Factor accounting
for creep in Nominal Curvature method, Kr Minor (beam and column)

17 = Factor accounting
for creep in Nominal Curvature method, KPhi Minor (beam and column)

18 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Major (beam and column)

19 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Minor (beam and column)

20 = Factor for contribution
of reinforcement, Ks Major (beam and column)

21 = Factor for contribution
of reinforcement, Ks Minor (beam and column)

22 = Factor for effects
of cracking, creep etc, Kc Major (beam and column)

23 = Factor for effects
of cracking, creep etc, Kc Minor (beam and column)

24 = Effective creep
coefficient, Phief (beam and column)

25 = Consider torsion (beam only)

26
= Coefficient of concrete compressive stress limit, k1

27 = Coefficient of steel
tensile stress limit, k3

28 = Exposure class for
crack control

29 = Limiting crack width

30 = Age at cracking of
concrete, days

31 = Type of cement

32 = Load duration

33 = Longitudinal rebar
size top (beam only)

34 = Longitudinal rebar
size bottom (beam only)

35 = Is longitudinal rebar
ribbed?

36 = Is braced about major?

37 = Is braced about minor?

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Determined

1 = DC High

2 = DC Medium

3 = DC Low

4 = Secondary

2 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

3 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value.

4 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value.

5 = Effective length factor,
Beta Major – only applies to column design

Value >= 0; 0 means
use program determined value.

6 = Effective length factor,
Beta Minor – only applies to column design

Value >= 0; 0 means
use program determined value.

7 = Moment coefficient,
Cm Major – not used

Value >= 0; 0 means
use program determined value.

8 = Moment coefficient,
Cm Minor – not used

Value >= 0; 0 means
use program determined value.

9 = Nonsway moment factor,
Dns Major – not used

Value >= 0; 0 means
use program determined value.

10 = Nonsway moment factor,
Dns Minor – not used

  Value >=
0; 0 means use program determined value.

11 = Sway moment factor,
Ds Major – not used

  Value >=
0; 0 means use program determined value.

12 = Sway moment factor,
Ds Minor – not used

  Value >=
0; 0 means use program determined value.

13
= Correction factor depending on axial load in Nominal Curvature method,
Kr Major

Value >= 0; 0 means
use program determined value.

14 = Correction factor
depending on axial load in Nominal Curvature method, KPhi Major

Value >= 0; 0 means
use program determined value.

15 = Shear compressive
strut angle, TanTheta

Value >= 0; 0 means
use program determined value.

16 = Factor accounting
for creep in Nominal Curvature method, Kr Minor

Value >= 0; 0 means
use program determined value.

17 = Factor accounting
for creep in Nominal Curvature method, KPhi Minor

Value >= 0; 0 means
use program determined value.

18 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Major

Value >= 0; 0 means
use program determined value.

19 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Minor

Value >= 0; 0 means
use program determined value.

20 = Factor for contribution
of reinforcement, Ks Major

Value >= 0; 0 means
use program determined value.

21 = Factor for contribution
of reinforcement, Ks Minor

Value >= 0; 0 means
use program determined value.

22 = Factor for effects
of cracking, creep etc, Kc Major

Value >= 0; 0 means
use program determined value.

23 = Factor for effects
of cracking, creep etc, Kc Minor

Value >= 0; 0 means
use program determined value.

24 = Effective creep
coefficient, Phief

Value >= 0; 0 means
use program determined value.

25 = Consider torsion

0 = No

Any other value = Yes

26
= Coefficient of concrete compressive stress limit, k1

Value >=0; 0 means use
program determined value.

27 = Coefficient of steel
tensile stress limit, k3

Value >= 0; 0 means
use program determined value.

28 = Exposure class for
crack control

0 = Program Determined

1 = X0

2 = XC1

3 = XC2

4 = XC3

5 = XC4

6 = XD1

7 = XD2

8 = XS1

9 = XS2

10 = XS3

29 = Limiting crack width

Value >= 0; 0 means
use program determined value.

30 = Age at cracking of
concrete, days

Value >= 0; 0 means
use program determined value.

31 = Type of cement

0 = Program Determined

1 = Class R

2 = Class N

3 = Class S

32 = Loading duration

0 = Program Determined

1 = Short term

2 = Long term

33
= Longitudinal rebar size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

34 = Longitudinal rebar
size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

35 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

36 = Is braced about major?

0
= Program Determined

1 = No

2 = Yes

37 = Is braced about minor?

0
= Program Determined

1 = No

2 = Yes

ItemType

This is one of the following items in the eItemType
enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the
frame object specified by the Name item.

If this item is Group, the assignment is made to all
frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made
to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite
item.

The function returns zero if the item is successfully
set, otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemEurocode\_2\_2004()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Eurocode
2-2004")

   'set overwrite item
      ret = SapModel.DesignConcrete.Eurocode\_2\_2004.SetOverwrite("8",
1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.0.0.

Added items 16 – 24 in v21.1.0

Changed Description for items 1 and 5 through 12 in
v23.4.0.

Added item 25 in v23.4.0

Added items 26 through 35 in v24.2.0

Added items 36 and 37 in v25.1.0

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Eurocode_2-2004}.htm)



## SetPreference {Concrete Eurocode 2-2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2-2004/SetPreference_{Concrete_Eurocode_2-2004}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Eurocode\_2\_2004.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 23, inclusive, indicating
the preference item considered.

1 = Country

2 = Combos equation

3 = Second order method

4 = Number of interaction
curves

5 = Number of interaction
points

6 = Consider minimum eccentricity

7 = Theta0

8 = Gamma steel

9 = Gamma concrete

10 = AlphaCC

11 = AlphaCT

12 = AlphaLCC

13 = AlphaLCT

14 = Pattern live load
factor

15 = Utilization factor
limit

16 = Multi-response case design

17 = Reliability Class

18 = GammacE

19 = Alphae
(not used)

20 = Consider Torsion

21 = Longitudinal rebar
size top

22 = Longitudinal rebar
size bottom

23 = Is longitudinal rebar
ribbed?

Value

The value of the considered preference item.

1 = Country

      1
= CEN Default

      2
= United Kingdom

      3
= Slovenia

      5
= Norway

      6
= Singapore

      7
= Sweden

      8
= Finland

      9
= Denmark

    10
= Portugal

    11
= Germany

    12
= Poland

    13
= Ireland

2 = Combos equation

      1
= Eq. 6.10

      2
= Max of Eqs. 6.10a and 6.10b

3 = Second order method

      1
= Nominal stiffness

      2
= Nominal curvature

      3
= None

4 = Number of interaction
curves

Value >= 4 and divisible
by 4

5 = Number of interaction
points

Value >= 5 and odd

6 = Consider minimum eccentricity

0 = No

Any other value = Yes

7 = Theta0

Value > 0

8 = Gamma steel

Value > 0

9 = Gamma concrete

Value > 0

10
= AlphaCC

  Value
> 0

11
= AlphaCT

  Value
> 0

12
= AlphaLCC

  Value
> 0

13
= AlphaLCT

  Value
> 0

14 = Pattern live load
factor

  Value >=
0

15 = Utilization factor
limit

  Value >
0

16 = Multi-response case
design

  1 = Envelopes

  2 = Step-by-step

  3 = Last
step

  4 = Envelopes
-- All

  5 = Step-by-step
-- All

17
= Reliability Class

 1 = Class 1

 2 = Class 2

 3 = Class 3

                       18
= GammacE

                             Value
> 0

19
= Alphae (not used)

                             Value
> 0

20 = Consider torsion

0 = No

Any
other value = Yes

21 = Longitudinal rebar
size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

22 = Longitudinal rebar
size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

23 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

## Remarks

This function sets the value of a concrete design preference
item.

The function returns zero if the item is successfully
set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemEurocode\_2\_2004()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True,"R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Eurocode
2-2004")

   'set preference item
      ret = SapModel.DesignConcrete.Eurocode\_2\_2004.SetPreference(5,
9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.0.0.

Added Norway as a Country parameter in version 14.1.0.

Added Reliability Class parameter and added Sweden,
Finland, and Denmark as Country parameters in version 14.2.2.

Added Portugal and Germany as Country parameters in
SAP2000 Version 15.0.0.

Changed Time history design item to Multi-response case
design and added additional values in version 15.0.1.

Added items 18 – 19 in v21.1.0

Added item 20 in v23.4.0.

Changed item 19
to Not Used in v24.2.0

Added items 21 – 23 in v24.2.0

## See Also

[GetPreference](GetPreference{Concrete_Eurocode_2-2004}.htm)



## SetPreference {Concrete Shell Design Eurocode 2-2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2-2004/SetPreference_{Concrete_Shell_Design_Eurocode_2-2004}.htm`*

# SetPreference (Concrete Shell Design)

## Syntax

SapObject.SapModel.DesignConcreteShell.Eurocode\_2\_2004.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Country

2 = Gamma steel

3 = Gamma concrete

4 = AlphaCC

5 = AlphaCT

6 = Crack condition

7 = Shear design method

8 = Cotangent of the angle of concrete compressive strut

9 = Add tensile force due to shear

Value

The value of the considered preference item.

1 = Country

      1 = CEN Default

      2 = United Kingdom

      3 = Slovenia

      5 = Norway

      6 = Singapore

      7 = Sweden

      8 = Finland

      9 = Denmark

    10 = Portugal

    11 = Germany

    12 = Poland

    13 = Ireland

2 = Gamma steel

Value > 0

3 = Gamma concrete

Value > 0

4 = AlphaCC

  Value > 0

5 = AlphaCT

  Value > 0

6 = Crack condition

      1 = Program Determined - the program will perform the calculation according to EN 1992-2:2005 Annex LL (107) to check whether the shell elements are uncracked or cracked

2 = Cracked – the program will assume that the shell elements are cracked without performing the calculation according to EN 1992-2:2005 Annex LL (107)

7 = Shear design method

      1 = Method 1 – considers increasing longitudinal reinforcement to increase concrete shear capacity up to the allowable limit. If insufficient, shear reinforcement will be added

2 = Method 2 – determines required shear reinforcement without considering to increase longitudinal reinforcement

8 = Cotangent of the angle of concrete compressive strut

1 <= Value <= 3.0 for Germany

1 <= Value <= 2.0 for Poland

1 <= Value <= 2.5 for other countries

9 = Add tensile force due to shear

      0 = No

      Any Other Value = Yes

## Remarks

This function sets the value of a concrete shell design preference item.

The function returns zero if the item is successfully set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetConcreteShellDesignPreferenceItemEurocode\_2\_2004()
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

   'create blank model
       ret = SapModel.File.NewBlank()

   'set concrete design code
      ret = SapModel.DesignConcreteShell.SetCode("Eurocode 2-2004")

   'set preference item
      ret = SapModel.DesignConcreteShell.Eurocode\_2\_2004.SetPreference(2, 1.1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.0.0

Added items 5 through 8 in v24.1.0.

Added item 9 in v25.2.0.

## See Also

[GetPreference (Concrete Shell EC-2)](GetPreference_{Concrete_Shell_Design_Eurocode_2-2004}.htm)



## GetOverwrite {Concrete Eurocode 2 1992}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2_1992/GetOverwrite_{Concrete_Eurocode_2_1992}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.EUROCODE\_2\_1992.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Multi-response case design

2 = Consider environmental durability

3 = Consider shear design

4 = Shear design method

5 = Cotangent of the angle of concrete compressive strut

6 = Add tensile force due to shear

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemEUROCODE\_2\_1992()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("EUROCODE 2-1992")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.EUROCODE\_2\_1992.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_Eurocode_2_1992}.htm)



## GetPreference {Concrete Eurocode 2 1992}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2_1992/GetPreference_{Concrete_Eurocode_2_1992}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.EUROCODE\_2\_1992.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Nu

5 = Gamma steel

6 = Gamma concrete

7 = Pattern live load factor

8 = Utilization factor limit

9 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Nu

Value > 0

5 = Gamma steel

Value > 0

6 = Gamma concrete

Value > 0

7 = Pattern live load factor

Value >= 0

8 = Utilization factor limit

Value > 0

9 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemEUROCODE\_2\_1992()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("EUROCODE 2-1992")

   'get preference item
      ret = SapModel.DesignConcrete.EUROCODE\_2\_1992.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_Eurocode_2_1992}.htm)



## SetOverwrite {Concrete Eurocode 2 1992}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2_1992/SetOverwrite_{Concrete_Eurocode_2_1992}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.EUROCODE\_2\_1992.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, Beta Major

6 = Effective length factor, Beta Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemEUROCODE\_2\_1992()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("EUROCODE 2-1992")

   'set overwrite item
      ret = SapModel.DesignConcrete.EUROCODE\_2\_1992.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Eurocode_2_1992}.htm)



## SetPreference {Concrete Eurocode 2 1992}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Eurocode_2_1992/SetPreference_{Concrete_Eurocode_2_1992}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.EUROCODE\_2\_1992.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Nu

5 = Gamma steel

6 = Gamma concrete

7 = Pattern live load factor

8 = Utilization factor limit

9 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Nu

Value > 0

5 = Gamma steel

Value > 0

6 = Gamma concrete

Value > 0

7 = Pattern live load factor

Value >= 0

8 = Utilization factor limit

Value > 0

9 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemEUROCODE\_2\_1992()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("EUROCODE 2-1992")

   'set preference item
      ret = SapModel.DesignConcrete.EUROCODE\_2\_1992.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_Eurocode_2_1992}.htm)



## GetCode {Concrete Shell}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/GetCode_{Concrete_Shell}.htm`*

# GetCode (for Concrete Shell Design)

## Syntax

SapObject.SapModel.DesignConcreteShell.GetCode

## VB6 Procedure

Function GetCode(ByRef CodeName As String) As Long

## Parameters

CodeName

This is one of the following concrete shell design code names.

ACI 350-20

Eurocode 2-2004

## Remarks

This function retrieves the concrete shell design code.

The function returns zero if the code is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteShellDesignCode()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim CodeName As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create blank model
       ret = SapModel.File.NewBlank()

   'get concrete design code
      ret = SapModel.DesignConcreteShell.GetCode(CodeName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.0.0

Updated to include ACI 350-20 in list of code names in version 26.0.0

## See Also

[SetCode {Concrete Shell}](SetCode_{Concrete_Shell}.htm)



## GetCode {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/GetCode_{Concrete}.htm`*

# GetCode

## Syntax

SapObject.SapModel.DesignConcrete.GetCode

## VB6 Procedure

Function GetCode(ByRef CodeName As String) As Long

## Parameters

CodeName

This is one of the following concrete design code names.

AASHTO LRFD 2014
AASHTO LRFD 2012
AASHTO Concrete 07
ACI 318-14
ACI 318-11
ACI 318-08/IBC2009
AS 3600-09
BS8110 97
Chinese 2010
CSA A23.3-14
CSA A23.3-04
Eurocode 2-2004
Hong Kong CP 2013
Indian IS 456-2000
Italian NTC 2008
KBC 2009
Mexican RCDF 2004
NZS 3101:2006
Singapore CP 65:99
SP 63.13330.2012
TS 500-2000

## Remarks

This function retrieves the concrete design code.

The function returns zero if the code is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignCode()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim CodeName As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'get concrete design code
      ret = SapModel.DesignConcrete.GetCode(CodeName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Modified list of codes contained in the CodeName Parameter in version 15.0.1.

Updated list of available codes in v17.3.0.

Removed older codes which have been removed from the program in v18.0.0.

Updated list of available codes in v19.1.0.

## See Also

[SetCode](SetCode_{Concrete}.htm)



## GetComboAutoGenerate {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/GetComboAutoGenerate_{Concrete}.htm`*

# GetComboAutoGenerate

## Syntax

SapObject.SapModel.DesignConcrete.GetComboAutoGenerate

## VB6 Procedure

Function GetComboAutoGenerate(ByRef AutoGenerate As Boolean) As Long

## Parameters

AutoGenerate

If this item is True, the option to automatically generate code-based design load combinations for concrete frame design is turned on. If it is False, the option is turned off.

## Remarks

This function retrieves the value of the automatically generated code-based design load combinations option for concrete frame design.

The function returns zero if the options are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignComboAutoGenerate()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim AutoGenerate As Boolean

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

   'set option to not auto generate code-based design load combinations
      ret = SapModel.DesignConcrete.GetComboAutoGenerate(AutoGenerate)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 18.1.0.

## See Also

[SetComboAutoGenerate](SetComboAutoGenerate_{Concrete}.htm)



## GetComboStrength {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/GetComboStrength_{Concrete}.htm`*

# GetComboStrength

## Syntax

SapObject.SapModel.DesignConcrete.GetComboStrength

## VB6 Procedure

Function GetComboStrength(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of load combinations selected as design combinations for concrete strength design.

MyName

This is an array that includes the name of each response combination selected as a design combination for concrete strength design.

## Remarks

This function retrieves the names of all load combinations selected as design combinations for concrete strength design.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignComboStrength()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim NumberNames As Long
      Dim MyName2() As String
      Dim Selected As Boolean
      Dim NumberItems As Long
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default concrete design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(False, True, False, False)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName2)

   'select combos for concrete strength design
      For i = 0 To NumberNames - 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignConcrete.SetComboStrength(MyName2(i), Selected)
      Next i

   'get combos selected for concrete strength design
      ret = SapModel.DesignConcrete.GetComboStrength(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetComboStrength](SetComboStrength_{Concrete}.htm)



## GetDesignSection {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/GetDesignSection_{Concrete}.htm`*

# GetDesignSection

## Syntax

SapObject.SapModel.DesignConcrete.GetDesignSection

## VB6 Procedure

Function GetDesignSection(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

PropName

The name of the design section for the specified frame object.

## Remarks

This function retrieves the design section for a specified concrete frame object.

The function returns zero if the section is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignSection()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim PropName As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get design section
      ret = SapModel.DesignConcrete.GetDesignSection("8", PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetDesignSection](SetDesignSection_{Concrete}.htm)



## GetResultsAvailable {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/GetResultsAvailable_{Concrete}.htm`*

# GetResultsAvailable {Concrete}

## Syntax

SapObject.SapModel.DesignConcrete.GetResultsAvailable

## VB6 Procedure

Function GetResultsAvailable() As Boolean

## Parameters

None

## Remarks

The function returns True if the concrete frame design results are available, otherwise False.

## VBA Example

Sub GetResultsAvailable()

  'dimension variables

    Dim SapObject as cOAPI

    Dim SapModel As cSapModel

    Dim ret As Long

    Dim ResultsAvailable As Boolean

  'create Sap2000 object

    Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

  'start Sap2000 application

    SapObject.ApplicationStart

  'create SapModel object

    Set SapModel = SapObject.SapModel

  'initialize model

    ret = SapModel.InitializeNewModel

  'create new concrete frame section property

    ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

  'create model from template

    ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

  'run analysis

    ret = SapModel.File.Save("C:\SapAPI\x.sdb")

    ret = SapModel.Analyze.RunAnalysis

  'start concrete design

    ret = SapModel.DesignConcrete.StartDesign

  'check if design results are available

    ResultsAvailable = SapModel.DesignConcrete.GetResultsAvailable

  'close Sap2000

    SapObject.ApplicationExit.False

    Set SapModel = Nothing

    Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 18.2.0.



## GetSummaryResultsBeam

*Source file: `SAP2000_API_Fuctions/Design/Concrete/GetSummaryResultsBeam.htm`*

# GetSummaryResultsBeam

## Syntax

SapObject.SapModel.DesignConcrete.GetSummaryResultsBeam

## VB6 Procedure

Function GetSummaryResultsBeam(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef Location() As Double, ByRef TopCombo() As String, ByRef TopArea() As Double, ByRef BotCombo() As String, ByRef BotArea() As Double, ByRef VmajorCombo() As String, ByRef VmajorArea() As Double, ByRef TLCombo() As String, ByRef TLArea() As Double, ByRef TTCombo() As String, ByRef TTArea() As Double, ByRef ErrorSummary() As String, ByRef WarningSummary() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

NumberItems

The number of frame objects for which results are obtained.

FrameName

This is an array that includes each frame object name for which results are obtained.

Location

This is an array that includes the distance from the I-end of the frame object to the location where the results are reported. [L]

TopCombo

This is an array that includes the name of the design combination for which the controlling top longitudinal rebar area for flexure occurs. A combination name followed by (Sp) indicates that the design loads were obtained by applying special, code-specific multipliers to all or part of the specified design load combination, or that the design was based on the capacity of other objects (or other design locations for the same object).

TopArea

This is an array that includes the total top longitudinal rebar area required for the flexure at the specified location. It does not include the area of steel required for torsion. [L2]

BotCombo

This is an array that includes the name of the design combination for which the controlling bottom longitudinal rebar area for flexure occurs. A combination name followed by (Sp) indicates that the design loads were obtained by applying special, code-specific, multipliers to all or part of the specified design load combination, or that the design was based on the capacity of other objects (or other design locations for the same object).

BotArea

This is an array that includes the total bottom longitudinal rebar area required for the flexure at the specified location. It does not include the area of steel required for torsion. [L2]

VmajorCombo

This is an array that includes the name of the design combination for which the controlling shear occurs. A combination name followed by (Sp) indicates that the design loads were obtained by applying special, code-specific, multipliers to all or part of the specified design load combination, or that the design was based on the capacity of other objects (or other design locations for the same object).

VmajorArea

This is an array that includes the required area of transverse shear reinforcing per unit length along the frame object for shear at the specified location. [L2/L]

TLCombo

This is an array that includes the name of the design combination for which the controlling longitudinal rebar area for torsion occurs. A combination name followed by (Sp) indicates that the design loads were obtained by applying special, code-specific, multipliers to all or part of the specified design load combination, or that the design was based on the capacity of other objects (or other design locations for the same object).

TLArea

This is an array that includes the total longitudinal rebar area required for torsion. [L2]

TTCombo

This is an array that includes the name of the design combination for which the controlling transverse reinforcing for torsion occurs. A combination name followed by (Sp) indicates that the design loads were obtained by applying special, code-specific, multipliers to all or part of the specified design load combination, or that the design was based on the capacity of other objects (or other design locations for the same object).

TTArea

This is an array that includes the required area of transverse torsional shear reinforcing per unit length along the frame object for torsion at the specified location. [L2/L]

ErrorSummary

This is an array that includes the design error messages for the frame object, if any.

WarningSummary

This is an array that includes the design warning messages for the frame object, if any.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the design results are retrieved for the frame object specified by the Name item.

If this item is Group, the design results are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the design results are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves summary results for concrete design.

The function returns zero if the results are successfully retrieved; otherwise it returns a nonzero value.

Note that torsional design is only included for some codes.

## VBA Example

Sub GetConcreteBeamDesignSummaryResults()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim Location() As Double
      Dim TopCombo() As String
      Dim TopArea() As Double
      Dim BotCombo() As String
      Dim BotArea() As Double
      Dim VmajorCombo() As String
      Dim VmajorArea() As Double
      Dim TLCombo() As String
      Dim TLArea() As Double
      Dim TTCombo() As String
      Dim TTArea() As Double
      Dim ErrorSummary() As String
      Dim WarningSummary() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add ASTM A706 rebar material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_REBAR, , , , , MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A706)

   'create new concrete frame section properties
      ret = SapModel.PropFrame.SetRectangle("COL", "4000Psi", 20, 20)
      ret = SapModel.PropFrame.SetRectangle("BEAM", "4000Psi", 20, 12)
      ret = SapModel.PropFrame.SetRebarBeam("BEAM", Name, Name, 2, 2, 2, 2, 2, 2)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "BEAM", "COL")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get summary result data
      ret = SapModel.DesignConcrete.GetSummaryResultsBeam("8", NumberItems, FrameName, Location, TopCombo, TopArea, BotCombo, BotArea, VmajorCombo, VmajorArea, TLCombo, TLArea, TTCombo, TTArea, ErrorSummary, WarningSummary)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetSummaryResultsColumn](GetSummaryResultsColumn.htm)

[GetSummaryResultsJoint](GetSummaryResultsJoint.htm)



## GetSummaryResultsColumn

*Source file: `SAP2000_API_Fuctions/Design/Concrete/GetSummaryResultsColumn.htm`*

# GetSummaryResultsColumn

## Syntax

SapObject.SapModel.DesignConcrete.GetSummaryResultsColumn

## VB6 Procedure

Function GetSummaryResultsColumn(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef MyOption() As Long, ByRef Location() As Double, ByRef PMMCombo() As String, ByRef PMMArea() As Double, ByRef PMMRatio() As Double, ByRef VmajorCombo() As String, ByRef AVmajor() As Double, ByRef VminorCombo() As String, ByRef AVminor() As Double, ByRef ErrorSummary() As String, ByRef WarningSummary() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

NumberItems

The number of frame objects for which results are obtained.

FrameName

This is an array that includes each frame object name for which results are obtained.

MyOption

This is an array that includes 1 or 2, indicating the design option for each frame object.

1 = Check

2 = Design

Location

This is an array that includes the distance from the I-end of the frame object to the location where the results are reported. [L]

PMMCombo

This is an array that includes the name of the design combination for which the controlling PMM ratio or rebar area occurs. A combination name followed by (Sp) indicates that the design loads were obtained by applying special, code-specific multipliers to all or part of the specified design load combination, or that the design was based on the capacity of other objects (or other design locations for the same object).

PMMArea

This is an array that includes the total longitudinal rebar area required for the axial force plus biaxial moment (PMM) design at the specified location. [L2]

This item applies only when MyOption = 2 (design).

PMMRatio

This is an array that includes the axial force plus biaxial moment (PMM) stress ratio at the specified location.

This item applies only when MyOption = 1 (check).

VmajorCombo

This is an array that includes the name of the design combination for which the controlling major shear occurs.

AVmajor

This is an array that includes the required area of transverse shear reinforcing per unit length along the frame object for major shear at the specified location. [L2/L]

VminorCombo

This is an array that includes the name of the design combination for which the controlling minor shear occurs.

AVminor

This is an array that includes the required area of transverse shear reinforcing per unit length along the frame object for minor shear at the specified location. [L2/L]

ErrorSummary

This is an array that includes the design error messages for the frame object, if any.

WarningSummary

This is an array that includes the design warning messages for the frame object, if any.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the design results are retrieved for the frame object specified by the Name item.

If this item is Group, the design results are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the design results are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves summary results for concrete design.

The function returns zero if the results are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteColumnDesignSummaryResults()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim MyOption() As Long
      Dim Location() As Double
      Dim PMMCombo() As String
      Dim PMMArea() As Double
      Dim PMMRatio() As Double
      Dim VmajorCombo() As String
      Dim AVmajor() As Double
      Dim VminorCombo() As String
      Dim AVminor() As Double
      Dim ErrorSummary() As String
      Dim WarningSummary() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add ASTM A706 rebar material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_REBAR, , , , , MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A706)

   'create new concrete frame section properties
      ret = SapModel.PropFrame.SetRectangle("COL", "4000Psi", 20, 20)
      ret = SapModel.PropFrame.SetRectangle("BEAM", "4000Psi", 20, 12)
      ret = SapModel.PropFrame.SetRebarBeam("BEAM", Name, Name, 2, 2, 2, 2, 2, 2)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "BEAM", "COL")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get summary result data
      ret = SapModel.DesignConcrete.GetSummaryResultsColumn("1", NumberItems, FrameName, MyOption, Location, PMMCombo, PMMArea, PMMRatio, VmajorCombo, AVmajor, VminorCombo, AVminor, ErrorSummary, WarningSummary)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetSummaryResultsBeam](GetSummaryResultsBeam.htm)

[GetSummaryResultsJoint](GetSummaryResultsJoint.htm)



## GetSummaryResultsJoint

*Source file: `SAP2000_API_Fuctions/Design/Concrete/GetSummaryResultsJoint.htm`*

# GetSummaryResultsJoint

## Syntax

SapObject.SapModel.DesignConcrete.GetSummaryResultsJoint

## VB6 Procedure

Function GetSummaryResultsJoint(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef LCJSRatioMajor() As String, ByRef JSRatioMajor() As Double, ByRef LCJSRatioMinor() As String, ByRef JSRatioMinor() As Double, ByRef LCBCCRatioMajor() As String, ByRef BCCRatioMajor() As Double, ByRef LCBCCRatioMinor() As String, ByRef BCCRatioMinor() As Double, ByRef ErrorSummary() As String, ByRef WarningSummary() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

NumberItems

The number of frame objects for which results are obtained.

FrameName

This is an array that includes each frame object name for which results are obtained.

LCJSRatioMajor

This is an array that includes the name of the design combination for which the controlling joint shear ratio associated with the column major axis occurs. A combination name followed by (Sp) indicates that the design loads were obtained by applying special, code-specific multipliers to all or part of the specified design load combination, or that the design was based on the capacity of other objects (or other design locations for the same object).

JSRatioMajor

This is an array that includes the joint shear ratio associated with the column major axis. This is the joint shear divided by the joint shear capacity.

LCJSRatioMinor

This is an array that includes the name of the design combination for which the controlling joint shear ratio associated with the column minor axis occurs. A combination name followed by (Sp) indicates that the design loads were obtained by applying special, code-specific multipliers to all or part of the specified design load combination, or that the design was based on the capacity of other objects (or other design locations for the same object).

JSRatioMinor

This is an array that includes the joint shear ratio associated with the column minor axis. This is the joint shear divided by the joint shear capacity.

LCBCCRatioMajor

This is an array that includes the name of the design combination for which the controlling beam/column capacity ratio associated with the column major axis occurs. A combination name followed by (Sp) indicates that the design loads were obtained by applying special, code-specific multipliers to all or part of the specified design load combination, or that the design was based on the capacity of other objects (or other design locations for the same object).

BCCRatioMajor

This is an array that includes the beam/column capacity ratio associated with the column major axis. This is the sum of the column capacities divided by the sum of the beam capacities at the top of the specified column.

LCBCCRatioMinor

This is an array that includes the name of the design combination for which the controlling beam/column capacity ratio associated with the column minor axis occurs. A combination name followed by (Sp) indicates that the design loads were obtained by applying special, code-specific multipliers to all or part of the specified design load combination, or that the design was based on the capacity of other objects (or other design locations for the same object).

BCCRatioMinor

This is an array that includes the beam/column capacity ratio associated with the column minor axis. This is the sum of the column capacities divided by the sum of the beam capacities at the top of the specified column.

ErrorSummary

This is an array that includes the design error messages for the frame object, if any.

WarningSummary

This is an array that includes the design warning messages for the frame object, if any.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the design results are retrieved for the frame object specified by the Name item.

If this item is Group, the design results are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the design results are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves summary results for concrete design.

The function returns zero if the results are successfully retrieved; otherwise it returns a nonzero value.

Note that joint design is only included for some codes.

## VBA Example

Sub GetConcreteJointDesignSummaryResults()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim LCJSRatioMajor() As String
      Dim JSRatioMajor() As Double
      Dim LCJSRatioMinor() As String
      Dim JSRatioMinor() As Double
      Dim LCBCCRatioMajor() As String
      Dim BCCRatioMajor() As Double
      Dim LCBCCRatioMinor() As String
      Dim BCCRatioMinor() As Double
      Dim ErrorSummary() As String
      Dim WarningSummary() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add ASTM A706 rebar material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_REBAR, , , , , MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A706)

   'create new concrete frame section properties
      ret = SapModel.PropFrame.SetRectangle("COL", "4000Psi", 20, 20)
      ret = SapModel.PropFrame.SetRectangle("BEAM", "4000Psi", 20, 12)
      ret = SapModel.PropFrame.SetRebarBeam("BEAM", Name, Name, 2, 2, 2, 2, 2, 2)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "BEAM", "COL")

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("EQX", LTYPE\_QUAKE)

   'assign IBC2003 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetIBC2003("EQX", 1, 0.05, 1, 0.035, 0, False, 0, 0, 1, 1, 3, 1, 0.4, 0, 0, 8, 3, 5.5)

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI 318-02")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get summary result data
      ret = SapModel.DesignConcrete.GetSummaryResultsJoint("3", NumberItems, FrameName, LCJSRatioMajor, JSRatioMajor, LCJSRatioMinor, JSRatioMinor, LCBCCRatioMajor, BCCRatioMajor, LCBCCRatioMinor, BCCRatioMinor, ErrorSummary, WarningSummary)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetSummaryResultsBeam](GetSummaryResultsBeam.htm)

[GetSummaryResultsColumn](GetSummaryResultsColumn.htm)



## GetOverwrite {Concrete Hong Kong CP 2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Hong_Kong_CP_2004/GetOverwrite_{Concrete_Hong_Kong_CP_2004}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Hong\_Kong\_CP\_2004.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, Beta Major

6 = Effective length factor, Beta Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemHong\_Kong\_CP\_2004()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Hong Kong CP 2004")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.Hong\_Kong\_CP\_2004.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_Hong_Kong_CP_2004}.htm)



## GetPreference {Concrete Hong Kong CP 2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Hong_Kong_CP_2004/GetPreference_{Concrete_Hong_Kong_CP_2004}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Hong\_Kong\_CP\_2004.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Gamma steel

5 = Gamma concrete

6 = Gamma concrete shear

7 = Pattern live load factor

8 = Utilization factor limit

9 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Gamma steel

Value > 0

5 = Gamma concrete

Value > 0

6 = Gamma concrete shear

Value > 0

7 = Pattern live load factor

Value >= 0

8 = Utilization factor limit

Value > 0

9 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemHong\_Kong\_CP\_2004()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Hong Kong CP 2004")

   'get preference item
      ret = SapModel.DesignConcrete.Hong\_Kong\_CP\_2004.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_Hong_Kong_CP_2004}.htm)



## SetOverwrite {Concrete Hong Kong CP 2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Hong_Kong_CP_2004/SetOverwrite_{Concrete_Hong_Kong_CP_2004}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Hong\_Kong\_CP\_2004.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, Beta Major

6 = Effective length factor, Beta Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemHong\_Kong\_CP\_2004()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Hong Kong CP 2004")

   'set overwrite item
      ret = SapModel.DesignConcrete.Hong\_Kong\_CP\_2004.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Hong_Kong_CP_2004}.htm)



## SetPreference {Concrete Hong Kong CP 2004}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Hong_Kong_CP_2004/SetPreference_{Concrete_Hong_Kong_CP_2004}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Hong\_Kong\_CP\_2004.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Gamma steel

5 = Gamma concrete

6 = Gamma concrete shear

7 = Pattern live load factor

8 = Utilization factor limit

9 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Gamma steel

Value > 0

5 = Gamma concrete

Value > 0

6 = Gamma concrete shear

Value > 0

7 = Pattern live load factor

Value >= 0

8 = Utilization factor limit

Value > 0

9 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemHong\_Kong\_CP\_2004()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Hong Kong CP 2004")

   'set preference item
      ret = SapModel.DesignConcrete.Hong\_Kong\_CP\_2004.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_Hong_Kong_CP_2004}.htm)



## GetOverwrite {Concrete Hong Kong CP 2013}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Hong_Kong_CP_2013/GetPreference_{Concrete_Hong_Kong_CP_2013}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Hong\_Kong\_CP\_2013.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, Beta Major

6 = Effective length factor, Beta Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemHong\_Kong\_CP\_2013()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Hong Kong CP 2013")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.Hong\_Kong\_CP\_2013.GetOverwrite("8", 1, Value, ProgDet)
   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 19.0.0.

## See Also

[SetOverwrite](SetOverwrite{Concrete_Hong_Kong_2013}.htm)



## SetOverwrite {Concrete Hong Kong 2013}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Hong_Kong_CP_2013/SetOverwrite{Concrete_Hong_Kong_2013}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Hong\_Kong\_CP\_2013.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, Beta Major

6 = Effective length factor, Beta Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemHong\_Kong\_CP\_2013()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Hong Kong CP 2013")

   'set overwrite item
      ret = SapModel.DesignConcrete.Hong\_Kong\_CP\_2013.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 19.0.0.

## See Also

[GetOverwrite](GetPreference_{Concrete_Hong_Kong_CP_2013}.htm)



## SetPreference {Concrete Hong Kong CP 2013}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Hong_Kong_CP_2013/SetPreference_{Concrete_Hong_Kong_CP_2013}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Hong\_Kong\_CP\_2013.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Gamma steel

5 = Gamma concrete

6 = Gamma concrete shear

7 = Pattern live load factor

8 = Utilization factor limit

9 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Gamma steel

Value > 0

5 = Gamma concrete

Value > 0

6 = Gamma concrete shear

Value > 0

7 = Pattern live load factor

Value >= 0

8 = Utilization factor limit

Value > 0

9 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemHong\_Kong\_CP\_2013)
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Hong Kong CP 2013")

   'set preference item
      ret = SapModel.DesignConcrete.Hong\_Kong\_CP\_2013.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 19.0.0.

## See Also

[GetPreference](SetPreferences_{Concrete}.htm)



## GetPreference {Concrete Hong Kong CP 2013}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Hong_Kong_CP_2013/SetPreferences_{Concrete}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Hong\_Kong\_CP\_2013.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Gamma steel

5 = Gamma concrete

6 = Gamma concrete shear

7 = Pattern live load factor

8 = Utilization factor limit

9 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Gamma steel

Value > 0

5 = Gamma concrete

Value > 0

6 = Gamma concrete shear

Value > 0

7 = Pattern live load factor

Value >= 0

8 = Utilization factor limit

Value > 0

9 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemHong\_Kong\_CP\_2013()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Hong Kong CP 2013")

   'get preference item
      ret = SapModel.DesignConcrete.Hong\_Kong\_CP\_2013.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 19.0.0.

## See Also

[SetPreference](SetPreference_{Concrete_Hong_Kong_CP_2013}.htm)



## GetOverwrite {Concrete Indian IS 456 2000}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Indian_IS_456_2000/GetOverwrite_{Concrete_Indian_IS_456_2000}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Indian\_IS\_456\_2000.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design
procedure.

Item

This is an integer between 1 and 22, inclusive, indicating
the overwrite item considered.

1 = Framing type (beam
and column)

2 = Live load reduction
factor (beam and column)

3 = Unbraced length ratio,
Major (beam and column)

4 = Unbraced length ratio,
Minor (beam and column)

5 = Effective length factor,
K Major (column only)

6 = Effective length factor,
K Minor (column only)

7 = Moment coefficient,
Cm Major (not used)

8 = Moment coefficient,
Cm Minor (not used)

9 = Non-sway moment factor,
Dns Major (not used)

10 = Non-sway moment factor,
Dns Minor (not used)

11 = Sway moment factor,
Ds Major (not used)

12 = Sway moment factor, Ds
Minor (not used)

13 = Top rebar area of a beam
at the left end (I-end) (beam only)

14 = Bottom rebar area of
a beam at the left end (I-end) (beam
only)

15 = Top rebar area of a beam
at the right end (J-end) (beam only)

16 = Bottom rebar area of
a beam at the right end (J-end) (beam only)

17 = Consider torsion (not
used)

18 = Concrete cover for
closed stirrups (beam only)

19 = Effective length factor
braced, K Major braced (column only)

20 = Effective length factor
braced, K Minor braced (column only)

21 = Q factor in global
X direction (column only)

22 = Q factor in global
Y direction (column only)

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ductile

2 = Ordinary

3 = Non-sway

2 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

3 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value.

4 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value.

5 = Effective length factor,
K Major

Value >= 0; 0 means
use program determined value.

6 = Effective length factor,
K Minor

Value >= 0; 0 means
use program determined value.

7 = Moment coefficient,
Cm Major

Value >= 0; 0 means
use program determined value.

8 = Moment coefficient,
Cm Minor

Value >= 0; 0 means
use program determined value.

9 = Non-sway moment factor,
Dns Major

Value >= 0; 0 means
use program determined value.

10 = Non-sway moment factor,
Dns Minor

Value >= 0; 0 means
use program determined value.

11 = Sway moment factor,
Ds Major

Value >= 0; 0 means
use program determined value.

12 = Sway moment factor,
Ds Minor

Value >= 0; 0 means
use program determined value.

13
= Top rebar area of a beam at the left end (I-end)

        Value
>= 0; 0 means use program determined value.

14
= Bottom rebar area of a beam at the left end (I-end)

        Value
>= 0; 0 means use program determined value.

15
= Top rebar area of a beam at the right end (J-end)

        Value
>= 0; 0 means use program determined value.

16
= Bottom rebar area of a beam at the right end (J-end)

        Value
>= 0; 0 means use program determined value.

17 = Consider torsion (not
used)

0 = No

Any other value = Yes

18 = Concrete cover for
closed stirrups

Value >= 0; 0 means
use program determined value.

19 = Effective length factor
braced, K Major braced

Value >= 0; 0 means
use program determined value.

20 = Effective length factor
braced, K Minor braced

Value >= 0; 0 means
use program determined value.

21 = Q factor in global
X direction

Value >= 0; 0 means
use program determined value.

22 = Q factor in global
Y direction

Value >= 0; 0 means
use program determined value.

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a concrete design
overwrite item.

The function returns zero if the item is successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemIndian\_IS\_456\_2000()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Indian
IS 456-2000")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.Indian\_IS\_456\_2000.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added Items 13, 14, 15, and 16 in Version 14.0.0.

Changed description for items 7 through 12 and added
items 17-22 in v23.4.0.

Changed description of item 17 to “not used” in version
24.2.0

## See Also

[SetOverwrite](SetOverwrite_{Concrete_Indian_IS_456_2000}.htm)



## GetPreference {Concrete Indian IS 456 2000}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Indian_IS_456_2000/GetPreference_{Concrete_Indian_IS_456_2000}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Indian\_IS\_456\_2000.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 12, inclusive, indicating
the preference item considered.

1 = Number of interaction
curves

2 = Number of interaction
points

3 = Consider minimum eccentricity

4 = Gamma steel

5 = Gamma concrete

6 = Pattern live load
factor

7 = Utilization factor
limit

8 = Multi-response case design

9 = Consider torsion (not
used)

10 = Consider additional
moment

11 = Consider P-Delta done

12 = Design for B/C capacity
ratio

Value

The value of the considered preference item.

1 = Number of interaction
curves

Value >= 4 and devisable
by 4

2 = Number of interaction
points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Gamma steel

Value > 0

5 = Gamma concrete

Value > 0

6 = Pattern live load
factor

Value >= 0

7 = Utilization factor
limit

Value > 0

8 = Multi-response case
design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

9
= Consider torsion (not used)

0 = No

Any other value = Yes

10 = Consider additional
moment

0 = No

Any other value = Yes

11 = Consider P-Delta done

0 = No

Any other value = Yes

12 = Design for B/C capacity
ratio

0 = No

Any other value = Yes

## Remarks

This function retrieves the value of a concrete design
preference item.

The function returns zero if the item is successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemIndian\_IS\_456\_2000()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Indian
IS 456-2000")

   'get preference item
      ret = SapModel.DesignConcrete.Indian\_IS\_456\_2000.GetPreference(2,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case
design and added additional values in version 15.0.1.

Added items 9-12 in version 23.4.0

Changed description of item 9 to “not used” in version
24.2.0

## See Also

[SetPreference](SetPreference_{Concrete_Indian_IS_456_2000}.htm)



## SetOverwrite {Concrete Indian IS 456 2000}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Indian_IS_456_2000/SetOverwrite_{Concrete_Indian_IS_456_2000}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Indian\_IS\_456\_2000.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByValItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending
on the value of the ItemType item.

Item

This is an integer between 1 and 22, inclusive, indicating
the overwrite item considered.

1 = Framing type (beam
and column)

2 = Live load reduction
factor (beam and column)

3 = Unbraced length ratio,
Major (beam and column)

4 = Unbraced length ratio,
Minor (beam and column)

5 = Effective length factor,
K Major (column only)

6 = Effective length factor,
K Minor (column only)

7 = Moment coefficient,
Cm Major (not used)

8 = Moment coefficient,
Cm Minor (not used)

9 = Non-sway moment factor,
Dns Major (not used)

10 = Non-sway moment factor,
Dns Minor (not used)

11 = Sway moment factor,
Ds Major (not used)

12 = Sway moment factor, Ds
Minor (not used)

13 = Top rebar area of a beam
at the left end (I-end) (beam only)

14 = Bottom rebar area of
a beam at the left end (I-end) (beam
only)

15 = Top rebar area of a beam
at the right end (J-end) (beam only)

16 = Bottom rebar area of
a beam at the right end (J-end) (beam only)

17 = Consider torsion (not
used)

18 = Concrete cover for
closed stirrups (beam only)

19 = Effective length factor
braced, K Major braced (column only)

20 = Effective length factor
braced, K Minor braced (column only)

21 = Q factor in global
X direction (column only)

22 = Q factor in global
Y direction (column only)

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ductile

2 = Ordinary

3 = Non-sway

2 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

3 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value.

4 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value.

5 = Effective length factor,
K Major

Value >= 0; 0 means
use program determined value.

6 = Effective length factor,
K Minor

Value >= 0; 0 means
use program determined value.

7 = Moment coefficient,
Cm Major

Value >= 0; 0 means
use program determined value.

8 = Moment coefficient,
Cm Minor

Value >= 0; 0 means
use program determined value.

9 = Non-sway moment factor,
Dns Major

Value >= 0; 0 means
use program determined value.

10 = Non-sway moment factor,
Dns Minor

Value >= 0; 0 means
use program determined value.

11 = Sway moment factor,
Ds Major

Value >= 0; 0 means
use program determined value.

12 = Sway moment factor,
Ds Minor

Value >= 0; 0 means use
program determined value.

13
= Top rebar area of a beam at the left end (I-end)

        Value
>= 0; 0 means use program determined value.

14
= Bottom rebar area of a beam at the left end (I-end)

        Value
>= 0; 0 means use program determined value.

15
= Top rebar area of a beam at the right end (J-end)

        Value
>= 0; 0 means use program determined value.

16
= Bottom rebar area of a beam at the right end (J-end)

        Value
>= 0; 0 means use program determined value.

17
= Consider torsion (not used)

0 = No

Any other value = Yes

18 = Concrete cover for
closed stirrups

Value >= 0; 0 means
use program determined value.

19 = Effective length factor
braced, K Major braced

Value >= 0; 0 means
use program determined value.

20 = Effective length factor
braced, K Minor braced

Value >= 0; 0 means
use program determined value.

21 = Q factor in global
X direction

Value >= 0; 0 means
use program determined value.

22 = Q factor in global
Y direction

Value >= 0; 0 means
use program determined value.

ItemType

This is one of the following items in the eItemType
enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the
frame object specified by the Name item.

If this item is Group,the assignment is made to all
frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made
to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemIndian\_IS\_456\_2000()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Indian
IS 456-2000")

   'set overwrite item
      ret = SapModel.DesignConcrete.Indian\_IS\_456\_2000.SetOverwrite("8",
1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added Items 13, 14, 15, and 16 in Version 14.0.0.

Changed description for items 7 through 12 and added
items 17-22 in v23.4.0.

Changed description of item 17 to “not used” in version
24.2.0

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Indian_IS_456_2000}.htm)



## SetPreference {Concrete Indian IS 456 2000}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Indian_IS_456_2000/SetPreference_{Concrete_Indian_IS_456_2000}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Indian\_IS\_456\_2000.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 12, inclusive, indicating
the preference item considered.

1 = Number of interaction
curves

2 = Number of interaction
points

3 = Consider minimum eccentricity

4 = Gamma steel

5 = Gamma concrete

6 = Pattern live load
factor

7 = Utilization factor
limit

8 = Multi-response case design

9
= Consider torsion (not used)

10 = Consider additional
moment

11 = Consider P-Delta done

12 = Design for B/C capacity
ratio

Value

The value of the considered preference item.

1 = Number of interaction
curves

Value >= 4 and devisable
by 4

2 = Number of interaction
points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Gamma steel

Value > 0

5 = Gamma concrete

Value > 0

6 = Pattern live load
factor

Value >= 0

7 = Utilization factor
limit

Value > 0

8 = Multi-response case
design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

9 = Consider torsion (not
used)

0 = No

Any other value = Yes

10 = Consider additional
moment

0 = No

Any other value = Yes

11 = Consider P-Delta done

0 = No

Any other value = Yes

12 = Design for B/C capacity
ratio

0 = No

Any other value = Yes

## Remarks

This function sets the value of a concrete design preference
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemIndian\_IS\_456\_2000()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Indian
IS 456-2000")

   'set preference item
      ret = SapModel.DesignConcrete.Indian\_IS\_456\_2000.SetPreference(2,
9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case
design and added additional values in version 15.0.1.

Added items 9-12 in version 23.4.0

Changed description of item 9 to “not used” in version
24.2.0

## See Also

[GetPreference](GetPreference_{Concrete_Indian_IS_456_2000}.htm)



## GetOverwrite {Concrete Italian DM 14 292}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Italian_dm_14_292/GetOverwrite_{Concrete_Italian_DM_14_292}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Italian\_DM\_14\_2\_92.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Amplification Coefficient, Omega Major

8 = Amplification Coefficient, Omega Minor

9 = Moment coefficient, c Major

10 = Moment coefficient, c Minor

11 = Moment coefficient, c\_sway Major

12 = Moment coefficient, c\_sway Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Braced

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Amplification coefficient, Omega Major

Value >= 0; 0 means use program determined value.

8 = Amplification coefficient, Omega Minor

Value >= 0; 0 means use program determined value.

9 = Moment coefficient, c Major

Value >= 0; 0 means use program determined value.

10 = Moment coefficient, c Minor

Value >= 0; 0 means use program determined value.

11 = Moment coefficient, c\_sway Major

Value >= 0; 0 means use program determined value.

12 = Moment coefficient, c\_sway Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemItalian\_DM\_14\_2\_92()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Italian DM 14-2-92")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.Italian\_DM\_14\_2\_92.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_Italian_DM_14_292}.htm)



## GetPreference {Concrete Italian DM 14 292}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Italian_dm_14_292/GetPreference_{Concrete_Italian_DM_14_292}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Italian\_DM\_14\_2\_92.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 5, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Pattern live load factor

4 = Utilization factor limit

5 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Pattern live load factor

Value >= 0

4 = Utilization factor limit

Value > 0

5 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemItalian\_DM\_14\_2\_92()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'createSapModelobject
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Italian DM 14-2-92")

   'get preference item
      ret = SapModel.DesignConcrete.Italian\_DM\_14\_2\_92.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_Italian_DM_14_292}.htm)



## SetOverwrite {Concrete Italian DM 14 292}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Italian_dm_14_292/SetOverwrite_{Concrete_Italian_DM_14_292}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Italian\_DM\_14\_2\_92.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Amplification Coefficient, Omega Major

8 = Amplification Coefficient, Omega Minor

9 = Moment coefficient, c Major

10 = Moment coefficient, c Minor

11 = Moment coefficient, c\_sway Major

12 = Moment coefficient, c\_sway Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Braced

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Amplification coefficient, Omega Major

Value >= 0; 0 means use program determined value.

8 = Amplification coefficient, Omega Minor

Value >= 0; 0 means use program determined value.

9 = Moment coefficient, c Major

Value >= 0; 0 means use program determined value.

10 = Moment coefficient, c Minor

Value >= 0; 0 means use program determined value.

11 = Moment coefficient, c\_sway Major

Value >= 0; 0 means use program determined value.

12 = Moment coefficient, c\_sway Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemItalian\_DM\_14\_2\_92()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'createSap2000 object
      Set SapObject= New Sap2000v16.SapObject

   'startSap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel= SapObject.SapModel

   'initialize model
      ret= SapModel.InitializeNewModel

   'createnew concrete frame section property
      ret= SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret= SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret= SapModel.DesignConcrete.SetCode("Italian DM 14-2-92")

   'set overwrite item
      ret= SapModel.DesignConcrete.Italian\_DM\_14\_2\_92.SetOverwrite("8", 1, 2)

   'closeSap2000
      SapObject.ApplicationExit False
      Set SapModel= Nothing
      Set SapObject= Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Italian_DM_14_292}.htm)



## SetPreference {Concrete Italian DM 14 292}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Italian_dm_14_292/SetPreference_{Concrete_Italian_DM_14_292}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Italian\_DM\_14\_2\_92.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 5, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Pattern live load factor

4 = Utilization factor limit

5 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Pattern live load factor

Value >= 0

4 = Utilization factor limit

Value > 0

5 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemItalian\_DM\_14\_2\_92()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Italian DM 14-2-92")

   'set preference item
      ret = SapModel.DesignConcrete.Italian\_DM\_14\_2\_92.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_Italian_DM_14_292}.htm)



## GetOverwrite {Concrete KCI 1999}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/KCI_1999/GetOverwrite_{Concrete_KCI_1999}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.KCI\_1999.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway intermediate

3 = Sway ordinary

4 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemKCI\_1999()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("KCI-1999")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.KCI\_1999.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_KCI_1999}.htm)



## GetPreference {Concrete KCI 1999}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/KCI_1999/GetPreference_{Concrete_KCI_1999}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.KCI\_1999.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi bending tension

5 = Phi compression controlled tied

6 = Phi compression controlled spiral

7 = Phi shear

8 = Pattern live load factor

9 = Utilization factor limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi bending tension

Value > 0

5 = Phi compression controlled tied

Value > 0

6 = Phi compression controlled spiral

Value > 0

7 = Phi shear

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Utilization factor limit

Value > 0

10 = Multi-response case design

 1 = Envelopes

 2 = Step-by-step

 3 = Last step

 4 = Envelopes -- All

 5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemKCI\_1999()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("KCI-1999")

   'get preference item
      ret = SapModel.DesignConcrete.KCI\_1999.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_KCI_1999}.htm)



## SetOverwrite {Concrete KCI 1999}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/KCI_1999/SetOverwrite_{Concrete_KCI_1999}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.KCI\_1999.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway intermediate

3 = Sway ordinary

4 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemKCI\_1999 ()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("KCI-1999")

   'set overwrite item
      ret = SapModel.DesignConcrete.KCI\_1999.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_KCI_1999}.htm)



## SetPreference {Concrete KCI 1999}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/KCI_1999/SetPreference_{Concrete_KCI_1999}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.KCI\_1999.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi bending tension

5 = Phi compression controlled tied

6 = Phi compression controlled spiral

7 = Phi shear

8 = Pattern live load factor

9 = Utilization factor limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi bending tension

Value > 0

5 = Phi compression controlled tied

Value > 0

6 = Phi compression controlled spiral

Value > 0

7 = Phi shear

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Utilization factor limit

Value > 0

10 = Multi-response case design

 1 = Envelopes

 2 = Step-by-step

 3 = Last step

 4 = Envelopes -- All

 5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemKCI\_1999()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("KCI-1999")

   'set preference item
      ret = SapModel.DesignConcrete.KCI\_1999.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_KCI_1999}.htm)



## GetOverwrite {Concrete Mexican RCDF 2001}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Mexican_RCDF_2001/GetOverwrite_{Concrete_Mexican_RCDF_2001}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Mexican\_RCDF\_2001.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, k Major

6 = Effective length factor, k Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Fab Major

10 = Non-sway moment factor, Fab Minor

11 = Sway moment factor, Fas Major

12 = Sway moment factor, Fas Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway ordinary

3 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, k Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, k Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Fab Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Fab Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Fas Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Fas Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemMexican\_RCDF\_2001()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Mexican RCDF 2001")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.Mexican\_RCDF\_2001.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_Mexican_RCDF_2001}.htm)



## GetPreference {Concrete Mexican RCDF 2001}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Mexican_RCDF_2001/GetPreference_{Concrete_Mexican_RCDF_2001}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Mexican\_RCDF\_2001.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi bending

5 = Phi tension

6 = Phi compression controlled tied

7 = Phi compression controlled spiral

8 = Phi shear

9 = Pattern live load factor

10 = Utilization factor limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi bending

Value > 0

5 = Phi tension

Value > 0

6 = Phi compression controlled tied

Value > 0

7 = Phi compression controlled spiral

Value > 0

8 = Phi shear

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Utilization factor limit

Value > 0

11 = Multi-response case design

 1 = Envelopes

 2 = Step-by-step

 3 = Last step

 4 = Envelopes -- All

 5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemMexican\_RCDF\_2001()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'createSapModelobject
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Mexican RCDF 2001")

   'get preference item
      ret = SapModel.DesignConcrete.Mexican\_RCDF\_2001.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_Mexican_RCDF_2001}.htm)



## SetOverwrite {Concrete Mexican RCDF 2001}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Mexican_RCDF_2001/SetOverwrite_{Concrete_Mexican_RCDF_2001}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Mexican\_RCDF\_2001.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, k Major

6 = Effective length factor, k Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Fab Major

10 = Non-sway moment factor, Fab Minor

11 = Sway moment factor, Fas Major

12 = Sway moment factor, Fas Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway ordinary

3 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, k Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, k Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Fab Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Fab  Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Fas Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Fas Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemMexican\_RCDF\_2001()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Mexican RCDF 2001")

   'set overwrite item
      ret = SapModel.DesignConcrete.Mexican\_RCDF\_2001.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Mexican_RCDF_2001}.htm)



## SetPreference {Concrete Mexican RCDF 2001}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Mexican_RCDF_2001/SetPreference_{Concrete_Mexican_RCDF_2001}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Mexican\_RCDF\_2001.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi bending

5 = Phi tension

6 = Phi compression controlled tied

7 = Phi compression controlled spiral

8 = Phi shear

9 = Pattern live load factor

10 = Utilization factor limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi bending

Value > 0

5 = Phi tension

Value > 0

6 = Phi compression controlled tied

Value > 0

7 = Phi compression controlled spiral

Value > 0

8 = Phi shear

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Utilization factor limit

Value > 0

11 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemMexican\_RCDF\_2001()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Mexican RCDF 2001")

   'set preference item
      ret = SapModel.DesignConcrete.Mexican\_RCDF\_2001.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_Mexican_RCDF_2001}.htm)



## GetOverwrite {Concrete NTC-2008}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/NTC_2008/GetOverwrite_{Concrete_NTC_2008}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.ItalianNTC2008C.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design
procedure.

Item

This is an integer between 1 and 37, inclusive, indicating
the overwrite item considered.

1 = Framing type (beam and column)

2 = Live load reduction
factor (beam and column)

3 = Unbraced length ratio,
Major (beam and column)

4 = Unbraced length ratio,
Minor (beam and column)

5 = Effective length factor,
Beta Major (column only)

6 = Effective length factor,
Beta Minor (column only)

7 = Moment coefficient,
Cm Major (not used)

8 = Moment coefficient,
Cm Minor (not used)

9 = Nonsway moment factor,
Dns Major (not used)

10 = Nonsway moment factor,
Dns Minor (not used)

11 = Sway moment factor,
Ds Major (not used)

12 = Sway moment factor,
Ds Minor (not used)

13 = Correction factor
depending on axial load in Nominal Curvature method, Kr Major (beam and
column)

14 = Correction factor
depending on axial load in Nominal Curvature method, KPhi Major (beam
and column)

15 = Shear compressive
strut angle, TanTheta 25 = Consider torsion (beam only)

16 = Factor accounting
for creep in Nominal Curvature method, Kr Minor (beam and column)

17 = Factor accounting
for creep in Nominal Curvature method, KPhi Minor (beam and column)

18 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Major (beam and column)

19 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Minor (beam and column)

20 = Factor for contribution
of reinforcement, Ks Major (beam and column)

21 = Factor for contribution
of reinforcement, Ks Minor (beam and column)

22 = Factor for effects
of cracking, creep etc, Kc Major (beam and column)

23 = Factor for effects
of cracking, creep etc, Kc Minor (beam and column)

24 = Effective creep
coefficient, Phief (beam and column)

25 = Consider torsion
(beam only)

28 = Exposure class for crack
control

29 = Limiting crack width

30 = Age at cracking of
concrete, days

31 = Type of cement

32 = Load duration

33 = Longitudinal rebar
size top (beam only)

34 = Longitudinal rebar
size bottom (beam only)

35 = Is longitudinal rebar
ribbed?

36
= Is braced about major?

37 = Is braced about minor?

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Determined

1 = DC High

2 = DC Medium

3 = DC Low

4 = Secondary

2 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

3 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value.

4 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value.

5 = Effective length factor,
Beta Major – only applies to column design

Value >= 0; 0 means
use program determined value.

6 = Effective length factor,
Beta Minor – only applies to column design

Value >= 0; 0 means
use program determined value.

7 = Moment coefficient,
Cm Major – not used

Value >= 0; 0 means
use program determined value.

8 = Moment coefficient,
Cm Minor – not used

Value >= 0; 0 means
use program determined value.

9 = Nonsway moment factor,
Dns Major – not used

Value >= 0; 0 means
use program determined value.

10 = Nonsway moment factor,
Dns Minor – not used

  Value >=
0; 0 means use program determined value.

11 = Sway moment factor,
Ds Major – not used

  Value >=
0; 0 means use program determined value.

12 = Sway moment factor,
Ds Minor – not used

  Value >=
0; 0 means use program determined value.

13
= Correction factor depending on axial load in Nominal Curvature method,
Kr Major

Value >= 0; 0 means
use program determined value.

14 = Correction factor
depending on axial load in Nominal Curvature method, KPhi Major

Value >= 0; 0 means
use program determined value.

15 = Shear compressive
strut angle, TanTheta

Value >= 0; 0 means
use program determined value.

16 = Factor accounting
for creep in Nominal Curvature method, Kr Minor

Value >= 0; 0 means
use program determined value.

17 = Factor accounting
for creep in Nominal Curvature method, KPhi Minor

Value >= 0; 0 means
use program determined value.

18 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Major

Value >= 0; 0 means
use program determined value.

19 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Minor

Value >= 0; 0 means
use program determined value.

20 = Factor for contribution
of reinforcement, Ks Major

Value >= 0; 0 means
use program determined value.

21 = Factor for contribution
of reinforcement, Ks Minor

Value >= 0; 0 means
use program determined value.

22 = Factor for effects
of cracking, creep etc, Kc Major

Value >= 0; 0 means
use program determined value.

23 = Factor for effects
of cracking, creep etc, Kc Minor

Value >= 0; 0 means
use program determined value.

24 = Effective creep
coefficient, Phief

Value >= 0; 0 means
use program determined value.

25 = Consider torsion

0 = No

Any other value = Yes

26
= Coefficient of concrete compressive stress limit, k1

Value >=0; 0 means use
program determined value.

27 = Coefficient of steel
tensile stress limit, k3

Value >= 0; 0 means
use program determined value.

28 = Exposure class for
crack control

0 = Program Determined

1 = X0

2 = XC1

3 = XC2

4 = XC3

5 = XC4

6 = XD1

7 = XD2

8 = XS1

9 = XS2

10 = XS3

29 = Limiting crack width

Value >= 0; 0 means
use program determined value.

30 = Age at cracking of
concrete, days

Value >= 0; 0 means
use program determined value.

31 = Type of cement

0 = Program Determined

1 = Class R

2 = Class N

3 = Class S

32 = Loading duration

0 = Program Determined

1 = Short term

2 = Long term

33
= Longitudinal rebar size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

34 = Longitudinal rebar
size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

35 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

36 = Is braced about major?

0
= Program Determined

1 = No

2 = Yes

37 = Is braced about minor?

0 = Program Determined

1 = No

2 = Yes

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a concrete design
overwrite item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemItalianNTC2008C()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Italian
NTC 2008")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.ItalianNTC2008C.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version in v23.4.0.

Added items 26 through 35 in v24.2.0

Added items 36 and 37 in v25.1.0

## See Also

[SetOverwrite](SetOverwrite{Concrete_NTC_2008}.htm)



## GetPreference {Concrete NTC-2008}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/NTC_2008/GetPreference_{Concrete_NTC_2008}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.ItalianNTC2008C.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 3 and 23, inclusive, indicating
the preference item considered.

3 = Second order method

4 = Number of interaction
curves

5 = Number of interaction
points

6
= Consider minimum eccentricity

7
= Theta0

8
= Gamma steel

9 = Gamma concrete

10 = AlphaCC

11 = AlphaCT

12 = AlphaLCC

13 = AlphaLCT

14 = Pattern live load
factor

15 = Utilization factor
limit

16 = Multi-response case design

17 = GammacE

18 = Alphae (not used)

20 = Consider torsion

21
= Longitudinal rebar size top

22 = Longitudinal rebar
size bottom

23 = Is longitudinal rebar
ribbed?

Value

The value of the considered preference item.

3 = Second order method

      1
= Nominal stiffness

      2
= Nominal curvature

      3
= None

4 = Number of interaction
curves

Value >= 4 and divisible
by 4

5 = Number of interaction
points

Value >= 5 and odd

6 = Consider minimum eccentricity

0 = No

Any other value = Yes

7
= Theta0

Value
> 0

8
= Gamma steel

Value
> 0

9
= Gamma concrete

Value > 0

10 = AlphaCC

  Value >
0

11 = AlphaCT

  Value >
0

12 = AlphaLCC

  Value >
0

13 = AlphaLCT

  Value >
0

14 = Pattern live load
factor

  Value >=
0

15 = Utilization factor
limit

  Value >
0

16 = Multi-response case
design

  1 = Envelopes

  2 = Step-by-step

  3 = Last
step

  4 = Envelopes
-- All

  5 = Step-by-step
-- All

                       17
= GammacE

                             Value
> 0

18 = Alphae

                             Value
> 0

20 = Consider torsion

0 = No

Any other value = Yes

21
= Longitudinal rebar size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

22 = Longitudinal rebar
size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

23 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

## Remarks

This function retrieves the value of a concrete design
preference item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemItalianNTC2008C()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Italian
NTC 2008")

   'get preference item
      ret = SapModel.DesignConcrete.ItalianNTC2008C.GetPreference(5,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version v23.4.0.

Added items 21 – 23 in v24.2.0

## See Also

[SetPreference](SetPreference_{Concrete_NTC_2008}.htm)



## SetOverwrite{Concrete NTC-2008}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/NTC_2008/SetOverwrite{Concrete_NTC_2008}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.ItalianNTC2008C.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 37, inclusive, indicating
the overwrite item considered.

1 = Framing type (beam and column)

2 = Live load reduction
factor (beam and column)

3 = Unbraced length ratio,
Major (beam and column)

4 = Unbraced length ratio,
Minor (beam and column)

5 = Effective length factor,
Beta Major (column only)

6 = Effective length factor,
Beta Minor (column only)

7 = Moment coefficient,
Cm Major (not used)

8 = Moment coefficient,
Cm Minor (not used)

9 = Nonsway moment factor,
Dns Major (not used)

10 = Nonsway moment factor,
Dns Minor (not used)

11 = Sway moment factor,
Ds Major (not used)

12 = Sway moment factor,
Ds Minor (not used)

13 = Correction factor
depending on axial load in Nominal Curvature method, Kr Major (beam and
column)

14 = Correction factor
depending on axial load in Nominal Curvature method, KPhi Major (beam
and column)

15 = Shear compressive
strut angle, TanTheta 25 = Consider torsion (beam only)

16 = Factor accounting
for creep in Nominal Curvature method, Kr Minor (beam and column)

17 = Factor accounting
for creep in Nominal Curvature method, KPhi Minor (beam and column)

18 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Major (beam and column)

19 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Minor (beam and column)

20 = Factor for contribution
of reinforcement, Ks Major (beam and column)

21 = Factor for contribution
of reinforcement, Ks Minor (beam and column)

22 = Factor for effects
of cracking, creep etc, Kc Major (beam and column)

23 = Factor for effects
of cracking, creep etc, Kc Minor (beam and column)

24 = Effective creep
coefficient, Phief (beam and column)

25 = Consider torsion
(beam only)

26 = Coefficient of concrete compressive
stress limit, k1

27 = Coefficient of steel
tensile stress limit, k3

28 = Exposure class for
crack control

29 = Limiting crack width

30 = Age at cracking of
concrete, days

31 = Type of cement

32 = Load duration

33 = Longitudinal rebar
size top (beam only)

34 = Longitudinal rebar
size bottom (beam only)

35 = Is longitudinal rebar
ribbed?

36 = Is braced about major?

37 = Is braced about minor?

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Determined

1 = DC High

2 = DC Medium

3 = DC Low

4 = Secondary

2 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

3 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value.

4 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value.

5 = Effective length factor,
Beta Major – only applies to column design

Value >= 0; 0 means
use program determined value.

6 = Effective length factor,
Beta Minor – only applies to column design

Value >= 0; 0 means
use program determined value.

7 = Moment coefficient,
Cm Major – not used

Value >= 0; 0 means
use program determined value.

8 = Moment coefficient,
Cm Minor – not used

Value >= 0; 0 means
use program determined value.

9 = Nonsway moment factor,
Dns Major – not used

Value >= 0; 0 means
use program determined value.

10 = Nonsway moment factor,
Dns Minor – not used

  Value >=
0; 0 means use program determined value.

11 = Sway moment factor,
Ds Major – not used

  Value >=
0; 0 means use program determined value.

12 = Sway moment factor,
Ds Minor – not used

  Value >=
0; 0 means use program determined value.

13
= Correction factor depending on axial load in Nominal Curvature method,
Kr Major

Value >= 0; 0 means
use program determined value.

14 = Correction factor
depending on axial load in Nominal Curvature method, KPhi Major

Value >= 0; 0 means
use program determined value.

15 = Shear compressive
strut angle, TanTheta

Value >= 0; 0 means
use program determined value.

16 = Factor accounting
for creep in Nominal Curvature method, Kr Minor

Value >= 0; 0 means
use program determined value.

17 = Factor accounting
for creep in Nominal Curvature method, KPhi Minor

Value >= 0; 0 means
use program determined value.

18 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Major

Value >= 0; 0 means
use program determined value.

19 = Coefficient depending
on the distribution of first-order moment in both Nominal Stiffness and
Nominal Curvature methods, c Minor

Value >= 0; 0 means
use program determined value.

20 = Factor for contribution
of reinforcement, Ks Major

Value >= 0; 0 means
use program determined value.

21 = Factor for contribution
of reinforcement, Ks Minor

Value >= 0; 0 means
use program determined value.

22 = Factor for effects
of cracking, creep etc, Kc Major

Value >= 0; 0 means
use program determined value.

23 = Factor for effects
of cracking, creep etc, Kc Minor

Value >= 0; 0 means
use program determined value.

24 = Effective creep
coefficient, Phief

Value >= 0; 0 means
use program determined value.

25
= Consider torsion

0 = No

Any other value = Yes

26 = Coefficient of concrete
compressive stress limit, k1

Value >=0; 0 means use
program determined value.

27 = Coefficient of steel
tensile stress limit, k3

Value >= 0; 0 means
use program determined value.

28 = Exposure class for
crack control

0 = Program Determined

1 = X0

2 = XC1

3 = XC2

4 = XC3

5 = XC4

6 = XD1

7 = XD2

8 = XS1

9 = XS2

10 = XS3

29 = Limiting crack width

Value >= 0; 0 means
use program determined value.

30 = Age at cracking of
concrete, days

Value >= 0; 0 means
use program determined value.

31 = Type of cement

0 = Program Determined

1 = Class R

2 = Class N

3 = Class S

32 = Loading duration

0 = Program Determined

1 = Short term

2 = Long term

33
= Longitudinal rebar size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

34 = Longitudinal rebar
size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

35 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

36
= Is braced about major?

0
= Program Determined

1 = No

2 = Yes

37 = Is braced about minor?

0
= Program Determined

1 = No

2 = Yes

ItemType

This is one of the following items in the eItemType
enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the
frame object specified by the Name item.

If this item is Group, the assignment is made to all
frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made
to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite
item.

The function returns zero if the item is successfully
set, otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemItalianNTC2008C()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Italian
NTC 2008")

   'set overwrite item
      ret = SapModel.DesignConcrete.ItalianNTC2008C.SetOverwrite("8",
1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version in v23.4.0.

Added items 26 through 35 in v24.2.0

Added items 36 and 37 in v25.1.0

## See Also

[GetOverwrite](../../Steel/NTC_2008/GetOverwrite_{NTC_2008}.htm)



## SetPreference {Concrete NTC-2008}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/NTC_2008/SetPreference_{Concrete_NTC_2008}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.ItalianNTC2008C.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Item

This is an integer between 3 and 23, inclusive, indicating
the preference item considered.

3 = Second order method

4 = Number of interaction
curves

5 = Number of interaction
points

6 = Consider minimum eccentricity

7 = Theta0

8 = Gamma steel

9 = Gamma concrete

10 = AlphaCC

11 = AlphaCT

12 = AlphaLCC

13 = AlphaLCT

14 = Pattern live load
factor

15 = Utilization factor
limit

16 = Multi-response case design

17 = GammacE

18 = Alphae (not used)

20 = Consider torsion

21
= Longitudinal rebar size top

22 = Longitudinal rebar
size bottom

23 = Is longitudinal rebar
ribbed?

Value

The value of the considered preference item.

3 = Second order method

      1
= Nominal stiffness

      2
= Nominal curvature

      3
= None

4 = Number of interaction
curves

Value >= 4 and divisible
by 4

5 = Number of interaction
points

Value >= 5 and odd

6 = Consider minimum eccentricity

0 = No

Any other value = Yes

7 = Theta0

Value > 0

8 = Gamma steel

Value > 0

9 = Gamma concrete

Value > 0

10
= AlphaCC

  Value
> 0

11
= AlphaCT

  Value
> 0

12
= AlphaLCC

  Value
> 0

13
= AlphaLCT

  Value
> 0

14 = Pattern live load
factor

  Value >=
0

15 = Utilization factor
limit

  Value >
0

16 = Multi-response case
design

  1 = Envelopes

  2 = Step-by-step

  3 = Last
step

  4 = Envelopes
-- All

  5 = Step-by-step
-- All

                       17
= GammacE

                             Value
> 0

18 = Alphae

                             Value
> 0

20
= Consider torsion

0 = No

Any other value = Yes

21
= Longitudinal rebar size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

22 = Longitudinal rebar
size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

23 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

## Remarks

This function sets the value of a concrete design preference
item.

The function returns zero if the item is successfully
set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemItalianNTC2008C()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True,"R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Italian
NTC 2008")

   'set preference item
      ret = SapModel.DesignConcrete.ItalianNTC2008C.SetPreference(5,
9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version in v23.4.0.

Added items 21 – 23 in v24.2.0

## See Also

[GetPreference](GetPreference_{Concrete_NTC_2008}.htm)



## ResetOverwrites {Concrete Shell}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ResetOverwrites_{Concrete_Shell}.htm`*

# ResetOverwrites {Concrete Shell}

## Syntax

SapObject.SapModel.DesignConcreteShell.ResetOverwrites

## VB6 Procedure

Function ResetOverwrites() As Long

## Parameters

None

## Remarks

This function resets all concrete shell design overwrites to default values.

The function returns zero if the overwrites are successfully reset; otherwise it returns a nonzero value.

The function will fail if no concrete shell objects are present.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub ResetConcreteShellDesignOverwrites()

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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

Dim value As Double

Dim progdet As Boolean

ret = SapModel.DesignConcreteShell.ACI350\_20.SetPreference(5, 0.7)

ret = SapModel.DesignConcreteShell.ACI350\_20.GetPreference(5, value)

ret = SapModel.DesignConcreteShell.ACI350\_20.SetOverwrite("1", 4, 1.345)

ret = SapModel.DesignConcreteShell.ACI350\_20.GetOverwrite("1", 4, value, progdet)

ret = SapModel.DesignConcreteShell.ResetOverwrites

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0

## See Also



## ResetOverwrites {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/ResetOverwrites_{Concrete}.htm`*

# ResetOverwrites

## Syntax

SapObject.SapModel.DesignConcrete.ResetOverwrites

## VB6 Procedure

Function ResetOverwrites() As Long

## Parameters

None

## Remarks

This function resets all concrete frame design overwrites to default values.

The function returns zero if the overwrites are successfully reset; otherwise it returns a nonzero value.

The function will fail if no concrete frame objects are present.

## VBA Example

Sub ResetConcreteDesignOverwrites()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'reset concrete design overwrites
      ret = SapModel.DesignConcrete.ResetOverwrites

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## GetOverwrite {Concrete SP_63-13330-2012}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/SP_63-13330-2012/GetOverwrite.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.SP63\_13330\_2012.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design
procedure.

Item

This is an integer between 1 and 20, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Live load reduction
factor

3 = Unbraced length ratio,
Major

4 = Unbraced length ratio,
Minor

5 = Effective length factor,
K Major

6 = Effective length factor,
K Minor

7 = Moment amplification
factor, Eta Major

8 = Moment amplification
factor, Eta Minor

9 = Gammab3 for column

10 = Gammab3 for beam

11 = Consider torsion?

12 = (qsw,1\*Z1)/(Rs\*As,1)

13 = Corner rebar fraction
top

14 = Corner rebar fraction
bottom (beam only)

15 = Consider crack analysis?
(beam only)

16 = Crack width limit
full load (beam only)

17 = Crack width limit
long term (beam only)

18 = Longitudinal rebar
size top (beam only)

19 = Longitudinal rebar
size bottom (beam only)

20 = Is longitudinal rebar
ribbed? (beam only)

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Determined

1 = Sway

2 = Nonsway

2 = Live load reduction
factor

Value >=0; 0 means
use program determined value.

3 = Unbraced length ratio,
Major

Value >=0; 0 means
use program determined value.

4 = Unbraced length ratio,
Minor

Value >=0; 0 means
use program determined value.

5 = Effective length factor,
K Major

Value >=0; 0 means
use program determined value.

6 = Effective length factor,
K Minor

Value >=0; 0 means
use program determined value.

7 = Moment amplification
factor, Eta Major

Value >=0; 0 means
use program determined value.

8 = Moment amplification
factor, Eta Minor

Value >=0; 0 means
use program determined value.

9 = Gammab3 for column

Value >=0; 0 means
use program determined value.

10 = Gammab3 for beam

Value >=0; 0 means
use program determined value.

11 = Consider torsion?

0 = Program Determined

1 = No

2 = Yes

12 = (qsw,1\*Z1)/(Rs\*As,1)

0.5 <= Value <=
1.5; 0 means use program determined value.

13 = Corner rebar fraction
top

0 < Value <= 1;
0 means use program determined value.

14 = Corner rebar fraction
bottom

0 < Value <= 1;
0 means use program determined value.

14 = Corner rebar fraction
bottom

0 < Value <= 1;
0 means use program determined value.

15 = Consider crack analysis?

0 = No

Any other value = Yes

16 = Crack width limit
full load

Value >=0; 0 means use
program determined value.

17 = Crack width limit
long term

Value >=0; 0 means use
program determined value.

18 = Longitudinal rebar
size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

19 = Longitudinal rebar
size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

20 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a concrete design
overwrite item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemSP63\_13330\_2012()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("SP
63.13330.2012")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.SP63\_13330\_2012.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

Added items 15-20 in v23.4.0

## See Also

[SetOverwrite](SetOverwrite.htm)



## GetPreference {Concrete SP_63-13330-2012}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/SP_63-13330-2012/GetPreference.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.SP63\_13330\_2012.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 35, inclusive, indicating
the preference item considered.

1 = Multi-response case
design

2 = Number of interaction
curves

3 = Number of interaction
points

4 = Consider minimum eccentricity?

5 = Consider torsion?

6 = (qsw,1\*Z1)/(Rs\*As,1)

7 = Corner rebar fraction
top

8 = Corner rebar fraction
bottom

9 = Relative humidity

10 = Moisture content

11 = Gamma\_b

12 = Gamma\_bt

13 = Gamma\_b1 short term

14 = Gamma\_b1 long term

15 = Gamma\_b2

16 = Gamma\_b3 beams

17 = Gamma\_b3 columns

18 = Gamma\_b4

19 = Gamma\_b5

20 = Gamma\_S

21 = Gamma\_S1

22 = Pattern live load
factor

23 = Utilization factor
limit

24 = Live load duration
factor

25 = Snow load duration
factor

26 = Consider crack analysis

27 = Crack width limit
full load

28 = Crack width limit
long term

29 = Longitudinal rebar
size top

30 = Longitudinal rebar
size bottom

31 = Is longitudinal rebar
ribbed?

32 = Reliability factor

33 = Seismic factor mtr\_strength

34 = Seismic factor mtr\_shear

35 = Site seismicity

Value

The value of the considered preference item.

1 = Multi-response case
design

      1
= Envelopes

      2
= Step-by-step

      3
= Last step

      4
= Envelopes -- All

      5
= Step-by-step -- All

2 = Number of interaction
curves

      Value
>= 4 and divisible by 4

3 = Number of interaction
points

Value >= 5 and odd

4 = Consider minimum eccentricity?

0 = No

Any other value = Yes

5 = Consider torsion?

0 = No

Any other value = Yes

6 = (qsw,1\*Z1)/(Rs\*As,1)

0.5 <= Value <=
1.5

7 = Corner rebar fraction
top

0 < Value <= 1

8 = Corner rebar fraction
bottom

0 < Value <= 1

9 = Relative humidity

0 <= Value <= 100

10 = Moisture content

0 <= Value <= 1

11 = Gamma\_b

Value > 0

12 = Gamma\_bt

Value > 0

13 = Gamma\_b1 short term

Value > 0

14 = Gamma\_b1 long term

Value > 0

15 = Gamma\_b2

Value > 0

16 = Gamma\_b3 beams

Value > 0

17 = Gamma\_b3 columns

Value > 0

18 = Gamma\_b4

Value > 0

19 = Gamma\_b5

Value > 0

20 = Gamma\_S

Value > 0

21 = Gamma\_S1

Value > 0

22 = Pattern live load
factor

Value >= 0

23 = Utilization factor
limit

Value > 0

24 = Live load duration
factor

Value >= 0

25 = Snow load duration
factor

Value >= 0

26 = Consider crack analysis?

0 = No

Any other value = Yes

27 = Crack width limit
full load

Value >= 0

28 = Crack width limit
long term

Value >= 0

29 = Longitudinal rebar
size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

30 = Longitudinal rebar
size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

31 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

32 = Reliability factor

Value > 0

33 = Seismic factor mtr\_strength

Value > 0

34 = Seismic factor mtr\_shear

Value > 0

35 = Site seismicity

      1
= Site seismicity 9

      2
= Site seismicity 8

      3
= Site seismicity 7

      4
= Non seismic

## Remarks

This function retrieves the value of a concrete design
preference item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemSP63\_13330\_2012()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("SP
63.13330.2012")

   'get preference item
      ret = SapModel.DesignConcrete.SP63\_13330\_2012.GetPreference(11,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

Added items 24-35 in v23.4.0

## See Also

[SetPreference](SetPreference.htm)



## SetOverwrite {Concrete SP_63-13330-2012}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/SP_63-13330-2012/SetOverwrite.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.SP63\_13330\_2012.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType as eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 20, inclusive, indicating
the overwrite item considered.

1 = Framing type (beam
and column)

2 = Live load reduction
factor (beam and column)

3 = Unbraced length ratio,
Major (beam and column)

4 = Unbraced length ratio,
Minor (beam and column)

5 = Effective length factor,
K Major (column only)

6 = Effective length factor,
K Minor (column only)

7 = Moment amplification
factor, Eta Major (column only)

8 = Moment amplification
factor, Eta Minor (column only)

9 = Gammab3 for column

10 = Gammab3 for beam

11 = Consider torsion? (beam
only)

12 = (qsw,1\*Z1)/(Rs\*As,1) (beam
only)

13 = Corner rebar fraction
top (beam only)

14 = Corner rebar fraction
bottom (beam only)

15 = Consider crack analysis?
(beam only)

16 = Crack width limit
full load (beam only)

17 = Crack width limit
long term (beam only)

18 = Longitudinal rebar
size top (beam only)

19 = Longitudinal rebar
size bottom (beam only)

20 = Is longitudinal rebar
ribbed? (beam only)

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Determined

1 = Sway

2 = Nonsway

2 = Live load reduction
factor

Value >=0; 0 means
use program determined value.

3 = Unbraced length ratio,
Major

Value >=0; 0 means
use program determined value.

4 = Unbraced length ratio,
Minor

Value >=0; 0 means
use program determined value.

5 = Effective length factor,
K Major

Value >=0; 0 means
use program determined value.

6 = Effective length factor,
K Minor

Value >=0; 0 means
use program determined value.

7 = Moment amplification
factor, Eta Major

Value >=0; 0 means
use program determined value.

8 = Moment amplification
factor, Eta Minor

Value >=0; 0 means
use program determined value.

9 = Gammab3 for column

Value >=0; 0 means
use program determined value.

10 = Gammab3 for beam

Value >=0; 0 means
use program determined value.

11 = Consider torsion?

0 = Program Determined

1 = No

2 = Yes

12 = (qsw,1\*Z1)/(Rs\*As,1)

0.5 <= Value <=
1.5; 0 means use program determined value.

13 = Corner rebar fraction
top

0 < Value <= 1;
0 means use program determined value.

14 = Corner rebar fraction
bottom

0 < Value <= 1;
0 means use program determined value.

15 = Consider crack analysis?

0 = No

Any other value = Yes

16 = Crack width limit
full load

Value >=0; 0 means use
program determined value.

17 = Crack width limit
long term

Value >=0; 0 means use
program determined value.

18 = Longitudinal rebar
size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

19 = Longitudinal rebar
size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

20 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

ItemType

This is one of the following items in the eItemType
enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the
frame object specified by the Name item.

If this item is Group, the assignment is made to all
frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made
to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite
item.

The function returns zero if the item is successfully
set, otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemSP63\_13330\_2012()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("SP
63.13330.2012")

   'set overwrite item
      ret = SapModel.DesignConcrete.SP63\_13330\_2012.SetOverwrite("8",
1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

Added items 15-20 in v23.4.0

## See Also

[GetOverwrite](GetOverwrite.htm)



## SetPreference {Concrete SP_63-13330-2012}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/SP_63-13330-2012/SetPreference.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.SP63\_13330\_2012.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 35, inclusive, indicating
the preference item considered.

1 = Multi-response case
design

2 = Number of interaction
curves

3 = Number of interaction
points

4 = Consider minimum eccentricity?

5 = Consider torsion?

6 = (qsw,1\*Z1)/(Rs\*As,1)

7 = Corner rebar fraction
top

8 = Corner rebar fraction
bottom

9 = Relative humidity

10 = Moisture content

11 = Gamma\_b

12 = Gamma\_bt

13 = Gamma\_b1 short term

14 = Gamma\_b1 long term

15 = Gamma\_b2

16 = Gamma\_b3 beams

17 = Gamma\_b3 columns

18 = Gamma\_b4

19 = Gamma\_b5

20 = Gamma\_S

21 = Gamma\_S1

22 = Pattern live load
factor

23 = Utilization factor
limit

24 = Live load duration
factor

25 = Snow load duration
factor

26 = Consider crack analysis

27 = Crack width limit
full load

28 = Crack width limit
long term

29 = Longitudinal rebar
size top

30 = Longitudinal rebar
size bottom

31 = Is longitudinal rebar
ribbed?

32 = Reliability factor

33 = Seismic factor mtr\_strength

34 = Seismic factor mtr\_shear

35 = Site seismicity

Value

The value of the considered preference item.

1 = Multi-response case
design

      1
= Envelopes

      2
= Step-by-step

      3
= Last step

      4
= Envelopes -- All

      5
= Step-by-step -- All

2 = Number of interaction
curves

      Value
>= 4 and divisible by 4

3 = Number of interaction
points

Value >= 5 and odd

4 = Consider minimum eccentricity?

0 = No

Any other value = Yes

5 = Consider torsion?

0 = No

Any other value = Yes

6 = (qsw,1\*Z1)/(Rs\*As,1)

0.5 <= Value <=
1.5

7 = Corner rebar fraction
top

0 < Value <= 1

8 = Corner rebar fraction
bottom

0 < Value <= 1

9 = Relative humidity

0 <= Value <= 100

10 = Moisture content

0 <= Value <= 1

11 = Gamma\_b

Value > 0

12 = Gamma\_bt

Value > 0

13 = Gamma\_b1 short term

Value > 0

14 = Gamma\_b1 long term

Value > 0

15 = Gamma\_b2

Value > 0

16 = Gamma\_b3 beams

Value > 0

17 = Gamma\_b3 columns

Value > 0

18 = Gamma\_b4

Value > 0

19 = Gamma\_b5

Value > 0

20 = Gamma\_S

Value > 0

21 = Gamma\_S1

Value > 0

22 = Pattern live load
factor

Value >= 0

23 = Utilization factor
limit

Value > 0

24 = Live load duration
factor

Value >= 0

25 = Snow load duration
factor

Value >= 0

26 = Consider crack analysis?

0 = No

Any other value = Yes

27 = Crack width limit
full load

Value >= 0

28 = Crack width limit
long term

Value >= 0

29 = Longitudinal rebar
size top

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

30
= Longitudinal rebar size bottom

      1
= #2

      2
= #3

      3
= #4

      4
= #5

      5
= #6

      6
= #7

      7
= #8

      8
= #9

      9
= #10

      10
= #11

      11
= #14

      12
= #18

      13
= 10M

      14
= 15M

      15
= 20M

      16
= 25M

      17
= 30M

      18
= 35M

      19
= 45M

      20
= 55M

      21
= 6d

      22
= 8d

      23
= 10d

      24
= 12d

      25
= 14d

      26
= 16d

      27
= 20d

      28
= 25d

      29
= 26d

      30
= 28d

      31
= N12

      32
= N16

      33
= N20

      34
= N24

      35
= N28

      36
= N32

      37
= N36

31 = Is longitudinal rebar
ribbed?

0 = No

Any other value = Yes

32 = Reliability factor

Value > 0

33 = Seismic factor mtr\_strength

Value > 0

34 = Seismic factor mtr\_shear

Value > 0

35 = Site seismicity

      1
= Site seismicity 9

      2
= Site seismicity 8

      3
= Site seismicity 7

      4
= Non seismic

## Remarks

This function retrieves the value of a concrete design
preference item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemSP63\_13330\_2012()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True,"R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("SP63.13330.2012")

   'set preference item
      ret = SapModel.DesignConcrete.SP63\_13330\_2012.SetPreference(11,
1.2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

Added items 24-35 in v23.4.0

## See Also

[GetPreference](GetPreference.htm)



## SetCode {Concrete Shell}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/SetCode_{Concrete_Shell}.htm`*

# SetCode (for Concrete Shell Design)

## Syntax

SapObject.SapModel.DesignConcreteShell.SetCode

## VB6 Procedure

Function SetCode(ByVal CodeName As String) As Long

## Parameters

CodeName

This is one of the following concrete shell design code names.

ACI 350-20

Eurocode 2-2004

## Remarks

This function sets the concrete shell design code.

The function returns zero if the code is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteShellDesignCode()
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

   'create blank model
       ret = SapModel.File.NewBlank()

   'set concrete design code
      ret = SapModel.DesignConcreteShell.SetCode("Eurocode 2-2004")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.0.0

Updated to include ACI 350-20 in list of code names in version 26.0.0

## See Also

[GetCode {Concrete Shell}](GetCode_{Concrete_Shell}.htm)



## SetCode {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/SetCode_{Concrete}.htm`*

# SetCode

## Syntax

SapObject.SapModel.DesignConcrete.SetCode

## VB6 Procedure

Function SetCode(ByVal CodeName As String) As Long

## Parameters

CodeName

This is one of the following concrete design code names.

AASHTO LRFD 2014
AASHTO LRFD 2012
AASHTO Concrete 07
ACI 318-14
ACI 318-11
ACI 318-08/IBC2009
AS 3600-09
BS8110 97
Chinese 2010
CSA A23.3-14
CSA A23.3-04
Eurocode 2-2004
Hong Kong CP 2013
Indian IS 456-2000
Italian NTC 2008
KBC 2009
Mexican RCDF 2004
NZS 3101:2006
Singapore CP 65:99
SP 63.13330.2012
TS 500-2000

## Remarks

This function sets the concrete design code.

The function returns zero if the code is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignCode()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("ACI 318-14")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Updated list of available codes in v17.3.0.

Removed older codes which have been removed from the program in v18.0.0.

Updated list of available codes in v19.1.0.

## See Also

[GetCode](GetCode_{Concrete}.htm)



## SetComboAutoGenerate {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/SetComboAutoGenerate_{Concrete}.htm`*

# SetComboAutoGenerate

## Syntax

SapObject.SapModel.DesignConcrete.SetComboAutoGenerate

## VB6 Procedure

Function SetComboAutoGenerate(ByVal AutoGenerate As Boolean) As Long

## Parameters

AutoGenerate

If this item is True, the option to automatically generate code-based design load combinations for concrete frame design is turned on. If it is False, the option is turned off.

## Remarks

This function turns on or off the option to automatically generate code-based design load combinations for concrete frame design.

The function returns zero if the options are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignComboAutoGenerate()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'set option to not auto generate code-based design load combinations
      ret = SapModel.DesignConcrete.SetComboAutoGenerate(False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 18.1.0.

## See Also

[GetComboAutoGenerate](GetComboAutoGenerate_{Concrete}.htm)



## SetComboStrength {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/SetComboStrength_{Concrete}.htm`*

# SetComboStrength

## Syntax

SapObject.SapModel.DesignConcrete.SetComboStrength

## VB6 Procedure

Function SetComboStrength(ByVal Name As String, ByVal Selected As Boolean) As Long

## Parameters

Name

The name of an existing load combination.

Selected

If this item is True, the specified load combination is selected as a design combination for concrete strength design. If it is False, the combination is not selected for concrete strength design.

## Remarks

This function selects or deselects a load combination for concrete strength design.

The function returns zero if the selection status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignComboStrength()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim NumberNames As Long
      Dim MyName() As String
      Dim Selected As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section properties
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default concrete design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(False, True, False, False)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName)

   'select combos for concrete strength design
      For i = 0 To NumberNames - 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignConcrete.SetComboStrength(MyName(i), Selected)
      Next i

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetComboStrength](GetComboStrength_{Concrete}.htm)



## SetDesignSection {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/SetDesignSection_{Concrete}.htm`*

# SetDesignSection

## Syntax

SapObject.SapModel.DesignConcrete.SetDesignSection

## VB6 Procedure

Function SetDesignSection(ByVal Name As String, ByVal PropName As String, ByVal LastAnalysis As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

PropName

The name of an existing frame section property to be used as the design section for the specified frame objects. This item applies only when LastAnalysis = False.

LastAnalysis

If this item is True, the design section for the specified frame objects is reset to the last analysis section for the frame object. If it is False, the design section is set to that specified by PropName.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function modifies the design section for all specified frame objects that have a concrete frame design procedure.

The function returns zero if the design section is successfully modified; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignSection()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section properties
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)
      ret = SapModel.PropFrame.SetRectangle("R2", "4000Psi", 20, 16)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'set design section
      ret = SapModel.DesignConcrete.SetDesignSection("8", "R2", False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetDesignSection](GetDesignSection_{Concrete}.htm)



## GetOverwrite {Concrete Singapore CP 6599}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Singapore_CP_6599/GetOverwrite_{Concrete_Singapore_CP_6599}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Singapore\_CP\_65\_99.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, Beta Major

6 = Effective length factor, Beta Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemSingapore\_CP\_65\_99()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Singapore CP 65:99")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.Singapore\_CP\_65\_99.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_Singapore_CP_6599}.htm)



## GetPreference {Concrete Singapore CP 6599}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Singapore_CP_6599/GetPreference_{Concrete_Singapore_CP_6599}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Singapore\_CP\_65\_99.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Gamma steel

5 = Gamma concrete

6 = Gamma concrete shear

7 = Pattern live load factor

8 = Utilization factor limit

9 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Gamma steel

Value > 0

5 = Gamma concrete

Value > 0

6 = Gamma concrete shear

Value > 0

7 = Pattern live load factor

Value >= 0

8 = Utilization factor limit

Value > 0

9 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemSingapore\_CP\_65\_99()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'createSapModelobject
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Singapore CP 65:99")

   'get preference item
      ret = SapModel.DesignConcrete.Singapore\_CP\_65\_99.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_Singapore_CP_6599}.htm)



## SetOverwrite {Concrete Singapore CP 6599}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Singapore_CP_6599/SetOverwrite_{Concrete_Singapore_CP_6599}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Singaopre\_CP\_65\_99.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, Beta Major

6 = Effective length factor, Beta Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway

2 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemSingapore\_CP\_65\_99()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'createSapModelobject
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Singapore CP 65:99")

   'set overwrite item
      ret = SapModel.DesignConcrete.Singapore\_CP\_65\_99.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Singapore_CP_6599}.htm)



## SetPreference {Concrete Singapore CP 6599}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/Singapore_CP_6599/SetPreference_{Concrete_Singapore_CP_6599}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Singapore\_CP\_65\_99.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 9, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Gamma steel

5 = Gamma concrete

6 = Gamma concrete shear

7 = Pattern live load factor

8 = Utilization factor limit

9 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Gamma steel

Value > 0

5 = Gamma concrete

Value > 0

6 = Gamma concrete shear

Value > 0

7 = Pattern live load factor

Value >= 0

8 = Utilization factor limit

Value > 0

9 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemSingapore\_CP\_65\_99()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("Singapore CP 65:99")

   'set preference item
      ret = SapModel.DesignConcrete.Singapore\_CP\_65\_99.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_Singapore_CP_6599}.htm)



## StartDesign {Concrete Shell}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/StartDesign_{Concrete_Shell}.htm`*

# StartDesign {Concrete Shell}

## Syntax

SapObject.SapModel.DesignConcreteShell.StartDesign

## VB6 Procedure

Function StartDesign() As Long

## Parameters

None

## Remarks

This function starts the concrete shell design.

The function returns zero if the concrete shell design is successfully started; otherwise it returns a nonzero value.

The function will fail if no concrete shell objects are present. It also will fail if analysis results are not available.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub StartConcreteShellDesign()

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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fluid", eLoadPatternType.EarthHydrostatic)

'add point load

Dim LoadValue() As Double

ReDim LoadValue(5)

LoadValue(1) = 10

ret = SapModel.PointObj.SetLoadForce("14", "DEAD", LoadValue)

'add combo

ret = SapModel.RespCombo.Add("COMB1", 1)

ret = SapModel.RespCombo.Add("COMB2", 1)

ret = SapModel.RespCombo.Add("COMB3", 1)

ret = SapModel.RespCombo.Add("COMB4", 1)

'add load case to combo

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.1)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.2)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.3)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.4)

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

Dim RequestName As String

Dim GroupList() As String

Dim ComboList() As String

Dim AutoCombo As Boolean

Dim AutoComboCaseList() As String

Dim NewName As String

Dim NumberRequest As Integer

Dim RequestList() As String

Dim NumberGroup As Integer

Dim NumberCombo As Integer

RequestName = "R1"

ReDim RequestList(1)

RequestList(0) = ""

RequestList(1) = ""

ReDim GroupList(1)

ReDim ComboList(1)

ReDim AutoComboCaseList(2)

GroupList(1) = "GROUP1"

ComboList(1) = "COMB1"

AutoCombo = True

AutoComboCaseList(1) = "DEAD"

AutoComboCaseList(2) = "Fluid"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

NewName = "R11"

ret = SapModel.DesignConcreteShell.DesignRequest.ChangeName(RequestName, NewName)

RequestName = "R2"

GroupList(1) = "GROUP2"

ComboList(1) = "COMB2"

AutoCombo = False

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

RequestName = "R123"

ReDim GroupList(3)

ReDim ComboList(3)

GroupList(1) = "GROUP1"

GroupList(2) = "GROUP2"

GroupList(3) = "GROUP3"

ComboList(1) = "COMB1"

ComboList(2) = "COMB2"

ComboList(3) = "COMB3"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetRequestList(NumberRequest, RequestList)

RequestName = "R123"

ReDim GroupList(0)

ReDim ComboList(0)

ret = SapModel.DesignConcreteShell.DesignRequest.GetGroupList(RequestName, NumberGroup, GroupList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetComboList(RequestName, NumberCombo, ComboList)

ReDim GroupList(2)

GroupList(1) = "GROUP3"

GroupList(2) = "GROUP4"

ret = SapModel.DesignConcreteShell.DesignRequest.SetGroup(RequestName, GroupList)

ReDim ComboList(2)

ComboList(1) = "COMB3"

ComboList(2) = "COMB4"

ret = SapModel.DesignConcreteShell.DesignRequest.SetCombo(RequestName, ComboList)

Dim AutoComboCaseList1() As String

ReDim AutoComboCaseList1(2)

AutoComboCaseList1(1) = "DEAD"

AutoComboCaseList1(2) = "Fluid"

RequestName = "R2"

ret = SapModel.DesignConcreteShell.DesignRequest.SetAutoCombo(RequestName, AutoComboCaseList1)

Dim value As Double

Dim progdet As Boolean

ret = SapModel.DesignConcreteShell.ACI350\_20.SetPreference(5, 0.7)

ret = SapModel.DesignConcreteShell.ACI350\_20.GetPreference(5, value)

ret = SapModel.DesignConcreteShell.ACI350\_20.SetOverwrite("1", 4, 1.345)

ret = SapModel.DesignConcreteShell.ACI350\_20.GetOverwrite("1", 4, value, progdet)

'save model

ret = SapModel.File.Save("C:\CSiAPIexample\x.sdb")

'run model (this will create the analysis model)

ret = SapModel.Analyze.RunAnalysis

'design concrete shell elements

ret = SapModel.DesignConcreteShell.StartDesign

   'close Sap2000
      SapObject.ApplicationExit(False)
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0.

## See Also



## StartDesign {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/StartDesign_{Concrete}.htm`*

# StartDesign

## Syntax

SapObject.SapModel.DesignConcrete.StartDesign

## VB6 Procedure

Function StartDesign() As Long

## Parameters

None

## Remarks

This function starts the concrete frame design.

The function returns zero if the concrete frame design is successfully started; otherwise it returns a nonzero value.

The function will fail if no concrete frame objects are present. It also will fail if analysis results are not available.

## VBA Example

Sub StartConcreteDesign()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## GetOverwrite {Concrete TCVN_5574-2018}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/TCVN_5574_2018/GetOverwrite.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.TCVN\_5574\_2018.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 21, inclusive, indicating the overwrite item considered.

1 = Framing type (beam and column)

2 = Live load reduction factor (beam and column)

3 = Unbraced length ratio, Major (beam and column)

4 = Unbraced length ratio, Minor (beam and column)

5 = Effective length factor, K Major (columns only)

6 = Effective length factor, K Minor (columns only)

7 = Moment amplification factor, Eta Major (not used)

8 = Moment amplification factor, Eta Minor (not used)

9 = Gammab3 for column (columns only)

10 = Gammab3 for beam (columns only)

11 = Consider torsion? (beams only)

12 = (qsw,1\*Z1) / (Rs\*As,1)

13 = Corner rebar fraction top (beams only)

14 = Corner rebar fraction bottom (beams only)

15 = Consider minimum eccentricity (beams only)

16 = Consider crack analysis? (beams only)

17 = Crack width limit full load (beams only)

18 = Crack width limit long term (beams only)

19 = Longitudinal rebar size top (beams only)

20 = Longitudinal rebar size bottom (beams only)

21 = Is longitudinal rebar ribbed? (beams only)

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Determined

1 = DC High

2 = DC Medium

3 - DC Low

4 Secondary

2 = Live load reduction factor

Value >=0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >=0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >=0; 0 means use program determined value.

5 = Effective length factor, K Major - only applies to column design

Value >=0; 0 means use program determined value.

6 = Effective length factor, K Minor - only applies to column design

Value >=0; 0 means use program determined value.

7 = Moment amplification factor, Eta Major

Value >=0; 0 means use program determined value.

8 = Moment amplification factor, Eta Minor

Value >=0; 0 means use program determined value.

9 = Gammab3 (columns only)

Value >=0; 0 means use program determined value.

10 = Gammab3 (beams only)

Value >=0; 0 means use program determined value.

11 = Consider torsion? (beams only)

0 = Program Determined

Any other value = Yes

12 = (qsw,1\*Z1) / (Rs\*As,1)

0.5 <= Value <= 1.5; 0 means use program determined value.

13 = Corner rebar fraction top  (beams only)

0 < Value <= 1; 0 means use program determined value.

14 = Corner rebar fraction bottom  (beams only)

0 < Value <= 1; 0 means use program determined value.

15 = Consider minimum eccentricity  (columns only)

0 = No

Any other value = Yes

16= Consider crack analysis?

0 = No

Any other value = Yes

17 = Crack width limit full load (beams only)

Value >=0; 0 means use program determined value.

18 = Crack width limit long term (beams only)

Value >=0; 0 means use program determined value.

19 = Longitudinal rebar size top

      1 = #2

      2 = #3

      3 = #4

      4 = #5

      5 = #6

      6 = #7

      7 = #8

      8 = #9

      9 = #10

      10 = #11

      11 = #14

      12 = #18

      13 = 10M

      14 = 15M

      15 = 20M

      16 = 25M

      17 = 30M

      18 = 35M

      19 = 45M

      20 = 55M

      21 = 6d

      22 = 8d

      23 = 10d

      24 = 12d

      25 = 14d

      26 = 16d

      27 = 20d

      28 = 25d

      29 = 26d

      30 = 28d

      31 = N12

      32 = N16

      33 = N20

      34 = N24

      35 = N28

      36 = N32

      37 = N36

20 = Longitudinal rebar size bottom

      1 = #2

      2 = #3

      3 = #4

      4 = #5

      5 = #6

      6 = #7

      7 = #8

      8 = #9

      9 = #10

      10 = #11

      11 = #14

      12 = #18

      13 = 10M

      14 = 15M

      15 = 20M

      16 = 25M

      17 = 30M

      18 = 35M

      19 = 45M

      20 = 55M

      21 = 6d

      22 = 8d

      23 = 10d

      24 = 12d

      25 = 14d

      26 = 16d

      27 = 20d

      28 = 25d

      29 = 26d

      30 = 28d

      31 = N12

      32 = N16

      33 = N20

      34 = N24

      35 = N28

      36 = N32

      37 = N36

21 = Is longitudinal rebar ribbed?

0 = No

Any other value = Yes

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemTCVN55742018()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("TCVN 5574:2018")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.TCVN\_5574\_2018.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v27.0.0.

## See Also

[SetOverwrite](SetOverwrite.htm)



## GetPreference {Concrete TCVN_5574-2018}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/TCVN_5574_2018/GetPreference.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.TCVN\_5574\_2018.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 34, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Number of interaction curves

3 = Number of interaction points

4 = Consider minimum eccentricity?

5 = Consider torsion?

6 = (qsw,1\*Z1) / (Rs\*As,1)

7 = Corner rebar fraction top

8 = Corner rebar fraction bottom

9 = Relative humidity (%)

10 = Moisture content (fraction)

11 = Gamma\_b

12 = Gamma\_bt

13 = Gamma\_b1 short term loadings

14 = Gamma\_b1 long term loadings

15 = Gamma\_b2

16 = Gamma\_b3 beams

17 = Gamma\_b3 columns

18 = Gamma\_b4

19 = Gamma\_S

20 = Gamma\_S1

21 = Pattern live load factor

22 = Utilization factor limit

23 = Live load duration factor

24 = Snow load duration factor

25 = Reliability factor, gamma\_n

26 = Seismic factor mtr\_Flexure

27 = Seismic factor mtr\_Shear

28 = Site seismicity

29 = Consider crack analysis

30 = Crack width limit full load, acrc,u

31 = Crack width limit long term, acrc,u

32 = Longitudinal rebar size top

33 = Longitudinal rebar size bottom

34 = Is longitudinal rebar ribbed?

Value

The value of the considered preference item.

1 = Multi-response case design

      1 = Envelopes

      2 = Step-by-step

      3 = Last step

      4 = Envelopes -- All

      5 = Step-by-step -- All

2 = Number of interaction curves

      Value >= 4 and divisible by 4

3 = Number of interaction points

Value >= 5 and odd

4 = Consider minimum eccentricity?

0 = No

Any other value = Yes

5 = Consider torsion?

0 = No

Any other value = Yes

6 = (qsw,1\*Z1) / (Rs\*As,1)

0.5 <= Value <= 1.5

7 = Corner rebar fraction top

0 < Value <= 1

8 = Corner rebar fraction bottom

0 < Value <= 1

9 = Relative humidity (%)

0 <= Value <= 100

10 = Moisture content

0 <= Value <= 1

11 = Gamma\_b

Value > 0

12 = Gamma\_bt

Value > 0

13 = Gamma\_b1 short term loadings

Value > 0

14 = Gamma\_b1 long term loadings

Value > 0

15 = Gamma\_b2

Value > 0

16 = Gamma\_b3 beams

Value > 0

17 = Gamma\_b3 columns

Value > 0

18 = Gamma\_b4

Value > 0

19 = Gamma\_S

Value > 0

20 = Gamma\_S1

Value > 0

21 = Pattern live load factor

Value >= 0

22 = Utilization factor limit

Value > 0

23 = Live load duration factor

Value >= 0

24 = Snow load duration factor

Value >= 0

25 = Reliability factor

       Value > 0

26 = Seismic factor mtr\_Flexure

       Value > 0

27 = Seismic factor mtr\_Shear

       Value > 0

28 = Site seismicity>

      1 = Site seismicity 9>

      2 = Site seismicity 8>

      3 = Site seismicity 7>

      4 = Non seismic

29 = Consider crack analysis?

0 = No

Any other value = Yes

30 = Crack width limit full load

Value >= 0

31 = Crack width limit long term

Value >= 0

32 = Longitudinal rebar size top

      1 = #2

      2 = #3

      3 = #4

      4 = #5

      5 = #6

      6 = #7

      7 = #8

      8 = #9

      9 = #10

      10 = #11

      11 = #14

      12 = #18

      13 = 10M

      14 = 15M

      15 = 20M

      16 = 25M

      17 = 30M

      18 = 35M

      19 = 45M

      20 = 55M

      21 = 6d

      22 = 8d

      23 = 10d

      24 = 12d

      25 = 14d

      26 = 16d

      27 = 20d

      28 = 25d

      29 = 26d

      30 = 28d

      31 = N12

      32 = N16

      33 = N20

      34 = N24

      35 = N28

      36 = N32

      37 = N36

33 = Longitudinal rebar size bottom

      1 = #2

      2 = #3

      3 = #4

      4 = #5

      5 = #6

      6 = #7

      7 = #8

      8 = #9

      9 = #10

      10 = #11

      11 = #14

      12 = #18

      13 = 10M

      14 = 15M

      15 = 20M

      16 = 25M

      17 = 30M

      18 = 35M

      19 = 45M

      20 = 55M

      21 = 6d

      22 = 8d

      23 = 10d

      24 = 12d

      25 = 14d

      26 = 16d

      27 = 20d

      28 = 25d

      29 = 26d

      30 = 28d

      31 = N12

      32 = N16

      33 = N20

      34 = N24

      35 = N28

      36 = N32

      37 = N36

34 = Is longitudinal rebar ribbed?

0 = No

Any other value = Yes

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemTCVN55742018()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("TCVN 5574:2018")

   'get preference item
      ret = SapModel.DesignConcrete.TCVN\_5574\_2018.GetPreference(5, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v27.0.0.

## See Also

[SetPreference](SetPreference.htm)



## SetOverwrite {Concrete TCVN_5574-2018}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/TCVN_5574_2018/SetOverwrite.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.TCVN\_5574\_2018.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 21, inclusive, indicating the overwrite item considered.

1 = Framing type (beam and column)

2 = Live load reduction factor (beam and column)

3 = Unbraced length ratio, Major (beam and column)

4 = Unbraced length ratio, Minor (beam and column)

5 = Effective length factor, K Major (columns only)

6 = Effective length factor, K Minor (columns only)

7 = Moment amplification factor, Eta Major (not used)

8 = Moment amplification factor, Eta Minor (not used)

9 = Gammab3 for column (columns only)

10 = Gammab3 for beam (columns only)

11 = Consider torsion? (beams only)

12 = (qsw,1\*Z1) / (Rs\*As,1)

13 = Corner rebar fraction top (beams only)

14 = Corner rebar fraction bottom (beams only)

15 = Consider minimum eccentricity (beams only)

16 = Consider crack analysis? (beams only)

17 = Crack width limit full load (beams only)

18 = Crack width limit long term (beams only)

19 = Longitudinal rebar size top (beams only)

20 = Longitudinal rebar size bottom (beams only)

21 = Is longitudinal rebar ribbed? (beams only)

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Determined

1 = DC High

2 = DC Medium

3 - DC Low

4 Secondary

2 = Live load reduction factor

Value >=0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >=0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >=0; 0 means use program determined value.

5 = Effective length factor, K Major - only applies to column design

Value >=0; 0 means use program determined value.

6 = Effective length factor, K Minor- only applies to column design

Value >=0; 0 means use program determined value.

7 = Moment amplification factor, Eta Major

Value >=0; 0 means use program determined value.

8 = Moment amplification factor, Eta Minor

Value >=0; 0 means use program determined value.

9 = Gammab3 (columns only)

Value >=0; 0 means use program determined value.

10 = Gammab3 (beams only)

Value >=0; 0 means use program determined value.

11 = Consider torsion?

0 = Program Determined

Any other value = Yes

12 = (qsw,1\*Z1) / (Rs\*As,1)

0.5 <= Value <= 1.5; 0 means use program determined value.

13 = Corner rebar fraction top (beams only)

0 < Value <= 1; 0 means use program determined value.

14 = Corner rebar fraction bottom (beams only)

0 < Value <= 1; 0 means use program determined value.

15 = Consider minimum eccentricity  (columns only)

0 = No

Any other value = Yes

16 = Consider crack analysis? (beams only)

0 = No

Any other value = Yes

17 = Crack width limit full load (beams only)

Value >=0; 0 means use program determined value.

18 = Crack width limit long term (beams only)

Value >=0; 0 means use program determined value.

19 = Longitudinal rebar size top

      1 = #2

      2 = #3

      3 = #4

      4 = #5

      5 = #6

      6 = #7

      7 = #8

      8 = #9

      9 = #10

      10 = #11

      11 = #14

      12 = #18

      13 = 10M

      14 = 15M

      15 = 20M

      16 = 25M

      17 = 30M

      18 = 35M

      19 = 45M

      20 = 55M

      21 = 6d

      22 = 8d

      23 = 10d

      24 = 12d

      25 = 14d

      26 = 16d

      27 = 20d

      28 = 25d

      29 = 26d

      30 = 28d

      31 = N12

      32 = N16

      33 = N20

      34 = N24

      35 = N28

      36 = N32

      37 = N36

20 = Longitudinal rebar size bottom

      1 = #2

      2 = #3

      3 = #4

      4 = #5

      5 = #6

      6 = #7

      7 = #8

      8 = #9

      9 = #10

      10 = #11

      11 = #14

      12 = #18

      13 = 10M

      14 = 15M

      15 = 20M

      16 = 25M

      17 = 30M

      18 = 35M

      19 = 45M

      20 = 55M

      21 = 6d

      22 = 8d

      23 = 10d

      24 = 12d

      25 = 14d

      26 = 16d

      27 = 20d

      28 = 25d

      29 = 26d

      30 = 28d

      31 = N12

      32 = N16

      33 = N20

      34 = N24

      35 = N28

      36 = N32

      37 = N36

21 = Is longitudinal rebar ribbed?

0 = No

Any other value = Yes

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemTCVN55742018()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("TCVN 5574:2018")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'set overwrite item
      ret = SapModel.DesignConcrete.TCVN\_5574\_2018.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v27.0.0.

## See Also

[GetOverwrite](GetOverwrite.htm)



## SetPreference {Concrete TCVN_5574-2018}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/TCVN_5574_2018/SetPreference.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.TCVN\_5574\_2018.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 34, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Number of interaction curves

3 = Number of interaction points

4 = Consider minimum eccentricity?

5 = Consider torsion?

6 = (qsw,1\*Z1) / (Rs\*As,1)

7 = Corner rebar fraction top

8 = Corner rebar fraction bottom

9 = Relative humidity (%)

10 = Moisture content

11 = Gamma\_b

12 = Gamma\_bt

13 = Gamma\_b1 short term

14 = Gamma\_b1 long term

15 = Gamma\_b2

16 = Gamma\_b3 beams

17 = Gamma\_b3 columns

18 = Gamma\_b4

19 = Gamma\_S

20 = Gamma\_S1

21 = Pattern live load factor

22 = Utilization factor limit

23 = Live load duration factor

24 = Snow load duration factor

25 = Reliability factor

26 = Seismic factor mtr\_strength

27 = Seismic factor mtr\_shear

28 = Site seismicity

29 = Consider crack analysis

30 = Crack width limit full load, acrc,u

31 = Crack width limit long term, acrc,u

32 = Longitudinal rebar size top

33 = Longitudinal rebar size bottom

34 = Is longitudinal rebar ribbed?

Value

The value of the considered preference item.

1 = Multi-response case design

      1 = Envelopes

      2 = Step-by-step

      3 = Last step

      4 = Envelopes -- All

      5 = Step-by-step -- All

2 = Number of interaction curves

      Value >= 4 and divisible by 4

3 = Number of interaction points

Value >= 5 and odd

4 = Consider minimum eccentricity?

0 = No

Any other value = Yes

5 = Consider torsion?

0 = No

Any other value = Yes

6 = (qsw,1\*Z1) / (Rs\*As,1)

0.5 <= Value <= 1.5

7 = Corner rebar fraction top

0 < Value <= 1

8 = Corner rebar fraction bottom

0 < Value <= 1

9 = Relative humidity (%)

0 <= Value <= 100

10 = Moisture content

0 <= Value <= 1

11 = Gamma\_b

Value > 0

12 = Gamma\_bt

Value > 0

13 = Gamma\_b1 short term

Value > 0

14 = Gamma\_b1 long term

Value > 0

15 = Gamma\_b2

Value > 0

16 = Gamma\_b3 beams

Value > 0

17 = Gamma\_b3 columns

Value > 0

18 = Gamma\_b4

Value > 0

19 = 20 = Gamma\_S

Value > 0

20 = Gamma\_S1

Value > 0

21 = Pattern live load factor

Value >= 0

22 = Utilization factor limit

Value > 0

23 = Live load duration factor

Value >= 0

24 = Snow load duration factor

Value >= 0

25 = Reliability factor

Value >= 0

26 = Seismic factor mtr\_Flexure

Value >= 0

27 = Seismic factor mtr\_hear

Value > 0

28 = Site seismicity

      1 = Site seismicity 9

      2 = Site seismicity 8

      3 = Site seismicity 7

      4 = Non seismic

29 = Consider crack analysis?

0 = No

Any other value = Yes

30 = Crack width limit full load

Value >= 0

31 = Crack width limit long term

Value >= 0

32 = Longitudinal rebar size top

      1 = #2

      2 = #3

      3 = #4

      4 = #5

      5 = #6

      6 = #7

      7 = #8

      8 = #9

      9 = #10

      10 = #11

      11 = #14

      12 = #18

      13 = 10M

      14 = 15M

      15 = 20M

      16 = 25M

      17 = 30M

      18 = 35M

      19 = 45M

      20 = 55M

      21 = 6d

      22 = 8d

      23 = 10d

      24 = 12d

      25 = 14d

      26 = 16d

      27 = 20d

      28 = 25d

      29 = 26d

      30 = 28d

      31 = N12

      32 = N16

      33 = N20

      34 = N24

      35 = N28

      36 = N32

      37 = N36

33 = Longitudinal rebar size bottom

      1 = #2

      2 = #3

      3 = #4

      4 = #5

      5 = #6

      6 = #7

      7 = #8

      8 = #9

      9 = #10

      10 = #11

      11 = #14

      12 = #18

      13 = 10M

      14 = 15M

      15 = 20M

      16 = 25M

      17 = 30M

      18 = 35M

      19 = 45M

      20 = 55M

      21 = 6d

      22 = 8d

      23 = 10d

      24 = 12d

      25 = 14d

      26 = 16d

      27 = 20d

      28 = 25d

      29 = 26d

      30 = 28d

      31 = N12

      32 = N16

      33 = N20

      34 = N24

      35 = N28

      36 = N32

      37 = N36

34 = Is longitudinal rebar ribbed?

0 = No

Any other value = Yes

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemSP63\_13330\_2012()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True,"R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("SP63.13330.2012")

   'set preference item
      ret = SapModel.DesignConcrete.SP63\_13330\_2012.SetPreference(11, 1.2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v27.0.0.

## See Also

[GetPreference](GetPreference.htm)



## GetOverwrite {Concrete TS 500-2000}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/TS_500_2000/GetOverwrite_{Concrete_TS_500-2000}.htm`*

# GetOverwrite

SapObject.SapModel.DesignConcrete.TS\_500\_2000.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design
procedure.

Item

This is an integer between 1 and 14, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Live load reduction
factor

3 = Unbraced length ratio,
Major

4 = Unbraced length ratio,
Minor

5 = Effective length factor,
k Major

6 = Effective length factor,
k Minor

7 = Moment coefficient,
Cm Major

8 = Moment coefficient,
Cm Minor

9 = Non-sway moment factor,
Bns Major

10 = Non-sway moment factor,
Bns Minor

11 = Sway moment factor,
Bs Major

12 = Sway
moment factor, Bs Minor

13
= Consider torsion (beam only) (beam only)

14 = Concrete cover for
closed stirrups (beam only)

Value

The value of the considered preference item.

1 = Framing type

0 = Program Default

1 = High Ductile

2 = Nominal Ductile

3 = Ordinary

4 = Non-sway

2 = Live load reduction
factor

Value >= 0; 0 means
use program determined value

3 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value

4 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value

5 = Effective length factor,
k Major

Value >= 0; 0 means
use program determined value

6 =  Effective length
factor, k Minor

Value >= 0; 0 means
use program determined value

7 = Moment coefficient,
Cm Major

Value >= 0; 0 means
use program determined value

8 = Moment coefficient,
Cm Minor

Value >= 0; 0 means
use program determined value

9 = Non-sway moment factor,
Bns Major

Value >= 0; 0 means
use program determined value

10 = Non-sway moment factor,
Bns Minor

Value >= 0; 0 means
use program determined value

11 = Sway moment factor,
Bs Major

Value >= 0; 0 means
use program determined value

12 = Sway moment factor,
Bs Minor

Value >= 0; 0 means
use program determined value

13 = Consider torsion

0 = No

Any other value = Yes

14 = Concrete cover for
closed stirrups

Value >= 0; 0 means
use program determined value.

## ProgDet

If this Item is true, the specified value is program
determined.

## Remarks

This function sets the value of a concrete design overwrite
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemTS\_500\_2000()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim Value As Double

      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("TS
500-2000")

   'run analysis

      ret = SapModel.File.Save("C:\SapAPI\x.sdb")

      ret = SapModel.Analyze.RunAnalysis

   'start concrete design

      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.TS\_500\_2000.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 19.0.0.

Added items 13-14 in version 23.4.0

## See Also

[SetOverwrite](SetOverwrite_{TS_500_2000}.htm)



## GetPreference {Concrete TS 500 2000}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/TS_500_2000/GetPreference_{Concrete_TS_500-2000}.htm`*

# GetPreference

SapObject.SapModel.DesignConcrete.TS\_500\_2000.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Name

The name of an existing frame object or group, depending
on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating
the overwrite item considered.

1 = Number of interaction
curves

2 = Number of interaction
points

3 = Consider maximum eccentricity

4 = Seismic zone

5 = Gamma steel

6 = Gamma concrete

7 = Gamma concrete shear

8 = Pattern live load
factor

9 = Utilization factor
limit

10 = Multi-response case
design

11 = Consider torsion

12 = Design for B/C capacity
ratio

Value

The value of the considered preference item.

1 = Number of interaction
curves

Value >= 4 and divisible
by 4

2 = Number of interaction
points

Value >= 5 and odd

3 = Consider maximum eccentricity

0 = No

Any other value = Yes

4 = Seismic zone

1 = Zone 1

2 = Zone 2

3 = Zone 3

4 = Zone 4

5 = Gamma steel

Value > 0

6 = Gamma concrete

Value > 0

7 = Gamma concrete shear

Value > 0

8 = Pattern live load
factor

Value >= 0

9 = Utilization factor
limit

Value >= 0.

10 = Multi-response case
design

1 = Envelopes

2 = Step-by-Step

3 = Last Step

4 = Envelopes -- All

5 = Step-by-Step -- All

11 = Consider torsion

0 = No

Any other value = Yes

12 = Design for B/C capacity
ratio

0 = No

Any other value = Yes

## Remarks

This function sets the value of a concrete design preference
item.

The function returns zero if the item is successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemTS\_500\_2000()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("TS
500-2000")

   'get preference item
      ret = SapModel.DesignConcrete.TS\_500\_2000.GetPreference(2,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 19.0.0.

Added items 11-12 in version 23.4.0

## See Also

SetPreference



## SetOverwrite {ConcreteTS 500 2000}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/TS_500_2000/SetOverwrite_{TS_500_2000}.htm`*

# SetOverwrite

SapObject.SapModel.DesignConcrete.TS\_500\_2000.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByValItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending
on the value of the ItemType item.

Item

This is an integer between 1 and 14, inclusive, indicating
the overwrite item considered.

1 = Framing type (beam
and column)

2 = Live load reduction
factor (beam and column)

3 = Unbraced length ratio,
Major (beam and column)

4 = Unbraced length ratio,
Minor (beam and column)

5 = Effective length factor,
k Major (column only)

6 = Effective length factor,
k Minor (column only)

7 = Moment coefficient,
Cm Major (column only)

8 = Moment coefficient,
Cm Minor (column only)

9 = Non-sway moment factor,
Bns Major (column only)

10 = Non-sway moment factor,
Bns Minor (column only)

11 = Sway moment factor,
Bs Major (column only)

12 = Sway
moment factor, Bs Minor (column only)

13 = Consider torsion (beam
only) (beam only)

14 = Concrete cover for
closed stirrups (beam only)

Value

The value of the considered preference item.

1 = Framing type

0 = Program Default

1 = High Ductile

2 = Nominal Ductile

3 = Ordinary

4 = Non-sway

2 = Live load reduction
factor

Value >= 0; 0 means
use program determined value

3 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value

4 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value

5 = Effective length factor,
k Major

Value >= 0; 0 means
use program determined value

6 =  Effective length
factor, k Minor

Value >= 0; 0 means
use program determined value

7 = Moment coefficient,
Cm Major

Value >= 0; 0 means
use program determined value

8 = Moment coefficient,
Cm Minor

Value >= 0; 0 means
use program determined value

9 = Non-sway moment factor,
Bns Major

Value >= 0; 0 means
use program determined value

10 = Non-sway moment factor,
Bns Minor

Value >= 0; 0 means
use program determined value

11 = Sway moment factor,
Bs Major

Value >= 0; 0 means
use program determined value

12 = Sway moment factor,
Bs Minor

Value >= 0; 0 means
use program determined value

13
= Consider torsion

0 = No

Any other value = Yes

14 = Concrete cover for
closed stirrups

Value >= 0; 0 means
use program determined value.

## ItemType

This is one of the following items in the eItemType
enumeration:

Object
= 0

Group
= 1

Selected Objects = 2

If this item is Object, the assignment is made to the
frame object specified by the Name item.

If this item is Group, the assignment is made to all
frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made
to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemTS\_500\_2000()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("TS
500-2000")

   'set overwrite item
      ret = SapModel.DesignConcrete.TS\_500\_2000.SetOverwrite(2,
9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 19.0.0.

Added items 13-14 in version 23.4.0

## See Also

[GetOverwrite](GetOverwrite_{Concrete_TS_500-2000}.htm)



## SetPreference {Concrete TS 500 2000}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/TS_500_2000/SetPreference_{Concrete_TS_500_2000}.htm`*

# SetPreference

SapObject.SapModel.DesignConcrete.TS\_500\_2000.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Name

The name of an existing frame object or group, depending
on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating
the overwrite item considered.

1 = Number of interaction
curves

2 = Number of interaction
points

3 = Consider maximum eccentricity

4 = Seismic zone

5 = Gamma steel

6 = Gamma concrete

7 = Gamma concrete shear

8 = Pattern live load
factor

9 = Utilization factor
limit

10 = Multi-response case
design

11
= Consider torsion

12 = Design for B/C capacity
ratio

Value

The value of the considered preference item.

1 = Number of interaction
curves

Value >= 4 and divisible
by 4

2 = Number of interaction
points

Value >= 5 and odd

3 = Consider maximum eccentricity

0 = No

Any other value = Yes

4 = Seismic zone

1 = Zone 1

2 = Zone 2

3 = Zone 3

4 = Zone 4

5 = Gamma steel

Value > 0

6 = Gamma concrete

Value > 0

7 = Gamma concrete shear

Value > 0

8 = Pattern live load
factor

Value >= 0

9 = Utilization factor
limit

Value >= 0.

10 = Multi-response case
design

1 = Envelopes

2 = Step-by-Step

3 = Last Step

4 = Envelopes -- All

5 = Step-by-Step -- All

11
= Consider torsion

0 = No

Any other value = Yes

12 = Design for B/C capacity
ratio

0 = No

Any other value = Yes

## Remarks

This function sets the value of a concrete design preference
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemTS\_500\_2000()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1",
"4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("TS
500-2000")

   'set overwrite item
      ret = SapModel.DesignConcrete.TS\_500\_2000.SetPreference(2,
9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 19.0.0.

Added items 11-12 in version 23.4.0

## See Also

[GetPreference](GetPreference_{Concrete_TS_500-2000}.htm)



## GetOverwrite {Concrete UBC 97}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/UBC_97/GetOverwrite_{Concrete_UBC_97}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.UBC97.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway Intermediate

3 = Sway Ordinary

4 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemUBC97()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("UBC97")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.UBC97.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_UBC_97}.htm)



## GetPreference {Concrete UBC 97}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/UBC_97/GetPreference_{Concrete_UBC_97}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.UBC97.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi bending tension

5 = Phi compression controlled tied

6 = Phi compression controlled spiral

7 = Phi shear

8 = Pattern live load factor

9 = Utilization factor limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi bending tension

Value > 0

5 = Phi compression controlled tied

Value > 0

6 = Phi compression controlled spiral

Value > 0

7 = Phi shear

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Utilization factor limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemUBC97()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("UBC97")

   'get preference item
      ret = SapModel.DesignConcrete.UBC97.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_UBC_97}.htm)



## SetOverwrite {Concrete UBC 97}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/UBC_97/SetOverwrite_{Concrete_UBC_97}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.UBC97.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Dns Major

10 = Non-sway moment factor, Dns Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway special

2 = Sway Intermediate

3 = Sway Ordinary

4 = Non-sway

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Dns Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Dns Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemUBC97()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("UBC97")

   'set overwrite item
      ret = SapModel.DesignConcrete.UBC97.SetOverwrite("8", 1, 4)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_UBC_97}.htm)



## SetPreference {Concrete UBC 97}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/UBC_97/SetPreference_{Concrete_UBC_97}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.UBC97.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi bending tension

5 = Phi compression controlled tied

6 = Phi compression controlled spiral

7 = Phi shear

8 = Pattern live load factor

9 = Utilization factor limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi bending tension

Value > 0

5 = Phi compression controlled tied

Value > 0

6 = Phi compression controlled spiral

Value > 0

7 = Phi shear

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Utilization factor limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemUBC97()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("UBC97")

   'set preference item
      ret = SapModel.DesignConcrete.UBC97.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_UBC_97}.htm)



## VerifyPassed {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/VerifyPassed_{Concrete}.htm`*

# VerifyPassed

## Syntax

SapObject.SapModel.DesignConcrete.VerifyPassed

## VB6 Procedure

Function VerifyPassed(ByRef NumberItems As Long, ByRef n1 As Long, ByRef n2 As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of concrete frame objects that did not pass the design check or have not yet been checked.

n1

The number of concrete frame objects that did not pass the design check.

n2

The number of concrete frame objects that have not yet been checked.

MyName

This is an array that includes the name of each frame object that did not pass the design check or has not yet been checked.

## Remarks

This function retrieves the names of the frame objects that did not pass the design check or have not yet been checked, if any.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub VerifyConcreteDesignPassed()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyName2() As String
      Dim NumberItems As Long
      Dim n1 As Long
      Dim n2 As Long
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'verify frame objects successfully designed
      ret = SapModel.DesignConcrete.VerifyPassed(NumberItems, n1, n2, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## VerifySections {Concrete}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/VerifySections_{Concrete}.htm`*

# VerifySections

## Syntax

SapObject.SapModel.DesignConcrete.VerifySections

## VB6 Procedure

Function VerifySections(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of frame objects that have different analysis and design sections.

MyName

This is an array that includes the name of each frame object that has different analysis and design sections.

## Remarks

This function retrieves the names of the frame objects that have different analysis and design sections, if any.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub VerifyConcreteDesignSections()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyName2() As String
      Dim NumberItems As Long
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'verify analysis versus design section
      ret = SapModel.DesignConcrete.VerifySections(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## GetOverwrite {Concrete NZS 3101 95}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/nzs_3101_95/GetOverwrite_{Concrete_NZS_3101_95}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.NZS\_3101\_95.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a concrete frame design procedure.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Db Major

10 = Non-sway moment factor, Db Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ductile

2 = Limited

3 = Elastic

4 = Ordinary

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Db Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a concrete design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignOverwriteItemNZS\_3101\_95 ()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("NZS 3101-95")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.NZS\_3101\_95.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_NZS_3101_95}.htm)



## GetPreference {Concrete NZS 3101 95}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/nzs_3101_95/GetPreference_{Concrete_NZS_3101_95}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.NZS\_3101\_95.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi bending

5 = Phi tension

6 = Phi compression

7 = Phi shear

8 = Omega

9 = Phi 0

10 = Rm

11 = Rv

12 = Pattern live load factor

13 = Utilization factor limit

14 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi bending

Value > 0

5 = Phi tension

Value > 0

6 = Phi compression

Value > 0

7 = Phi shear

Value > 0

8 = Omega

Value > 0

9 = Phi 0

Value > 0

10 = Rm

Value > 0

11 = Rv

Value > 0

12 = Pattern live load factor

Value >= 0

13 = Utilization factor limit

Value > 0

14 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a concrete design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetConcreteDesignPreferenceItemNZS\_3101\_95()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("NZS 3101-95")

   'get preference item
      ret = SapModel.DesignConcrete.NZS\_3101\_95.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_NZS_3101_95}.htm)



## SetOverwrite {Concrete NZS 3101 95}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/nzs_3101_95/SetOverwrite_{Concrete_NZS_3101_95}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.NZS\_3101\_95.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 12, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Non-sway moment factor, Db Major

10 = Non-sway moment factor, Db Minor

11 = Sway moment factor, Ds Major

12 = Sway moment factor, Ds Minor

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ductile

2 = Limited

3 = Elastic

4 = Ordinary

2 = Live load reduction factor

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Non-sway moment factor, Db Major

Value >= 0; 0 means use program determined value.

10 = Non-sway moment factor, Db Minor

Value >= 0; 0 means use program determined value.

11 = Sway moment factor, Ds Major

Value >= 0; 0 means use program determined value.

12 = Sway moment factor, Ds Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a concrete design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignOverwriteItemNZS\_3101\_95()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("NZS 3101-95")

   'set overwrite item
      ret = SapModel.DesignConcrete.NZS\_3101\_95.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_NZS_3101_95}.htm)



## SetPreference {Concrete NZS 3101 95}

*Source file: `SAP2000_API_Fuctions/Design/Concrete/nzs_3101_95/SetPreference_{Concrete_NZS_3101_95}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.NZS\_3101\_95.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1 = Number of interaction curves

2 = Number of interaction points

3 = Consider minimum eccentricity

4 = Phi bending

5 = Phi tension

6 = Phi compression

7 = Phi shear

8 = Omega

9 = Phi 0

10 = Rm

11 = Rv

12 = Pattern live load factor

13 = Utilization factor limit

14 = Multi-response case design

Value

The value of the considered preference item.

1 = Number of interaction curves

Value >= 4 and devisable by 4

2 = Number of interaction points

Value >= 5 and odd

3 = Consider minimum eccentricity

0 = No

Any other value = Yes

4 = Phi bending

Value > 0

5 = Phi tension

Value > 0

6 = Phi compression

Value > 0

7 = Phi shear

Value > 0

8 = Omega

Value > 0

9 = Phi 0

Value > 0

10 = Rm

Value > 0

11 = Rv

Value > 0

12 = Pattern live load factor

Value >= 0

13 = Utilization factor limit

Value > 0

14 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a concrete design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetConcreteDesignPreferenceItemNZS\_3101\_95()
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

   'create new concrete frame section property
      ret = SapModel.PropFrame.SetRectangle("R1", "4000Psi", 20, 12)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "R1", "R1")

   'set concrete design code
      ret = SapModel.DesignConcrete.SetCode("NZS 3101-95")

   'set preference item
      ret = SapModel.DesignConcrete.NZS\_3101\_95.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_NZS_3101_95}.htm)

