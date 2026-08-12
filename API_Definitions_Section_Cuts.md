# API Definitions Section Cuts

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Definitions/Section_Cuts

---



## AddQuad

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/AddQuad.htm`*

# AddQuad

## Syntax

SapObject.SapModel.SectCut.AddQuad

## VB6 Procedure

Function AddQuad(ByVal Name As String, ByRef X() As Double, ByRef Y() As Double, ByRef Z() As Double) As Long

## Parameters

Name

The name of an existing section cut.

GroupName

X

This is an array of four X coordinates, one for each of the four points defining the quadrilateral.

Y

This is an array of four Y coordinates, one for each of the four points defining the quadrilateral.

Z

This is an array of four Z coordinates, one for each of the four points defining the quadrilateral.

## Remarks

This function adds a new quadrilateral to a section cut defined by quadrilaterals.

The function returns zero if the quadrilateral is successfully, otherwise it returns a nonzero value.

## VBA Example

Sub AddSectionCutQuad()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim X(3) As Double

Dim Y(3) As Double

Dim Z(3) As Double

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("2", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("3", "Group1")

'define section cut

X(0) = -300

X(1) = -270

X(2) = -270

X(3) = -300

Y(0) = 10

Y(1) = 10

Y(2) = -10

Y(3) = -10

Z(0) = 10

Z(1) = 10

Z(2) = 10

Z(3) = 10

ret = SapModel.SectCut.SetByQuad("SCut1", "Group1", 1, X, Y, Z)

'add a second quadrilateral

X(0) = 270

X(1) = 300

X(2) = 300

X(3) = 270

Y(0) = 10

Y(1) = 10

Y(2) = -10

Y(3) = -10

Z(0) = 10

Z(1) = 10

Z(2) = 10

Z(3) = 10

ret = SapModel.SectCut.AddQuad("SCut1", X, Y, Z)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also

[SetByQuad](SetByQuad.htm)



## DeleteCut

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/DeleteCut.htm`*

# DeleteCut

## Syntax

SapObject.SapModel.SectCut.Delete

## VB6 Procedure

Function Delete(ByVal Name As String) As Long

## Parameters

Name

The name of the section cut to be deleted.

## Remarks

This function deletes an existing section cut.

The function returns zero if the section cut is successfully
deleted, otherwise it returns a nonzero value.

## VBA Example

Sub
DeleteSectionCut()

'dimension
variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim X(3) As Double
      Dim Y(3) As Double
      Dim Z(3) As Double

'create
Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

'start
Sap2000 application
      SapObject.ApplicationStart

'create
SapModel object
      Set SapModel = SapObject.SapModel

'initialize
model
      ret
= SapModel.InitializeNewModel

'create
model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

'define
new group
 ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to
group
 ret = SapModel.FrameObj.SetGroupAssign("1",
"Group1")
 ret = SapModel.FrameObj.SetGroupAssign("2", "Group1")
 ret = SapModel.FrameObj.SetGroupAssign("3", "Group1")

'define section
cut
 X(0) = -300
 X(1) = -270
 X(2) = -270
 X(3) = -300
 Y(0) = 10
 Y(1) = 10
 Y(2) = -10
 Y(3) = -10
 Z(0) = 10
 Z(1) = 10
 Z(2) = 10
 Z(3) = 10
 ret = SapModel.SectCut.SetByQuad("SCut1", "Group1",
1, X, Y, Z)

'delete section
cut
 ret = SapModel.SectCut.Delete("SCut1")

'close Sap2000
 SapObject.ApplicationExit False
 Set SapModel = Nothing
 Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 23.4.0.

## See Also

[SetByQuad](SetByQuad.htm)



## GetCutInfo

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/GetCutInfo.htm`*

# GetCutInfo

## Syntax

SapObject.SapModel.SectCut.GetCutInfo

## VB6 Procedure

Function GetCutInfo(ByVal Name As String, ByRef GroupName As String, ByRef MyType As Long , ByRef Num As Long) As Long

## Parameters

Name

The name of an existing section cut.

GroupName

The name of the group associated with the section cut.

MyType

This is either 1, 2, 3 or 4 indicating the result type of the section cut.

1 = Analysis

2 = Design Wall

3 = Design Spandrel

4 = Design Slab

Num

The number of quadrilateral cutting planes defined for the section cut. If this number is zero then the section cut is defined by the associated group.

## Remarks

This function gets basic information about an existing section cut.

The function returns zero if the section cut information is successfully obtained, otherwise it returns a nonzero value.

## VBA Example

Sub GetSectionCutInfo()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim GroupName As String

Dim MyType As Long

Dim Num As Long

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 1)

'get basic section cut information

ret = SapModel.SectCut.GetCutInfo ("SCut1", GroupName, MyType, Num)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also



## GetLocalAxesAnalysys

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/GetLocalAxesAnalysys.htm`*

# GetLocalAxesAnalysys

## Syntax

SapObject.SapModel.SectCut.GetLocalAxesAnalysis

## VB6 Procedure

Function GetLocalAxesAnalysis(ByVal Name As String, ByRef Z As Double, ByRef Y As Double, ByRef X As Double, ByRef IsAdvanced As Boolean) As Long

## Parameters

Name

The name of an existing section cut.

Z

The Rotation about the Z axis.

Y

The rotation about the Y' axis where Y' is the orientation of the Y axis after rotation about the Z axis.

X

The rotation about the X'' axis where X'' is the orientation of the X axis after rotation about the Z axis and about the Y' axis.

IsAdvanced

Indicates if advanced local axes are specified.

## Remarks

This function gets the local axes angles for an existing section cut whose result type is Analysis.

The function returns zero if the angles are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSectionCutLocalAxesAnalysis()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim Z As Double

Dim Y As Double

Dim X As Double

Dim IsAdvanced As Boolean

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 1)

'set section cut local axes angles

ret = SapModel.SectCut.SetLocalAxesAnalysis ("SCut1", 10, 20, 30)

'get section cut local axes data

ret = SapModel.SectCut.GetLocalAxesAnalysis ("SCut1",Z, Y, X, IsAdvanced)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also

[GetLocalAxesAdvancedAnalysis](GetLocalAxisAdvancedAnalysis.htm)



## GetLocalAxesAngleDesign

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/GetLocalAxesAngleDesign.htm`*

# GetLocalAxesAngleDesign

## Syntax

SapObject.SapModel.SectCut.GetLocalAxesAngleDesign

## VB6 Procedure

Function GetLocalAxesAngleDesign(ByVal Name As String, ByRef Angle As Double) As Long

## Parameters

Name

The name of an existing section cut.

Angle

For design local axes orientation type wall this is the angle from the global X to the local 2 axis.  For orientation types spandrel and slab it is the angle from the global X to the local 1 axis.

## Remarks

This function gets the local axes angle for section cuts whose result type is Design (Wall, Spandrel or Slab).

The function returns zero if the angle is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSectionCutLocalAxesAngleDesign ()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim Angle As Double

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut with result type of Design - Wall

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 2)

'set section cut local axes angle

ret = SapModel.SectCut.SetLocalAxesAngleDesign("SCut1", 24)

'get section cut local axes angle

ret = SapModel.SectCut.GetLocalAxesAngleDesign("SCut1", Angle)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also



## GetLocalAxisAdvancedAnalysis

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/GetLocalAxisAdvancedAnalysis.htm`*

# GetLocalAxisAdvancedAnalysis

## Syntax

SapObject.SapModel.SectCut.GetLocalAxesAdvancedAnalysis

## VB6 Procedure

Function GetLocalAxesAdvancedAnalysis(ByVal Name As String, ByRef Active As Boolean, ByRef AxVectOpt As Long, ByRef AxCSys As String, ByRef axdir() As Long, ByRef AxPt() As String, ByRef AxVect() As Double, ByRef Plane2 As Long, ByRef PlVectOpt As Long, ByRef PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double) As Long

## Parameters

Name

The name of an existing section cut.

Active

This is True if advanced local axes exist.

AxVectOpt, PlVectOpt

This is 1, 2 or 3, indicating the axis/plane reference vector option. This item applies only when the Active item is True.

1 = Coordinate direction

2 = Two joints

3 = User vector

AxCSys, PlCSys

The coordinate system used to define the axis/plane reference vector coordinate directions and the axis/plane user vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 1 or 3.

AxDir, PlDir

This is an array dimensioned to 1 (2 integers), indicating the axis/plane reference vector primary and secondary coordinate directions, PlDir(0) and PlDir(1) respectively, taken at the object center in the specified coordinate system and used to determine the plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 1. Possible coordinate direction values are:

1 = +X            -1 = -X

2 = +Y            -2 = -Y

3 = +Z            -3 = -Z

4 = +CR           -4 = -CR

5 = +CA           -5 = -CA

6 = +CZ           -6 = -CZ

7 = +SR           -7 = -SR

8 = +SA           -8 = -SA

9 = +SB           -9 = -SB

AxPt, PlPt

This is an array dimensioned to 1 (2 strings), indicating the labels of two joints that define the axis/plane reference vector. Either of these joints may be specified as None to indicate the center of the specified object.  If both joints are specified as None, they are not used to define the plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 2.

AxVect, PlVect

This is an array dimensioned to 2 (3 doubles) that defines the axis/plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 3.

Plane2

This is 12, 13, 21, 23, 31 or 32, indicating that the local plane determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, 0r 3-2 plane. This item applies only when the Active item is True.

## Remarks

This function gets the advanced local axes data for an existing section cut whose result type is Analysis.

The function returns zero if the data is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSectionCutLocalAxesAdvancedAnalysis()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim Active As Boolean

Dim AxVectOpt As Long

Dim AxCSys As String

Dim MyAxDir() As Long

Dim MyAxPt() As String

Dim MyAxVect() As Double

Dim Plane2 As Long

Dim PlVectOpt As Long

Dim PlCSys As String

Dim MyPlDir() As Long

Dim MyPlPt() As String

Dim MyPlVect() As Double

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 1)

'set section cut advanced local axes data

Redim MyAxDir(1)

Redim MyAxPt(1)

Redim MyAxVect(2)

Redim MyPlDir(1)

Redim MyPlPt(1)

Redim MyPlVect(2)

**MyAxVect(0)=0.707**

MyAxVect(1)=0.707

MyAxVect(2)=0

MyPlDir(0) = 2

MyPlDir(1) = 3

ret = SapModel.SectCut.SetLocalAxesAdvancedAnalysis("SCut1", True, 3, "Global", MyAxDir, MyAxPt, MyAxVect, 12, 1, "Global", MyPlDir, MyPlPt, MyPlVect)

'get section cut advanced local axes data

ret = SapModel.SectCut.GetLocalAxesAdvancedAnalysis("SCut1", Active, AxVectOpt, AxCSys, MyAxDir, MyAxPt, MyAxVect, Plane2, PlVectOpt, PlCSys, MyPlDir, MyPlPt, MyPlVect)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also

[GetLocalAxesAnalysis](GetLocalAxesAnalysys.htm)



## GetNameList

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/GetNameList.htm`*

# GetNameList

## Syntax

SapObject.SapModel.SectCut. GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of section cut names retrieved by the program.

MyName

This is a one-dimensional array of section cut names. The MyName array is created as a dynamic, zero-based, array by the API user:

Dim MyName() as String

The array is dimensioned to (NumberNames – 1) inside the Sap2000 program, filled with the names, and returned to the API user.

## Remarks

This function retrieves the names of all defined section cuts.

The function returns zero if the names are successfully retrieved, otherwise it returns nonzero.

## VBA Example

Sub GetSectionCutNames()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim NumberNames As Long

Dim MyName() As String

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 1)

'get section cut names

ret = SapModel.SectCut.GetNameList(NumberNames, MyName)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also



## GetQuad

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/GetQuad.htm`*

# GetQuad

## Syntax

SapObject.SapModel.SectCut.GetQuad

## VB6 Procedure

Function AddQuad(ByVal Name As String, ByVal Num As Long, ByRef X() As Double, ByRef Y() As Double, ByRef Z() As Double) As Long

## Parameters

Name

The name of an existing section cut defined using quadrilateral cutting planes.

Num

The number of a quadirilateral cutting plane in the section cut.

GroupName

X

This is an array of four X coordinates, one for each of the four points defining the quadrilateral.

Y

This is an array of four Y coordinates, one for each of the four points defining the quadrilateral.

Z

This is an array of four Z coordinates, one for each of the four points defining the quadrilateral.

## Remarks

This function returns the coordinates of a quadrilateral cutting plane in a section cut defined by quadrilaterals.

The function returns zero if the coordinates are successfully returned, otherwise it returns a nonzero value.

## VBA Example

Sub GetSectionCutQuad()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim X() As Double

Dim Y() As Double

Dim Z() As Double

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("2", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("3", "Group1")

'define section cut

Redim X(3)

Redim Y(3)

Redim Z(3)

X(0) = -300

X(1) = -270

X(2) = -270

X(3) = -300

Y(0) = 10

Y(1) = 10

Y(2) = -10

Y(3) = -10

Z(0) = 10

Z(1) = 10

Z(2) = 10

Z(3) = 10

ret = SapModel.SectCut.SetByQuad("SCut1", "Group1", 1, X, Y, Z)

'add a second quadrilateral

X(0) = 270

X(1) = 300

X(2) = 300

X(3) = 270

Y(0) = 10

Y(1) = 10

Y(2) = -10

Y(3) = -10

Z(0) = 10

Z(1) = 10

Z(2) = 10

Z(3) = 10

ret = SapModel.SectCut.AddQuad("SCut1", X, Y, Z)

'get coordinates of quadrilateral 2

ret = SapModel.SectCut.GetQuad("SCut1", 2, X, Y, Z)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also



## GetResultLocation

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/GetResultLocation.htm`*

# GetResultLocation

## Syntax

SapObject.SapModel.SectCut.GetResultLocation

## VB6 Procedure

Function GetResultLocation(ByVal Name As String, ByRef IsDefault As Boolean, ByRef X As Double, ByRef Y As Double, ByRef Z As Double) As Long

## Parameters

Name

The name of an existing section cut.

IsDefault

Indicates if the section cut results are reported at the default location.  If so, the X, Y and Z items are ignored.

X

The X coordinate of the section cut result location when it is not default

Y

The Y coordinate of the section cut result location when it is not default

Z

The Z coordinate of the section cut result location when it is not default

## Remarks

This function gets the results location for an existing section cut.

The function returns zero if the result location is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSectionCutResultsLocation()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim IsDefault As Boolean

Dim X As Double

Dim Y As Double

Dim Z As Double

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 1)

'set section cut result location

ret = SapModel.SectCut.SetResultLocation("SCut1", False, -288, 0, 10)

'get section cut result location

ret = SapModel.SectCut.GetResultLocation("SCut1", IsDefault, X, Y, Z)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also



## GetResultsSide

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/GetResultsSide.htm`*

# GetResultsSide

## Syntax

SapObject.SapModel.SectCut.GetResultsSide

## VB6 Procedure

Function GetResultsSide(ByVal Name As String, ByRef Side As Long) As Long

## Parameters

Name

The name of an existing section cut.

Side

This item is either 1 or 2 and indicates the side of the elements from which section cut results are obtained.

For section cuts defined from quadrilaterals with an Analysis result type:

1 = Positive 3-axis side of quadrilateral

2 = Negative 3-axis side of quadrilateral

For section cuts with a Design Wall result type:

1 = Top

2 = Bottom

For section cuts with a Design Spandrel or Design Slab result type:

1 = Right

2 = Left

## Remarks

This function gets the side of the elements from which results are obtained.

The function returns zero if the side is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSectionCutResultsSide()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim Side As Long

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut with result type of Design - Wall

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 2)

'set section cut results side

ret = SapModel.SectCut.SetResultsSide ("SCut1", 2)

'get section cut results side

ret = SapModel.SectCut.GetResultsSide ("SCut1", Side)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also



## SetByGroup

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/SetByGroup.htm`*

# SetByGroup

## Syntax

SapObject.SapModel.SectCut.SetByGroup

## VB6 Procedure

Function SetByGroup(ByVal Name As String, ByVal GroupName As String, ByVal MyType As Long) As Long

## Parameters

Name

The section cut name. If a section cut with this name already exists then the section cut is reinitialized with the new data.  All previous data assigned to the section cut is lost. If a section cut with this name does not exist then a new section cut is added.

GroupName

The name of the group on which the section cut is based.

MyType

This is either 1, 2, 3 or 4 indicating the result type of the section cut.

1 = Analysis

2 = Design Wall

3 = Design Spandrel

4 = Design Slab

## Remarks

This function adds a new section cut defined by a group to the model or reinitializes an existing section cut to be defined by a group.

The function returns zero if the section cut is successfully added or initialized, otherwise it returns a nonzero value.

## VBA Example

Sub SetSectionCutByGroup()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 1)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also

[SetByQuad](SetByQuad.htm)



## SetByQuad

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/SetByQuad.htm`*

# SetByQuad

## Syntax

SapObject.SapModel.SectCut.SetByQuad

## VB6 Procedure

Function SetByQuad(ByVal Name As String, ByVal GroupName As String, ByVal MyType As Long, ByRef X() As Double, ByRef Y() As Double, ByRef Z() As Double) As Long

## Parameters

Name

The section cut name. If a section cut with this name already exists then the section cut is reinitialized with the new data.  All previous data assigned to the section cut is lost. If a section cut with this name does not exist then a new section cut is added.

GroupName

The name of the group associated with the section cut.

MyType

This is either 1, 2, 3 or 4 indicating the result type of the section cut.

1 = Analysis

2 = Design Wall

3 = Design Spandrel

4 = Design Slab

X

This is an array of four X coordinates, one for each of the four points defining the quadrilateral.

Y

This is an array of four Y coordinates, one for each of the four points defining the quadrilateral.

Z

This is an array of four Z coordinates, one for each of the four points defining the quadrilateral.

## Remarks

This function adds a new section cut defined by a quadrilateral to the model or reinitializes an existing section cut to be defined by a quadrilateral.

The function returns zero if the section cut is successfully added or initialized, otherwise it returns a nonzero value.

## VBA Example

Sub SetSectionCutByQuad()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim X(3) As Double

Dim Y(3) As Double

Dim Z(3) As Double

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("2", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("3", "Group1")

'define section cut

X(0) = -300

X(1) = 300

X(2) = 300

X(3) = -300

Y(0) = 10

Y(1) = 10

Y(2) = -10

Y(3) = -10

Z(0) = 10

Z(1) = 10

Z(2) = 10

Z(3) = 10

ret = SapModel.SectCut.SetByQuad("SCut1", "Group1", 1, X, Y, Z)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also

[SetByGroup](SetByGroup.htm)

[AddQuad](AddQuad.htm)

[DeleteCut](DeleteCut.htm)



## SetLocalAxesAnalysis

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/SetLocalAxesAnalysis.htm`*

# SetLocalAxesAnalysis

## Syntax

SapObject.SapModel.SectCut.SetLocalAxesAnalysis

## VB6 Procedure

Function SetLocalAxesAnalysis(ByVal Name As String, ByVal Z As Double, ByVal Y As Double, ByVal X As Double) As Long

## Parameters

Name

The name of an existing section cut.

Z

The Rotation about the Z axis.

Y

The rotation about the Y' axis where Y' is the orientation of the Y axis after rotation about the Z axis.

X

The rotation about the X'' axis where X'' is the orientation of the X axis after rotation about the Z axis and about the Y' axis.

## Remarks

This function sets the local axes angles for an existing section cut whose result type is Analysis.

The function returns zero if the angles are successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSectionCutLocalAxesAnalysis()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 1)

'set section cut local axes angles

ret = SapModel.SectCut.SetLocalAxesAnalysis ("SCut1", 10, 20, 30)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also

[SetLocalAxesAdvancedAnalysis](SetLocalAxisAdvancedAnalysis.htm)



## SetLocalAxisAdvancedAnalysis

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/SetLocalAxisAdvancedAnalysis.htm`*

# SetLocalAxisAdvancedAnalysis

## Syntax

SapObject.SapModel.SectCut.SetLocalAxesAdvancedAnalysis

## VB6 Procedure

Function SetLocalAxesAdvancedAnalysis(ByVal Name As String, ByVal Active As Boolean, ByVal AxVectOpt As Long, ByVal AxCSys As String, ByRef axdir() As Long, ByRef AxPt() As String, ByRef AxVect() As Double, ByVal Plane2 As Long, ByVal PlVectOpt As Long, ByVal PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double) As Long

## Parameters

Name

The name of an existing section cut.

Active

This is True if advanced local axes exist.

AxVectOpt, PlVectOpt

This is 1, 2 or 3, indicating the axis/plane reference vector option. This item applies only when the Active item is True.

1 = Coordinate direction

2 = Two joints

3 = User vector

AxCSys, PlCSys

The coordinate system used to define the axis/plane reference vector coordinate directions and the axis/plane user vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 1 or 3.

AxDir, PlDir

This is an array dimensioned to 1 (2 integers), indicating the axis/plane reference vector primary and secondary coordinate directions, PlDir(0) and PlDir(1) respectively, taken at the object center in the specified coordinate system and used to determine the plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 1. Possible coordinate direction values are:

1 = +X            -1 = -X

2 = +Y            -2 = -Y

3 = +Z            -3 = -Z

4 = +CR           -4 = -CR

5 = +CA           -5 = -CA

6 = +CZ           -6 = -CZ

7 = +SR           -7 = -SR

8 = +SA           -8 = -SA

9 = +SB           -9 = -SB

AxPt, PlPt

This is an array dimensioned to 1 (2 strings), indicating the labels of two joints that define the axis/plane reference vector. Either of these joints may be specified as None to indicate the center of the specified object.  If both joints are specified as None, they are not used to define the plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 2.

AxVect, PlVect

This is an array dimensioned to 2 (3 doubles) that defines the axis/plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 3.

Plane2

This is 12, 13, 21, 23, 31 or 32, indicating that the local plane determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, 0r 3-2 plane. This item applies only when the Active item is True.

## Remarks

This function sets the advanced local axes data for an existing section cut whose result type is Analysis.

The function returns zero if the data is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSectionCutLocalAxesAdvancedAnalysis()

'dimension variables

Dim SapObject as cOAPI

Dim SapModel As cSapModel

Dim ret As Long

Dim MyAxDir(1) As Long

Dim MyAxPt(1) As String

Dim MyAxVect(2) As Double

Dim MyPlDir(1) As Long

Dim MyPlPt(1) As String

Dim MyPlVect(2) As Double

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

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 1)

'set section cut advanced local axes data

**MyAxVect(0)=0.707**

MyAxVect(1)=0.707

MyAxVect(2)=0

MyPlDir(0) = 2

MyPlDir(1) = 3

ret = SapModel.SectCut.SetLocalAxesAdvancedAnalysis("SCut1", True, 3, "Global", MyAxDir, MyAxPt, MyAxVect, 12, 1, "Global", MyPlDir, MyPlPt, MyPlVect)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also

SetLocalAxesAnalysis



## SetLocalAxisAngleDesign

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/SetLocalAxisAngleDesign.htm`*

# SetLocalAxisAngleDesign

## Syntax

SapObject.SapModel.SectCut.SetLocalAxesAngleDesign

## VB6 Procedure

Function SetLocalAxesAngleDesign(ByVal Name As String, ByVal Angle As Double) As Long

## Parameters

Name

The name of an existing section cut.

Angle

For design local axes orientation type wall this is the angle from the global X to the local 2 axis.  For orientation types spandrel and slab it is the angle from the global X to the local 1 axis.

## Remarks

This function sets the local axes angle for section cuts whose result type is Design (Wall, Spandrel or Slab).

The function returns zero if the angle is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSectionCutLocalAxesAngleDesign ()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut with result type of Design - Wall

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 2)

'set section cut local axes angle

ret = SapModel.SectCut.SetLocalAxesAngleDesign("SCut1", 24)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also



## SetResultLocation

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/SetResultLocation.htm`*

# SetResultLocation

## Syntax

SapObject.SapModel.SectCut.SetResultLocation

## VB6 Procedure

Function SetResultLocation(ByVal Name As String, ByVal IsDefault As Boolean, Optional ByVal X As Double = 0, Optional ByVal Y As Double = 0, Optional ByVal Z As Double = 0) As Long

## Parameters

Name

The name of an existing section cut.

IsDefault

Indicates if the section cut results are reported at the default location.  If so, the X, Y and Z items are ignored.

X

The X coordinate of the section cut result location when it is not default

Y

The Y coordinate of the section cut result location when it is not default

Z

The Z coordinate of the section cut result location when it is not default

## Remarks

This function sets the results location for an existing section cut.

The function returns zero if the result location is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSectionCutResultsLocation()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 1)

'set section cut result location

ret = SapModel.SectCut.SetResultLocation("SCut1", False, -288, 0, 10)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also



## SetResultsSide

*Source file: `SAP2000_API_Fuctions/Definitions/Section_Cuts/SetResultsSide.htm`*

# SetResultsSide

## Syntax

SapObject.SapModel.SectCut.SetResultsSide

## VB6 Procedure

Function SetResultsSide(ByVal Name As String, ByVal Side As Long) As Long

## Parameters

Name

The name of an existing section cut.

Side

This item is either 1 or 2 and indicates the side of the elements from which section cut results are obtained.

For section cuts defined from quadrilaterals with an Analysis result type:

1 = Positive 3-axis side of quadrilateral

2 = Negative 3-axis side of quadrilateral

For section cuts with a Design Wall result type:

1 = Top

2 = Bottom

For section cuts with a Design Spandrel or Design Slab result type:

1 = Right

2 = Left

## Remarks

This function sets the side of the elements from which results are obtained.

The function returns zero if the side is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSectionCutResultsSide()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

'create Sap2000 object

Set SapObject = New Sap2000v16.SapObject

'start Sap2000 application

SapObject.ApplicationStart

'create SapModel object

Set SapModel = SapObject.SapModel

'initialize model

ret = SapModel.InitializeNewModel

'create model from template

ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'define new group

ret = SapModel.GroupDef.SetGroup("Group1")

'add objects to group

ret = SapModel.PointObj.SetGroupAssign("1", "Group1")

ret = SapModel.FrameObj.SetGroupAssign("1", "Group1")

'define section cut with result type of Design - Wall

ret = SapModel.SectCut.SetByGroup("SCut1", "Group1", 2)

'set section cut results side

ret = SapModel.SectCut.SetResultsSide ("SCut1", 2)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also

