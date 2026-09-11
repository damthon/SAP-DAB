# API Object Model Frame Object

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Object_Model/Frame_Object

---



## AddByCoord {Frame Objects}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/AddByCoord_{Frame_Objects}.htm`*

# AddByCoord

## Syntax

SapObject.SapModel.FrameObj.AddByCoord

## VB6 Procedure

Function AddByCoord(ByVal xi As Double, ByVal yi As Double, ByVal zi As Double, ByVal xj As Double, ByVal yj As Double, ByVal zj As Double, ByRef Name As String, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "", Optional ByVal CSys As String = "Global") As Long

## Parameters

xi, yi, zi

The coordinates of the I-End of the added frame object. The coordinates are in the coordinate system defined by the CSys item.

xj, yj, zj

The coordinates of the J-End of the added frame object. The coordinates are in the coordinate system defined by the CSys item.

Name

This is the name that the program ultimately assigns for the frame object. If no UserName is specified, the program assigns a default name to the frame object. If a UserName is specified and that name is not used for another frame, cable or tendon object, the UserName is assigned to the frame object, otherwise a default name is assigned to the frame object.

PropName

This is Default, None, or the name of a defined frame section property.

If it is Default, the program assigns a default section property to the frame object. If it is None, no section property is assigned to the frame object. If it is the name of a defined frame section property, that property is assigned to the frame object.

UserName

This is an optional user specified name for the frame object. If a UserName is specified and that name is already used for another frame object, the program ignores the UserName.

CSys

The name of the coordinate system in which the frame object end point coordinates are defined.

## Remarks

This function adds a new frame object whose end points are at the specified coordinates.

The function returns zero if the frame object is successfully added, otherwise it returns a nonzero value.

## VBA Example

Sub AddFrameObjByCoord()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add frame object by coordinates
      ret = SapModel.FrameObj.AddByCoord(-300, 0, 0, -100, 0, 124, Name)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByPoint](AddByPoint_{Frame_Objects}.htm)



## AddByPoint {Frame Objects}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/AddByPoint_{Frame_Objects}.htm`*

# AddByPoint

## Syntax

SapObject.SapModel.FrameObj.AddByPoint

## VB6 Procedure

Function AddByPoint(ByVal Point1 as String, ByVal Point2 as String, ByRef Name As String, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "") As Long

## Parameters

Point1

The name of a defined point object at the I-End of the added frame object.

Point2

The name of a defined point object at the J-End of the added frame object.

Name

This is the name that the program ultimately assigns for the frame object. If no UserName is specified, the program assigns a default name to the frame object. If a UserName is specified and that name is not used for another frame, cable or tendon object, the UserName is assigned to the frame object, otherwise a default name is assigned to the frame object.

PropName

This is Default, None, or the name of a defined frame section property.

If it is Default, the program assigns a default section property to the frame object. If it is None, no section property is assigned to the frame object. If it is the name of a defined frame section property, that property is assigned to the frame object.

UserName

This is an optional user specified name for the frame object. If a UserName is specified and that name is already used for another frame object, the program ignores the UserName.

## Remarks

This function adds a new frame object whose end points are specified by name.

The function returns zero if the frame object is successfully added, otherwise it returns a nonzero value.

## VBA Example

Sub AddFrameObjByPoint()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add frame object by points
      ret = SapModel.FrameObj.AddByPoint("1", "6", Name)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Frame_Objects}.htm)



## ChangeName {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/ChangeName_{Frame_Object}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.FrameObj.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a defined frame object.

NewName

The new name for the frame object.

## Remarks

The function returns zero if the new name is successfully applied, otherwise it returns a nonzero value.

## VBA Example

Sub ChangeFrameObjName()
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

   'change name
      ret = SapModel.FrameObj.ChangeName("1", "MyFrame")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## Count {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/Count_{Frame_Object}.htm`*

# Count

## Syntax

SapObject.SapModel.FrameObj.Count

## VB6 Procedure

Function Count(Optional ByVal MyType As String = "All") As Long

## Parameters

MyType

This is All, Straight, or Curved.

All returns a count of all frame objects in the model, including both straight and curved frame objects. Straight returns a count of all straight frame objects in the model. Curved returns a count of all curved frame objects in the model.

## Remarks

This function returns a count of the frame objects in the model. Depending on the value of the MyType item, the count may be of all frame objects in the model, just the straight frame objects in the model or just the curved frame objects in the model.

## VBA Example

Sub CountFrameObjects()
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

   'return number of frame objects
      Count = SapModel.FrameObj.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## DeleteFireproofing

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteFireproofing.htm`*

# DeleteFireproofing

## Syntax

SapObject.SapModel.FrameObj.DeleteFireproofing

## VB6 Procedure

Function DeleteFireproofing(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the fireproofing assignments are deleted for the frame object specified by the Name item.

If this item is Group, the fireproofing assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the fireproofing assignments are deleted for all selected frame objects, and the Name item is ignored.

## Remarks

This function deletes the fireproofing assignments for frame objects.

The function returns zero if the fireproofing assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFireproofing()
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

   'delete fireproofing
      ret = SapModel.FrameObj.DeleteFireproofing("3")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetFireproofing](../../Obsolete_Functions/GetFireproofing.htm)

[SetFireproofing](../../Obsolete_Functions/SetFireproofing.htm)



## DeleteLateralBracing

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLateralBracing.htm`*

# DeleteLateralBracing

## Syntax

SapObject.SapModel.FrameObj.DeleteLateralBracing

## VB6 Procedure

Function DeleteLateralBracing(ByVal Name As String, Optional ByVal MyType As Long = 3, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

MyType

This is 1, 2 or 3, indicating the bracing to be deleted.

1 = Delete point bracing

2 = Delete uniform bracing

3 = Delete both point and uniform bracing

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the lateral bracing assignments are deleted for the frame object specified by the Name item.

If this item is Group, the lateral bracing assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects then the lateral bracing assignments are deleted for all selected frame objects, and the Name item is ignored.

## Remarks

This function deletes the lateral bracing assignments for frame objects.

The function returns zero if the assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameLatealBracing()
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

   'assign frame lateral bracing
      ret = SapModel.FrameObj.SetLateralBracing("8", 1, 3, 0, 0)
      ret = SapModel.FrameObj.SetLateralBracing("8", 1, 3, 0.25, 0)
      ret = SapModel.FrameObj.SetLateralBracing("8", 1, 3, 1, 0)
      ret = SapModel.FrameObj.SetLateralBracing("8", 2, 1, 0.5, 1)

   'delete frame lateral bracing
      ret = SapModel.FrameObj.DeleteLateralBracing("8", 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetLateralBracing](SetLateralBracing.htm)

[GetLateralBracing](GetLateralBracing.htm)



## DeleteLoadDeformation {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLoadDeformation_{Frame_Object}.htm`*

# DeleteLoadDeformation

## Syntax

SapObject.SapModel.FrameObj.DeleteLoadDeformation

## VB6 Procedure

Function DeleteLoadDeformation(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the frame object specified by the Name item.

If this item is Group, the load assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected frame objects, and the Name item is ignored.

## Remarks

This function deletes the deformation load assignments to the specified frame objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameDeformationLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DOF() As Boolean
      Dim d() As double

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

   'assign frame deformation loads
      ReDim DOF(5)
      ReDim d(5)
      DOF(0) = True
      D(0) = 2
      ret = SapModel.FrameObj.SetLoadDeformation("ALL", "DEAD", DOF, d, Group)

   'delete frame deformation load
      ret = SapModel.FrameObj.DeleteLoadDeformation("3", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDeformation](GetLoadDeformation_{Frame_Object}.htm)

[SetLoadDeformation](SetLoadDeformation_{Frame_Object}.htm)



## DeleteLoadDistributedWithGUID {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLoadDistributedWithGUID_{Frame_Object}.htm`*

# DeleteLoadDistributedWithGUID

## Syntax

SapObject.SapModel.FrameObj.DeleteLoadDistributedWithGUID

## VB6 Procedure

Function DeleteLoadDistributedWithGUID(ByVal Name As String, ByVal GUID As String) As Long

## Parameters

Name

The name of an existing frame object.

GUID

The global unique ID of one of the distributed loads on that frame object.

## Remarks

This function deletes the distributed load assignment with the specified global unique ID for the frame objects for the specified frame object.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## Release Notes

Initial release in version 17.20.

## See Also

[GetLoadDistributedWithGUID](GetLoadDistributedWithGUID_{Frame_Object}.htm)

[SetLoadDistributedWithGUID](../../../SetLoadDistributed_{Frame_Object}.htm)



## DeleteLoadDistributed {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLoadDistributed_{Frame_Object}.htm`*

# DeleteLoadDistributed

## Syntax

SapObject.SapModel.FrameObj.DeleteLoadDistributed

## VB6 Procedure

Function DeleteLoadDistributed(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the frame object specified by the Name item.

If this item is Group, the load assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected frame objects, and the Name item is ignored.

## Remarks

This function deletes the distributed load assignments to the specified frame objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameDistributedLoad()
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

   'assign frame distributed loads
      ret = SapModel.FrameObj.SetLoadDistributed("14", "DEAD", 1, 10, 0, 1, 0.08, 0.08)
      ret = SapModel.FrameObj.SetLoadDistributed("15", "DEAD", 1, 10, 0, 1, 0.08, 0.08)

   'delete frame distributed load
      ret = SapModel.FrameObj.DeleteLoadDistributed("14", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDistributed](GetLoadDistributed_{Frame_Object}.htm)

[SetLoadDistributed](SetLoadDistributed_{Frame_Object}.htm)



## DeleteLoadGravity {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLoadGravity_{Frame_Object}.htm`*

# DeleteLoadGravity

## Syntax

SapObject.SapModel.FrameObj.DeleteLoadGravity

## VB6 Procedure

Function DeleteLoadGravity(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object,the load assignments are deleted for the frame object specified by the Name item.

If this item is Group, the load assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected frame objects, and the Name item is ignored.

## Remarks

This function deletes the gravity load assignments to the specified frame objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameGravityLoad()
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

   'assign frame gravity loads
      ret = SapModel.FrameObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'delete frame gravity load
      ret = SapModel.FrameObj.DeleteLoadGravity("3", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Frame_Object}.htm)

[SetLoadGravity](SetLoadGravity_{Frame_Object}.htm)



## DeleteLoadPoint

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLoadPoint.htm`*

# DeleteLoadPoint

## Syntax

SapObject.SapModel.FrameObj.DeleteLoadPoint

## VB6 Procedure

Function DeleteLoadPoint(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the frame object specified by the Name item.

If this item is Group, the load assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected frame objects, and the Name item is ignored.

## Remarks

This function deletes the point load assignments to the specified frame objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFramePointLoad()
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

   'assign frame point loads
      ret = SapModel.FrameObj.SetLoadPoint("14", "DEAD", 1, 10, .5, 20)
      ret = SapModel.FrameObj.SetLoadPoint("15", "DEAD", 1, 10, .5, 20)

   'delete frame point load
      ret = SapModel.FrameObj.DeleteLoadPoint("14", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadPoint](GetLoadPoint_{Frame_Object}.htm)

[SetLoadPoint](SetLoadPoint.htm)



## DeleteLoadPointWithGUID {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLoadPointWithGUID_{Frame_Object}.htm`*

# DeleteLoadPointWithGUID {Frame Object}

## Syntax

SapObject.SapModel.FrameObj.DeleteLoadPointWithGUID

## VB6 Procedure

Function DeleteLoadPointWithGUID(ByVal Name As String, ByVal GUID As String) As Long

## Parameters

Name

The name of an existing frame object.

GUID

The global unique ID for one of the point loads on that frame object.

## Remarks

This function deletes the point load assignment with the specified global unique ID for the specified frame object.

The function returns zero if the load assignment is successfully deleted, otherwise it returns a nonzero value.

## Release Notes

Initial release in version 17.2.0.

## See Also

[GetLoadPointWithGUID](../../../GetLoadPointWithGUID_{Frame_Object}.htm)

[SetLoadPointWithGUID](SetLoadPointWithGUID_{Frame_Object}.htm)



## DeleteLoadStrain {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLoadStrain_{Frame_Object}.htm`*

# DeleteLoadStrain

## Syntax

SapObject.SapModel.FrameObj.DeleteLoadStrain

## VB6 Procedure

Function DeleteLoadStrain(ByVal Name As String, ByVal LoadPat As String, ByVal DOF As Long, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

DOF

This is 1, 2, 3, 4, 5 or 6, indicating the degree of freedom to which the strain load is applied.

1 = Strain11

2 = Strain12

3 = Strain13

4 = Curvature1

5 = Curvature2

6 = Curvature3

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the frame object specified by the Name item.

If this item is Group, the load assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected frame objects, and the Name item is ignored.

## Remarks

This function deletes the strain load assignments to the specified frame objects, for the specified load pattern, for the specified degree of freedom.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameStrainLoad()
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

   'assign frame strain load
      ret = SapModel.FrameObj.SetLoadStrain("1", "DEAD", 1, 0.001)
      ret = SapModel.FrameObj.SetLoadStrain("2", "DEAD", 1, 0.001)

   'delete frame strain load
      ret = SapModel.FrameObj.DeleteLoadStrain("1", "DEAD", 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadStrain](GetLoadStrain_{Frame_Object}.htm)

[SetLoadStrain](SetLoadStrain_{Frame_Object}.htm)



## DeleteLoadTargetForce {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLoadTargetForce_{Frame_Object}.htm`*

# DeleteLoadTargetForce

## Syntax

SapObject.SapModel.FrameObj.DeleteLoadTargetForce

## VB6 Procedure

Function DeleteLoadTargetForce(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the frame object specified by the Name item.

If this item is Group, the load assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected frame objects, and the Name item is ignored.

## Remarks

This function deletes the target force assignments to the specified frame objects for the specified load pattern.

The function returns zero if the target force assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameTargetForce()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DOF() As Boolean
      Dim f() As double
      Dim RD() As double

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

   'assign frame target force
      ReDim DOF(5)
      ReDim f(5)
      ReDim RD(5)
      DOF(0) = True
      f(0) = 50
      RD(0) = 0.5
      ret = SapModel.FrameObj.SetLoadTargetForce("1", "DEAD", DOF, f, RD)
      ret = SapModel.FrameObj.SetLoadTargetForce("2", "DEAD", DOF, f, RD)

   'delete frame target force
      ret = SapModel.FrameObj.DeleteLoadTargetForce("1", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTargetForce](GetLoadTargetForce_{Frame_Object}.htm)

[SetLoadTargetForce](SetLoadTargetForce_{Frame_Object}.htm)



## DeleteLoadTemperature {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLoadTemperature_{Frame_Object}.htm`*

# DeleteLoadTemperature

## Syntax

SapObject.SapModel.FrameObj.DeleteLoadTemperature

## VB6 Procedure

Function DeleteLoadTemperature(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the frame object specified by the Name item.

If this item is Group, the load assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected frame objects, and the Name item is ignored.

## Remarks

This function deletes the temperature load assignments to the specified frame objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameTemperatureLoad()
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

   'assign frame temperature load
      ret = SapModel.FrameObj.SetLoadTemperature("All", "DEAD", 1, 50, , , Group)

   'delete frame temperature load
      ret = SapModel.FrameObj.DeleteLoadTemperature("3", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTemperature](GetLoadTemperature_{Frame_Object}.htm)

[SetLoadTemperature](SetLoadTemperature_{Frame_Object}.htm)



## DeleteMass {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteMass_{Frame_Object}.htm`*

# DeleteMass

## Syntax

SapObject.SapModel.FrameObj.DeleteMass

## VB6 Procedure

Function DeleteMass(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the frame mass assignments are deleted for the frame object specified by the Name item.

If this item is Group, the frame mass assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the frame mass assignments are deleted for all selected frame objects and the Name item is ignored.

## Remarks

This function deletes the frame mass assignments for frame objects.

The function returns zero if the mass assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameMass()
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

   'assign frame mass
      ret = SapModel.FrameObj.SetMass("ALL", .0001, False, Group)

   'delete frame mass
      ret = SapModel.FrameObj.DeleteMass("15")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMass](GetMass_{Frame_Object}.htm)

[SetMass](SetMass_{Frame_Object}.htm)



## DeleteModifiers {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteModifiers_{Frame_Object}.htm`*

# DeleteModifiers

## Syntax

SapObject.SapModel.FrameObj.DeleteModifiers

## VB6 Procedure

Function DeleteModifiers(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the frame modifier assignments are deleted for the frame object specified by the Name item.

If this item is Group, the frame modifier assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the frame modifier assignments are deleted for all selected frame objects, and the Name item is ignored.

## Remarks

This function deletes the frame modifier assignments for frame objects.

The function returns zero if the modifier assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameModifiers()
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

   'assign modifiers
      ReDim Value(7)
      For i = 0 To 7
         Value(i) = 1
      Next i
      Value(5) = 100
      ret = SapModel.FrameObj.SetModifiers("ALL", Value, Group)

   'delete modifiers
      ret = SapModel.FrameObj.DeleteModifiers("3")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetModifiers](GetModifiers_{Frame_Object}.htm)

[SetModifiers](SetModifiers_{Frame_Object}.htm)



## DeletePDeltaForce

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeletePDeltaForce.htm`*

# DeletePDeltaForce

## Syntax

SapObject.SapModel.FrameObj.DeletePDeltaForce

## VB6 Procedure

Function DeletePDeltaForce(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the frame modifier assignments are deleted for the frame object specified by the Name item.

If this item is Group, the frame modifier assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the frame modifier assignments are deleted for all selected frame objects, and the Name item is ignored.

## Remarks

This function deletes the P-Delta force assignments for frame objects.

The function returns zero if the assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeletePDeltaForces()
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

   'assign P-Delta force
      ret = SapModel.FrameObj.SetPDeltaForce("ALL", 100, 0, True, , Group)

   'delete P-Delta force
      ret = SapModel.FrameObj.DeletePDeltaForce("3")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetPDeltaForce](GetPDeltaForce_{Frame_Object}.htm)

[SetPDeltaForce](SetPDeltaForce.htm)



## DeleteSpring {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteSpring_{Frame_Object}.htm`*

# DeleteSpring

## Syntax

SapObject.SapModel.FrameObj.DeleteSpring

## VB6 Procedure

Function DeleteSpring(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the frame spring assignments are deleted for the frame object specified by the Name item.

If this item is Group, the frame spring assignments are deleted for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the frame spring assignments are deleted for all selected frame objects and the Name item is ignored.

## Remarks

This function deletes all spring assignments for the specified frame objects.

The function returns zero if the assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameSprings()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Vec() As Double

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

   'assign springs to frame
      ReDim Vec(2)
      ret = SapModel.FrameObj.SetSpring("ALL", 1, 1, 1, "", 1, 2, 0, Vec, 0, False, "Local", Group)

   'delete springs
      ret = SapModel.FrameObj.DeleteSpring("15")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Frame_Object}.htm)

[SetSpring](SetSpring__{Frame_Object}.htm)



## Delete {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/Delete_{Frame_Object}.htm`*

# Delete

## Syntax

SapObject.SapModel.FrameObj.Delete

## VB6 Procedure

Function Delete(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the frame object specified by the Name item is deleted.

If this item is Group, all of the frame objects in the group specified by the Name item are deleted.

If this item is SelectedObjects, all selected frame objects are deleted, and the Name item is ignored.

## Remarks

The function deletes frame objects.

The function returns zero if the frame object is successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteFrameObj()
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

   'delete frame object
      ret = SapModel.FrameObj.Delete("1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Frame_Objects}.htm)

[AddByPoint](AddByPoint_{Frame_Objects}.htm)



## GetAutoMesh {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetAutoMesh_{Frame_Object}.htm`*

# GetAutoMesh

## Syntax

SapObject.SapModel.FrameObj.GetAutoMesh

## VB6 Procedure

Function GetAutoMesh(ByVal Name As String, ByRef AutoMesh As Boolean, ByRef AutoMeshAtPoints As Boolean, ByRef AutoMeshAtLines As Boolean, ByRef NumSegs As Long, ByRef AutoMeshMaxLength As Double) As Long

## Parameters

Name

The name of an existing frame object.

AutoMesh

This item is True if the frame object is to be automatically meshed by the program when the analysis model is created.

AutoMeshAtPoints

This item is applicable only when the AutoMesh item is True. If this item is True, the frame object is automatically meshed at intermediate joints along its length.

AutoMeshAtLines

This item is applicable only when the AutoMesh item is True. If this item is True, the frame object is automatically meshed at intersections with other frames, area object edges and solid object edges.

NumSegs

This item is applicable only when the AutoMesh item is True. It is the minimum number of elements into which the frame object is automatically meshed. If this item is zero, the number of elements is not checked when the automatic meshing is done.

AutoMeshMaxLength

This item is applicable only when the AutoMesh item is True. It is the maximum length of auto meshed frame elements. If this item is zero, the element length is not checked when the automatic meshing is done. [L]

## Remarks

This function retrieves the automatic meshing assignments to frame objects.

The function returns zero if the meshing assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameAutoMesh()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim AutoMesh As Boolean
      Dim AutoMeshAtPoints As Boolean
      Dim AutoMeshAtLines As Boolean
      Dim NumSegs As Long
      Dim AutoMeshMaxLength As Double

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

   'assign automesh options
      ret = SapModel.FrameObj.SetAutoMesh("ALL", True, True, True, 0, 0, Group)

   'get automesh assignment
      ret = SapModel.FrameObj.GetAutoMesh("3", AutoMesh, AutoMeshAtPoints, AutoMeshAtLines,NumSegs, AutoMeshMaxLength)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetAutoMesh](SetAutoMesh_{Frame_Object}.htm)



## GetCurved_1

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetCurved_1.htm`*

# GetCurved\_1

## Syntax

SapObject.SapModel.FrameObj.GetCurved\_1

## VB6 Procedure

Function GetCurved\_1(ByRef NumberItems As Integer, ByRef MyName As String(), ByRef MyType() As Integer, ByRef gx() As Double, ByRef gy() As Double, ByRef gz() As Double, ByRef PointName() As String, ByRef Radius() As Double, ByRef NumSegs() As Integer) As Long

## Parameters

NumberItems

The number of curved frame objects returned.

MyName

This is a one-dimensional array of frame object names. The MyName array is created as a dynamic, zero-based, array by the APIuser:

Dim MyName() as String

The array is dimensioned to (NumberNames – 1) inside the Sap2000 program, filled with the names, and returned to the APIuser

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
      Dim MyName() As String

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
      ret = SapModel.FrameObj.GetCurved\_1(NumberItems, MyName, MyType, gx, gy, gz, PointName, Radius, NumSegs)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 17.2.0.

This function supersedes [GetCurved](../../Obsolete_Functions/GetCurved.htm).

## See Also

[SetStraight](SetStraight.htm)

[SetCurved](SetCurved.htm)

[GetType](GetType_{Frame_Object}.htm)



## GetDAMModifiers

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetDAMModifiers.htm`*

# GetDAMModifiers

## Syntax

SapObject.SapModel.FrameObj.GetDAMModifiers

## VB6 Procedure

Function GetDAMModifiers(ByVal Name As String, ByRef EAModifier As Double, ByRef EIModifier As Double) As Long

## Parameters

Name

The name of an existing frame section whose design type is Steel Frame design.

EAModifier

The modification factor for axial stiffness if the Direct Analysis method is used.

EIModifier

The modification factor for flexural stiffness if the Direct Analysis method is used.

## **Remarks**

This function gets the modification factors for axial and flexural stiffness for a frame object if the Direct Analysis method is used.

The function returns zero if the factors are successfully retrieved, otherwise it returns a nonzero value. The function will return nonzero the modification factors are not available for the frame object.

## VBA Example

Sub GetDAMModifiers()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim EAModifier As Double

Dim EIModifier As Double

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

'set the steel frame design code

ret =SapModel.DesignSteel.SetCode("AISC360-05/IBC2006")

'save model

ret = SapModel.File.Save("C:\SapAPI\x.sdb")

'run analysis

ret =SapModel.Analyze.RunAnalysis

'run design

ret =SapModel.DesignSteel.StartDesign

'get direct analysis method modification factors

ret = SapModel.FrameObj.GetDAMModifiers("1", EAModifier, EIModifier)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also



## GetDesignProcedure

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetDesignProcedure.htm`*

# GetDesignProcedure

## Syntax

SapObject.SapModel.FrameObj.GetDesignProcedure

## VB6 Procedure

Function GetDesignProcedure(ByVal Name As String, ByRef MyType As Long) As Long

## Parameters

Name

The name of an existing frame object.

MyType

This is 1, 2, 7, 8 or 9, indicating the design procedure for the specified frame object.

1 = Steel

2 = Concrete

7 = Aluminum

8 = Cold Formed

9 = No Design

## Remarks

This function retrieves the design procedure for a frame object.

The function returns zero if the design procedure is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameObjDesignProcedure()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'get design procedure
      ret = SapModel.FrameObj.GetDesignProcedure("8", MyType)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[SetDesignProcedure](SetDesignProcedure.htm)



## GetElm {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetElm_{Frame_Object}.htm`*

# GetElm

## Syntax

SapObject.SapModel.FrameObj.GetElm

## VB6 Procedure

Function GetElm(ByVal Name As String, ByRef nelm As Long, ByRef Elm() as String, ByRef RDI() As Double, ByRef RDJ() As Double) As Long

## Parameters

Name

The name of an existing frame object.

nelm

The number of line elements created from the specified frame object.

Elm

An array that includes the name of a frame element created from the specified frame object.

RDI

An array that includes the relative distance along the frame object to the I-End of the frame element.

RDJ

An array that includes the relative distance along the line object to the J-End of the frame element.

## Remarks

This function retrieves the names of the frame elements (analysis model lines) associated with a specified frame object in the object-based model. It also retrieves information about the location of the frame elements along the frame object.

This function returns zero if the frame element information is successfully returned; otherwise it returns nonzero. An error occurs if the analysis model does not exist.

## VBA Example

Sub GetLineElementInfo()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim nelm As Long
      Dim Elm() As String
      Dim RDI() As Double
      Dim RDJ() As Double

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

   'create the analysis model
      ret = SapModel.Analyze.CreateAnalysisModel

   'get line element information
      ret = SapModel.FrameObj.GetElm("5", nelm, Elm, RDI, RDJ)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetEndLengthOffset {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetEndLengthOffset_{Frame_Object}.htm`*

# GetEndLengthOffset

## Syntax

SapObject.SapModel.FrameObj.GetEndLengthOffset

## VB6 Procedure

Function GetEndLengthOffset(ByVal Name As String, ByRef AutoOffset As Boolean, ByRef Length1 As Double, ByRef Length2 As Double, ByRef rz As Double) As Long

## Parameters

Name

The name of an existing frame object.

AutoOffset

If this item is True, the end length offsets are automatically determined by the program from object connectivity.

Length1

The offset length along the 1-axis of the frame object at the I-End of the frame object. [L]

Length2

The offset along the 1-axis of the frame object at the J-End of the frame object. [L]

rz

The rigid zone factor.  This is the fraction of the end offset length assumed to be rigid for bending and shear deformations.

## Remarks

This function retrieves the frame object end offsets along the 1-axis of the object.

The function returns zero if the offsets are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameEndOffsets()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim AutoOffset As Boolean
      Dim Length1 As Double
      Dim Length2 As Double
      Dim rz As Double

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

   'get offsets
      ret = SapModel.FrameObj.GetEndLengthOffset("15", AutoOffset, Length1, Length2, rz)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetEndLengthOffset](SetEndLengthOffset.htm)



## GetEndSkew

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetEndSkew.htm`*

# GetEndSkew

## Syntax

SapObject.SapModel.FrameObj.GetEndSkew

## VB6 Procedure

Function GetEndSkew(ByVal Name As String, ByRef SkewI As Double, ByRef SkewJ As Double) As Long

## Parameters

Name

The name of an existing frame object.

SkewI

The angle in degrees measured counter clockwise from the positive local 3-axis to a line parallel to the I-End of the frame object (-90 < SkewI < 90). [deg]

SkewJ

The angle in degrees measured counter clockwise from the positive local 3-axis to a line parallel to the J-End of the frame object (-90 < SkewJ < 90). [deg]

## Remarks

This function retrieves frame object end skew assignments.

The function returns zero if the end skew data is successfully retrieved, otherwise it returns a nonzero value.

End skew assignments are only applicable to straight frame objects. An error is returned if skew data is requested for a curved frame object.

End skew data is only used in the program to plot the extruded view of bridge objects that have been updated as spine models.

## VBA Example

Sub GetFrameEndSkewData()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim SkewI As Double
      Dim SkewJ As Double

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

   'get end skew data
      ret = SapModel.FrameObj.GetEndSkew("15", SkewI, SkewJ)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetEndSkew](SetEndSkew.htm)



## GetFireproofing_1

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetFireproofing_1.htm`*

# GetFireproofing\_1

## Syntax

SapObject.SapModel.FrameObj.GetFireProofing\_1

## VB6 Procedure

Function GetFireProofing\_1(ByVal Name As String, ByRef MyType As Long, ByRef Thickness As Double, ByRef Perimeter As Double, ByRef Density As Double, ByRef tf As Boolean, ByRef IncludeInSelfWeight As Boolean, ByRef IncludeInGravityLoads As Boolean, ByRef IncludeInThisLoadPattern As String) As Long

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

IncludeInSelfWeight

If this item is True the fireproofing is included in the structure self weight.

IncludeInGravityLoads

If this item is True the fireproofing is included gravity loads applied in the X, Y and Z directions.

IncludeInThisLoadPattern

This item is either None or the name of an existing load pattern. If it is the name of a load pattern then the weight of the fireproofing is applied as a distributed load in the global Z direction in the load pattern.

## **Remarks**

This function gets the fireproofing assignment to an existing frame object.

The function returns zero if the fireproofing assignment is successfully retrieved, otherwise it returns a nonzero value.

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

Dim IncludeInSelfWeight As Boolean

Dim IncludeInGravityLoads As Boolean

Dim IncludeInThisLoadPattern As String

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

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fireproofing", LTYPE\_SUPERDEAD)

'assign fireproofing, use in self weight and in load pattern

ret = SapModel.FrameObj.SetFireproofing\_1("ALL", 1, 2, 0, 8.68E-06, False, True, False, "Fireproofing", Group)

'get fireproofing data for frame object 3

ret = SapModel. FrameObj.GetFireproofing\_1("3", MyType, Thickness, Perimeter, Density, tf, IncludeInSelfWeight, IncludeInGravityLoads, IncludeInThisLoadPattern)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.  This function supersedes obsolete function GetFireProofing

## See Also

[SetFireProofing\_1](SetFireproofing_1.htm)

[DeleteFireProofing](DeleteFireproofing.htm)



## GetGUID {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetGUID_{Frame_Object}.htm`*

# GetGUID

## Syntax

SapObject.SapModel.FrameObj.GetGUID

## VB6 Procedure

Function GetGUID(ByVal name As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing frame object.

GUID

The GUID (Global Unique ID) for the specified frame object.

## Remarks

This function retrieves the GUID for the specified frame object.

This function returns zero if the frame object GUID is successfully retrieved; otherwise it returns nonzero.

## VBA Example

Sub GetFrameObjGUID()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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

   'set program created GUID
      ret = SapObject.SapModel.FrameObj.SetGUID("1")

   'get GUID
      ret = SapObject.SapModel.FrameObj.GetGUID("1", GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetGUID](SetGUID_{Frame_Object}.htm)



## GetGroupAssign {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetGroupAssign_{Frame_Object}.htm`*

# GetGroupAssign

## Syntax

SapObject.SapModel.FrameObj.GetGroupAssign

## VB6 Procedure

Function GetGroupAssign(ByVal Name As String, ByRef NumberGroups As Long, ByRef Groups() As String)  As Long

## Parameters

Name

The name of an existing frame object.

NumberGroups

The number of group names retrieved.

Groups

The names of the groups to which the frame object is assigned.

## Remarks

This function retrieves the names of the groups to which a specified frame object is assigned.

The function returns zero if the group assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameObjectGroups()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim NumberGroups As Long
      Dim Groups() As String

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

   'define new groups
      ret = SapModel.GroupDef.SetGroup("Group1")
      ret = SapModel.GroupDef.SetGroup("Group2")

   'add frame object to groups
      ret = SapModel.FrameObj.SetGroupAssign("2", "Group1")
      ret = SapModel.FrameObj.SetGroupAssign("2", "Group2")

   'get frame object groups
      ret = SapModel.FrameObj.GetGroupAssign("2", NumberGroups, Groups)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.0.0.

## See Also

[SetGroupAssign](SetGroupAssign_{Frame_Object}.htm)



## GetHingeAssigns

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetHingeAssigns.htm`*

# GetHingeAssigns (Note:  Newer function available)

## Syntax

SapObject.SapModel.FrameObj.GetHingeAssigns

## VB6 Procedure

Function GetHingeAssigns(ByVal Name As String, ByRef
NumberHinges As Long, ByRef HingeNum() As Long, ByRef Prop() As String,
ByRef MyType() As Long, ByRef Behavior() As Long, ByRef Source() As String,
ByRef RD() As Double) As Long

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

RD

An array that indicates the relative distance of each
hinge along the frame object.

## Remarks

This function reports the hinge assignments for a specified
frame object.

The function returns zero if the assignment data is
successfully obtained; otherwise it returns a nonzero value.

## VBA Example

This example assumes that a file MyHinge.sdb exists.

Sub GetFrameHingeAssigns()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberHinges As Long
      Dim HingeNum() As Long
      Dim Prop() As String
      Dim MyType() As Long
      Dim Behavior() As Long
      Dim Source() As String
      Dim RD() As Double

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
      ret = SapModel.FrameObj.GetHingeAssigns("1",
NumberHinges, HingeNum, Prop, MyType, Behavior, Source, RD)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.20.

## See Also

[GetHingeAssigns\_2](GetHingeAssigns_2.htm)



## GetHingeAssigns_2

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetHingeAssigns_2.htm`*

# GetHingeAssigns\_2

## Syntax

SapObject.SapModel.FrameObj.GetHingeAssigns\_2

## VB6 Procedure

Function GetHingeAssigns\_2(ByVal
Name As String, ByRef HingeDistrType As eHingeDistributionType, ByRef
NumberHinges As Long, ByRef HingeNum() As Long, ByRef Prop() As String,
ByRef MyType() As Long, ByRef Behavior() As Long, ByRef Source() As String,
ByRef LocType() As eHingeLocationType, ByRef RD() As Double, ByRef AD()
As Double, ByRef LengthOWType() as eHingeLengthOverwriteType, ByRef LengthOWRel()
As Double, ByRef LengthOWAbs() As Double) As Long

## Parameters

Name

The name of an existing frame object.

HingeDistrType

This is a value from the eHingeDistributionType enumeration,
specifying the type of hinge distribution used for the frame hinge assignment:

1= NonlinearBeamColumn

2= DistributedPlasticity

3 = EqualSpacing

4 = ContinuousSupport

5 = UserDefined

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

LengthOWType

This is a value from the eHingeLengthOverwriteType enumeration,
specifying the hinge length overwrite assigned to the hinge:

None = 1

Absolute = 2

Relative = 3

LengthOWRel

If LengthOWType = eHingeLocationType.Relative, this
is the length of the hinge length overwrite, as a ratio to the clear length
of the frame object.

LengthOWAbs

If LengthOWType = eHingeLocationType.Absolute, this
is the absolute length of the hinge length overwrite.

## Remarks

This function reports the hinge assignments for a specified
frame object.

The function returns zero if the assignment data is
successfully obtained; otherwise it returns a nonzero value.

## VBA Example

This example assumes that a file MyHinge.sdb exists.

Sub GetFrameHingeAssigns\_2()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberHinges As Long

 Dim HingeDistrType As
eHingeDistributionType

      Dim HingeNum() As
Long
      Dim Prop() As String
      Dim MyType() As Long
      Dim Behavior() As Long
      Dim Source() As String

 Dim LocType() As eHingeLocationType

      Dim RD() As Double

      Dim AD() As Double

      Dim
LenOWType() As eHingeLengthOverwriteType

      Dim
LenOWRel() As Double

      Dim
LenOWAbs() As Double

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
     ret = SapModel.FrameObj.GetHingeAssigns\_2("1",
NumberHinges, HingeNum, Prop, MyType, Behavior, Source, LocType, RD, AD,
LengthOWType, LengthOWRel, LenthOWAbs)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.0.0

This function supersedes [GetHingeAssigns\_1](../../Obsolete_Functions/GetHingeAssigns_1.htm).

## See Also



## GetInsertionPoint_1{Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetInsertionPoint_1{Frame_Object}.htm`*

# GetInsertionPoint\_1

## Syntax

SapObject.SapModel.FrameObj.GetInsertionPoint\_1

## VB6 Procedure

Function GetInsertionPoint\_1(ByVal Name As String, ByRef
CardinalPoint As Long, ByRef Mirror2, ByRef Mirror3, As Boolean, ByRef
StiffTransform As Boolean, ByRef Offset1() As Double, ByRef Offset2()
As Double, ByRef CSys As String) As Long

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

Mirror3

If this item is True, the frame object section is assumed
to be mirrored (flipped) about its local 3-axis.

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
      Dim Mirror3 As Boolean

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
      ret = SapModel.FrameObj.SetInsertionPoint\_1("15",
7, False, False, True, Offset1, Offset2)

   'get frame insertion point
      ReDim Offset1(2)
      ReDim Offset2(2)
      ret = SapModel.FrameObj.GetInsertionPoint\_1("15",
CardinalPoint, Mirror2, Mirror3, StiffTransform, Offset1, Offset2, CSys)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.1.

This function supersedes [GetInsertionPoint](../../Obsolete_Functions/GetInsertionPoint_{Frame_Object}.htm),
adding the Mirror3 parameter.

## See Also

[SetInsertionPoint\_1](SetInsertionPoint_1{Frame_Object}.htm)



## GetLateralBracing

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLateralBracing.htm`*

# GetLateralBracing

## Syntax

SapObject.SapModel.FrameObj.GetLateralBracing

## VB6 Procedure

Function GetLateralBracing(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef MyType() As Long, ByRef Loc() As Long, ByRef RD1() As Double, ByRef RD2() As Double, ByRef Dist1() As Double, ByRef Dist2() As Double) As Long

## Parameters

Name

The name of an existing frame object.

NumberItems

The total number of bracing assignments retrieved for the specified frame objects.

FrameName

This is an array that includes the name of the frame object associated with each bracing assignment.

MyType

This is an array that includes 1 or 2, indicating the bracing type assigned.

1 = Point bracing

2 = Uniform bracing

Loc

This is an array that includes 1, 2 or 3; indicating the bracing location.

1 = Top

2 = Bottom

3 = All (top and bottom)

RD1

This is an array that includes the relative location of the point bracing (when MyType = 1) or the relative location of the start of the uniform bracing (when MyType = 2).

RD2

This is an array that includes the relative location of the start of the uniform bracing (when MyType = 2).

This item does not apply for point bracing (when MyType = 1).

Dist1

This is an array that includes the actual location of the point bracing (when MyType = 1) or the actual location of the start of the uniform bracing (when MyType = 2). [L]

Dist2

This is an array that includes the actual location of the start of the uniform bracing (when MyType = 2). [L]

This item does not apply for point bracing (when MyType = 1).

## Remarks

This function retrieves the lateral bracing location assignments for frame objects.

The function returns zero if the assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameLateralBracing()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim MyType() As Long
      Dim Loc() As Long
      Dim RD1() As Double
      Dim RD2() As Double
      Dim Dist1() As Double
      Dim Dist2() As Double

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

   'assign frame lateral bracing
      ret = SapModel.FrameObj.SetLateralBracing("8", 1, 3, 0, 0)
      ret = SapModel.FrameObj.SetLateralBracing("8", 1, 3, 0.25, 0)
      ret = SapModel.FrameObj.SetLateralBracing("8", 1, 3, 1, 0)
      ret = SapModel.FrameObj.SetLateralBracing("8", 2, 1, 0.5, 1)

   'get frame lateral bracing
      ret = SapModel.FrameObj.GetLateralBracing("8", NumberItems, FrameName, MyType, Loc, RD1, RD2, Dist1, Dist2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetLateralBracing](SetLateralBracing.htm)

[DeleteLateralBracing](DeleteLateralBracing.htm)



## GetLoadDeformation {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLoadDeformation_{Frame_Object}.htm`*

# GetLoadDeformation

## Syntax

SapObject.SapModel.FrameObj.GetLoadDeformation

## VB6 Procedure

Function GetLoadDeformation(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef LoadPat() As String, ByRef dof1() As Boolean, ByRef dof2() As Boolean, ByRef dof3() As Boolean, ByRef dof4() As Boolean, ByRef dof5() As Boolean, ByRef dof6() As Boolean, ByRef U1() As Double, ByRef U2() As Double, ByRef U3() As Double, ByRef R1() As Double, ByRef R2() As Double, ByRef R3() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

NumberItems

The total number of deformation loads retrieved for the specified frame objects.

FrameName

This is an array that includes the name of the frame object associated with each deformation load.

LoadPat

This is an array that includes the name of the load pattern associated with each deformation load.

dof1, dof2, dof3, dof4, dof5, dof6

These are arrays of boolean values indicating if the considered degree of freedom has a deformation load.

dof1 = U1

dof2 = U2

dof3 = U3

dof4 = R1

dof5 = R2

dof6 = R3

U1, U2, U3, R1, R2, R3

These are arrays of deformation load values. The deformations specified for a given degree of freedom are applicable only if the corresponding DOF item for that degree of freedom is True.

U1 = U1 deformation [L]

U2 = U2 deformation [L]

U3 = U3 deformation [L]

R1 = R1 deformation [rad]

R2 = R2 deformation [rad]

R3 = R3 deformation [rad]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the frame object specified by the Name item.

If this item is Group, the assignments are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves the deformation load assignments to frame objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameDeformationLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DOF() As Boolean
      Dim d() As double
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim LoadPat() As String
      Dim dof1() As Boolean
      Dim dof2() As Boolean
      Dim dof3() As Boolean
      Dim dof4() As Boolean
      Dim dof5() As Boolean
      Dim dof6() As Boolean
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

   'assign frame deformation loads
      ReDim DOF(5)
      ReDim d(5)
      DOF(0) = True
      D(0) = 2
      ret = SapModel.FrameObj.SetLoadDeformation("ALL", "DEAD", DOF, d, Group)

   'get frame deformation loads
      ret = SapModel.FrameObj.GetLoadDeformation("3", NumberItems, FrameName, LoadPat, dof1, dof2, dof3, dof4, dof5, dof6, U1, U2, U3, R1, R2, R3)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadDeformation](SetLoadDeformation_{Frame_Object}.htm)

[DeleteLoadDeformation](DeleteLoadDeformation_{Frame_Object}.htm)



## GetLoadDistributedWithGUID {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLoadDistributedWithGUID_{Frame_Object}.htm`*

# GetLoadDistributedWithGUID {Frame Object}

## Syntax

SapObject.SapModel.FrameObj.GetLoadDistributedWthGUID

## VB6 Procedure

Function GetLoadDistributed(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef LoadPat() As String, ByRef MyType() As Long, ByRef CSys() As String, ByRef Dir() As Long, ByRef RD1() As Double, ByRef RD2() As Double, ByRef Dist1() As Double, ByRef Dist2() As Double, ByRef Val1() As Double, ByRef Val2() As Double, ByRef GUID() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

NumberItems

The total number of distributed loads retrieved for the specified frame objects.

FrameName

This is an array that includes the name of the frame object associated with each distributed load.

LoadPat

This is an array that includes the name of the coordinate system in which the distributed loads are specified.

MyType

This is an array that includes 1 or 2, indicating the type of distributed load.

1 = Force

2 = Moment

CSys

This is an array that includes the name of the coordinate system in which each distributed load is defined. It may be Local or the name of a defined coordinate system.

Dir

This is an array that includes an integer between 1 and 11, indicating the direction of the load.

1 = Local 1 axis (only applies when CSys is Local)

2 = Local 2 axis (only applies when CSys is Local)

3 = Local 3 axis (only applies when CSys is Local)

4 = X direction (does not apply when CSys is Local)

5 = Y direction (does not apply when CSys is Local)

6 = Z direction (does not apply when CSys is Local)

7 = Projected X direction (does not apply when CSys is Local)

8 = Projected Y direction (does not apply when CSys is Local)

9 = Projected Z direction (does not apply when CSys is Local)

10 = Gravity direction (only applies when CSys is Global)

11 = Projected Gravity direction (only applies when CSys is Global)

The positive gravity direction (see Dir = 10 and 11) is in the negative Global Z direction.

RD1

This is an array that includes the relative distance from the I-End of the frame object to the start of the distributed load.

RD2

This is an array that includes the relative distance from the I-End of the frame object to the end of the distributed load.

Dist1

This is an array that includes the actual distance from the I-End of the frame object to the start of the distributed load. [L]

Dist2

This is an array that includes the actual distance from the I-End of the frame object to the end of the distributed load. [L]

Val1

This is an array that includes the load value at the start of the distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2

Val2

This is an array that includes the load value at the end of the distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2

GUID

This is an array that includes the global unique ID of the distributed load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the frame object specified by the Name item.

If this item is Group, the assignments are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function is identical to GetLoadDistributed but it includes an extra return parameter, which includes the global unique IDs of the retrieved distributed loads.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## Release Notes

Initial release in version 17.2.0.

## See Also

[SetLoadDistributedWithGUID](../../../SetLoadDistributed_{Frame_Object}.htm)

[DeleteLoadDistributedWithGUID](DeleteLoadDistributedWithGUID_{Frame_Object}.htm)



## GetLoadDistributed {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLoadDistributed_{Frame_Object}.htm`*

# GetLoadDistributed

## Syntax

SapObject.SapModel.FrameObj.GetLoadDistributed

## VB6 Procedure

Function GetLoadDistributed(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef LoadPat() As String, ByRef MyType() As Long, ByRef CSys() As String, ByRef Dir() As Long, ByRef RD1() As Double, ByRef RD2() As Double, ByRef Dist1() As Double, ByRef Dist2() As Double, ByRef Val1() As Double, ByRef Val2() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

NumberItems

The total number of distributed loads retrieved for the specified frame objects.

FrameName

This is an array that includes the name of the frame object associated with each distributed load.

LoadPat

This is an array that includes the name of the coordinate system in which the distributed loads are specified.

MyType

This is an array that includes 1 or 2, indicating the type of distributed load.

1 = Force

2 = Moment

CSys

This is an array that includes the name of the coordinate system in which each distributed load is defined. It may be Local or the name of a defined coordinate system.

Dir

This is an array that includes an integer between 1 and 11, indicating the direction of the load.

1 = Local 1 axis (only applies when CSys is Local)

2 = Local 2 axis (only applies when CSys is Local)

3 = Local 3 axis (only applies when CSys is Local)

4 = X direction (does not apply when CSys is Local)

5 = Y direction (does not apply when CSys is Local)

6 = Z direction (does not apply when CSys is Local)

7 = Projected X direction (does not apply when CSys is Local)

8 = Projected Y direction (does not apply when CSys is Local)

9 = Projected Z direction (does not apply when CSys is Local)

10 = Gravity direction (only applies when CSys is Global)

11 = Projected Gravity direction (only applies when CSys is Global)

The positive gravity direction (see Dir = 10 and 11) is in the negative Global Z direction.

RD1

This is an array that includes the relative distance from the I-End of the frame object to the start of the distributed load.

RD2

This is an array that includes the relative distance from the I-End of the frame object to the end of the distributed load.

Dist1

This is an array that includes the actual distance from the I-End of the frame object to the start of the distributed load. [L]

Dist2

This is an array that includes the actual distance from the I-End of the frame object to the end of the distributed load. [L]

Val1

This is an array that includes the load value at the start of the distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2

Val2

This is an array that includes the load value at the end of the distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the frame object specified by the Name item.

If this item is Group, the assignments are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves the distributed load assignments to frame objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameDistributedLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim LoadPat() As String
      Dim MyType() As Long
      Dim CSys() As String
      Dim Dir() As Long
      Dim RD1() As Double
      Dim RD2() As Double
      Dim Dist1() As Double
      Dim Dist2() As Double
      Dim Val1() As Double
      Dim Val2() As Double

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

   'assign frame distributed loads
      ret = SapModel.FrameObj.SetLoadDistributed("14", "DEAD", 1, 10, 0, 1, 0.08, 0.08)
      ret = SapModel.FrameObj.SetLoadDistributed("15", "DEAD", 1, 10, 0, 1, 0.08, 0.08)

   'get frame distributed loads
      ret = SapModel.FrameObj.GetLoadDistributed("ALL", NumberItems, FrameName, LoadPat, MyType, CSys, Dir, RD1, RD2, Dist1, Dist2, Val1, Val2, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadDistributed](SetLoadDistributed_{Frame_Object}.htm)

[DeleteLoadDistributed](DeleteLoadDistributed_{Frame_Object}.htm)



## GetLoadGravity {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLoadGravity_{Frame_Object}.htm`*

# GetLoadGravity

## Syntax

SapObject.SapModel.FrameObj.GetLoadGravity

## VB6 Procedure

Function GetLoadGravity(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef LoadPat() As String, ByRef CSys() As String, ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

NumberItems

The total number of gravity loads retrieved for the specified frame objects.

FrameName

This is an array that includes the name of the frame object associated with each gravity load.

LoadPat

This is an array that includes the name of the coordinate system in which the gravity load multipliers are specified.

CSys

This is an array that includes the name of the coordinate system associated with each gravity load.

x, y, z

These are arrays of gravity load multipliers in the x, y and z directions of the specified coordinate system.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the frame object specified by the Name item.

If this item is Group, the assignments are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves the gravity load assignments to frame objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameGravityLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim LoadPat() As String
      Dim CSys() As String
      Dim x() As Double
      Dim y() As Double
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'assign frame gravity loads
      ret = SapModel.FrameObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'get frame gravity load
      ret = SapModel.FrameObj.GetLoadGravity("3", NumberItems, FrameName, LoadPat, CSys, x, y, z)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadGravity](SetLoadGravity_{Frame_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Frame_Object}.htm)



## GetLoadPoint {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLoadPoint_{Frame_Object}.htm`*

# GetLoadPoint

## Syntax

SapObject.SapModel.FrameObj.GetLoadPoint

## VB6 Procedure

Function GetLoadPoint(ByVal Name As String, ByRef NumberItems
As Long, ByRef FrameName() As String, ByRef LoadPat() As String, ByRef
MyType() As Long, ByRef CSys() As String, ByRef Dir() As Long, ByRef RelDist()
As Double, ByRef Dist() As Double, ByRef Val() As Double, Optional ByVal
ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

NumberItems

The total number of point loads retrieved for the specified
frame objects.

FrameName

This is an array that includes the name of the frame
object associated with each point load.

LoadPat

This is an array that includes the name of the coordinate
system in which the point loads are specified.

MyType

This is an array that includes 1 or 2, indicating the
type of point load.

1 = Force

2 = Moment

CSys

This is an array that includes the name of the coordinate
system in which each point load is defined. It may be Local or the name
of a defined coordinate system.

Dir

This is an array that includes an integer between 1
and 11 indicating the direction of the load.

1 = Local 1 axis (only
applies when CSys is Local)

2 = Local 2 axis (only
applies when CSys is Local)

3 = Local 3 axis (only
applies when CSys is Local)

4 = X direction (does
not apply when CSys is Local)

5 = Y direction (does
not apply when CSys is Local)

6 = Z direction (does
not apply when CSys is Local)

7 = Not used - Projected
X direction (does not apply when CSys is Local)

8 = Not used - Projected
Y direction (does not apply when CSys is Local)

9 = Not used - Projected
Z direction (does not apply when CSys is Local)

10 = Gravity direction
(only applies when CSys is Global)

11 = Not used - Projected
Gravity direction (only applies when CSys is Global)

The positive gravity direction (see Dir = 10 and 11)
is in the negative Global Z direction.

RelDist

This is an array that includes the relative distance
from the I-End of the frame object to the location where the point load
is applied.

Dist

This is an array that includes the actual distance from
the I-End of the frame object to the location where the point load is
applied. [L]

Val

This is an array that includes the value of the point
load. [F] when MyType is 1 and [FL] when MyType is 2

ItemType

This is one of the following items in the eItemType
enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved
for the frame object specified by the Name item.

If this item is Group, the assignments are retrieved
for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved
for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves the point load assignments to
frame objects.

The function returns zero if the load assignments are
successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePointLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim LoadPat() As String
      Dim MyType() As Long
      Dim CSys() As String
      Dim Dir() As Long
      Dim RelDist() As Double
      Dim Dist() As Double
      Dim Val() As Double

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

   'assign frame point loads
      ret = SapModel.FrameObj.SetLoadPoint("14",
"DEAD", 1, 10, .5, 20)
      ret = SapModel.FrameObj.SetLoadPoint("15",
"DEAD", 1, 10, .5, 20)

   'get frame point loads
      ret = SapModel.FrameObj.GetLoadPoint("ALL",
NumberItems, FrameName, LoadPat, MyType, CSys, Dir, RelDist, Dist, Val,
Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases
and Response Combinations to Load Patterns, Load Cases and Load Combinations,
respectively, in version 12.00.

Changed descriptions for Dir 7, 8, 9 and 11 to "Not
Used" in version 25.0.0

## See Also

[SetLoadPoint](SetLoadPoint.htm)

[DeleteLoadPoint](DeleteLoadPoint.htm)



## GetLoadStrain {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLoadStrain_{Frame_Object}.htm`*

# GetLoadStrain

## Syntax

SapObject.SapModel.FrameObj.GetLoadStrain

## VB6 Procedure

Function GetLoadStrain(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef LoadPat() As String, ByRef DOF() As Long, ByRef Val() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

NumberItems

The total number of strain loads retrieved for the specified frame objects.

FrameName

This is an array that includes the name of the frame object associated with each strain load.

LoadPat

This is an array that includes the name of the load pattern associated with each strain load.

DOF

This is an array that includes 1, 2, 3, 4, 5 or 6, indicating the degree of freedom associated with each strain load.

1 = Strain11

2 = Strain12

3 = Strain13

4 = Curvature1

5 = Curvature2

6 = Curvature3

Val

This is an array that includes the strain value. [L/L] for DOF = 1, 2 and 3 and [1/L] for DOF = 4, 5 and 6

PatternName

This is an array that includes the joint pattern name, if any, used to specify the strain load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the frame object specified by the Name item.

If this item is Group, the assignments are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves the strain load assignments to frame objects.

The function returns zero if the strain load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameStrainLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim LoadPat() As String
      Dim DOF() As Long
      Dim Val() As Double
      Dim PatternName() As String

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

   'assign frame strain load
      ret = SapModel.FrameObj.SetLoadStrain("1", "DEAD", 1, 0.001)

   'get frame strain load
      ret = SapModel.FrameObj.GetLoadStrain("1", NumberItems, FrameName, LoadPat, DOF, Val, PatternName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadStrain](SetLoadStrain_{Frame_Object}.htm)

[DeleteLoadStrain](DeleteLoadStrain_{Frame_Object}.htm)



## GetLoadTargetForce {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLoadTargetForce_{Frame_Object}.htm`*

# GetLoadTargetForce

## Syntax

SapObject.SapModel.FrameObj.GetLoadTargetForce

## VB6 Procedure

Function GetLoadTargetForce(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef LoadPat() As String, ByRef dof1() As Boolean, ByRef dof2() As Boolean, ByRef dof3() As Boolean, ByRef dof4() As Boolean, ByRef dof5() As Boolean, ByRef dof6() As Boolean, ByRef P() As Double, ByRef V2() As Double, ByRef V3() As Double, ByRef T() As Double, ByRef M2() As Double, ByRef M3() As Double, ByRef T1() As Double, ByRef T2() As Double, ByRef T3() As Double, ByRef T4() As Double, ByRef T5() As Double, ByRef T6() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

NumberItems

The total number of deformation loads retrieved for the specified frame objects.

FrameName

This is an array that includes the name of the frame object associated with each target force.

LoadPat

This is an array that includes the name of the load pattern associated with each target force.

dof1, dof2, dof3, dof4, dof5, dof6

These are arrays of boolean values indicating if the considered degree of freedom has a target force assignment.

dof1 = P

dof2 = V2

dof3 = V3

dof4 = T

dof5 = M2

dof6 = M3

P, V2, V3, T, M2, M3

These are arrays of target force values. The target forces specified for a given degree of freedom are applicable only if the corresponding DOF item for that degree of freedom is True.

U1 = U1 deformation [L]

U2 = U2 deformation [L]

U3 = U3 deformation [L]

R1 = R1 deformation [rad]

R2 = R2 deformation [rad]

R3 = R3 deformation [rad]

T1, T2, T3, T4, T5, T6

These are arrays of the relative distances along the frame objects where the target force values apply. The relative distances specified for a given degree of freedom are applicable only if the corresponding dofn item for that degree of freedom is True.

T1 = relative location for P target force

T2 = relative location for V2 target force

T3 = relative location for V3 target force

T4 = relative location for T target force

T5 = relative location for M2 target force

T6 = relative location for M3 target force

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the frame object specified by the Name item.

If this item is Group, the assignments are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves the target force assignments to frame objects.

The function returns zero if the target force assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameTargetForce()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DOF() As Boolean
      Dim f() As double
      Dim RD() As double
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim LoadPat() As String
      Dim dof1() As Boolean
      Dim dof2() As Boolean
      Dim dof3() As Boolean
      Dim dof4() As Boolean
      Dim dof5() As Boolean
      Dim dof6() As Boolean
      Dim P() As Double
      Dim V2() As Double
      Dim V3() As Double
      Dim T() As Double
      Dim M2() As Double
      Dim M3() As Double
      Dim T1() As Double
      Dim T2() As Double
      Dim T3() As Double
      Dim T4() As Double
      Dim T5() As Double
      Dim T6() As Double

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

   'assign frame target force
      ReDim DOF(5)
      ReDim f(5)
      ReDim RD(5)
      DOF(0) = True
      f(0) = 50
      RD(0) = 0.5
      ret = SapModel.FrameObj.SetLoadTargetForce("1", "DEAD", DOF, f, RD)

   'get frame target force
      ret = SapModel.FrameObj.GetLoadTargetForce("1", NumberItems, FrameName, LoadPat, dof1, dof2, dof3, dof4, dof5, dof6, P, V2, V3, T, M2, M3, T1, T2, T3, T4, T5, T6)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadTargetForce](SetLoadTargetForce_{Frame_Object}.htm)

[DeleteLoadTargetForce](DeleteLoadTargetForce_{Frame_Object}.htm)



## GetLoadTemperature {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLoadTemperature_{Frame_Object}.htm`*

# GetLoadTemperature

## Syntax

SapObject.SapModel.FrameObj.GetLoadTemperature

## VB6 Procedure

Function GetLoadTemperature(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef LoadPat() As String, ByRef MyType() As Long, ByRef Val() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

NumberItems

The total number of temperature loads retrieved for the specified frame objects.

FrameName

This is an array that includes the name of the frame object associated with each temperature load.

LoadPat

This is an array that includes the name of the load pattern associated with each temperature load.

MyType

This is an array that includes 1, 2 or 3, indicating the type of temperature load.

1 = Temperature

2 = Temperature gradient along local 2 axis

3 = Temperature gradient along local 3 axis

Val

This is an array that includes the temperature load value. [T] for MyType= 1 and [T/L] for MyType= 2 and 3

PatternName

This is an array that includes the joint pattern name, if any, used to specify the temperature load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the frame object specified by the Name item.

If this item is Group, the assignments are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves the temperature load assignments to frame objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameTemperatureLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim LoadPat() As String
      Dim MyType() As Long
      Dim Val() As Double
      Dim PatternName() As String

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

   'assign frame temperature load
      ret = SapModel.FrameObj.SetLoadTemperature("All", "DEAD", 1, 50, , , Group)

   'get frame temperature load
      ret = SapModel.FrameObj.GetLoadTemperature("ALL", NumberItems, FrameName, LoadPat, MyType, Val, PatternName, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadTemperature](SetLoadTemperature_{Frame_Object}.htm)

[DeleteLoadTemperature](DeleteLoadTemperature_{Frame_Object}.htm)



## GetLoadTransfer

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLoadTransfer.htm`*

# GetLoadTransfer

## Syntax

SapObject.SapModel.FrameObj.GetLoadTransfer

## VB6 Procedure

Function GetLoadTransfer(ByVal Name As String, ByRef Val As Boolean) As Long

## Parameters

Name

The name of an existing frame.

Val

This boolean value indicates if load is allowed to be transferred from area objects to this frame object.

## Remarks

This function returns the load transfer option for a frame object.  It indicates whether the frame receives load from an area object when the area object is loaded with a load of type uniform to frame.

The function returns zero if the load transfer option is successfully returned, otherwise it returns a nonzero value.

## VBA Example

Sub GetLoadTransferOption()

'dimension variables

Dim SapObject as cOAPI

Dim SapModel As cSapModel

Dim ret As Long

Dim val As Boolean

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

'get the load transfer option to False for frame object 1

ret = SapModel.FrameObj.GetLoadTransfer("1", val)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

## Initial release in version 16.0.0.

## See Also

## [SetLoadTransfer](SetLoadTransfer.htm)

##



## GetLocalAxesAdvanced Frame Object

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLocalAxesAdvanced_Frame_Object.htm`*

# GetLocalAxesAdvanced

## Syntax

SapObject.SapModel.FrameObj.GetLocalAxesAdvanced

## VB6 Procedure

Function GetLocalAxesAdvanced(ByVal Name As String, ByRef Active As Boolean, ByRef Plane2 As Long, ByRef PlVectOpt As Long, ByRef PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double) As Long

## Parameters

Name

The name of an existing frame object.

Active

This is True if advanced local axes exist.

Plane2

This is 12 or 13, indicating that the local plane determined by the plane reference vector is the 1-2 plane or the 1-3 plane. This item applies only when the Active item is True.

PlVectOpt

This is 1, 2, or 3, indicating the plane reference vector option. This item applies only when the Active item is True.

1 = Coordinate direction

2 = Two joints

3 = User vector

PlCSys

The coordinate system used to define the plane reference vector coordinate directions and the plane user vector. This item applies when the Active item is True and the PlVectOpt item is 1 or 3.

PlDir

This is an array dimensioned to 1 (2 integers), indicating the plane reference vector primary and secondary coordinate directions, PlDir(0) and PlDir(1) respectively, taken at the object center in the specified coordinate system and used to determine the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 1. Possible coordinate direction values are:

1 = +X      -1 = -X

2 = +Y      -2 = -Y

3 = +Z      -3 = -Z

4 = +CR     -4 = -CR

5 = +CA     -5 = -CA

6 = +CZ     -6 = -CZ

7 = +SR     -7 = -SR

8 = +SA     -8 = -SA

9 = +SB     -9 = -SB

PlPt

This is an array dimensioned to 1 (2 strings), indicating the labels of two joints that define the plane reference vector. Either of these joints may be specified as None to indicate the center of the specified object.  If both joints are specified as None, they are not used to define the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 2.

PlVect

This is an array dimensioned to 2 (3 doubles) that defines the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 3.

## Remarks

This function retrieves the advanced local axes assignments to frame objects.

The function returns zero if the advanced local axes assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameAdvancedLocalAxes()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyPlDir(1) As Long
      Dim MyPlPt(1) As String
      Dim MyPlVect(2) As Double
      Dim Ang As Double
      Dim Advanced As Boolean
      Dim Active As Boolean
      Dim Plane2 As Long
      Dim PlVectOpt As Long
      Dim PlCSys As String
      Dim PlDir() As Long
      Dim PlPt() As String
      Dim PlVect() As Double

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

   'assign frame advanced local axes
      MyPlDir(0) = 2
      MyPlDir(1) = 3
      ret = SapModel.FrameObj.SetLocalAxesAdvanced("3", True, 12, 1, "Global", MyPlDir, MyPlPt, MyPlVect)

   'get frame local axis angle
      ret = SapModel.FrameObj.GetLocalAxes("3", Ang, Advanced)

   'get frame advanced local axes data
      If Advanced Then
         ret = SapModel.FrameObj.GetLocalAxesAdvanced("3", Active, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect)
      End If

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

## See Also

[SetLocalAxesAdvanced](SetLocalAxesAdvanced_Frame_Object.htm)

[SetLocalAxes](SetLocalAxes_{Frame_Object}.htm)

[GetLocalAxes](GetLocalAxes_{Frame_Object}.htm)



## GetLocalAxes {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLocalAxes_{Frame_Object}.htm`*

# GetLocalAxes

## Syntax

SapObject.SapModel.FrameObj.GetLocalAxes

## VB6 Procedure

Function GetLocalAxes(ByVal Name As String, ByRef Ang As Double, ByRef Advanced As Boolean) As Long

## Parameters

Name

The name of an existing frame object.

Ang

This is the angle that the local 2 and 3 axes are rotated about the positive local 1 axis, from the default orientation or, if the Advanced item is True, from the orientation determined by the plane reference vector. The rotation for a positive angle appears counter clockwise when the local +1 axis is pointing toward you. [deg]

Advanced

This item is True if the line object local axes orientation was obtained using advanced local axes parameters.

## Remarks

This function retrieves the frame local axis angle assignment for frame objects.

The function returns zero if the assignment is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameLocalAxisAngle()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Ang As Double
      Dim Advanced As boolean

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

   'get frame local axis angle
      ret = SapModel.FrameObj.GetLocalAxes("3", Ang, Advanced)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetLocalAxes](SetLocalAxes_{Frame_Object}.htm)



## GetMass {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetMass_{Frame_Object}.htm`*

# GetMass

## Syntax

SapObject.SapModel.FrameObj.GetMass

## VB6 Procedure

Function GetMass(ByVal Name As String, ByRef MassOverL As Double) As Long

## Parameters

Name

The name of an existing frame object.

MassOverL

The mass per unit length assigned to the frame object. [M/L]

## Remarks

This function retrieves the frame mass per unit length assignment for frame objects.

The function returns zero if the mass assignment is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameMass()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MassOverL As Double

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

   'assign frame mass
      ret = SapModel.FrameObj.SetMass("ALL", .0001, False, Group)

   'get frame mass assignment
      ret = SapModel.FrameObj.GetMass("3", MassOverL)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMass](SetMass_{Frame_Object}.htm)

[DeleteMass](DeleteMass_{Frame_Object}.htm)



## GetMatTemp {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetMatTemp_{Frame_Object}.htm`*

# GetMatTemp

## Syntax

SapObject.SapModel.FrameObj.GetMatTemp

## VB6 Procedure

Function GetMatTemp(ByVal Name As String, ByRef Temp As Double, ByRef PatternName As String) As Long

## Parameters

Name

The name of an existing frame object.

Temp

This is the material temperature value assigned to the frame object. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the material temperature for the frame object is uniform along the object at the value specified by Temp.

If PatternName is the name of a defined joint pattern, the material temperature for the frame object may vary from one end to the other. The material temperature at each end of the object is equal to the specified temperature multiplied by the pattern value at the joint at the end of the frame object.

## Remarks

This function retrieves the material temperature assignments to frame objects.

The function returns zero if the material temperature assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameMatTemp()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Temp As Double
      Dim PatternName As String

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

   'assign material temperature
      ret = SapModel.FrameObj.SetMatTemp("ALL", 50, , Group)

   'get material temperature
      ret = SapModel.FrameObj.GetMatTemp("3", Temp, PatternName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMatTemp](SetMatTemp_{Frame_Object}.htm)



## GetMaterialOverwrite {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetMaterialOverwrite_{Frame_Object}.htm`*

# GetMaterialOverwrite

## Syntax

SapObject.SapModel.FrameObj.GetMaterialOverwrite

## VB6 Procedure

Function GetMaterialOverwrite(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a defined frame object.

PropName

This is None, indicating that no material overwrite exists for the specified frame object, or it is the name of an existing material property.

## Remarks

This function retrieves the material overwrite assigned to a frame object, if any. It returns None if there is no material overwrite assignment.

The function returns zero if the material overwrite assignment is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameMaterialOverwrite()
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

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'assign material overwrite
      ret = SapModel.FrameObj.SetMaterialOverwrite("3", "4000Psi")

   'get material overwrite assignment
      ret = SapModel.FrameObj.GetMaterialOverwrite("3", PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMaterialOverwrite](SetMaterialOverwrite_{Frame_Object}.htm)



## GetModifiers {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetModifiers_{Frame_Object}.htm`*

# GetModifiers

## Syntax

SapObject.SapModel.FrameObj.GetModifiers

## VB6 Procedure

Function GetModifiers(ByVal Name As String, ByRef Value() As Double) As Long

## Parameters

Name

The name of an existing frame object.

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

This function retrieves the frame modifier assignment for frame objects. The default value for all modifiers is one.

The function returns zero if the modifier assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameModifiers()
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

   'assign modifiers
      ReDim Value(7)
      For i = 0 To 7
         Value(i) = 1
      Next i
      Value(5) = 100
      ret = SapModel.FrameObj.SetModifiers("3", Value)

   'get modifiers
      ReDim Value(7)
      ret = SapModel.FrameObj.GetModifiers("3", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetModifiers](SetModifiers_{Frame_Object}.htm)

[DeleteModifiers](DeleteModifiers_{Frame_Object}.htm)



## GetNameList {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetNameList_{Frame_Object}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.FrameObj.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of frame object names retrieved by the program.

MyName

This is a one-dimensional array of frame object names. The MyName array is created as a dynamic, zero-based, array by the APIuser:

   Dim MyName() as String

The array is dimensioned to (NumberNames – 1) inside the Sap2000 program, filled with the names, and returned to the APIuser.

## Remarks

This function retrieves the names of all defined frame objects.

The function returns zero if the names are successfully retrieved, otherwise it returns nonzero.

## VBA Example

Sub GetFrameObjectNames()
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

   'get frame object names
      ret = SapModel.FrameObj.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetNotionalSize

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetNotionalSize_1.htm`*

# GetNotionalSize

## Syntax

SapObject.SapModel.PropFrame.GetNotionalSize

## VB6 Procedure

Function GetNotionalSize(ByVal Name As String, ByRef stype As String, ByRef Value As Double) As Long

## Parameters

Name

The name of an existing frame section property.

stype

The type to define the notional size of a section. It can be:

"Auto" = Program will determine the notional size based on the average thickness of an area element.

"User" = The notional size is based on the user-defined value.

"None" = Notional size will not be considered. In other words, the time-dependent effect of this section will not be considered.

Value

For stype is "Auto", the Value represents for the scale factor to the program-determined notional size; for **stype** is “User”, the **Value** represents for the user-defined notional size [L]; for **stype** is “None”, the **Value** will not be used and can be set to 1.

## Remarks

This function retrieves the method to determine the notional size of a frame section for the creep and shrinkage calculations. This function is currently worked for the steel/aluminum sections - I/Wide Flange, Channel, Tee, Angle, Double Angle, Double Channel, Pipe and Tube sections, and all the concrete sections - Rectangular, Circular, Pipe, Tube, Precast I.

The function returns zero if the parameters are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePropNotionalSize()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long

 Dim stype As String

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
   ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

'assign parameters
   ret = SapModel.PropFrame.SetNotionalSize("FSEC1", “Auto”, 1.1)

'get parameters
   ret = SapModel.PropFrame.SetNotionalSize("FSEC1", stype, Value)

'close Sap2000
   SapObject.ApplicationExit False
   Set SapModel = Nothing
   Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.1.0

## See Also

[SetNotionalSize](SetNotionalSize_1.htm)



## GetOutputStations {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetOutputStations_{Frame_Object}.htm`*

# GetOutputStations

## Syntax

SapObject.SapModel.FrameObj.GetOutputStations

## VB6 Procedure

Function GetOutputStations(ByVal Name As String, ByRef MyType As Long, ByRef MaxSegSize As Double, ByRef MinSections As Long, ByRef NoOutPutAndDesignAtElementEnds As Boolean, ByRef NoOutPutAndDesignAtPointLoads As Boolean) As Long

## Parameters

Name

The name of an existing frame object.

MyType

This is either 1 or 2 indicating how the output stations are specified.

1 = maximum segment size, that is, maximum station spacing

2 = minimum number of stations

MaxSegSize

The maximum segment size, that is, the maximum station spacing. This item applies only when MyType = 1. [L]

MinSections

The minimum number of stations. This item applies only when MyType = 2.

NoOutPutAndDesignAtElementEnds

If this item is True, no additional output stations are added at the ends of line elements when the frame object is internally meshed.

NoOutPutAndDesignAtPointLoads

If this item is True, no additional output stations are added at point load locations.

## Remarks

This function retrieves frame object output station data.

The function returns zero if the data is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameOutputStationData()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyType As Long
      Dim MaxSegSize As Double
      Dim MinSections As Long
      Dim NoOutPutAndDesignAtElementEnds As Boolean
      Dim NoOutPutAndDesignAtPointLoads As Boolean

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

   'get frame output station data
      ret = SapModel.FrameObj.GetOutputStations("15", MyType, MaxSegSize, MinSections, NoOutPutAndDesignAtElementEnds, NoOutPutAndDesignAtPointLoads)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetOutputStations](SetOutputStations_{Frame_Object}.htm)



## GetPDeltaForce {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetPDeltaForce_{Frame_Object}.htm`*

# GetPDeltaForce

## Syntax

SapObject.SapModel.FrameObj.GetPDeltaForce

## VB6 Procedure

Function GetPDeltaForce(ByVal Name As String, ByRef NumberForces As Long, ByRef PDeltaForce() As Double, ByRef Dir() As Long, ByRef CSys() As String) As Long

## Parameters

Name

The name of an existing straight frame object.

NumberForces

The number of P-Delta forces assigned to the frame object.

PDeltaForce

This is an array of the P-Delta force values assigned to the frame object. [F]

Dir

This is an array that contains 0, 1, 2 or 3, indicating the direction of each P-Delta force assignment.

0 = Frame object local 1-axis direction

1 = Projected X direction in CSys coordinate system

2 = Projected Y direction in CSys coordinate system

3 = Projected Z direction in CSys coordinate system

CSys

This is an array that contains the name of the coordinate system in which each projected P-Delta force is defined. This item is blank when the Dir item is zero, that is, when the P-Delta force is defined in the frame object local 1-axis direction.

## Remarks

This function retrieves the P-Delta force assignments to frame objects. P-Delta forces do not apply to curved frame objects. If you request data for a curved frame, an error is returned.

The function returns zero if the assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePDeltaForce()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberForces As Long
      Dim PDeltaForce() As Double
      Dim Dir() As Long
      Dim CSys() As String

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

   'assign P-Delta force
      ret = SapModel.FrameObj.SetPDeltaForce("ALL", 100, 0, True, , Group)

   'get P-Delta force
      ret = SapModel.FrameObj.GetPDeltaForce("3", NumberForces, PDeltaForce, Dir, CSys)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetPDeltaForce](SetPDeltaForce.htm)

[DeletePDeltaForce](DeletePDeltaForce.htm)



## GetPoints {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetPoints_{Frame_Object}.htm`*

# GetPoints

## Syntax

SapObject.SapModel.FrameObj.GetPoints

## VB6 Procedure

Function GetPoints(ByVal Name As String, ByRef Point1 As String, ByRef Point2 As String) As Long

## Parameters

Name

The name of a defined frame object.

Point1

The name of the point object at the I-End of the specified frame object.

Point2

The name of the point object at the J-End of the specified frame object.

## Remarks

This function retrieves the names of the point objects at each end of a specified frame object.

The function returns zero if the point names are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameObjPoints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Point1 As String
      Dim Point2 As String

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

   'get names of points
      ret = SapModel.FrameObj.GetPoints("3", Point1, Point2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetReleases {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetReleases_{Frame_Object}.htm`*

# GetReleases

## Syntax

SapObject.SapModel.FrameObj.GetReleases

## VB6 Procedure

Function GetReleases(ByVal Name As String, ByRef ii() As Boolean, ByRef jj() As Boolean, ByRef StartValue() As Double, ByRef EndValue() As Double) As Long

## Parameters

Name

The name of an existing frame object.

ii, jj

These are arrays of six booleans indicating the I-End and J-End releases for the frame object.

ii(0) and jj(0) = U1 release

ii(1) and jj(1) = U2 release

ii(2) and jj(2) = U3 release

ii(3) and jj(3) = R1 release

ii(4) and jj(4) = R2 release

ii(5) and jj(5) = R3 release

StartValue, EndValue

These are arrays of six values indicating the I-End and J-End partial fixity springs for the frame object.

StartValue(0) and EndValue(0) = U1 partial fixity [F/L]

StartValue(1) and EndValue(1) = U2 partial fixity [F/L]

StartValue(2) and EndValue(2) = U3 partial fixity [F/L]

StartValue(3) and EndValue(3) = R1 partial fixity [FL/rad]

StartValue(4) and EndValue(4) = R2 partial fixity [FL/rad]

StartValue(5) and EndValue(5) = R3 partial fixity [FL/rad]

## Remarks

This function retrieves the frame object end release and partial fixity assignments.

The function returns zero if the assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameEndReleases()
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

   'assign end releases
      ReDim ii(5)
      ReDim jj(5)
      ReDim StartValue(5)
      ReDim EndValue(5)
      ii(5) = True
      jj(5) = True
      ret = SapModel.FrameObj.SetReleases("13", ii, jj, StartValue, EndValue)

   'get end releases
      ReDim ii(5)
      ReDim jj(5)
      ReDim StartValue(5)
      ReDim EndValue(5)
      ret = SapModel.FrameObj.GetReleases("13", ii, jj, StartValue, EndValue)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetReleases](SetReleases_{Frame_Object}.htm)



## GetSectionNonPrismatic

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetSectionNonPrismatic.htm`*

# GetSectionNonPrismatic

## Syntax

SapObject.SapModel.FrameObj.GetSectionNonPrismatic

## VB6 Procedure

Function GetSectionNonPrismatic(ByVal Name As String, ByRef PropName As String, ByRef sVarTotalLength As Double, ByRef sVarRelStartLoc As Double) As Long

## Parameters

Name

The name of a defined frame object.

PropName

The name of the nonprismatic frame section property assigned to the frame object.

sVarTotalLength

This is the total assumed length of the nonprismatic section. Enter 0 for this item to indicate that the section length is the same as the frame object length.

sVarRelStartLoc

This is the relative distance along the nonprismatic section to the I-End (start) of the frame object. This item is ignored when the sVarTotalLengthitem is 0.

## Remarks

This function retrieves the nonprismatic frame section property data assigned to a frame object.

The function returns zero if the nonprismatic frame object property data is successfully retrieved, otherwise it returns a nonzero value.

The function returns an error if the section property assigned to the frame object is not a nonprismatic property.

## VBA Example

Sub GetFrameSectionNonPrismatic()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim StartSec() As String
      Dim EndSec() As String
      Dim MyLength() As Double
      Dim MyType() As Long
      Dim EI33() As Long
      Dim EI22() As Long
      Dim Color As Long
      Dim Notes As String
      Dim GUID As String
      Dim PropName As String
      Dim sVarTotalLength As Double
      Dim sVarRelStartLoc As Double

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

   'set new I-type frame section property
      ret = SapModel.PropFrame.SetISection("ISEC1", "A992Fy50", 24, 8, 0.5, 0.3, 8, 0.5)

   'set new I-type frame section property
      ret = SapModel.PropFrame.SetISection("ISEC2", "A992Fy50", 20, 8, 0.5, 0.3, 8, 0.5)

   'set new nonprismatic frame section property
      ReDim StartSec(2)
      ReDim EndSec(2)
      ReDim MyLength(2)
      ReDim MyType(2)
      ReDim EI33(2)
      ReDim EI22(2)
      StartSec(0) = "ISEC2"
      EndSec(0) = "ISEC1"
      MyLength(0) = 60
      MyType(0) = 2
      EI33(0)= 2
      EI22(0)= 1

      StartSec(1) = "ISEC1"
      EndSec(1) = "ISEC1"
      MyLength(1) = 1
      MyType(1) = 1
      EI33(1)= 2
      EI22(1)= 1

      StartSec(2) = "ISEC1"
      EndSec(2) = "ISEC2"
      MyLength(2) = 60
      MyType(2) = 2
      EI33(2)= 2
      EI22(2)= 1

      ret = SapModel.PropFrame.SetNonPrismatic("NP1", 3, StartSec, EndSec, MyLength, MyType, EI33, EI22)

   'set frame section property
      ret = SapModel.FrameObj.SetSection("8", "NP1", Object, 0.1, 360)

   'get nonprismatic frame section property
      ret = SapModel.FrameObj.GetSectionNonPrismatic("8", PropName, sVarTotalLength, sVarRelStartLoc)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSection](GetSection_{Frame_Object}.htm)

[SetSection](SetSection.htm)



## GetSection {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetSection_{Frame_Object}.htm`*

# GetSection

## Syntax

SapObject.SapModel.FrameObj.GetSection

## VB6 Procedure

Function GetSection(ByVal Name As String, ByRef PropName
As String, ByRef SAuto As String) As Long

## Parameters

Name

The name of a defined frame object.

PropName

If no auto select list is assigned to the frame object,
this is the name of the frame section property assigned to the frame object.
If an auto select list is assigned to the frame object, this is the name
of the frame section property, within the auto select list, which is currently
being used as the analysis property for the frame object. If this item
is None, no frame section property is assigned to the frame object.

SAuto

This is the name of the auto select list assigned to
the frame object, if any. If this item is returned as a blank string,
no auto select list is assigned to the frame object.

## Remarks

This function retrieves the frame section property assigned
to a frame object.

The function returns zero if the frame object property
is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameSectionProp()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim PropName As String
      Dim SAuto As String

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

   'get frame section property
      ret = SapModel.FrameObj.GetSection("3",
PropName, SAuto)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSectionNonPrismatic](GetSectionNonPrismatic.htm)

[SetSection](SetSection.htm)



## GetSelected {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetSelected_{Frame_Object}.htm`*

# GetSelected

## Syntax

Sap2000.FrameObj.GetSelected

## VB6 Procedure

Function GetSelected(ByVal Name As String, ByRef Selected As Boolean) As Long

## Parameters

Name

The name of an existing frame object.

Selected

This item returns True if the specified frame object is selected, otherwise it returns False.

## Remarks

This function retrieves the selected status for a frame object.

The function returns zero if the selected status is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameObjectSelectedStatus()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Selected As Boolean

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

   'set all frames selected
      ret = SapModel.FrameObj.SetSelected("All", True, Group)

   'get frame object selected status
      ret = SapModel.FrameObj.GetSelected("8", Selected)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSelected](SetSelected_{Frame_Object}.htm)



## GetSpring {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetSpring_{Frame_Object}.htm`*

# GetSpring

## Syntax

SapObject.SapModel.FrameObj.GetSpring

## VB6 Procedure

Function GetSpring(ByVal Name As String, ByRef NumberSprings As Long, ByRef MyType() As Long, ByRef s() As Double, ByRef SimpleSpringType() As Long, ByRef LinkProp() As String, ByRef SpringLocalOneType() As Long, ByRef Dir() As Long, ByRef Plane23Angle() As Double, ByRef VecX() As Double, ByRef VecY() As Double, ByRef VecZ() As Double, ByRef CSys() As String, ByRef Ang() As Double) As Long

## Parameters

Name

The name of an existing frame object.

NumberSprings

The number of springs assignments made to the specified frame object.

MyType

Each value in this array is either 1 or 2, indicating the spring property type.

1 = Simple spring

2 = Link property

s

Each value in this array is the simple spring stiffness per unit length of the frame object. This item applies only when the corresponding MyType = 1. [F/L2]

SimpleSpringType

Each value in this array is 1, 2 or 3, indicating the simple spring type. This item applies only when the corresponding MyType = 1.

1 = Spring resists tension and compression

2 = Spring resists compression only

3 = Spring resists tension only

LinkProp

Each value in this array is the name of the link property assigned to the spring. This item applies only when the corresponding MyType = 2.

SpringLocalOneType

Each value in this array is 1, 2 or 3, indicating the method used to specify the spring positive local 1-axis orientation.

1 = Parallel to frame object local axis

2 = In the frame object 2-3 plane

3 = User specified direction vector

Dir

Each value in this array is 1, 2, 3, -1, -2 or -3, indicating the frame object local axis that corresponds to the positive local 1-axis of the spring. This item applies only when the corresponding SpringLocalOneType = 1.

Plane23Angle

Each value in this array is the angle in the frame object 2-3 plane measured counter clockwise from the frame positive 2-axis to the spring positive 1-axis. This item applies only when the corresponding SpringLocalOneType = 2. [deg]

VecX

Each value in this array is the X-axis or frame local 1-axis component (depending on the CSys specified) of the user specified direction vector for the spring local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when the corresponding SpringLocalOneType = 3.

VecY

Each value in this array is the Y-axis or frame local 2-axis component (depending on the CSys specified) of the user specified direction vector for the spring local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when the corresponding SpringLocalOneType = 3.

VecZ

Each value in this array is the X-axis or frame local 3-axis component (depending on the CSys specified) of the user specified direction vector for the spring local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when the corresponding SpringLocalOneType = 3.

CSys

Each value in this array is Local (meaning the frame object local coordinate system) or the name of a defined coordinate system. This item is the coordinate system in which the user specified direction vector, Vec, is specified. This item applies only when the corresponding SpringLocalOneType = 3.

Ang

Each value in this array is the angle that the link local 2-axis is rotated from its default orientation. This item applies only when the corresponding MyType = 2. [deg]

## Remarks

This function retrieves the spring assignments to a frame object.

The function returns zero if the assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameSprings()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Vec() As Double
      Dim NumberSprings As Long
      Dim MyType() As Long
      Dim s() As Double
      Dim SimpleSpringType() As Long
      Dim LinkProp() As String
      Dim SpringLocalOneType() As Long
      Dim Dir() As Long
      Dim Plane23Angle() As Double
      Dim VecX() As Double
      Dim VecY() As Double
      Dim VecZ() As Double
      Dim CSys() As String
      Dim Ang() As Double

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

   'assign springs to frame
      ReDim Vec(2)
      ret = SapModel.FrameObj.SetSpring("ALL", 1, 1, 1, "", 1, 2, 0, Vec, 0, False, "Local", Group)

   'get spring assignments to frames
      ret = SapModel.FrameObj.GetSpring("1", numbersprings, MyType, s, SimpleSpringType, LinkProp, SpringLocalOneType, Dir, Plane23Angle, VecX, VecY, VecZ, CSys, Ang)

   'close Sap2000}
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSpring](SetSpring__{Frame_Object}.htm)

[DeleteSpring](DeleteSpring_{Frame_Object}.htm)



## GetTC Limits {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetTCLimits{Frame_Object}.htm`*

# GetTCLimits

## Syntax

SapObject.SapModel.FrameObj.GetTCLimits

## VB6 Procedure

Function GetTCLimits(ByVal Name As String, ByRef LimitCompressionExists As Boolean, ByRef LimitCompression As Double, ByRef LimitTensionExists As Boolean, ByRef LimitTension As Double) As Long

## Parameters

Name

The name of an existing frame object.

LimitCompressionExists

This item is True if a compression force limit exists for the frame object.

LimitCompression

The compression force limit for the frame object. [F]

LimitTensionExists

This item is True if a tension force limit exists for the frame object.

LimitTension

The tension force limit for the frame object. [F]

## Remarks

This function retrieves the tension/compression force limit assignments to frame objects.

The function returns zero if the assignments are successfully retrieved, otherwise it returns a nonzero value.

Note that the tension and compression limits are used only in nonlinear analyses.

## VBA Example

Sub GetFrameTCLimits()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim LimitCompressionExists As Boolean
      Dim LimitCompression As Double
      Dim LimitTensionExists As Boolean
      Dim LimitTension As Double

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

   'assign tension/compression limits
      ret = SapModel.FrameObj.SetTCLimits("1", False, 0, True, 100)

   'get tension/compression limits
      ret = SapModel.FrameObj.GetTCLimits("1", LimitCompressionExists, LimitCompression, LimitTensionExists, LimitTension)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetTCLimits](SetTCLimits_{Frame_Object}htm.htm)



## GetTransformationMatrix {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetTransformationMatrix_{Frame_Object}.htm`*

# GetTransformationMatrix

## Syntax

Sap2000.FrameObj.GetTransformationMatrix

## VB6 Procedure

Function GetTransformationMatrix(ByVal Name As String, ByRef Value() As Double,Optional ByVal IsGlobal As Boolean = True) As Long

## Parameters

Name

The name of an existing frame object.

Value

Value is an array of nine direction cosines that define the transformation matrix.

The following matrix equation shows how the transformation matrix is used to convert items from the frame object local coordinate system to the global coordinate system.

![](../../../assets/images/Images/Transformation%20Matrix.JPG)

In the equation, c0 through c8 are the nine values from the transformation array, (Local1, Local2, Local3) are an item (such as a load) in the object local coordinate system, and (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.

The transformation from the local coordinate system to the present coordinate system is the same as that shown above for the global system if you substitute the present system for the global system.

IsGlobal

If this item is True, the transformation matrix is between the Global coordinate system and the frame object local coordinate system.

If this item is False, the transformation maxtrix is between the present coordinate system and the frame object local coordinate system.

## Remarks

The function returns zero if the frame object transformation matrix is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameObjectMatrix()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'assign frame object local axis angle
      ret = SapModel.FrameObj.SetLocalAxes("3", 30)

   'get frame object transformation matrix
      ReDim Value(8)
      ret = SapModel.FrameObj.GetTransformationMatrix("3", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetTrapezoidal

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetTrapezoidal.htm`*

# GetTrapezoidal

## Syntax

SapObject.SapModel.PropFrame.GetTrapezoidal

## VB6 Procedure

Function GetTrapezoidal(ByVal Name As String, ByRef FileName As String, ByRef MatProp As String, ByRef t3 As Double, ByRef t2 As Double, ByRef t2b As Double, ByRef Color As Long, ByRef Notes As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing trapezoidal frame section property.

FileName

If the section property was imported from a property file, this is the name of that file. If the section property was not imported, this item is blank.

MatProp

The name of the material property for the section.

t3

The section depth. [L]

t2

The section top width. [L]

t2b

The section bottom width. [L]

Color

The display color assigned to the section.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned to the section.

## Remarks

This function retrieves frame section property data for a trapezoidal frame section.

The function returns zero if the section property is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetFramePropTrapezoidal()

   'dimension variables

      Dim SapObject as cOAPI

      Dim SapModel As cSapModel

      Dim ret As Long

      Dim FileName As String
      Dim MatProp As String
      Dim t3 As Double
      Dim t2 As Double
      Dim t2b As Double
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
      ret = SapModel.PropFrame.SetTrapezoidal("R1", "4000Psi", 20, 20, 12)

  'get frame section property data

      ret = SapModel.PropFrame.SetTrapezoidal("R1", FileName, MatProp, t3, t2, t2b, Color, Notes, GUID)

  'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 17.2.0

## See Also

SetTrapezoidal

SetRebarBeam

SetRebarColumn

GetRebarBeam

GetRebarColumn



## GetTypeOAPI {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/GetType_{Frame_Object}.htm`*

# GetTypeOAPI

## Syntax

SapObject.SapModel.FrameObj.GetTypeOAPI

## VB6 Procedure

Function GetTypeOAPI(ByVal Name As String, ByRef MyType As String) As Long

## Parameters

Name

The name of a defined frame object.

MyType

This is Straight or Curved, indicating the type of frame object.

## Remarks

This function retrieves the type of frame object (straight or curved).

The function returns zero if the frame object type is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetFrameType()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyType As String

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

   'get frame type
      ret = SapModel.FrameObj.GetTypeOAPI("3", MyType)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed function name to GetTypeOAPI in v17.0.0.

## See Also

[SetStraight](SetStraight.htm)

[SetCurved](SetCurved.htm)

[GetCurved](../../Obsolete_Functions/GetCurved.htm)



## SetAutoMesh {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetAutoMesh_{Frame_Object}.htm`*

# SetAutoMesh

## Syntax

SapObject.SapModel.FrameObj.SetAutoMesh

## VB6 Procedure

Function SetAutoMesh(ByVal Name As String, ByVal AutoMesh As Boolean, ByVal AutoMeshAtPoints As Boolean, ByVal AutoMeshAtLines As Boolean, ByVal NumSegs As Long, ByVal AutoMeshMaxLength As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

AutoMesh

This item is True if the frame object is to be automatically meshed by the program when the analysis model is created.

AutoMeshAtPoints

This item is applicable only when the AutoMesh item is True. If this item is True, the frame object is automatically meshed at intermediate joints along its length.

AutoMeshAtLines

This item is applicable only when the AutoMesh item is True. If this item is True, the frame object is automatically meshed at intersections with other frames, area object edges and solid object edges.

NumSegs

This item is applicable only when the AutoMesh item is True. It is the minimum number of elements into which the frame object is automatically meshed. If this item is zero, the number of elements is not checked when the automatic meshing is done.

AutoMeshMaxLength

This item is applicable only when the AutoMesh item is True. It is the maximum length of auto meshed frame elements. If this item is zero, the element length is not checked when the automatic meshing is done. [L]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function makes automatic meshing assignments to frame objects.

The function returns zero if the meshing options are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameAutoMesh()
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

   'assign automesh options
      ret = SapModel.FrameObj.SetAutoMesh("ALL", True, True, True, 0, 0, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetAutoMesh](GetAutoMesh_{Frame_Object}.htm)



## SetCurved

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetCurved.htm`*

# SetCurved

## Syntax

SapObject.SapModel.FrameObj.SetCurved

## VB6 Procedure

Function SetCurved(ByVal Name As String, ByVal MyType As Long, ByVal x As Double, ByVal y As Double, ByVal z As Double, ByVal PointName As String, ByVal Radius As Double, ByVal NumSegs As Long, Optional ByVal CSys As String = "Global") As Long

## Parameters

Name

The name of a defined curved frame object.

MyType

This is 1, 2, 3, 4, or 5, indicating the curved frame type.

1 = Circular Arc Specified by a Third Point Name

2 = Circular Arc Specified by Third Point Coordinates

3 = Circular Arc Specified by Planar Point Coordinates and Radius

4 = Parabolic Arc Specified by a Third Point Name

5 = Parabolic Arc Specified by Third Point Coordinates

MyTypes 1, 2, 4, and 5 all define the curve by three points. The three points are the two end point of the frame object and a third point defined by naming an existing point object or specifying point coordinates.

MyType 3 defines a circular curved frame by it end points, the coordinates of another point that lies in the plane of the curve but not necessarily on the curved frame, and a curve radius.

x, y, z

These are point coordinates in the coordinate system specified by CSys. [L]

For MyType 1 and 4 these items do not apply.

For MyType 2 and 5 these are the coordinates of the third point on the curved frame.

For MyType 3 these are the coordinates of the planar point that lies in the plane of the curved frame.

PointName

This is the name of the point object that is the third point on the curved frame. This item applies for MyType 1 and 4. It does not apply for MyType 2, 3 and 5.

Radius

The radius of the circular curved frame. This item only applies for MyType 3. [L]

NumSegs

This is the number of segments into which the program internally divides the curved frame.

CSys

This is the coordinate system in which the coordinates x, y and z are defined.

## Remarks

This function changes the curve data for a curved frame object and sets straight frame objects to be curved.

The function returns zero if the frame object type is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetFrameCurved()
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

   'set frame curved
      ret = SapModel.FrameObj.SetCurved("13", 1, 0, 0, 0, "1", 0, 16)
      ret = SapModel.FrameObj.SetCurved("14", 2, -200, 0, 176, "", 0, 16)
      ret = SapModel.FrameObj.SetCurved("15", 3, 0, 0, 0, "", 100, 16)
      ret = SapModel.FrameObj.SetCurved("16", 4, 0, 0, 0, "3", 0, 16)
      ret = SapModel.FrameObj.SetCurved("17", 5, 0, 0, 176, "", 0, 16)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Modified optional argument CSys to be ByVal in version 12.0.1.

## See Also

[SetStraight](SetStraight.htm)

[GetCurved](../../Obsolete_Functions/GetCurved.htm)

[GetType](GetType_{Frame_Object}.htm)



## SetDesignProcedure

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetDesignProcedure.htm`*

# SetDesignProcedure

## Syntax

SapObject.SapModel.FrameObj.SetDesignProcedure

## VB6 Procedure

Function SetDesignProcedure(ByVal Name As String, ByVal MyType As Long, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

MyType

This is 1 or 2, indicating the design procedure type desired for the specified frame object.

1 = Default from material

2 = No design

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

Selection = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is Selection, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the design procedure for frame objects.

The function returns zero if the design procedure is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetFrameObjDesignProcedure()
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

   'set design procedure
      ret = SapModel.FrameObj.SetDesignProcedure("8", 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.02.

## See Also

[GetDesignProcedure](GetDesignProcedure.htm)



## SetEndLengthOffset

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetEndLengthOffset.htm`*

# SetEndLengthOffset

## Syntax

SapObject.SapModel.FrameObj.SetEndLengthOffset

## VB6 Procedure

Function SetEndLengthOffset(ByVal Name As String, ByVal AutoOffset As Boolean, ByVal Length1 As Double, ByVal Length2 As Double, ByVal rz As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

AutoOffset

If this item is True, the end length offsets are automatically determined by the program from object connectivity, and the Length1, Length2 and rz items are ignored.

Length1

The offset length along the 1-axis of the frame object at the I-End of the frame object. [L]

Length2

The offset along the 1-axis of the frame object at the J-End of the frame object. [L]

rz

The rigid zone factor.  This is the fraction of the end offset length assumed to be rigid for bending and shear deformations.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function assigns frame object end offsets along the 1-axis of the object.

The function returns zero if the offsets are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameEndOffsets()
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

   'assign offsets
      ret = SapModel.FrameObj.SetEndLengthOffset("15", False, 12, 12, 0.5)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetEndLengthOffset](GetEndLengthOffset_{Frame_Object}.htm)



## SetEndSkew

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetEndSkew.htm`*

# SetEndSkew

## Syntax

SapObject.SapModel.FrameObj.SetEndSkew

## VB6 Procedure

Function SetEndSkew(ByVal Name As String, ByVal SkewI As Double, ByVal SkewJ As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

SkewI

The angle in degrees measured counter clockwise from the positive local 3-axis to a line parallel to the I-End of the frame object (-90 < SkewI < 90). [deg]

SkewJ

The angle in degrees measured counter clockwise from the positive local 3-axis to a line parallel to the J-End of the frame object (-90 < SkewJ < 90). [deg]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function assigns frame object end skew data. End skew data is used in the program to plot the extruded view of bridge objects that have been updated as spine models only.

The function returns zero if the end skew data is successfully assigned, otherwise it returns a nonzero value.

End skew assignments are applicable only to straight frame objects.

## VBA Example

Sub AssignFrameEndSkewData()
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

   'assign frame end skew data
      ret = SapModel.FrameObj.SetEndSkew("15", 10, 20)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetEndSkew](GetEndSkew.htm)



## SetFireproofing_1

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetFireproofing_1.htm`*

# SetFireproofing\_1

## Syntax

SapObject.SapModel.FrameObj.SetFireProofing\_1

## VB6 Procedure

Function SetFireProofing\_1(ByVal Name As String, ByVal MyType As Long, ByVal Thickness As Double, ByVal Perimeter As Double, ByVal Density As Double, ByVal tf As Boolean, ByVal IncludeInSelfWeightAs Boolean, ByVal IncludeInGravityLoads As Boolean, Optional ByVal IncludeInThisLoadPattern As String = "None", Optional ByVal ItemType As eItemType = Object) As Long

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

IncludeInSelfWeight

If this item is True the fireproofing is included in the structure self weight.

IncludeInGravityLoads

If this item is True the fireproofing is included gravity loads applied in the X, Y and Z directions.

IncludeInThisLoadPattern

This item is either None or the name of an existing load pattern. If it is the name of a load pattern then the weight of the fireproofing is applied as a distributed load in the global Z direction in the load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## **Remarks**

This function sets the fireproofing assignments to existing frame objects.

The function returns zero if the fireproofing assignments are successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetFireproofing()

'dimension variables

Dim SapObject As Sap2000v16.SapObject

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

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fireproofing", LTYPE\_SUPERDEAD)

'assign fireproofing, use in self weight and in load pattern

ret = SapModel.FrameObj.SetFireproofing\_1("ALL", 1, 2, 0, 8.68E-06, False, True, False, "Fireproofing", Group)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.0.0.  This function supersedes obsolete function SetFireProofing

## See Also

[GetFireProofing\_1](GetFireproofing_1.htm)

[DeleteFireProofing](DeleteFireproofing.htm)



## SetGUID {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetGUID_{Frame_Object}.htm`*

# SetGUID

## Syntax

SapObject.SapModel.FrameObj.SetGUID

## VB6 Procedure

Function SetGUID(ByVal Name As String, Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing frame object.

GUID

The GUID (Global Unique ID) for the specified frame object.

## Remarks

This function sets the GUID for the specified frame object. If the GUID is passed in as a blank string, the program automatically creates a GUID for the object.

This function returns zero if the frame object GUID is successfully set; otherwise it returns nonzero.

## VBA Example

Sub SetFrameObjGUID()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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

   'set program created GUID
      ret = SapObject.SapModel.FrameObj.SetGUID("1")

   'get GUID
      ret = SapObject.SapModel.FrameObj.GetGUID("1", GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[GetGUID](GetGUID_{Frame_Object}.htm)



## SetGroupAssign {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetGroupAssign_{Frame_Object}.htm`*

# SetGroupAssign

## Syntax

SapObject.SapModel.FrameObj.SetGroupAssign

## VB6 Procedure

Function SetGroupAssign(ByVal Name As String, ByVal GroupName As String, Optional By Val Remove As Boolean = False, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

GroupName

The name of an existing group to which the assignment is made.

Remove

If this item is False, the specified frame objects are added to the group specified by the GroupName item. If it is True, the frame objects are removed from the group.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the frame object specified by the Name item is added or removed from the group specified by the GroupName item.

If this item is Group, all frame objects in the group specified by the Name item are added or removed from the group specified by the GroupName item.

If this item is SelectedObjects, all selected frame objects are added or removed from the group specified by the GroupName item, and the Name item is ignored.

## Remarks

This function adds or removes frame objects from a specified group.

The function returns zero if the group assignment is successful, otherwise it returns a nonzero value.

## VBA Example

Sub AddFrameObjectsToGroup()
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

   'define new group
      ret = SapModel.GroupDef.SetGroup("Group1")

   'add frame objects to group
      ret = SapModel.FrameObj.SetGroupAssign("8", "Group1")
      ret = SapModel.FrameObj.SetGroupAssign("10", "Group1")

   'select objects in group
      ret = SapModel.SelectObj.Group("Group1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetGroupAssign](GetGroupAssign_{Frame_Object}.htm)



## SetInsertionPoint_1 {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetInsertionPoint_1{Frame_Object}.htm`*

# SetInsertionPoint\_1

## Syntax

SapObject.SapModel.FrameObj.SetInsertionPoint\_1

## VB6 Procedure

Function SetInsertionPoint\_1(ByVal Name As String, ByVal
CardinalPoint As Long, ByVal Mirror2, ByVal Mirror3,  As Boolean,
ByVal StiffTransform As Boolean, ByRef Offset1() As Double, ByRef Offset2()
As Double, Optional ByVal CSys As String = "Local", Optional
ByVal ItemType As eItemType = Object) As Long

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

Mirror3

If this item is True, the frame object section is assumed
to be mirrored (flipped) about its local 3-axis.

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
      ret = SapModel.FrameObj.SetInsertionPoint\_1("15",
7, False, False, True, Offset1, Offset2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.1.

This function supersedes [SetInsertionPoint](../../Obsolete_Functions/SetInsertionPoint{Frame_Object}.htm),
adding the Mirror3 parameter.

## See Also

[GetInsertionPoint\_1](GetInsertionPoint_1{Frame_Object}.htm)



## SetLateralBracing

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLateralBracing.htm`*

# SetLateralBracing

## Syntax

SapObject.SapModel.FrameObj.SetLateralBracing

## VB6 Procedure

Function SetLateralBracing(ByVal Name As String, ByVal MyType As Long, ByVal Loc As Long, ByVal MyDist1 As Double, ByVal MyDist2 As Double, Optional ByVal RelDist As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

MyType

This is 1 or 2, indicating the bracing type assigned.

1 = Point bracing

2 = Uniform bracing

Loc

This is 1, 2 or 3, indicating the bracing location.

1 = Top

2 = Bottom

3 = All (top and bottom)

MyDist1

When MyType = 1 this is the location of the point bracing.

When MyType = 2 this is the location of the start of the uniform bracing. [L] when RelDist = False

MyDist2

This item is not used when MyType = 1.

When MyType = 2 this is the location of the end of the uniform bracing. [L] when RelDist = False

RelDist

If this item is True, MyDist1 and MyDist2 are relative distances; otherwise they are actual distances.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function assigns a lateral bracing location to frame objects.

The function returns zero if the location is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameLateralBracing()
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

   'assign frame lateral bracing
      ret = SapModel.FrameObj.SetLateralBracing("8", 1, 3, 0, 0)
      ret = SapModel.FrameObj.SetLateralBracing("8", 1, 3, 0.25, 0)
      ret = SapModel.FrameObj.SetLateralBracing("8", 1, 3, 1, 0)
      ret = SapModel.FrameObj.SetLateralBracing("8", 2, 1, 0.5, 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetLateralBracing](GetLateralBracing.htm)

[DeleteLateralBracing](DeleteLateralBracing.htm)



## SetLoadDeformation {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLoadDeformation_{Frame_Object}.htm`*

# SetLoadDeformation

## Syntax

SapObject.SapModel.FrameObj.SetLoadDeformation

## VB6 Procedure

Function SetLoadDeformation(ByVal Name As String, ByVal LoadPat As String, ByRef DOF() As Boolean, ByRef d() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

DOF

This is a array of boolean values indicating if the considered degree of freedom has a deformation load.

DOF(1) = U1

DOF(2) = U2

DOF(3) = U3

DOF(4) = R1

DOF(5) = R2

DOF(6) = R3

d

This is a array of deformation load values. The deformations specified for a given degree of freedom are applied only if the corresponding DOF item for that degree of freedom is True.

d(1) = U1 deformation [L]

d(2) = U2 deformation [L]

d(3) = U3 deformation [L]

d(4) = R1 deformation [rad]

d(5) = R2 deformation [rad]

d(6) = R3 deformation [rad]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function assigns deformation loads to frame objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameDeformationLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DOF() As Boolean
      Dim d() As double

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

   'assign frame deformation loads
      ReDim DOF(5)
      ReDim d(5)
      DOF(0) = True
      D(0) = 2
      ret = SapModel.FrameObj.SetLoadDeformation("ALL", "DEAD", DOF, d, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDeformation](GetLoadDeformation_{Frame_Object}.htm)

[DeleteLoadDeformation](DeleteLoadDeformation_{Frame_Object}.htm)



## SetLoadDistributed {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLoadDistributed_{Frame_Object}.htm`*

# SetLoadDistributed

## Syntax

SapObject.SapModel.FrameObj.SetLoadDistributed

## VB6 Procedure

Function SetLoadDistributed(ByVal Name As String, ByVal LoadPat As String, ByVal MyType As Long, ByVal Dir As Long, ByVal Dist1 As Double, ByVal Dist2 As Double, ByVal Val1 As Double, ByVal Val2 As Double, Optional ByVal CSys As String = "Global", Optional ByVal RelDist As Boolean = True, Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

MyType

This is 1 or 2, indicating the type of distributed load.

1 = Force per unit length

2 = Moment per unit length

Dir

This is an integer between 1 and 11, indicating the direction of the load.

1 = Local 1 axis (only applies when CSys is Local)

2 = Local 2 axis (only applies when CSys is Local)

3 = Local 3 axis (only applies when CSys is Local)

4 = X direction (does not apply when CSys is Local)

5 = Y direction (does not apply when CSys is Local)

6 = Z direction (does not apply when CSys is Local)

7 = Projected X direction (does not apply when CSys is Local)

8 = Projected Y direction (does not apply when CSys is Local)

9 = Projected Z direction (does not apply when CSys is Local)

10 = Gravity direction (only applies when CSys is Global)

11 = Projected Gravity direction (only applies when CSys is Global)

The positive gravity direction (see Dir = 10 and 11) is in the negative Global Z direction.

Dist1

This is the distance from the I-End of the frame object to the start of the distributed load. This may be a relative distance (0 <= Dist1 <= 1) or an actual distance, depending on the value of the RelDist item. [L] when RelDist is False

Dist2

This is the distance from the I-End of the frame object to the end of the distributed load. This may be a relative distance (0 <= Dist2 <= 1) or an actual distance, depending on the value of the RelDist item. [L] when RelDist is False

Val1

This is the load value at the start of the distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2

Val2

This is the load value at the end of the distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2

CSys

This is Local or the name of a defined coordinate system. It is the coordinate system in which the loads are specified.

RelDist

If this item is True, the specified Dist item is a relative distance, otherwise it is an actual distance.

Replace

If this item is True, all previous distributed loads, if any, assigned to the specified frame object(s), in the specified load pattern, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function assigns distributed loads to frame objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameDistributedLoad()
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

   'assign frame distributed loads
      ret = SapModel.FrameObj.SetLoadDistributed("15", "DEAD", 1, 10, 0, 1, 0.08, 0.08)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDistributed](GetLoadDistributed_{Frame_Object}.htm)

[DeleteLoadDistributed](DeleteLoadDistributed_{Frame_Object}.htm)



## SetLoadGravity {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLoadGravity_{Frame_Object}.htm`*

# SetLoadGravity

## Syntax

SapObject.SapModel.FrameObj.SetLoadGravity

## VB6 Procedure

Function SetLoadGravity(ByVal Name As String, ByVal LoadPat As String, ByVal x As Double, ByVal y As Double, ByVal z As Double, Optional ByVal Replace As Boolean = True, Optional ByVal CSys As String = "Global", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

x, y, z

These are the gravity load multipliers in the x, y and z directions of the specified coordinate system.

Replace

If this item is True, all previous gravity loads, if any, assigned to the specified frame object(s), in the specified load pattern, are deleted before making the new assignment.

CSys

The coordinate system in which the x, y and z multipliers are specified.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function assigns gravity load multipliers to frame objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameGravityLoad()
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

   'assign frame gravity loads
      ret = SapModel.FrameObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Frame_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Frame_Object}.htm)



## SetLoadPoint

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLoadPoint.htm`*

# SetLoadPoint

## Syntax

SapObject.SapModel.FrameObj.SetLoadPoint

## VB6 Procedure

Function SetLoadPoint(ByVal Name As String, ByVal LoadPat
As String, ByVal MyType As Long, ByVal Dir As Long, ByVal Dist As Double,
ByVal Val As Double, Optional ByVal CSys As String = "Global",
Optional ByVal RelDist As Boolean = True, Optional ByVal Replace As Boolean
= True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending
on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

MyType

This is 1 or 2, indicating the type of point load.

1 = Force

2 = Moment

Dir

This is an integer between 1 and 11, indicating the
direction of the load.

1 = Local 1 axis (only
applies when CSys is Local)

2 = Local 2 axis (only
applies when CSys is Local)

3 = Local 3 axis (only
applies when CSys is Local)

4 = X direction (does
not apply when CSys is Local)

5 = Y direction (does
not apply when CSys is Local)

6 = Z direction (does
not apply when CSys is Local)

7 = Not Used - Projected
X direction (does not apply when CSys is Local)

8 = Not Used - Projected
Y direction (does not apply when CSys is Local)

9 = Not Used - Projected
Z direction (does not apply when CSys is Local)

10 = Gravity direction
(only applies when CSys is Global)

11 = Not Used - Projected
Gravity direction (only applies when CSys is Global)

The positive gravity direction (see Dir = 10 and 11)
is in the negative Global Z direction.

Dist

This is the distance from the I-End of the frame object
to the load location. This may be a relative distance (0 <= Dist <=
1) or an actual distance, depending on the value of the RelDist item.
[L] when RelDist is False

Val

This is the value of the point load. [F] when MyType
is 1 and [FL] when MyType is 2

CSys

This is Local or the name of a defined coordinate system.
It is the coordinate system in which the loads are specified.

RelDist

If this item is True, the specified Dist item is a relative
distance, otherwise it is an actual distance.

Replace

If this item is True, all previous loads, if any, assigned
to the specified frame object(s), in the specified load pattern, are deleted
before making the new assignment.

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

This function assigns point loads to frame objects.

The function returns zero if the loads are successfully
assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFramePointLoad()
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
3, 124, 3, 200)

   'assign frame point loads
      ret = SapModel.FrameObj.SetLoadPoint("15",
"DEAD", 1, 10, .5, 20)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases
and Response Combinations to Load Patterns, Load Cases and Load Combinations,
respectively, in version 12.00.

Changed descriptions for Dir 7, 8, 9 and 11 to "Not
Used" in version 25.0.0

## See Also

[GetLoadPoint](GetLoadPoint_{Frame_Object}.htm)

[DeleteLoadPoint](DeleteLoadPoint.htm)



## SetLoadPointWithGUID {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLoadPointWithGUID_{Frame_Object}.htm`*

# SetLoadPointWithGUID {Frame Object}

## Syntax

SapObject.SapModel.FrameObj.SetLoadPointWithGUID

## VB6 Procedure

Function SetLoadPointWithGUID(ByVal Name As String, ByVal LoadPat As String, ByVal MyType As Integer, ByVal dir As Integer, ByVal dist As Double, ByVal val As Double, ByRef GUID As String, Optional ByVal csys As String = "Global", Optional ByVal RelDist As Boolean = True, Optional ByVal Replace As Boolean = True) As Long

## Parameters

Name

The name of an existing frame object.

LoadPat

The name of a defined load pattern.

MyType

This is 1 or 2, indicating the type of point load.

1 = Force

2 = Moment

Dir

This is an integer between 1 and 11, indicating the direction of the load.

1 = Local 1 axis (only applies when CSys is Local)

2 = Local 2 axis (only applies when CSys is Local)

3 = Local 3 axis (only applies when CSys is Local)

4 = X direction (does not apply when CSys is Local)

5 = Y direction (does not apply when CSys is Local)

6 = Z direction (does not apply when CSys is Local)

7 = Projected X direction (does not apply when CSys is Local)

8 = Projected Y direction (does not apply when CSys is Local)

9 = Projected Z direction (does not apply when CSys is Local)

10 = Gravity direction (only applies when CSys is Global)

11 = Projected Gravity direction (only applies when CSys is Global)

The positive gravity direction (see Dir = 10 and 11) is in the negative Global Z direction.

Dist

This is the distance from the I-End of the frame object to the load location. This may be a relative distance (0 <= Dist <= 1) or an actual distance, depending on the value of the RelDist item. [L] when RelDist is False

Val

This is the value of the point load. [F] when MyType is 1 and [FL] when MyType is 2

GUID

This is the global unique ID of a point load assigned to the frame object or if it is not the global unique id of a point load assigned to the frame object and it is not blank, the global unique ID which is assigned to the newly assigned load. If left blank, a new load is assigned to the frame object and the value of this parameter is set to the global unique ID of the newly assigned load

CSys

This is Local or the name of a defined coordinate system. It is the coordinate system in which the loads are specified.

RelDist

If this item is True, the specified Dist item is a relative distance, otherwise it is an actual distance.

Replace

If this item is True and the input GUID is not the GUID of any point load assigned to the frame object, all previous point loads, if any, assigned to the specified frame object, in the specified load pattern, are deleted before making the new assignment. If the input GUID is the GUID of a point load already assigned to the frame object, the parameters of the point load are updated with the values provided and this item is ignored.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## Remarks

This function assigns point loads to frame objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## Release Notes

Initial release in version 17.2.0.

## See Also

[GetLoadPointWithGUID](GetLoadPoint_{Frame_Object}.htm)

[DeleteLoadPointWithGUID](DeleteLoadPointWithGUID_{Frame_Object}.htm)



## SetLoadStrain {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLoadStrain_{Frame_Object}.htm`*

# SetLoadStrain

## Syntax

SapObject.SapModel.FrameObj.SetLoadStrain

## VB6 Procedure

Function SetLoadStrain(ByVal Name As String, ByVal LoadPat As String, ByVal DOF As Long, ByVal Val As Double, Optional ByVal Replace As Boolean = True, Optional ByVal PatternName As String = "", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

DOF

This is 1, 2, 3, 4, 5 or 6, indicating the degree of freedom to which the strain load is applied.

1 = Strain11

2 = Strain12

3 = Strain13

4 = Curvature1

5 = Curvature2

6 = Curvature3

Val

This is the strain load value. [L/L] for DOF = 1, 2 and 3 and [1/L] for DOF = 4, 5 and 6

Replace

If this item is True, all previous strain loads, if any, assigned to the specified frame object(s), in the specified load pattern, for the specified degree of freedom, are deleted before making the new assignment.

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the strain load for the frame object is uniform along the object at the value specified by Val.

If PatternName is the name of a defined joint pattern, the strain load for the frame object is based on the specified strain value multiplied by the pattern value at the joints at each end of the frame object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function assigns strain loads to frame objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameStrainLoad()
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

   'assign frame strain load
      ret = SapModel.FrameObj.SetLoadStrain("1", "DEAD", 1, 0.001)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadStrain](GetLoadStrain_{Frame_Object}.htm)

[DeleteLoadStrain](DeleteLoadStrain_{Frame_Object}.htm)



## SetLoadTargetForce {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLoadTargetForce_{Frame_Object}.htm`*

# SetLoadTargetForce

## Syntax

SapObject.SapModel.FrameObj.SetLoadTargetForce

## VB6 Procedure

Function SetLoadTargetForce(ByVal Name As String, ByVal LoadPat As String, ByRef DOF() As Boolean, ByRef f() As Double, ByRef RD() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

DOF

This is a array of boolean values indicating if the considered degree of freedom has a target force.

DOF(1) = P

DOF(2) = V2

DOF(3) = V3

DOF(4) = T

DOF(5) = M2

DOF(6) = M3

f

This is a array of target force values. The target forces specified for a given degree of freedom are applied only if the corresponding DOF item for that degree of freedom is True.

f(1) = P [F]

f(2) = V2 [F]

f(3) = V3 [F]

f(4) = T [FL]

f(5) = M2 [FL]

f(6) = M3 [FL]

RD

This is a array of relative distances along the frame objects where the target force values apply. The relative distances specified for a given degree of freedom are applicable only if the corresponding DOF item for that degree of freedom is True. The relative distance must be between 0 and 1, 0 <= RD <=1.

RD(1) = relative location for P target force

RD(2) = relative location for V2 target force

RD(3) = relative location for V3 target force

RD(4) = relative location for T target force

RD(5) = relative location for M2 target force

RD(6) = relative location for M3 target force

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function assigns target forces to frame objects.

The function returns zero if the target forces are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameTargetForce()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DOF() As Boolean
      Dim f() As double
      Dim RD() As double

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

   'assign frame target force
      ReDim DOF(5)
      ReDim f(5)
      ReDim RD(5)
      DOF(0) = True
      f(0) = 50
      RD(0) = 0.5
      ret = SapModel.FrameObj.SetLoadTargetForce("1", "DEAD", DOF, f, RD)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTargetForce](GetLoadTargetForce_{Frame_Object}.htm)

[DeleteLoadTargetForce](DeleteLoadTargetForce_{Frame_Object}.htm)



## SetLoadTemperature {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLoadTemperature_{Frame_Object}.htm`*

# SetLoadTemperature

## Syntax

SapObject.SapModel.FrameObj.SetLoadTemperature

## VB6 Procedure

Function SetLoadTemperature(ByVal Name As String, ByVal LoadPat As String, ByVal MyType As Long, ByVal Val As Double, Optional ByVal PatternName As String = "", Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

MyType

This is 1, 2 or 3, indicating the type of temperature load.

1 = Temperature

2 = Temperature gradient along local 2 axis

3 = Temperature gradient along local 3 axis

Val

This is the temperature change value. [T] for MyType = 1 and [T/L] for MyType = 2 and 3

PatternName

This is blank or the name of a defined joint pattern. If it is blank the temperature load for the frame object is uniform along the object at the value specified by Val.

If PatternName is the name of a defined joint pattern, the temperature load for the frame object is based on the specified temperature value multiplied by the pattern value at the joints at each end of the frame object.

Replace

If this item is True, all previous temperature loads, if any, assigned to the specified frame object(s), in the specified load case, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function assigns temperature loads to frame objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameTemperatureLoad()
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

   'assign frame temperature load
      ret = SapModel.FrameObj.SetLoadTemperature("All", "DEAD", 1, 50, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTemperature](GetLoadTemperature_{Frame_Object}.htm)

[DeleteLoadTemperature](DeleteLoadTemperature_{Frame_Object}.htm)



## SetLoadTransfer

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLoadTransfer.htm`*

# SetLoadTransfer

## Syntax

SapObject.SapModel.FrameObj.SetLoadTransfer

## VB6 Procedure

Function SetLoadTransfer(ByVal Name As String, ByVal Val As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Val

This boolean value indicates if load is allowed to be transferred from area objects to this frame object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function returns the load transfer option for frame objects.  It indicates whether the frame receives load from an area object when the area object is loaded with a load of type uniform to frame.

The function returns zero if the load transfer option is successfully returned, otherwise it returns a nonzero value.

## VBA Example

Sub GetLoadTransferOption()

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

'set the load transfer option to False for frame object 1

ret = SapModel.FrameObj.SetLoadTransfer("1", False)

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## Release Notes

## Initial release in version 16.0.0.

## See Also

## [GetLoadTransfer](GetLoadTransfer.htm)



## SetLocalAxesAdvanced Frame Object

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLocalAxesAdvanced_Frame_Object.htm`*

# SetLocalAxesAdvanced

## Syntax

SapObject.SapModel.FrameObj.SetLocalAxesAdvanced

## VB6 Procedure

Function SetLocalAxesAdvanced(ByVal Name As String, ByVal Active As Boolean, ByVal Plane2 As Long, ByVal PlVectOpt As Long, ByVal PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Active

This is True if advanced local axes exist.

Plane2

This is 12 or 13, indicating that the local plane determined by the plane reference vector is the 1-2 plane or the 1-3 plane. This item applies only when the Active item is True.

PlVectOpt

This is 1, 2, or 3, indicating the plane reference vector option. This item applies only when the Active item is True.

1 = Coordinate direction

2 = Two joints

3 = User vector

PlCSys

The coordinate system used to define the plane reference vector coordinate directions and the plane user vector. This item applies when the Active item is True and the PlVectOpt item is 1 or 3.

PlDir

This is an array dimensioned to 1 (2 integers), indicating the plane reference vector primary and secondary coordinate directions, PlDir(0) and PlDir(1) respectively, taken at the object center in the specified coordinate system and used to determine the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 1. Possible coordinate direction values are:

1 = +X      -1 = -X

2 = +Y      -2 = -Y

3 = +Z      -3 = -Z

4 = +CR     -4 = -CR

5 = +CA     -5 = -CA

6 = +CZ     -6 = -CZ

7 = +SR     -7 = -SR

8 = +SA     -8 = -SA

9 = +SB     -9 = -SB

PlPt

This is an array dimensioned to 1 (2 strings), indicating the labels of two joints that define the plane reference vector. Either of these joints may be specified as None to indicate the center of the specified object.  If both joints are specified as None, they are not used to define the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 2.

PlVect

This is an array dimensioned to 2 (3 doubles) that defines the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 3.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

Selection = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is Selection, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function assigns advanced local axes to frame objects.

The function returns zero if the advanced local axes assignments are assigned successfully; otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameAdvancedLocalAxes()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'assign frame advanced local axes
      MyPlDir(0) = 2
      MyPlDir(1) = 3
      ret = SapModel.FrameObj.SetLocalAxesAdvanced("3", True, 12, 1, "Global", MyPlDir, MyPlPt, MyPlVect)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

## See Also

[GetLocalAxesAdvanced](GetLocalAxesAdvanced_Frame_Object.htm)

[GetLocalAxes](GetLocalAxes_{Frame_Object}.htm)



## SetLocalAxes {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLocalAxes_{Frame_Object}.htm`*

# SetLocalAxes

## Syntax

SapObject.SapModel.FrameObj.SetLocalAxes

## VB6 Procedure

Function SetLocalAxes(ByVal Name As String, ByVal Ang As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Ang

This is the angle that the local 2 and 3 axes are rotated about the positive local 1 axis, from the default orientation or, if the Advanced item is True, from the orientation determined by the plane reference vector. The rotation for a positive angle appears counter clockwise when the local +1 axis is pointing toward you. [deg]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function assigns a local axis angle to frame objects.

The function returns zero if the local axis angle is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameLocalAxisAngle()
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

   'assign frame local axis angle
      ret = SapModel.FrameObj.SetLocalAxes("3", 30)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetLocalAxes](GetLocalAxes_{Frame_Object}.htm)



## SetMass {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetMass_{Frame_Object}.htm`*

# SetMass

## Syntax

SapObject.SapModel.FrameObj.SetMass

## VB6 Procedure

Function SetMass(ByVal Name As String, ByVal MassOverL As Double, Optional ByVal Replace As Boolean = False, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

MassOverL

The mass per unit length assigned to the frame object. [M/L]

Replace

If this item is True, all existing mass assignments to the frame object are removed before assigning the specified mas. If it is False, the specified mass is added to any existing mass already assigned to the frame object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function assigns mass per unit length to frame objects.

The function returns zero if the mass is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameMass()
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

   'assign frame mass
      ret = SapModel.FrameObj.SetMass("ALL", .0001, False, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMass](GetMass_{Frame_Object}.htm)

[DeleteMass](DeleteMass_{Frame_Object}.htm)



## SetMatTemp {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetMatTemp_{Frame_Object}.htm`*

# SetMatTemp

## Syntax

SapObject.SapModel.FrameObj.SetMatTemp

## VB6 Procedure

Function SetMatTemp(ByVal Name As String, ByVal Temp As Double, Optional ByVal PatternName As String = "", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Temp

This is the material temperature value assigned to the frame object. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the material temperature for the frame object is uniform along the object at the value specified by Temp.

If PatternName is the name of a defined joint pattern, the material temperature for the frame object may vary from one end to the other. The material temperature at each end of the object is equal to the specified temperature multiplied by the pattern value at the joint at the end of the frame object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function assigns material temperatures to frame objects.

The function returns zero if the material temperatures are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameMatTemp()
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

   'assign material temperature
      ret = SapModel.FrameObj.SetMatTemp("ALL", 50, , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMatTemp](GetMatTemp_{Frame_Object}.htm)



## SetMaterialOverwrite {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetMaterialOverwrite_{Frame_Object}.htm`*

# SetMaterialOverwrite

## Syntax

SapObject.SapModel.FrameObj.SetMaterialOverwrite

## VB6 Procedure

Function SetMaterialOverwrite(ByVal Name As String, ByVal PropName As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

PropName

This is None or a blank string, indicating that any existing material overwrites assigned to the specified frame objects are to be removed, or it is the name of an existing material property.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the material overwrite assignment for frame objects.

The function returns zero if the material overwrite assignment is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameMaterialOverwrite()
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

   'assign material overwrite
      ret = SapModel.FrameObj.SetMaterialOverwrite("3", "4000Psi")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMaterialOverwrite](GetMaterialOverwrite_{Frame_Object}.htm)



## SetModifiers {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetModifiers_{Frame_Object}.htm`*

# SetModifiers

## Syntax

SapObject.SapModel.FrameObj.SetModifiers

## VB6 Procedure

Function SetModifiers(ByVal Name As String, ByRef Value() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

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

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the frame modifier assignment for frame objects. The default value for all modifiers is one.

The function returns zero if the modifier assignments are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameModifiers()
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

   'assign modifiers
      ReDim Value(7)
      For i = 0 To 7
         Value(i) = 1
      Next i
      Value(5) = 100
      ret = SapModel.FrameObj.SetModifiers("3", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetModifiers](GetModifiers_{Frame_Object}.htm)

[DeleteModifiers](DeleteModifiers_{Frame_Object}.htm)



## SetNotionalSize

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetNotionalSize_1.htm`*

# SetNotionalSize

## Syntax

SapObject.SapModel.PropFrame.SetNotionalSize

## VB6 Procedure

Function SetNotionalSize(ByVal Name As String, ByVal stype As String, ByVal Value As Double) As Long

## Parameters

Name

The name of an existing frame section property.

stype

The type to define the notional size of a section. It can be:

"Auto" = Program will determine the notional size based on the average thickness of an area element.

"User" = The notional size is based on the user-defined value.

"None" = Notional size will not be considered. In other words, the time-dependent effect of this section will not be considered.

Value

For stype is "Auto", the Value represents for the scale factor to the program-determined notional size; for **stype** is “User”, the **Value** represents for the user-defined notional size [L]; for **stype** is “None”, the **Value** will not be used and can be set to 1.

## Remarks

This function assigns the method to determine the notional size of a frame section for the creep and shrinkage calculations. This function is currently worked for the steel/aluminum sections - I/Wide Flange, Channel, Tee, Angle, Double Angle, Double Channel, Pipe and Tube sections, and all the concrete sections - Rectangular, Circular, Pipe, Tube, Precast I.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignFramePropNotionalSize()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long

 Dim stype As String

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
   ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

'assign parameters
   stype = “Auto”
   Value = 1.1
   ret = SapModel.PropFrame.SetNotionalSize("FSEC1", stype, Value)

'close Sap2000
   SapObject.ApplicationExit False
   Set SapModel = Nothing
   Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.1.0

## See Also

[GetNotionalSize](GetNotionalSize_1.htm)



## SetOutputStations {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetOutputStations_{Frame_Object}.htm`*

# SetOutputStations

## Syntax

SapObject.SapModel.FrameObj.SetOutputStations

## VB6 Procedure

Function SetOutputStations(ByVal Name As String, ByVal MyType As Long, ByVal MaxSegSize As Double, ByVal MinSections As Long, Optional ByVal NoOutPutAndDesignAtElementEnds As Boolean = False, Optional ByVal NoOutPutAndDesignAtPointLoads As Boolean = False, Optional ByVal ItemType As eItemType = eItemType\_Objects) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

MyType

This is 1 or 2, indicating how the output stations are specified.

1 = maximum segment size, that is, maximum station spacing

2 = minimum number of stations

MaxSegSize

The maximum segment size, that is, the maximum station spacing. This item applies only when MyType = 1. [L]

MinSections

The minimum number of stations. This item applies only when MyType = 2.

NoOutPutAndDesignAtElementEnds

If this item is True, no additional output stations are added at the ends of line elements when the frame object is internally meshed.

NoOutPutAndDesignAtPointLoads

If this item is True, no additional output stations are added at point load locations.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function assigns frame object output station data.

The function returns zero if the data is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameOutputStationData()
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

   'assign frame output station data
      ret = SapModel.FrameObj.SetOutputStations("15", 1, 18, 0)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetOutputStations](GetOutputStations_{Frame_Object}.htm)



## SetPDeltaForce

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetPDeltaForce.htm`*

# SetPDeltaForce

## Syntax

SapObject.SapModel.FrameObj.SetPDeltaForce

## VB6 Procedure

Function SetPDeltaForce(ByVal Name As String, ByVal PDeltaForce As Double, ByVal Dir As Long, ByVal Replace As Boolean, Optional ByVal CSys As String = "Global", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

PDeltaForce

The P-Delta force assigned to the frame object. [F]

Dir

This is 0, 1, 2 or 3, indicating the direction of the P-Delta force assignment.

0 = Frame object local 1-axis direction

1 = Projected X direction in CSys coordinate system

2 = Projected Y direction in CSys coordinate system

3 = Projected Z direction in CSys coordinate system

Replace

If this item is True, all existing P-Delta force assignments to the frame object are removed before assigning the specified P-Delta force. If it is False, the specified P-Delta force is added to any existing P-Delta forces already assigned to the frame object.

CSys

This is the name of the coordinate system in which the projected X, Y or Z direction P-Delta forces are defined. This item does not apply if the Dir item is zero (frame object local 1-axis direction).

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function assigns P-Delta forces to straight frame objects. P-Delta force assignments do not apply to curved frames.

The function returns zero if the assignments are successfully applied, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFramePDeltaForce()
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

   'assign P-Delta force
      ret = SapModel.FrameObj.SetPDeltaForce("ALL", 100, 0, True, , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetPDeltaForce](GetPDeltaForce_{Frame_Object}.htm)

[DeletePDeltaForce](DeletePDeltaForce.htm)



## SetReleases {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetReleases_{Frame_Object}.htm`*

# SetReleases

## Syntax

SapObject.SapModel.FrameObj.SetReleases

## VB6 Procedure

Function SetReleases(ByVal Name As String, ByRef ii() As Boolean, ByRef jj() As Boolean, ByRef StartValue() As Double, ByRef EndValue() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

ii, jj

These are arrays of six booleans indicating the I-End and J-End releases for the frame object.

ii(0) and jj(0) = U1 release

ii(1) and jj(1) = U2 release

ii(2) and jj(2) = U3 release

ii(3) and jj(3) = R1 release

ii(4) and jj(4) = R2 release

ii(5) and jj(5) = R3 release

StartValue, EndValue

These are arrays of six values indicating the I-End and J-End partial fixity springs for the frame object.

StartValue(0) and EndValue(0) = U1 partial fixity [F/L]

StartValue(1) and EndValue(1) = U2 partial fixity [F/L]

StartValue(2) and EndValue(2) = U3 partial fixity [F/L]

StartValue(3) and EndValue(3) = R1 partial fixity [FL/rad]

StartValue(4) and EndValue(4) = R2 partial fixity [FL/rad]

StartValue(5) and EndValue(5) = R3 partial fixity [FL/rad]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function makes end release and partial fixity assignments to frame objects.

The function returns zero if the assignments are successfully retrieved, otherwise it returns a nonzero value.

Partial fixity assignments are made to degrees of freedom that have been released only.

Some release assignments would cause instability in the model. An error is returned if this type of assignment is made. Unstable release assignments include the following:

U1 released at both ends

U2 released at both ends

U3 released at both ends

R1 released at both ends

R2 released at both ends and U3 at either end

R3 released at both ends and U2 at either end

## VBA Example

Sub SetFrameEndReleases()
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

   'assign end releases
      ReDim ii(5)
      ReDim jj(5)
      ReDim StartValue(5)
      ReDim EndValue(5)
      ii(5) = True
      jj(5) = True
      ret = SapModel.FrameObj.SetReleases("13", ii, jj, StartValue, EndValue)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetReleases](GetReleases_{Frame_Object}.htm)



## SetSection

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetSection.htm`*

# SetSection

## Syntax

SapObject.SapModel.FrameObj.SetSection

## VB6 Procedure

Function SetSection(ByVal name As String, ByVal PropName As String, Optional ByVal ItemType As eItemType = object, Optional ByVal sVarRelStartLoc As Double = 0, Optional ByVal sVarTotalLength As Double = 0) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

PropName

This is None or the name of a frame section property to be assigned to the specified frame object(s).

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

sVarTotalLength

This is the total assumed length of the nonprismatic section. Enter 0 for this item to indicate that the section length is the same as the frame object length.

This item is applicable only when the assigned frame section property is a nonprismatic section.

sVarRelStartLoc

This is the relative distance along the nonprismatic section to the I-End (start) of the frame object. This item is ignored when the sVarTotalLengthitem is 0.

This item is applicable only when the assigned frame section property is a nonprismatic section, and the sVarTotalLengthitem is greater than zero.

## Remarks

This function assigns a frame section property to a frame object.

The function returns zero if the frame section property data is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub SetFrameSectionProp()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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
      FileName = "C:\SapAPI\Example 1-022.sdb"
      ret = SapModel.File.OpenFile(FileName)

   'unlock model
      ret = SapModel.SetModelIsLocked(False)

   'set frame section property
      ret = SapModel.FrameObj.SetSection("28", "W24X160")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSection](GetSection_{Frame_Object}.htm)

[GetSectionNonPrismatic](GetSectionNonPrismatic.htm)



## SetSelected {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetSelected_{Frame_Object}.htm`*

# SetSelected

## Syntax

Sap2000.FrameObj.SetSelected

## VB6 Procedure

Function SetSelected(ByVal Name As String, ByVal Selected As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Selected

This item is True if the specified frame object is selected, otherwise it is False.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the selected status is set for the frame object specified by the Name item.

If this item is Group, the selected status is set for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the selected status is set for all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the selected status for a frame object.

The function returns zero if the selected status is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetFrameObjectSelected()
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

   'set frame object selected
      ret = SapModel.FrameObj.SetSelected("8", True)

   'update view
      ret = SapModel.View.RefreshView

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSelected](GetSelected_{Frame_Object}.htm)



## SetSpring {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetSpring__{Frame_Object}.htm`*

# SetSpring

## Syntax

SapObject.SapModel.FrameObj.SetSpring

## VB6 Procedure

Function SetSpring(ByVal Name As String, ByVal MyType As Long, ByVal s As Double, ByVal SimpleSpringType As Long, ByVal LinkProp As String, ByVal SpringLocalOneType As Long, ByVal Dir As Long, ByVal Plane23Angle As Double, ByRef Vec() As Double, ByVal Ang As Double, ByVal Replace As Boolean, Optional ByVal CSys As String = "Local", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

MyType

This is 1 or 2, indicating the spring property type.

1 = Simple spring

2 = Link property

s

The simple spring stiffness per unit length of the frame object. This item applies only when MyType = 1. [F/L2]

SimpleSpringType

This is 1, 2 or 3, indicating the simple spring type. This item applies only when MyType = 1.

1 = Spring resists tension and compression

2 = Spring resists compression only

3 = Spring resists tension only

LinkProp

The name of the link property assigned to the spring. This item applies only when MyType = 2.

SpringLocalOneType

This is 1, 2 or 3, indicating the method used to specify the spring positive local 1-axis orientation.

1 = Parallel to frame object local axis

2 = In the frame object 2-3 plane

3 = User specified direction vector

Dir

This is 1, 2, 3, -1, -2 or -3, indicating the frame object local axis that corresponds to the positive local 1-axis of the spring. This item applies only when SpringLocalOneType = 1.

Plane23Angle

This is the angle in the frame object 2-3 plane measured counter clockwise from the frame positive 2-axis to the spring positive 1-axis. This item applies only when SpringLocalOneType = 2. [deg]

Vec

This is an array of three values that define the direction vector of the spring positive local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when SpringLocalOneType = 3.

Ang

This is the angle that the link local 2-axis is rotated from its default orientation. This item applies only when MyType = 2. [deg]

Replace

If this item is True, all existing spring assignments to the frame object are removed before assigning the specified spring. If it is False, the specified spring is added to any existing springs already assigned to the frame object.

CSys

This is Local (meaning the frame object local coordinate system) or the name of a defined coordinate system. This item is the coordinate system in which the user specified direction vector, Vec, is specified. This item applies only when SpringLocalOneType = 3.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function makes spring assignments to frame objects.

The function returns zero if the assignments are successfully applied, otherwise it returns a nonzero value.

## VBA Example

Sub AssignFrameSprings()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Vec() As Double

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

   'assign springs to frame
      ReDim Vec(2)
      ret = SapModel.FrameObj.SetSpring("ALL", 1, 1, 1, "", 1, 2, 0, Vec, 0, False, "Local", Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Frame_Object}.htm)

[DeleteSpring](DeleteSpring_{Frame_Object}.htm)



## SetStraight

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetStraight.htm`*

# SetStraight

## Syntax

SapObject.SapModel.FrameObj.SetStraight

## VB6 Procedure

Function SetStraight(ByVal Name As String) As Long

## Parameters

Name

The name of a defined curved frame object.

## Remarks

This function sets a curved frame object straight.

The function returns zero if the frame object type is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetFrameStraight()
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

   'set frame curved
      ret = SapModel.FrameObj.SetCurved("15", 2, -200, 0, 300, "", 0, 16)

   'set frame straight
      ret = SapModel.FrameObj.SetStraight("15")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetCurved](SetCurved.htm)

[GetCurved](../../Obsolete_Functions/GetCurved.htm)

[GetType](GetType_{Frame_Object}.htm)



## SetTCLimits {Frame Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetTCLimits_{Frame_Object}htm.htm`*

# SetTCLimits

## Syntax

SapObject.SapModel.FrameObj.SetTCLimits

## VB6 Procedure

Function SetTCLimits(ByVal Name As String, ByVal LimitCompressionExists As Boolean, ByVal LimitCompression As Double, ByVal LimitTensionExists As Boolean, ByVal LimitTension As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

LimitCompressionExists

This item is True if a compression force limit exists for the frame object.

LimitCompression

The compression force limit for the frame object. [F]

LimitTensionExists

This item is True if a tension force limit exists for the frame object.

LimitTension

The tension force limit for the frame object. [F]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function makes tension/compression force limit assignments to frame objects.

The function returns zero if the assignments are successfully applied, otherwise it returns a nonzero value.

Note that the tension and compression limits are only used in nonlinear analyses.

## VBA Example

Sub AssignFrameTCLimits()
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

   'assign tension/compression limits
      ret = SapModel.FrameObj.SetTCLimits("1", False, 0, True, 100)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetTCLimits](GetTCLimits{Frame_Object}.htm)



## SetTrapezoidal

*Source file: `SAP2000_API_Fuctions/Object_Model/Frame_Object/SetTrapezoidal.htm`*

# SetTrapezoidal

## Syntax

SapObject.SapModel.PropFrame.SetTrapezoidal

## VB6 Procedure

Function SetTrapezoidal(ByVal Name As String, ByVal MatProp As String, ByVal t3 As Double, ByVal t2 As Double, ByVal t2b As Double, Optional ByVal Color As Long = -1, Optional ByVal Notes As String = "", Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing or new frame section property. If this is an existing property, that property is modified; otherwise, a new property is added.

MatProp

The name of the material property for the section.

t3

The section depth. [L]

t2

The section top width. [L]

t2b

The section bottom width. [L]

Color

The display color assigned to the section. If Color is specified as -1, the program will automatically assign a color.

Notes

The notes, if any, assigned to the section.

GUID

The GUID (global unique identifier), if any, assigned to the section. If this item is input as Default, the program assigns a GUID to the section.

## Remarks

This function initializes a solid trapezoidal frame section property. If this function is called for an existing frame section property, all items for the section are reset to their default value.

The function returns zero if the section property is successfully initialized; otherwise it returns a nonzero value.

## VBA Example

Sub SetFramePropTrapezoidal()

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

  'set new frame section property
      ret = SapModel.PropFrame.SetTrapezoidal("R1", "4000Psi", 20, 20, 12)

  'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 17.2.0

## See Also

GetTrapezoidal

SetRebarBeam

SetRebarColumn

GetRebarBeam

GetRebarColumn

