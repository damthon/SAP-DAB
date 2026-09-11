# API Definitions General Reference Line

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Definitions/General_Reference_Line

---



## ConvertLineToBLL

*Source file: `SAP2000_API_Fuctions/Definitions/General_Reference_Line/ConvertLineToBLL.htm`*

# ConvertLineToBLL

## Syntax

SapObject.SapModel.GenRefLine.ConvertLineToBLL

## VB6 Procedure

Function ConvertLineToBLL(ByVal Name As String, Optional ByVal FirstStation As Double = 0, Optional ByVal CSys As String = "Global", Optional ByVal OffsetX As Double = 0, Optional ByVal OffsetY As Double = 0, Optional ByVal OffsetZ As Double) As Long

## Parameters

Name

This is the name of an existing general reference line.

FirstStation

The first station value on the bridge layout line. [L]

CSys

The name of the coordinate system in which the general reference line is offset to create the bridge layout line.

OffsetX

The distance to offset the general reference line in the x-direction of the specified CSys, to the location of the new bridge layout line.

OffsetY
The distance to offset the general reference line in the y-direction of the specified CSys, to the location of the new bridge layout line.

OffsetZ
The distance to offset the general reference line in the z-direction of the specified CSys, to the location of the new bridge layout line.

## Remarks

This function converts an existing general reference line to a new bridge layout line, with the ability to specify offset values.

The function returns zero if the bridge layout line is successfully created; otherwise it returns a nonzero value.

## VBA Example

Sub ConvertGenRefLine()
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

   'define new general reference line
      ret = SapModel.GenRefLine.SetLine("GRef1", 120, 5)

   'convert general reference line to bridge layout line
      ret = SapModel.GenRefLine.ConvertLineToBLL("GRef1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.0.

## See Also

[SetLine](SetLine_{Gen_Ref_Line}.htm)



## Count {Gen Ref Line}

*Source file: `SAP2000_API_Fuctions/Definitions/General_Reference_Line/Count_{Gen_Ref_Line}.htm`*

# Count

## Syntax

SapObject.SapModel.GenRefLine.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None.

## Remarks

The function returns the number of defined general reference lines.

## VBA Example

Sub CountGenRefLine()
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

   'define new general reference line
      ret = SapModel.GenRefLine.SetLine("GRef1", 120, 5)

   'get number of general reference line
      ret = SapModel.GenRefLine.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.0.

## See Also

[SetLine](SetLine_{Gen_Ref_Line}.htm)



## Delete {Gen Ref Line}

*Source file: `SAP2000_API_Fuctions/Definitions/General_Reference_Line/Delete_{Gen_Ref_Line}.htm`*

# Delete

## Syntax

SapObject.SapModel.GenRefLine.Delete

## VB6 Procedure

Function Delete(ByVal Name As String) As Long

## Parameters

Name

The name of an existing general reference line.

## Remarks

The function deletes the specified general reference line.

The function returns zero if the general reference line is successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteGenRefLine()
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

   'define new general reference line
      ret = SapModel.GenRefLine.SetLine("GRef1", 120, 5)

   'delete general reference line
      ret = SapModel.GenRefLine.Delete("GRef1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.0.

## See Also

[SetLine](SetLine_{Gen_Ref_Line}.htm)

[SetLinePlanPoints](SetLinePlanPoints.htm)

[SetLineElevPoints](SetLineElevPoints.htm)



## GetLineElevPoints

*Source file: `SAP2000_API_Fuctions/Definitions/General_Reference_Line/GetLineElevPoints.htm`*

# GetLineElevPoints

## Syntax

SapObject.SapModel.GenRefLine.GetLineElevPoints

## VB6 Procedure

Function GetLineElevPoints(ByVal Name As String, ByRef NumberPoints As Long, ByRef CurveType() As Long, ByRef Value1() As Double, ByRef Value2() As Double, ByRef Value3() As Double, ByRef s() As Double, ByRef z() As Double, Optional ByVal CSys As String = "Global") As Long

## Parameters

Name

The name of an existing general reference line.

NumberPoints

The number of points used to define the general reference line elevation layout.

CurveType

This is an array of values indicating the general reference line elevation layout curve type for each point.

0 = None
1 = Circular Curve
2 = Highway Curve
3 = Parabolic Curve
4 = Bezier Curve
5 = BSpline Curve
6 = Bezier Curve Child Point
7 = BSpline Curve Child Point

Value1

This is the value of a parameter used to define the general reference line layout. The item that Value1 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Curve Radius [L]
CurveType = 2: Curve Radius [L]
CurveType = 3: Angle measured from the horizontal, up station axis, to the axis of symmetry of the parabolic curve. [deg]
CurveType = 4: Number of control points. This is currently hard-wired internally to 4.
CurveType = 5: Number of control points.
CurveType = 6: Not Used
CurveType = 7: Not Used

Value2
This is the value of a parameter used to define the general reference line layout. The item that Value2 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Not Used
CurveType = 2: Curve length, including length of spirals on either end. [L]
CurveType = 3: Rate at which the slope of a parabolic curve is changing in percent. [1/L]
CurveType = 4: Number of discretization points.
CurveType = 5: Number of discretization points.
CurveType = 6: Not Used
CurveType = 7: Not Used

Value3

This is the value of a parameter used to define the general reference line layout. The item that Value3 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Not Used
CurveType = 2: Not Used
CurveType = 3: Not Used
CurveType = 4: Not Used
CurveType = 5: Curve order.
CurveType = 6: Not Used
CurveType = 7: Not Used

s

This is an array of the station coordinate of each point in the coordinate system specified for the general reference line. [L]

z

This is an array of the Z coordinate of each point in the coordinate system specified for the general reference line. [L]

## Remarks

This function retrieves the general reference line elevation points and the associated parameters.

The function returns zero if the general reference line parameters are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetElevPoints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberPoints As Long
      Dim CurveType() As Long
      Dim Value1() As Double
      Dim Value2() As Double
      Dim Value3() As Double
      Dim s() As Double
      Dim z() As Double

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

   'add new general reference line
      Name = "GRef1"
      ret = SapModel.GenRefLine.SetLine(Name, 120, 5)

   'set general reference line elev points data
      NumberPoints = 3
      ReDim CurveType(NumberPoints – 1)
      ReDim x(NumberPoints – 1)
      Redim y(NumberPoints – 1)
      CurveType(0) = 0
      CurveType(1) = 1
      CurveType(2) = 0
      s(0) = 0: z(0) = 0
      s(1) = 100: z(1) = 100
      s(2) = 200: z(2) = 100
      Value1(0) = 0: Value1(1) = 100: Value1(2) = 0
      Value2(0) = 0: Value2(1) = 0: Value2(2) = 0
      Value3(0) = 0: Value3(1) = 0: Value3(2) = 0
      ret = SapModel.GenRefLine.SetLineElevPoints(Name, NumberPoints, CurveType, Value1, Value2, Value3, s, z)

   'get general reference line plan points data
      ReDim CurveType(0)
      ReDim Value1(0)
      ReDim Value2(0)
      ReDim Value3(0)
      ReDim s(0)
      ReDim z(0)
      Ret = SapModel.GenRefLine.GetLinePlanPoints(Name, NumberPoints, Value1, Value2, Value3, s, z)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.0.

## See Also

[SetLineElevPoints](SetLineElevPoints.htm) [GetLine](GetLine_{Gen_Ref_Line}.htm) [GetLinePlanPoints](GetLinePlanPoints.htm)



## GetLinePlanPoints

*Source file: `SAP2000_API_Fuctions/Definitions/General_Reference_Line/GetLinePlanPoints.htm`*

# GetLinePlanPoints

## Syntax

SapObject.SapModel.GenRefLine.GetLinePlanPoints

## VB6 Procedure

Function GetLinePlanPoints(ByVal Name As String, ByRef NumberPoints As Long, ByRef CurveType() As Long, ByRef Value1() As Double, ByRef Value2() As Double, ByRef Value3() As Double, ByRef x() As Double, ByRef y() As Double, Optional ByVal CSys As String = "Global") As Long

## Parameters

Name

The name of an existing general reference line.

NumberPoints

The number of points used to define the general reference line plan layout.

CurveType

This is an array of values indicating the general reference line plan layout curve type for each point.

0 = None
1 = Circular Curve
2 = Highway Curve
3 = Parabolic Curve
4 = Bezier Curve
5 = BSpline Curve
6 = Bezier Curve Child Point
7 = BSpline Curve Child Point

Value1

This is the value of a parameter used to define the general reference line layout. The item that Value1 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Curve Radius [L]
CurveType = 2: Curve Radius [L]
CurveType = 3: Angle measured from the X-axis of the coordinate system in which the general reference line is defined, to the axis of symmetry of the parabolic curve. [deg]
CurveType = 4: Number of control points. This is currently hard-wired internally to 4.
CurveType = 5: Number of control points.
CurveType = 6: Not Used
CurveType = 7: Not Used

Value2

This is the value of a parameter used to define the general reference line layout. The item that Value2 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Not Used
CurveType = 2: Curve length, including length of spirals on either end. [L]
CurveType = 3: Rate at which the slope of a parabolic curve is changing in percent. [1/L]
CurveType = 4: Number of discretization points.
CurveType = 5: Number of discretization points.
CurveType = 6: Not Used
CurveType = 7: Not Used

Value3

This is the value of a parameter used to define the general reference line layout. The item that Value3 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Not Used
CurveType = 2: Not Used
CurveType = 3: Not Used
CurveType = 4: Not Used
CurveType = 5: Curve order.
CurveType = 6: Not Used
CurveType = 7: Not Used

x

This is an array of the X coordinate of each point in the coordinate system specified for the general reference line. [L]

y

This is an array of the Y coordinate of each point in the coordinate system specified for the general reference line. [L]

## Remarks

This function retrieves the general reference line plan points and the associated parameters.

The function returns zero if the general reference line parameters are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetPlanPoints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberPoints As Long
      Dim CurveType() As Long
      Dim Value1() As Double
      Dim Value2() As Double
      Dim Value3() As Double
      Dim x() As Double
      Dim y() As Double

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

   'add new general reference line
      Name = "GRef1"
      ret = SapModel.GenRefLine.SetLine(Name, 120, 5)

   'set general reference line plan points data
      NumberPoints = 3
      ReDim CurveType(NumberPoints – 1)
      ReDim x(NumberPoints – 1)
      Redim y(NumberPoints – 1)
      CurveType(0) = 0
      CurveType(1) = 1
      CurveType(2) = 0
      x(0) = 0: y(0) = 0
      x(1) = 100: y(1) = 100
      x(2) = 200: y(2) = 100
      Value1(0) = 0: Value1(1) = 100: Value1(2) = 0
      Value2(0) = 0: Value2(1) = 0: Value2(2) = 0
      Value3(0) = 0: Value3(1) = 0: Value3(2) = 0
      ret = SapModel.GenRefLine.SetLinePlanPoints(Name, NumberPoints, CurveType, Value1, Value2, Value3, x, y)

   'get general reference line plan points data
      ReDim CurveType(0)
      ReDim Value1(0)
      ReDim Value2(0)
      ReDim Value3(0)
      ReDim x(0)
      ReDim y(0)
      Ret = SapModel.GenRefLine.GetLinePlanPoints(Name, NumberPoints, Value1, Value2, Value3, x, y)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.0.

## See Also

[SetLinePlanPoints](SetLinePlanPoints.htm) [GetLine](GetLine_{Gen_Ref_Line}.htm) [GetLineElevPoints](GetLineElevPoints.htm)



## GetLine {Gen Ref Line}

*Source file: `SAP2000_API_Fuctions/Definitions/General_Reference_Line/GetLine_{Gen_Ref_Line}.htm`*

# GetLine

## Syntax

SapObject.SapModel.GenRefLine.GetLine

## VB6 Procedure

Function GetLine(ByVal Name As String, ByRef DiscLength As Double, ByRef DiscAngle As Double, ByRef Color As Long, ByRef Visible As Boolean) As Long

## Parameters

Name

The name of an existing general reference line.

DiscLength

The maximum segment discretization length of the segments used to define curves in the general reference line. [L]

DiscAngle

The maximum discretization angle in degrees for the general reference line. [deg]

Color

The display color assigned to the general reference line.

Visible

Specifies whether the general reference line will be displayed in windows displaying the model.

## Remarks

The function returns zero if the general reference line data is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetGenRefLine()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim discLength As Double, discAngle As Double
      Dim color As Long
      Dim visible As Boolean

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

   'define new general reference line
      ret = SapModel.GenRefLine.SetLine("GRef1", 120, 5)

   'get new general reference line
      ret = SapModel.GenRefLine.GetLine("GRef1", discLength, discAngle, color, visible)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.0.

## See Also

[SetLine](SetLine_{Gen_Ref_Line}.htm) [GetLinePlanPoints](GetLinePlanPoints.htm) [GetLineElevPoints](GetLineElevPoints.htm)



## GetNameList {Gen Ref Line}

*Source file: `SAP2000_API_Fuctions/Definitions/General_Reference_Line/GetNameList_{Gen_Ref_Line}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.GenRefLine.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of general reference line names retrieved by the program.

MyName

This is a one-dimensional array of general reference line names. The MyName array is created as a dynamic, zero-based array by the API user:

Dim MyName() As String

The array is dimensioned to (NumberNames – 1) inside the SAP2000 program, filled with the names, and returned to the API user.

## Remarks

This function retrieves the names of all defined general reference lines.

The function returns the names; otherwise it returns a nonzero value.

## VBA Example

Sub GetGenRefLineNames()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'define new general reference line
      ret = SapModel.GenRefLine.SetLine("GRef1", 120, 5)

   'get general reference line names
      ret = SapModel.GenRefLine.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.0.

## See Also

[SetLine](SetLine_{Gen_Ref_Line}.htm)



## SetLineElevPoints

*Source file: `SAP2000_API_Fuctions/Definitions/General_Reference_Line/SetLineElevPoints.htm`*

# SetLineElevPoints

## Syntax

SapObject.SapModel.GenRefLine.SetLineElevPoints

## VB6 Procedure

Function SetLineElevPoints(ByVal Name As String, ByVal NumberPoints As Long, ByRef CurveType() As Long, ByRef Value1() As Double, ByRef Value2() As Double, ByRef Value3() As Double, ByRef s() As Double, ByRef z() As Double) As Long

## Parameters

Name

The name of a defined general reference line.

NumberPoints

The number of points used to define the general reference line elevation layout.

CurveType

This is an array of values indicating the general reference line elevation layout curve type for each point.

0 = None
1 = Circular Curve
2 = Highway Curve
3 = Parabolic Curve
4 = Bezier Curve
5 = BSpline Curve
6 = Bezier Curve Child Point
7 = BSpline Curve Child Point

Value1

This is the value of a parameter used to define the general reference line layout. The item that Value1 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Curve Radius [L]
CurveType = 2: Curve Radius [L]
CurveType = 3: Angle measured from the horizontal, up station axis, to the axis of symmetry of the parabolic curve. [deg]
CurveType = 4: Number of control points. This is currently hard-wired internally to 4.
CurveType = 5: Number of control points.
CurveType = 6: Not Used
CurveType = 7: Not Used

Value2

This is the value of a parameter used to define the general reference line layout. The item that Value2 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Not Used
CurveType = 2: Curve length, including length of spirals on either end. [L]
CurveType = 3: Rate at which the slope of a parabolic curve is changing in percent. [1/L]
CurveType = 4: Number of discretization points.
CurveType = 5: Number of discretization points.
CurveType = 6: Not Used
CurveType = 7: Not Used

Value3

This is the value of a parameter used to define the general reference line layout. The item that Value3 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Not Used
CurveType = 2: Not Used
CurveType = 3: Not Used
CurveType = 4: Not Used
CurveType = 5: Curve order.
CurveType = 6: Not Used
CurveType = 7: Not Used

x

This is an array of the station coordinate of each point in the coordinate system specified for the general reference line. [L]

y

This is an array of the Z coordinate of each point in the coordinate system specified for the general reference line. [L]

## Remarks

This function assigns the general reference line elevation layout parameters.

A minimum of three points is required for the Circular, Highway, and Parabolic curves. The Bezier curve requires a minimum of four points. The BSpline curve requires a minimum of two points.

The Bezier and BSpline curve types require additional control points as specified by Value2. These control points are considered to be defined directly after the point specifying the Bezier or BSpline curve. Any Value1, Value2, or Value3 parameters defined on these control points are ignored.

The function returns zero if the general reference line parameters are successfully defined; otherwise it returns a nonzero value.

## VBA Example

Sub SetElevPoints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberPoints As Long
      Dim CurveType() As Long
      Dim Value1() As Double
      Dim Value2() As Double
      Dim Value3() As Double
      Dim s() As Double
      Dim z() As Double

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

   'add new general reference line
      Name = "GRef1"
      ret = SapModel.GenRefLine.SetLine(Name, 120, 5)

   'set general reference line elev points data
      NumberPoints = 3
      ReDim CurveType(NumberPoints – 1)
      ReDim s(NumberPoints – 1)
      Redim z(NumberPoints – 1)
      CurveType(0) = 0
      CurveType(1) = 1
      CurveType(2) = 0
      s(0) = 0: z(0) = 0
      s(1) = 100: z(1) = 100
      s(2) = 200: z(2) = 100
      Value1(0) = 0: Value1(1) = 100: Value1(2) = 0
      Value2(0) = 0: Value2(1) = 0: Value2(2) = 0
      Value3(0) = 0: Value3(1) = 0: Value3(2) = 0
      ret = SapModel.GenRefLine.SetLineElevPoints(Name, NumberPoints, CurveType, Value1, Value2, Value3, s, z)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.0.

## See Also

[GetLineElevPoints](GetLineElevPoints.htm)
[SetLine](SetLine_{Gen_Ref_Line}.htm)
[SetLinePlanPoints](SetLinePlanPoints.htm)



## SetLinePlanPoints

*Source file: `SAP2000_API_Fuctions/Definitions/General_Reference_Line/SetLinePlanPoints.htm`*

# SetLinePlanPoints

## Syntax

SapObject.SapModel.GenRefLine.SetLinePlanPoints

## VB6 Procedure

Function SetLinePlanPoints(ByVal Name As String, ByVal NumberPoints As Long, ByRef CurveType() As Long, ByRef Value1() As Double, ByRef Value2() As Double, ByRef Value3() As Double, ByRef x() As Double, ByRef y() As Double) As Long

## Parameters

Name

The name of a defined general reference line.

NumberPoints

The number of points used to define the general reference line plan layout.

CurveType

This is an array of values indicating the general reference line plan layout curve type for each point.

0 = None
1 = Circular Curve
2 = Highway Curve
3 = Parabolic Curve
4 = Bezier Curve
5 = BSpline Curve
6 = Bezier Curve Child Point
7 = BSpline Curve Child Point

Value1

This is the value of a parameter used to define the general reference line layout. The item that Value1 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Curve Radius [L]
CurveType = 2: Curve Radius [L]
CurveType = 3: Angle measured from the X-axis of the coordinate system in which the general reference line is defined, to the axis of symmetry of the parabolic curve. [deg]
CurveType = 4: Number of control points. This is currently hard-wired internally to 4.
CurveType = 5: Number of control points.
CurveType = 6: Not Used
CurveType = 7: Not Used

Value2

This is the value of a parameter used to define the general reference line layout. The item that Value2 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Not Used
CurveType = 2: Curve length, including length of spirals on either end. [L]
CurveType = 3: Rate at which the slope of a parabolic curve is changing in percent. [1/L]
CurveType = 4: Number of discretization points.
CurveType = 5: Number of discretization points.
CurveType = 6: Not Used
CurveType = 7: Not Used

Value3

This is the value of a parameter used to define the general reference line layout. The item that Value3 represents depends on the CurveType item.

CurveType = 0: Not Used
CurveType = 1: Not Used
CurveType = 2: Not Used
CurveType = 3: Not Used
CurveType = 4: Not Used
CurveType = 5: Curve order.
CurveType = 6: Not Used
CurveType = 7: Not Used

x

This is an array of the X coordinate of each point in the coordinate system specified for the general reference line. [L]

y

This is an array of the Y coordinate of each point in the coordinate system specified for the general reference line. [L]

## Remarks

This function assigns the general reference line plan layout parameters.

A minimum of three points is required for the Circular, Highway, and Parabolic curves. The Bezier curve requires a minimum of four points. The BSpline curve requires a minimum of two points.

The Bezier and BSpline curve types require additional control points as specified by Value2. These control points are considered to be defined directly after the point specifying the Bezier or BSpline curve. Any Value1, Value2, or Value3 parameters defined on these control points are ignored.

The function returns zero if the general reference line parameters are successfully defined; otherwise it returns a nonzero value.

## VBA Example

Sub SetPlanPoints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberPoints As Long
      Dim CurveType() As Long
      Dim Value1() As Double
      Dim Value2() As Double
      Dim Value3() As Double
      Dim x() As Double
      Dim y() As Double

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

   'add new general reference line
      Name = "GRef1"
      ret = SapModel.GenRefLine.SetLine(Name, 120, 5)

   'set general reference line plan points data
      NumberPoints = 3
      ReDim CurveType(NumberPoints – 1)
      ReDim x(NumberPoints – 1)
      Redim y(NumberPoints – 1)
      CurveType(0) = 0
      CurveType(1) = 1
      CurveType(2) = 0
      x(0) = 0: y(0) = 0
      x(1) = 100: y(1) = 100
      x(2) = 200: y(2) = 100
      Value1(0) = 0: Value1(1) = 100: Value1(2) = 0
      Value2(0) = 0: Value2(1) = 0: Value2(2) = 0
      Value3(0) = 0: Value3(1) = 0: Value3(2) = 0
      ret = SapModel.GenRefLine.SetLinePlanPoints(Name, NumberPoints, CurveType, Value1, Value2, Value3, x, y)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.0.

## See Also

[GetLinePlanPoints](GetLinePlanPoints.htm)
[SetLine](SetLine_{Gen_Ref_Line}.htm)
[SetLineElevPoints](SetLineElevPoints.htm)



## SetLine {Gen Ref Line}

*Source file: `SAP2000_API_Fuctions/Definitions/General_Reference_Line/SetLine_{Gen_Ref_Line}.htm`*

# SetLine

## Syntax

SapObject.SapModel.GenRefLine.SetLine

## VB6 Procedure

Function SetLine(ByVal Name As String, ByVal DiscLength As Double, ByVal DiscAngle As Double, Optional ByVal CSys As String = "Global", Optional ByVal Color As Long = -1, Optional ByVal Visible As Boolean = True) As Long

## Parameters

Name

This is the name of a general reference line. If this is the name of an existing general reference line, that general reference line is modified; otherwise a new general reference line is added.

DiscLength

The maximum segment discretization length of the segments used to define curves in the general reference line. [L]

DiscAngle

The maximum discretization angle in degrees for the general reference line. [deg]

CSys

The name of the coordinate system in which the general reference line is defined.

Color

The display color assigned to the general reference line. If Color is specified as -1, the program will automatically assign a color.

Visible

The item is True if the general reference line should be displayed in windows displaying the model.

## Remarks

The function returns zero if the general reference line is successfully added or modified; otherwise it returns a nonzero value.

## VBA Example

Sub AddGenRefLine()
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

   'define new general reference line
      ret = SapModel.GenRefLine.SetLine("GRef1", 120, 5)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.0.

## See Also

[GetLine](GetLine_{Gen_Ref_Line}.htm) [SetLinePlanPoints](SetLinePlanPoints.htm) [SetLineElevPoints](SetLineElevPoints.htm)

[Delete](Delete_{Gen_Ref_Line}.htm)

