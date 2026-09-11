# API Bridge Advanced

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Bridge_Advanced

---



## CountSuperCutWebStressPoint

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/Concrete_Box_Girder/CountSuperCutWebStressPoint.htm`*

# CountSuperCutWebStressPoint

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.BASConcBox.CountSuperCutWebStressPoint

## VB6 Procedure

Function CountSuperCutWebStressPoint(ByVal Name As String, ByVal CutIndex As Long, ByVal WebIndex As Long, ByRef Count As Long) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by function CountSuperCut.

WebIndex

The index number of the web in this section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by function GetSuperCutSectionValues.

Count

The number of stress points in this web for this section cut in this bridge object. They will be identified in subsequent API functions using the indices 0 to Count-1.

## Remarks

This function returns the number of stress points at the specified web of the specified superstructure section cut.

The function returns zero if the count is successfully retrieved; otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutStressPointCount()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim CountWeb As Long
      Dim CountPoint As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get section cut count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCut("BOBJ1", Count)

   'get web count at first section cut (0)
      ret = SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSectionValues ("BOBJ1", 0, 1, CountWeb)

   'get stress point count at first web (0)
      ret = SapModel.BridgeAdvancedSuper.CountSuperCutWebStressPoint("BOBJ1", 0, 0, CountPoint)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[CountSuperCut](../CountSuperCut.htm)

[GetSuperCutSectionValues](GetSuperCutSectionValues.htm)



## GetSuperCutSectionPropsAtY

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/Concrete_Box_Girder/GetSuperCutSectionPropsAtY.htm`*

# GetSuperCutSectionPropsAtY

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSectionPropsAtY

## VB6 Procedure

Function GetSuperCutSectionPropsAtY (ByVal Name As String, ByVal CutIndex As Long, ByVal Y as Double, ByVal AboveY as Boolean, ByRef Ycg as Double, ByRef Area as Double, ByRef Inertia as Double) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of the section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by the function CountSuperCut. Section cuts will be in order of increasing Station and increasing SuperCutType.

Y

The Y coordinate in the section local coordinate system above or below which the section properties are calculated.

AboveY

Boolean indicating whether properties are to be computed for the region above (if true) or below (if false) the specified coordinate Y.

Ycg

Y coordinate of the centroid of the region above/below specified coordinate Y. [L]

Area

Area of the region above/below specified coordinate Y. [L2]

Inertia

Moment of inertia of the region above/below specified coordinate Y, taken about a horizontal axis at Ycg. [L4]

## Remarks

This function returns section properties for the region above or below a given Y coordinate value at a single superstructure section cut in a bridge object. These properties are calculated for the section before skew, grade, and superelevation are applied. Coordinate values are measured from the lower-left corner of the section bounding-box. X is positive to the right when looking upstation, and Y is positive upward.

The function returns zero if the information is successfully retrieved; otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutSectionValues()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim Y As Double
      Dim Ycg As Double
      Dim Area As Double
      Dim Inertia As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get section cut count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCut("BOBJ1", Count)

   'get section properties for region above Y = 10 at first cut (0)
      ret = SapModel.BridgeAdvancedSuper.BASConcBox. GetSuperCutSectionPropsAtY ("BOBJ1", 0, Y, True, Ycg, Area, Inertia)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.0.0.

## See Also

[CountSuperCut](../CountSuperCut.htm)



## GetSuperCutSectionValues

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/Concrete_Box_Girder/GetSuperCutSectionValues.htm`*

# GetSuperCutSectionValues

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSectionValues

## VB6 Procedure

Function GetSuperCutSectionValues (ByVal Name As String, ByVal CutIndex As Long, ByVal Item as Long, ByRef Value as Double) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of the section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by the function CountSuperCut. Section cuts will be in order of increasing Station and increasing SuperCutType.

Item

This is an integer from 1 to 12, inclusive, indicating the type of property value to be gotten:

1 = Number of girders or webs

2 = Design area of top slab, ASlabTop

3 = Design area of bottom slab, ASlabBot

4 = Width of top slab, BSlabTop

5 = Width of bottom slab, BSlabBot

6 = X coordinate of top slab centroid, XSlabTop

7 = X coordinate of bottom slab centroid, XSlabBot

8 = Y coordinate of top slab centroid, YSlabTop

9 = Y coordinate of bottom slab centroid, YSlabBot

10 = Area inside torsion circuit, ATorsion

11 = Length of torsion circuit, LTorsion

12 = Number of tendons

13 = Top outside width of torsion circuit, BTorsionTop

14 = Bottom outside width of torsion circuit, BTorsionBot

15 = Left outside length of torsion circuit (along slope), HTorsionLeft

16 = Right outside length of torsion circuit (along slope), HTorsionRight

Value

The value of the requested item:

1 = Number of girders or webs

Value >= 0, integral.

2 = Design area of top slab, ASlabTop

Value > 0. [L2]

3 = Design area of bottom slab, ASlabBot

Value >= 0. [L2]

4 = Width of top slab, BSlabTop

Value > 0. [L]

5 = Width of bottom slab, BSlabBot

Value >= 0. [L]

6 = X coordinate of top slab centroid, XSlabTop

Any value is valid. [L]

7 = X coordinate of bottom slab centroid, XSlabBot

Any value is valid. [L]

8 = Y coordinate of top slab centroid, YSlabTop

Value >= 0. [L]

9 = Y coordinate of bottom slab centroid, YSlabBot

Value <= 0. [L]

10 = Area inside torsion circuit, ATorsion

Value >= 0. [L2]

11 = Length of torsion circuit, LTorsion

Value >= 0. [L]

12 = Number of tendons

Value >= 0.

13 = Top outside width of torsion circuit, BTorsionTop

Value > 0. [L]

14 = Bottom outside width of torsion circuit, BTorsionBot

Value > 0. [L]

15 = Left outside length of torsion circuit (along slope), HTorsionLeft

Value > 0. [L]

16 = Right outside length of torsion circuit (along slope), HTorsionRight

Value > 0. [L]

## Remarks

This function returns an individual section property at a single superstructure section cut in a bridge object. These properties are calculated for the section before skew, grade, and superelevation are applied. Coordinate values are measured from the lower-left corner of the section bounding-box. X is positive to the right when looking upstation, and Y is positive upward.

The function returns zero if the information is successfully retrieved; otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutSectionValues()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get section cut count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCut("BOBJ1", Count)

   'get section cut section top-slab area in Value
      ret = SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSectionValues ("BOBJ1", 1, 2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[CountSuperCut](../CountSuperCut.htm)



## GetSuperCutSlabCoordsAtX

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/Concrete_Box_Girder/GetSuperCutSlabCoordsAtX.htm`*

# GetSuperCutSlabCoordsAtX

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSlabCoordsAtX

## VB6 Procedure

Function GetSuperCutSlabCoordsAtX(ByVal Name As String, ByVal CutIndex As Long, ByVal X As Double, ByRef Status As Long, ByRef y1 As Double, ByRef y2 As Double, ByRef y3 As Double, ByRef y4 As Double) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of the section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by function CountSuperCut. Section cuts will be in order of increasing Station and increasing SuperCutType.

X

The X coordinate in the section local coordinate system at which a vertical line is passed through the section and the slab coordinates are returned.

Status

This is 0, 1, or 2.

0 = No portion of the section is cut.

1 = Only the section is cut; no interior cell is cut.

2 = The section and an interior cell are cut.

y1

The topmost Y coordinate where the vertical line cuts the section.  This item is returned as zero when Status < 1.

y2

The bottommost Y coordinate where the vertical line cuts the section.  This item is returned as zero when Status < 1.

y3

The topmost Y coordinate where the vertical line cuts an interior cell.  This item is returned as zero when Status < 2.

y4

The bottommost Y coordinate where the vertical line cuts an interior cell.  This item is returned as zero when Status < 2.

## Remarks

This function returns information about the box girder slab thicknesses at a given horizontal location across the box girder section.

The function returns zero if the information is successfully retrieved; otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutSlabCoordsAtX()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Status As Long
      Dim y1 As Double
      Dim y2 As Double
      Dim y3 As Double
      Dim y4 As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get slab thickness information at X = 60
      ret = SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSlabCoordsAtX("BOBJ1", 1, 60, Status, y1, y2, y3, y4)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## GetSuperCutTendonNames

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/Concrete_Box_Girder/GetSuperCutTendonNames.htm`*

# GetSuperCutTendonNames

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutTendonNames

## VB6 Procedure

Function GetSuperCutTendonNames(ByVal Name As String, ByVal CutIndex As Long, ByVal TendonIndex As Long, ByRef BridgeTendon As String, ByRef TendonObj as String) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of the section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by the function CountSuperCut. Section cuts will be in order of increasing Station and increasing SuperCutType.

TendonIndex

The index number of a tendon in this section cut of this bridge object. This must be from 0 to CountTendon-1, where CountTendon is the number of tendons returned by function GetSuperCutSectionValues using Item = 12.

BridgeTendon

The name of the tendon inside of the bridge object corresponding to TendonIndex.

TendonObj

The name of the tendon object created by the program from the bridge object tendon corresponding to TendonIndex.

## Remarks

This function returns the name of a single tendon object, giving access to tendon assignments, tendon section, and material property.

The function returns zero if the information is successfully retrieved; otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutTendonNames()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim CountTendon As Long
      Dim BridgeTendon As String
      Dim TendonObj As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get section cut count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCut("BOBJ1", Count)

   'get tendon count at section cut 1
      ret = SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSectionValues ("BOBJ1", 12, 1, CountTendon)

   'get tendon object name for first tendon (0)
      ret = SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutTendonNames("BOBJ1", 1, 0, BridgeTendon, TendonObj)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[CountSuperCut](../CountSuperCut.htm)

[GetSuperCutSectionValues](GetSuperCutSectionValues.htm)

[GetSuperCutTendonValues](GetSuperCutTendonValues.htm)



## GetSuperCutTendonValues

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/Concrete_Box_Girder/GetSuperCutTendonValues.htm`*

# GetSuperCutTendonValues

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutTendonValues

## VB6 Procedure

Function GetSuperCutTendonValues(ByVal Name As String, ByVal CutIndex As Long, ByVal TendonIndex As Long, ByVal Item as Long, ByRef Value as Double) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of the section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by the function CountSuperCut. Section cuts will be in order of increasing Station and increasing SuperCutType.

TendonIndex

The index number of a tendon in this section cut of this bridge object. This must be from 0 to CountTendon-1, where CountTendon is the number of tendons returned by the function GetSuperCutSectionValues using Item = 12.

Item

This is an integer from 1 to 4, inclusive, indicating the type of property value to be gotten:

1 = X coordinate of tendon centroid, Xcg

2 = Y coordinate of tendon centroid, Ycg

3 = Duct diameter for tendon

4 = Bonding type for tendon

5 = Tendon slope

Value

The value of the requested item:

1 = X coordinate of tendon centroid, Xcg

Any value OK. [L]

2 = Y coordinate of tendon centroid, Ycg

Any value OK. [L]

3 = Duct diameter for tendon

Value >= 0. [L]

4 = Bonding type for tendon

1 = Bonded

2 = Unbonded

5 = Tendon slope

Any value OK. [L/L]

## Remarks

This function returns an individual section property for a single tendon at a single superstructure section cut in a bridge object. These properties are calculated for the section before skew, grade, and superelevation are applied. Coordinate values are measured from the lower-left corner of the section bounding-box. X is positive to the right when looking upstation, and Y is positive upward.

The function returns zero if the information is successfully retrieved; otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutTendonValues()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim CountTendon As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get section cut count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCut("BOBJ1", Count)

   'get tendon count at section cut 1
      ret = SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSectionValues ("BOBJ1", 12, 1, CountTendon)

   'get Y coordinate of centroid for first tendon (0)
      ret = SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutTendonValues("BOBJ1", 1, 0, 2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[CountSuperCut](../CountSuperCut.htm)

[GetSuperCutSectionValues](GetSuperCutSectionValues.htm)

[GetSuperCutTendonNames](GetSuperCutTendonNames.htm)



## GetSuperCutWebCoordsAtY

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/Concrete_Box_Girder/GetSuperCutWebCoordsAtY.htm`*

# GetSuperCutWebCoordsAtY

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutWebCoordsAtY

## VB6 Procedure

Function GetSuperCutWebCoordsAtY(ByVal Name As String, ByVal CutIndex As Long, ByVal Y As Double, ByRef NumberWebs As Long, ByRef WebIsCut() As Boolean, ByRef WebLeft() As Double, ByRef WebRight() As Double) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of the section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by the function CountSuperCut. Section cuts will be in order of increasing Station and increasing SuperCutType.

Y

The Y coordinate in the section local coordinate system at which the web coordinates are returned.

NumberWebs

The number of webs in the section.

WebIsCut

This is a array of booleans indicating if each web is cut by a horizontal line at the specified Y coordinate.

WebLeft

This is a array of X coordinates of the left side of each web. If the web is not cut by a horizontal line at the specified Y coordinate, this value is returned as zero.

WebRight

This is a array of X coordinates of the right side of each web. If the web is not cut by a horizontal line at the specified Y coordinate, this value is returned as zero.

## Remarks

This function returns information about the box girder web thicknesses at a given elevation in the box girder section.

The function returns zero if the information is successfully retrieved; otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutWebCoordsAtY()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberWebs As Long
      Dim WebIsCut() As Boolean
      Dim WebLeft() As Double
      Dim WebRight() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get web information
      ret = SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutWebCoordsAtY("BOBJ1", 1, 44, NumberWebs, WebIsCut, WebLeft, WebRight)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## GetSuperCutWebStressPoint

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/Concrete_Box_Girder/GetSuperCutWebStressPoint.htm`*

# GetSuperCutWebStressPoint

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutWebStressPoint

## VB6 Procedure

Function GetSuperCutWebStressPoint(ByVal Name As String, ByVal CutIndex As Long, ByVal WebIndex As Long, ByVal PointIndex As Long, ByRef X As Double, ByRef Y As Double, ByRef MatProp As String, ByRef Note as String) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by function CountSuperCut.

WebIndex

The index number of the web in this section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by function GetSuperCutSectionValues.

PointIndex

The index number of the stress point in this web of this section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by function CountSuperCutWebStressPoint.

X, Y

The transverse and vertical coordinates of the stress point in the section, measured from the bottom left corner of the section.  X is positive to the right when looking upstation. Y is positive upward. [L]

MatProp

The name of the material property at this stress point.

Note

A description of the stress point that may be used for identification. Points that are pre-defined by the program will have prescribed notes.

## Remarks

This function returns location and material information about a single stress point in a web at a superstructure section cut in a bridge object. The function returns zero if the information is successfully retrieved; otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutStressPointInfo()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim CountWeb As Long
      Dim CountPoint As Long
      Dim X As Double,
      Dim Y As Double
      Dim MatProp As String
      Dim Note As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get section cut count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCut("BOBJ1", Count)

   'get web count at first section cut (0)
      ret = SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSectionValues ("BOBJ1", 0, 1, CountWeb)

   'get stress point count at first web (0)
      ret = SapModel.BridgeAdvancedSuper.CountSuperCutWebStressPoint("BOBJ1", 0, 0, CountPoint)

   'get web stress point location information
      ret = SapModel.BridgeAdvancedSuper.GetSuperCutWebStressPoint("BOBJ1", 0, 0, 0, X, Y, MatProp, Note)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.0.0.

## See Also

[CountSuperCut](../CountSuperCut.htm)

[GetSuperCutSectionValues](GetSuperCutSectionValues.htm)

[CountSuperCutWebStressPoint](CountSuperCutWebStressPoint.htm)



## GetSuperCutWebValues

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/Concrete_Box_Girder/GetSuperCutWebValues.htm`*

# GetSuperCutWebValues

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutWebValues

## VB6 Procedure

Function GetSuperCutWebValues(ByVal Name As String, ByVal CutIndex As Long, ByVal WebIndex As Long, ByVal Item as Long, ByRef Value as Double) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of the section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by the function CountSuperCut. Section cuts will be in order of increasing Station and increasing SuperCutType.

WebIndex

The index number of a web in this section cut of this bridge object. This must be from 0 to CountWeb-1, where CountWeb is the number of webs returned by thenfunction GetSuperCutSectionValues using Item = 1. Webs count from left to right when looking upstation.

Item

This is an integer from 1 to 6, inclusive, indicating the type of property value to be gotten:

1 = Angle from vertical (Y) axis, clockwise is positive

2 = Minimum horizontal (X) web thickness

3 = Minimum top slab thickness above cell to left of web

4 = Minimum bottom slab thickness above cell to left of web

5 = Top width of cell to left of web measured from centerline of girders on each side of cell

6 = Bottom width of cell to left of web measured from centerline of girders on each side of cell.

Value

The value of the requested item:

1 = Angle from vertical (Y) axis, clockwise is positive

Abs(Value) < 90. [deg]

2 = Minimum horizontal (X) web thickness

Value > 0. [L]

3 = Minimum top slab thickness

Value < 0. [L]

4 = Minimum bottom slab thickness

Value > 0. [L]

5 = Top width of cell

Value >= 0. [L]

6 = Bottom width of cell

Value >= 0. [L]

## Remarks

This function returns an individual section property for a single web at a single superstructure section cut in a bridge object. These properties are calculated for the section before skew, grade, and superelevation are applied. Coordinate values are measured from the lower-left corner of the section bounding-box. X is positive to the right when looking upstation, and Y is positive upward

The function returns zero if the information is successfully retrieved; otherwise it returns a nonzero value. An error is returned for items 3, 4, 5 and 6 if the WebIndex is specified as 0.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutWebValues()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim CountWeb As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get section cut count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCut("BOBJ1", Count)

   'get web count at section cut 1
      ret = SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutSectionValues ("BOBJ1", 1, 1, CountWeb)

   'get minimum thickness for first web (0)
      ret = SapModel.BridgeAdvancedSuper.BASConcBox.GetSuperCutWebValues("BOBJ1", 1, 0, 2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[CountSuperCut](../CountSuperCut.htm)

[GetSuperCutSectionValues](GetSuperCutSectionValues.htm)



## CountSuperCut

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/CountSuperCut.htm`*

# CountSuperCut

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.CountSuperCut

## VB6 Procedure

Function CountSuperCut(ByVal Name As String, ByRef Count As Long) As Long

## Parameters

Name

The name of an existing bridge object.

Count

The number of section cuts in this bridge object. They will be identified in subsequent API functions using the indices 0 to Count-1. There may be one or two section cuts at each output station along the length of the superstructure.

## Remarks

This function returns the number of superstructure section cuts that are available for getting analysis results and performing design.

The function returns zero if the count is successfully retrieved, otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutCount()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim FileName As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get section cut count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCut("BOBJ1", Count)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## CountSuperCutStressPoint

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/CountSuperCutStressPoint.htm`*

# CountSuperCutStressPoint

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.CountSuperCutStressPoint

## VB6 Procedure

Function CountSuperCutStressPoint(ByVal Name As String, ByVal CutIndex As Long, ByRef Count As Long) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by function CountSuperCut.

Count

The number of stress points for this section cut in this bridge object. They will be identified in subsequent API functions using the indices 0 to Count-1.

## Remarks

This function returns the number of stress points at the specified superstructure section cut.

The function returns zero if the count is successfully retrieved, otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutStressPointCount()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim CountPoint As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get section cut count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCut("BOBJ1", Count)

   'get section cut stress point count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCutStressPoint("BOBJ1", 1, CountPoint)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[CountSuperCut](CountSuperCut.htm)



## GetSuperCutLocation

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/GetSuperCutLocation.htm`*

# GetSuperCutLocation

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.GetSuperCutLocation

## VB6 Procedure

Function GetSuperCutLocation(ByVal Name As String, ByVal CutIndex As Long, ByRef Location As Long, ByRef Station As Double, ByRef XRefPt As Double, ByRef YRefPt As Double, ByRef Skew As Double, ByRef Grade As Double, ByRef SuperElev As Double) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by function CountSuperCut. Section cuts will be in order of increasing Station and increasing SuperCutType.

Location

This is 1 or 2, indicating whether the CutIndex section cut occurs before or after the associated station.

1 = Before the specified station.

2 = After the specified station.

Station

The station ordinate of the CutIndex section cut at the reference line of the superstructure. [L]

XRefPt, YRefPt

The transverse and vertical coordinates in the section of the reference point that corresponds to the layout line in the bridge object. XRefPt is positive to the right when looking upstation. YRefPt is positive upward. Coordinates are measured from the lower-left corner of the section bounding-box before skew, grade, and superelevation are applied. The rotations of the section due to skew, grade, and superelevation occur about the reference point. [L]

Skew

The skew angle, in degrees, of the section cut, measured from the horizontal normal to the superstructure reference line, with positive being about the upward vertical axis.

Grade

The grade, as a slope (abs(Grade) < 1.0), giving the vertical rise per distance along the superstructure reference line.

SuperElev

The superelevation, as a slope (abs(SuperElev) < 1.0), giving the vertical rise per distance along the transverse normal to the superstructure reference line.

## Remarks

This function returns location and orientation information about a single superstructure section cut in a bridge object.

The function returns zero if the information is successfully retrieved, otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutCount()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim Location As Long
      Dim Station As Double
      Dim XRefPt As Double,
      Dim YRefPt As Double
      Dim Skew As Double
      Dim Grade As Double
      Dim SuperElev As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get section cut count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCut("BOBJ1", Count)

   'get section cut location information
      ret = SapModel.BridgeAdvancedSuper.GetSuperCutLocation("BOBJ1", 1, Location, Station, RefPt, YRefPt Skew, Grade, SuperElev)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[CountSuperCut](CountSuperCut.htm)



## GetSuperCutStressPoint

*Source file: `SAP2000_API_Fuctions/Bridge_Advanced/Superstructure/GetSuperCutStressPoint.htm`*

# GetSuperCutStressPoint

## Syntax

SapObject.SapModel.BridgeAdvancedSuper.GetSuperCutStressPoint

## VB6 Procedure

Function GetSuperCutStressPoint(ByVal Name As String, ByVal CutIndex As Long, ByVal PointIndex As Long, ByRef X As Double, ByRef Y As Double, ByRef MatProp As String, ByRef Note as String) As Long

## Parameters

Name

The name of an existing bridge object.

CutIndex

The index number of section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by function CountSuperCut.

PointIndex

The index number of the stress point in this section cut in this bridge object. This must be from 0 to Count-1, where Count is the value returned by function CountSuperCutStressPoint.

X, Y

The transverse and vertical coordinates of the stress point in the section, measured from the bottom left corner of the section.  X is positive to the right when looking upstation. Y is positive upward. [L]

MatProp

The name of the material property at this stress point.

Note

A description of the stress point that may be used for identification. Points that are pre-defined by the program will have prescribed notes.

## Remarks

This function returns location and material information about a single stress point at a superstructure section cut in a bridge object.

The function returns zero if the information is successfully retrieved, otherwise it returns a nonzero value.

If the bridge object is not currently linked to existing objects in the model, an error is returned.

## VBA Example

This example assumes that a file MyBridge.sdb exists and has a linked bridge object named BOBJ1 in it.

Sub GetBridgeSuperCutStressPointInfo()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim CountPoint As Long
      Dim X As Double,
      Dim Y As Double
      Dim MatProp As String
      Dim Note As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyBridge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get section cut count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCut("BOBJ1", Count)

   'get section cut stress point count
      ret = SapModel.BridgeAdvancedSuper.CountSuperCutStressPoint("BOBJ1", 1, CountPoint)

   'get section cut stress point location information
      ret = SapModel.BridgeAdvancedSuper.GetSuperCutStressPoint("BOBJ1", 1, 1, X, Y, MatProp, Note)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[CountSuperCut](CountSuperCut.htm)

[CountSuperCutStressPoint](GetSuperCutStressPoint.htm)

