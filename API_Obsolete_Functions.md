# API Obsolete Functions

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Obsolete_Functions

---



## AddQuick {Material}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/AddQuick_{Material}.htm`*

# AddQuick  (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropMaterial.AddQuick

## VB6 Procedure

Function AddQuick(ByVal Name As String, ByVal MatType As eMatType, Optional ByVal SteelType As eMatTypeSteel = MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A992\_Fy50, Optional ByVal ConcreteType As eMatTypeConcrete = MATERIAL\_CONCRETE\_SUBTYPE\_FC4000\_NORMALWEIGHT, Optional ByVal AluminumType As eMatTypeAluminum = MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6, Optional ByVal ColdFormedType As eMatTypeColdFormed = MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50, Optional ByVal RebarType As eMatTypeRebar = MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr60, Optional ByVal TendonType As eMatTypeTendon = MATERIAL\_TENDON\_SUBTYPE\_ASTM\_A416Gr270, Optional ByVal UserName As String = "") As Long

## Parameters

Name

This item is returned by the program. It is the name that the program ultimately assigns for the material property. If no UserName is specified, the program assigns a default name to the material property. If a UserName is specified and that name is not used for another material property, the UserName is assigned to the material property.

MatType

This is one of the following items in the eMatType enumeration.

MATERIAL\_STEEL = 1

MATERIAL\_CONCRETE = 2

MATERIAL\_NODESIGN = 3

MATERIAL\_ALUMINUM = 4

MATERIAL\_COLDFORMED = 5

MATERIAL\_REBAR = 6

MATERIAL\_TENDON = 7

SteelType

This is one of the following items in the eMatTypeSteel enumeration.

MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A36 = 1

MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A53GrB = 2

MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A500GrB\_Fy42 = 3

MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A500GrB\_Fy46 = 4

MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A572Gr50 = 5

MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A913Gr50 = 6

MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A992\_Fy50 = 7

MATERIAL\_STEEL\_SUBTYPE\_CHINESE\_Q235 = 8

MATERIAL\_STEEL\_SUBTYPE\_CHINESE\_Q345 = 9

MATERIAL\_STEEL\_SUBTYPE\_INDIAN\_Fe250 = 10

MATERIAL\_STEEL\_SUBTYPE\_INDIAN\_Fe345 = 11

MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S235 = 12

MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S275 = 13

MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S355 = 14

MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S450 = 15

This item is applicable only when MatType = MATERIAL\_STEEL.

ConcreteType

This is one of the following items in the eMatTypeConcrete enumeration.

MATERIAL\_CONCRETE\_SUBTYPE\_FC3000\_NORMALWEIGHT = 1

MATERIAL\_CONCRETE\_SUBTYPE\_FC4000\_NORMALWEIGHT = 2

MATERIAL\_CONCRETE\_SUBTYPE\_FC5000\_NORMALWEIGHT = 3

MATERIAL\_CONCRETE\_SUBTYPE\_FC6000\_NORMALWEIGHT = 4

MATERIAL\_CONCRETE\_SUBTYPE\_FC3000\_LIGHTWEIGHT = 5

MATERIAL\_CONCRETE\_SUBTYPE\_FC4000\_LIGHTWEIGHT = 6

MATERIAL\_CONCRETE\_SUBTYPE\_FC5000\_LIGHTWEIGHT = 7

MATERIAL\_CONCRETE\_SUBTYPE\_FC6000\_LIGHTWEIGHT = 8

MATERIAL\_CONCRETE\_SUBTYPE\_CHINESE\_C20\_NORMALWEIGHT = 9

MATERIAL\_CONCRETE\_SUBTYPE\_CHINESE\_C30\_NORMALWEIGHT = 10

MATERIAL\_CONCRETE\_SUBTYPE\_CHINESE\_C40\_NORMALWEIGHT = 11

MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M15\_NORMALWEIGHT = 12

MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M20\_NORMALWEIGHT = 13

MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M25\_NORMALWEIGHT = 14

MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M30\_NORMALWEIGHT = 15

MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M35\_NORMALWEIGHT = 16

MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M40\_NORMALWEIGHT = 17

MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M45\_NORMALWEIGHT = 18

MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M50\_NORMALWEIGHT = 19

MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M55\_NORMALWEIGHT = 20

MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M60\_NORMALWEIGHT = 21

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C12\_NORMALWEIGHT = 22

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C16\_NORMALWEIGHT = 23

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C20\_NORMALWEIGHT = 24

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C25\_NORMALWEIGHT = 25

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C30\_NORMALWEIGHT = 26

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C35\_NORMALWEIGHT = 27

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C40\_NORMALWEIGHT = 28

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C45\_NORMALWEIGHT = 29

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C50\_NORMALWEIGHT = 30

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C55\_NORMALWEIGHT = 31

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C60\_NORMALWEIGHT = 32

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C70\_NORMALWEIGHT = 33

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C80\_NORMALWEIGHT = 34

MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C90\_NORMALWEIGHT = 35

This item is applicable only when MatType = MATERIAL\_CONCRETE.

AluminumType

This is one of the following items in the eMatTypeAluminum enumeration.

MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6 = 1

MATERIAL\_ALUMINUM\_SUBTYPE\_6063\_T6 = 2

MATERIAL\_ALUMINUM\_SUBTYPE\_5052\_H34 = 3

This item is applicable only when MatType = MATERIAL\_ALUMINUM.

ColdFormedType

This is one of the following items in the eMatTypeColdFormed enumeration.

MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr33 = 1

MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50 = 2

This item is applicable only when MatType = MATERIAL\_COLDFORMED.

RebarType

This is one of the following items in the eMatTypeRebar enumeration.

MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr40 = 1

MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr60 = 2

MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr75 = 3

MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A706 = 4

MATERIAL\_REBAR\_SUBTYPE\_CHINESE\_HPB235 = 5

MATERIAL\_REBAR\_SUBTYPE\_CHINESE\_HRB335 = 6

MATERIAL\_REBAR\_SUBTYPE\_CHINESE\_HRB400 = 7

MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_Mild250 = 8

MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_HYSD415 = 9

MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_HYSD500 = 10

MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_HYSD550 = 11

This item is applicable only when MatType = MATERIAL\_REBAR.

TendonType

This is one of the following items in the eMatTypeTendon enumeration.

MATERIAL\_TENDON\_SUBTYPE\_ASTM\_A416Gr250 = 1

MATERIAL\_TENDON\_SUBTYPE\_ASTM\_A416Gr270 = 2

This item is applicable only when MatType = MATERIAL\_TENDON.

UserName

This is an optional user specified name for the material property. If a UserName is specified and that name is already used for another material property, the program ignores the UserName.

## Remarks

This function adds a new material property to the model using built-in default values.

The function returns zero if the property is successfully added; otherwise it returns nonzero.

## VBA Example

Sub AddMaterialQuick()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String

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

   'add ASTM A706 rebar material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_REBAR, , , , , MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A706)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Added Steel Material Types for Indian and European codes, Concrete Material Types for Indian and European codes, and Rebar for the Indian code in SAP2000 Version 15.0.0 and CSiBridge Version 15.1.0.

The function is obsolete and has been superseded by [AddMaterial](../Definitions/Properties/Material/AddMaterial.htm) as of version 15.2.0. This function is maintained for backward compatibility. New function added.

## See Also



## AssembledJointMass

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/AssembledJointMass.htm`*

# AssembledJointMass

## Syntax

SapObject.SapModel.Results.AssembledJointMass

## VB6 Procedure

Function AssembledJointMass(ByVal Name As String, ByVal ItemTypeElm As eItemTypeElm, ByRef PointElm() As String, ByRef U1() As Double, ByRef U2() As Double, ByRef U3() As Double, ByRef R1() As Double, ByRef R2() As Double, ByRef R3() As Double) As Long

## Parameters

Name

The name of an existing point element or group of objects, depending on the value of the ItemTypeElm item.

ItemTypeElm

This is one of the following items in the eItemTypeElm enumeration:

ObjectElm = 0

Element = 1

GroupElm = 2

SelectionElm = 3

If this item is ObjectElm, the result request is for the point element corresponding to the point object specified by the Name item.

If this item is Element, the result request is for the point element specified by the Name item.

If this item is GroupElm, the result request is for all point elements directly or indirectly specified in the group specified by the Name item.

If this item is SelectionElm, the result request is for all point elements directly or indirectly selected and the Name item is ignored.

See Item [Type for Elements](../Analysis_Results/Results/Item_Type_for_Elements.htm) for more information.

NumberResults

The total number of results returned by the program.

PointElm

This is an array that includes the point element name associated with each result.

U1, U2, U3

These are one dimensional arrays that include the translational mass in the point element local 1, 2 and 3 axes directions, respectively, for each result. [M]

R1, R2, R3

These are one dimensional arrays that include the rotational mass moment of inertia about the point element local 1, 2 and 3 axes, respectively, for each result. [ML2]

## Remarks

This function reports the assembled joint masses for the specified point elements.

The function returns zero if the masses are successfully recovered, otherwise it returns a nonzero value.

See [Analysis Results Remarks](../Analysis_Results/Results/Analysis_Results_Remarks.htm) for more information.

## VBA Example

Sub GetAssembledJointMass()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberResults As Long
      Dim PointElm() As String
      Dim U1() As Double
      Dim U2() As Double
      Dim U3() As Double
      Dim R1() As Double
      Dim R2() As Double
      Dim R3() As Double

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

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'get assembled joint mass for all point elements
      ret = SapModel.Results.AssembledJointMass("ALL", GroupElm, NumberResults, PointElm, U1, U2, U3, R1, R2, R3)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## ChangeCoordinates {Point}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/ChangeCoordinates_{Point}.htm`*

# ChangeCoordinates  (Note:  Newer function available)

## Syntax

SapObject.SapModel.EditPoint.ChangeCoordinates

## VB6 Procedure

Function ChangeCoordinates(ByVal Name As String, ByVal x As Double, ByVal y As Double, ByVal z As Double) As Long

## Parameters

Name

The name of an existing point object.

x, y, z

These are the new x, y and z coordinates, in the present coordinate system, for the specified point object.

## Remarks

This function changes the coordinates of a specified point object.

The function returns zero if the coordinate change is successful; otherwise it returns a nonzero value.

## VBA Example

Sub ChangePointCoordinates()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'change point coordinates
      ret = SapModel.EditPoint.ChangeCoordinates("1", -288, 0, 36)
      ret = SapModel.View.RefreshWindow

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

The function is obsolete and has been superseded by [ChangeCoordinates\_1](../edit/edit_point/ChangeCoordinates_1_{Point}.htm) as of version 11.05. This function is maintained for backward compatibility. New function added.

## See Also



## Divide {Area Object}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/Divide_{Area_Object}.htm`*

# Divide (Note:  Newer function available)

## Syntax

SapObject.SapModel.EditArea.Divide

## VB6 Procedure

Function Divide(ByVal Name As String, ByVal MeshType As Long, ByRef NumberAreas As Long, ByRef AreaName() As String, Optional ByVal n1 As Long = 2, Optional ByVal n2 As Long = 2, Optional ByVal MaxSize1 As Double = 0, Optional ByVal MaxSize2 As Double = 0, Optional ByVal PointOnEdgeFromGrid As Boolean = False, Optional ByVal PointOnEdgeFromLine As Boolean = False, Optional ByVal PointOnEdgeFromPoint As Boolean = False, Optional ByVal ExtendCookieCutLines As Boolean = False, Optional ByVal Rotation As Double = 0, Optional ByVal MaxSizeGeneral As Double = 0, Optional ByVal LocalAxesOnEdge As Boolean = False, Optional ByVal LocalAxesOnFace As Boolean = False, Optional ByVal RestraintsOnEdge As Boolean = False, Optional ByVal RestraintsOnFace As Boolean = False) As Long

## Parameters

Name

The name of an existing area object.

MeshType

This item is 1, 2, 3, 4, 5 or 6, indicating the mesh type for the area object.

1 = Mesh area into a specified number of objects

2 = Mesh area into objects of a specified maximum size

3 = Mesh area based on points on area edges

4 = Cookie cut mesh area based on lines intersecting edges

5 = Cookie cut mesh area based on points

6 = Mesh area using General Divide Tool

Mesh options 1, 2 and 3 apply to quadrilaterals and triangles only.

NumberAreas

The number of area objects created when the specified area object is divided.

AreaName

This is an array of the name of each area object created when the specified area object is divided.

n1

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed area object that runs from point 1 to point 2.

n2

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed area object that runs from point 1 to point 3.

MaxSize1

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed area object that runs from point 1 to point 2. [L]

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

MaxSize2

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed area object that runs from point 1 to point 3. [L]

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

PointOnEdgeFromGrid

This item applies when MeshType = 3. If it is True, points on the area object edges are determined from intersections of visible grid lines with the area object edges.

PointOnEdgeFromLine

This item applies when MeshType = 3. If it is True, points on the area object edges are determined from intersections of selected straight line objects with the area object edges.

PointOnEdgeFromPoint

This item applies when MeshType = 3. If it is True, points on the area object edges are determined from selected point objects that lie on the area object edges.

ExtendCookieCutLines

This item applies when MeshType = 4. MeshType = 4 provides cookie cut meshing based on selected straight line objects that intersect the area object edges. If the ExtendCookieCutLines item is True, all selected straight line objects are extended to intersect the area object edges for the purpose of meshing the area object.

Rotation

This item applies when MeshType = 5. MeshType = 5 provides cookie cut meshing based on two perpendicular lines passing through selected point objects. By default these lines align with the area object local 1 and 2 axes. The Rotation item is an angle in degrees that the meshing lines are rotated from their default orientation. [deg]

MaxSizeGeneral

This item applies when MeshType = 6. It is the maximum size of objects created by the General Divide Tool.

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

LocalAxesOnEdge

If this item is True, and if both points along an edge of the original area object have the same local axes, the program makes the local axes for added points along the edge the same as the edge end points.

LocalAxesOnFace

If this item is True, and if all points around the perimeter of the original area object have the same local axes, the program makes the local axes for all added points the same as the perimeter points.

RestraintsOnEdge

If this item is True, and if both points along an edge of the original area object have the same restraint/constraint, then, if the added point and the adjacent corner points have the same local axes definition, the program includes the restraint/constraint for added points along the edge.

RestraintsOnFace

If this item is True, and if all points around the perimeter of the original area object have the same restraint/constraint, then, if an added point and the perimeter points have the same local axes definition, the program includes the restraint/constraint for the added point.

## Remarks

This function meshes area objects.

The function returns zero if the meshing is successful; otherwise it returns a nonzero value.

## VBA Example

Sub DivideAreaObject()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberAreas As Long
      Dim AreaName() As String

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

   'divide area object
      ret = SapModel.EditArea.Divide("1", 1, NumberAreas, AreaName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

This function is obsolete and was superseded by [Divide\_1](Divide_{Area_Object}.htm) in release v27.0.0. This function is maintained for backwards compatibility.

## See Also



## GetAPI4F2008

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetAPI4F2008.htm`*

# GetAPI4F2008 (Note:  Newer function available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.GetAPI4F2008

## VB6 Procedure

Function GetAPI4F2008(ByVal Name As String, ByRef ExposureFrom As Long, ByRef DirAngle As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef WindSpeed As Double, ByRef SSLFactor As Double, ) As Long

## Parameters

Name

The name of an existing Wind-type load case with an API 4F 2008 auto wind assignment.

ExposureFrom

This is 2, 3 or 4, indicating the source of the wind exposure.

2 = From area objects

3 = From frame objects (open structure)

4 = From area objects and frame objects (open structure)

DirAngle

The direction angle for the wind load.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

WindSpeed

The design reference wind velocity, Vref, in knots.

SSLFactor

The structural safety level multiplier.

## Remarks

This function retrieves auto wind loading parameters for API 4F 2008.

The function returns zero if the parameters are successfully assigned; otherwise, it returns a nonzero value.

## VBA Example

Sub GetWindAPI4F2008()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ExposureFrom As Long
      Dim DirAngle As Double
      Dim UserZ As Boolean
      Dim TopZ As Double
      Dim BottomZ As Double
      Dim WindSpeed As Double
      Dim SSLFactor As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'add new load case
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WIND)

   'assign API 4F 2008 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetAPI4F2008("WIND", 3, 0, False, 0, 0, 93, 1.1)

   'get API 4F 2008 parameters
      ret = SapModel.LoadPatterns.AutoWind.GetAPI4F2008("WIND", ExposureFrom, DirAngle, UserZ, TopZ, BottomZ, WindSpeed, SSLFactor)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00

The function is obsolete and has been superseded by [GetAPI4F2008\_1](../Definitions/Load_Pattern/Auto_Wind_Load/GetAPI4F2008_1.htm) as of version 14.1.0. This function is maintained for backward compatibility. New function added.

## See Also

[SetAPI4F2008](SetAPI4F2008.htm)



## GetASCE 16 {Auto Seismic}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetASCE_16_{Auto_Seismic}-obsolete.htm`*

# GetASCE716 (Note:  Obsolete, Newer Function Available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoSeismic.GetASCE716

## VB6 Procedure

Function GetASCE716(ByVal Name As String, ByRef nDir() As Boolean, ByRef Eccen As Double, ByRef PeriodFlag As Integer, ByRef CtType As Integer, ByRef UserT As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef R As Double, ByRef Omega As Double, ByRef Cd As Double, ByRef I As Double, ByRef Ss As Double, ByRef S1 As Double, ByRef TL As Double, ByRef SiteClass As Integer, ByRef Fa As Double, ByRef Fv As Double) As Long

## Parameters

Name

The name of an existing Quake-type load pattern with a ASCE 7-16 auto seismic load assignment.

nDir

This is an array with 2 inputs that indicate the seismic load direction.

nDir(1) = True = Global X

nDir(2) = True = Global Y

Eccen

The eccentricity ratio that applies to all diaphragms.

PeriodFlag

This is 1, 2 or 3, indicating the time period option.

1 = Approximate

2 = Program calculated

3 = User defined

CtType

This is 0, 1, 2 or 3, indicating the values of Ct and x. This item is meaningful when the PeriodFlag item is 1 or 2.

0 = Ct = 0.028 (ft),     x = 0.8

1 = Ct = 0.016 (ft),     x = 0.9

2 = Ct = 0.03 (ft),      x = 0.75

3 = Ct = 0.02 (ft),      x = 0.75

UserT

The user specified time period. This item is meaningful when the PeriodFlag item is 3. [s]

UserZ

This item is True if the top and bottom elevations of the seismic load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto seismic loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto seismic loads are applied. [L]

R

The response modification factor.

Omega

The system overstrength factor.

Cd

The deflection amplification factor.

I

The occupancy importance factor.

SS, S1

The seismic coefficients Ss and S1.

TL

The long-period transition period. [s]

SiteClass

This is 1, 2, 3, 4, 5 or 6, indicating the site class.

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

Fa, Fv

The site coefficients Fa and Fv.

## Remarks

This function retrieves auto seismic loading parameters for the 2016 ASCE 7 code.

The function returns zero if the parameters are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSeismicParametersASCE716()

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(e3DFrameType.BeamSlab, 2, 144, 3, 336, 2, 432 )

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("EQX", eLoadPatternType.Quake)

   'dimension ASCE716 parameters

        Dim nDir() As Boolean

        Dim Eccen As Double

        Dim PeriodFlag As Long

        Dim CtType As Long

        Dim UserT As Double

        Dim UserZ As Boolean

        Dim TopZ As Double

        Dim BottomZ As Double

        Dim R As Double

        Dim Omega As Double

        Dim Cd As Double

        Dim I As Double

        Dim SS As Double

        Dim S1 As Double

        Dim TL As Double

        Dim SiteClass As Long

        Dim Fa As Double

        Dim Fv As Double

        ReDim nDir(2)

        nDir(1) = True

        TopZ = 32

        BottomZ = 14

   'set ASCE716 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetASCE716("EQX", nDir, 0.04, 3, 1, 1.76, True, TopZ, BottomZ, 6, 3.5, 6.5, 1.5, 1.9, 1.1, 8, 3, 0, 0)

   'get ASCE716 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.GetASCE716("EQX", nDir, Eccen, PeriodFlag, CtType, UserT, UserZ, TopZ, BottomZ, R, Omega, Cd, I, SS, S1, TL, SiteClass, Fa, Fv)

      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.2.0.

This function was replaced by [GetASCE716\_1](../Definitions/Load_Pattern/Auto_Seismic_Load/GetASCE_16_{Auto_Seismic}.htm), which is more consistent with other API functions.

## See Also

[SetASCE716](SetASCE16_{Auto_Seismic}-obsolete.htm)



## GetAngle {Frame}_old

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetAngle_{Frame}_old.htm`*

# GetAngle (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropFrame.GetAngle

## VB6 Procedure

Function GetAngle(ByVal Name As String, ByRef FileName
As String, ByRef MatProp As String, ByRef t3 As Double, ByRef t2 As Double,
ByRef tf As Double, ByRef tw As Double, ByRef Color As Long, ByRef Notes
As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing frame section property.

FileName

If the section property was imported from a property
file; this is the name of that file. If the section property was not imported;
this item is blank.

MatProp

The name of the material property for the section.

t3

The vertical leg depth. [L]

t2

The horizontal leg width. [L]

tf

The horizontal leg thickness. [L]

tw

The vertical leg thickness. [L]

Color

The display color assigned to the section.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section.

## Remarks

This function retrieves frame section property data
for an angle-type frame section.

The function returns zero if the section property data
is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePropAngle()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim FileName As String
      Dim MatProp As String
      Dim t3 As Double
      Dim t2 As Double
      Dim tf As Double
      Dim tw As Double
      Dim Color As Long
      Dim Notes As String
      Dim GUID As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetAngle("ANGLE1",
"A992Fy50", 6, 4, 0.5, 0.5)

   'get frame section property data
      ret = SapModel.PropFrame.GetAngle("ANGLE1",
FileName, MatProp, t3, t2, tf, tw, Color, Notes, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[SetAngle](../Definitions/Properties/Frame/SetAngle_{Frame}.htm)

[SetRebarBeam](../Definitions/Properties/Frame/SetRebarBeam.htm)

[GetRebarBeam](../Definitions/Properties/Frame/GetRebarBeam.htm)



## GetAutoLiveLoad {Bridge Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetAutoLiveLoad_{Bridge_Wind_Load}.htm`*

# GetAutoLiveLoad {Bridge Wind Load} (Note:  Newer function available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoWindBridge.GetAutoLiveLoad

## VB6 Procedure

Function GetAutoLiveLoad(ByVal Name As String, ByRef RefLoadPat As String, ByRef Height As Double) As Long

## Parameters

Name

The name of an existing bridge wind - live load type pattern.

RefLoadPat

The name of an existing bridge wind load pattern that is referenced from this wind on live load pattern.

Height

The height above the roadway surface at which the wind on live load should be applied. [L]

## Remarks

This function retrieves auto wind on live load parameters.

The function returns zero if the parameters are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAutoWindLiveLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim RefLoadPat As String

      Dim Height As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open existing model containing a bridge object
      ret = SapModel.File.OpenFile(“C:\Temp\BridgeModel.bdb” )

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WINDONLIVELOAD)

   'set auto wind live load loading type to Auto
      ret = SapModel.LoadPatterns.AutoWindBridge.SetAutoLiveLoad("WINDLIVE", "WIND", 0)

   'get auto wind live load parameters

      ret = SapModel.LoadPatterns.AutoWindBridge.GetAutoLiveLoad("WINDLIVE", RefLoadPat, Height)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v21.0.0.

This function is obsolete and was superseded by [GetAutoLiveLoad\_1](../Definitions/Load_Pattern/Auto_Wind_Bridge/GetAutoLiveLoad_1{Bridge_Wind_Load}.htm) in release v25.2.0. This function is maintained for backwards compatibility.

## See Also

[SetAutoLiveLoad](SetAutoLiveLoad_{Bridge_Wind_Load}.htm)

[GetAutoLiveLoad\_1](../Definitions/Load_Pattern/Auto_Wind_Bridge/GetAutoLiveLoad_1{Bridge_Wind_Load}.htm)



## GetAutoMesh {Area Object}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetAutoMesh_{Area_Object}.htm`*

# GetAutoMesh (Note:  Newer function available)

## Syntax

SapObject.SapModel.AreaObj.GetAutoMesh

## VB6 Procedure

Function GetAutoMesh(ByVal Name As String, ByRef MeshType As Long, ByRef n1 As Long, ByRef n2 As Long, ByRef MaxSize1 As Double, ByRef MaxSize2 As Double, ByRef PointOnEdgeFromLine As Boolean, ByRef PointOnEdgeFromPoint As Boolean, ByRef ExtendCookieCutLines As Boolean, ByRef Rotation As Double, ByRef MaxSizeGeneral As Double, ByRef LocalAxesOnEdge As Boolean, ByRef LocalAxesOnFace As Boolean, ByRef RestraintsOnEdge As Boolean, ByRef RestraintsOnFace As Boolean, ByRef Group As String, ByRef SubMesh As Boolean, ByRef SubMeshSize As Double) As Long

## Parameters

Name

The name of an existing area object.

MeshType

This item is 0, 1, 2, 3, 4, 5 or 6, indicating the automatic mesh type for the area object.

0 = No automatic meshing

1 = Mesh area into a specified number of objects

2 = Mesh area into objects of a specified maximum size

3 = Mesh area based on points on area edges

4 = Cookie cut mesh area based on lines intersecting edges

5 = Cookie cut mesh area based on points

6 = Mesh area using General Divide Tool

Mesh options 1, 2 and 3 apply to quadrilaterals and triangles only.

n1

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed area object that runs from point 1 to point 2.

n2

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed area object that runs from point 1 to point 3.

MaxSize1

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed area object that runs from point 1 to point 2. [L]

MaxSize2

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed area object that runs from point 1 to point 3. [L]

PointOnEdgeFromLine

This item applies when MeshType = 3. If it is True, points on the area object edges are determined from intersections of straight line objects included in the group specified by the Group item with the area object edges.

PointOnEdgeFromPoint

This item applies when MeshType = 3. If it is True, points on the area object edges are determined from point objects included in the group specified by the Group item that lie on the area object edges.

ExtendCookieCutLines

This item applies when MeshType = 4. MeshType = 4 provides cookie cut meshing based on straight line objects included in the group specified by the Group item that intersect the area object edges. If the ExtendCookieCutLines item is True, all straight line objects included in the group specified by the Group item are extended to intersect the area object edges for the purpose of meshing the area object.

Rotation

This item applies when MeshType = 5. MeshType = 5 provides cookie cut meshing based on two perpendicular lines passing through point objects included in the group specified by the Group item. By default these lines align with the area object local 1 and 2 axes. The Rotation item is an angle in degrees that the meshing lines are rotated from their default orientation. [deg]

MaxSizeGeneral

This item applies when MeshType = 6. It is the maximum size of objects created by the General Divide Tool.

LocalAxesOnEdge

If this item is True, and if both points along an edge of the original area object have the same local axes, the program makes the local axes for added points along the edge the same as the edge end points.

LocalAxesOnFace

If this item is True, and if all points around the perimeter of the original area object have the same local axes, the program makes the local axes for all added points the same as the perimeter points.

RestraintsOnEdge

If this item is True, and if both points along an edge of the original area object have the same restraint/constraint, then, if the added point and the adjacent corner points have the same local axes definition, the program includes the restraint/constraint for added points along the edge.

RestraintsOnFace

If this item is True, and if all points around the perimeter of the original area object have the same restraint/constraint, then, if an added point and the perimeter points have the same local axes definition, the program includes the restraint/constraint for the added point.

Group

The name of a defined group. Some of the meshing options make use of point and line objects included in this group.

SubMesh

If this item is True, after initial meshing, the program further meshes any area objects that have an edge longer than the length specified by the SubMeshSize item.

SubMeshSize

This item applies when the SubMesh item is True. It is the maximum size of area objects to remain when the auto meshing is complete. [L]

## Remarks

This function retrieves the automatic meshing assignments to area objects.

The function returns zero if the meshing assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjAutoMesh()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MeshType As Long
      Dim n1 As Long
      Dim n2 As Long
      Dim MaxSize1 As Double
      Dim MaxSize2 As Double
      Dim PointOnEdgeFromLine As Boolean
      Dim PointOnEdgeFromPoint As Boolean
      Dim ExtendCookieCutLines As Boolean
      Dim Rotation As Double
      Dim MaxSizeGeneral As Double
      Dim LocalAxesOnEdge As Boolean
      Dim LocalAxesOnFace As Boolean
      Dim RestraintsOnEdge As Boolean
      Dim RestraintsOnFace As Boolean
      Dim MyGroup As String
      Dim SubMesh As Boolean
      Dim SubMeshSize As Double

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

   'assign auto mesh options
      ret = SapModel.AreaObj.SetAutoMesh("ALL", 1, 3, 3, , , , , , , , , , , , , True, , Group)

   'get auto mesh options for area object
      ret = SapModel.AreaObj.GetAutoMesh("1", MeshType, n1, n2, MaxSize1, MaxSize2, PointOnEdgeFromLine, PointOnEdgeFromPoint, ExtendCookieCutLines, Rotation, MaxSizeGeneral, LocalAxesOnEdge, LocalAxesOnFace, RestraintsOnEdge, RestraintsOnFace, MyGroup, SubMesh, SubMeshSize)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

This function is obsolete and was superseded by [GetAutoMesh\_1](../Object_Model/Area_Object/GetAutoMesh_1_{Area_Object}.htm) in release v27.0.0. This function is maintained for backwards compatibility.

## See Also

[SetAutoMesh](SetAutoMesh_{Area_Object}.htm)



## GetChannel {Frame}_old

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetChannel_{Frame}_old.htm`*

# GetChannel (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropFrame.GetChannel

## VB6 Procedure

Function GetChannel(ByVal Name As String, ByRef FileName
As String, ByRef MatProp As String, ByRef t3 As Double, ByRef t2 As Double,
ByRef tf As Double, ByRef tw As Double, ByRef Color As Long, ByRef Notes
As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing frame section property.

FileName

If the section property was imported from a property
file, this is the name of that file. If the section property was not imported,
this item is blank.

MatProp

The name of the material property for the section.

t3

The section depth. [L]

t2

The flange width. [L]

tf

The flange thickness. [L]

tw

The web thickness. [L]

Color

The display color assigned to the section.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section.

## Remarks

This function retrieves frame section property data
for a channel-type frame section.

The function returns zero if the section property data
is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePropChannel()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim FileName As String
      Dim MatProp As String
      Dim t3 As Double
      Dim t2 As Double
      Dim tf As Double
      Dim tw As Double
      Dim Color As Long
      Dim Notes As String
      Dim GUID As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetChannel("CHN1",
"A992Fy50", 24, 6, 0.5, 0.3)

   'get frame section property data
      ret = SapModel.PropFrame.GetChannel("CHN1",
FileName, MatProp, t3, t2, tf, tw, Color, Notes, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[SetChannel](../Definitions/Properties/Frame/SetChannel_{Frame}.htm)



## GetChinese2002_1{Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetChinese2002_1{Wind_Load}.htm`*

# GetChinese2002\_1

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.GetChinese2002\_1

## VB6 Procedure

Function GetChinese2002\_1(ByVal Name As String, ByRef ExposureFrom As Long, ByRef DirAngle As Double, ByRef BuildingWidth As Double, ByRef Us As Double, ByRef UniformTaper As Boolean, ByRef BHoverB0 As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef wzero As Double, ByRef Rt As Long, ByRef PhiZOpt As Long, ByRef T1Opt As Long, ByRef UserT As Double, ByRef DampRatio As Double, ByRef UserExposure As Boolean) As Long

## Parameters

Name

The name of an existing Wind-type load pattern with an Chinese 2002 auto wind assignment.

ExposureFrom

This is 1 or 2 indicating the source of the wind exposure.

1 = From extents of rigid diaphragms

2 = From area objects

DirAngle

The direction angle for the wind load. This item applies only when ExposureFrom = 1.

BuildingWidth

The building width. [L]

Us

The shape coefficient. This item applies only when ExposureFrom = 1.

UniformTaper

This item is True if a correction is to be applied to the wind load for a uniform taper.

BHoverB0

The taper ratio, Bh/B0. This item applies only when UniformTaper = True.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

wzero

The basic wind pressure in kN/m2.

Rt

This is 1, 2, 3 or 4, indicating the ground roughness.

1 = A

2 = B

3 = C

4 = D

PhiZOpt

This is 0 or 1, indicating the Phi Z source.

0 = Modal analysis

1 = Z/H ratio

T1Opt

This is 0 or 1, indicating the T1 source.

0 = Modal analysis

1 = User defined

UserT

This item only applies when the T1 source is user defined (T1Opt = 1). It is the user defined T1 period. [s]

DampRatio

The damping ratio.

UserExposure

If this item is True, the wind exposure widths are provided by the user. If it is False, the wind exposure widths are calculated by the program from the extents of the diaphragms.

## Remarks

This function retrieves auto wind loading parameters for Chinese 2002.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub GetWindChinese2002\_1()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ExposureFrom As Long
      Dim DirAngle As Double
      Dim BuildingWidth As Double
      Dim Us As Double
      Dim UniformTaper As Boolean
      Dim BHoverB0 As Double
      Dim UserZ As Boolean
      Dim TopZ As Double
      Dim BottomZ As Double
      Dim wzero As Double
      Dim Rt As Long
      Dim PhiZOpt As Long
      Dim T1Opt As Long
      Dim UserT As Double
      Dim DampRatio As Double
      Dim UserExposure As Boolean

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WIND)

   'assign Chinese2002\_1 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetChinese2002\_1("WIND", 1, 0, 1200, 0.5, False, 1, False, 0, 0, 0.48, 3, 1, 1, 0.6, 0.04)

   'get Chinese2002\_1 parameters
      ret = SapModel.LoadPatterns.AutoWind.GetChinese2002\_1("WIND", ExposureFrom, DirAngle, BuildingWidth, Us, UniformTaper, BHoverB0, UserZ, TopZ, BottomZ, wzero, Rt, PhiZOpt, T1Opt, UserT, DampRatio, UserExposure)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.1.0.

This function supersedes [GetChinese2002 {Wind Load}](GetChinese2002_{Wind_Load}.htm)

## See Also

[SetChinese2002\_1](SetChinese2002_1{Wind_Load}.htm)



## GetChinese2002 {Auto Seismic}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetChinese2002_{Auto_Seismic}.htm`*

# GetChinese2002

## Syntax

SapObject.SapModel.LoadPatterns.AutoSeismic.GetChinese2002

## VB6 Procedure

Function GetChinese2002(ByVal Name As String, ByRef DirFlag As Long, ByRef Eccen As Double, ByRef PeriodFlag As Long, ByRef UserT As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef JGJ32002AlphaMax As Double, ByRef JGJ32002SI As Long, ByRef JGJ32002DampRatio As Double, ByRef JGJ32002Tg As Double, ByRef JGJ32002PTDF As Double, ByRef EnhancementFactor As Double) As Long

## Parameters

Name

The name of an existing Quake-type load pattern with a Chinese 2002 auto seismic load assignment.

DirFlag

This is 1, 2 or 3, indicating the seismic load direction.

1 = Global X

2 = Global Y

3 = Global Z

Eccen

The eccentricity ratio that applies to all diaphragms.

PeriodFlag

This is either 2 or 3, indicating the time period option.

2 = Program calculated

3 = User defined

UserT

The user specified time period. This item applies when the PeriodFlag item is 3. [s]

UserZ

This item is True if the top and bottom elevations of the seismic load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto seismic loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto seismic loads are applied. [L]

JGJ32002AlphaMax

The maximum influence factor.

JGJ32002SI

This is 1, 2, 3, 4, 5 or 6, indicating the seismic intensity.

1 = 6  (0.05g)

2 = 7  (0.10g)

3 = 7  (0.15g)

4 = 8  (0.20g)

5 = 8  (0.30g)

6 = 9  (0.40g)

JGJ32002DampRatio

The damping ratio.

JGJ32002Tg

The characteristic ground period. [s]

JGJ32002PTDF

The period time discount factor.

EnhancementFactor

The enhancement factor.

## Remarks

This function retrieves auto seismic loading parameters for the Chinese 2002 code.

The function returns zero if the parameters are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSeismicParametersChinese2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DirFlag As Long
      Dim Eccen As Double
      Dim PeriodFlag As Long
      Dim UserT As Double
      Dim UserZ As Boolean
      Dim TopZ As Double
      Dim BottomZ As Double
      Dim JGJ32002AlphaMax As Double
      Dim JGJ32002SI As Long
      Dim JGJ32002DampRatio As Double
      Dim JGJ32002Tg As Double
      Dim JGJ32002PTDF As Double
      Dim EnhancementFactor As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("EQX", LTYPE\_QUAKE)

   'assign Chinese 2002 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetChinese2002("EQX", 1, 0.05, 2, 0, False, 0, 0, 0.16, 4, 0.06, 0.4, 1, 1)

   'get Chinese 2002 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.GetChinese2002("EQX", DirFlag, Eccen, PeriodFlag, UserT, UserZ, TopZ, BottomZ, JGJ32002AlphaMax, JGJ32002SI, JGJ32002DampRatio, JGJ32002Tg, JGJ32002PTDF, EnhancementFactor)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.01.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetChinese2002](SetChinese2002_{Auto_Seismic}.htm)



## GetChinese2002 {RS}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetChinese2002_{RS}.htm`*

# GetChinese2002

## Syntax

SapObject.SapModel.Func.FuncRS.GetChinese2002

## VB6 Procedure

Function GetChinese2002(ByVal Name As String, ByRef JGJ32002AlphaMax As Double, ByRef JGJ32002SI As Long, ByRef JGJ32002Tg As Double, ByRef JGJ32002PTDF As Double, ByRef DampRatio As Double) As Long

## Parameters

Name

The name of a Chinese 2002 response spectrum function.

JGJ32002AlphaMax

The maximum influence factor.

JGJ32002SI

This is 1, 2, 3, 4, 5 or 6, indicating the seismic intensity.

1 = 6 (0.05g)

2 = 7 (0.10g)

3 = 7 (0.15g)

4 = 8 (0.20g)

5 = 8 (0.30g)

6 = 9 (0.40g)

JGJ32002Tg

The characteristic ground period, Tg > 0.1. [s]

JGJ32002PTDF

The period time discount factor.

DampRatio

The damping ratio for the function, 0 <= DampRatio < 1.

## Remarks

This function retrieves the definition of a Chinese 2002 response spectrum function.

The function returns zero if the function definition is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetRSFuncChinese2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim JGJ32002AlphaMax As Double
      Dim JGJ32002SI As Long
      Dim JGJ32002Tg As Double
      Dim JGJ32002PTDF As Double
      Dim DampRatio As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add Chinese2002 RS function
      ret = SapModel.Func.FuncRS.SetChinese2002("RS-1", 0.18, 5, 0.36, 1, 0.04)

   'get Chinese2002 RS function
      ret = SapModel.Func.FuncRS.GetChinese2002("RS-1", JGJ32002AlphaMax, JGJ32002SI, JGJ32002Tg, JGJ32002PTDF, DampRatio)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[SetChinese2002](SetChinese2002_{RS}.htm)



## GetChinese2002 {Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetChinese2002_{Wind_Load}.htm`*

# GetChinese2002 (Note:  Newer function available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.GetChinese2002

## VB6 Procedure

Function GetChinese2002(ByVal Name As String, ByRef ExposureFrom As Long, ByRef DirAngle As Double, ByRef BuildingWidth As Double, ByRef Us As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef wzero As Double, ByRef Rt As Long, ByRef PhiZOpt As Long, ByRef T1Opt As Long, ByRef UserT As Double, ByRef DampRatio As Double, ByRef UserExposure As Boolean) As Long

## Parameters

Name

The name of an existing Wind-type load pattern with an Chinese 2002 auto wind assignment.

ExposureFrom

This is either 1 or 2, indicating the source of the wind exposure.

1 = From extents of rigid diaphragms

2 = From area objects

DirAngle

The direction angle for the wind load. This item applies only when ExposureFrom = 1.

BuildingWidth

The building width. [L]

Us

The shape coefficient. This item applies only when ExposureFrom = 1.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

wzero

The basic wind pressure in kN/m2.

Rt

This is 1, 2, 3 or 4, indicating the ground roughness.

1 = A

2 = B

3 = C

4 = D

PhiZOpt

This is either 0 or 1, indicating the Phi Z source.

0 = Modal analysis

1 = Z/H ratio

T1Opt

This is either 0 or 1, indicating the T1 source.

0 = Modal analysis

1 = User defined

UserT

This item applies only when the T1 source is user defined (T1Opt = 1). It is the user defined T1 period. [s]

DampRatio

The damping ratio.

UserExposure

If this item is True, the wind exposure widths are provided by the user. If it is False, the wind exposure widths are calculated by the program from the extents of the diaphragms.

## Remarks

This function retrieves auto wind loading parameters for Chinese 2002.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub GetWindChinese2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ExposureFrom As Long
      Dim DirAngle As Double
      Dim BuildingWidth As Double
      Dim Us As Double
      Dim UserZ As Boolean
      Dim TopZ As Double
      Dim BottomZ As Double
      Dim wzero As Double
      Dim Rt As Long
      Dim PhiZOpt As Long
      Dim T1Opt As Long
      Dim UserT As Double
      Dim DampRatio As Double
      Dim UserExposure As Boolean

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WIND)

   'assign Chinese2002 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetChinese2002("WIND", 1, 0, 1200, 0.5, False, 0, 0, 0.48, 3, 1, 1, 0.6, 0.04)

   'get Chinese2002 parameters
      ret = SapModel.LoadPatterns.AutoWind.GetChinese2002("WIND", ExposureFrom, DirAngle, BuildingWidth, Us, UserZ, TopZ, BottomZ, wzero, Rt, PhiZOpt, T1Opt, UserT, DampRatio, UserExposure)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.01.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

The function is obsolete and has been superseded by [GetChinese2002\_1](GetChinese2002_1{Wind_Load}.htm) as of version 14.1.0. This function is maintained for backward compatibility. New function added.

## See Also

[SetChinese2002](SetChinese2002_{Wind_Load}.htm)



## GetCurved

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetCurved.htm`*

# GetCurved

## Syntax

SapObject.SapModel.FrameObj.GetCurved

## VB6 Procedure

Function GetCurved(ByRef NumberItems As Long, ByRef MyType() As Long, ByRef gx() As Double, ByRef gy() As Double, ByRef gz() As Double, ByRef PointName() As String, ByRef Radius() As Double, ByRef NumSegs() As Long) As Long

## Parameters

NumberItems

The number of curved frame objects returned.

MyType

This is an array that includes a numeric value indicating the curved frame type. The type is 1, 2, 3, 4, or 5.

1 = Circular Arc Specified by a Third Point Name

2 = Circular Arc Specified by Third Point Coordinates

3 = Circular Arc Specified by Planar Point Coordinates and Radius

4 = Parabolic Arc Specified by a Third Point Name

5 = Parabolic Arc Specified by Third Point Coordinates

MyTypes 1, 2, 4, and 5 all define the curve by three points. The three points are the two end point of the frame object and a third point defined by naming an existing point object or specifying point coordinates.

MyType 3 defines a circular curved frame by it end points, the coordinates of another point that lies in the plane of the curve but not necessarily on the curved frame, and a curve radius.

gx, gy, gz

These are arrays that include the point coordinates in the global coordinate system. [L]

For MyType 1 and 4 these items do not apply.

For MyType 2 and 5 these are the coordinates of the third point on the curved frame.

For MyType 3 these are the coordinates of the planar point that lies in the plane of the curved frame.

PointName

This is an array that includes the name of the point object that is the third point on the curved frame. This item applies for MyType 1 and 4. It does not apply for MyType 2, 3 and 5.

Radius

This is an array of the radii of the circular curved frame. This item only applies for MyType 3. [L]

NumSegs

This is an array that includes the number of segments into which the program internally divides the curved frame.

## Remarks

This function retrieves definition data for all curved frame objects and returns the data in arrays.

The function returns zero if the curved frame object data is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCurvedFrames()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim MyType() As Long
      Dim gx() As Double
      Dim gy() As Double
      Dim gz() As Double
      Dim PointName() As String
      Dim Radius() As Double
      Dim NumSegs() As Long

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

   'set frames curved
      ret = SapModel.FrameObj.SetCurved("13", 1, 0, 0, 0, "1", 0, 16)
      ret = SapModel.FrameObj.SetCurved("14", 2, -200, 0, 176, "", 0, 16)
      ret = SapModel.FrameObj.SetCurved("15", 3, 0, 0, 0, "", 100, 16)
      ret = SapModel.FrameObj.SetCurved("16", 4, 0, 0, 0, "3", 0, 16)
      ret = SapModel.FrameObj.SetCurved("17", 5, 0, 0, 176, "", 0, 16)

   'get curved frame data
      ret = SapModel.FrameObj.GetCurved(NumberItems, MyType, gx, gy, gz, PointName, Radius, NumSegs)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetStraight](../Object_Model/Frame_Object/SetStraight.htm)

[SetCurved](../Object_Model/Frame_Object/SetCurved.htm)

[GetType](../Object_Model/Frame_Object/GetType_{Frame_Object}.htm)



## GetDblAngle

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetDblAngle_old.htm`*

# GetDblAngle (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropFrame.GetDblAngle

## VB6 Procedure

Function GetDblAngle(ByVal Name As String, ByRef FileName
As String, ByRef MatProp As String, ByRef t3 As Double, ByRef t2 As Double,
ByRef tf As Double, ByRef tw As Double, ByRef dis As Double, ByRef Color
As Long, ByRef Notes As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing frame section property.

FileName

If the section property was imported from a property
file, this is the name of that file. If the section property was not imported,
this item is blank.

MatProp

The name of the material property for the section.

t3

The vertical leg depth. [L]

t2

The total width of the section, that is, the sum of
the widths of each horizontal leg plus the back-to-back distance. [L]

tf

The horizontal leg thickness. [L]

tw

The vertical leg thickness. [L]

dis

The back-to-back distance between the angles. [L]

Color

The display color assigned to the section.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section.

## Remarks

This function retrieves frame section property data
for a double angle-type frame section.

The function returns zero if the section property data
is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePropDblAngle()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim FileName As String
      Dim MatProp As String
      Dim t3 As Double
      Dim t2 As Double
      Dim tf As Double
      Dim tw As Double
      Dim dis As Double
      Dim Color As Long
      Dim Notes As String
      Dim GUID As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetDblAngle("DBANG1",
"A992Fy50", 6, 9, 0.5, 0.5, 1)

   'get frame section property data
      ret = SapModel.PropFrame.GetDblAngle("DBANG1",
FileName, MatProp, t3, t2, tf, tw, dis, Color, Notes, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[SetDblAngle](../Definitions/Properties/Frame/SetDblAngle_{Frame}.htm)



## GetDblChannel

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetDblChannel_old.htm`*

# GetDblChannel (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropFrame.GetDblChannel

## VB6 Procedure

Function GetDblChannel(ByVal Name As String, ByRef FileName
As String, ByRef MatProp As String, ByRef t3 As Double, ByRef t2 As Double,
ByRef tf As Double, ByRef tw As Double, ByRef dis As Double, ByRef Color
As Long, ByRef Notes As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing frame section property.

FileName

If the section property was imported from a property
file, this is the name of that file. If the section property was not imported,
this item is blank.

MatProp

The name of the material property for the section.

t3

The section depth. [L]

t2

The total width of the section, that is, the sum of
the widths of each flange plus the back-to-back distance. [L]

tf

The flange thickness. [L]

tw

The web thickness. [L]

dis

The back-to-back distance between the channels. [L]

Color

The display color assigned to the section.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section.

## Remarks

This function retrieves frame section property data
for a double channel-type frame section.

The function returns zero if the section property data
is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePropDblChannel()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim FileName As String
      Dim MatProp As String
      Dim t3 As Double
      Dim t2 As Double
      Dim tf As Double
      Dim tw As Double
      Dim dis As Double
      Dim Color As Long
      Dim Notes As String
      Dim GUID As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetDblChannel("DBCHN1",
"A992Fy50", 12, 6.5, 0.5, 0.3, 0.5)

   'get frame section property data
      ret = SapModel.PropFrame.GetDblChannel("DBCHN1",
FileName, MatProp, t3, t2, tf, tw, dis, Color, Notes, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[SetDblChannel](../Definitions/Properties/Frame/SetDblChannel.htm)



## GetEurocode12005 {Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetEurocode12005_{Wind_Load}.htm`*

# GetEurocode12005 (Note:  Newer function available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.GetEurocode12005

## VB6 Procedure

Function GetEurocode12005(ByVal Name As String, ByRef ExposureFrom As Long, ByRef DirAngle As Double, ByRef Cpw As Double, ByRef Cpl As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef WindSpeed As Double, ByRef Terrain As Long, ByRef Orography As Double, ByRef k1 As Double, ByRef CsCd As Double, ByRef UserExposure As Boolean) As Long

## Parameters

Name

The name of an existing Wind-type load pattern with a Eurocode 1 2005 auto wind assignment.

ExposureFrom

This is 1 or 2, indicating the source of the wind exposure.

1 = From extents of rigid diaphragms

2 = From area objects

DirAngle

The direction angle for the wind load. This item applies only when ExposureFrom = 1.

Cpw

The windward coefficient, Cp. This item applies only when ExposureFrom = 1.

Cpl

The leeward coefficient, Cp. This item applies only when ExposureFrom = 1.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

WindSpeed

The basic wind speed, vb, in meters per second.

Terrain

This is 0, 1, 2, 3 or 4, indicating the terrain category.

0 = 0

1 = I

2 = II

3 = III

4 = IV

Orography

The orography factor, Co.

k1

The turbulence factor, k1.

CsCd

The structural factor, CsCd.

UserExposure

If this item is True, the wind exposure widths are provided by the user. If it is False, the wind exposure widths are calculated by the program from the extents of the diaphragms.

## Remarks

This function retrieves auto wind loading parameters for Eurocode 1 2005.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub GetWindEurocode12005()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ExposureFrom As Long
      Dim DirAngle As Double
      Dim Cpw As Double
      Dim Cpl As Double
      Dim UserZ As Boolean
      Dim TopZ As Double
      Dim BottomZ As Double
      Dim WindSpeed As Double
      Dim Terrain As Long
      Dim Orography As Double
      Dim k1 As Double
      Dim CsCd As Double
      Dim UserExposure As Boolean

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WIND)

   'assign Eurocode 1 2005 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetEurocode12005("WIND", 1, 0, 0.8, 0.5, False, 0, 0, 35, 2, 1, 1, 1)

   'get Eurocode 1 2005 parameters
      ret = SapModel.LoadPatterns.AutoWind.GetEurocode12005("WIND", ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, WindSpeed, Terrain, Orography, k1, CsCd, UserExposure)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

The function is obsolete and has been superseded by  [GetEurocode12005\_1](../Definitions/Load_Pattern/Auto_Wind_Load/GetEurocode12005_1{Wind_Load}.htm) as of version 14.1.0. This function is maintained for backward compatibility. New function added.

## See Also

[SetEurocode12005](SetEurocode12005_{Wind_Load}.htm)



## GetEurocode82004 (Auto Seismic)

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetEurocode82004_(Auto_Seismic).htm`*

# GetEurocode82004  (Note:  Newer function available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoSeismic.GetEurocode82004

## VB6 Procedure

Function GetEurocode82004(ByVal Name As String, ByRef DirFlag As Long, ByRef Eccen As Double, ByRef PeriodFlag As Long, ByRef CT As Double, ByRef UserT As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef EURO2004GroundType As Long, ByRef EURO2004SpectrumType As Long, ByRef EURO2004ag As Double, ByRef EURO2004Beta As Double, ByRef EURO2004q As Double, ByRef EURO2004Lambda As Double) As Long

## Parameters

Name

The name of an existing Quake-type load pattern with a Eurocode 8 2004 auto seismic load assignment.

DirFlag

This is 1 or 2, indicating the seismic load direction.

1 = Global X

2 = Global Y

Eccen

The eccentricity ratio that applies to all diaphragms.

PeriodFlag

This is 1, 2 or 3, indicating the time period option.

1 = Approximate

2 = Program calculated

3 = User defined

CT

The code-specified Ct factor. This item applies when the PeriodFlag item is 1.

UserT

The user specified time period. This item applies when the PeriodFlag item is 3. [s]

UserZ

This item is True if the top and bottom elevations of the seismic load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto seismic loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto seismic loads are applied. [L]

EURO2004GroundType

This is 1, 2, 3, 4 or 5, indicating the ground type.

1 = A

2 = B

3 = C

4 = D

5 = E

EURO2004SpectrumType

This is 1 or 2, indicating the spectrum type.

1 = Type 1

2 = Type 2

EURO2004ag

The design ground acceleration in g, ag.

EURO2004Beta

The lower bound factor, Beta.

EURO2004q

The behavior factor, q.

EURO2004Lambda

The correction factor, Lambda.

## Remarks

This function retrieves auto seismic loading parameters for the Eurocode 8 2004 code.

The function returns zero if the parameters are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSeismicParametersEurocode82004()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DirFlag As Long
      Dim Eccen As Double
      Dim PeriodFlag As Long
      Dim CT As Double
      Dim UserT As Double
      Dim UserZ As Boolean
      Dim TopZ As Double
      Dim BottomZ As Double
      Dim EURO2004GroundType As Long
      Dim EURO2004SpectrumType As Long
      Dim EURO2004ag As Double
      Dim EURO2004Beta As Double
      Dim EURO2004q As Double
      Dim EURO2004Lambda As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("EQX", LTYPE\_QUAKE)

   'assign Eurocode 8 2004 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetEurocode82004("EQX", 2, 0.1, 2, 0.075, 0, False, 0, 0, 2, 1, 0.4, 0.2, 2, 1)

   'get Eurocode 8 2004 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.GetEurocode82004("EQX", DirFlag, Eccen, PeriodFlag, CT, UserT, UserZ, TopZ, BottomZ, EURO2004GroundType, EURO2004SpectrumType, EURO2004ag, EURO2004Beta, EURO2004q, EURO2004Lambda)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

The function is obsolete and has been superseded by [GetEurocode82004\_1](../Definitions/Load_Pattern/Auto_Seismic_Load/GetEurocode82004_1_{Auto_Seismic}.htm) as of version 14.1.0. This function is maintained for backward compatibility. New function added.

## See Also

[SetEurocode82004](SetEurocode82004_(Auto_Seismic).htm)



## GetEurocode82004 (RS)

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetEurocode82004_(RS).htm`*

# GetEurocode82004  (Note:  Newer function available)

## Syntax

SapObject.SapModel.Func.FuncRS.GetEurocode82004

## VB6 Procedure

Function GetEurocode82004(ByVal Name As String, ByRef EURO2004GroundType As Long, ByRef EURO2004SpectrumType As Long, ByRef EURO2004ag As Double, ByRef EURO2004Beta As Double, ByRef EURO2004q As Double, ByRef DampRatio As Double) As Long

## Parameters

Name

The name of a Eurocode 8 2004 response spectrum function.

EURO2004GroundType

This is 1, 2, 3, 4 or 5, indicating the ground type.

1 = A

2 = B

3 = C

4 = D

5 = E

EURO2004SpectrumType

This is 1 or 2, indicating the spectrum type.

1 = Type 1

2 = Type 2

EURO2004ag

The design ground acceleration in g, ag.

EURO2004Beta

The lower bound factor, Beta.

EURO2004q

The behavior factor, q.

DampRatio

The damping ratio for the function, 0 <= DampRatio < 1.

## Remarks

This function retrieves the definition of a Eurocode 8 2004 response spectrum function.

The function returns zero if the function definition is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetRSFuncEurocode82004()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim EURO2004GroundType As Long
      Dim EURO2004SpectrumType As Long
      Dim EURO2004ag As Double
      Dim EURO2004Beta As Double
      Dim EURO2004q As Double
      Dim DampRatio As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add Eurocode 8 2004 RS function
      ret = SapModel.Func.FuncRS.SetEurocode82004("RS-1", 2, 1, 0.4, 0.2, 2, 0.04)

   'get Eurocode 8 2004 RS function
      ret = SapModel.Func.FuncRS.GetEurocode82004("RS-1", EURO2004GroundType, EURO2004SpectrumType, EURO2004ag, EURO2004Beta, EURO2004q, DampRatio)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
   End Sub

## Release Notes

Initial release in version 14.00.

The function is obsolete and has been superseded by [GetEurocode82004\_1](../Definitions/Functions/Response_Spectrum/GetEurocode82004_1_{RS}.htm) as of version 14.1.0. This function is maintained for backward compatibility. New function added.

## See Also

[SetEurocode82004](SetEurocode82004_{RS}.htm)



## GetExposure

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetExposure.htm`*

# GetExposure

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.GetExposure

## VB6 Procedure

Function GetExposure(ByVal Name As String, ByRef Num As Long, ByRef Diaph() As String, ByRef x() As Double, ByRef y() As Double, ByRef MyWidth() As Double, ByRef Height() As Double) As Long

## Parameters

Name

The name of an existing Wind-type load pattern that has an auto wind load assigned.

Num

The number of diaphragms at which exposure data is reported.

Diaph

This is an array that includes the names of the diaphragms that have eccentricity overrides.

x

This is an array that includes the global X-coordinate of the point where the wind force load is applied to the diaphragm. [L]

y

This is an array that includes the global Y-coordinate of the point where the wind force load is applied to the diaphragm. [L]

MyWidth

This is an array that includes the exposure width for the wind load applied to the specified diaphragm. [L]

Height

This is an array that includes the exposure height for the wind load applied to the specified diaphragm. [L]

## Remarks

This function retrieves exposure parameters for auto wind loads determined from extents of rigid diaphragms. This function does not apply for User-type auto wind loads.

The function returns zero if the parameters are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetWindExposure()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Num As Long
      Dim Diaph() As String
      Dim x() As Double
      Dim y() As Double
      Dim MyWidth() As Double
      Dim Height() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
         SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WIND)

   'assign ASCE788 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetASCE788("WIND", 1, 0, 0.8, 0.5, False, 0, 0, 80, 3, 1, 0.85, True)

   'assign user exposure data
      ret = SapModel.LoadPatterns.AutoWind.SetExposure("WIND", "Diaph2", 0, 0, 900, 125)

   'get exposure data
      ret = SapModel.LoadPatterns.AutoWind.GetExposure("WIND", Num, Diaph, x, y, MyWidth, Height)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.01.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetExposure](SetExposure.htm)

[GetSpecialRigidDiaphragmList](../Definitions/Constraints/GetSpecialRigidDiaphragmList.htm)



## GetFireproofing

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetFireproofing.htm`*

# GetFireproofing

## Syntax

SapObject.SapModel.FrameObj.GetFireproofing

## VB6 Procedure

Function GetFireproofing(ByVal Name As String, ByRef MyType As Long, ByRef Thickness As Double, ByRef Perimeter As Double, ByRef Density As Double, ByRef tf As Boolean) As Long

## Parameters

Name

The name of an existing frame object.

MyType

This is 1, 2 or 3, indicating the type of fireproofing assigned.

1 = Sprayed on - program calculate section perimeter

2 = Sprayed on - user provides section perimeter

3 = Concrete encased

Thickness

When MyType = 1 or MyType = 2 this is the thickness of the sprayed on fireproofing. When MyType = 3 this is the concrete cover dimension. [L]

Perimeter

This item applies only when MyType = 2. It is the length of fireproofing applied measured around the perimeter of the frame object cross-section. [L]

Density

This is the weight per unit volume of the fireproofing material. [F/L3]

tf

This item  applies only when MyType = 1 or MyType = 3. If this item is True, the fireproofing is assumed to be applied to the top flange of the section. If it is False, the program assumes no fireproofing is applied to the section top flange. This flag applies for I, channel and double channel sections.

## Remarks

This function retrieves the fireproofing assignments to frame objects.

The function returns zero if the fireproofing assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFireproofing()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyType As Long
      Dim Thickness As Double
      Dim Perimeter As Double
      Dim Density As Double
      Dim tf As Boolean

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

   'assign fireproofing
      ret = SapModel.FrameObj.SetFireproofing("ALL", 1, 2, 0, 8.68E-06, False, Group)

   'get fireproofing
      ret = SapModel.FrameObj.GetFireproofing("3", MyType, Thickness, Perimeter, Density, tf)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetFireproofing](SetFireproofing.htm)

[DeleteFireproofing](../Object_Model/Frame_Object/DeleteFireproofing.htm)



## GetFromFile {Time History}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetFromFile_{Time_History}.htm`*

# GetFromFile (Note:  Newer function available)

## Syntax

SapObject.SapModel.Func.FuncTH.GetFromFile

## VB6 Procedure

Function GetFromFile(ByVal Name As String, ByRef FileName As String, ByRef HeadLines As Long, ByRef PreChars As Long, ByRef PointsPerLine As Long, ByRef ValueType As Long, ByRef FreeFormat As Boolean, ByRef NumberFixed As Long) As Long

## Parameters

Name

The name of a defined time history function specified to be from a text file.

FileName

The full path of the text file containing the function data.

HeadLines

The number of header lines in the text file to be skipped before starting to read function data.

PreChars

The number of prefix characters to be skipped on each line in the text file.

PointsPerLine

The number of function points included on each text file line.

ValueType

This is either 1 or 2, indicating value type.

1 = Values at equal time intervals

2 = Time and function values

FreeFormat

This item is True if the data is provided in a free format. It is False if it is in a fixed format.

NumberFixed

This item applies only when the FreeFormat item is False. It is the number of characters per item.

## Remarks

This function retrieves the definition of a time history function from file.

The function returns zero if the function definition is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetTHFuncFromFile()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim FileName As String
      Dim HeadLines As Long
      Dim PreChars As Long
      Dim PointsPerLine As Long
      Dim ValueType As Long
      Dim FreeFormat As Boolean
      Dim NumberFixed As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add TH function from file
      ret = SapModel.Func.FuncTH.SetFromFile("TH-1", "C:\SapAPI\FuncTH.txt", 3, 0, 3, 2, True)

   'get TH function from file
      ret = SapModel.Func.FuncTH.GetFromFile("TH-1", FileName, HeadLines, PreChars, PointsPerLine, ValueType, FreeFormat, NumberFixed)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Text File

Following is the contents of the text file name FuncTH.txt used in the VBA Example.

Time History Function

Time (sec) and Acceleration (g) values

3 points per line

   0.00000    .01080    .04200    .00100    .09700    .01590
    .16100   -.00010    .22100    .01890    .26300    .00010
    .29100    .00590    .33200   -.00120    .37400    .02000
    .42900   -.02370    .47100    .00760    .58100    .04250
    .62300    .00940    .66500    .01380    .72000   -.00880
    .72010   -.02560    .78900   -.03870    .78910   -.05680
    .87200   -.02320    .87210   -.03430    .94100   -.04020
    .94110   -.06030    .99700   -.07890   1.06600   -.06660
   1.06610   -.03810   1.09400   -.04290   1.16800    .08970
   1.31500   -.16960   1.38400   -.08280   1.41200   -.08280
   1.44000   -.09450   1.48100   -.08850   1.50900   -.10800
   1.53700   -.12800   1.62800    .11440   1.70300    .23550
   1.80000    .14280   1.85500    .17770   1.92400   -.26100
   2.00700   -.31940   2.21500    .29520   2.27000    .26340
   2.32000   -.29840   2.39500    .00540   2.45000    .28650
   2.51900   -.04690   2.57500    .15160   2.65200    .20770
   2.70800    .10870   2.76900   -.03250   2.89300    .10330
   2.97600   -.08030   3.06800    .05200   3.12900   -.15470
   3.21200    .00650   3.25300   -.20600   3.38600    .19270
   3.41900   -.09370   3.53000    .17080   3.59900   -.03590
   3.66800    .03650   3.73800   -.07360   3.83500    .03110
   3.90400   -.18330   4.01400    .02270   4.05600   -.04350
   4.10600    .02160   4.22200   -.19720   4.31400   -.17620
   4.41600    .14600   4.47100   -.00470   4.61800    .25720
   4.66500   -.20450   4.75600    .06080   4.83100   -.27330
   4.97000    .17790   5.03900    .03010   5.10800    .21830
   5.19900    .02670   5.23300    .12520   5.30200    .12900
   5.33000    .10890   5.34300   -.02390   5.45400    .17230
   5.51000   -.10210   5.60600    .01410   5.69000   -.19490
   5.77300   -.02420   5.80000   -.00500   5.80900   -.02750
   5.86900   -.05730   5.88300   -.03270   5.92500    .02160
   5.98000    .01080   6.01300    .02350   6.08500   -.06650
   6.13200    .00140   6.17400    .04930   6.18800    .01490
   6.18810   -.02000   6.22900   -.03810   6.27900    .02070
   6.32600   -.00580   6.36800   -.06030   6.38200   -.01620
   6.40900    .02000   6.45900   -.01760   6.47800   -.00330
   6.52000    .00430   6.53400   -.00400   6.56200   -.00990
   6.57500   -.00170   6.60300   -.01700   6.64500    .03730
   6.68600    .04570   6.71400    .03850   6.72800    .00090
   6.76900   -.02880   6.76910    .00160   6.81100    .01130
   6.85200    .00220   6.90800    .00920   6.99100   -.09960
   7.07400    .03600   7.12100    .00780   7.14300   -.02770
   7.14900    .00260   7.17100    .02720   7.22600    .05760
   7.29500   -.04920   7.37000    .02970   7.40600    .01090
   7.42500    .01860   7.46100   -.02530   7.52500   -.03470
   7.57200    .00360   7.60000   -.06280   7.64100   -.02800
   7.66900   -.01960   7.69100    .00680   7.75200   -.00540
   7.79400   -.06030   7.83500   -.03570   7.87700   -.07160
   7.96000   -.01400   7.98700   -.00560   8.00100    .02220
   8.07000    .04680   8.12600    .02600   8.12610   -.03350
   8.19500   -.01280   8.22300    .06610   8.27800    .03050
   8.33400    .02460   8.40300    .03470   8.45800   -.03690
   8.53300   -.03440   8.59600   -.01040   8.63800   -.02600
   8.73500    .15340   8.81800   -.00280   8.86000    .02330
   8.88200   -.02610   8.91500   -.00220   8.95600   -.18490
   9.05300    .12600   9.09500    .03200   9.12300    .09550
   9.15000    .12460   9.25300   -.03280   9.28900   -.04510
   9.42700    .13010   9.44100   -.16570   9.51000    .04190
   9.63500   -.09360   9.70400    .08160   9.81500   -.08810
   9.89800    .00640   9.93900   -.00060   9.99500    .05860
  10.02200   -.07130  10.05000   -.04480  10.05010   -.02210
  10.10500    .00930  10.10510    .00240  10.18800    .05100
  10.27200   -.12430  10.38200    .05870  10.42400    .01330
  10.45200    .03860  10.46500    .11640  10.50700   -.03740
  10.53400   -.05720  10.64500    .03080  10.70100    .02230
  10.71400    .05150  10.77000    .09030  10.83900   -.01940
  10.92200    .04710  10.92210   -.06770  10.96400   -.07940
  10.99100   -.01200  11.07400    .06080  11.08800   -.02690
  11.11600   -.04160  11.20700    .02930  11.20710    .05520
  11.22700    .07560  11.26800    .04310  11.32400    .02080
  11.43400    .11800  11.57300   -.09990  11.65600   -.12470
  11.72500   -.20940  11.72510   -.14180  11.78000   -.11630
  11.80800   0.00000  11.87700    .07620  11.91900    .05700
  11.98800    .13540  12.04300    .06730  12.11300    .08650

## Release Notes

Initial release in version 11.02.

The function is obsolete and has been superseded by [GetFromFile\_1](../definitions/functions/time_history/GetFromFile_1_{Time_History}.htm) as of version 14.12. This function is maintained for backward compatibility. New function added.

## See Also

[SetFromFile](SetFromFile_{Time_History}.htm)



## GetHingeAssigns_1

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetHingeAssigns_1.htm`*

# GetHingeAssigns\_1(Note:  Newer function available)

## Syntax

SapObject.SapModel.FrameObj.GetHingeAssigns\_1

## VB6 Procedure

Function GetHingeAssigns\_1(ByVal Name As String, ByRef
NumberHinges As Long, ByRef HingeNum() As Long, ByRef Prop() As String,
ByRef MyType() As Long, ByRef Behavior() As Long, ByRef Source() As String,
ByRef LocType() As eHingeLocationType, ByRef RD() As Double) As Long,
ByRef AD() As Double) As Long

## Parameters

Name

The name of an existing frame object.

NumberHinges

The number of hinge assignments on the specified frame
object.

HingeNum

An array that includes the hinge number for each hinge
on the frame object.

Prop

An array that includes the name of the generated hinge
property for each hinge on the frame object.

MyType

An array that specifies the type of hinge for each hinge
on the frame object. It is one of the following:

  1 = Axial
P

  2 = Shear
V2

  3 = Shear
V3

  4 = Torsion
T

  5 = Moment
M2

  6 = Moment
M3

  7 = Interacting
P-M2

  8 = Interacting
P-M3

  9 = Interacting
M2-M3

10 = Interacting P-M2-M3

11 = Fiber P-M2-M3

Behavior

An array that specifies the behavior of the hinge for
each hinge on the frame object. It is one of the following:

1 = Force controlled

2 = Deformation controlled

Source

An array that indicates the source of the generated
hinge property for each hinge on the frame object. The source is either
Auto or the name of a defined (not generated) hinge property.

LocType

This is a value from
the eHingeLocationType enumeration, specifying the type used to define
the location of the hinge:

RelativeDistance = 1

OffsetFromIEnd = 2

OffsetFromJEnd = 3

RD

If LocType = eHingeLocationType.RelativeDistance, this
is the distance of the hinge from the end of the i-end offset, as a ratio
to the clear length of the frame object.

AD

If LocType = eHingeLocationType.OffsetFromIEnd, this
is the absolute distance of the hinge from the end of the i-end offset.
 If LocType = eHingeLocationType.OffsetFromJEnd, this is the absolute
distance of the hinge from the end of the j-end offset.

## Remarks

This function reports the hinge assignments for a specified
frame object.

The function returns zero if the assignment data is
successfully obtained; otherwise it returns a nonzero value.

## VBA Example

This example assumes that a file MyHinge.sdb exists.

Sub GetFrameHingeAssigns()
   'dimension variables

      Dim SapObject as
cOAPI

      Dim SapModel As cSapModel

      Dim ret As Long

      Dim NumberHinges
As Long

      Dim HingeNum() As
Long

      Dim Prop() As String

      Dim MyType() As Long

      Dim Behavior() As
Long

      Dim Source() As String

 Dim LocType() As eHingeLocationType

      Dim RD() As Double

      Dim AD() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'open an existing file
      FileName = "C:\SapAPI\MyHinge.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'get hinge data for the frame object named 1
      ret = SapModel.FrameObj.GetHingeAssigns\_1("1",
NumberHinges, HingeNum, Prop, MyType, Behavior, Source, LocType, RD, AD)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.1.0

This function was superseded by [GetHingeAssigns\_2](../Object_Model/Frame_Object/GetHingeAssigns_2.htm)
in version 25.0.0.

## See Also



## GetISection {Frame}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetISection_{Frame}_old.htm`*

# GetISection (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropFrame.GetISection

## VB6 Procedure

Function GetISection(ByVal Name As String, ByRef FileName
As String, ByRef MatProp As String, ByRef t3 As Double, ByRef t2 As Double,
ByRef tf As Double, ByRef tw As Double, ByRef t2b As Double, ByRef tfb
As Double, ByRef Color As Long, ByRef Notes As String, ByRef GUID As String)
As Long

## Parameters

Name

The name of an existing I-type frame section property.

FileName

If the section property was imported from a property
file, this is the name of that file. If the section property was not imported,
this item is blank.

MatProp

The name of the material property for the section.

t3

The section depth. [L]

t2

The top flange width. [L]

tf

The top flange thickness. [L]

tw

The web thickness. [L]

t2b

The bottom flange width. [L]

tfb

The bottom flange thickness. [L]

Color

The display color assigned to the section.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section.

## Remarks

This function retrieves frame section property data
for an I-type frame section.

The function returns zero if the section property data
is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePropISection()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim FileName As String
      Dim MatProp As String
      Dim t3 As Double
      Dim t2 As Double
      Dim tf As Double
      Dim tw As Double
      Dim t2b As Double
      Dim tfb As Double
      Dim Color As Long
      Dim Notes As String
      Dim GUID As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'get frame section property data
      ret = SapModel.PropFrame.GetISection("FSEC1",
FileName, MatProp, t3, t2, tf, tw, t2b, tfb, Color, Notes, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[SetISection](../Definitions/Properties/Frame/SetISection_{Frame}.htm)



## GetInsertionPoint {Cable Object}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetInsertionPoint_{Cable_Object}.htm`*

# GetInsertionPoint

## Syntax

SapObject.SapModel.CableObj.GetInsertionPoint

## VB6 Procedure

Function GetInsertionPoint(ByVal Name As String, ByRef StiffTransform As Boolean, ByRef Offset1() As Double, ByRef Offset2() As Double, ByRef CSys As String) As Long

## Parameters

Name

The name of an existing cable object.

StiffTransform

If this item is True, the cable object stiffness is transformed for cardinal point and joint offsets from the cable section centroid.

Offset1

This is an array of three joint offset distances, in the coordinate directions specified by CSys, at the I-End of the cable object. [L]

Offset1(0) = Offset in the 1-axis or X-axis direction

Offset1(1) = Offset in the 2-axis or Y-axis direction

Offset1(2) = Offset in the 3-axis or Z-axis direction

Offset2

This is an array of three joint offset distances, in the coordinate directions specified by CSys, at the J-End of the cable object. [L]

Offset2(0) = Offset in the 1-axis or X-axis direction

Offset2(1) = Offset in the 2-axis or Y-axis direction

Offset2(2) = Offset in the 3-axis or Z-axis direction

CSys

This is Local or the name of a defined coordinate system. It is the coordinate system in which the Offset1 and Offset2 items are specified.

## Remarks

This function retrieves cable object insertion point assignments. The assignments include the end joint offsets.

The function returns zero if the insertion point data is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableInsertionPoint()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim StiffTransform As Boolean
      Dim Offset1() As Double
      Dim Offset2() As Double
      Dim CSys As String
      Dim Name As String

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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable insertion point
      ReDim Offset1(2)
      ReDim Offset2(2)
      For i = 0 To 2
         Offset1(i)=10 + i
         Offset2(i)=20 + i
      Next i
      ret = SapModel.CableObj.SetInsertionPoint(Name, True, Offset1, Offset2)

   'get cable insertion point
      ReDim Offset1(2)
      ReDim Offset2(2)
      ret = SapModel.CableObj.GetInsertionPoint(Name, StiffTransform, Offset1, Offset2, CSys)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

This function is obsolete as of v19.2.0 when cable insertion point assignments were removed from the program.

## See Also

[SetInsertionPoint](SetInsertionPoint_{Cable_Object}.htm)



## GetInsertionPoint {Frame Object}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetInsertionPoint_{Frame_Object}.htm`*

# GetInsertionPoint (Note:  Newer function available)

## Syntax

SapObject.SapModel.FrameObj.GetInsertionPoint

## VB6 Procedure

Function GetInsertionPoint(ByVal Name As String, ByRef
CardinalPoint As Long, ByRef Mirror2 As Boolean, ByRef StiffTransform
As Boolean, ByRef Offset1() As Double, ByRef Offset2() As Double, ByRef
CSys As String) As Long

## Parameters

Name

The name of an existing frame object.

CardinalPoint

This is a numeric value from 1 to 11 that specifies
the cardinal point for the frame object. The cardinal point specifies
the relative position of the frame section on the line representing the
frame object.

1 = bottom left

2 = bottom center

3 = bottom right

4 = middle left

5 = middle center

6 = middle right

7 = top left

8 = top center

9 = top right

10 = centroid

11
= shear center

Mirror2

If this item is True, the frame object section is assumed
to be mirrored (flipped) about its local 2-axis.

StiffTransform

If this item is True, the frame object stiffness is
transformed for cardinal point and joint offsets from the frame section
centroid.

Offset1

This is an array of three joint offset distances, in
the coordinate directions specified by CSys, at the I-End of the frame
object. [L]

Offset1(0) = Offset in
the 1-axis or X-axis direction

Offset1(1) = Offset in
the 2-axis or Y-axis direction

Offset1(2)
= Offset in the 3-axis or Z-axis direction

Offset2

This is an array of three joint offset distances, in
the coordinate directions specified by CSys, at the J-End of the frame
object. [L]

Offset2(0) = Offset in
the 1-axis or X-axis direction

Offset2(1) = Offset in
the 2-axis or Y-axis direction

Offset2(2) = Offset in the
3-axis or Z-axis direction

CSys

This is either Local or the name of a defined coordinate
system. It is the coordinate system in which the Offset1 and Offset2 items
are specified.

## Remarks

This function retrieves frame object insertion point
assignments. The assignments include the cardinal point and end joint
offsets.

The function returns zero if the insertion point data
is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameInsertionPoint()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim CardinalPoint As Long
      Dim Mirror2 As Boolean

      Dim StiffTransform
As Boolean
      Dim Offset1() As Double
      Dim Offset2() As Double
      Dim CSys As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
3, 124, 3, 200)

   'assign frame insertion point
      ReDim Offset1(2)
      ReDim Offset2(2)
      For i=0 To 2
         Offset1(i)=10 + i
         Offset2(i)=20 + i
      Next i
      ret = SapModel.FrameObj.SetInsertionPoint("15",
7, False, True, Offset1, Offset2)

   'get frame insertion point
      ReDim Offset1(2)
      ReDim Offset2(2)
      ret = SapModel.FrameObj.GetInsertionPoint("15",
CardinalPoint, Mirror2, StiffTransform, Offset1, Offset2, CSys)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

This function is obsolete and has been superseded by
[GetInsertionPoint\_1](../Object_Model/Frame_Object/GetInsertionPoint_1{Frame_Object}.htm)
as of version 24.1. This function is maintained for backwards compatibility.

## See Also

[SetInsertionPoint](SetInsertionPoint{Frame_Object}.htm)



## GetLoadWindPressure

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetLoadWindPressure.htm`*

# GetLoadWindPressure (Note: Newer function available)

## Syntax

SapObject.SapModel.AreaObj.GetLoadWindPressure

## VB6 Procedure

Function GetLoadWindPressure(ByVal Name As String, ByRef NumberItems As Long, ByRef AreaName() As String, ByRef LoadPat() As String, ByRef MyType() As Long, ByRef Cp() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

NumberItems

The total number of wind pressure loads retrieved for the specified area objects.

AreaName

This is an array that includes the name of the area object associated with each wind pressure load.

LoadPat

This is an array that includes the name of the load pattern associated with each wind pressure load.

MyType

This is an array that includes either 1 or 2, indicating the wind pressure type.

1 = Windward, pressure varies over height

2 = Other, pressure is constant over height

Cp

This is an array that includes the wind pressure coefficient value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the area object specified by the Name item.

If this item is Group, the assignments are retrieved for all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected area objects, and the Name item is ignored.

## Remarks

This function retrieves the wind pressure load assignments to area objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectWindPressureLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim AreaName() As String
      Dim LoadPat() As String
      Dim MyType() As Long
      Dim Cp() As Double

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

   'assign area object wind pressure load
      ret = SapModel.AreaObj.SetLoadWindPressure("ALL", "DEAD", 1, 0.8, Group)

   'get area object wind pressure load
      ret = SapModel.AreaObj.GetLoadWindPressure("ALL", NumberItems, AreaName, LoadPat, MyType, Cp, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

The function is obsolete and has been superseded by [GetLoadWindPressure\_1](../Object_Model/Area_Object/GetLoadWindPressure_1.htm) as of v22.1.0. This function is maintained for backward compatibility.

## See Also

[SetLoadWindPressure](../Object_Model/Area_Object/SetLoadWindPressure.htm)

[DeleteLoadWindPressure](../Object_Model/Area_Object/DeleteLoadWindPressure.htm)



## GetLoads {Static Linear Multistep}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetLoads_{Static_Linear_Multistep}.htm`*

# GetLoads

## Syntax

SapObject.SapModel.LoadCases.StaticLinearMultistep.GetLoads

## VB6 Procedure

Function GetLoads(ByVal Name As String, ByRef NumberLoads As Long, ByRef LoadType() As String, ByRef LoadName() As String, ByRef SF() As Double) As Long

## Parameters

Name

The name of an existing static linear multistep analysis case.

NumberLoads

The number of loads assigned to the specified analysis case.

LoadType

This is an array that includes either Load or Accel, indicating the type of each load assigned to the load case.

LoadName

This is an array that includes the name of each load assigned to the load case.

If the LoadType item is Load, this item is the name of a defined load pattern.

If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or RZ, indicating the direction of the load.

SF

This is an array that includes the scale factor of each load assigned to the load case. [L/s2] for Accel UX UY and UZ; otherwise unitless

## Remarks

This function retrieves the load data for the specified load case.

The function returns zero if the data is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetCaseStaticLinearMultistepLoads()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyLoadType() As String
      Dim MyLoadName() As String
      Dim MySF() As Double
      Dim NumberLoads As Long
      Dim LoadType() As String
      Dim LoadName() As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add static linear multistep load case
      ret = SapModel.LoadCases.StaticLinearMultistep.SetCase("LCASE1")

   'set load data
      ReDim MyLoadType(1)
      ReDim MyLoadName(1)
      ReDim MySF(1)
      MyLoadType(0) = "Load"
      MyLoadName(0) = "DEAD"
      MySF(0) = 0.7
      MyLoadType(1) = "Accel"
      MyLoadName(1) = "UZ"
      MySF(1) = 1.2
      ret = SapModel.LoadCases.StaticLinearMultistep.SetLoads("LCASE1", 2, MyLoadType, MyLoadName, MySF)

   'get load data
      ret = SapModel.LoadCases.StaticLinearMultistep.GetLoads("LCASE1", NumberLoads, LoadType, LoadName, SF)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoads](SetLoads_{Static_Linear_Multistep}.htm)



## GetModalComb

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetModalComb.htm`*

# GetModalComb (Note:  Newer function available)

## Syntax

SapObject.SapModel.LoadCases.ResponseSpectrum.GetModalComb

## VB6 Procedure

Function GetModalComb(ByVal Name As String, ByRef MyType As Long, ByRef F1 As Double, ByRef F2 As Double, ByRef td As Double) As Long

## Parameters

Name

The name of an existing response spectrum load case.

MyType

This is 1, 2, 3, 4, 5 or 6, indicating the modal combination option.

1 = CQC

2 = SRSS

3 = ABS

4 = GMC

5 = 10 percent

6 = Double sum

F1

This item applies only when MyType = 4. It is the GMC f1 factor. [cyc/s]

F2

This item applies only when MyType = 4. It is the GMC f2 factor. [cyc/s]

td

This item applies only when MyType = 6. It is the factor td. [s]

## Remarks

This function retrieves the modal combination option assigned to the specified load case.

The function returns zero if the option is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetCaseResponseSpectrumModalComb()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyType As Long
      Dim F1 As Double
      Dim F2 As Double
      Dim td As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add response spectrum load case
      ret = SapModel.LoadCases.ResponseSpectrum.SetCase("LCASE1")

   'get modal combination option
      ret = SapModel.LoadCases.ResponseSpectrum.GetModalComb("LCASE1", MyType, F1, F2, td)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

The function is obsolete and has been superseded by [GetModalComb\_1](../definitions/load_case/response_spectrum/GetModalComb_1.htm) as of version 14.00. This function is maintained for backward compatibility. New function added

## See Also

[SetModalComb](GetModalComb.htm)



## GetNTC2008 {Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetNTC2008_{Wind_Load}-obsolete.htm`*

# GetNTC2008 (Note:  Obsolete, Newer Function Available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.GetNTC2008

## VB6 Procedure

Function GetNTC2008(ByVal Name As String, ByRef ExposureFrom As Long, ByRef DirAngle As Double, ByRef Cpw As Double, ByRef Cpl As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef Vb As Double, ByRef ExposureCategory As Long, ByRef ct As Double, ByRef cd As Double, ByRef cp As Double, ByRef UserExposure As Boolean) As Long

## Parameters

Name

The name of an existing Wind-type load pattern with an NTC 2008 auto wind assignment.

ExposureFrom

This is 1 or 2, indicating the source of the wind exposure.

1 = From extents of rigid diaphragms

2 = From area objects

DirAngle

The direction angle for the wind load. This item applies only when ExposureFrom = 1.

Cpw

The windward coefficient, Cp. This item applies only when ExposureFrom = 1.

Cpl

The leeward coefficient, Cp. This item applies only when ExposureFrom = 1.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

Vb

The wind velocity in m/s.

ExposureCategory

This is 1, 2, 3, 4, or 5, indicating the exposure category.

1 = I

2 = II

3 = III

4 = IV

5 = V

ct

The topography factor, ct.

cd

The dynamic coefficient, cd.

cp

The shape factor, cp.

UserExposure

If this item is True, the wind exposure widths are provided by the user. If it is False, the wind exposure widths are calculated by the program from the extents of the diaphragms.

## Remarks

This function retrieves auto wind loading parameters for NTC 2008.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub GetWindNTC2008()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ExposureFrom As Long
      Dim DirAngle As Double
      Dim Cpw As Double
      Dim Cpl As Double
      Dim UserZ As Boolean
      Dim TopZ As Double
      Dim BottomZ As Double
      Dim Vb As Double
      Dim ExposureCategory As Long

      Dim ct As Double

      Dim cd As Double

      Dim cp As Double
      Dim UserExposure As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", eLoadPatternType\_WIND)

   'assign NTC2008 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetNTC2008("WIND", 1, 0, 0.8, 0.5, False, 0, 0, 35, 3, 1, 1, 1, False)

   'get NTC2008 parameters
      ret = SapModel.LoadPatterns.AutoWind.GetNTC2008("WIND", ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, Vb, ExposureCategory, ct, cd, cp , UserExposure )

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 18.1.0.

This function was replaced by [GetNTC2008\_1](../Definitions/Load_Pattern/Auto_Wind_Load/GetNTC2008_1{Wind_Load}.htm).

## See Also

[SetNTC2008](SetNTC2008_{Wind_Load}-obsolete.htm)



## GetNTC2018 {Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetNTC2018_{Wind_Load}-obsolete.htm`*

# GetNTC2018 (Note:  Obsolete, Newer Function Available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.GetNTC2018

## VB6 Procedure

Function GetNTC2018(ByVal Name As String, ByRef ExposureFrom As Long, ByRef DirAngle As Double, ByRef Cpw As Double, ByRef Cpl As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef Vb As Double, ByRef ExposureCategory As Long, ByRef ct As Double, ByRef cd As Double, ByRef cp As Double, ByRef UserExposure As Boolean) As Long

## Parameters

Name

The name of an existing Wind-type load pattern with an NTC 2018 auto wind assignment.

ExposureFrom

This is 1 or 2, indicating the source of the wind exposure.

1 = From extents of rigid diaphragms

2 = From area objects

DirAngle

The direction angle for the wind load. This item applies only when ExposureFrom = 1.

Cpw

The windward coefficient, Cp. This item applies only when ExposureFrom = 1.

Cpl

The leeward coefficient, Cp. This item applies only when ExposureFrom = 1.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

Vb

The wind velocity in m/s.

ExposureCategory

This is 1, 2, 3, 4, or 5, indicating the exposure category.

1 = I

2 = II

3 = III

4 = IV

5 = V

ct

The topography factor, ct.

cd

The dynamic coefficient, cd.

cp

The shape factor, cp.

UserExposure

If this item is True, the wind exposure widths are provided by the user. If it is False, the wind exposure widths are calculated by the program from the extents of the diaphragms.

## Remarks

This function retrieves auto wind loading parameters for NTC 2018.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub GetWindNTC2018()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ExposureFrom As Long
      Dim DirAngle As Double
      Dim Cpw As Double
      Dim Cpl As Double
      Dim UserZ As Boolean
      Dim TopZ As Double
      Dim BottomZ As Double
      Dim Vb As Double
      Dim ExposureCategory As Long

      Dim ct As Double

      Dim cd As Double

      Dim cp As Double
      Dim UserExposure As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", eLoadPatternType\_WIND)

   'assign NTC2018 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetNTC2018("WIND", 1, 0, 0.8, 0.5, False, 0, 0, 35, 3, 1, 1, 1, False)

   'get NTC2018 parameters
      ret = SapModel.LoadPatterns.AutoWind.GetNTC2018("WIND", ExposureFrom, DirAngle, Cpw, Cpl, UserZ, TopZ, BottomZ, Vb, ExposureCategory, ct, cd, cp , UserExposure )

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

This function was replaced by [GetNTC2018\_1](../Definitions/Load_Pattern/Auto_Wind_Load/GetNTC2018_1{Wind_Load}.htm).

## See Also

[SetNTC2018](SetNTC2018_{Wind_Load}_obsolete.htm)



## GetNZS11702004

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetNZS11702004.htm`*

# GetNZS11702004

## Syntax

SapObject.SapModel.Func.FuncRS.GetNZS11702004

## VB6 Procedure

Function GetNZS11702004(ByVal Name As String, ByVal NZS2004SiteClass As Long, ByVal NZS2004Z As Double, ByVal NZS2004R As Double, ByVal NZS2004DIST As Double, ByRef DampRatio As Double) As Long

## Parameters

Name

The name of a NZS 1170 2004 response spectrum function.

NZS2004SiteClass

This is 1, 2, 3, 4 or 5, indicating the site class.

1 = A

2 = B

3 = C

4 = D

5 = E

NZS2004Z

The hazard factor, Z.

NZS2004R

The return period factor, R.

NZS2004DIST

Distance to the fault in km, used to calculate the near fault factor.

DampRatio

The damping ratio for the function, 0 <= DampRatio < 1.

## Remarks

This function retrieves the definition of an NZS 1170 2004 response spectrum function.

The function returns zero if the function definition is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetRSFuncNZS11702004()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NZS2004SiteClass As Long
      Dim NZS2004Z As Double
      Dim NZS2004R As Double
      Dim NZS2004DIST As Double
      Dim DampRatio As Double

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

   'add NZS 1170 2004 RS function
      ret = SapModel.Func.FuncRS.SetNZS11702004("RS-1", 3, 0.4, 1.3, 20, 0.04)

   'get NZS 1170 2004 RS function
      ret = SapModel.Func.FuncRS.GetNZS11702004("RS-1", NZS2004SiteClass, NZS2004Z, NZS2004R, NZS2004DIST, DampRatio)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

Modified NZS2004N to NZS2004DIST in version 14.1.0.

## See Also

[SetNZS11702004](SetNZS11702004.htm)



## GetNZS11702004 (Auto Seismic)

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetNZS11702004_(Auto_Seismic).htm`*

# GetNZS11702004

## Syntax

SapObject.SapModel.LoadPatterns.AutoSeismic.GetNZS11702004

## VB6 Procedure

Function GetNZS11702004(ByVal Name As String, ByRef DirFlag As Long, ByRef Eccen As Double, ByRef PeriodFlag As Long, ByRef UserT As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef NZS2004SiteClass As Long, ByRef NZS2004Z As Double, ByRef NZS2004R As Double, ByRef NZS2004DIST As Double, ByRef NZS2004Sp As Double, ByRef NZS2004Mu As Double) As Long

## Parameters

Name

The name of an existing Quake-type load pattern with a NZS 1170 2004 auto seismic load assignment.

DirFlag

This is 1 or 2, indicating the seismic load direction.

1 = Global X

2 = Global Y

Eccen

The eccentricity ratio that applies to all diaphragms.

PeriodFlag

This is 1, 2 or 3, indicating the time period option.

1 = Approximate

2 = Program calculated

3 = User defined

UserT

The user specified time period. This item applies when the PeriodFlag item is 3. [s]

UserZ

This item is True if the top and bottom elevations of the seismic load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto seismic loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto seismic loads are applied. [L]

NZS2004SiteClass

This is 1, 2, 3, 4 or 5, indicating the site class.

1 = A

2 = B

3 = C

4 = D

5 = E

NZS2004Z

The hazard factor, Z.

NZS2004R

The return period factor, R.

NZS2004DIST

Distance to the fault in km, used to calculate the near fault factor..

NZS2004Sp

The structural performance factor, Sp.

NZS2004Mu

The structural ductility factor, u.

## Remarks

This function retrieves auto seismic loading parameters for the NZS 1170 2004 code.

The function returns zero if the parameters are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSeismicParametersNZS11702004()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DirFlag As Long
      Dim Eccen As Double
      Dim PeriodFlag As Long
      Dim UserT As Double
      Dim UserZ As Boolean
      Dim TopZ As Double
      Dim BottomZ As Double
      Dim NZS2004SiteClass As Long
      Dim NZS2004Z As Double
      Dim NZS2004R As Double
      Dim NZS2004DIST As Double
      Dim NZS2004Sp As Double
      Dim NZS2004Mu As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("EQX", LTYPE\_QUAKE)

   'assign NZS 1170 2004 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetNZS11702004("EQX", 2, 0.1, 2, 0, False, 0, 0, 3, 0.4, 1.3, 20, 0.7, 3)

   'get NZS 1170 2004 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.GetNZS11702004("EQX", DirFlag, Eccen, PeriodFlag, UserT, UserZ, TopZ, BottomZ, NZS2004SiteClass, NZS2004Z, NZS2004R, NZS2004DIST, NZS2004Sp, NZS2004Mu)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

Modified NZS2004N TO NZS2004DIST in version 14.1.0.

## See Also

[SetNZS11702004](SetNZS11702004_(Auto_Seismic).htm)



## GetNZS11702004 (Auto Seismic)_1

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetNZS11702004_(Auto_Seismic)_1.htm`*

# GetNZS11702004\_1 (Note: Newer function available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoSeismic.GetNZS11702004\_1

## VB6 Procedure

Function GetNZS11702004\_1(ByVal Name As String, ByRef
DirFlag As Long, ByRef Eccen As Double, ByRef PeriodFlag As Long, ByRef
UserT As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ
As Double, ByRef NZS2004SiteClass As Long, ByRef NZS2004Z As Double, ByRef
NZS2004R As Double, ByRef NZS2004DIST As Double, ByRef NZS2004Sp As Double,
ByRef NZS2004Mu As Double, ByRefNZS2004ConsiderTSite As Boolean, ByRefNZS2004TSite
As Double) As Long

## Parameters

Name

The name of an existing Quake-type load pattern with
a NZS 1170 2004 auto seismic load assignment.

DirFlag

This is 1 or 2, indicating the seismic load direction.

1 = Global X

2 = Global Y

Eccen

The eccentricity ratio that applies to all diaphragms.

PeriodFlag

This is 1, 2 or 3, indicating the time period option.

1 = Approximate

2 = Program calculated

3 = User defined

UserT

The user specified time period. This item applies when
the PeriodFlag item is 3. [s]

UserZ

This item is True if the top and bottom elevations of
the seismic load are user specified. It is False if the elevations are
determined by the program.

TopZ

This item applies only when the UserZ item is True.
It is the global Z-coordinate at the highest level where auto seismic
loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True.
It is the global Z-coordinate at the lowest level where auto seismic loads
are applied. [L]

NZS2004SiteClass

This is 1, 2, 3, 4 or 5, indicating the site class.

1 = A

2 = B

3 = C

4 = D

5 = E

NZS2004Z

The hazard factor, Z.

NZS2004R

The return period factor, R.

NZS2004DIST

Distance to the fault in km, used to calculate the near
fault factor..

NZS2004Sp

The structural performance factor, Sp.

NZS2004Mu

The structural ductility factor, u.

NZS2004ConsiderTSite

Indicates whether to consider the site period for the
spectral shape factor.

NZS2004TSite

The low amplitude site period.

## Remarks

This function retrieves auto seismic loading parameters
for the NZS 1170 2004 code.

The function returns zero if the parameters are successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSeismicParametersNZS11702004\_1()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DirFlag As Long
      Dim Eccen As Double
      Dim PeriodFlag As Long
      Dim UserT As Double
      Dim UserZ As Boolean
      Dim TopZ As Double
      Dim BottomZ As Double
      Dim NZS2004SiteClass As Long
      Dim NZS2004Z As Double
      Dim NZS2004R As Double
      Dim NZS2004DIST As Double
      Dim NZS2004Sp As Double
      Dim NZS2004Mu As Double

      Dim NZS2004ConsiderTSite
As Boolean

      Dim NZS2004TSite
As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab,
2, 144, 3, 336, 2, 432)

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("EQX",
LTYPE\_QUAKE)

   'assign NZS 1170 2004 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetNZS11702004\_1("EQX",
2, 0.1, 2, 0, False, 0, 0, 3, 0.4, 1.3, 20, 0.7, 3, True, 1)

   'get NZS 1170 2004 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.GetNZS11702004\_1("EQX",
DirFlag, Eccen, PeriodFlag, UserT, UserZ, TopZ, BottomZ, NZS2004SiteClass,
NZS2004Z, NZS2004R, NZS2004DIST, NZS2004Sp, NZS2004Mu, NZS2004ConsiderTSite,
NZS2004TSite)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v21.0.0.

This function supersedes [GetNZS11702004](GetNZS11702004_(Auto_Seismic).htm).

This function is obsolete and has been superseded by
GetNZS11702004\_2 as of v22.0.0. This function is maintained for backward
compatibility.

## See Also

[SetNZS11702004\_1](SetNZS11702004_(Auto_Seismic)_1.htm)



## GetNameList {Load Case}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetNameList_{Load_Case}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.LoadCases.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String, Optional ByVal CaseType As eLoadCaseType) As Long

## Parameters

NumberNames

The number of load case names retrieved by the program.

MyName

This is a one-dimensional array of load case names. The MyName array is created as a dynamic, zero-based, array by the API user:

Dim MyName() as String

The array is dimensioned to (NumberNames - 1) inside the Sap2000 program, filled with the names, and returned to the API user.

CaseType

This optional value is one of the following items in the eLoadCaseType enumeration.

LinearStatic = 1

NonlinearStatic = 2

Modal = 3

ResponseSpectrum = 4

LinearHistory = 5  (Modal Time History)

NonlinearHistory = 6  (Modal Time History)

LinearDynamic = 7  (Direct Integration Time History)

NonlinearDynamic = 8  (Direct Integration Time History)

MovingLoad = 9

Buckling = 10

SteadyState = 11

PowerSpectralDensity = 12

LinearStaticMultistep = 13

Hyperstatic = 14

ExternalResults = 15

If no value is input for CaseType, names are returned for all load cases in the model regardless of type.

## Remarks

This function retrieves the names of all defined load cases of the specified type.

The function returns zero if the names are successfully retrieved, otherwise it returns nonzero.

## VBA Example

Sub GetLoadCaseNames()
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

   'get load case names
      ret = SapModel.LoadCases.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Added optional CaseType parameter in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

Added one item to the eLoadCaseType enumeration in version 12.00.

This function is obsolete and has been superseded by GetNameList\_1 as of v21.0.0. This function is maintained for backwards compatibility where staged construction and nonlinear multi-step cases are a subtype of load case type nonlinear static.

## See Also



## GetOConcrete

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetOConcrete.htm`*

# GetOConcrete (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropMaterial.GetOConcrete

## VB6 Procedure

Function GetOConcrete(ByVal Name As String, ByRef fc As Double, ByRef IsLightweight As Boolean, ByRef fcsfactor As Double, ByRef SSType As Long, ByRef SSHysType As Long, ByRef StrainAtfc As Double, ByRef StrainUltimate As Double, ByRef FrictionAngle As Double, ByRef DilatationalAngle As Double, Optional ByVal Temp As Double = 0) As Long

## Parameters

Name

The name of an existing concrete material property.

fc

The concrete compressive strength. [F/L2]

IsLightweight

If this item is True, the concrete is assumed to be lightweight concrete.

fcsfactor

The shear strength reduction factor for lightweight concrete.

eFu

The expected tensile stress. [F/L2]

SSType

This is 0, 1 or 2, indicating the stress-strain curve type.

0 = User defined

1 = Parametric - Simple

2 = Parametric - Mander

SSHysType

This is 0, 1 or 2, indicating the stress-strain hysteresis type.

0 = Elastic

1 = Kinematic

2 = Takeda

StrainAtfc

This item applies only to parametric stress-strain curves. It is the strain at the unconfined compressive strength.

StrainUltimate

This item applies only to parametric stress-strain curves. It is the ultimate unconfined strain capacity.

FrictionAngle

The Drucker-Prager friction angle, 0 <= FrictionAngle < 90. [deg]

DilatationalAngle

The Drucker-Prager dilatational angle, 0 <= DilatationalAngle < 90. [deg]

Temp

This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.

This item is the temperature at which the specified data is to be retrieved. The temperature must have been defined previously for the material.

## Remarks

This function retrieves the other material property data for concrete materials.

The function returns zero if the data is successfully retrieved; otherwise it returns a nonzero value. The function returns an error if the specified material is not concrete.

## VBA Example

Sub GetMatPropConcreteData()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim fc As Double
      Dim IsLightweight As Boolean
      Dim fcsfactor As Double
      Dim SSType As Long
      Dim SSHysType As Long
      Dim StrainAtfc As Double
      Dim StrainUltimate As Double
      Dim FrictionAngle As Double
      Dim DilatationalAngle As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'initialize new material property
      ret = SapModel.PropMaterial.SetMaterial("Concrete", MATERIAL\_CONCRETE)

   'assign other properties
      ret = SapModel.PropMaterial.SetOConcrete("Concrete", 5, False, 0, 1, 2, 0.0022, 0.0052)

   'get other properties
      ret = SapModel.PropMaterial.GetOConcrete("Concrete", fc, IsLightweight, fcsfactor, SSType, SSHysType, StrainAtfc, StrainUltimate, FrictionAngle, DilatationalAngle)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

This function is obsolete and has been superseded by [GetOConcrete\_1](GetOConcrete_1.htm) as of version 12.00. This function is maintained for backwards compatibility.

## See Also

[SetOConcrete](GetOConcrete.htm)



## GetOConcrete_1

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetOConcrete_1.htm`*

# GetOConcrete\_1

## Syntax

SapObject.SapModel.PropMaterial.GetOConcrete\_1

## VB6 Procedure

Function GetOConcrete\_1(ByVal Name As String, ByRef fc As Double, ByRef IsLightweight As Boolean, ByRef fcsfactor As Double, ByRef SSType As Long, ByRef SSHysType As Long, ByRef StrainAtfc As Double, ByRef StrainUltimate As Double, ByRef FinalSlope As Double, ByRef FrictionAngle As Double, ByRef DilatationalAngle As Double, Optional ByVal Temp As Double = 0) As Long

## Parameters

Name

The name of an existing concrete material property.

fc

The concrete compressive strength. [F/L2]

IsLightweight

If this item is True, the concrete is assumed to be lightweight concrete.

fcsfactor

The shear strength reduction factor for lightweight concrete.

SSType

This is 0, 1 or 2, indicating the stress-strain curve type.

0 = User defined

1 = Parametric - Simple

2 = Parametric - Mander

SSHysType

This is 0, 1 or 2, indicating the stress-strain hysteresis type.

0 = Elastic

1 = Kinematic

2 = Takeda

StrainAtfc

This item applies only to parametric stress-strain curves. It is the strain at the unconfined compressive strength.

StrainUltimate

This item applies only to parametric stress-strain curves. It is the ultimate unconfined strain capacity.

FinalSlope

This item applies only to parametric stress-strain curves. It is a multiplier on the material modulus of elasticity, E. This value multiplied times E gives the final slope on the compression side of the curve.

FrictionAngle

The Drucker-Prager friction angle, 0 <= FrictionAngle < 90. [deg]

DilatationalAngle

The Drucker-Prager dilatational angle, 0 <= DilatationalAngle < 90. [deg]

Temp

This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.

This item is the temperature at which the specified data is to be retrieved. The temperature must have been defined previously for the material.

## Remarks

This function retrieves the other material property data for concrete materials.

The function returns zero if the data is successfully retrieved; otherwise it returns a nonzero value. The function returns an error if the specified material is not concrete.

## VBA Example

Sub GetMatPropConcreteData\_1()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim fc As Double
      Dim IsLightweight As Boolean
      Dim fcsfactor As Double
      Dim SSType As Long
      Dim SSHysType As Long
      Dim StrainAtfc As Double
      Dim StrainUltimate As Double
      Dim FinalSlope As Double
      Dim FrictionAngle As Double
      Dim DilatationalAngle As Double

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

   'initialize new material property
      ret = SapModel.PropMaterial.SetMaterial("Concrete", MATERIAL\_CONCRETE)

   'assign other properties
      ret = SapModel.PropMaterial.SetOConcrete\_1("Concrete", 5, False, 0, 1, 2, 0.0022, 0.0052, -0.1)

   'get other properties
      ret = SapModel.PropMaterial.GetOConcrete\_1("Concrete", fc, IsLightweight, fcsfactor, SSType, SSHysType, StrainAtfc, StrainUltimate, FinalSlope, FrictionAngle, DilatationalAngle)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

This function supersedes [GetOConcrete](GetOConcrete.htm).

## See Also

[SetOConcrete\_1](SetOConcrete_1.htm)



## GetORebar

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetORebar.htm`*

# GetORebar (Note:  Newer Function Available)

## Syntax

SapObject.SapModel.PropMaterial.GetORebar

## VB6 Procedure

Function GetORebar(ByVal Name As String, ByRef Fy As Double, ByRef Fu As Double, ByRef eFy As Double, ByRef eFu As Double, ByRef SSType As Long, ByRef SSHysType As Long, ByRef StrainAtHardening As Double, ByRef StrainUltimate As Double, ByRef UseCaltransSSDefaults As Boolean, Optional ByVal Temp As Double = 0) As Long

## Parameters

Name

The name of an existing rebar material property.

Fy

The minimum yield stress. [F/L2]

Fu

The minimum tensile stress. [F/L2]

eFy

The expected yield stress. [F/L2]

eFu

The expected tensile stress. [F/L2]

SSType

This is 0, 1 or 2, indicating the stress-strain curve type.

0 = User defined

1 = Parametric - Simple

2 = Parametric - Park

SSHysType

This is 0, 1 or 2, indicating the stress-strain hysteresis type.

0 = Elastic

1 = Kinematic

2 = Takeda

StrainAtHardening

This item applies only when parametric stress-strain curves are used and when UseCaltransSSDefaults is False. It is the strain at the onset of strain hardening.

StrainUltimate

This item applies only when parametric stress-strain curves are used and when UseCaltransSSDefaults is False. It is the ultimate strain capacity. This item must be larger than the StrainAtHardening item.

UseCaltransSSDefaults

If this item is True, the program uses Caltrans default controlling strain values, which are bar size dependent.

Temp

This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.

This item is the temperature at which the specified data is to be retrieved. The temperature must have been defined previously for the material.

## Remarks

This function retrieves the other material property data for rebar materials.

The function returns zero if the data is successfully retrieved; otherwise it returns a nonzero value. The function returns an error if the specified material is not rebar.

## VBA Example

Sub GetMatPropRebarData()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Fy As Double
      Dim Fu As Double
      Dim eFy As Double
      Dim eFu As Double
      Dim SSType As Long
      Dim SSHysType As Long
      Dim StrainAtHardening As Double
      Dim StrainUltimate As Double
      Dim UseCaltransSSDefaults As Boolean

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'initialize new material property
      ret = SapModel.PropMaterial.SetMaterial("Rebar", MATERIAL\_REBAR)

   'assign other properties
      ret = SapModel.PropMaterial.SetORebar("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, False)

   'get other properties
      ret = SapModel.PropMaterial.GetORebar("Rebar", Fy, Fu, eFy, eFu, SSType, SSHysType, StrainAtHardening, StrainUltimate, UseCaltransSSDefaults)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

This function is obsolete and has been superseded by .[GetORebar\_1](../Definitions/Properties/Material/GetORebar_1.htm) as of version 12.00. This function is maintained for backwards compatibility.

## See Also

[SetORebar](GetORebar.htm)



## GetOSteel

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetOSteel.htm`*

# GetOSteel (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropMaterial.GetOSteel

## VB6 Procedure

Function GetOSteel(ByVal Name As String, ByRef Fy As Double, ByRef Fu As Double, ByRef eFy As Double, ByRef eFu As Double, ByRef SSType As Long, ByRef SSHysType As Long, ByRef StrainAtHardening As Double, ByRef StrainAtMaxStress As Double, ByRef StrainAtRupture As Double, Optional ByVal Temp As Double = 0) As Long

## Parameters

Name

The name of an existing steel material property.

Fy

The minimum yield stress. [F/L2]

Fu

The minimum tensile stress. [F/L2]

eFy

The expected yield stress. [F/L2]

eFu

The expected tensile stress. [F/L2]

SSType

This is 0 or 1. indicating the stress-strain curve type.

0 = User defined

1 = Parametric - Simple

SSHysType

This is 0, 1 or 2, indicating the stress-strain hysteresis type.

0 = Elastic

1 = Kinematic

2 = Takeda

StrainAtHardening

This item applies only to parametric stress-strain curves. It is the strain at the onset of strain hardening.

StrainAtMaxStress

This item applies only to parametric stress-strain curves. It is the strain at maximum stress.

StrainAtRupture

This item applies only to parametric stress-strain curves. It is the strain at rupture.

Temp

This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.

This item is the temperature at which the specified data is to be retrieved. The temperature must have been defined previously for the material.

## Remarks

This function retrieves the other material property data for steel materials.

The function returns zero if the data is successfully retrieved; otherwise it returns a nonzero value. The function returns an error if the specified material is not steel.

## VBA Example

Sub GetMatPropSteelData()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Fy As Double
      Dim Fu As Double
      Dim eFy As Double
      Dim eFu As Double
      Dim SSType As Long
      Dim SSHysType As Long
      Dim StrainAtHardening As Double
      Dim StrainAtMaxStress As Double
      Dim StrainAtRupture As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'initialize new material property
      ret = SapModel.PropMaterial.SetMaterial("Steel", MATERIAL\_STEEL)

   'assign other properties
      ret = SapModel.PropMaterial.SetOSteel("Steel", 55, 68, 60, 70, 1, 2, 0.02, 0.1, 0.2)

   'get other properties
      ret = SapModel.PropMaterial.GetOSteel("Steel", Fy, Fu, eFy, eFu, SSType, SSHysType, StrainAtHardening, StrainAtMaxStress, StrainAtRupture)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

This function is obsolete and has been superseded by [GetOSteel\_1](../Definitions/Properties/Material/GetOSteel_1.htm) as of version 12.00. This function is maintained for backwards compatibility.

## See Also

[SetOSteel](SetOSteel.htm)



## GetOTendon

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetOTendon.htm`*

# GetOTendon (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropMaterial.GetOTendon

## VB6 Procedure

Function GetOTendon(ByVal Name As String, ByRef Fy As Double, ByRef Fu As Double, ByRef SSType As Long, ByRef SSHysType As Long, Optional ByVal Temp As Double = 0) As Long

## Parameters

Name

The name of an existing tendon material property.

Fy

The minimum yield stress. [F/L2]

Fu

The minimum tensile stress. [F/L2]

SSType

This is 0, 1 or 2, indicating the stress-strain curve type.

0 = User defined

1 = Parametric – 250 ksi strand

2 = Parametric – 270 ksi strand

SSHysType

This is 0, 1 or 2, indicating the stress-strain hysteresis type.

0 = Elastic

1 = Kinematic

2 = Takeda

Temp

This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.

This item is the temperature at which the specified data is to be retrieved. The temperature must have been defined previously for the material.

## Remarks

This function retrieves the other material property data for tendon materials.

The function returns zero if the data is successfully retrieved; otherwise it returns a nonzero value. The function returns an error if the specified material is not tendon.

## VBA Example

Sub GetMatPropTendonData()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Fy As Double
      Dim Fu As Double
      Dim SSType As Long
      Dim SSHysType As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'initialize new material property
      ret = SapModel.PropMaterial.SetMaterial("Tendon", MATERIAL\_TENDON)

   'assign other properties
      ret = SapModel.PropMaterial.SetOTendon("Tendon", 230, 255, 1, 1)

   'get other properties
      ret = SapModel.PropMaterial.GetOTendon("Tendon", Fy, Fu, SSType, SSHysType)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

This function is obsolete and has been superseded by [GetOTendon\_1](../Definitions/Properties/Material/GetOTendon_1.htm) as of version 12.00. This function is maintained for backwards compatibility.

## See Also

[SetOTendon](SetOTendon.htm)



## GetOverwrite {Concrete Chinese 2002}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetOverwrite_{Concrete_Chinese_2002}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Chinese\_2002.GetOverwrite

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

Sub GetConcreteDesignOverwriteItemChinese\_2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

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
      ret = SapModel.DesignConcrete.SetCode("Chinese 2002")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start concrete design
      ret = SapModel.DesignConcrete.StartDesign

   'get overwrite item
      ret = SapModel.DesignConcrete.Chinese\_2002.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added Items 17 and 18 in Version 14.0.0.

## See Also

[SetOverwrite](SetOverwrite_{Concrete_Chinese_2002}.htm)



## GetOverwrite {Steel Chinese 2002}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetOverwrite_{Steel_Chinese_2002}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Chinese\_2002.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 51, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Element type

3 = Is transfer column

4 = Seismic magnification factor

5 = Is rolled section

6 = Is flange edge cut by gas

7 = Is both end pinned

8 = Ignore b/t check

9 = Classify beam as flexo-compression member

10 = Is beam top loaded

11 = Consider deflection

12 = Deflection check type

13 = DL deflection limit, L/Value

14 = SDL + LL deflection limit, L/Value

15 = LL deflection limit, L/Value

16 = Total load deflection limit, L/Value

17 = Total camber limit, L/Value

18 = DL deflection limit, absolute

19 = SDL + LL deflection limit, absolute

20 = LL deflection limit, absolute

21 = Total load deflection limit, absolute

22 = Total camber limit, absolute

23 = Specified camber

24 = Net area to total area ratio

25 = Live load reduction factor

26 = Unbraced length ratio, Major

27 = Unbraced length ratio, Minor Lateral Torsional Buckling

28 = Effective length factor, Mue Major

29 = Effective length factor, Mue Minor

30 = Moment coefficient, Beta\_m Major

31 = Moment coefficient, Beta\_m Minor

32 = Moment coefficient, Beta\_t Major

33 = Moment coefficient, Beta\_t Minor

34 = Axial stability coefficient, Phi Major

35 = Axial stability coefficient, Phi Minor

36 = Flexural stability coeff, Phi\_bMajor

37 = Flexural stability coeff, Phi\_bMinor

38 = Plasticity factor, Gamma Major

39 = Plasticity factor, Gamma Minor

40 = Section influence coefficient, Eta

41 = B/C capacity factor, Eta

42 = Euler moment factor, Delta Major

43 = Euler moment factor, Delta Minor

44 = Yield stress, Fy

45 = Allowable normal stress, f

46 = Allowable shear stress, fv

47 = Consider fictitious shear

48 = Demand/capacity ratio limit

49 = Dual system magnification factor

50 = Lo/r limit in compression

51 = L/r limit in tension

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Sway Moment Frame, SMF

2 = Concentrically Braced Frame, CBF

3 = Eccentrically Braced Frame, EBF

4 = NonSway Moment Frame, NMF

2 = Element type

0 = Program Determined

1 = Column

2 = Beam

3 = Brace

4 = Truss

3 = Is transfer column

0 = Program Determined

1 = No

2 = Yes

4 = Seismic magnification factor

Value >= 0; 0 means no check for this item.

5 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

6 = Is flange edge cut by gas

0 = Program Determined

1 = No

2 = Yes

7 = Is both end pinned

0 = Program Determined

1 = No

2 = Yes

8 = Ignore b/t check

0 = Program Determined

1 = No

2 = Yes

9 = Classify beam as flexo-compression member

0 = Program Determined

1 = No

2 = Yes

10 = Is beam top loaded

0 = Program Determined

1 = No

2 = Yes

11 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

12 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

13 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

14 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

15 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

16 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

17 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

18 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

19 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

20 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

21 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

22 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

23 = Specified camber

Value >= 0. [L]

24 = Net area to total area ratio

Value >= 0; 0 means use program default value.

25 = Live load reduction factor

Value >= 0; 0 means use program determined value.

26 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

27 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

28 = Effective length factor, Mue Major

Value >= 0; 0 means use program determined value.

29 = Effective length factor, Mue Minor

Value >= 0; 0 means use program determined value.

30 = Moment coefficient, Beta\_m Major

Value >= 0; 0 means use program determined value.

31 = Moment coefficient, Beta\_m Minor

Value >= 0; 0 means use program determined value.

32 = Moment coefficient, Beta\_t Major

Value >= 0; 0 means use program determined value.

33 = Moment coefficient, Beta\_t Minor

Value >= 0; 0 means use program determined value.

34 = Axial stability coefficient, Phi Major

Value >= 0; 0 means use program determined value.

35 = Axial stability coefficient, Phi Minor

Value >= 0; 0 means use program determined value.

36 = Flexural stability coefficient, Phi\_b Major

Value >= 0; 0 means use program determined value.

37 = Flexural stability coefficient, Phi\_b Minor

Value >= 0; 0 means use program determined value.

38 = Plasticity factor, Gamma Major

Value >= 0; 0 means use program determined value.

39 = Plasticity factor, Gamma Minor

Value >= 0; 0 means use program determined value.

40 = Section influence coefficient, Eta

Value >= 0; 0 means use program determined value.

41 = B/C capacity factor, Eta

Value >= 0; 0 means use program determined value.

42 = Euler moment factor, Delta Major

Value >= 0; 0 means use program determined value.

43 = Euler moment factor, Delta Minor

Value >= 0; 0 means use program determined value.

44 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

45 = Allowable normal stress, f

Value >= 0; 0 means use program determined value. [F/L2]

46 = Allowable shear stress, fv

Value >= 0; 0 means use program determined value. [F/L2]

47 = Consider fictitious shear

0 = Program Determined

1 = No

2 = Yes

48 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

49 = Dual system magnification factor

        Value >= 0; 0 means use program default value.

50 = Lo/r limit in compression

        Value >= 0; 0 means use program determined value.

51 = L/r limit in tension

        Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemChinese\_2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Chinese 2002")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Chinese\_2002.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added Items 49, 50, and 51 in Version 14.0.0.

Modified Item 1 and added Truss to Item 2 in version 14.1.0.

## See Also

[SetOverwrite](SetOverwrite_{Steel_Chinese_2002}.htm)



## GetOverwrite {Steel Eurocode 3 2005}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetOverwrite_{Steel_Eurocode_3_2005}.htm`*

# GetOverwrite (Note:  Deprecated, Newer Function Available)

## Syntax

SapObject.SapModel.DesignSteel.Eurocode\_3\_2005.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design
procedure.

Item

This is an integer between 1 and 54, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection
limit, L/Value

5 = SDL + LL deflection
limit, L/Value

6 = LL deflection limit,
L/Value

7 = Total load deflection
limit, L/Value

8 = Total camber limit,
L/Value

9 = DL deflection limit,
absolute

10 = SDL + LL deflection
limit, absolute

11 = LL deflection limit,
absolute

12 = Total load deflection
limit, absolute

13 = Total camber limit,
absolute

14 = Specified camber

15 = Net area to total
area ratio

16 = Live load reduction
factor

17 = Unbraced length ratio,
y-y

18 = Unbraced length ratio,
z-z

19 = Effective length
factor, K2y

20 = Effective length
factor, K2z

21 = Moment coefficient,
kyy

22 = Moment coefficient,
kzz

23 = Bending coefficient,
C1

24
= Moment coefficient, kzy

25
= Moment coefficient, kyz

26 = Yield stress, Fy

27 = Compressive capacity,
Nc.Rd

28 = Tensile capacity,
Nt.Rd

29 = Bending capacity
about y-y axis,Mcy.Rd

30 = Bending capacity
about z-z axis Mcz.Rd

31 = Buckling resistance
moment, Mb.Rd

32 = Shear capacity along
z-z axis, Vz.Rd

33 = Shear capacity along
y-y axis, Vy.Rd

34 = Demand/capacity ratio
limit

35 = Section class

36 = Column buckling curve,
y-y

37 = Column buckling curve,
z-z

38 = Buckling curve for LTB

39 = System overstrength factor,
Omega

40 = Is rolled section

41 = Unbraced length ratio,
LTB

42 = Effective length factor
braced, K1y

43 = Effective length factor
braced, K1z

44 = Effective length factor,
K LTB

45 = Material overstrength
factor, GammaOV

46 = Warping constant, Iw

47 = Elastic torsional buckling
force, Ncr T

48 = Elastic torsional-flexural
buckling force, Ncr TF

49
= Bending coefficient, C2

50 = Bending coefficient,
C3

51 = Warping coefficient,
kw

52 = Coordinate of load application,
za

53
= Shear center coordinate, zs

54
= Elastic critical moment for lateral-torsional buckling, Mcr

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = DCH MRF (Ductility
Class High – Moment Frame)

2 = DCM MRF (Ductility
Class Medium – Moment Frame)

3 = DCL MRF (Ductility
Class Low – Moment Frame)

4 = DCH CBF (Ductility
Class High – Concentrically Braced Frame)

5 = DCM CBF (Ductility
Class Medium – Concentrically Braced Frame)

6 = DCL CBF (Ductility
Class Low – Concentrically Braced Frame)

7 = DCH EBF (Ductility
Class High – Eccentrically Braced Frame)

8 = DCM EBF (Ductility
Class Medium – Eccentrically Braced Frame)

9 = DCL EBF (Ductility
Class Low – Eccentrically Braced Frame)

10 = Inverted pendulum
structure

11 = Secondary

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

5 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

6 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

7 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

8 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

9 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

10 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

11 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

12 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

14 = Specified camber

  Value >=
0. [L]

15 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

16 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

17 = Unbraced length ratio,
y-y

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
z-z

  Value >=
0; 0 means use program determined value.

19 = Effective length
factor sway, K2y

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor sway, K2z

  Value >=
0; 0 means use program determined value.

21 = Moment coefficient,
kyy

  Value >=
0; 0 means use program determined value.

22 = Moment coefficient,
kzz

  Value >=
0; 0 means use program determined value.

23 = Bending coefficient,
C1

  Value >=
0; 0 means use program determined value.

24 = Moment coefficient,
kzy

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
kyz

  Value >=
0; 0 means use program determined value.

26 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

27 = Compressive capacity,
Nc.Rd

  Value >=
0; 0 means use program determined value. [F]

28 = Tensile capacity,
Nt.Rd

  Value >=
0; 0 means use program determined value. [F]

29 = Bending capacity
about y-y axis, Mcy.Rd

  Value >=
0; 0 means use program determined value. [FL]

30 = Bending capacity
about z-z axis, Mcz.Rd

  Value >=
0; 0 means use program determined value. [FL]

31 = Buckling resistance
moment, Mb.Rd

  Value >=
0; 0 means use program determined value. [FL]

32 = Shear capacity along
z-z axis, Vz.Rd

  Value >=
0; 0 means use program determined value. [F]

33 = Shear capacity along
y-y axis, Vy.Rd

  Value >=
0; 0 means use program determined value. [F]

34 = Demand/capacity ratio
limit

  Value >= 0;
0 means use program determined value.

35 = Section class

0 = Program default

1 = Class 1

2 = Class 2

3 = Class 3

4 = Class 4

36 = Column buckling curve,
y-y

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

37 = Column buckling curve,
z-z

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

38
= Buckling curve for LTB

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

39 = System overstrength factor,
Omega

Value >= 0; 0 means use
program determined value.

40 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

41 = Unbraced length ratio,
LTB

Value >= 0; 0 means use
program determined value.

42 = Effective length factor
braced, K1y

Value >= 0; 0 means use
program determined value.

43 = Effective length factor
braced, K1z

Value >= 0; 0 means use
program determined value.

44 = Effective length factor,
K LTB

Value >= 0; 0 means use
program determined value.

45 = Material overstrength
factor, GammaOV

Value >= 0; 0 means use
program determined value.

46 = Warping constant, Iw

Value >= 0; 0 means use
program determined value. [L6]

47 = Elastic torsional buckling
force, Ncr T

Value >= 0; 0 means use
program determined value. [F]

48 = Elastic torsional-flexural
buckling force, Ncr TF

Value >= 0; 0 means use
program determined value. [F]

49
= Bending coefficient, C2

Value >= 0; 0 means
use program determined value.

50 = Bending coefficient,
C3

Value >= 0; 0 means
use program determined value.

51 = Warping coefficient,
kw (used in Mcr calculation)

0.5 =<Value =<
1; 0 means use program determined value which is defaulted to 1.0.

52 = Coordinate of load application, za
(used in Mcr calculation)

53
= Shear center coordinate, zs (used in Mcr calculation)

54
= Elastic critical moment for lateral-torsional buckling, Mcr

Value >=
0; 0 means use program determined value. [FL]

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a steel design
overwrite item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemEurocode\_3\_2005()
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

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Eurocode
3-2005")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Eurocode\_3\_2005.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.0.0.

Updated the list of items in v18.0.0.

Added items 46 – 48 in v18.2.0.

Added items 49 - 52 in v22.0.0

Included all framing types as in Preference form in
SAP2000 Version 22.1.0

Added items 53 - 54 in v22.0.0

Changed references from major and minor axes to y-y
and z-z in version 23.4.0.

The function is DEPRECATED as of version 25.1. Please
use [Get
Overwrite](../Design/Steel/EN_1993_1_1_2005_(Formerly_Eurocode_3-2005)/GetOverwrite_{Steel_EN_1993-1-1_2005}.htm). This topic is maintained for reference.

## See Also

[SetOverwrite](SetOverwrite_{Steel_Eurocode_3_2005}.htm)



## GetPrecastI

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetPrecastI.htm`*

# GetPrecastI (Note: Newer function available)

## Syntax

SapObject.SapModel.PropFrame.GetPrecastI

## VB6 Procedure

Function GetPrecastI(ByVal Name As String, ByRef FileName As String, ByRef MatProp As String, ByRef b() As Double, ByRef d() As Double, ByRef Color As Long, ByRef Notes As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing precast concrete I girder frame section property.

FileName

If the section property was imported from a property file, this is the name of that file. If the section property was not imported, this item is blank.

MatProp

The name of the material property for the section.

b

This is an array, dimensioned to 3, containing the horizontal section dimensions. [L]

b(0) = B1 (> 0)

b(1) = B2 (> 0)

b(2) = B3 (> 0)

b(3) = B4 (>= 0)

Section dimensions B1 through B4 are defined on the precast concrete I girder definition form.

d

This is an array, dimensioned to 5, containing the vertical section dimensions. [L]

d(0) = D1 (> 0)

d(1) = D2 (> 0)

d(2) = D3 (>= 0)

d(3) = D4 (>= 0)

d(4) = D5 (>= 0)

d(5) = D6 (> 0)

Section dimensions D1 through D6 are defined on the precast concrete I girder definition form.

Color

The display color assigned to the section.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned to the section.

## Remarks

This function retrieves frame section property data for a precast concrete I girder frame section.

The function returns zero if the section property data is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePropPrecastI()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim FileName As String
      Dim MatProp As String
      Dim bb() As Double
      Dim dd() As Double
      Dim b() As Double
      Dim d() As Double
      Dim Color As Long
      Dim Notes As String
      Dim GUID As String

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

   'set new frame section property
      ReDim bb(3)
      ReDim dd(5)
      bb(0) = 16
      bb(1) = 22
      bb(2) = 7
      bb(3) = 0
      dd(0) = 45
      dd(1) = 7
      dd(2) = 4.5
      dd(3) = 0
      dd(4) = 7.5
      dd(5) = 7
      ret = SapModel.PropFrame.SetPrecastI("PC1", "4000Psi", bb, dd)

   'get frame section property data
      ret = SapModel.PropFrame.GetPrecastI("PC1", FileName, MatProp, b, d, Color, Notes, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

This function is obsolete and has been superseded by GetPrecast\_1 as of version 17.2.0. This function is maintained for backward compatibility.

## See Also

[SetPrecastI](SetPrecastI.htm)



## GetPreference {Concrete Chinese 2002}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetPreference_{Concrete_Chinese_2002}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Chinese\_2002.GetPreference

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

Sub GetConcreteDesignPreferenceItemChinese\_2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

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
      ret = SapModel.DesignConcrete.SetCode("Chinese 2002")

   'get preference item
      ret = SapModel.DesignConcrete.Chinese\_2002.GetPreference(2, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added Items 9, 10, and 11 in Version 14.0.0.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Concrete_Chinese_2002}.htm)



## GetPreference {Steel Chinese 2002}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetPreference_{Steel_Chinese_2002}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Chinese\_2000.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1 = Framing type

2 = Gamma0

3 = Ignore b/t check

4 = Classify beam as flexo compression member

5 = Consider deflection

6 = DL deflection limit, L/Value

7 = SDL + LL deflection limit, L/Value

8 = LL deflection limit, L/Value

9 = Total load deflection limit, L/Value

10 = Total camber limit, L/Value

11 = Pattern live load factor

12 = Demand/capacity ratio limit

13 = Multi-response case design

14 = Is tall building?

Value

The value of the considered preference item.

1 = Framing type

0 = As specified in preferences

1 = Sway Moment Frame, SMF

2 = Concentrically Braced Frame, CBF

3 = Eccentrically Braced Frame, EBF

4 = NonSway Moment Frame, NMF

2 = Gamma0

Value > 0

3 = Ignore b/t check

0 = No

Any other value = Yes

4 = Classify beam as flexo compression member

0 = No

Any other value = Yes

5 = Consider deflection

0 = No

Any other value = Yes

6 = DL deflection limit, L/Value

Value > 0

7 = SDL + LL deflection limit, L/Value

Value > 0

8 = LL deflection limit, L/Value

Value > 0

9 = Total load deflection limit, L/Value

Value > 0

10 = Total camber limit, L/Value

Value > 0

11 = Pattern live load factor

Value >= 0

12 = Demand/capacity ratio limit

Value > 0

13 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

14 = Tall building

        0 = No

        1 = Yes

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemChinese\_2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'createSapModelobject
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Chinese 2002")

   'get preference item
      ret = SapModel.DesignSteel.Chinese\_2002.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added item 14 in Version 14.0.0.

Modified Item 1 in version 14.1.0.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_Chinese_2002}.htm)



## GetPreference {Steel Eurocode 3 2005}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetPreference_{Steel_Eurocode_3_2005}.htm`*

# GetPreference (Note:  Deprecated, Newer Function Available)

## Syntax

SapObject.SapModel.DesignSteel.Eurocode\_3\_2005.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 24, inclusive, indicating
the preference item considered.

1 = Country

2 = Combos equation

3 = Reliability class

4 = K factor method

5 = Multi-response case
design

6 = Framing type

7 = Behavior factor, q

8 = System overstrength
factor, Omega

9 = Consider P-Delta Done

10 = Consider torsion

11 = GammaM0

12 = GammaM1

13 = GammaM2

14 = Ignore seismic code

15 = Ignore special seismic
load

16 = Doubler plate is
plug-welded

17 = Consider deflection

18 = DL deflection limit,
L/Value

19 = SDL + LL deflection
limit, L/Value

20 = LL deflection limit,
L/Value

21 = Total deflection
limit, L/Value

22 = Total camber limit,
L/Value

23 = Pattern live load
factor

24 = Demand/capacity ratio
limit

Value

The value of the considered preference item.

1 = Country

   1 =
CEN Default

   2 =
United Kingdom

   3 =
Slovenia

   4 =
Bulgaria

   5 =
Norway

   7 =
Sweden

   8 =
Finland

   9 =
Denmark

 10 = Portugal

 11 = Germany

2 = Combos equation

   1 =
1 = Eq. 6.10

   2 =
Max of Eqs. 6.10a and 6.10b

3 = Reliability class

   1 =
Class 1

   2 =
Class 2

   3 =
Class 3

4 = K factor method

   1 =
Method 1 (Annex A)

   2 =
Method 2 (Annex B)

5 = Multi-response case
design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step --  All

6 = Framing type

1 = DCH MRF (Ductility
Class High - Moment Frame)

2 = DCM MRF (Ductility
Class Medium - Moment Frame)

3 = DCL MRF (Ductility
Class Low - Moment Frame)

4 = DCH CBF (Ductility
Class High - Concentrically Braced Frame)

5 = DCH CBF (Ductility
Class Medium - Concentrically Braced Frame)

6 = DCH CBF (Ductility
Class Low - Concentrically Braced Frame)

7 = DCH EBF (Ductility
Class High - Eccentrically Braced Frame)

8 = DCM EBF (Ductility
Class Medium - Eccentrically Braced Frame)

9 = DCL EBF (Ductility
Class Low - Eccentrically Braced Frame)

10 = Inverted pendulum
structure

11 = Secondary

7 = Behavior factor, q

Value > 0

8 = System overstrength
factor, Omega

Value > 0

9 = Consider P-Delta Done

0 = No

Any other value = Yes

10 = Consider torsion

0 = No

Any other value = Yes

11 = GammaM0

Value > 0

12 = GammaM1

Value > 0

13 = GammaM2

      Value
> 0

14 = Ignore seismic code

0 = No

Any other value = Yes

15 = Ignore special seismic
load

0 = No

Any other value = Yes

16 = Doubler plate is
plug-welded

0 = No

Any other value = Yes

17 = Consider deflection

0 = No

Any other value = Yes

18 = DL deflection limit,
L/Value

Value > 0

19 = SDL + LL deflection
limit, L/Value

  Value >
0

20 = LL deflection limit,
L/Value

  Value >
0

21 = Total deflection
limit, L/Value

  Value >
0

22 = Total camber limit,
L/Value

  Value >
0

23 = Pattern live load
factor

  Value >=
0

24 = Demand/capacity ratio
limit

  Value >
0

## Remarks

This function retrieves the value of a steel design
preference item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemEurocode\_3\_2005()
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

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Eurocode
3-2005")

   'get preference item
      ret = SapModel.DesignSteel.EUROCODE\_3\_2005.GetPreference(4,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.0.0.

Fixed typographical error in version 14.1.0.

Added Reliability Class parameter and added Sweden,
Finland, and Denmark as Country parameters in version 14.2.2.

Added Portugal and Germany as Country parameters in
SAP2000 Version 15.0.0.

Changed Time history design item to Multi-response case
design and added additional values in version 15.0.1.

Included all parameters and all framing types as in
Preference form in SAP2000 Version 22.1.0

The function is DEPRECATED as of version 25.1. Please
use [Get
Preferences](../Design/Steel/EN_1993_1_1_2005_(Formerly_Eurocode_3-2005)/GetPreference_{Steel_EN_1993-1-1_2005}.htm) . This topic is maintained for reference.

## See Also

[SetPreference](SetPreference_{Steel_Eurocode_3_2005}.htm)



## GetProp {Solid}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetProp_{Solid}.htm`*

# GetProp (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropSolid.GetProp

## VB6 Procedure

Function GetProp(ByVal Name As String, ByRef MatProp As String, ByRef a As Double, ByRef B As Double, ByRef c As Double, ByRef Incompatible As Boolean, ByRef Color As Long, ByRef Notes As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing solid property.

MatProp

The name of the material property assigned to the solid property.

a

The material angle A. [deg]

b

The material angle B. [deg]

c

The material angle C. [deg]

Incompatible

If this item is True, incompatible bending modes are included in the stiffness formulation. In general, incompatible modes significantly improve the bending behavior of the object.

Color

The display color assigned to the property.

Notes

The notes, if any, assigned to the property.

GUID

The GUID (global unique identifier), if any, assigned to the property.

## Remarks

This function retrieves solid property definition data.

The function returns zero if the property data is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidProperty()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MatProp As String
      Dim a As Double
      Dim b As Double
      Dim c As Double
      Dim Incompatible As Boolean
      Dim Color As Long
      Dim Notes As String
      Dim GUID As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewSolidBlock(20, 50, 20)

   'get solid property data
      ret = SapModel.PropSolid.GetProp("SOLID1", MatProp, a, b, c, Incompatible, Color, Notes, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

The function is obsolete and has been superseded by [GetProp\_1](../Definitions/Properties/Solid/GetProp_1_{Solid}.htm) as of version 26.40. This function is maintained for backward compatibility, but the parameter Incompatible is no longer applicable and will always be returned as false.

## See Also

[SetProp\_1](../Definitions/Properties/Solid/SetProp_1_{Solid}.htm)

[GetProp\_1](../Definitions/Properties/Solid/GetProp_1_{Solid}.htm)



## GetShell

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetShell.htm`*

# GetShell (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropArea.GetShell

## VB6 Procedure

Function GetShell(ByVal Name As String, ByRef ShellType As Long, ByRef MatProp As String, ByRef MatAng As Double, ByRef Thickness As Double, ByRef Bending As Double, ByRef Color As Long, ByRef Notes As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing shell-type area property.

ShellType

This is 1, 2, 3, 4, 5 or 6, indicating the shell type.

1 = Shell - thin

2 = Shell - thick

3 = Plate - thin

4 = Plate - thick

5 = Membrane

6 = Shell layered/nonlinear

MatProp

The name of the material property for the area property. This item does not apply when ShellType = 6.

MatAng

The material angle. [deg]

This item does not apply when ShellType = 6.

Thickness

The membrane thickness. [L]

This item does not apply when ShellType = 6.

Bending

The bending thickness. [L]

This item does not apply when ShellType = 6.

Color

The display color assigned to the property.

Notes

The notes, if any, assigned to the property.

GUID

The GUID (global unique identifier), if any, assigned to the property.

## Remarks

This function retrieves area property data for a shell-type area section.

The function returns zero if the property data is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaPropShell()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ShellType As Long
      Dim MatProp As String
      Dim MatAng As Double
      Dim Thickness As Double
      Dim Bending As Double
      Dim Color As Long
      Dim Notes As String
      Dim GUID As String

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'set new area property
      ret = SapModel.PropArea.SetShell("A1", 1, "4000Psi", 0, 16, 16)

   'get area property data
      ret = SapModel.PropArea.GetShell("A1", ShellType, MatProp, MatAng, Thickness, Bending, Color, Notes, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

The function is obsolete and has been superseded by [GetShell\_1](../definitions/properties/area/GetShell_1.htm) as of version 14.00. This function is maintained for backward compatibility. New function added

## See Also

[SetShell](SetShell.htm)



## GetShellLayer

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetShellLayer.htm`*

# GetShellLayer (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropArea.GetShellLayer

## VB6 Procedure

Function GetShellLayer(ByVal Name As String, ByRef MatProp As String, ByRef SteelLayoutOption As Long, ByRef DesignCoverTopDir1 As Double, ByRef DesignCoverTopDir2 As Double, ByRef DesignCoverBotDir1 As Double, ByRef DesignCoverBotDir2 As Double) As Long

## Parameters

Name

The name of an existing shell-type area property that is specified to be a layered shell property.

NumberLayers

The number of layers in the area property.

LayerName

This is an array that includes the name of each layer.

Dist

This is an array that includes the distance from the area reference surface (area object joint location plus offsets) to the midheight of the layer. [L]

Thickness

This is an array that includes the thickness of each layer. [L]

MatProp

This is an array that includes the name of the material property for the layer.

NonLinear

This is an array that includes a boolean (True or False) value. If this item is True, and if the material property assigned to the layer is nonlinear, the layer will behave nonlinearly in a nonlinear load case. If this item is False, the layer will never behave nonlinearly.

MatAng

This is an array that includes the material angle for the layer. [deg]

NumIntegrationPts

The number of integration points in the thickness direction for the layer. The locations are determined by the program using standard Guass-quadrature rules.

## Remarks

This function retrieves area property layer parameters for a shell-type area section.

The function returns zero if the parameters are successfully retrieved; otherwise it returns a nonzero value.

The function returns an error if the specified area property is not a shell-type property specified to be a layered shell.

## VBA Example

Sub GetAreaPropShellLayer()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim MyNumberLayers As Long
      Dim MyLayerName() As String
      Dim MyDist() As Double
      Dim MyThickness() As Double
      Dim MyMatProp() As String
      Dim MyNonLinear() As Boolean
      Dim MyMatAng() As Double
      Dim MyNumIntegrationPts() As Long
      Dim NumberLayers As Long
      Dim LayerName() As String
      Dim Dist() As Double
      Dim Thickness() As Double
      Dim MatProp() As String
      Dim NonLinear() As Boolean
      Dim MatAng() As Double
      Dim NumIntegrationPts() As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'set new area property
      ret = SapModel.PropArea.SetShell("A1", 6, "", 0, 0, 0)

   'add A615Gr60 rebar material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_REBAR, , , , , MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr60)

   'set area property layer parameters
      MyNumberLayers = 5
      ReDim MyLayerName(MyNumberLayers - 1)
      ReDim MyDist(MyNumberLayers - 1)
      ReDim MyThickness(MyNumberLayers - 1)
      ReDim MyMatProp(MyNumberLayers - 1)
      ReDim MyNonLinear(MyNumberLayers - 1)
      ReDim MyMatAng(MyNumberLayers - 1)
      ReDim MyNumIntegrationPts(MyNumberLayers - 1)

      MyLayerName(0) = "Concrete"
      MyDist(0) = 0
      MyThickness(0) = 16
      MyMatProp(0) = "4000Psi"
      MyNonLinear(0) = False
      MyMatAng(0) = 0
      MyNumIntegrationPts(0) = 2

      MyLayerName(1) = "Top Bar 1"
      MyDist(1) = 6
      MyThickness(1) = 0.03
      MyMatProp(1) = Name
      MyNonLinear(1) = False
      MyMatAng(1) = 0
      MyNumIntegrationPts(1) = 1

      MyLayerName(2) = "Top Bar 2"
      MyDist(2) = 6
      MyThickness(2) = 0.03
      MyMatProp(2) = Name
      MyNonLinear(2) = False
      MyMatAng(2) = 90
      MyNumIntegrationPts(2) = 1

      MyLayerName(3) = "Bot Bar 1"
      MyDist(3) = -6
      MyThickness(3) = 0.03
      MyMatProp(3) = Name
      MyNonLinear(3) = False
      MyMatAng(3) = 0
      MyNumIntegrationPts(3) = 1

      MyLayerName(4) = "Bot Bar 2"
      MyDist(4) = -6
      MyThickness(4) = 0.03
      MyMatProp(4) = Name
      MyNonLinear(4) = False
      MyMatAng(4) = 90
      MyNumIntegrationPts(4) = 1

      ret = SapModel.PropArea.SetShellLayer("A1", MyNumberLayers, MyLayerName, MyDist, MyThickness, MyMatProp, MyNonLinear, MyMatAng, MyNumIntegrationPts)

   'get area property layer parameters
      ret = SapModel.PropArea.GetShellLayer("A1", NumberLayers, LayerName, Dist, Thickness, MatProp, NonLinear, MatAng, NumIntegrationPts)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

This function is obsolete and has been superseded by [GetShellLayer\_1](../Definitions/Properties/Area/GetShellLayer_1.htm) as of version 12.5. This function is maintained for backwards compatibility.

## See Also

[SetShellLayer](SetShellLayer.htm)

[SetShellLayer\_1](../Definitions/Properties/Area/SetShellLayer_1.htm)



## GetSolverOption

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetSolverOption.htm`*

# GetSolverOption (Note:  Newer function available)

## Syntax

SapObject.SapModel.Analyze.GetSolverOption

## VB6 Procedure

Function GetSolverOption(ByRef SolverType As Long, ByRef Force32BitSolver As Boolean, ByRef StiffCase As String) As Long

## Parameters

SolverType

This is 0 or 1, indicating the solver type.

0 = Standard solver

1 = Advanced solver

Force32BitSolver

This is True if the analysis is always run using 32-bit, even on 64-bit computers.

StiffCase

The name of the load case used when outputting the mass and stiffness matrices to text files If this item is blank, no matrices are output.

## Remarks

This function retrieves the model solver options.

The function returns zero if the options are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetModelSolverOption()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim SolverType As Long
      Dim Force32BitSolver As Boolean
      Dim StiffCase As String

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set model solver options
      ret = SapModel.Analyze.GetSolverOption(SolverType, Force32BitSolver, StiffCase)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

This function is obsolete and has been superseded by [GetSolverOption\_1](GetSolverOption_1.htm) as of version 14.2.2. This function is maintained for backwards compatibility.

## See Also

[SetSolverOption](SetSolverOption.htm)



## GetSolverOption_1

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetSolverOption_1.htm`*

# GetSolverOption\_1 (Note:  Newer function available)

## Syntax

SapObject.SapModel.Analyze.GetSolverOption

## VB6 Procedure

Function GetSolverOption(ByRef SolverType As Long, ByRef
SolverProcessType As Long , ByRef Force32BitSolver As Boolean, ByRef StiffCase
As String) As Long

## Parameters

SolverType

This is 0, 1 or 2, indicating the solver type.

0 = Standard solver

1 = Advanced solver

2
= Multi-threaded solver

SolverProcessType

This is 0, 1 or 2, indicating the process the analysis
is run.

0 = Auto (program determined)

1 = GUI process

2
= Separate process

Force32BitSolver

This is True if the analysis is always run using 32-bit,
even on 64-bit computers.

StiffCase

The name of the load case used when outputting the mass
and stiffness matrices to text files. If this item is blank, no matrices
are output.

## Remarks

This function retrieves the model solver options.

The function returns zero if the options are successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetModelSolverOption()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim SolverType As Long
      Dim SolverProcessType As Long
      Dim Force32BitSolver As Boolean
      Dim StiffCase As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set model solver options
      ret = SapModel.Analyze.GetSolverOption\_1(SolverType,
SolverProcessType , Force32BitSolver, StiffCase)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.2.2.

This function superseded [GetSolverOption.](GetSolverOption.htm)

This function is obsolete and has been superseded by
[GetSolverOption\_2](NEW_-_Analyze.GetSolverOption_2.htm)
as of version 21.1.0. This function is maintained for backwards compatibility.

## See Also

[SetSolverOption\_1](SetSolverOption_1.htm)



## GetStageData

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetStageData.htm`*

# GetStageData  (Note:  Newer Function Available)

## Syntax

SapObject.SapModel.LoadCases.StaticNonlinear.GetStageData

## VB6 Procedure

Function GetStageData(ByVal Name As String, ByVal Stage As Long, ByRef NumberOperations As Long, ByRef Operation() As Long, ByRef GroupName() As String, ByRef Age() As Long, ByRef LoadType() As String, ByRef LoadName() As String, ByRef SF() As Double) As Long

## Parameters

Name

The name of an existing static nonlinear staged analysis case.

Stage

The stage in the specified load case for which data is requested. Stages are numbered sequentially starting from 1.

NumberOperations

The number of operations in the specified stage.

Operation

This is an array that includes 1, 2, 3 or 4, indicating an operation type.

1 = Add structure

2 = Remove structure

3 = Load added items in group

4 = Load all items in group

GroupName

This is an array that includes the name of the group associated with the specified operation.

Age

This is an array that includes the age of the added structure, at the time it is added, in days. This item applies only to operations with Operation = 1.

LoadType

This is an array that includes either Load or Accel, indicating the load type of an added load. This item applies only to operations with Operation = 3 or 4.

LoadName

This is an array that includes the name of the load assigned to the operation. This item applies only to operations with Operation = 3 or 4.

If the associated LoadType item is Load, this item is the name of a defined load pattern.

If the associated LoadType item is Accel, this item is UX, UY, UZ, RX, RY or RZ, indicating the direction of the load.

SF

This is an array that includes the scale factor for the load assigned to the operation. [L/s2] for Accel UX UY and UZ; otherwise unitless

This item applies only to operations with Operation = 3 or 4.

## Remarks

This function retrieves stage data for the specified stage in the specified load case.

The function returns zero if the data is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetCaseStaticNonlinearStagedStageData()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyDuration() As Long
      Dim MyComment() As String
      Dim MyOperation() As Long
      Dim MyGroupName() As String
      Dim MyAge() As Long
      Dim MyLoadType() As String
      Dim MyLoadName() As String
      Dim MySF() As Double
      Dim NumberOperations As Long
      Dim Operation() As Long
      Dim GroupName() As String
      Dim Age() As Long
      Dim LoadType() As String
      Dim LoadName() As String
      Dim SF() As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add static nonlinear staged load case
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetCase("LCASE1")

   'initialize stage definitions
      ReDim MyDuration(1)
      ReDim MyComment(1)
      MyDuration(0) = 0
      MyComment(0) = "Build structure"
      MyDuration(1) = 60
      MyComment(1) = "Wait"
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageDefinitions("LCASE1", 2, MyDuration, MyComment)

   'set stage data
      ReDim MyOperation(1)
      ReDim MyGroupName(1)
      ReDim MyAge(1)
      ReDim MyLoadType(1)
      ReDim MyLoadName(1)
      ReDim MySF(1)
      MyOperation(0) = 1
      MyGroupName(0) = "ALL"
      MyAge(0) = 3
      MyOperation(1) = 4
      MyGroupName(1) = "ALL"
      MyLoadType(1) = "Load"
      MyLoadName(1) = "DEAD"
      MySF(1) = 0.85
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageData("LCASE1", 1, 2, MyOperation, MyGroupName, MyAge, MyLoadType, MyLoadName, MySF)

   'get stage data
      ret = SapModel.LoadCases.StaticNonlinearStaged.GetStageData("LCASE1", 1, NumberOperations, Operation, GroupName, Age, LoadType, LoadName, SF)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

This function is obsolete and has been replaced by [GetStageData\_1](GetStageData_1.htm) as of version 12.00. This function is maintained for backward compatibility.

## See Also

[SetStageData\_1](SetStageData_1.htm)



## GetStageData_1

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetStageData_1.htm`*

# GetStageData\_1 (Note: Newer Function Available)

## Syntax

SapObject.SapModel.LoadCases.StaticNonlinear.GetStageData\_1

## VB6 Procedure

Function GetStageData\_1(ByVal Name As String, ByVal Stage As Long, ByRef NumberOperations As Long, ByRef Operation() As Long, ByRef ObjectType() As String, ByRef ObjectName() As String, ByRef Age() As Long, ByRef MyType() As String, ByRef MyName() As String, ByRef SF() As Double) As Long

## Parameters

Name

The name of an existing static nonlinear staged load case.

Stage

The stage in the specified load case for which data is requested. Stages are numbered sequentially starting from 1.

NumberOperations

The number of operations in the specified stage.

Operation

This is an array that includes 1, 2, 3, 4, 5, 6, 7, or 11, indicating an operation type.

1 = Add structure

2 = Remove structure

3 = Load objects if new

4 = Load objects

5 = Change section properties

6 = Change section property modifiers

7 = Change releases

11 = Change section properties and age

ObjectType

This is an array that includes the object type associated with the specified operation. The object type may be one of the following:

Group

Frame

Cable

Tendon

Area

Solid

Link

Point

The following list shows which object types are applicable to each operation type:

Operation = 1 (Add structure):  All object types

Operation = 2 (Remove structure):  All object types

Operation = 3 (Load objects if new):  All object types

Operation = 4 (Load objects):  All object types

Operation = 5 (Change section properties):  All object types except Point

Operation = 6 (Change section property modifiers):  Group, Frame, Cable, Area

Operation = 7 (Change releases):  Group, Frame

Operation = 11 (Change section properties and age): All object types except Point

ObjectName

This is an array that includes the name of the object associated with the specified operation. This is the name of a Group, Frame object, Cable object, Tendon object, Area object, Solid object, Link object or Point object, depending on the ObjectType item.

Age

This is an array that includes the age of the added structure, at the time it is added, in days. This item applies only to operations with Operation = 1.

MyType

This is an array that includes a load type or an object type, depending on what is specified for the Operation item. This item applies only to operations with Operation = 3, 4, 5, 6, 7, or 11.

When Operation = 3 or 4, this is an array that includes Load or Accel, indicating the load type of an added load.

When Operation = 5 or 11, and the ObjectType item is Group, this is an array that includes Frame, Cable, Tendon, Area, Solid or Link, indicating the object type for which the section property is changed.

When Operation = 6 and the ObjectType item is Group, this is an array that includes Frame, Cable or Area, indicating the object type for which the section property modifiers are changed.

When Operation = 7 and the ObjectType item is Group, this is an array that includes Frame, indicating the object type for which the releases are changed.

When Operation = 5, 6, 7, or 11, and the ObjectType item is not Group and not Point, this item is ignored and the type is picked up from the ObjectType item.

MyName

This is an array that includes a load assignment or an object name, depending on what is specified for the Operation item. This item applies only to operations with Operation = 3, 4, 5, 6, 7, or 11.

When Operation = 3 or 4, this is an array that includes the name of the load assigned to the operation. If the associated LoadType item is Load, this item is the name of a defined load pattern. If the associated LoadType item is Accel , this item is UX, UY, UZ, RX, RY or RZ, indicating the direction of the load.

When Operation = 5 or 11, this is the name of a Frame, Cable, Tendon, Area, Solid or Link object, depending on the object type specified.

When Operation = 6, this is the name of a Frame, Cable or Area object, depending on the object type specified.

When Operation = 7, this is the name of a Frame object.

SF

This is an array that includes the scale factor for the load assigned to the operation, if any. [L/s2] for Accel UX UY and UZ; otherwise unitless

This item applies only to operations with Operation = 3 or 4.

## Remarks

This function retrieves stage data for the specified stage in the specified load case.

The function returns zero if the data is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetCaseStaticNonlinearStagedStageData\_1()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyDuration() As Long
      Dim MyOutput() As Boolean
      Dim MyOutputName() As String
      Dim MyComment() As String
      Dim MyOperation() As Long
      Dim MyObjectType() As String
      Dim MyObjectName() As String
      Dim MyAge() As Long
      Dim MyMyType() As String
      Dim MyMyName() As String
      Dim MySF() As Double
      Dim NumberOperations As Long
      Dim Operation() As Long
      Dim ObjectType() As String
      Dim ObjectName() As String
      Dim Age() As Long
      Dim MyType() As String
      Dim MyName() As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add static nonlinear staged load case
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetCase("ACASE1")

   'initialize stage definitions
      ReDim MyDuration(1)
      ReDim MyOutput(1)
      ReDim MyOutputName(1)
      ReDim MyComment(1)
      MyDuration(0) = 0
      MyOutput(0) = False
      MyComment(0) = "Build structure"
      MyDuration(1) = 60
      MyOutput(1) = True
      MyOutputName(1) = "HBC2"
      MyComment(1) = "Wait"
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageDefinitions\_1("ACASE1", 2, MyDuration, MyOutput, MyOutputName, MyComment)

   'set stage data
      ReDim MyOperation(1)
      ReDim MyObjectType(1)
      ReDim MyObjectName(1)
      ReDim MyAge(1)
      ReDim MyMyType(1)
      ReDim MyMyName(1)
      ReDim MySF(1)
      MyOperation(0) = 1
      MyObjectType(0) = "Group"
      MyObjectName(0) = "ALL"
      MyAge(0) = 3
      MyOperation(1) = 4
      MyObjectType(1) = "Frame"
      MyObjectName(1) = "8"
      MyMyType(1) = "Load"
      MyMyName(1) = "DEAD"
      MySF(1) = 0.85
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageData\_1("ACASE1", 1, 2, MyOperation, MyObjectType, MyObjectName, MyAge, MyMyType, MyMyName, MySF)

   'get stage data
      ret = SapModel.LoadCases.StaticNonlinearStaged.GetStageData\_1("ACASE1", 1, NumberOperations, Operation, ObjectType, ObjectName, Age, MyType, MyName, SF)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

Added Operation 11 (Change section properties and age) in version 16.10.

This function supersedes [GetStageData](GetStageData.htm).

This function is obsolete and has been replaced by [GetStageData\_2](../Definitions/Load_Case/Staged/GetStageData_2.htm) as of v19.0.0. This function is maintained for backward compatibility

## See Also

[SetStageData\_1](SetStageData_1.htm)



## GetStageDefinitions

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetStageDefinitions.htm`*

# GetStageDefinitions  (Note:  Newer Function Available)

## Syntax

SapObject.SapModel.LoadCases.StaticNonlinear.GetStageDefinitions

## VB6 Procedure

Function GetStageDefinitions(ByVal Name As String, ByRef NumberStages As Long, ByRef Duration() As Long, ByRef Comment() As String) As Long

## Parameters

Name

The name of an existing static nonlinear staged analysis case.

NumberStages

The number of stages defined for the specified analysis case.

Duration

This is an array that includes the duration in days for each stage.

Comment

This is an array that includes a comment for each stage. The comment may be a blank string.

## Remarks

This function retrieves the stage definition data for the specified load case.

The function returns zero if the data is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetCaseStaticNonlinearStagedStageDefinitions()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyDuration() As Long
      Dim MyComment() As String
      Dim NumberStages As Long
      Dim Duration() As Long
      Dim Comment() As String

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add static nonlinear staged load case
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetCase("LCASE1")

   'initialize stage definitions
      ReDim MyDuration(1)
      ReDim MyComment(1)
      MyDuration(0) = 0
      MyComment(0) = "Build structure"
      MyDuration(1) = 60
      MyComment(1) = "Wait"
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageDefinitions("LCASE1", 2, MyDuration, MyComment)

   'get stage definitions
      ret = SapModel.LoadCases.StaticNonlinearStaged.GetStageDefinitions("LCASE1", NumberStages, Duration, Comment)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

This function is obsolete and has been superseded by [GetStageDefinitions\_1](GetStageDefinitions_1.htm) as of version 12.00. This function is maintained for backwards compatibility.

## See Also

[SetStageDefinitions](SetStageDefinitions.htm)



## GetStageDefinitions_1

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetStageDefinitions_1.htm`*

# GetStageDefinitions\_1  (Note: Newer Function Available)

## Syntax

SapObject.SapModel.LoadCases.StaticNonlinear.GetStageDefinitions\_1

## VB6 Procedure

Function GetStageDefinitions\_1(ByVal Name As String, ByRef NumberStages As Long, ByRef Duration() As Long, ByRef Output() As Boolean, ByRef OutputName() As String, ByRef Comment() As String) As Long

## Parameters

Name

The name of an existing static nonlinear staged load case.

NumberStages

The number of stages defined for the specified load case.

Duration

This is an array that includes the duration in days for each stage.

Output

This is an array that includes True or False, indicating if analysis output is to be saved for each stage.

OutputName

This is an array that includes a user-specified output name for each stage.

Comment

This is an array that includes a comment for each stage. The comment may be a blank string.

## Remarks

This function retrieves the stage definition data for the specified load case.

The function returns zero if the data is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetCaseStaticNonlinearStagedStageDefinitions\_1()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyDuration() As Long
      Dim MyOutput() As Boolean
      Dim MyOutputName() As String
      Dim MyComment() As String
      Dim NumberStages As Long
      Dim Duration() As Long
      Dim Output() As Boolean
      Dim OutputName() As String
      Dim Comment() As String

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

   'add static nonlinear staged load case
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetCase("ACASE1")

   'initialize stage definitions
      ReDim MyDuration(1)
      ReDim MyOutput(1)
      ReDim MyOutputName(1)
      ReDim MyComment(1)
      MyDuration(0) = 0
      MyOutput(0) = False
      MyComment(0) = "Build structure"
      MyDuration(1) = 60
      MyOutput(1) = True
      MyOutputName(1) = "HBC2"
      MyComment(1) = "Wait"
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageDefinitions\_1("ACASE1", 2, MyDuration, MyOutput, MyOutputName, MyComment)

   'get stage definitions
      ret = SapModel.LoadCases.StaticNonlinearStaged.GetStageDefinitions\_1("ACASE1", NumberStages, Duration, Output, OutputName, Comment)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

This function supersedes [GetStageDefinitions](GetStageDefinitions.htm)

This function is obsolete and has been replaced by [GetStageDefinitions\_2](../Definitions/Load_Case/Staged/GetStageDefinitions_2.htm) as of v19.0.0. This function is maintained for backward compatibility.

## See Also

[SetStageDefinitions\_1](SetStageDefinitions_1.htm)



## GetTee {Frame}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetTee_{Frame}_old.htm`*

# GetTee (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropFrame.GetTee

## VB6 Procedure

Function GetTee(ByVal Name As String, ByRef FileName
As String, ByRef MatProp As String, ByRef t3 As Double, ByRef t2 As Double,
ByRef tf As Double, ByRef tw As Double, ByRef Color As Long, ByRef Notes
As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing frame section property.

FileName

If the section property was imported from a property
file, this is the name of that file. If the section property was not imported,
this item is blank.

MatProp

The name of the material property for the section.

t3

The section depth. [L]

t2

The flange width. [L]

tf

The flange thickness. [L]

tw

The web thickness. [L]

Color

The display color assigned to the section.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section.

## Remarks

This function retrieves frame section property data
for a tee-type frame section.

The function returns zero if the section property data
is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePropTee()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim FileName As String
      Dim MatProp As String
      Dim t3 As Double
      Dim t2 As Double
      Dim tf As Double
      Dim tw As Double
      Dim Color As Long
      Dim Notes As String
      Dim GUID As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetTee("TEE1",
"A992Fy50", 12, 10, 0.6, 0.3)

   'get frame section property data
      ret = SapModel.PropFrame.GetTee("TEE1",
FileName, MatProp, t3, t2, tf, tw, Color, Notes, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[SetTee](../Definitions/Properties/Frame/GetTee_{Frame}.htm)

[SetRebarBeam](../Definitions/Properties/Frame/SetRebarBeam.htm)

[GetRebarBeam](../Definitions/Properties/Frame/GetRebarBeam.htm)



## GetTube {Frame}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetTube_{Frame}.htm`*

# GetTube (Note: Newer function available)

## Syntax

SapObject.SapModel.PropFrame.GetTube

## VB6 Procedure

Function GetTube(ByVal Name As String, ByRef FileName
As String, ByRef MatProp As String, ByRef t3 As Double, ByRef t2 As Double,
ByRef tf As Double, ByRef tw As Double, ByRef Color As Long, ByRef Notes
As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing frame section property.

FileName

If the section property was imported from a property
file, this is the name of that file. If the section property was not imported,
this item is blank.

MatProp

The name of the material property for the section.

t3

The section depth. [L]

t2

The section width. [L]

tf

The flange thickness. [L]

tw

The web thickness. [L]

Color

The display color assigned to the section.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section.

## Remarks

This function retrieves frame section property data
for a tube-type frame section.

The function returns zero if the section property data
is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePropTube()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim FileName As String
      Dim MatProp As String
      Dim t3 As Double
      Dim t2 As Double
      Dim tf As Double
      Dim tw As Double
      Dim Color As Long
      Dim Notes As String
      Dim GUID As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetTube("TUBE1",
"A992Fy50", 8, 6, 0.5, 0.5)

   'get frame section property data
      ret = SapModel.PropFrame.GetTube("TUBE1",
FileName, MatProp, t3, t2, tf, tw, Color, Notes, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

This function is obsolete and has been superseded by
[GetTube\_1](../Definitions/Properties/Frame/GetTube_1_{Frame}.htm)
as of version 24.2.

## See Also

[SetTube](SetTube.htm)



## GetTypeOAPI {Load Case}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/GetType_{Load_Case}.htm`*

# GetTypeOAPI   (Note:  Newer Function Available)

## Syntax

SapObject.SapModel.LoadCases.GetTypeOAPI

## VB6 Procedure

Function GetTypeOAPI(ByVal Name As String, ByRef CaseType As eLoadCaseType, ByRef SubType as long) As Long

## Parameters

Name

The name of an existing load case.

CaseType

This is one of the following items in the eLoadCaseType enumeration.

CASE\_LINEAR\_STATIC = 1

CASE\_NONLINEAR\_STATIC = 2

CASE\_MODAL = 3

CASE\_RESPONSE\_SPECTRUM = 4

CASE\_LINEAR\_HISTORY = 5  (Modal Time History)

CASE\_NONLINEAR\_HISTORY = 6  (Modal Time History)

CASE\_LINEAR\_DYNAMIC = 7  (Direct Integration Time History)

CASE\_NONLINEAR\_DYNAMIC = 8  (Direct Integration Time History)

CASE\_MOVING\_LOAD = 9

CASE\_BUCKLING = 10

CASE\_STEADY\_STATE = 11

CASE\_POWER\_SPECTRAL\_DENSITY = 12

CASE\_LINEAR\_STATIC\_MULTISTEP = 13

CASE\_HYPERSTATIC = 14

SubType

This is an integer representing the load case sub type. This item only applies for certain case types.

For CASE\_NONLINEAR\_STATIC:

1 = Nonlinear

2 = Nonlinear staged construction

For CASE\_MODAL:

1 = Eigen

2 = Ritz

For CASE\_LINEAR\_HISTORY:

1 = Transient

2 = Periodic

## Remarks

This function retrieves the case type for the specified load case.

The function returns zero if the type is successfully retrieved; otherwise it returns nonzero.

## VBA Example

Sub GetLoadCaseType()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim CaseType As eLoadCaseType
      Dim SubType As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'get load case type
      ret = SapModel.LoadCases.GetTypeOAPI("DEAD", CaseType, SubType)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

Added one item to the eLoadCaseType enumeration in version 12.00.

This function is obsolete and has been superseded by [GetType\_1](../definitions/load_case/GetType_1_{Load_Case}.htm) as of version 12.00. This function is maintained for backwards compatibility.

Changed function name to GetTypeOAPI in v17.0.0.

## See Also



## GetSolverOption_2

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/NEW_-_Analyze.GetSolverOption_2.htm`*

# **GetSolverOption\_2** (Note:  Newer function available)

## **Syntax**

SapObject.SapModel.Analyze.GetSolverOption\_2

## **VB6 Procedure**

Function GetSolverOption\_2(ByRef SolverType As Long,
ByRef SolverProcessType As Long, ByRef NumberParallelRuns As Long, ByRef
StiffCase As String) As Long

## **Parameters**

**SolverType**

This is 0, 1 or 2, indicating the solver type.

0 = Standard solver
1 = Advanced solver
2 = Multi-threaded solver

**SolverProcessType**

This is 0, 1 or 2, indicating the process the analysis
is run.

0 = Auto (program determined)
1 = GUI process
2 = Separate process

**NumberParallelRuns**

This is an integer between -8 and 8, inclusive, not
including -1 or 0.

-8 to -2 = The negative
of the program determined value when the assigned value is 0
= Auto parallel (use up to all physical cores - max 8).
1 = Serial.
2 to 8 = User defined parallel (use up to this fixed number of cores -
max 8

**StiffCase**

The name of the load case used when outputting the mass
and stiffness matrices to text files. If this item is blank, no matrices
are output.

## **Remarks**

This function retrieves the model solver options.

The function returns zero if the options are successfully
retrieved; otherwise it returns a nonzero value.

## **VBA Example**

Sub GetModelSolverOption()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim SolverType As Long
      Dim SolverProcessType As Long
      Dim StiffCase As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set model solver options
      ret = SapModel.Analyze.GetSolverOption\_2(SolverType,
SolverProcessType, NumberParallelRuns, StiffCase)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## **Release Notes**

Initial release in v21.1.0.

Modified the allowed values for NumberParallelRuns in
v 22.1.0.

This function is obsolete and has been superseded by
[GetSolverOption\_3](../Analyze/Analyze.GetSolverOption_3.htm)
as of version 23.2.0. This function is maintained for backwards compatibility.

This function supersedes [GetSolverOption\_1](GetSolverOption_1.htm),
adding the NumberParallelRuns parameter and removing the previous Force32BitSolver
parameter

## **See Also**

[SetSolverOption\_2](NEW_-_Analyze.SetSolverOption_2.htm)



## SetSolverOption_2

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/NEW_-_Analyze.SetSolverOption_2.htm`*

# **SetSolverOption\_2** (Note:  Newer function available)

## **Syntax**

SapObject.SapModel.Analyze.SetSolverOption\_2

## **VB6 Procedure**

Function SetSolverOption\_2(ByVal SolverType As Long,
ByVal SolverProcessType As Long, ByVal NumberParallelRuns As Long, Optional
ByVal StiffCase As String = "") As Long

## **Parameters**

**SolverType**

This is 0, 1 or 2, indicating the solver type.

0 = Standard
solver
1 = Advanced solver
2 = Multi-threaded solver

**SolverProcessType**

This is 0, 1 or 2, indicating the process the analysis
is run.

0 = Auto
(program determined)
1 = GUI process
2 = Separate process

**NumberParallelRuns**

This is an integer between -8 and 8, inclusive, not
including -1.

            -8
to -2 = Auto parallel (use up to all physical cores - max 8). Treated
the same as 0.
            -1
= Illegal value; will return an error.
            0
= Auto parallel (use up to all physical cores).
            1
= Serial.
            2
to 8 = User defined parallel (use up to this fixed number of cores -
max 8).

**StiffCase**

The name of the load case used when outputting the mass
and stiffness matrices to text files If this item is blank, no matrices
are output.

## **Remarks**

This function sets the model solver options.

The function returns zero if the options are successfully
set; otherwise it returns a nonzero value.

## **VBA Example**

Sub SetModelSolverOption()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New SAP2000.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set model solver options
      ret = SapModel.Analyze.SetSolverOption\_2(1,
1, 3, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## **Release Notes**

Initial release in v21.1.0.

Modified the allowed values for NumberParallelRuns in
v 22.1.0.

This function is obsolete and has been superseded by
[SetSolverOption\_3](../Analyze/Analyze.SetSolverOption_3.htm)
as of version 23.2.0. This function is maintained for backwards compatibility.

This function supersedes [SetSolverOption\_1](SetSolverOption_1.htm),
adding the NumberParallelRuns parameter and removing the previous Force32BitSolver
parameter.

## **See Also**

[GetSolverOption\_2](NEW_-_Analyze.GetSolverOption_2.htm)



## SetAPI4F2008

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetAPI4F2008.htm`*

# SetAPI4F2008 (Note:  Newer function available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.SetAPI4F2008

## VB6 Procedure

Function SetAPI4F2008(ByVal Name As String, ByVal ExposureFrom As Long, ByVal DirAngle As Double, ByVal UserZ As Boolean, ByVal TopZ As Double, ByVal BottomZ As Double, ByVal WindSpeed As Double, ByVal SSLFactor As Double) As Long

## Parameters

Name

The name of an existing Wind-type load case.

ExposureFrom

This is 2, 3 or 4, indicating the source of the wind exposure.

2 = From area objects

3 = From frame objects (open structure)

4 = From area objects and frame objects (open structure)

DirAngle

The direction angle for the wind load.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

WindSpeed

The design reference wind velocity, Vref, in knots.

SSLFactor

The structural safety level multiplier.

## Remarks

This function assigns auto wind loading parameters for API 4F 2008.

The function returns zero if the parameters are successfully assigned; otherwise, it returns a nonzero value.

## VBA Example

Sub AssignWindAPI4F20085()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'add new load case
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WIND)

   'assign API 4F 2008 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetAPI4F2008("WIND", 3, 0, False, 0, 0, 93, 1.1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

The function is obsolete and has been superseded by [SetAPI4F2008\_1](../Definitions/Load_Pattern/Auto_Wind_Load/SetAPI4F2008_1.htm) as of version 14.1.0. This function is maintained for backward compatibility. New function added.

## See Also

[GetAPI4F2008](GetAPI4F2008.htm)



## SetASCE16 {Auto Seismic}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetASCE16_{Auto_Seismic}-obsolete.htm`*

# SetASCE716 (Note:  Obsolete Function, Newer Function Available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoSeismic.SetASCE716

## VB6 Procedure

Function SetASCE716(ByVal Name As String, ByRef nDir() As Boolean, ByRef Eccen As Double, ByRef PeriodFlag As Long, ByRef CtType As Long, ByRef UserT As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef R As Double, ByRef Omega As Double, ByRef Cd As Double, ByRef I As Double, ByRef Ss As Double, ByRef S1 As Double, ByRef TL As Double, ByRef SiteClass As Long, ByRef Fa As Double, ByRef Fv As Double) As Long

## Parameters

Name

The name of an existing Quake-type load pattern.

nDir

This is an array with 2 inputs that indicate the seismic load direction.

nDir(1) = True = Global X

nDir(2) = True = Global Y

If nDir(1) and nDir(2) are both True or False, the default direction in Global X will be assigned.

Eccen

The eccentricity ratio that applies to all diaphragms.

PeriodFlag

This is 1, 2 or 3, indicating the time period option.

1 = Approximate

2 = Program calculated

3 = User defined

CtType

This is 0, 1, 2 or 3, indicating the values of Ct and x. This item applies when the PeriodFlag item is 1 or 2.

0 = Ct = 0.028 (ft),     x = 0.8

1 = Ct = 0.016 (ft),     x = 0.9

2 = Ct = 0.03 (ft),      x = 0.75

3 = Ct = 0.02 (ft),      x = 0.75

UserT

The user specified time period. This item applies when the PeriodFlag item is 3. [s]

UserZ

This item is True if the top and bottom elevations of the seismic load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto seismic loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto seismic loads are applied. [L]

R

The response modification factor.

Omega

The system overstrength factor.

Cd

The deflection amplification factor.

I

The occupancy importance factor.

SS, S1

The seismic coefficients Ss and S1. This item is used only when ASCE716Option = 2.

TL

The long-period transition period. [s]

SiteClass

This is 1, 2, 3, 4, 5 or 6, indicating the site class.

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

Fa, Fv

The site coefficients Fa and Fv. These items are used only when ASCE716SiteClass is 5 or 6.

## Remarks

This function assigns auto seismic loading parameters for the 2016 ASCE 7 code.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSeismicASCE716()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim nDir() As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(e3DFrameType.BeamSlab, 2, 144, 3, 336, 2, 432 )

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("EQX", eLoadPatternType.Quake)

   'dimension ASCE716 parameters

        Dim nDir() As Boolean

        Dim Eccen As Double

        Dim PeriodFlag As Long

        Dim CtType As Long

        Dim UserT As Double

        Dim UserZ As Boolean

        Dim TopZ As Double

        Dim BottomZ As Double

        Dim R As Double

        Dim Omega As Double

        Dim Cd As Double

        Dim I As Double

        Dim SS As Double

        Dim S1 As Double

        Dim TL As Double

        Dim SiteClass As Long

        Dim Fa As Double

        Dim Fv As Double

        ReDim nDir(2)

        nDir(1) = True

        TopZ = 32

        BottomZ = 14

   'set ASCE716 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetASCE716("EQX", nDir, 0.04, 3, 1, 1.76, True, TopZ, BottomZ, 6, 3.5, 6.5, 1.5, 1.9, 1.1, 8, 3, 0, 0)

   'get ASCE716 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.GetASCE716("EQX", nDir, Eccen, PeriodFlag, CtType, UserT, UserZ, TopZ, BottomZ, R, Omega, Cd, I, SS, S1, TL, SiteClass, Fa, Fv)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.2.0.

This function was replaced by [SetASCE716\_1](../Definitions/Load_Pattern/Auto_Seismic_Load/SetASCE16_{Auto_Seismic}.htm), which is more consistent with other API functions.

## See Also

[GetASCE716](GetASCE_16_{Auto_Seismic}-obsolete.htm)



## SetAngle {Frame}_old

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetAngle_{Frame}_old.htm`*

# SetAngle (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropFrame.SetAngle

## VB6 Procedure

Function SetAngle(ByVal Name As String, ByVal MatProp
As String, ByVal t3 As Double, ByVal t2 As Double, ByVal tf As Double,
ByVal tw As Double, Optional ByVal Color As Long = -1, Optional ByVal
Notes As String = "", Optional ByVal GUID As String = "")
As Long

## Parameters

Name

The name of an existing or new frame section property.
If this is an existing property, that property is modified; otherwise,
a new property is added.

MatProp

The name of the material property for the section.

t3

The vertical leg depth. [L]

t2

The horizontal leg width. [L]

tf

The horizontal leg thickness. [L]

tw

The vertical leg thickness. [L]

Color

The display color assigned to the section. If Color
is specified as -1, the program will automatically assign a color.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section. If this item is input as Default, then the program assigns
a GUID to the section.

## Remarks

This function initializes an angle-type frame section
property. If this function is called for an existing frame section property,
all items for the section are reset to their default value.

The function returns zero if the section property is
successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetFramePropAngle()
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
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetAngle("ANGLE1",
"A992Fy50", 6, 4, 0.5, 0.5)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[GetAngle](../Definitions/Properties/Frame/GetAngle_{Frame}.htm)

[SetRebarBeam](../Definitions/Properties/Frame/SetRebarBeam.htm)

[GetRebarBeam](../Definitions/Properties/Frame/GetRebarBeam.htm)



## SetAutoLiveLoad {Bridge Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetAutoLiveLoad_{Bridge_Wind_Load}.htm`*

# SetAutoLiveLoad {Bridge Wind Load} (Note:  Newer function available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoWindBridge.SetAutoLiveLoad

## VB6 Procedure

Function SetAutoLiveLoad(ByVal Name As String, ByVal RefLoadPat As String, ByVal Height As Double) As Long

## Parameters

Name

The name of an existing bridge wind - live load type pattern.

RefLoadPat

The name of an existing bridge wind load pattern that is referenced from this wind on live load pattern.

Height

The height above the roadway surface at which the wind on live load should be applied. [L]

## Remarks

This function applies auto wind on live load parameters.

The function returns zero if the parameters are successfully applied; otherwise it returns a nonzero value.

## VBA Example

Sub SetAutoWindLiveLoad()
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

   'open existing model containing a bridge object
      ret = SapModel.File.OpenFile(“C:\Temp\BridgeModel.bdb” )

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WINDONLIVELOAD)

   'set auto wind live load loading type to Auto
      ret = SapModel.LoadPatterns.AutoWindBridge.SetAutoLiveLoad("WINDLIVE", "WIND", 0)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v21.0.0.

This function is obsolete and was superseded by [SetAutoLiveLoad\_1](../Definitions/Load_Pattern/Auto_Wind_Bridge/SetAutoLiveLoad_1{Bridge_Wind_Load}.htm) in release v25.2.0. This function is maintained for backwards compatibility.

## See Also

[GetAutoLiveLoad](GetAutoLiveLoad_{Bridge_Wind_Load}.htm)

[SetAutoLiveLoad\_1](../Definitions/Load_Pattern/Auto_Wind_Bridge/SetAutoLiveLoad_1{Bridge_Wind_Load}.htm)



## SetAutoMesh {Area Object}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetAutoMesh_{Area_Object}.htm`*

# SetAutoMesh (Note:  Newer function available)

## Syntax

SapObject.SapModel.AreaObj.SetAutoMesh

## VB6 Procedure

Function SetAutoMesh(ByVal Name As String, ByVal MeshType As Long, Optional ByVal n1 As Long = 2, Optional ByVal n2 As Long = 2, Optional ByVal MaxSize1 As Double = 0, Optional ByVal MaxSize2 As Double = 0, Optional ByVal PointOnEdgeFromLine As Boolean = False, Optional ByVal PointOnEdgeFromPoint As Boolean = False, Optional ByVal ExtendCookieCutLines As Boolean = False, Optional ByVal Rotation As Double = 0, Optional ByVal MaxSizeGeneral As Double = 0, Optional ByVal LocalAxesOnEdge As Boolean = False, Optional ByVal LocalAxesOnFace As Boolean = False, Optional ByVal RestraintsOnEdge As Boolean = False, Optional ByVal RestraintsOnFace As Boolean = False, Optional ByVal Group As String = "ALL", Optional ByVal SubMesh As Boolean = False, Optional ByVal SubMeshSize As Double = 0, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

MeshType

This item is 0, 1, 2, 3, 4, 5 or 6, indicating the automatic mesh type for the area object.

0 = No automatic meshing

1 = Mesh area into a specified number of objects

2 = Mesh area into objects of a specified maximum size

3 = Mesh area based on points on area edges

4 = Cookie cut mesh area based on lines intersecting edges

5 = Cookie cut mesh area based on points

6 = Mesh area using General Divide Tool

Mesh options 1, 2 and 3 apply to quadrilaterals and triangles only.

n1

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed area object that runs from point 1 to point 2.

n2

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed area object that runs from point 1 to point 3.

MaxSize1

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed area object that runs from point 1 to point 2. [L]

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

MaxSize2

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed area object that runs from point 1 to point 3. [L]

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

PointOnEdgeFromLine

This item applies when MeshType = 3. If it is True, points on the area object edges are determined from intersections of straight line objects included in the group specified by the Group item with the area object edges.

PointOnEdgeFromPoint

This item applies when MeshType = 3. If it is True, points on the area object edges are determined from point objects included in the group specified by the Group item that lie on the area object edges.

ExtendCookieCutLines

This item applies when MeshType = 4. MeshType = 4 provides cookie cut meshing based on straight line objects included in the group specified by the Group item that intersect the area object edges. If the ExtendCookieCutLines item is True, all straight line objects included in the group specified by the Group item are extended to intersect the area object edges for the purpose of meshing the area object.

Rotation

This item applies when MeshType = 5. MeshType = 5 provides cookie cut meshing based on two perpendicular lines passing through point objects included in the group specified by the Group item. By default these lines align with the area object local 1 and 2 axes. The Rotation item is an angle in degrees that the meshing lines are rotated from their default orientation. [deg]

MaxSizeGeneral

This item applies when MeshType = 6. It is the maximum size of objects created by the General Divide Tool.

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

LocalAxesOnEdge

If this item is True, and if both points along an edge of the original area object have the same local axes, then the program makes the local axes for added points along the edge the same as the edge end points.

LocalAxesOnFace

If this item is True, and if all points around the perimeter of the original area object have the same local axes, the program makes the local axes for all added points the same as the perimeter points.

RestraintsOnEdge

If this item is True, and if both points along an edge of the original area object have the same restraint/constraint, then, if the added point and the adjacent corner points have the same local axes definition, the program includes the restraint/constraint for added points along the edge.

RestraintsOnFace

If this item is True, and if all points around the perimeter of the original area object have the same restraint/constraint, then, if an added point and the perimeter points have the same local axes definition, the program includes the restraint/constraint for the added point.

Group

The name of a defined group. Some of the meshing options make use of point and line objects included in this group.

SubMesh

If this item is True, after initial meshing, the program further meshes any area objects that have an edge longer than the length specified by the SubMeshSize item.

SubMeshSize

This item applies when the SubMesh item is True. It is the maximum size of area objects to remain when the auto meshing is complete. [L]

If this item is input as 0, the default value is used. The default value is 12 inches if the database units are English or 30 centimeters if the database units are metric.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function makes automatic meshing assignments to area objects.

The function returns zero if the meshing options are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjAutoMesh()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign auto mesh options
      ret = SapModel.AreaObj.SetAutoMesh("ALL", 1, 3, 3, , , , , , , , , , , , , , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

This function is obsolete and was superseded by [SetAutoMesh\_1](../Object_Model/Area_Object/SetAutoMesh__1{Area_Object}.htm) in release v27.0.0. This function is maintained for backwards compatibility.

## See Also

[GetAutoMesh](GetAutoMesh_{Area_Object}.htm)



## SetChannel {Frame}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetChannel_{Frame}_old.htm`*

# SetChannel (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropFrame.SetChannel

## VB6 Procedure

Function SetChannel(ByVal Name As String, ByVal MatProp
As String, ByVal t3 As Double, ByVal t2 As Double, ByVal tf As Double,
ByVal tw As Double, Optional ByVal Color As Long = -1, Optional ByVal
Notes As String = "", Optional ByVal GUID As String = "")
As Long

## Parameters

Name

The name of an existing or new frame section property.
If this is an existing property, that property is modified; otherwise,
a new property is added.

MatProp

The name of the material property for the section.

t3

The section depth. [L]

t2

The flange width. [L]

tf

The flange thickness. [L]

tw

The web thickness. [L]

Color

The display color assigned to the section. If Color
is specified as -1, the program will automatically assign a color.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section. If this item is input as Default, the program assigns
a GUID to the section.

## Remarks

This function initializes a channel-type frame section
property. If this function is called for an existing frame section property,
all items for the section are reset to their default value.

The function returns zero if the section property is
successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetFramePropChannel()
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
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetChannel("CHN1",
"A992Fy50", 24, 6, 0.5, 0.3)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[GetChannel](../Definitions/Properties/Frame/GetChannel_{Frame}.htm)



## SetChinese2002_1{Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetChinese2002_1{Wind_Load}.htm`*

# SetChinese2002\_1

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.SetChinese2002\_1

## VB6 Procedure

Function SetChinese2002\_1(ByVal Name As String, ByVal ExposureFrom As Long, ByVal DirAngle As Double, ByVal BuildingWidth As Double, ByVal Us As Double, ByVal UniformTaper As Boolean, ByVal BHoverB0 As Double, ByVal UserZ As Boolean, ByVal TopZ As Double, ByVal BottomZ As Double, ByVal wzero As Double, ByVal Rt As Long, ByVal PhiZOpt As Long, ByVal T1Opt As Long, ByVal UserT As Double, ByVal DampRatio As Double, Optional ByVal UserExposure As Boolean = False) As Long

## Parameters

Name

The name of an existing Wind-type load pattern.

ExposureFrom

This is 1 or 2, indicating the source of the wind exposure.

1 = From extents of rigid diaphragms

2 = From area objects

DirAngle

The direction angle for the wind load. This item only applies when ExposureFrom = 1.

BuildingWidth

The building width. [L]

Us

The shape coefficient. This item applies only when ExposureFrom = 1.

UniformTaper

This item is True if a correction is to be applied to the wind load for a uniform taper.

BHoverB0

The taper ratio, Bh/B0. This item applies only when UniformTaper = True.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

wzero

The basic wind pressure in kN/m2.

Rt

This is 1, 2, 3 or 4, indicating the ground roughness.

1 = A

2 = B

3 = C

4 = D

PhiZOpt

This is 0 or 1, indicating the Phi Z source.

0 = Modal analysis

1 = Z/H ratio

T1Opt

This is 0 or 1, indicating the T1 source.

0 = Modal analysis

1 = User defined

UserT

This item applies only when the T1 source is user defined (T1Opt = 1). It is the user defined T1 period. [s]

DampRatio

The damping ratio.

UserExposure

If this item is True, the wind exposure widths are provided by the user. If it is False, the wind exposure widths are calculated by the program from the extents of the diaphragms.

## Remarks

This function assigns auto wind loading parameters for Chinese 2002.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignWindChinese2002\_1()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WIND)

   'assign Chinese2002\_1 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetChinese2002\_1("WIND", 1, 0, 1200, 0.5, False, 1, False, 0, 0, 0.48, 3, 1, 1, 0.6, 0.04)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.1.0.

This function supersedes [SetChinese2002 {Wind Load}](SetChinese2002_{Wind_Load}.htm)

## See Also

[GetChinese2002\_1](GetChinese2002_1{Wind_Load}.htm)



## SetChinese2002 {Auto Seismic}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetChinese2002_{Auto_Seismic}.htm`*

# SetChinese2002

## Syntax

SapObject.SapModel.LoadPatterns.AutoSeismic.SetChinese2002

## VB6 Procedure

Function SetChinese2002(ByVal Name As String, ByVal DirFlag As Long, ByVal Eccen As Double, ByVal PeriodFlag As Long, ByVal UserT As Double, ByVal UserZ As Boolean, ByVal TopZ As Double, ByVal BottomZ As Double, ByVal JGJ32002AlphaMax As Double, ByVal JGJ32002SI As Long, ByVal JGJ32002DampRatio As Double, ByVal JGJ32002Tg As Double, ByVal JGJ32002PTDF As Double, ByVal EnhancementFactor As Double) As Long

## Parameters

Name

The name of an existing Quake-type load pattern.

DirFlag

This is 1, 2 or 3, indicating the seismic load direction.

1 = Global X

2 = Global Y

3 = Global Z

Eccen

The eccentricity ratio that applies to all diaphragms.

PeriodFlag

This is either 2 or 3, indicating the time period option.

2 = Program calculated

3 = User defined

UserT

The user specified time period. This item applies when the PeriodFlag item is 3. [s]

UserZ

This item is True if the top and bottom elevations of the seismic load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto seismic loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto seismic loads are applied. [L]

JGJ32002AlphaMax

The maximum influence factor.

JGJ32002SI

This is 1, 2, 3, 4, 5 or 6, indicating the seismic intensity.

1 = 6  (0.05g)

2 = 7  (0.10g)

3 = 7  (0.15g)

4 = 8  (0.20g)

5 = 8  (0.30g)

6 = 9  (0.40g)

JGJ32002DampRatio

The damping ratio.

JGJ32002Tg

The characteristic ground period. [s]

JGJ32002PTDF

The period time discount factor.

EnhancementFactor

The enhancement factor.

## Remarks

This function assigns auto seismic loading parameters for the Chinese 2002 code.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSeismicChinese2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("EQX", LTYPE\_QUAKE)

   'assign Chinese 2002 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetChinese2002("EQX", 1, 0.05, 2, 0, False, 0, 0, 0.16, 4, 0.06, 0.4, 1, 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.01.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetChinese2002](GetChinese2002_{Auto_Seismic}.htm)



## SetChinese2002 {RS}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetChinese2002_{RS}.htm`*

# SetChinese2002

## Syntax

SapObject.SapModel.Func.FuncRS.SetChinese2002

## VB6 Procedure

Function SetChinese2002(ByVal Name As String, ByVal JGJ32002AlphaMax As Double, ByVal JGJ32002SI As Long, ByVal JGJ32002Tg As Double, ByVal JGJ32002PTDF As Double, ByVal DampRatio As Double) As Long

## Parameters

Name

The name of an existing or new function. If this is an existing function, that function is modified; otherwise, a new function is added.

JGJ32002AlphaMax

The maximum influence factor.

JGJ32002SI

This is 1, 2, 3, 4, 5 or 6, indicating the seismic intensity.

1 = 6 (0.05g)

2 = 7 (0.10g)

3 = 7 (0.15g)

4 = 8 (0.20g)

5 = 8 (0.30g)

6 = 9 (0.40g)

JGJ32002Tg

The characteristic ground period, Tg > 0.1. [s]

JGJ32002PTDF

The period time discount factor.

DampRatio

The damping ratio for the function, 0 <= DampRatio < 1.

## Remarks

This function defines a Chinese 2002 response spectrum function.

The function returns zero if the function is successfully defined; otherwise it returns a nonzero value.

## VBA Example

Sub SetRSFuncChinese2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add Chinese2002 RS function
      ret = SapModel.Func.FuncRS.SetChinese2002("RS-1", 0.18, 5, 0.36, 1, 0.04)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[GetChinese2002](GetChinese2002_{RS}.htm)



## SetChinese2002 {Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetChinese2002_{Wind_Load}.htm`*

# SetChinese2002

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.SetChinese2002

## VB6 Procedure

Function SetChinese2002(ByVal Name As String, ByVal ExposureFrom As Long, ByVal DirAngle As Double, ByVal BuildingWidth As Double, ByVal Us As Double, ByVal UserZ As Boolean, ByVal TopZ As Double, ByVal BottomZ As Double, ByVal wzero As Double, ByVal Rt As Long, ByVal PhiZOpt As Long, ByVal T1Opt As Long, ByVal UserT As Double, ByVal DampRatio As Double, Optional ByVal UserExposure As Boolean = False) As Long

## Parameters

Name

The name of an existing Wind-type load pattern.

ExposureFrom

This is either 1 or 2, indicating the source of the wind exposure.

1 = From extents of rigid diaphragms

2 = From area objects

DirAngle

The direction angle for the wind load. This item applies only when ExposureFrom = 1.

BuildingWidth

The building width. [L]

Us

The shape coefficient. This item applies only when ExposureFrom = 1.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

wzero

The basic wind pressure in kN/m2.

Rt

This is 1, 2, 3 or 4, indicating the ground roughness.

1 = A

2 = B

3 = C

4 = D

PhiZOpt

This is either 0 or 1, indicating the Phi Z source.

0 = Modal analysis

1 = Z/H ratio

T1Opt

This is either 0 or 1, indicating the T1 source.

0 = Modal analysis

1 = User defined

UserT

This item applies only when the T1 source is user defined (T1Opt = 1). It is the user defined T1 period. [s]

DampRatio

The damping ratio.

UserExposure

If this item is True, the wind exposure widths are provided by the user. If it is False, the wind exposure widths are calculated by the program from the extents of the diaphragms.

## Remarks

This function assigns auto wind loading parameters for Chinese 2002.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignWindChinese2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WIND)

   'assign Chinese2002 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetChinese2002("WIND", 1, 0, 1200, 0.5, False, 0, 0, 0.48, 3, 1, 1, 0.6, 0.04)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.01.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

The function is obsolete and has been superseded by [SetChinese2002\_1](SetChinese2002_1{Wind_Load}.htm) as of version 14.1.0. This function is maintained for backward compatibility. New function added.

## See Also

[GetChinese2002](GetChinese2002_{Wind_Load}.htm)



## SetDblAngle {Frame}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetDblAngle_{Frame}_old.htm`*

# SetDblAngle (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropFrame.SetDblAngle

## VB6 Procedure

Function SetDblAngle(ByVal Name As String, ByVal MatProp
As String, ByVal t3 As Double, ByVal t2 As Double, ByVal tf As Double,
ByVal tw As Double, ByVal dis As Double, Optional ByVal Color As Long
= -1, Optional ByVal Notes As String = "", Optional ByVal GUID
As String = "") As Long

## Parameters

Name

The name of an existing or new frame section property.
If this is an existing property, that property is modified; otherwise,
a new property is added.

MatProp

The name of the material property for the section.

t3

The vertical leg depth. [L]

t2

The total width of the section, that is, the sum of
the widths of each horizontal leg plus the back-to-back distance. [L]

tf

The horizontal leg thickness. [L]

tw

The vertical leg thickness. [L]

dis

The back-to-back distance between the angles. [L]

Color

The display color assigned to the section. If Color
is specified as -1, the program will automatically assign a color.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section. If this item is input as Default, the program assigns
a GUID to the section.

## Remarks

This function initializes a double angle-type frame
section property. If this function is called for an existing frame section
property, all items for the section are reset to their default value.

The function returns zero if the section property is
successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetFramePropDblAngle()
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
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetDblAngle("DBANG1",
"A992Fy50", 6, 9, 0.5, 0.5, 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[GetDblAngle](../Definitions/Properties/Frame/GetDblAngle.htm)



## SetEurocode12005 {Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetEurocode12005_{Wind_Load}.htm`*

# SetEurocode12005 (Note:  Newer function available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.SetEurocode12005

## VB6 Procedure

Function SetEurocode12005(ByVal Name As String, ByVal ExposureFrom As Long, ByVal DirAngle As Double, ByVal Cpw As Double, ByVal Cpl As Double, ByVal UserZ As Boolean, ByVal TopZ As Double, ByVal BottomZ As Double, ByVal WindSpeed As Double, ByVal Terrain As Long, ByVal Orography As Double, ByVal k1 As Double, ByVal CsCd As Double, Optional ByVal UserExposure As Boolean = False) As Long

## Parameters

Name

The name of an existing Wind-type load pattern.

ExposureFrom

This is 1 or 2, indicating the source of the wind exposure.

1 = From extents of rigid diaphragms

2 = From area objects

DirAngle

The direction angle for the wind load. This item applies only when ExposureFrom = 1.

Cpw

The windward coefficient, Cp. This item applies only when ExposureFrom = 1.

Cpl

The leeward coefficient, Cp. This item applies only when ExposureFrom = 1.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

WindSpeed

The basic wind speed, vb, in meters per second.

Terrain

This is 0, 1, 2, 3 or 4, indicating the terrain category.

0 = 0

1 = I

2 = II

3 = III

4 = IV

Orography

The orography factor, Co.

k1

The turbulence factor, k1.

CsCd

The structural factor, CsCd.

UserExposure

If this item is True, the wind exposure widths are provided by the user. If it is False, the wind exposure widths are calculated by the program from the extents of the diaphragms.

## Remarks

This function assigns auto wind loading parameters for Eurocode 1 2005.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignWindEurocode12005()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WIND)

   'assign Eurocode 1 2005 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetEurocode12005("WIND", 1, 0, 0.8, 0.5, False, 0, 0, 35, 2, 1, 1, 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

The function is obsolete and has been superseded by [SetEurocode12005\_1](../Definitions/Load_Pattern/Auto_Wind_Load/SetEurocode12005_1{Wind_Load}.htm) as of version 14.1.0. This function is maintained for backward compatibility. New function added.

## See Also

[GetEurocode12005](GetEurocode12005_{Wind_Load}.htm)



## SetEurocode82004 (Auto Seismic)

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetEurocode82004_(Auto_Seismic).htm`*

# SetEurocode82004  (Note:  Newer function available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoSeismic.SetEurocode82004

## VB6 Procedure

Function SetEurocode82004(ByVal Name As String, ByVal DirFlag As Long, ByVal Eccen As Double, ByVal PeriodFlag As Long, ByVal CT As Double, ByVal UserT As Double, ByVal UserZ As Boolean, ByVal TopZ As Double, ByVal BottomZ As Double, ByVal EURO2004GroundType As Long, ByVal EURO2004SpectrumType As Long, ByVal EURO2004ag As Double, ByVal EURO2004Beta As Double, ByVal EURO2004q As Double, ByVal EURO2004Lambda As Double) As Long

## Parameters

Name

The name of an existing Quake-type load pattern.

DirFlag

This is 1 or 2, indicating the seismic load direction.

1 = Global X

2 = Global Y

Eccen

The eccentricity ratio that applies to all diaphragms.

PeriodFlag

This is 1, 2 or 3, indicating the time period option.

1 = Approximate

2 = Program calculated

3 = User defined

CT

The code-specified Ct factor. This item applies when the PeriodFlag item is 1.

UserT

The user specified time period. This item applies when the PeriodFlag item is 3. [s]

UserZ

This item is True if the top and bottom elevations of the seismic load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto seismic loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto seismic loads are applied. [L]

EURO2004GroundType

This is 1, 2, 3, 4 or 5, indicating the ground type.

1 = A

2 = B

3 = C

4 = D

5 = E

EURO2004SpectrumType

This is 1 or 2, indicating the spectrum type.

1 = Type 1

2 = Type 2

EURO2004ag

The design ground acceleration in g, ag.

EURO2004Beta

The lower bound factor, Beta.

EURO2004q

The behavior factor, q.

EURO2004Lambda

The correction factor, Lambda.

## Remarks

This function assigns auto seismic loading parameters for the Eurocode 8 2004 code.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSeismicEurocode82004()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("EQX", LTYPE\_QUAKE)

   'assign Eurocode 8 2004 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetEurocode82004("EQX", 2, 0.1, 2, 0.075, 0, False, 0, 0, 2, 1, 0.4, 0.2, 2, 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

The function is obsolete and has been superseded by [SetEurocode82004\_1](../Definitions/Load_Pattern/Auto_Seismic_Load/SetEurocode82004_1_{Auto_Seismic}.htm) as of version 14.1.0. This function is maintained for backward compatibility. New function added.

## See Also

[GetEurocode82004](GetEurocode82004_(Auto_Seismic).htm)



## SetEurocode82004 {RS}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetEurocode82004_{RS}.htm`*

# SetEurocode82004  (Note:  Newer function available)

## Syntax

SapObject.SapModel.Func.FuncRS.SetEurocode82004

## VB6 Procedure

Function SetEurocode82004(ByVal Name As String, ByVal EURO2004GroundType As Long, ByVal EURO2004SpectrumType As Long, ByVal EURO2004ag As Double, ByVal EURO2004Beta As Double, ByVal EURO2004q As Double, ByVal DampRatio As Double) As Long

## Parameters

Name

The name of an existing or new function. If this is an existing function,n that function is modified; otherwise, a new function is added.

EURO2004GroundType

This is 1, 2, 3, 4 or 5, indicating the ground type.

1 = A

2 = B

3 = C

4 = D

5 = E

EURO2004SpectrumType

This is 1 or 2, indicating the spectrum type.

1 = Type 1

2 = Type 2

EURO2004ag

The design ground acceleration in g, ag.

EURO2004Beta

The lower bound factor, Beta.

EURO2004q

The behavior factor, q.

DampRatio

The damping ratio for the function, 0 <= DampRatio < 1.

## Remarks

This function defines a Eurocode 8 2004 response spectrum function.

The function returns zero if the function is successfully defined; otherwise it returns a nonzero value.

## VBA Example

Sub SetRSFuncEurocode82004()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add Eurocode 8 2004 RS function
      ret = SapModel.Func.FuncRS.SetEurocode82004("RS-1", 2, 1, 0.4, 0.2, 2, 0.04)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

The function is obsolete and has been superseded by [SetEurocode82004\_1](../Definitions/Functions/Response_Spectrum/SetEurocode82004_1_{RS}.htm) as of version 14.1.0. This function is maintained for backward compatibility. New function added.

## See Also

[GetEurocode82004](GetEurocode82004_(RS).htm)



## SetExposure

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetExposure.htm`*

# SetExposure

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.SetExposure

## VB6 Procedure

Function SetExposure(ByVal Name As String, ByVal Diaph As String, ByVal x As Double, ByVal y As Double, ByVal Width As Double, ByVal Height As Double) As Long

## Parameters

Name

The name of an existing Wind-type load pattern that has an auto wind load assigned.

Diaph

The name of an existing special rigid diaphragm constraint, that is, a diaphragm constraint with the following features:

1. The constraint type is CONSTRAINT\_DIAPHRAGM = 2.

2. The constraint coordinate system is Global.

3. The constraint axis is Z.

x

The global X-coordinate of the point where the wind force is applied. [L]

y

The global Y-coordinate of the point where the wind force is applied. [L]

Width

The exposure width for the wind load applied to the specified diaphragm. [L]

Height

The exposure height for the wind load applied to the specified diaphragm. [L]

## Remarks

This function assigns exposure parameters for auto wind loads determined from extents of rigid diaphragms. This function does not apply for User-type auto wind loads.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value. The function returns an error if the auto wind load is not specified to have user exposure parameters.

## VBA Example

Sub AssignWindUserExposure()
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
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", LTYPE\_WIND)

   'assign ASCE788 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetASCE788("WIND", 1, 0, 0.8, 0.5, False, 0, 0, 80, 3, 1, 0.85, True)

   'assign user exposure data
      ret = SapModel.LoadPatterns.AutoWind.SetExposure("WIND", "Diaph2", 0, 0, 900, 124)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.01.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetExposure](GetExposure.htm)

[GetSpecialRigidDiaphragmList](../Definitions/Constraints/GetSpecialRigidDiaphragmList.htm)



## SetFireproofing

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetFireproofing.htm`*

# SetFireproofing

## Syntax

SapObject.SapModel.FrameObj.SetFireproofing

## VB6 Procedure

Function SetFireproofing(ByVal Name As String, ByVal MyType As Long, ByVal Thickness As Double, ByVal Perimeter As Double, ByVal Density As Double, ByVal tf As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

MyType

This is 1, 2 or 3, indicating the type of fireproofing assigned.

1 = Sprayed on - program calculate section perimeter

2 = Sprayed on - user provides section perimeter

3 = Concrete encased

Thickness

When MyType = 1 or MyType = 2, this is the thickness of the sprayed on fireproofing. When MyType = 3, this is the concrete cover dimension. [L]

Perimeter

This item applies only when MyType = 2. It is the length of fireproofing applied, measured around the perimeter of the frame object cross-section. [L]

Density

This is the weight per unit volume of the fireproofing material. [F/L3]

tf

This item applies only when MyType = 1 or MyType = 3. If this item is True, the fireproofing is assumed to be applied to the top flange of the section. If it is False, the program assumes no fireproofing is applied to the section top flange. This flag applies for I, channel and double channel sections.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function assigns fireproofing to frame objects.

The function returns zero if the fireproofing assignments are successfully assigned, otherwise it returns a nonzero value.

The program automatically adds the load \*(weight) calculated for the fireproofing to all load patterns that include self weight.

## VBA Example

Sub AssignFireproofing()
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

   'assign fireproofing
      ret = SapModel.FrameObj.SetFireproofing("ALL", 1, 2, 0, 8.68E-06, False, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetFireproofing](GetFireproofing.htm)

[DeleteFireproofing](../Object_Model/Frame_Object/DeleteFireproofing.htm)



## SetFromFile {Time History}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetFromFile_{Time_History}.htm`*

# SetFromFile (Note:  Newer function available)

## Syntax

SapObject.SapModel.Func.FuncTH.SetFromFile

## VB6 Procedure

Function SetFromFile(ByVal Name As String, ByVal FileName As String, ByVal HeadLines As Long, ByVal PreChars As Long, ByVal PointsPerLine As Long, ByVal ValueType As Long, ByVal FreeFormat As Boolean, Optional ByVal NumberFixed As Long = 10) As Long

## Parameters

Name

The name of an existing or new function. If this is an existing function, that function is modified; otherwise, a new function is added.

FileName

The full path of the text file containing the function data.

HeadLines

The number of header lines in the text file to be skipped before starting to read function data.

PreChars

The number of prefix characters to be skipped on each line in the text file.

PointsPerLine

The number of function points included on each text file line.

ValueType

This is either 1 or 2, indicating value type.

1 = Values at equal time intervals

2 = Time and function values

FreeFormat

This item is True if the data is provided in a free format. It is False if it is in a fixed format.

NumberFixed

This item applies only when the FreeFormat item is False. It is the number of characters per item.

## Remarks

This function defines a time history function from file.

The function returns zero if the function is successfully defined; otherwise it returns a nonzero value.

## VBA Example

Sub SetTHFuncFromFile()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add TH function from file
      ret = SapModel.Func.FuncTH.SetFromFile("TH-1", "C:\SapAPI\FuncTH.txt", 3, 0, 3, 2, True)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Text File

Following is the contents of the text file name FuncTH.txt used in the VBA Example.

Time History Function

Time (sec) and Acceleration (g) values

3 points per line

   0.00000    .01080    .04200    .00100    .09700    .01590
    .16100   -.00010    .22100    .01890    .26300    .00010
    .29100    .00590    .33200   -.00120    .37400    .02000
    .42900   -.02370    .47100    .00760    .58100    .04250
    .62300    .00940    .66500    .01380    .72000   -.00880
    .72010   -.02560    .78900   -.03870    .78910   -.05680
    .87200   -.02320    .87210   -.03430    .94100   -.04020
    .94110   -.06030    .99700   -.07890   1.06600   -.06660
   1.06610   -.03810   1.09400   -.04290   1.16800    .08970
   1.31500   -.16960   1.38400   -.08280   1.41200   -.08280
   1.44000   -.09450   1.48100   -.08850   1.50900   -.10800
   1.53700   -.12800   1.62800    .11440   1.70300    .23550
   1.80000    .14280   1.85500    .17770   1.92400   -.26100
   2.00700   -.31940   2.21500    .29520   2.27000    .26340
   2.32000   -.29840   2.39500    .00540   2.45000    .28650
   2.51900   -.04690   2.57500    .15160   2.65200    .20770
   2.70800    .10870   2.76900   -.03250   2.89300    .10330
   2.97600   -.08030   3.06800    .05200   3.12900   -.15470
   3.21200    .00650   3.25300   -.20600   3.38600    .19270
   3.41900   -.09370   3.53000    .17080   3.59900   -.03590
   3.66800    .03650   3.73800   -.07360   3.83500    .03110
   3.90400   -.18330   4.01400    .02270   4.05600   -.04350
   4.10600    .02160   4.22200   -.19720   4.31400   -.17620
   4.41600    .14600   4.47100   -.00470   4.61800    .25720
   4.66500   -.20450   4.75600    .06080   4.83100   -.27330
   4.97000    .17790   5.03900    .03010   5.10800    .21830
   5.19900    .02670   5.23300    .12520   5.30200    .12900
   5.33000    .10890   5.34300   -.02390   5.45400    .17230
   5.51000   -.10210   5.60600    .01410   5.69000   -.19490
   5.77300   -.02420   5.80000   -.00500   5.80900   -.02750
   5.86900   -.05730   5.88300   -.03270   5.92500    .02160
   5.98000    .01080   6.01300    .02350   6.08500   -.06650
   6.13200    .00140   6.17400    .04930   6.18800    .01490
   6.18810   -.02000   6.22900   -.03810   6.27900    .02070
   6.32600   -.00580   6.36800   -.06030   6.38200   -.01620
   6.40900    .02000   6.45900   -.01760   6.47800   -.00330
   6.52000    .00430   6.53400   -.00400   6.56200   -.00990
   6.57500   -.00170   6.60300   -.01700   6.64500    .03730
   6.68600    .04570   6.71400    .03850   6.72800    .00090
   6.76900   -.02880   6.76910    .00160   6.81100    .01130
   6.85200    .00220   6.90800    .00920   6.99100   -.09960
   7.07400    .03600   7.12100    .00780   7.14300   -.02770
   7.14900    .00260   7.17100    .02720   7.22600    .05760
   7.29500   -.04920   7.37000    .02970   7.40600    .01090
   7.42500    .01860   7.46100   -.02530   7.52500   -.03470
   7.57200    .00360   7.60000   -.06280   7.64100   -.02800
   7.66900   -.01960   7.69100    .00680   7.75200   -.00540
   7.79400   -.06030   7.83500   -.03570   7.87700   -.07160
   7.96000   -.01400   7.98700   -.00560   8.00100    .02220
   8.07000    .04680   8.12600    .02600   8.12610   -.03350
   8.19500   -.01280   8.22300    .06610   8.27800    .03050
   8.33400    .02460   8.40300    .03470   8.45800   -.03690
   8.53300   -.03440   8.59600   -.01040   8.63800   -.02600
   8.73500    .15340   8.81800   -.00280   8.86000    .02330
   8.88200   -.02610   8.91500   -.00220   8.95600   -.18490
   9.05300    .12600   9.09500    .03200   9.12300    .09550
   9.15000    .12460   9.25300   -.03280   9.28900   -.04510
   9.42700    .13010   9.44100   -.16570   9.51000    .04190
   9.63500   -.09360   9.70400    .08160   9.81500   -.08810
   9.89800    .00640   9.93900   -.00060   9.99500    .05860
  10.02200   -.07130  10.05000   -.04480  10.05010   -.02210
  10.10500    .00930  10.10510    .00240  10.18800    .05100
  10.27200   -.12430  10.38200    .05870  10.42400    .01330
  10.45200    .03860  10.46500    .11640  10.50700   -.03740
  10.53400   -.05720  10.64500    .03080  10.70100    .02230
  10.71400    .05150  10.77000    .09030  10.83900   -.01940
  10.92200    .04710  10.92210   -.06770  10.96400   -.07940
  10.99100   -.01200  11.07400    .06080  11.08800   -.02690
  11.11600   -.04160  11.20700    .02930  11.20710    .05520
  11.22700    .07560  11.26800    .04310  11.32400    .02080
  11.43400    .11800  11.57300   -.09990  11.65600   -.12470
  11.72500   -.20940  11.72510   -.14180  11.78000   -.11630
  11.80800   0.00000  11.87700    .07620  11.91900    .05700
  11.98800    .13540  12.04300    .06730  12.11300    .08650

## Release Notes

Initial release in version 11.02.

The function is obsolete and has been superseded by [SetFromFile\_1](../definitions/functions/time_history/SetFromFile_1_{Time_History}.htm) as of version 14.12. This function is maintained for backward compatibility. New function added.

## See Also

[GetFromFile](GetFromFile_{Time_History}.htm)



## SetISection {Frame}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetISection_{Frame}_old.htm`*

# SetISection (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropFrame.SetISection

## VB6 Procedure

Function SetISection(ByVal Name As String, ByVal MatProp
As String, ByVal t3 As Double, ByVal t2 As Double, ByVal tf As Double,
ByVal tw As Double, ByVal t2b As Double, ByVal tfb As Double, Optional
ByVal Color As Long = -1, Optional ByVal Notes As String = "",
Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing or new frame section property.
If this is an existing property, that property is modified; otherwise,
a new property is added.

MatProp

The name of the material property for the section.

t3

The section depth. [L]

t2

The top flange width. [L]

tf

The top flange thickness. [L]

tw

The web thickness. [L]

t2b

The bottom flange width. [L]

tfb

The bottom flange thickness. [L]

Color

The display color assigned to the section. If Color
is specified as -1, the program will automatically assign a color.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section. If this item is input as Default, the program assigns
a GUID to the section.

## Remarks

This function initializes an I-type frame section property.
If this function is called for an existing frame section property, all
items for the section are reset to their default value.

The function returns zero if the section property is
successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetFramePropISection()
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
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetISection("ISEC1",
"A992Fy50", 24, 10, 0.5, 0.3, 14, 0.6)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[GetISection](../Definitions/Properties/Frame/GetISection_{Frame}.htm)



## SetInsertionPoint {Cable Object}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetInsertionPoint_{Cable_Object}.htm`*

# SetInsertionPoint

## Syntax

SapObject.SapModel.CableObj.SetInsertionPoint

## VB6 Procedure

Function SetInsertionPoint(ByVal Name As String, ByVal StiffTransform As Boolean, ByRef Offset1() As Double, ByRef Offset2() As Double, Optional ByVal CSys As String = "Local", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

StiffTransform

If this item is True, the cable object stiffness is transformed for cardinal point and joint offsets from the cable section centroid.

Offset1

This is an array of three joint offset distances, in the coordinate directions specified by CSys, at the I-End of the cable object. [L]

Offset1(0) = Offset in the 1-axis or X-axis direction

Offset1(1) = Offset in the 2-axis or Y-axis direction

Offset1(2) = Offset in the 3-axis or Z-axis direction

Offset2

This is an array of three joint offset distances, in the coordinate directions specified by CSys, at the J-End of the cable object. [L]

Offset2(0) = Offset in the 1-axis or X-axis direction

Offset2(1) = Offset in the 2-axis or Y-axis direction

Offset2(2) = Offset in the 3-axis or Z-axis direction

CSys

This is Local or the name of a defined coordinate system. It is the coordinate system in which the Offset1 and Offset2 items are specified.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function assigns cable object insertion point data. The assignments include the end joint offsets.

The function returns zero if the insertion point data is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableInsertionPoint()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Offset1() As Double
      Dim Offset2() As Double
      Dim Name As String

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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable insertion point
      ReDim Offset1(2)
      ReDim Offset2(2)
      For i = 0 To 2
         Offset1(i)=10 + i
         Offset2(i)=20 + i
      Next i
      ret = SapModel.CableObj.SetInsertionPoint(Name, True, Offset1, Offset2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

This function is obsolete as of v19.2.0 when cable insertion point assignments were removed from the program.

## See Also

[GetInsertionPoint](GetInsertionPoint_{Cable_Object}.htm)



## SetInsertionPoint{Frame Object}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetInsertionPoint{Frame_Object}.htm`*

# SetInsertionPoint (Note:  Newer function available)

## Syntax

SapObject.SapModel.FrameObj.SetInsertionPoint

## VB6 Procedure

Function SetInsertionPoint(ByVal Name As String, ByVal
CardinalPoint As Long, ByVal Mirror2 As Boolean, ByVal StiffTransform
As Boolean, ByRef Offset1() As Double, ByRef Offset2() As Double, Optional
ByVal CSys As String = "Local", Optional ByVal ItemType As eItemType
= Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending
on the value of the ItemType item.

CardinalPoint

This is a numeric value from 1 to 11 that specifies
the cardinal point for the frame object. The cardinal point specifies
the relative position of the frame section on the line representing the
frame object.

1 = bottom left

2 = bottom center

3 = bottom right

4 = middle left

5 = middle center

6 = middle right

7 = top left

8 = top center

9 = top right

10 = centroid

11 = shear center

Mirror2

If this item is True, the frame object section is assumed
to be mirrored (flipped) about its local 2-axis.

StiffTransform

If this item is True, the frame object stiffness is
transformed for cardinal point and joint offsets from the frame section
centroid.

Offset1

This is an array of three joint offset distances, in
the coordinate directions specified by CSys, at the I-End of the frame
object. [L]

Offset1(0) = Offset in
the 1-axis or X-axis direction

Offset1(1) = Offset in
the 2-axis or Y-axis direction

Offset1(2) = Offset in the
3-axis or Z-axis direction

Offset2

This is an array of three joint offset distances, in
the coordinate directions specified by CSys, at the J-End of the frame
object. [L]

Offset2(0) = Offset in
the 1-axis or X-axis direction

Offset2(1) = Offset in
the 2-axis or Y-axis direction

Offset2(2) = Offset in the
3-axis or Z-axis direction

CSys

This is Local or the name of a defined coordinate system.
It is the coordinate system in which the Offset1 and Offset2 items are
specified.

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

This function assigns frame object insertion point data.
The assignments include the cardinal point and end joint offsets.

The function returns zero if the insertion point data
is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameInsertionPoint()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Offset1() As Double
      Dim Offset2() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
3, 124, 3, 200)

   'assign frame insertion point
      ReDim Offset1(2)
      ReDim Offset2(2)
      For i=0 To 2
         Offset1(i)=10 + i
         Offset2(i)=20 + i
   Next i
      ret = SapModel.FrameObj.SetInsertionPoint("15",
7, False, True, Offset1, Offset2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

This function is obsolete and has been superseded by
[SetInsertionPoint\_1](../Object_Model/Frame_Object/SetInsertionPoint_1{Frame_Object}.htm)
as of version 24.1. This function is maintained for backwards compatibility.

## See Also

[GetInsertionPoint](GetInsertionPoint_{Frame_Object}.htm)



## SetLoads {Static Linear Multistep}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetLoads_{Static_Linear_Multistep}.htm`*

# SetLoads

## Syntax

SapObject.SapModel.LoadCases.StaticLinearMultistep.SetLoads

## VB6 Procedure

Function SetLoads(ByVal Name As String, ByVal NumberLoads As Long, ByRef LoadType() As String, ByRef LoadName() As String, ByRef SF() As Double) As Long

## Parameters

Name

The name of an existing static linear multistep analysis case.

NumberLoads

The number of loads assigned to the specified analysis case.

LoadType

This is an array that includes either Load or Accel, indicating the type of each load assigned to the load case.

LoadName

This is an array that includes the name of each load assigned to the load case.

If the LoadType item is Load, this item is the name of a defined load pattern.

If the LoadType item is Accel, this item is UX, UY, UZ, RX, RY or RZ, indicating the direction of the load.

SF

This is an array that includes the scale factor of each load assigned to the load case. [L/s2] for Accel UX UY and UZ; otherwise unitless

## Remarks

This function sets the load data for the specified analysis case.

The function returns zero if the data is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetCaseStaticLinearMultistepLoads()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyLoadType() As String
      Dim MyLoadName() As String
      Dim MySF() As Double

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

   'add static linear multistep load case
      ret = SapModel.LoadCases.StaticLinearMultistep.SetCase("LCASE1")

   'set load data
      ReDim MyLoadType(1)
      ReDim MyLoadName(1)
      ReDim MySF(1)
      MyLoadType(0) = "Load"
      MyLoadName(0) = "DEAD"
      MySF(0) = 0.7
      MyLoadType(1) = "Accel"
      MyLoadName(1) = "UZ"
      MySF(1) = 1.2
      ret = SapModel.LoadCases.StaticLinearMultistep.SetLoads("LCASE1", 2, MyLoadType, MyLoadName, MySF)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoads](GetLoads_{Static_Linear_Multistep}.htm)



## SetModalComb

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetModalComb.htm`*

# SetModalComb (Note:  Newer function available)

## Syntax

SapObject.SapModel.LoadCases.ResponseSpectrum.SetModalComb

## VB6 Procedure

Function SetModalComb(ByVal Name As String, ByVal MyType As Long, Optional ByVal F1 As Double = 1, Optional ByVal F2 As Double = 0, Optional ByVal td As Double = 60) As Long

## Parameters

Name

The name of an existing response spectrum load case.

MyType

This is 1, 2, 3, 4, 5 or 6, indicating the modal combination option.

1 = CQC

2 = SRSS

3 = ABS

4 = GMC

5 = 10 percent

6 = Double sum

F1

This item applies only when MyType = 4. It is the GMC f1 factor. [cyc/s]

F2

This item applies only when MyType = 4. It is the GMC f2 factor. [cyc/s]

td

This item applies only when MyType = 6. It is the factor td. [s]

## Remarks

This function sets the modal combination option for the specified load case.

The function returns zero if the option is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetCaseResponseSpectrumModalComb()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add response spectrum load case
      ret = SapModel.LoadCases.ResponseSpectrum.SetCase("LCASE1")

   'set modal combination option
      ret = SapModel.LoadCases.ResponseSpectrum.SetModalComb("LCASE1", 4, 2, 0.5)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

The function is obsolete and has been superseded by [SetModalComb\_1](../definitions/load_case/response_spectrum/SetModalComb_1.htm) as of version 14.00. This function is maintained for backward compatibility. New function added

## See Also

[GetModalComb](GetModalComb.htm)



## SetNTC2008 {Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetNTC2008_{Wind_Load}-obsolete.htm`*

# SetNTC2008 (Note:  Obsolete, Newer Function Available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.SetNTC2008

## VB6 Procedure

Function SetNTC2008(ByVal Name As String, ByRef ExposureFrom As Long, ByRef DirAngle As Double, ByRef Cpw As Double, ByRef Cpl As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef Vb As Double, ByRef ExposureCategory As Long, ByRef ct As Double, ByRef cd As Double, ByRef cp As Double, ByRef UserExposure As Boolean = False) As Long

## Parameters

Name

The name of an existing Wind-type load pattern.

ExposureFrom

This is 1 or 2, indicating the source of the wind exposure.

1 = From extents of rigid diaphragms

2 = From area objects

DirAngle

The direction angle for the wind load. This item applies only when ExposureFrom = 1.

Cpw

The windward coefficient, Cp. This item applies only when ExposureFrom = 1.

Cpl

The leeward coefficient, Cp. This item applies only when ExposureFrom = 1.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

Vb

The wind velocity in m/s.

ExposureCategory

This is 1, 2, 3, 4, or 5, indicating the exposure category.

1 = I

2 = II

3 = III

4 = IV

5 = V

ct

The topography factor, ct.

cd

The dynamic coefficient, cd.

cp

The shape factor, cp.

UserExposure

If this item is True, the wind exposure widths are provided by the user. If it is False, the wind exposure widths are calculated by the program from the extents of the diaphragms.

## Remarks

This function retrieves auto wind loading parameters for NTC 2008.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub SetWindNTC2008()
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
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", eLoadPatternType\_WIND)

   'assign NTC2008 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetNTC2008("WIND", 1, 0, 0.8, 0.5, False, 0, 0, 35, 3, 1, 1, 1, False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 18.1.0.

This function was replaced by [SetNTC2008\_1](../Definitions/Load_Pattern/Auto_Wind_Load/SetNTC2008_1{Wind_Load}.htm).

## See Also

[GetNTC2008](GetNTC2008_{Wind_Load}-obsolete.htm)



## SetNTC2018 {Wind Load}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetNTC2018_{Wind_Load}_obsolete.htm`*

# SetNTC2018 (Note:  Obsolete, Newer Function Available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoWind.SetNTC2018

## VB6 Procedure

Function SetNTC2018(ByVal Name As String, ByRef ExposureFrom As Long, ByRef DirAngle As Double, ByRef Cpw As Double, ByRef Cpl As Double, ByRef UserZ As Boolean, ByRef TopZ As Double, ByRef BottomZ As Double, ByRef Vb As Double, ByRef ExposureCategory As Long, ByRef ct As Double, ByRef cd As Double, ByRef cp As Double, ByRef UserExposure As Boolean = False) As Long

## Parameters

Name

The name of an existing Wind-type load pattern.

ExposureFrom

This is 1 or 2, indicating the source of the wind exposure.

1 = From extents of rigid diaphragms

2 = From area objects

DirAngle

The direction angle for the wind load. This item applies only when ExposureFrom = 1.

Cpw

The windward coefficient, Cp. This item applies only when ExposureFrom = 1.

Cpl

The leeward coefficient, Cp. This item applies only when ExposureFrom = 1.

UserZ

This item is True if the top and bottom elevations of the wind load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto wind loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto wind loads are applied. [L]

Vb

The wind velocity in m/s.

ExposureCategory

This is 1, 2, 3, 4, or 5, indicating the exposure category.

1 = I

2 = II

3 = III

4 = IV

5 = V

ct

The topography factor, ct.

cd

The dynamic coefficient, cd.

cp

The shape factor, cp.

UserExposure

If this item is True, the wind exposure widths are provided by the user. If it is False, the wind exposure widths are calculated by the program from the extents of the diaphragms.

## Remarks

This function retrieves auto wind loading parameters for NTC 2018.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub SetWindNTC2018()
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
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'define diaphragm constraints
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1", Z)
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph2", Z)

   'assign points to diaphragm
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("2")
      ret = SapModel.PointObj.SetConstraint("", "Diaph1", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection
      ret = SapModel.SelectObj.PlaneXY("3")
      ret = SapModel.PointObj.SetConstraint("", "Diaph2", SelectedObjects)
      ret = SapModel.SelectObj.ClearSelection

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("WIND", eLoadPatternType\_WIND)

   'assign NTC2018 parameters
      ret = SapModel.LoadPatterns.AutoWind.SetNTC2018("WIND", 1, 0, 0.8, 0.5, False, 0, 0, 35, 3, 1, 1, 1, False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

This function was replaced by [SetNTC2018\_1](../Definitions/Load_Pattern/Auto_Wind_Load/SetNTC2018_1{Wind_Load}.htm).

## See Also

[GetNTC2018](GetNTC2018_{Wind_Load}-obsolete.htm)



## SetNZS11702004

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetNZS11702004.htm`*

# SetNZS11702004

## Syntax

SapObject.SapModel.Func.FuncRS.SetNZS11702004

## VB6 Procedure

Function SetNZS11702004(ByVal Name As String, ByVal NZS2004SiteClass As Long, ByVal NZS2004Z As Double, ByVal NZS2004R As Double, ByVal NZS2004DIST As Double, ByVal DampRatio As Double) As Long

## Parameters

Name

The name of an existing or new function. If this is an existing function, that function is modified; otherwise, a new function is added.

NZS2004SiteClass

This is 1, 2, 3, 4 or 5, indicating the site class.

1 = A

2 = B

3 = C

4 = D

5 = E

NZS2004Z

The hazard factor, Z.

NZS2004R

The return period factor, R.

NZS2004DIST

Distance to the fault in kim, used to calculate the near fault factor.

DampRatio

The damping ratio for the function, 0 <= DampRatio < 1.

## Remarks

This function defines an NZS 1170.5 2004 response spectrum function.

The function returns zero if the function is successfully defined; otherwise it returns a nonzero value.

## VBA Example

Sub SetRSFuncNZS11702004()
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

   'add NZS 1170 2004 RS function
      ret = SapModel.Func.FuncRS.SetNZS11702004("RS-1", 3, 0.4, 1.3, 20, 0.04)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

Modified NZS2004N to NZS2004DIST in version 14.1.0.

## See Also

[GetNZS11702004](GetNZS11702004.htm)



## SetNZS11702004 (Auto Seismic)

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetNZS11702004_(Auto_Seismic).htm`*

# SetNZS11702004

## Syntax

SapObject.SapModel.LoadPatterns.AutoSeismic.SetNZS11702004

## VB6 Procedure

Function SetNZS11702004(ByVal Name As String, ByVal DirFlag As Long, ByVal Eccen As Double, ByVal PeriodFlag As Long, ByVal UserT As Double, ByVal UserZ As Boolean, ByVal TopZ As Double, ByVal BottomZ As Double, ByVal NZS2004SiteClass As Long, ByVal NZS2004Z As Double, ByVal NZS2004R As Double, ByVal NZS2004DIST As Double, ByVal NZS2004Sp As Double, ByVal NZS2004Mu As Double) As Long

## Parameters

Name

The name of an existing Quake-type load pattern.

DirFlag

This is 1 or 2, indicating the seismic load direction.

1 = Global X

2 = Global Y

Eccen

The eccentricity ratio that applies to all diaphragms.

PeriodFlag

This is 1, 2 or 3, indicating the time period option.

1 = Approximate

2 = Program calculated

3 = User defined

UserT

The user specified time period. This item applies when the PeriodFlag item is 3. [s]

UserZ

This item is True if the top and bottom elevations of the seismic load are user specified. It is False if the elevations are determined by the program.

TopZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the highest level where auto seismic loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True. It is the global Z-coordinate at the lowest level where auto seismic loads are applied. [L]

NZS2004SiteClass

This is 1, 2, 3, 4 or 5, indicating the site class.

1 = A

2 = B

3 = C

4 = D

5 = E

NZS2004Z

The hazard factor, Z.

NZS2004R

The return period factor, R.

NZS2004DIST

Distance to the fault in km, used to calculate the near fault factor.

NZS2004Sp

The structural performance factor, Sp.

NZS2004Mu

The structural ductility factor, u.

## Remarks

This function assigns auto seismic loading parameters for the NZS 1170.5 2004 code.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSeismicNZS11702004()
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
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 336, 2, 432)

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("EQX", LTYPE\_QUAKE)

   'assign NZS 1170 2004 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetNZS11702004("EQX", 2, 0.1, 2, 0, False, 0, 0, 3, 0.4, 1.3, 20, 0.7, 3)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

Modified NZS2004N to NZS2004DIST in version 14.1.0.

## See Also

[GetNZS11702004](GetNZS11702004_(Auto_Seismic).htm)



## SetNZS11702004 (Auto Seismic)_1

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetNZS11702004_(Auto_Seismic)_1.htm`*

# SetNZS11702004\_1 (Note: Newer function available)

## Syntax

SapObject.SapModel.LoadPatterns.AutoSeismic.SetNZS11702004\_1

## VB6 Procedure

Function SetNZS11702004\_1(ByVal Name As String, ByVal
DirFlag As Long, ByVal Eccen As Double, ByVal PeriodFlag As Long, ByVal
UserT As Double, ByVal UserZ As Boolean, ByVal TopZ As Double, ByVal BottomZ
As Double, ByVal NZS2004SiteClass As Long, ByVal NZS2004Z As Double, ByVal
NZS2004R As Double, ByVal NZS2004DIST As Double, ByVal NZS2004Sp As Double,
ByVal NZS2004Mu As Double, ByValNZS2004ConsiderTSite As Boolean, ByValNZS2004TSite
As Double) As Long

## Parameters

Name

The name of an existing Quake-type load pattern.

DirFlag

This is 1 or 2, indicating the seismic load direction.

1 = Global X

2 = Global Y

Eccen

The eccentricity ratio that applies to all diaphragms.

PeriodFlag

This is 1, 2 or 3, indicating the time period option.

1 = Approximate

2 = Program calculated

3 = User defined

UserT

The user specified time period. This item applies when
the PeriodFlag item is 3. [s]

UserZ

This item is True if the top and bottom elevations of
the seismic load are user specified. It is False if the elevations are
determined by the program.

TopZ

This item applies only when the UserZ item is True.
It is the global Z-coordinate at the highest level where auto seismic
loads are applied. [L]

BottomZ

This item applies only when the UserZ item is True.
It is the global Z-coordinate at the lowest level where auto seismic loads
are applied. [L]

NZS2004SiteClass

This is 1, 2, 3, 4 or 5, indicating the site class.

1 = A

2 = B

3 = C

4 = D

5 = E

NZS2004Z

The hazard factor, Z.

NZS2004R

The return period factor, R.

NZS2004DIST

Distance to the fault in km, used to calculate the near
fault factor.

NZS2004Sp

The structural performance factor, Sp.

NZS2004Mu

The structural ductility factor, u.

NZS2004ConsiderTSite

Indicates whether to consider the site period for the
spectral shape factor.

NZS2004TSite

The low amplitude site period.

## Remarks

This function assigns auto seismic loading parameters
for the NZS 1170.5 2004 code.

The function returns zero if the parameters are successfully
assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSeismicNZS11702004\_1()
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
      ret = SapModel.File.New3DFrame(BeamSlab,
2, 144, 3, 336, 2, 432)

   'add new load pattern
      ret = SapModel.LoadPatterns.Add("EQX",
LTYPE\_QUAKE)

   'assign NZS 1170 2004 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetNZS11702004\_1("EQX",
2, 0.1, 2, 0, False, 0, 0, 3, 0.4, 1.3, 20, 0.7, 3, True, 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v21.0.0.

This function supersedes [SetNZS11702004](SetNZS11702004_(Auto_Seismic).htm).

This function is obsolete and has been superseded by
SetNZS11702004\_2 as of v22.0.0. This function is maintained for backward
compatibility.

## See Also

[GetNZS11702004\_1](GetNZS11702004_(Auto_Seismic)_1.htm)



## SetOConcrete

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetOConcrete.htm`*

# SetOConcrete (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropMaterial.SetOConcrete

## VB6 Procedure

Function SetOConcrete(ByVal Name As String, ByVal fc As Double, ByVal IsLightweight As Boolean, ByVal fcsfactor As Double, ByVal sstype As Long, ByVal SSHysType As Long, ByVal StrainAtfc As Double, ByVal StrainUltimate As Double, Optional ByVal FrictionAngle As Double = 0, Optional ByVal DilatationalAngle As Double = 0, Optional ByVal Temp As Double = 0) As Long

## Parameters

Name

The name of an existing concrete material property.

fc

The concrete compressive strength. [F/L2]

IsLightweight

If this item is True, the concrete is assumed to be lightweight concrete.

fcsfactor

The shear strength reduction factor for lightweight concrete.

eFu

The expected tensile stress. [F/L2]

SSType

This is 0, 1 or 2, indicating the stress-strain curve type.

0 = User defined

1 = Parametric - Simple

2 = Parametric - Mander

SSHysType

This is 0, 1 or 2, indicating the stress-strain hysteresis type.

0 = Elastic

1 = Kinematic

2 = Takeda

StrainAtfc

This item applies only to parametric stress-strain curves. It is the strain at the unconfined compressive strength.

StrainUltimate

This item applies only to parametric stress-strain curves. It is the ultimate unconfined strain capacity. This item must be larger than the StrainAtfc item.

FrictionAngle

The Drucker-Prager friction angle, 0 <= FrictionAngle < 90. [deg]

DilatationalAngle

The Drucker-Prager dilatational angle, 0 <= DilatationalAngle < 90. [deg]

Temp

This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.

This item is the temperature at which the specified data applies. The temperature must have been defined previously for the material.

## Remarks

This function sets the other material property data for concrete materials.

The function returns zero if the data is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignMatPropConcreteData()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'initialize new material property
      ret = SapModel.PropMaterial.SetMaterial("Concrete", MATERIAL\_CONCRETE)

   'assign other properties
      ret = SapModel.PropMaterial.SetOConcrete("Concrete", 5, False, 0, 1, 2, 0.0022, 0.0052)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

This function is obsolete and is superseded by [SetOConcrete](SetOConcrete.htm) as of version 12.00. This function is maintained for backwards compatibility.

## See Also

[GetOConcrete](GetOConcrete.htm)



## SetOConcrete_1

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetOConcrete_1.htm`*

# SetOConcrete\_1

## Syntax

SapObject.SapModel.PropMaterial.SetOConcrete\_1

## VB6 Procedure

Function SetOConcrete\_1(ByVal Name As String, ByVal fc As Double, ByVal IsLightweight As Boolean, ByVal fcsfactor As Double, ByVal sstype As Long, ByVal SSHysType As Long, ByVal StrainAtfc As Double, ByVal StrainUltimate As Double, ByVal FinalSlope As Double, Optional ByVal FrictionAngle As Double = 0, Optional ByVal DilatationalAngle As Double = 0, Optional ByVal Temp As Double = 0) As Long

## Parameters

Name

The name of an existing concrete material property.

fc

The concrete compressive strength. [F/L2]

IsLightweight

If this item is True, the concrete is assumed to be lightweight concrete.

fcsfactor

The shear strength reduction factor for lightweight concrete.

SSType

This is 0, 1 or 2, indicating the stress-strain curve type.

0 = User defined

1 = Parametric - Simple

2 = Parametric - Mander

SSHysType

This is 0, 1 or 2, indicating the stress-strain hysteresis type.

0 = Elastic

1 = Kinematic

2 = Takeda

StrainAtfc

This item applies only to parametric stress-strain curves. It is the strain at the unconfined compressive strength.

StrainUltimate

This item applies only to parametric stress-strain curves. It is the ultimate unconfined strain capacity. This item must be larger than the StrainAtfc item.

FinalSlope

This item applies only to parametric stress-strain curves. It is a multiplier on the material modulus of elasticity, E. This value multiplied times E gives the final slope on the compression side of the curve.

FrictionAngle

The Drucker-Prager friction angle, 0 <= FrictionAngle < 90. [deg]

DilatationalAngle

The Drucker-Prager dilatational angle, 0 <= DilatationalAngle < 90. [deg]

Temp

This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.

This item is the temperature at which the specified data applies. The temperature must have been defined previously for the material.

## Remarks

This function sets the other material property data for concrete materials.

The function returns zero if the data is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignMatPropConcreteData\_1()
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

   'initialize new material property
      ret = SapModel.PropMaterial.SetMaterial("Concrete", MATERIAL\_CONCRETE)

   'assign other properties
      ret = SapModel.PropMaterial.SetOConcrete\_1("Concrete", 5, False, 0, 1, 2, 0.0022, 0.0052, -0.1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

This function supersedes [SetOConcrete](SetOConcrete.htm).

## See Also

[GetOConcrete\_1](GetOConcrete_1.htm)



## SetORebar

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetORebar.htm`*

# SetORebar (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropMaterial.SetORebar

## VB6 Procedure

Function SetORebar(ByVal Name As String, ByVal Fy As Double, ByVal Fu As Double, ByVal eFy As Double, ByVal eFu As Double, ByVal SSType As Long, ByVal SSHysType As Long, ByVal StrainAtHardening As Double, ByVal StrainUltimate As Double, ByVal UseCaltransSSDefaults As Boolean, Optional ByVal Temp As Double = 0) As Long

## Parameters

Name

The name of an existing rebar material property.

Fy

The minimum yield stress. [F/L2]

Fu

The minimum tensile stress. [F/L2]

eFy

The expected yield stress. [F/L2]

eFu

The expected tensile stress. [F/L2]

SSType

This is 0, 1 or 2, indicating the stress-strain curve type.

0 = User defined

1 = Parametric - Simple

2 = Parametric - Park

SSHysType

This is 0, 1 or 2, indicating the stress-strain hysteresis type.

0 = Elastic

1 = Kinematic

2 = Takeda

StrainAtHardening

This item applies only when parametric stress-strain curves are used and when UseCaltransSSDefaults is False. It is the strain at the onset of strain hardening.

StrainUltimate

This item applies only when parametric stress-strain curves are used and when UseCaltransSSDefaults is False. It is the ultimate strain capacity. This item must be larger than the StrainAtHardening item.

UseCaltransSSDefaults

If this item is True, the program uses Caltrans default controlling strain values, which are bar size dependent.

Temp

This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.

This item is the temperature at which the specified data applies. The temperature must have been defined previously for the material.

## Remarks

This function sets the other material property data for rebar materials.

The function returns zero if the data is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignMatPropRebarData()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'initialize new material property
      ret = SapModel.PropMaterial.SetMaterial("Rebar", MATERIAL\_REBAR)

   'assign other properties
      ret = SapModel.PropMaterial.SetORebar("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

This function is obsolete and has been superseded by [SetORebar](SetORebar.htm). This function is maintained for backwards compatibility.

## See Also

[GetORebar](GetORebar.htm)



## SetOSteel

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetOSteel.htm`*

# SetOSteel (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropMaterial.SetOSteel

## VB6 Procedure

Function SetOSteel(ByVal Name As String, ByVal Fy As Double, ByVal Fu As Double, ByVal eFy As Double, ByVal eFu As Double, ByVal SSType As Long, ByVal SSHysType As Long, ByVal StrainAtHardening As Double, ByVal StrainAtMaxStress As Double, ByVal StrainAtRupture As Double, Optional ByVal Temp As Double = 0) As Long

## Parameters

Name

The name of an existing steel material property.

Fy

The minimum yield stress. [F/L2]

Fu

The minimum tensile stress. [F/L2]

eFy

The expected yield stress. [F/L2]

eFu

The expected tensile stress. [F/L2]

SSType

This is 0 or 1, indicating the stress-strain curve type.

0 = User defined

1 = Parametric - Simple

SSHysType

This is 0, 1 or 2, indicating the stress-strain hysteresis type.

0 = Elastic

1 = Kinematic

2 = Takeda

StrainAtHardening

This item applies only to parametric stress-strain curves. It is the strain at the onset of strain hardening.

StrainAtMaxStress

This item applies only to parametric stress-strain curves. It is the strain at maximum stress. This item must be larger than the StrainAtHardening item.

StrainAtRupture

This item applies only to parametric stress-strain curves. It is the strain at rupture. This item must be larger than the StrainAtMaxStress item.

Temp

This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.

This item is the temperature at which the specified data applies. The temperature must have been defined previously for the material.

## Remarks

This function sets the other material property data for steel materials.

The function returns zero if the data is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignMatPropSteelData()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'initialize new material property
      ret = SapModel.PropMaterial.SetMaterial("Steel", MATERIAL\_STEEL)

   'assign other properties
      ret = SapModel.PropMaterial.SetOSteel("Steel", 55, 68, 60, 70, 1, 2, 0.02, 0.1, 0.2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

This function is obsolete and has been superseded by [SetOSteel\_1](../Definitions/Properties/Material/SetOSteel_1.htm) as of version 12.00. This function is maintained for backwards compatibility.

## See Also

[GetOSteel](GetOSteel.htm)



## SetOTendon

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetOTendon.htm`*

# SetOTendon (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropMaterial.SetOTendon

## VB6 Procedure

Function SetOTendon(ByVal Name As String, ByVal Fy As Double, ByVal Fu As Double, ByVal SSType As Long, ByVal SSHysType As Long, Optional ByVal Temp As Double = 0) As Long

## Parameters

Name

The name of an existing tendon material property.

Fy

The minimum yield stress. [F/L2]

Fu

The minimum tensile stress. [F/L2]

SSType

This is 0, 1 or 2, indicating the stress-strain curve type.

0 = User defined

1 = Parametric – 250 ksi strand

2 = Parametric – 270 ksi strand

SSHysType

This is 0, 1 or 2, indicating the stress-strain hysteresis type.

0 = Elastic

1 = Kinematic

2 = Takeda

Temp

This item applies only if the specified material has properties that are temperature dependent. That is, it applies only if properties are specified for the material at more than one temperature.

This item is the temperature at which the specified data applies. The temperature must have been defined previously for the material.

## Remarks

This function sets the other material property data for tendon materials.

The function returns zero if the data is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignMatPropTendonData()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'initialize new material property
      ret = SapModel.PropMaterial.SetMaterial("Tendon", MATERIAL\_TENDON)

   'assign other properties
      ret = SapModel.PropMaterial.SetOTendon("Tendon", 230, 255, 1, 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

This function is obsolete and has been superseded by [SetOTendon\_1](../Definitions/Properties/Material/SetOTendon_1.htm) as of version 12.00. This function is maintained for backwards compatibility.

## See Also

[GetOTendon](GetOTendon.htm)



## SetOverwrite {Concrete Chinese 2002}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetOverwrite_{Concrete_Chinese_2002}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignConcrete.Chinese\_2002.SetOverwrite

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

Sub SetConcreteDesignOverwriteItemChinese\_2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'createSap2000 object
      Set SapObject= New Sap2000v15.SapObject

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
      ret= SapModel.DesignConcrete.SetCode("Chinese 2002")

   'set overwrite item
      ret= SapModel.DesignConcrete.Chinese\_2002.SetOverwrite("8", 1, 2)

   'closeSap2000
      SapObject.ApplicationExit False
      Set SapModel= Nothing
      Set SapObject= Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added Items 17 and 18 in Version 14.0.0.

## See Also

[GetOverwrite](GetOverwrite_{Concrete_Chinese_2002}.htm)



## SetOverwrite {Steel Chinese 2002}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetOverwrite_{Steel_Chinese_2002}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Chinese\_2002.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 51, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Element type

3 = Is transfer column

4 = Seismic magnification factor

5 = Is rolled section

6 = Is flange edge cut by gas

7 = Is both end pinned

8 = Ignore b/t check

9 = Classify beam as flexo-compression member

10 = Is beam top loaded

11 = Consider deflection

12 = Deflection check type

13 = DL deflection limit, L/Value

14 = SDL + LL deflection limit, L/Value

15 = LL deflection limit, L/Value

16 = Total load deflection limit, L/Value

17 = Total camber limit, L/Value

18 = DL deflection limit, absolute

19 = SDL + LL deflection limit, absolute

20 = LL deflection limit, absolute

21 = Total load deflection limit, absolute

22 = Total camber limit, absolute

23 = Specified camber

24 = Net area to total area ratio

25 = Live load reduction factor

26 = Unbraced length ratio, Major

27 = Unbraced length ratio, Minor Lateral TorsionalBuckling

28 = Effective length factor, Mue Major

29 = Effective length factor, Mue Minor

30 = Moment coefficient, Beta\_m Major

31 = Moment coefficient, Beta\_m Minor

32 = Moment coefficient, Beta\_t Major

33 = Moment coefficient, Beta\_t Minor

34 = Axial stability coefficient, Phi Major

35 = Axial stability coefficient, Phi Minor

36 = Flexural stability coeff, Phi\_bMajor

37 = Flexural stability coeff, Phi\_bMinor

38 = Plasticity factor, Gamma Major

39 = Plasticity factor, Gamma Minor

40 = Section influence coefficient, Eta

41 = B/C capacity factor, Eta

42 = Euler moment factor, Delta Major

43 = Euler moment factor, Delta Minor

44 = Yield stress, Fy

45 = Allowable normal stress, f

46 = Allowable shear stress, fv

47 = Consider fictitious shear

48 = Demand/capacity ratio limit

49 = Dual system magnification factor

50 = Lo/r limit in compression

51 = L/r limit in tension

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Sway Moment Frame, SMF

2 = Concentrically Braced Frame, CBF

3 = Eccentrically Braced Frame, EBF

4 = NonSway Moment Frame, NMF

2 = Element type

0 = Program Determined

1 = Column

2 = Beam

3 = Brace

4 = Truss

3 = Is transfer column

0 = Program Determined

1 = No

2 = Yes

4 = Seismic magnification factor

Value >= 0; 0 means no check for this item.

5 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

6 = Is flange edge cut by gas

0 = Program Determined

1 = No

2 = Yes

7 = Is both end pinned

0 = Program Determined

1 = No

2 = Yes

8 = Ignore b/t check

0 = Program Determined

1 = No

2 = Yes

9 = Classify beam as flexo-compression member

0 = Program Determined

1 = No

2 = Yes

10 = Is beam top loaded

0 = Program Determined

1 = No

2 = Yes

11 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

12 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

13 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

14 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

15 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

16 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

17 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

18 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

19 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

20 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

21 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

22 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

23 = Specified camber

Value >= 0. [L]

24 = Net area to total area ratio

Value >= 0; 0 means use program default value.

25 = Live load reduction factor

Value >= 0; 0 means use program determined value.

26 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

27 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

28 = Effective length factor, Mue Major

Value >= 0; 0 means use program determined value.

29 = Effective length factor, Mue Minor

Value >= 0; 0 means use program determined value.

30 = Moment coefficient, Beta\_m Major

Value >= 0; 0 means use program determined value.

31 = Moment coefficient, Beta\_m Minor

Value >= 0; 0 means use program determined value.

32 = Moment coefficient, Beta\_t Major

Value >= 0; 0 means use program determined value.

33 = Moment coefficient, Beta\_t Minor

Value >= 0; 0 means use program determined value.

34 = Axial stability coefficient, Phi Major

Value >= 0; 0 means use program determined value.

35 = Axial stability coefficient, Phi Minor

Value >= 0; 0 means use program determined value.

36 = Flexural stability coefficient, Phi\_b Major

Value >= 0; 0 means use program determined value.

37 = Flexural stability coefficient, Phi\_b Minor

Value >= 0; 0 means use program determined value.

38 = Plasticity factor, Gamma Major

Value >= 0; 0 means use program determined value.

39 = Plasticity factor, Gamma Minor

Value >= 0; 0 means use program determined value.

40 = Section influence coefficient, Eta

Value >= 0; 0 means use program determined value.

41 = B/C capacity factor, Eta

Value >= 0; 0 means use program determined value.

42 = Euler moment factor, Delta Major

Value >= 0; 0 means use program determined value.

43 = Euler moment factor, Delta Minor

Value >= 0; 0 means use program determined value.

44 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

45 = Allowable normal stress, f

Value >= 0; 0 means use program determined value. [F/L2]

46 = Allowable shear stress, fv

Value >= 0; 0 means use program determined value. [F/L2]

47 = Consider fictitious shear

0 = Program Determined

1 = No

2 = Yes

48 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value

49 = Dual system magnification factor

        Value >= 0; 0 means use program default value.

50 = Lo/r limit in compression

        Value >= 0; 0 means use program determined value.

51 = L/r limit in tension

        Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects= 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemChinese\_2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Chinese 2002")

   'set overwrite item
      ret = SapModel.DesignSteel.Chinese\_2002.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added Items 49, 50, and 51 in Version 14.0.0.

Modified Item 1 and added Truss to Item 2 in version 14.1.0.

## See Also

[GetOverwrite](GetOverwrite_{Steel_Chinese_2002}.htm)



## SetOverwrite {Steel Eurocode 3 2005}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetOverwrite_{Steel_Eurocode_3_2005}.htm`*

# SetOverwrite (Note:  Deprecated, Newer Function Available)

## Syntax

SapObject.SapModel.DesignSteel.Eurocode\_3\_2005.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 54, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit,
L/Value

5 = SDL + LL deflection
limit, L/Value

6 = LL deflection limit,
L/Value

7 = Total load deflection
limit, L/Value

8 = Total camber limit,
L/Value

9 = DL deflection limit,
absolute

10 = SDL + LL deflection
limit, absolute

11 = LL deflection limit,
absolute

12 = Total load deflection
limit, absolute

13 = Total camber limit,
absolute

14 = Specified camber

15 = Net area to total
area ratio

16 = Live load reduction
factor

17 = Unbraced length ratio,
y-y

18 = Unbraced length ratio,
z-z

19 = Effective length
factor, K2y

20 = Effective length
factor, K2z

21 = Moment coefficient,
kyy

22 = Moment coefficient,
kzz

23 = Bending coefficient,
C1

24
= Moment coefficient, kzy

25
= Moment coefficient, kyz

26 = Yield stress, Fy

27 = Compressive capacity,
Nc.Rd

28 = Tensile capacity,
Nt.Rd

29 = Bending capacity
about y-y axis,Mcy.Rd

30 = Bending capacity
about z-z axis Mcz.Rd

31 = Buckling resistance
moment, Mb.Rd

32 = Shear capacity along
z-z axis, Vz.Rd

33 = Shear capacity along
y-y axis, Vy.Rd

34 = Demand/capacity ratio
limit

35 = Section class

36 = Column buckling curve,
y-y

37 = Column buckling curve,
z-z

38 = Buckling curve for LTB

39 = System overstrength factor,
Omega

40 = Is rolled section

41 = Unbraced length ratio,
LTB

42 = Effective length factor
braced, K1y

43 = Effective length factor
braced, K1z

44 = Effective length factor,
K LTB

45 = Material overstrength
factor, GammaOV

46 = Warping constant, Iw

47 = Elastic torsional buckling
force, Ncr T

48 = Elastic torsional-flexural
buckling force, Ncr TF

49 = Bending coefficient,
C2

50 = Bending coefficient,
C3

51 = Warping coefficient,
kw

52 = Coordinate
of load application, za (used in Mcr calculation)

53
= Shear center coordinate, zs (used in Mcr calculation)

54
= Elastic critical moment for lateral-torsional buckling, Mcr

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = DCH MRF (Ductility
Class High – Moment Frame)

2 = DCM MRF (Ductility
Class Medium – Moment Frame)

3 = DCL MRF (Ductility
Class Low – Moment Frame)

4 = DCH CBF (Ductility
Class High – Concentrically Braced Frame)

5 = DCM CBF (Ductility
Class Medium – Concentrically Braced Frame)

6 = DCL CBF (Ductility
Class Low – Concentrically Braced Frame)

7 = DCH EBF (Ductility
Class High – Eccentrically Braced Frame)

8 = DCM EBF (Ductility
Class Medium – Eccentrically Braced Frame)

9 = DCL EBF (Ductility
Class Low – Eccentrically Braced Frame)

10 = Inverted pendulum
structure

11 = Secondary

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

5 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

6 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

7 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

8 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

9 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

10 = SDL + LL deflection
limit, absolute

Value >= 0; 0 means
no check for this item. [L]

11 = LL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

12 = Total load deflection
limit, absolute

Value >= 0; 0 means
no check for this item. [L]

13 = Total camber limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total
area ratio

Value >= 0; 0 means
use program default value.

16 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

17 = Unbraced length ratio,
y-y

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
z-z

  Value >=
0; 0 means use program determined value.

19 = Effective length
factor sway, K2y

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor sway, K2z

  Value >=
0; 0 means use program determined value.

21 = Moment coefficient,
kyy

  Value >=
0; 0 means use program determined value.

22 = Moment coefficient,
kzz

  Value >=
0; 0 means use program determined value.

23 = Bending coefficient,
C1

  Value >=
0; 0 means use program determined value.

24 = Moment coefficient,
kzy

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
kyz

  Value >=
0; 0 means use program determined value.

26 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

27 = Compressive capacity,
Nc.Rd

  Value >=
0; 0 means use program determined value. [F]

28 = Tensile capacity,
Nt.Rd

  Value >=
0; 0 means use program determined value. [F]

29 = Bending capacity
about y-y axis, Mcy.Rd

  Value >=
0; 0 means use program determined value. [FL]

30 = Bending capacity
about z-z axis, Mcz.Rd

  Value >=
0; 0 means use program determined value. [FL]

31 = Buckling resistance
moment, Mb.Rd

  Value >=
0; 0 means use program determined value. [FL]

32 = Shear capacity along
z-z axis, Vz.Rd

  Value >=
0; 0 means use program determined value. [F]

33 = Shear capacity along
y-y axis, Vy.Rd

  Value >=
0; 0 means use program determined value. [F]

34 = Demand/capacity ratio
limit

  Value >= 0;
0 means use program determined value.

35 = Section class

0 = Program default

1 = Class 1

2 = Class 2

3 = Class 3

4 = Class 4

36 = Column buckling curve,
y-y

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

37 = Column buckling curve,
z-z

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

38
= Buckling curve for LTB

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

39 = System overstrength factor,
Omega

Value >= 0; 0 means use
program determined value.

40 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

41 = Unbraced length ratio,
LTB

Value >= 0; 0 means use
program determined value.

42 = Effective length factor
braced, K1y

Value >= 0; 0 means use
program determined value.

43 = Effective length factor
braced, K1z

Value >= 0; 0 means use
program determined value.

44 = Effective length factor,
K LTB

Value >= 0; 0 means use
program determined value.

45 = Material overstrength
factor, GammaOV

Value >= 0; 0 means use
program determined value.

46 = Warping constant, Iw

Value >= 0; 0 means use
program determined value. [L6]

47 = Elastic torsional buckling
force, Ncr T

Value >= 0; 0 means use
program determined value. [F]

48 = Elastic torsional-flexural
buckling force, Ncr TF

Value >= 0; 0 means use
program determined value. [F]

49
= Bending coefficient, C2

Value >= 0; 0 means
use program determined value.

50 = Bending coefficient,
C3

Value >= 0; 0 means
use program determined value.

51 = Warping coefficient,
kw (used in Mcr calculation)

0.5 =<Value =<
1; 0 means use program determined value which is defaulted to 1.0.

52 = Coordinate of load application, za
(used in Mcr calculation)

53
= Shear center coordinate, zs (used in Mcr calculation)

54
= Elastic critical moment for lateral-torsional buckling, Mcr

Value >=
0; 0 means use program determined value. [FL]

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
to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite
item.

The function returns zero if the item is successfully
set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemEurocode\_3\_2005()
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
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Eurocode
3-2005")

   'set overwrite item
      ret = SapModel.DesignSteel.EUROCODE\_3\_2005.SetOverwrite("8",
1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.0.0.

In version 14.1.0, fixed typographical error.

Updated the list of items in v18.0.0.

Added items 46 – 48 in v18.2.0.

Added items 49 - 52 in v22.0.0

Included all framing types as in Preference form in
SAP2000 Version 22.1.0

Added items 53 - 54 in v22.0.0

Changed references from major and minor axes to y-y
and z-z in version 23.4.0.

The function is DEPRECATED as of version 25.1. Please
use [Set Overwrite](SetOverwrite_{Steel_Eurocode_3_2005}.htm)
. This topic is maintained for reference.

## See Also

[GetOverwrite](GetOverwrite_{Steel_Eurocode_3_2005}.htm)



## SetPrecastI

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetPrecastI.htm`*

# SetPrecastI (Note: Newer Function Available)

## Syntax

SapObject.SapModel.PropFrame.SetPrecastI

## VB6 Procedure

Function SetPrecastI(ByVal Name As String, ByVal MatProp As String, ByRef b() As Double, ByRef d() As Double, Optional ByVal Color As Long = -1, Optional ByVal Notes As String = "", Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing or new frame section property. If this is an existing property, that property is modified; otherwise, a new property is added.

MatProp

The name of the material property for the section.

b

This is an array, dimensioned to 3, containing the horizontal section dimensions. [L]

b(0) = B1 (> 0)

b(1) = B2 (> 0)

b(2) = B3 (> 0)

b(3) = B4 (>= 0)

Section dimensions B1 through B4 are defined on the precast concrete I girder definition form.

d

This is an array, dimensioned to 5, containing the vertical section dimensions. [L]

d(0) = D1 (> 0)

d(1) = D2 (> 0)

d(2) = D3 (>= 0)

d(3) = D4 (>= 0)

d(4) = D5 (>= 0)

d(5) = D6 (> 0)

Section dimensions D1 through D6 are defined on the precast concrete I girder definition form.

Color

The display color assigned to the section. If Color is specified as -1, the program will automatically assign a color.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned to the section. If this item is input as Default, the program assigns a GUID to the section.

## Remarks

This function initializes a precast concrete I girder frame section property. If this function is called for an existing frame section property, all items for the section are reset to their default value.

The function returns zero if the section property is successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetFramePropPrecastI()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim bb() As Double
      Dim dd() As Double

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

   'set new frame section property
      ReDim bb(3)
      ReDim dd(5)
      bb(0) = 16
      bb(1) = 22
      bb(2) = 7
      bb(3) = 0
      dd(0) = 45
      dd(1) = 7
      dd(2) = 4.5
      dd(3) = 0
      dd(4) = 7.5
      dd(5) = 7
      ret = SapModel.PropFrame.SetPrecastI("PC1", "4000Psi", bb, dd)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

The function is obsolete and has been superseded by SetPrecastI\_1 as of version 17.2.0. This function is maintained for backward compatibility.

## See Also

[GetPrecastI](GetPrecastI.htm)



## SetPreference {Concrete Chinese 2002}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetPreference_{Concrete_Chinese_2002}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignConcrete.Chinese\_2002.SetPreference

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

Sub SetConcreteDesignPreferenceItemChinese\_2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

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
      ret = SapModel.DesignConcrete.SetCode("Chinese 2002")

   'set preference item
      ret = SapModel.DesignConcrete.Chinese\_2002.SetPreference(2, 9)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added Items 9, 10, and 11 in Version 14.0.0.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Concrete_Chinese_2002}.htm)



## SetPreference {Steel Chinese 2002}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetPreference_{Steel_Chinese_2002}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Chinese\_2000.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1 = Framing type

2 = Gamma0

3 = Ignore b/t check

4 = Classify beam as flexo compression member

5 = Consider deflection

6 = DL deflection limit, L/Value

7 = SDL + LL deflection limit, L/Value

8 = LL deflection limit, L/Value

9 = Total load deflection limit, L/Value

10 = Total camber limit, L/Value

11 = Pattern live load factor

12 = Demand/capacity ratio limit

13 = Multi-response case design

14 = Is tall building?

Value

The value of the considered preference item.

1 = Framing type

0 = As specified in preferences

1 = Sway Moment Frame, SMF

2 = Concentrically Braced Frame, CBF

3 = Eccentrically Braced Frame, EBF

4 = NonSway Moment Frame, NMF

2 = Gamma0

Value > 0

3 = Ignore b/t check

0 = No

Any other value = Yes

4 = Classify beam as flexo compression member

0 = No

Any other value = Yes

5 = Consider deflection

0 = No

Any other value = Yes

6 = DL deflection limit, L/Value

Value > 0

7 = SDL + LL deflection limit, L/Value

Value > 0

8 = LL deflection limit, L/Value

Value > 0

9 = Total load deflection limit, L/Value

Value > 0

10 = Total camber limit, L/Value

Value > 0

11 = Pattern live load factor

Value >= 0

12 = Demand/capacity ratio limit

Value > 0

13 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

14 = Tall building

        0 = No

        1 = Yes

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemChinese\_2002()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Chinese 2002")

   'set preference item
      ret = SapModel.DesignSteel.Chinese\_2002.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added Item 14 in Version 14.0.0.

Modified Item 1 in version 14.1.0.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_Chinese_2002}.htm)



## SetPreference {Steel Eurocode 3 2005}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetPreference_{Steel_Eurocode_3_2005}.htm`*

# SetPreference (Note:  Deprecated, Newer Function Available)

## Syntax

SapObject.SapModel.DesignSteel.Eurocode\_3\_2005.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 16, inclusive, indicating
the preference item considered.

1 = Country

2 = Combos equation

3 = Reliability class

4 = K factor method

5 = Multi-response case
design

6 = Framing type

7 = Behavior factor, q

8 = System overstrength
factor, Omega

9 = Consider P-Delta Done

10 = Consider torsion

11 = GammaM0

12 = GammaM1

13 = GammaM2

14 = Ignore seismic code

15 = Ignore special seismic
load

16 = Doubler plate is
plug-welded

17 = Consider deflection

18 = DL deflection limit,
L/Value

19 = SDL + LL deflection
limit, L/Value

20 = LL deflection limit,
L/Value

21 = Total deflection
limit, L/Value

22 = Total camber limit,
L/Value

23 = Pattern live load
factor

24 = Demand/capacity ratio
limit

Value

The value of the considered preference item.

1 = Country

   1 =
CEN Default

   2 =
United Kingdom

   3 =
Slovenia

   4 =
Bulgaria

   5 =
Norway

   7 =
Sweden

   8 =
Finland

   9 =
Denmark

 10 = Portugal

 11 = Germany

2 = Combos equation

   1 =
1 = Eq. 6.10

   2 =
Max of Eqs. 6.10a and 6.10b

3 = Reliability class

   1 =
Class 1

   2 =
Class 2

   3 =
Class 3

4 = K factor method

   1 =
Method 1 (Annex A)

   2 =
Method 2 (Annex B)

5 = Multi-response case
design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step --  All

6 = Framing type

1 = DCH MRF (Ductility
Class High - Moment Frame)

2 = DCM MRF (Ductility
Class Medium - Moment Frame)

3 = DCL MRF (Ductility
Class Low - Moment Frame)

4 = DCH CBF (Ductility
Class High - Concentrically Braced Frame)

5 = DCH CBF (Ductility
Class Medium - Concentrically Braced Frame)

6 = DCH CBF (Ductility
Class Low - Concentrically Braced Frame)

7 = DCH EBF (Ductility
Class High - Eccentrically Braced Frame)

8 = DCM EBF (Ductility
Class Medium - Eccentrically Braced Frame)

9 = DCL EBF (Ductility
Class Low - Eccentrically Braced Frame)

10 = Inverted pendulum
structure

11 = Secondary

7 = Behavior factor, q

Value > 0

8 = System overstrength
factor, Omega

Value > 0

9 = Consider P-Delta Done

0 = No

Any other value = Yes

10 = Consider torsion

0 = No

Any other value = Yes

11 = GammaM0

Value > 0

12 = GammaM1

Value > 0

13 = GammaM2

      Value
> 0

14 = Ignore seismic code

0 = No

Any other value = Yes

15 = Ignore special seismic
load

0 = No

Any other value = Yes

16 = Doubler plate is
plug-welded

0 = No

Any other value = Yes

17 = Consider deflection

0 = No

Any other value = Yes

18 = DL deflection limit,
L/Value

Value > 0

19 = SDL + LL deflection
limit, L/Value

  Value >
0

20 = LL deflection limit,
L/Value

  Value >
0

21 = Total deflection
limit, L/Value

  Value >
0

22 = Total camber limit,
L/Value

  Value >
0

23 = Pattern live load
factor

  Value >=
0

24 = Demand/capacity ratio
limit

  Value >
0

## Remarks

This function sets the value of a steel design preference
item.

The function returns zero if the item is successfully
set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemEurocode\_3\_2005()
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
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Eurocode
3-2005")

   'set preference item
      ret = SapModel.DesignSteel.Eurocode\_3\_2005.SetPreference(4,
2)

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

Included all parameters and all framing types as in
Preference form in SAP2000 Version 22.1.0

The function is DEPRECATED as of version 25.1. Please
use [Set
Preferences](../Design/Steel/EN_1993_1_1_2005_(Formerly_Eurocode_3-2005)/SetPreference_{Steel_EN_1993-1-1_2005}.htm). This topic is maintained for reference.

## See Also

[GetPreference](GetPreference_{Steel_Eurocode_3_2005}.htm)



## SetProp {Solid}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetProp_{Solid}.htm`*

# SetProp (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropSolid.SetProp

## VB6 Procedure

Function SetProp(ByVal Name As String, ByVal MatProp As String, ByVal a As Double, ByVal B As Double, ByVal c As Double, ByVal Incompatible As Boolean, Optional ByVal Color As Long = -1, Optional ByVal Notes As String = "", Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing or new solid property. If this is an existing property, that property is modified; otherwise, a new property is added.

MatProp

The name of the material property assigned to the solid property.

a

The material angle A. [deg]

b

The material angle B. [deg]

c

The material angle C. [deg]

Incompatible

If this item is True, incompatible bending modes are included in the stiffness formulation. In general, incompatible modes significantly improve the bending behavior of the object.

Color

The display color assigned to the property. If Color is specified as -1, the program will automatically assign a color.

Notes

The notes, if any, assigned to the property.

GUID

The GUID (global unique identifier), if any, assigned to the property. If this item is input as Default, the program assigns a GUID to the property.

## Remarks

This function defines a solid property.

The function returns zero if the property is successfully defined; otherwise it returns a nonzero value.

## VBA Example

Sub SetSolidProperty()
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
      ret = SapModel.File.NewSolidBlock(20, 50, 20)

   'set new solid property
      ret = SapModel.PropSolid.SetProp("S1", "4000Psi", 0, 10, 20, True)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

The function is obsolete and has been superseded by [SetProp\_1](../Definitions/Properties/Solid/SetProp_1_{Solid}.htm) as of version 26.40. This function is maintained for backward compatibility, but the parameter Incompatible is no longer applicable so its value will not be applied to the property.

## See Also

[SetProp\_1](../Definitions/Properties/Solid/SetProp_1_{Solid}.htm)

[GetProp\_1](../Definitions/Properties/Solid/GetProp_1_{Solid}.htm)



## SetShell

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetShell.htm`*

# SetShell  (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropArea.SetShell

## VB6 Procedure

Function SetShell(ByVal Name As String, ByVal ShellType As Long, ByVal MatProp As String, ByVal MatAng As Double, ByVal Thickness As Double, ByVal Bending As Double, Optional ByVal Color As Long = -1, Optional ByVal Notes As String = "", Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing or new area property. If this is an existing property, that property is modified; otherwise, a new property is added.

ShellType

This is 1, 2, 3, 4, 5 or 6, indicating the shell type.

1 = Shell - thin

2 = Shell - thick

3 = Plate - thin

4 = Plate - thick

5 = Membrane

6 = Shell layered/nonlinear

MatProp

The name of the material property for the area property. This item does not apply when ShellType = 6.

MatAng

The material angle. [deg]

This item does not apply when ShellType = 6.

Thickness

The membrane thickness. [L]

This item does not apply when ShellType = 6.

Bending

The bending thickness. [L]

This item does not apply when ShellType = 6.

Color

The display color assigned to the property. If Color is specified as -1, the program will automatically assign a color.

Notes

The notes, if any, assigned to the property.

GUID

The GUID (global unique identifier), if any, assigned to the property. If this item is input as Default, the program assigns a GUID to the property.

## Remarks

This function initializes a shell-type area property. If this function is called for an existing area property, all items for the property are reset to their default value.

The function returns zero if the property is successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetAreaPropShell()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'set new area property
      ret = SapModel.PropArea.SetShell("A1", 1, "4000Psi", 0, 16, 16)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

The function is obsolete and has been superseded by [SetShell\_1](../definitions/properties/area/SetShell_1.htm) as of version 14.00. This function is maintained for backward compatibility. New function added

## See Also

[GetShell](GetShell.htm)



## SetShellLayer

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetShellLayer.htm`*

# SetShellLayer (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropArea.SetShellLayer

## VB6 Procedure

Function SetShellLayer(ByVal Name As String, ByVal NumberLayers As Long, ByRef LayerName() As String, ByRef Dist() As Double, ByRef Thickness() As Double, ByRef MatProp() As String, ByRef NonLinear() As Boolean, ByRef MatAng() As Double, ByRef NumIntegrationPts() As Long) As Long

## Parameters

Name

The name of an existing shell-type area property that is specified to be a layered shell property.

NumberLayers

The number of layers in the area property.

LayerName

This is an array that includes the name of each layer.

Dist

This is an array that includes the distance from the area reference surface (area object joint location plus offsets) to the midheight of the layer. [L]

Thickness

This is an array that includes the thickness of each layer. [L]

MatProp

This is an array that includes the name of the material property for the layer.

NonLinear

This is an array that includes a boolean (True or False) value. If this item is True, and if the material property assigned to the layer is nonlinear, the layer will behave nonlinearly in a nonlinear load case. If this item is False, the layer will never behave nonlinearly.

MatAng

This is an array that includes the material angle for the layer. [deg]

NumIntegrationPts

The number of integration points in the thickness direction for the layer. The locations are determined by the program using standard Guass-quadrature rules.

## Remarks

This function assigns the layer parameters for shell-type area properties.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

The function returns an error if the specified area property is not a shell-type property specified to be a layered shell.

## VBA Example

Sub SetAreaPropShellLayer()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim MyNumberLayers As Long
      Dim MyLayerName() As String
      Dim MyDist() As Double
      Dim MyThickness() As Double
      Dim MyMatProp() As String
      Dim MyNonLinear() As Boolean
      Dim MyMatAng() As Double
      Dim MyNumIntegrationPts() As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'set new area property
      ret = SapModel.PropArea.SetShell("A1", 6, "", 0, 0, 0)

   'add A615Gr60 rebar material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_REBAR, , , , , MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr60)

   'set area property layer parameters
      MyNumberLayers = 5
      ReDim MyLayerName(MyNumberLayers - 1)
      ReDim MyDist(MyNumberLayers - 1)
      ReDim MyThickness(MyNumberLayers - 1)
      ReDim MyMatProp(MyNumberLayers - 1)
      ReDim MyNonLinear(MyNumberLayers - 1)
      ReDim MyMatAng(MyNumberLayers - 1)
      ReDim MyNumIntegrationPts(MyNumberLayers - 1)

      MyLayerName(0) = "Concrete"
      MyDist(0) = 0
      MyThickness(0) = 16
      MyMatProp(0) = "4000Psi"
      MyNonLinear(0) = False
      MyMatAng(0) = 0
      MyNumIntegrationPts(0) = 2

      MyLayerName(1) = "Top Bar 1"
      MyDist(1) = 6
      MyThickness(1) = 0.03
      MyMatProp(1) = Name
      MyNonLinear(1) = False
      MyMatAng(1) = 0
      MyNumIntegrationPts(1) = 1

      MyLayerName(2) = "Top Bar 2"
      MyDist(2) = 6
      MyThickness(2) = 0.03
      MyMatProp(2) = Name
      MyNonLinear(2) = False
      MyMatAng(2) = 90
      MyNumIntegrationPts(2) = 1

      MyLayerName(3) = "Bot Bar 1"
      MyDist(3) = -6
      MyThickness(3) = 0.03
      MyMatProp(3) = Name
      MyNonLinear(3) = False
      MyMatAng(3) = 0
      MyNumIntegrationPts(3) = 1

      MyLayerName(4) = "Bot Bar 2"
      MyDist(4) = -6
      MyThickness(4) = 0.03
      MyMatProp(4) = Name
      MyNonLinear(4) = False
      MyMatAng(4) = 90
      MyNumIntegrationPts(4) = 1

      ret = SapModel.PropArea.SetShellLayer("A1", MyNumberLayers, MyLayerName, MyDist, MyThickness, MyMatProp, MyNonLinear, MyMatAng, MyNumIntegrationPts)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

This function is obsolete and has been superseded by [SetShellLayer\_1](../Definitions/Properties/Area/SetShellLayer_1.htm) as of version 12.5. This function is maintained for backwards compatibility.

## See Also

[GetShellLayer](GetShellLayer.htm)

[GetShellLayer\_1](../Definitions/Properties/Area/GetShellLayer_1.htm)



## SetSolverOption

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetSolverOption.htm`*

# SetSolverOption (Note:  Newer function available)

## Syntax

SapObject.SapModel.Analyze.SetSolverOption

## VB6 Procedure

Function SetSolverOption(ByVal SolverType As Long, ByVal Force32BitSolver As Boolean, Optional ByVal StiffCase As String = "") As Long

## Parameters

SolverType

This is 0 or 1, indicating the solver type.

0 = Standard solver

1 = Advanced solver

Force32BitSolver

This is True if the analysis is always run using 32-bit, even on 64-bit computers.

StiffCase

The name of the load case used when outputting the mass and stiffness matrices to text files. If this item is blank, no matrices are output.

## Remarks

This function sets the model solver options.

The function returns zero if the options are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetModelSolverOption()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set model solver options
      ret = SapModel.Analyze.SetSolverOption(1, True, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

This function is obsolete and has been superseded by [SetSolverOption\_1](SetSolverOption_1.htm) as of version 14.2.2. This function is maintained for backwards compatibility.

## See Also

[GetSolverOption](GetSolverOption.htm)



## SetSolverOption_1

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetSolverOption_1.htm`*

# SetSolverOption\_1 (Note:  Newer function available)

## Syntax

SapObject.SapModel.Analyze.SetSolverOption\_1

## VB6 Procedure

Function SetSolverOption(ByVal SolverType As Long, ByVal
SolverProcessType As Long, ByVal Force32BitSolver As Boolean, Optional
ByVal StiffCase As String = "") As Long

## Parameters

SolverType

This is 0, 1 or 2, indicating the solver type.

0 = Standard solver

1 = Advanced solver

2
= Multi-threaded solver

SolverProcessType

This is 0, 1 or 2, indicating the process the analysis
is run.

0 = Auto (program determined)

1 = GUI process

2
= Separate process

Force32BitSolver

This is True if the analysis is always run using 32-bit,
even on 64-bit computers.

StiffCase

The name of the load case used when outputting the mass
and stiffness matrices to text files If this item is blank, no matrices
are output.

## Remarks

This function sets the model solver options.

The function returns zero if the options are successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetModelSolverOption()
   'dimension variables
      Dim SapObject as
cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject =
New SAP2000.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel =
SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set model solver options
      ret = SapModel.Analyze.SetSolverOption\_1(1,
1, True, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit
False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.2.2

This function is obsolete and has been superseded by
[SetSolverOption\_2](NEW_-_Analyze.SetSolverOption_2.htm) as
of version 21.1.0. This function is maintained for backwards compatibility.

This function supersedes [SetSolverOption](SetSolverOption.htm).

## See Also

[GetSolverOption\_1](GetSolverOption_1.htm)



## setstagedata

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetStageData.htm`*

# SetStageData  (Note:  Newer Function Available)

## Syntax

SapObject.SapModel.LoadCases.StaticNonlinear.SetStageData

## VB6 Procedure

Function SetStageData(ByVal Name As String, ByVal Stage As Long, ByVal NumberOperations As Long, ByRef Operation() As Long, ByRef GroupName() As String, ByRef Age() As Long, ByRef LoadType() As String, ByRef LoadName() As String, ByRef SF() As Double) As Long

## Parameters

Name

The name of an existing static nonlinear staged analysis case.

Stage

The stage in the specified load case to which the data applies. Stages are numbered sequentially starting from 1.

NumberOperations

The number of operations in the specified stage.

Operation

This is an array that includes 1, 2, 3 or 4, indicating an operation type.

1 = Add structure

2 = Remove structure

3 = Load added items in group

4 = Load all items in group

GroupName

This is an array that includes the name of the group associated with the specified operation.

Age

This is an array that includes the age of the added structure, at the time it is added, in days. This item applies only to operations with Operation = 1.

LoadType

This is an array that includes either Load or Accel, indicating the load type of an added load. This item applies only to operations with Operation = 3 or 4.

LoadName

This is an array that includes the name of the load assigned to the operation. This item applies only to operations with Operation = 3 or 4.

If the associated LoadType item is Load, this item is the name of a defined load pattern.

If the associated LoadType item is Accel, this item is UX, UY, UZ, RX, RY or RZ, indicating the direction of the load.

SF

This is an array that includes the scale factor for the load assigned to the operation. [L/s2] for Accel UX UY and UZ; otherwise unitless

This item applies only to operations with Operation = 3 or 4.

## Remarks

This function sets the stage data for the specified stage in the specified load case. All previous stage data for the specified stage is cleared when this function is called.

The function returns zero if the data is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetCaseStaticNonlinearStagedStageData()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyDuration() As Long
      Dim MyComment() As String
      Dim MyOperation() As Long
      Dim MyGroupName() As String
      Dim MyAge() As Long
      Dim MyLoadType() As String
      Dim MyLoadName() As String
      Dim MySF() As Double

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add static nonlinear staged load case
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetCase("LCASE1")

   'initialize stage definitions
      ReDim MyDuration(1)
      ReDim MyComment(1)
      MyDuration(0) = 0
      MyComment(0) = "Build structure"
      MyDuration(1) = 60
      MyComment(1) = "Wait"
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageDefinitions("LCASE1", 2, MyDuration, MyComment)

   'set stage data
      ReDim MyOperation(1)
      ReDim MyGroupName(1)
      ReDim MyAge(1)
      ReDim MyLoadType(1)
      ReDim MyLoadName(1)
      ReDim MySF(1)
      MyOperation(0) = 1
      MyGroupName(0) = "ALL"
      MyAge(0) = 3
      MyOperation(1) = 4
      MyGroupName(1) = "ALL"
      MyLoadType(1) = "Load"
      MyLoadName(1) = "DEAD"
      MySF(1) = 0.85
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageData("LCASE1", 1, 2, MyOperation, MyGroupName, MyAge, MyLoadType, MyLoadName, MySF)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

This function is obsolete and has been superseded by Stag [SetStageData\_1](SetStageData_1.htm) as of version 12.00.  This function is maintained for backwards compatibility.

## See Also

[GetStageData](GetStageData.htm)



## SetStageData_1

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetStageData_1.htm`*

# SetStageData\_1 (Note: Newer Function Available)

## Syntax

SapObject.SapModel.LoadCases.StaticNonlinear.SetStageData\_1

## VB6 Procedure

Function SetStageData\_1(ByVal Name As String, ByVal Stage As Long, ByVal NumberOperations As Long, ByRef Operation() As Long, ByRef ObjectType() As String, ByRef ObjectName() As String, ByRef Age() As Long, ByRef MyType() As String, ByRef MyName() As String, ByRef SF() As Double) As Long

## Parameters

Name

The name of an existing static nonlinear staged load case.

Stage

The stage in the specified load case to which the data applies. Stages are numbered sequentially starting from 1.

NumberOperations

The number of operations in the specified stage.

Operation

This is an array that includes 1, 2, 3, 4, 5, 6, 7, or 11, indicating an operation type.

1 = Add structure

2 = Remove structure

3 = Load objects if new

4 = Load objects

5 = Change section properties

6 = Change section property modifiers

7 = Change releases

11 = Change section properties and age

ObjectType

This is an array that includes the object type associated with the specified operation. The object type may be one of the following:

Group

Frame

Cable

Tendon

Area

Solid

Link

Point

The following list shows which object types are applicable to each operation type:

Operation = 1 (Add structure):  All object types

Operation = 2 (Remove structure):  All object types

Operation = 3 (Load objects if new):  All object types

Operation = 4 (Load objects):  All object types

Operation = 5 (Change section properties):  All object types except Point

Operation = 6 (Change section property modifiers):  Group, Frame, Cable, Area

Operation = 7 (Change releases):  Group, Frame

Operation = 11 (Change section properties and age): All object types except Point

ObjectName

This is an array that includes the name of the object associated with the specified operation. This is the name of a Group, Frame object, Cable object, Tendon object, Area object, Solid object, Link object or Point object, depending on the ObjectType item.

Age

This is an array that includes the age of the added structure, at the time it is added, in days. This item applies only to operations with Operation = 1.

MyType

This is an array that includes a load type or an object type, depending on what is specified for the Operation item. This item applies only to operations with Operation = 3, 4, 5, 6, 7, or 11.

When Operation = 3 or 4, this is an array that includes Load or Accel, indicating the load type of an added load.

When Operation = 5 or 11, and the ObjectType item is Group, this is an array that includes Frame, Cable, Tendon, Area, Solid or Link, indicating the object type for which the section property is changed.

When Operation = 6 and the ObjectType item is Group, this is an array that includes Frame, Cable or Area, indicating the object type for which the section property modifiers are changed.

When Operation = 7 and the ObjectType item is Group, this is an array that includes Frame, indicating the object type for which the releases are changed.

When Operation = 5, 6, 7, or 11,  and the ObjectType item is not Group and not Point, this item is ignored and the type is picked up from the ObjectType item.

MyName

This is an array that includes a load assignment or an object name, depending on what is specified for the Operation item. This item  applies only to operations with Operation = 3, 4, 5, 6, 7 or 11.

When Operation = 3 or 4, this is an array that includes the name of the load assigned to the operation. If the associated LoadType item is Load, this item is the name of a defined load pattern. If the associated LoadType item is Accel, this item is UX, UY, UZ, RX, RY or RZ, indicating the direction of the load.

When Operation = 5 or 11, this is the name of a Frame, Cable, Tendon, Area, Solid or Link object, depending on the object type specified.

When Operation = 6, this is the name of a Frame, Cable or Area object, depending on the object type specified.

When Operation = 7, this is the name of a Frame object.

SF

This is an array that includes the scale factor for the load assigned to the operation, if any. [L/s2] for Accel UX UY and UZ; otherwise unitless

This item applies only to operations with Operation = 3 or 4.

## Remarks

This function sets the stage data for the specified stage in the specified load case. All previous stage data for the specified stage is cleared when this function is called.

The function returns zero if the data is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetCaseStaticNonlinearStagedStageData\_1()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyDuration() As Long
      Dim MyOutput() As Boolean
      Dim MyOutputName() As String
      Dim MyComment() As String
      Dim MyOperation() As Long
      Dim MyObjectType() As String
      Dim MyObjectName() As String
      Dim MyAge() As Long
      Dim MyMyType() As String
      Dim MyMyName() As String
      Dim MySF() As Double

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

   'add static nonlinear staged load case
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetCase("ACASE1")

   'initialize stage definitions
      ReDim MyDuration(1)
      ReDim MyOutput(1)
      ReDim MyOutputName(1)
      ReDim MyComment(1)
      MyDuration(0) = 0
      MyOutput(0) = False
      MyComment(0) = "Build structure"
      MyDuration(1) = 60
      MyOutput(1) = True
      MyOutputName(1) = "HBC2"
      MyComment(1) = "Wait"
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageDefinitions\_1("ACASE1", 2, MyDuration, MyOutput, MyOutputName, MyComment)

   'set stage data
      ReDim MyOperation(1)
      ReDim MyObjectType(1)
      ReDim MyObjectName(1)
      ReDim MyAge(1)
      ReDim MyMyType(1)
      ReDim MyMyName(1)
      ReDim MySF(1)
      MyOperation(0) = 1
      MyObjectType(0) = "Group"
      MyObjectName(0) = "ALL"
      MyAge(0) = 3
      MyOperation(1) = 4
      MyObjectType(1) = "Frame"
      MyObjectName(1) = "8"
      MyMyType(1) = "Load"
      MyMyName(1) = "DEAD"
      MySF(1) = 0.85
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageData\_1("ACASE1", 1, 2, MyOperation, MyObjectType, MyObjectName, MyAge, MyMyType, MyMyName, MySF)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

Added Operation 11 (Change section properties and age) in version 16.10.

This function supersedes [SetStageData](SetStageData.htm).

This function is obsolete and has been replaced by [SetStageData\_2](SetStageData_1.htm) as of v19.0.0. This function is maintained for backward compatibility

## See Also

[GetStageData\_1](GetStageData_1.htm)



## setstagedefinitions

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetStageDefinitions.htm`*

# SetStageDefinitions (Note:  Newer Function Available)

## Syntax

SapObject.SapModel.LoadCases.StaticNonlinear.SetStageDefinitions

## VB6 Procedure

Function SetStageDefinitions(ByVal Name As String, ByVal NumberStages As Long, ByRef Duration() As Long, ByRef Comment() As String) As Long

## Parameters

Name

The name of an existing static nonlinear staged analysis case.

NumberStages

The number of stages defined for the specified analysis case.

Duration

This is an array that includes the duration in days for each stage.

Comment

This is an array that includes a comment for each stage. The comment may be a blank string.

## Remarks

This function initializes the stage definition data for the specified load case. All previous stage definition data for the case is cleared when this function is called.

The function returns zero if the data is successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetCaseStaticNonlinearStagedStageDefinitions()
   'dimension variables
      Dim SapObject As Sap2000v15.SapObject
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyDuration() As Long
      Dim MyComment() As String

   'create Sap2000 object
      Set SapObject = New Sap2000v15.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add static nonlinear staged load case
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetCase("LCASE1")

   'initialize stage definitions
      ReDim MyDuration(1)
      ReDim MyComment(1)
      MyDuration(0) = 0
      MyComment(0) = "Build structure"
      MyDuration(1) = 60
      MyComment(1) = "Wait"
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageDefinitions("LCASE1", 2, MyDuration, MyComment)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

This function is obsolete and has been superseded by [SetStageDefinitions\_1](SetStageDefinitions_1.htm) as of version 12.00. This function is maintained for backwards compatibility.

## See Also

[GetStageDefinitions](GetStageDefinitions.htm)



## SetStageDefinitions_1

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetStageDefinitions_1.htm`*

# SetStageDefinitions\_1 (Note: Newer Function Available)

## Syntax

SapObject.SapModel.LoadCases.StaticNonlinear.SetStageDefinitions\_1

## VB6 Procedure

Function SetStageDefinitions\_1(ByVal Name As String, ByVal NumberStages As Long, ByRef Duration() As Long, ByRef Output() As Boolean, ByRef OutputName() As String, ByRef Comment() As String) As Long

## Parameters

Name

The name of an existing static nonlinear staged load case.

NumberStages

The number of stages defined for the specified load case.

Duration

This is an array that includes the duration in days for each stage.

Output

This is an array that includes True or False, indicating if analysis output is to be saved for each stage.

OutputName

This is an array that includes a user-specified output name for each stage.

Comment

This is an array that includes a comment for each stage. The comment may be a blank string.

## Remarks

This function initializes the stage definition data for the specified load case. All previous stage definition data for the case is cleared when this function is called.

The function returns zero if the data is successfully initialized; otherwise, it returns a nonzero value.

## VBA Example

Sub SetCaseStaticNonlinearStagedStageDefinitions\_1()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyDuration() As Long
      Dim MyOutput() As Boolean
      Dim MyOutputName() As String
      Dim MyComment() As String

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

   'add static nonlinear staged load case
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetCase("ACASE1")

   'initialize stage definitions
      ReDim MyDuration(1)
      ReDim MyOutput(1)
      ReDim MyOutputName(1)
      ReDim MyComment(1)
      MyDuration(0) = 0
      MyOutput(0) = False
      MyComment(0) = "Build structure"
      MyDuration(1) = 60
      MyOutput(1) = True
      MyOutputName(1) = "HBC2"
      MyComment(1) = "Wait"
      ret = SapModel.LoadCases.StaticNonlinearStaged.SetStageDefinitions\_1("ACASE1", 2, MyDuration, MyOutput, MyOutputName, MyComment)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

This function supersedes [GetStageDefinitions](GetStageDefinitions.htm).

This function is obsolete and has been replaced by [SetStageDefinitions\_2](../Definitions/Load_Case/Staged/SetStageDefinitions_2.htm) as of v19.0.0. This function is maintained for backward compatibility.

## See Also

[GetStageDefinitions\_1](GetStageDefinitions_1.htm)



## SetTee {Frame}

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetTee_{Frame}_old.htm`*

# SetTee (Note:  Newer function available)

## Syntax

SapObject.SapModel.PropFrame.SetTee

## VB6 Procedure

Function SetTee(ByVal Name As String, ByVal MatProp
As String, ByVal t3 As Double, ByVal t2 As Double, ByVal tf As Double,
ByVal tw As Double, Optional ByVal Color As Long = -1, Optional ByVal
Notes As String = "", Optional ByVal GUID As String = "")
As Long

## Parameters

Name

The name of an existing or new frame section property.
If this is an existing property, that property is modified; otherwise,
a new property is added.

MatProp

The name of the material property for the section.

t3

The section depth. [L]

t2

The flange width. [L]

tf

The flange thickness. [L]

tw

The web thickness. [L]

Color

The display color assigned to the section. If Color
is specified as -1, the program will automatically assign a color.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section. If this item is input as Default, the program assigns
a GUID to the section.

## Remarks

This function initializes a tee-type frame section property.
If this function is called for an existing frame section property, all
items for the section are reset to their default value.

The function returns zero if the section property is
successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetFramePropTee()
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
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetTee("TEE1",
"A992Fy50", 12, 10, 0.6, 0.3)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[GetTee](../Definitions/Properties/Frame/GetTee_{Frame}.htm)

[SetRebarBeam](../Definitions/Properties/Frame/SetRebarBeam.htm)

[GetRebarBeam](../Definitions/Properties/Frame/GetRebarBeam.htm)



## SetTube

*Source file: `SAP2000_API_Fuctions/Obsolete_Functions/SetTube.htm`*

# SetTube (Note: Newer function available)

## Syntax

SapObject.SapModel.PropFrame.SetTube

## VB6 Procedure

Function SetTube(ByVal Name As String, ByVal MatProp
As String, ByVal t3 As Double, ByVal t2 As Double, ByVal tf As Double,
ByVal tw As Double, Optional ByVal Color As Long = -1, Optional ByVal
Notes As String = "", Optional ByVal GUID As String = "")
As Long

## Parameters

Name

The name of an existing or new frame section property.
If this is an existing property, that property is modified; otherwise,
a new property is added.

MatProp

The name of the material property for the section.

t3

The section depth. [L]

t2

The section width. [L]

tf

The flange thickness. [L]

tw

The web thickness. [L]

Color

The display color assigned to the section. If Color
is specified as -1, the program will automatically assign a color.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned
to the section. If this item is input as Default, the program assigns
a GUID to the section.

## Remarks

This function initializes a tube-type frame section
property. If this function is called for an existing frame section property,
all items for the section are reset to their default value.

The function returns zero if the section property is
successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetFramePropTube()
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
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set new frame section property
      ret = SapModel.PropFrame.SetTube("TUBE1",
"A992Fy50", 8, 6, 0.5, 0.5)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

This function is obsolete and has been superseded by
[SetTube\_1](../Definitions/Properties/Frame/SetTube_1.htm)
as of version 24.2.

## See Also

[GetTube](GetTube_{Frame}.htm)

