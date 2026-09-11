# API Object Model Solid Object

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Object_Model/Solid_Object

---



## AddByCoord {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/AddByCoord_{Solid_Object}.htm`*

# AddByCoord

## Syntax

SapObject.SapModel.SolidObj.AddByCoord

## VB6 Procedure

Function AddByCoord(ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, ByRef Name As String, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "", Optional ByVal CSys As String = "Global") As Long

## Parameters

x, y, z

These are arrays of x, y and z coordinates, respectively, for the corner points of the solid object. The coordinates are in the coordinate system defined by the CSys item.

Name

This is the name that the program ultimately assigns for the solid object. If no UserName is specified, the program assigns a default name to the solid object. If a UserName is specified and that name is not used for another solid object, the UserName is assigned to the solid object; otherwise a default name is assigned to the solid object.

PropName

This is either Default or the name of a defined solid property.

If it is Default, the program assigns a default solid property to the solid object. If it is the name of a defined solid property, that property is assigned to the solid object.

UserName

This is an optional user specified name for the solid object. If a UserName is specified and that name is already used for another solid object, the program ignores the UserName.

CSys

The name of the coordinate system in which the solid object point coordinates are defined.

## Remarks

This function adds a new solid object whose corner points are at the specified coordinates. Note that solid objects always are defined with eight corner points.

The function returns zero if the solid object is successfully added; otherwise it returns a nonzero value.

## VBA Example

Sub AddSolidObjByCoord()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim x() As Double
      Dim y() As Double
      Dim z() As Double
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
      ret = SapModel.File.NewBlank

   'add solid object by coordinates
      ReDim x(7)
      ReDim y(7)
      ReDim z(7)
      x(0) = 0:    y(0) = 0:    z(0) = 0
      x(1) = 100:  y(1) = 0:    z(1) = 0
      x(2) = 0:    y(2) = 100:  z(2) = 0
      x(3) = 100:  y(3) = 100:  z(3) = 0
      x(4) = 0:    y(4) = 0:    z(4) = 100
      x(5) = 100:  y(5) = 0:    z(5) = 100
      x(6) = 0:    y(6) = 100:  z(6) = 100
      x(7) = 100:  y(7) = 100:  z(7) = 100
      ret = SapModel.SolidObj.AddByCoord(x, y, z, Name)

   'refresh view
      ret = SapModel.View.RefreshView(0, False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByPoint](AddByPoint_{Solid_Object}.htm)



## AddByPoint {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/AddByPoint_{Solid_Object}.htm`*

# AddByPoint

## Syntax

SapObject.SapModel.SolidObj.AddByPoint

## VB6 Procedure

Function AddByPoint(ByRef Point() as String, ByRef Name As String, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "") As Long

## Parameters

Point

This is an array containing the names of the eight point objects that define the corner points of the added solid object.

Name

This is the name that the program ultimately assigns for the solid object. If no UserName is specified, the program assigns a default name to the solid object. If a UserName is specified and that name is not used for another solid object, the UserName is assigned to the solid object; otherwise a default name is assigned to the solid object.

PropName

This is either Default or the name of a defined solid property.

If it is Default, the program assigns a default solid property to the solid object. If it is the name of a defined solid property, that property is assigned to the solid object.

UserName

This is an optional user specified name for the solid object. If a UserName is specified and that name is already used for another solid object, the program ignores the UserName.

## Remarks

This function adds a new solid object whose corner points are specified by name.

The function returns zero if the solid object is successfully added; otherwise it returns a nonzero value.

## VBA Example

Sub AddSolidObjByPoint()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Point() As String
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
      ret = SapModel.File.New3DFrame(Openframe, 2, 144, 3, 288, 2, 288)

   'add solid object by points
      Redim Point(7)
      Point(0) = "1"
      Point(1) = "10"
      Point(2) = "4"
      Point(3) = "13"
      Point(4) = "2"
      Point(5) = "11"
      Point(6) = "5"
      Point(7) = "14"
      ret = SapModel.SolidObj.AddByPoint(Point, Name)

   'refresh view
      ret = SapModel.View.RefreshView(0, False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Solid_Object}.htm)



## ChangeName {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/ChangeName_{Solid_Object}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.SolidObj.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a defined solid object.

NewName

The new name for the solid object.

## Remarks

This function applies a new name to a solid object.

The function returns zero if the new name is successfully applied; otherwise it returns a nonzero value.

## VBA Example

Sub ChangeSolidObjName()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'change name
      ret = SapModel.SolidObj.ChangeName("1", "MySolid")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## Count {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/Count_{Solid_Object}.htm`*

# Count

## Syntax

SapObject.SapModel.SolidObj.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None

## Remarks

This function returns a count of the solid objects in the model.

## VBA Example

Sub CountSolidObjects()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'return number of solid objects
      Count = SapModel.SolidObj.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## DeleteLoadGravity {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/DeleteLoadGravity_{Solid_Object}.htm`*

# DeleteLoadGravity

## Syntax

SapObject.SapModel.SolidObj.DeleteLoadGravity

## VB6 Procedure

Function DeleteLoadGravity(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the solid object specified by the Name item.

If this item is Group, the load assignments are deleted for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected solid objects, and the Name item is ignored.

## Remarks

This function deletes the gravity load assignments to the specified solid objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteSolidObjectGravityLoad()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object gravity loads
      ret = SapModel.SolidObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'delete solid object gravity load
      ret = SapModel.SolidObj.DeleteLoadGravity("1", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Solid_Object}.htm)

[SetLoadGravity](SetLoadGravity_{Solid_Object}.htm)



## DeleteLoadPorePressure {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/DeleteLoadPorePressure_{Solid_Object}.htm`*

# DeleteLoadPorePressure

## Syntax

SapObject.SapModel.SolidObj.DeleteLoadPorePressure

## VB6 Procedure

Function DeleteLoadPorePressure(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the solid object specified by the Name item.

If this item is Group, the load assignments are deleted for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected solid objects, and the Name item is ignored.

## Remarks

This function deletes the pore pressure load assignments to the specified solid objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteSolidObjectPorePressureLoad()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object pore pressure load
      ret = SapModel.SolidObj.SetLoadPorePressure("ALL", "DEAD", .1, , , Group)

   'delete solid object pore pressure load
      ret = SapModel.SolidObj.DeleteLoadPorePressure("1", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadPorePressure](GetLoadPorePressure_{Solid_Object}.htm)

[SetLoadPorePressure](SetLoadPorePressure_{Solid_Object}.htm)



## DeleteLoadStrain {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/DeleteLoadStrain_{Solid_Object}.htm`*

# DeleteLoadStrain

## Syntax

SapObject.SapModel.SolidObj.DeleteLoadStrain

## VB6 Procedure

Function DeleteLoadStrain(ByVal Name As String, ByVal LoadPat As String, ByVal Component As Long, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Component

This is 1, 2, 3, 4, 5 or 6, indicating the component for which the strain load is to be deleted.

1 = Strain11

2 = Strain22

3 = Strain33

4 = Strain12

5 = Strain13

6 = Strain23

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the solid object specified by the Name item.

If this item is Group, the load assignments are deleted for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected solid objects, and the Name item is ignored.

## Remarks

This function deletes the strain load assignments to the specified solid objects, for the specified load pattern, for the specified components.

The function returns zero if the load assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteSolidObjectStrainLoad()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object strain load
      ret = SapModel.SolidObj.SetLoadStrain("ALL", "DEAD", 1, 0.001, , , Group)

   'delete solid object strain load
      ret = SapModel.SolidObj.DeleteLoadStrain("1", "DEAD", 1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadStrain](GetLoadStrain_{Solid_Object}.htm)

[SetLoadStrain](SetLoadStrain_{Solid_Object}.htm)



## DeleteLoadSurfacePressure {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/DeleteLoadSurfacePressure_{Solid_Object}.htm`*

# DeleteLoadSurfacePressure

## Syntax

SapObject.SapModel.SolidObj.DeleteLoadSurfacePressure

## VB6 Procedure

Function DeleteLoadSurfacePressure(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the solid object specified by the Name item.

If this item is Group, the load assignments are deleted for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected solid objects, and the Name item is ignored.

## Remarks

This function deletes the surface pressure load assignments to the specified solid objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteSolidObjectSurfacePressureLoad()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object surface pressure load
      ret = SapModel.SolidObj.SetLoadSurfacePressure("ALL", "DEAD", 1, .1, , , Group)

   'delete solid object surface pressure load
      ret = SapModel.SolidObj.DeleteLoadSurfacePressure("1", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadSurfacePressure](GetLoadSurfacePressure_{Solid_Object}.htm)

[SetLoadSurfacePressure](SetLoadSurfacePressure_{Solid_Object}.htm)



## DeleteLoadTemperature {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/DeleteLoadTemperature_{Solid_Object}.htm`*

# DeleteLoadTemperature

## Syntax

SapObject.SapModel.SolidObj.DeleteLoadTemperature

## VB6 Procedure

Function DeleteLoadTemperature(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the solid object specified by the Name item.

If this item is Group, the load assignments are deleted for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected solid objects, and the Name item is ignored.

## Remarks

This function deletes the temperature load assignments to the specified solid objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteSolidObjectTemperatureLoad()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object temperature load
      ret = SapModel.SolidObj.SetLoadTemperature("All", "DEAD", 50, , , Group)

   'delete solid object temperature load
      ret = SapModel.SolidObj.DeleteLoadTemperature("1", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTemperature](GetLoadTemperature_{Solid_Object}.htm)

[SetLoadTemperature](SetLoadTemperature_{Solid_Object}.htm)



## DeleteSpring {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/DeleteSpring_{Solid_Object}.htm`*

# DeleteSpring

## Syntax

SapObject.SapModel.SolidObj.DeleteSpring

## VB6 Procedure

Function DeleteSpring(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the spring assignments are deleted for the solid object specified by the Name item.

If this item is Group, the spring assignments are deleted for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, the spring assignments are deleted for all selected solid objects, and the Name item is ignored.

## Remarks

This function deletes all spring assignments for the specified solid objects.

The function returns zero if the assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteSolidObjectSprings()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign springs to solid objects
      ReDim Vec(2)
      ret = SapModel.SolidObj.SetSpring("1", 1, 1, 1, "", 1, 1, 3, True, Vec, 0, False, "Local")
      ret = SapModel.SolidObj.SetSpring("5", 1, 1, 1, "", 1, 1, 3, True, Vec, 0, False, "Local")

   'delete springs
      ret = SapModel.SolidObj.DeleteSpring("1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Solid_Object}.htm)

[SetSpring](SetSpring_{Solid_Object}.htm)



## Delete {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/Delete_{Solid_Object}.htm`*

# Delete

## Syntax

SapObject.SapModel.SolidObj.Delete

## VB6 Procedure

Function Delete(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the solid object specified by the Name item is deleted.

If this item is Group, the all solid objects in the group specified by the Name item are deleted.

If this item is SelectedObjects, all selected solid objects are deleted, and the Name item is ignored.

## Remarks

The function deletes solid objects.

The function returns zero if the solid objects are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteSolidObj()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'delete solid object
      ret = SapModel.SolidObj.Delete("2")

   'update view
      ret = SapModel.View.RefreshView(0, True)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Solid_Object}.htm)

[AddByPoint](AddByPoint_{Solid_Object}.htm)



## GetAutoMesh {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetAutoMesh_{Solid_Object}.htm`*

# GetAutoMesh

## Syntax

SapObject.SapModel.SolidObj.GetAutoMesh

## VB6 Procedure

Function GetAutoMesh(ByVal Name As String, ByRef MeshType As Long, ByRef n1 As Long, ByRef n2 As Long, ByRef MaxSize1 As Double, ByRef MaxSize2 As Double, ByRef RestraintsOnEdge As Boolean, ByRef RestraintsOnFace As Boolean) As Long

## Parameters

Name

The name of an existing solid object.

MeshType

This item is 0, 1 or 2, indicating the automatic mesh type for the solid object.

0 = No automatic meshing

1 = Mesh solid into a specified number of objects

2 = Mesh solid into objects of a specified maximum size

n1

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed solid object that runs from point 1 to point 2.

n2

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed solid object that runs from point 1 to point 3.

n3

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed solid object that runs from point 1 to point 5.

MaxSize1

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed solid object that runs from point 1 to point 2. [L]

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

MaxSize2

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed solid object that runs from point 1 to point 3. [L]

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

MaxSize3

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed solid object that runs from point 1 to point 5. [L]

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

RestraintsOnEdge

If this item is True, and if both points along an edge of the original solid object have the same restraint/constraint, then, if the an added point on that edge and the original corner points have the same local axes definition, the program assigns the restraint/constraint to the added point.

RestraintsOnFace

If this item is True, and if all corner points on an solid object face have the same restraint/constraint, then, if an added point on that face and the original corner points for the face have the same local axes definition, the program assigns the restraint/constraint to the added point.

## Remarks

This function retrieves the automatic meshing assignments to solid objects.

The function returns zero if the meshing assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjAutoMesh()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MeshType As Long
      Dim n1 As Long
      Dim n2 As Long
      Dim n3 As Long
      Dim MaxSize1 As Double
      Dim MaxSize2 As Double
      Dim MaxSize3 As Double
      Dim RestraintsOnEdge As Boolean
      Dim RestraintsOnFace As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign auto mesh options
      ret = SapModel.SolidObj.SetAutoMesh("ALL", 1, 3, 3,3, , , , , , Group)

   'get auto mesh options for solid object
      ret = SapModel.SolidObj.GetAutoMesh("1", MeshType, n1, n2, n3, MaxSize1, MaxSize2, MaxSize3, RestraintsOnEdge, RestraintsOnFace)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetAutoMesh](SetAutoMesh_{Solid_Object}.htm)



## GetEdgeConstraint {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetEdgeConstraint_{Solid_Object}.htm`*

# GetEdgeConstraint

## Syntax

SapObject.SapModel.SolidObj.GetEdgeConstraint

## VB6 Procedure

Function GetEdgeConstraint(ByVal Name As String, ByRef ConstraintExists As Boolean) As Long

## Parameters

Name

The name of an existing solid object.

ConstraintExists

This item is True if an automatic edge constraint is generated by the program for the solid object in the analysis model.

## Remarks

This function retrieves the generated edge constraint assignments to solid objects.

The function returns zero if the assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjEdgeConstraint()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim ConstraintExists As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign auto edge constraint option
      ret = SapModel.SolidObj.SetEdgeConstraint("ALL", True, Group)

   'get auto edge constraint option
      ret = SapModel.SolidObj.GetEdgeConstraint("1", ConstraintExists)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetEdgeConstraint](SetEdgeConstraint_{Solid_Object}.htm)



## GetElm {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetElm_{Solid_Object}.htm`*

# GetElm

## Syntax

SapObject.SapModel.SolidObj.GetElm

## VB6 Procedure

Function GetElm(ByVal Name As String, ByRef nelm As Long, ByRef Elm() as String) As Long

## Parameters

Name

The name of an existing solid object.

nelm

The number of solid elements created from the specified solid object.

Elm

An array that includes the name of a solid element created from the specified solid object.

## Remarks

This function retrieves the names of the solid elements (analysis model solid) associated with a specified solid object in the object-based model.

This function returns zero if the solid element information is successfully returned; otherwise it returns nonzero. An error occurs if the analysis model does not exist.

## VBA Example

Sub GetSolidElementInfoForSolidObject()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim nelm As Long
      Dim Elm() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'create the analysis model
      ret = SapModel.Analyze.CreateAnalysisModel

   'get solid element information
      ret = SapModel.SolidObj.GetElm("1", nelm, Elm)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetGUID {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetGUID_{Solid_Object}.htm`*

# GetGUID

## Syntax

SapObject.SapModel.SolidObj.GetGUID

## VB6 Procedure

Function GetGUID(ByVal name As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing solid object.

GUID

The GUID (Global Unique ID) for the specified solid object.

## Remarks

This function retrieves the GUID for the specified solid object.

This function returns zero if the solid object GUID is successfully retrieved; otherwise it returns nonzero.

## VBA Example

Sub GetSolidObjGUID()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'set program created GUID
      ret = SapObject.SapModel.SolidObj.SetGUID("1")

   'get GUID
      ret = SapObject.SapModel.SolidObj.GetGUID("1", GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetGUID](SetGUID_{Solid_Object}.htm)



## GetGroupAssign {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetGroupAssign_{Solid_Object}.htm`*

# GetGroupAssign

## Syntax

SapObject.SapModel.SolidObj.GetGroupAssign

## VB6 Procedure

Function GetGroupAssign(ByVal Name As String, ByRef NumberGroups As Long, ByRef Groups() As String)  As Long

## Parameters

Name

The name of an existing solid object.

NumberGroups

The number of group names retrieved.

Groups

The names of the groups to which the solid object is assigned.

## Remarks

This function retrieves the names of the groups to which a specified solid object is assigned.

The function returns zero if the group assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjectGroups()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'define new groups
      ret = SapModel.GroupDef.SetGroup("Group1")
      ret = SapModel.GroupDef.SetGroup("Group2")

   'add solid object to groups
      ret = SapModel.SolidObj.SetGroupAssign("2", "Group1")
      ret = SapModel.SolidObj.SetGroupAssign("2", "Group2")

   'get solid object groups
      ret = SapModel.SolidObj.GetGroupAssign("2", NumberGroups, Groups)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.0.0.

## See Also

[SetGroupAssign](SetGroupAssign_{Solid_Object}.htm)



## GetLoadGravity {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetLoadGravity_{Solid_Object}.htm`*

# GetLoadGravity

## Syntax

SapObject.SapModel.SolidObj.GetLoadGravity

## VB6 Procedure

Function GetLoadGravity(ByVal Name As String, ByRef NumberItems As Long, ByRef SolidName() As String, ByRef LoadPat() As String, ByRef CSys() As String, ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

NumberItems

The total number of gravity loads retrieved for the specified solid objects.

SolidName

This is an array that includes the name of the solid object associated with each gravity load.

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

If this item is Object, the assignments are retrieved for the solid object specified by the Name item.

If this item is Group, the assignments are retrieved for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected solid objects, and the Name item is ignored.

## Remarks

This function retrieves the gravity load assignments to solid objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjectGravityLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim SolidName() As String
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object gravity loads
      ret = SapModel.SolidObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'get solid object gravity load
      ret = SapModel.SolidObj.GetLoadGravity("1", NumberItems, SolidName, LoadPat, CSys, x, y, z)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadGravity](SetLoadGravity_{Solid_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Solid_Object}.htm)



## GetLoadPorePressure {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetLoadPorePressure_{Solid_Object}.htm`*

# GetLoadPorePressure

## Syntax

SapObject.SapModel.SolidObj.GetLoadPorePressure

## VB6 Procedure

Function GetLoadPorePressure(ByVal Name As String, ByRef NumberItems As Long, ByRef SolidName() As String, ByRef LoadPat() As String, ByRef Value() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

NumberItems

The total number of pore pressure loads retrieved for the specified solid objects.

SolidName

This is an array that includes the name of the solid object associated with each pore pressure load.

LoadPat

This is an array that includes the name of the load pattern associated with each pore pressure load.

Value

This is an array that includes the pore pressure load value. [F/L2]

PatternName

This is an array that includes the joint pattern name, if any, used to specify the pore pressure load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the solid object specified by the Name item.

If this item is Group, the assignments are retrieved for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected solid objects, and the Name item is ignored.

## Remarks

This function retrieves the pore pressure load assignments to solid objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjectPorePressureLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim SolidName() As String
      Dim LoadPat() As String
      Dim Value() As Double
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object pore pressure load
      ret = SapModel.SolidObj.SetLoadPorePressure("ALL", "DEAD", .1, , , Group)

   'get solid object pore pressure load
      ret = SapModel.SolidObj.GetLoadPorePressure("ALL", NumberItems, SolidName, LoadPat, Value, PatternName, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadPorePressure](SetLoadPorePressure_{Solid_Object}.htm)

[DeleteLoadPorePressure](DeleteLoadPorePressure_{Solid_Object}.htm)



## GetLoadStrain {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetLoadStrain_{Solid_Object}.htm`*

# GetLoadStrain

## Syntax

SapObject.SapModel.SolidObj.GetLoadStrain

## VB6 Procedure

Function GetLoadStrain(ByVal Name As String, ByRef NumberItems As Long, ByRef SolidName() As String, ByRef LoadPat() As String, ByRef Component() As Long, ByRef Value() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

NumberItems

The total number of strain loads retrieved for the specified solid objects.

SolidName

This is an array that includes the name of the solid object associated with each strain load.

LoadPat

This is an array that includes the name of the load pattern associated with each strain load.

Component

This is 1, 2, 3, 4, 5 or 6, indicating the component to which the strain load is applied.

1 = Strain11

2 = Strain22

3 = Strain33

4 = Strain12

5 = Strain13

6 = Strain23

Value

This is an array that includes the strain value. [L/L]

PatternName

This is an array that includes the joint pattern name, if any, used to specify the strain load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the solid object specified by the Name item.

If this item is Group, the assignments are retrieved for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected solid objects, and the Name item is ignored.

## Remarks

This function retrieves the strain load assignments to solid objects.

The function returns zero if the strain load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjectStrainLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim SolidName() As String
      Dim LoadPat() As String
      Dim Component() As Long
      Dim Value() As Double
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object strain load
      ret = SapModel.SolidObj.SetLoadStrain("ALL", "DEAD", 1, 0.001, , , Group)

   'get solid object strain load
      ret = SapModel.SolidObj.GetLoadStrain("1", NumberItems, SolidName, LoadPat, Component, Value, PatternName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadStrain](SetLoadStrain_{Solid_Object}.htm)

[DeleteLoadStrain](DeleteLoadStrain_{Solid_Object}.htm)



## GetLoadSurfacePressure {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetLoadSurfacePressure_{Solid_Object}.htm`*

# GetLoadSurfacePressure

## Syntax

SapObject.SapModel.SolidObj.GetLoadSurfacePressure

## VB6 Procedure

Function GetLoadSurfacePressure(ByVal Name As String, ByRef NumberItems As Long, ByRef SolidName() As String, ByRef LoadPat() As String, ByRef Face() As Long, ByRef Value() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

NumberItems

The total number of surface pressure loads retrieved for the specified solid objects.

SolidName

This is an array that includes the name of the solid object associated with each surface pressure load.

LoadPat

This is an array that includes the name of the load pattern associated with each surface pressure load.

Face

This is an array that includes 1, 2, 3, 4, 5 or 6, indicating the solid object face to which the specified load assignment applies.

Value

This is an array that includes the surface pressure load value. [F/L2]

PatternName

This is an array that includes the joint pattern name, if any, used to specify the surface pressure load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the solid object specified by the Name item.

If this item is Group, the assignments are retrieved for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected solid objects, and the Name item is ignored.

## Remarks

This function retrieves the surface pressure load assignments to solid objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjectSurfacePressureLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim SolidName() As String
      Dim LoadPat() As String
      Dim Face() As Long
      Dim Value() As Double
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object surface pressure load
      ret = SapModel.SolidObj.SetLoadSurfacePressure("ALL", "DEAD", 1, .1, , , Group)

   'get solid object surface pressure load
      ret = SapModel.SolidObj.GetLoadSurfacePressure("ALL", NumberItems, SolidName, LoadPat, Face, Value, PatternName, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadSurfacePressure](SetLoadSurfacePressure_{Solid_Object}.htm)

[DeleteLoadSurfacePressure](DeleteLoadSurfacePressure_{Solid_Object}.htm)



## GetLoadTemperature {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetLoadTemperature_{Solid_Object}.htm`*

# GetLoadTemperature

## Syntax

SapObject.SapModel.SolidObj.GetLoadTemperature

## VB6 Procedure

Function GetLoadTemperature(ByVal Name As String, ByRef NumberItems As Long, ByRef SolidName() As String, ByRef LoadPat() As String, ByRef Value() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

NumberItems

The total number of temperature loads retrieved for the specified solid objects.

SolidName

This is an array that includes the name of the solid object associated with each temperature load.

LoadPat

This is an array that includes the name of the load pattern associated with each temperature load.

Value

This is an array that includes the temperature load value. [T]

PatternName

This is an array that includes the joint pattern name, if any, used to specify the temperature load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the solid object specified by the Name item.

If this item is Group, the assignments are retrieved for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected solid objects, and the Name item is ignored.

## Remarks

This function retrieves the temperature load assignments to solid objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjectTemperatureLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim SolidName() As String
      Dim LoadPat() As String
      Dim Value() As Double
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object temperature load
      ret = SapModel.SolidObj.SetLoadTemperature("All", "DEAD", 50, , , Group)

   'get solid object temperature load
      ret = SapModel.SolidObj.GetLoadTemperature("ALL", NumberItems, SolidName, LoadPat, Value, PatternName, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadTemperature](SetLoadTemperature_{Solid_Object}.htm)

[DeleteLoadTemperature](DeleteLoadTemperature_{Solid_Object}.htm)



## GetLocalAxesAdvanced Solid Object

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetLocalAxesAdvanced_Solid_Object.htm`*

# GetLocalAxesAdvanced

## Syntax

SapObject.SapModel.SolidObj.GetLocalAxesAdvanced

## VB6 Procedure

Function GetLocalAxesAdvanced(ByVal Name As String, ByRef Active As Boolean, ByRef AxVectOpt As Long, ByRef AxCSys As String, ByRef AxDir() As Long, ByRef AxPt() As String, ByRef AxVect() As Double, ByRef Plane2 As Long, ByRef PlVectOpt As Long, ByRef PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double) As Long

## Parameters

Name

The name of an existing solid object.

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

This is an array dimensioned to 1 (2 integers) indicating the axis/plane reference vector primary and secondary coordinate directions, PlDir(0) and PlDir(1) respectively, taken at the object center in the specified coordinate system and used to determine the plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 1. Possible coordinate direction values are:

1 = +X         -1 = -X

2 = +Y        -2 = -Y

3 = +Z        -3 = -Z

4 = +CR     -4 = -CR

5 = +CA     -5 = -CA

6 = +CZ     -6 = -CZ

7 = +SR     -7 = -SR

8 = +SA     -8 = -SA

9 = +SB     -9 = -SB

AxPt, PlPt

This is an array dimensioned to 1 (2 strings), indicating the labels of two joints that define the axis/plane reference vector. Either of these joints may be specified as None to indicate the center of the specified object.  If both joints are specified as None, they are not used to define the plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 2.

AxVect, PlVect

This is an array dimensioned to 2 (3 doubles) that defines the axis/plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 3.

Plane2

This is 12, 13, 21, 23, 31 or 32, indicating that the local plane determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, 0r 3-2 plane. This item applies only when the Active item is True.

## Remarks

This function assigns advanced local axes to solid objects.

The function returns zero if the advanced local axes assignments are assigned successfully; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidAdvancedLocalAxes()
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
      Dim a As Double, b As Double, c As Double
      Dim Advanced As Boolean
      Dim Active As Boolean
      Dim AxVectOpt As Long
      Dim AxCSys As String
      Dim AxDir() As Long
      Dim AxPt() As String
      Dim AxVect() As Double
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid advanced local axes
      MyAxVect(0)=0.707
      MyAxVect(1)=0.707
      MyAxVect(2)=0
      MyPlDir(0) = 2
      MyPlDir(1) = 3
      ret = SapModel.SolidObj.SetLocalAxesAdvanced("ALL", True, 3, "Global", MyAxDir, MyAxPt, MyAxVect, 12, 1, "Global", MyPlDir, MyPlPt, MyPlVect, Group)

   'get local axes assignments
      ret = SapModel.SolidObj.GetLocalAxes("1", a, b, c, Advanced)

   'get solid advanced local axes data
      If Advanced Then
         ret = SapModel.SolidObj.GetLocalAxesAdvanced("3", Active, AxVectOpt, AxCSys, AxDir, AxPt, AxVect, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect)
      End If

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

## See Also

[SetLocalAxesAdvanced](SetLocalAxesAdvanced_Solid_Object.htm)

[SetLocalAxes](SetLocalAxes_{Solid_Object}.htm)



## GetLocalAxes {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetLocalAxes_{Solid_Object}.htm`*

# GetLocalAxes

## Syntax

SapObject.SapModel.SolidObj.GetLocalAxes

## VB6 Procedure

Function GetLocalAxes(ByVal Name As String, ByRef a As Double, ByRef b As Double, ByRef c As Double, ByRef Advanced As Boolean) As Long

## Parameters

Name

The name of an existing solid object.

a, b, c

The local axes of the solid object are defined by first setting the positive local 1, 2 and 3 axes the same as the positive global X, Y and Z axes and then doing the following: [deg]

1.    Rotate about the 3 axis by angle a.

2.    Rotate about the resulting 2 axis by angle b.

3.    Rotate about the resulting 1 axis by angle c.

Advanced

This item is True if the solid object local axes orientation was obtained using advanced local axes parameters.

## Remarks

This function retrieves the local axes angles for a solid object.

The function returns zero if the local axes angles are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidLocalAxes()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim a As Double, b As Double, c As Double
      Dim Advanced As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign local axes angles
      ret = SapModel.SolidObj.SetLocalAxes("ALL", 30, 40, 50, Group)

   'get local axes assignments
      ret = SapModel.SolidObj.GetLocalAxes("1", a, b, c, Advanced)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetLocalAxes](SetLocalAxes_{Solid_Object}.htm)



## GetMatTemp {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetMatTemp_{Solid_Object}.htm`*

# GetMatTemp

## Syntax

SapObject.SapModel.SolidObj.GetMatTemp

## VB6 Procedure

Function GetMatTemp(ByVal Name As String, ByRef Temp As Double, ByRef PatternName As String) As Long

## Parameters

Name

The name of an existing solid object.

Temp

This is the material temperature value assigned to the solid object. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the material temperature for the solid object is uniform over the object at the value specified by Temp.

If PatternName is the name of a defined joint pattern, the material temperature for the solid object may vary. The material temperature at each corner point of the solid object is equal to the specified temperature multiplied by the pattern value at the associated point object. The material temperature at other points in the solid object is calculated by interpolation from the corner points.

## Remarks

This function retrieves the material temperature assignments to solid objects.

The function returns zero if the material temperature assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjectMatTemp()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign material temperature
      ret = SapModel.SolidObj.SetMatTemp("ALL", 50, , Group)

   'get material temperature
      ret = SapModel.SolidObj.GetMatTemp("3", Temp, PatternName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMatTemp](SetMatTemp_{Solid_Object}.htm)



## GetNameList {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetNameList_{Solid_Object}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.SolidObj.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of solid object names retrieved by the program.

MyName

This is a one-dimensional array of solid object names. The MyName array is created as a dynamic, zero-based, array by the APIuser:

Dim MyName() as String

The array is dimensioned to (NumberNames – 1) inside the SAP2000 program, filled with the names, and returned to the APIuser.

## Remarks

This function retrieves the names of all defined solid objects.

The function returns zero if the names are successfully retrieved; otherwise it returns nonzero.

## VBA Example

Sub GetSolidObjectNames()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'get solid object names
      ret = SapModel.SolidObj.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetPoints {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetPoints_{Solid_Object}.htm`*

# GetPoints

## Syntax

SapObject.SapModel.SolidObj.GetPoints

## VB6 Procedure

Function GetPoints(ByVal Name As String, ByRef Point() As String) As Long

## Parameters

Name

The name of a defined solid object.

Point

This is an array containing the names of the corner point objects of the solid object.

## Remarks

This function retrieves the names of the corner point objects of a solid object.

The function returns zero if the point object names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjPoints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberPoints As Long
      Dim Point() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'get names of points
      ReDim Point(7)
      ret = SapModel.SolidObj.GetPoints("1", Point)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetProperty {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetProperty_{Solid_Object}.htm`*

# GetProperty

## Syntax

SapObject.SapModel.SolidObj.GetProperty

## VB6 Procedure

Function GetProperty(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a defined solid object.

PropName

The name of the solid property assigned to the solid object.

## Remarks

This function retrieves the solid property assigned to a solid object.

The function returns zero if the property is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjectProp()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'get solid property
      ret = SapModel.SolidObj.GetProperty("1", PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetProperty](SetProperty_{Solid_Object}.htm)



## GetSelected {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetSelected_{Solid_Object}.htm`*

# GetSelected

## Syntax

Sap2000.SolidObj.GetSelected

## VB6 Procedure

Function GetSelected(ByVal Name As String, ByRef Selected As Boolean) As Long

## Parameters

Name

The name of an existing solid object.

Selected

This item is True if the specified solid object is selected; otherwise it is False.

## Remarks

This function retrieves the selected status for a solid object.

The function returns zero if the selected status is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjectSelectedStatus()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'set all solid objects selected
      ret = SapModel.SolidObj.SetSelected("ALL", True, Group)

   'get solid object selected status
      ret = SapModel.SolidObj.GetSelected("1", Selected)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSelected](SetSelected_{Solid_Object}.htm)



## GetSpring {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetSpring_{Solid_Object}.htm`*

# GetSpring

## Syntax

SapObject.SapModel.SolidObj.GetSpring

## VB6 Procedure

Function GetSpring(ByVal Name As String, ByRef NumberSprings As Long, ByRef MyType() As Long, ByRef s() As Double, ByRef SimpleSpringType() As Long, ByRef LinkProp() As String, ByRef Face() As Long, ByRef SpringLocalOneType() As Long, ByRef Dir() As Long, ByRef Outward() As Boolean, ByRef VecX() As Double, ByRef VecY() As Double, ByRef VecZ() As Double, ByRef CSys() As String, ByRef Ang() As Double) As Long

## Parameters

Name

The name of an existing solid object.

NumberSprings

The number of springs assignments made to the specified solid object.

MyType

Each value in this array is either 1 or 2, indicating the spring property type.

1 = Simple spring

2 = Link property

s

Each value in this array is the simple spring stiffness per unit area of the specified solid object face. This item applies only when the corresponding MyType = 1. [F/L3]

SimpleSpringType

Each value in this array is 1, 2 or 3, indicating the simple spring type. This item applies only when the corresponding MyType = 1.

1 = Spring resists tension and compression

2 = Spring resists compression only

3 = Spring resists tension only

LinkProp

Each value in this array is the name of the link property assigned to the spring. This item applies only when the corresponding MyType = 2.

Face

This is 1, 2, 3, 4, 5 or 6, indicating the solid object face to which the specified spring assignment applies.

SpringLocalOneType

Each value in this array is 1, 2 or 3, indicating the method used to specify the spring positive local 1-axis orientation.

1 = Parallel to solid object local axis

2 = Normal to specified solid object face

3 = User specified direction vector

Dir

Each value in this array is 1, 2, 3, -1, -2 or -3, indicating the solid object local axis that corresponds to the positive local 1-axis of the spring. This item applies only when the corresponding SpringLocalOneType = 1.

Outward

Each value in this array is True if the spring positive local 1 axis is outward from the specified solid object face. This item applies only when SpringLocalOneType = 2.

VecX

Each value in this array is the X-axis or solid object local 1-axis component (depending on the CSys specified) of the user specified direction vector for the spring local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when the corresponding SpringLocalOneType = 3.

VecY

Each value in this array is the Y-axis or solid object local 2-axis component (depending on the CSys specified) of the user specified direction vector for the spring local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when the corresponding SpringLocalOneType = 3.

VecZ

Each value in this array is the X-axis or solid object local 3-axis component (depending on the CSys specified) of the user specified direction vector for the spring local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when the corresponding SpringLocalOneType = 3.

CSys

Each value in this array is Local (meaning the solid object local coordinate system) or the name of a defined coordinate system. This item is the coordinate system in which the user specified direction vector, Vec, is specified. This item applies only when the corresponding SpringLocalOneType = 3.

Ang

Each value in this array is the angle that the link local 2-axis is rotated from its default orientation. This item applies only when the corresponding MyType = 2. [deg]

## Remarks

This function retrieves the spring assignments to a solid object face.

The function returns zero if the assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjectSprings()
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
      Dim Face() As Long
      Dim SpringLocalOneType() As Long
      Dim Dir() As Long
      Dim Outward() As Boolean
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign springs to solid objects
      ReDim Vec(2)
      ret = SapModel.SolidObj.SetSpring("1", 1, 1, 1, "", 1, 1, 3, True, Vec, 0, False, "Local")

   'get spring assignments to solid objects
      ret = SapModel.SolidObj.GetSpring("1", NumberSprings, MyType, s, SimpleSpringType, LinkProp, Face, SpringLocalOneType, Dir, Outward, VecX, VecY, VecZ, CSys, Ang)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSpring](SetSpring_{Solid_Object}.htm)

[DeleteSpring](DeleteSpring_{Solid_Object}.htm)



## GetTransformationMatrix {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/GetTransformationMatrix_{Solid_Object}.htm`*

# GetTransformationMatrix

## Syntax

Sap2000.SolidObj.GetTransformationMatrix

## VB6 Procedure

Function GetTransformationMatrix(ByVal Name As String, ByRef Value() As Double,Optional ByVal IsGlobal As Boolean = True) As Long

## Parameters

Name

The name of an existing solid object.

Value

Value is an array of nine direction cosines that define the transformation matrix.

The following matrix equation shows how the transformation matrix is used to convert items from the solid object local coordinate system to the global coordinate system.

![](../../../assets/images/Images/Transformation%20Matrix.JPG)

In the equation, c0 through c8 are the nine values from the transformation array, (Local1, Local2, Local3) are an item (such as a load) in the object local coordinate system, and (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.

The transformation from the local coordinate system to the present coordinate system is the same as that shown above for the global system if you substitute the present system for the global system.

IsGlobal

If this item is True, the transformation matrix is between the Global coordinate system and the solid object local coordinate system.

If this item is False, the transformation matrix is between the present coordinate system and the solid object local coordinate system.

## Remarks

The function returns zero if the solid object transformation matrix is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSolidObjectMatrix()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'get solid object transformation matrix
      ReDim Value(8)
      ret = SapModel.SolidObj.GetTransformationMatrix("3", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## SetAutoMesh {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetAutoMesh_{Solid_Object}.htm`*

# SetAutoMesh

## Syntax

SapObject.SapModel.SolidObj.SetAutoMesh

## VB6 Procedure

Function SetAutoMesh(ByVal Name As String, ByVal MeshType As Long, Optional ByVal n1 As Long = 2, Optional ByVal n2 As Long = 2, Optional ByVal n3 As Long = 2, Optional ByVal MaxSize1 As Double = 0, Optional ByVal MaxSize2 As Double = 0, Optional ByVal MaxSize3 As Double = 0, Optional ByVal RestraintsOnEdge As Boolean = False, Optional ByVal RestraintsOnFace As Boolean = False) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

MeshType

This item is 0, 1 or 2, indicating the automatic mesh type for the solid object.

0 = No automatic meshing

1 = Mesh solid into a specified number of objects

2 = Mesh solid into objects of a specified maximum size

n1

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed solid object that runs from point 1 to point 2.

n2

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed solid object that runs from point 1 to point 3.

n3

This item applies when MeshType = 1. It is the number of objects created along the edge of the meshed solid object that runs from point 1 to point 5.

MaxSize1

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed solid object that runs from point 1 to point 2. [L]

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

MaxSize2

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed solid object that runs from point 1 to point 3. [L]

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

MaxSize3

This item applies when MeshType = 2. It is the maximum size of objects created along the edge of the meshed solid object that runs from point 1 to point 5. [L]

If this item is input as 0, the default value is used. The default value is 48 inches if the database units are English or 120 centimeters if the database units are metric.

RestraintsOnEdge

If this item is True, and if both points along an edge of the original solid object have the same restraint/constraint, then, if the an added point on that edge and the original corner points have the same local axes definition, the program assigns the restraint/constraint to the added point.

RestraintsOnFace

If this item is True, and if all corner points on an solid object face have the same restraint/constraint, then, if an added point on that face and the original corner points for the face have the same local axes definition, the program assigns the restraint/constraint to the added point.

## Remarks

This function makes automatic meshing assignments to solid objects.

The function returns zero if the meshing options are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSolidObjAutoMesh()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign auto mesh options
      ret = SapModel.SolidObj.SetAutoMesh("ALL", 1, 3, 3,3, , , , , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetAutoMesh](GetAutoMesh_{Solid_Object}.htm)



## SetEdgeConstraint {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetEdgeConstraint_{Solid_Object}.htm`*

# SetEdgeConstraint

## Syntax

SapObject.SapModel.SolidObj.SetEdgeConstraint

## VB6 Procedure

Function SetEdgeConstraint(ByVal Name As String, ByVal ConstraintExists As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

ConstraintExists

This item is True if an automatic edge constraint is generated by the program for the solid object in the analysis model.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the solid object specified by the Name item.

If this item is Group, the assignment is made to all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected solid objects, and the Name item is ignored.

## Remarks

This function makes generated edge constraint assignments to solid objects.

The function returns zero if the edge constraint option is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSolidObjAutoEdgeConstraint()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign auto edge constraint option
      ret = SapModel.SolidObj.SetEdgeConstraint("ALL", True, Group)
      ret = SapModel.SolidObj.SetEdgeConstraint("1", False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetEdgeConstraint](GetEdgeConstraint_{Solid_Object}.htm)



## SetGUID {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetGUID_{Solid_Object}.htm`*

# SetGUID

## Syntax

SapObject.SapModel.SolidObj.SetGUID

## VB6 Procedure

Function SetGUID(ByVal Name As String, Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing solid object.

GUID

The GUID (Global Unique ID) for the specified solid object.

## Remarks

This function sets the GUID for the specified solid object. If the GUID is passed in as a blank string, the program automatically creates a GUID for the object.

This function returns zero if the solid object GUID is successfully set; otherwise it returns nonzero.

## VBA Example

Sub SetSolidObjGUID()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'set program created GUID
      ret = SapObject.SapModel.SolidObj.SetGUID("1")

   'get GUID
      ret = SapObject.SapModel.SolidObj.GetGUID("1", GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[GetGUID](GetGUID_{Solid_Object}.htm)



## SetGroupAssign {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetGroupAssign_{Solid_Object}.htm`*

# SetGroupAssign

## Syntax

SapObject.SapModel.SolidObj.SetGroupAssign

## VB6 Procedure

Function SetGroupAssign(ByVal Name As String, ByVal GroupName As String, Optional By Val Remove As Boolean = False, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

GroupName

The name of an existing group to which the assignment is made.

Remove

If this item is False, the specified solid objects are added to the group specified by the GroupName item. If it is True, the solid objects are removed from the group.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the solid object specified by the Name item is added or removed from the group specified by the GroupName item.

If this item is Group, all solid objects in the group specified by the Name item are added or removed from the group specified by the GroupName item.

If this item is SelectedObjects, all selected solid objects are added or removed from the group specified by the GroupName item, and the Name item is ignored.

## Remarks

This function adds or removes solid objects from a specified group.

The function returns zero if the group assignment is successful; otherwise it returns a nonzero value.

## VBA Example

Sub AddSolidObjectsToGroup()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'define new group
      ret = SapModel.GroupDef.SetGroup("Group1")

   'add solid objects to group
      ret = SapModel.SolidObj.SetGroupAssign("1", "Group1")
      ret = SapModel.SolidObj.SetGroupAssign("2", "Group1")
      ret = SapModel.SolidObj.SetGroupAssign("3", "Group1")

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

[GetGroupAssign](GetGroupAssign_{Solid_Object}.htm)



## SetLoadGravity {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetLoadGravity_{Solid_Object}.htm`*

# SetLoadGravity

## Syntax

SapObject.SapModel.SolidObj.SetLoadGravity

## VB6 Procedure

Function SetLoadGravity(ByVal Name As String, ByVal LoadPat As String, ByVal x As Double, ByVal y As Double, ByVal z As Double, Optional ByVal Replace As Boolean = True, Optional ByVal CSys As String = "Global", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

x, y, z

These are the gravity load multipliers in the x, y and z directions of the specified coordinate system.

Replace

If this item is True, all previous gravity loads, if any, assigned to the specified solid object(s), in the specified load pattern, are deleted before making the new assignment.

CSys

The coordinate system in which the x, y and z multipliers are specified.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the solid object specified by the Name item.

If this item is Group, the assignment is made to all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected solid objects, and the Name item is ignored.

## Remarks

This function assigns gravity load multipliers to solid objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSolidObjectGravityLoad()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object gravity loads
      ret = SapModel.SolidObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Solid_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Solid_Object}.htm)



## SetLoadPorePressure {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetLoadPorePressure_{Solid_Object}.htm`*

# SetLoadPorePressure

## Syntax

SapObject.SapModel.SolidObj.SetLoadPorePressure

## VB6 Procedure

Function SetLoadPorePressure(ByVal Name As String, ByVal LoadPat As String, ByVal Value As Double, Optional ByVal PatternName As String = "", Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Value

This is the pore pressure value. [F/L2]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the pore pressure load for the solid object is uniform over the object at the value specified by Value.

If PatternName is the name of a defined joint pattern, the pore pressure load for the solid object is based on the specified pore pressure value multiplied by the pattern value at the corner point objects of the solid object.

Replace

If this item is True, all previous pore pressure loads, if any, assigned to the specified solid object(s), in the specified load case, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the solid object specified by the Name item.

If this item is Group, the assignment is made to all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected solid objects, and the Name item is ignored.

## Remarks

This function assigns pore pressure loads to solid objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSolidObjectPorePressureLoad()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object pore pressure load
      ret = SapModel.SolidObj.SetLoadPorePressure("ALL", "DEAD", .1, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadPorePressure](GetLoadPorePressure_{Solid_Object}.htm)

[DeleteLoadPorePressure](DeleteLoadPorePressure_{Solid_Object}.htm)



## SetLoadStrain {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetLoadStrain_{Solid_Object}.htm`*

# SetLoadStrain

## Syntax

SapObject.SapModel.SolidObj.SetLoadStrain

## VB6 Procedure

Function SetLoadStrain(ByVal Name As String, ByVal LoadPat As String, ByVal Component As Long, ByVal Value As Double, Optional ByVal Replace As Boolean = True, Optional ByVal PatternName As String = "", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Component

This is 1, 2, 3, 4, 5 or 6, indicating the component to which the strain load is applied.

1 = Strain11

2 = Strain22

3 = Strain33

4 = Strain12

5 = Strain13

6 = Strain23

Value

This is the strain load value. [L/L]

Replace

If this item is True, all previous strain loads, if any, assigned to the specified solid object(s), in the specified load pattern, for the specified degree of freedom, are deleted before making the new assignment.

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the strain load for the solid object is uniform over the object at the value specified by Value.

If PatternName is the name of a defined joint pattern, the strain load for the solid object is based on the specified strain value multiplied by the pattern value at the corner point objects of the solid object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the solid object specified by the Name item.

If this item is Group, the assignment is made to all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected solid objects, and the Name item is ignored.

## Remarks

This function assigns strain loads to solid objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSolidObjectStrainLoad()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object strain load
      ret = SapModel.SolidObj.SetLoadStrain("ALL", "DEAD", 1, 0.001, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadStrain](GetLoadStrain_{Solid_Object}.htm)

[DeleteLoadStrain](DeleteLoadStrain_{Solid_Object}.htm)



## SetLoadSurfacePressure {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetLoadSurfacePressure_{Solid_Object}.htm`*

# SetLoadSurfacePressure

## Syntax

SapObject.SapModel.SolidObj.SetLoadSurfacePressure

## VB6 Procedure

Function SetLoadSurfacePressure(ByVal Name As String, ByVal LoadPat As String, ByVal Face As Long, ByVal Value As Double, Optional ByVal PatternName As String = "", Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Face

This is 1, 2, 3, 4, 5 or 6, indicating the solid object face to which the specified load assignment applies.

Value

This is the surface pressure value. [F/L2]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the surface pressure load for the solid object is uniform over the object at the value specified by Value.

If PatternName is the name of a defined joint pattern, the surface pressure load for the solid object is based on the specified surface pressure value multiplied by the pattern value at the corner point objects of the solid object.

Replace

If this item is True, all previous surface pressure loads, if any, assigned to the specified solid object(s), on the specified face, in the specified load pattern, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the solid object specified by the Name item.

If this item is Group, the assignment is made to all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected solid objects, and the Name item is ignored.

## Remarks

This function assigns surface pressure loads to solid objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSolidObjectSurfacePressureLoad()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object surface pressure load
      ret = SapModel.SolidObj.SetLoadSurfacePressure("ALL", "DEAD", 1, .1, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadSurfacePressure](GetLoadSurfacePressure_{Solid_Object}.htm)

[DeleteLoadSurfacePressure](DeleteLoadSurfacePressure_{Solid_Object}.htm)



## SetLoadTemperature {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetLoadTemperature_{Solid_Object}.htm`*

# SetLoadTemperature

## Syntax

SapObject.SapModel.SolidObj.SetLoadTemperature

## VB6 Procedure

Function SetLoadTemperature(ByVal Name As String, ByVal LoadPat As String, ByVal Value As Double, Optional ByVal PatternName As String = "", Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Value

This is the temperature change value. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the temperature load for the solid object is uniform over the object at the value specified by Value.

If PatternName is the name of a defined joint pattern, the temperature load for the solid object is based on the specified temperature value multiplied by the pattern value at the corner point objects of the solid object.

Replace

If this item is True, all previous temperature loads, if any, assigned to the specified solid object(s), in the specified load case, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the solid object specified by the Name item.

If this item is Group, the assignment is made to all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected solid objects, and the Name item is ignored.

## Remarks

This function assigns temperature loads to solid objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSolidObjectTemperatureLoad()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid object temperature load
      ret = SapModel.SolidObj.SetLoadTemperature("All", "DEAD", 50, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTemperature](GetLoadTemperature_{Solid_Object}.htm)

[DeleteLoadTemperature](DeleteLoadTemperature_{Solid_Object}.htm)



## SetLocalAxesAdvanced Solid Object

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetLocalAxesAdvanced_Solid_Object.htm`*

# SetLocalAxesAdvanced

## Syntax

SapObject.SapModel.SolidObj.SetLocalAxesAdvanced

## VB6 Procedure

Function SetLocalAxesAdvanced(ByVal Name As String, ByVal Active As Boolean, ByVal AxVectOpt As Long, ByVal AxCSys As String, ByRef AxDir() As Long, ByRef AxPt() As String, ByRef AxVect() As Double, ByVal Plane2 As Long, ByVal PlVectOpt As Long, ByVal PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

Active

This is True if advanced local axes exist.

AxVectOpt, PlVectOpt

This is 1, 2, or 3, indicating the axis/plane reference vector option. This item applies only when the Active item is True.

1 = Coordinate direction

2 = Two joints

3 = User vector

AxCSys, PlCSys

The coordinate system used to define the axis/plane reference vector coordinate directions and the axis/plane user vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 1 or 3.

AxDir, PlDir

This is an array dimensioned to 1 (2 integers) indicating the axis/plane reference vector primary and secondary coordinate directions, PlDir(0) and PlDir(1) respectively, taken at the object center in the specified coordinate system and used to determine the plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 1. Possible coordinate direction values are:

1 = +X        -1 = -X

2 = +Y        -2 = -Y

3 = +Z        -3 = -Z

4 = +CR     -4 = -CR

5 = +CA     -5 = -CA

6 = +CZ     -6 = -CZ

7 = +SR     -7 = -SR

8 = +SA     -8 = -SA

9 = +SB     -9 = -SB

AxPt, PlPt

This is an array dimensioned to 1 (2 strings) indicating the labels of two joints that define the axis/plane reference vector. Either of these joints may be specified as None to indicate the center of the specified object.  If both joints are specified as None, they are not used to define the plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 2.

AxVect, PlVect

This is an array dimensioned to 2 (3 doubles) that defines the axis/plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 3.

Plane2

This is 12, 13, 21, 23, 31 or 32, indicating that the local plane determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, or 3-2 plane. This item applies only when the Active item is True.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

Selection = 2

If this item is Object, the assignment is made to the solid object specified by the Name item.

If this item is Group, the assignment is made to all solid objects in the group specified by the Name item.

If this item is Selection, assignment is made to all selected solid objects and the Name item is ignored.

## Remarks

This function assigns advanced local axes to solid objects.

The function returns zero if the advanced local axes assignments are assigned successfully; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSolidAdvancedLocalAxes()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign solid advanced local axes
      MyAxVect(0)=0.707
      MyAxVect(1)=0.707
      MyAxVect(2)=0
      MyPlDir(0) = 2
      MyPlDir(1) = 3
      ret = SapModel.SolidObj.SetLocalAxesAdvanced("ALL", True, 3, "Global", MyAxDir, MyAxPt, MyAxVect, 12, 1, "Global", MyPlDir, MyPlPt, MyPlVect, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

## See Also

[GetLocalAxesAdvanced](GetLocalAxesAdvanced_Solid_Object.htm)

[GetLocalAxes](GetLocalAxes_{Solid_Object}.htm)



## SetLocalAxes {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetLocalAxes_{Solid_Object}.htm`*

# SetLocalAxes

## Syntax

SapObject.SapModel.SolidObj.SetLocalAxes

## VB6 Procedure

Function SetLocalAxes(ByVal Name As String, ByVal a As Double, ByVal b As Double, ByVal c As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

a, b, c

The local axes of the solid object are defined by first setting the positive local 1, 2 and 3 axes the same as the positive global X, Y and Z axes and then doing the following: [deg]

1.    Rotate about the 3 axis by angle a.

2.    Rotate about the resulting 2 axis by angle b.

3.    Rotate about the resulting 1 axis by angle c.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the local axes assignment is made to the solid object specified by the Name item.

If this item is Group, the local axes assignment is made to all solid objects in the group specified by the Name item.

If this item is SelectedObjects, the local axes assignment is made to all selected solid objects, and the Name item is ignored.

## Remarks

This function sets the local axes angles for solid objects.

The function returns zero if the local axes angles are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSolidLocalAxes()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign local axes angles
      ret = SapModel.SolidObj.SetLocalAxes("1", 30, 40, 50)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetLocalAxes](GetLocalAxes_{Solid_Object}.htm)



## SetMatTemp {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetMatTemp_{Solid_Object}.htm`*

# SetMatTemp

## Syntax

SapObject.SapModel.SolidObj.SetMatTemp

## VB6 Procedure

Function SetMatTemp(ByVal Name As String, ByVal Temp As Double, Optional ByVal PatternName As String = "", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

Temp

This is the material temperature value assigned to the solid object. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the material temperature for the solid object is uniform over the object at the value specified by Temp.

If PatternName is the name of a defined joint pattern, the material temperature for the solid object may vary. The material temperature at each corner point of the solid object is equal to the specified temperature multiplied by the pattern value at the associated point object. The material temperature at other points in the solid object is calculated by interpolation from the corner points.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the solid object specified by the Name item.

If this item is Group, the assignment is made to all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected solid objects, and the Name item is ignored.

## Remarks

This function assigns material temperatures to solid objects.

The function returns zero if the material temperatures are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSolidObjectMatTemp()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign material temperature
      ret = SapModel.SolidObj.SetMatTemp("ALL", 50, , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMatTemp](GetMatTemp_{Solid_Object}.htm)



## SetProperty {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetProperty_{Solid_Object}.htm`*

# SetProperty

## Syntax

SapObject.SapModel.SolidObj.SetProperty

## VB6 Procedure

Function SetProperty(ByVal name As String, ByVal PropName As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

PropName

This is the name of a solid property to be assigned to the specified solid object(s).

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the solid object specified by the Name item.

If this item is Group, the assignment is made to all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected solid objects, and the Name item is ignored.

## Remarks

This function assigns a solid property to solid objects.

The function returns zero if the property is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub SetSolidObjectProp()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'set solid property
      ret = SapModel.SolidObj.SetProperty("1", "Solid1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetProperty](GetProperty_{Solid_Object}.htm)



## SetSelected {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetSelected_{Solid_Object}.htm`*

# SetSelected

## Syntax

Sap2000.SolidObj.SetSelected

## VB6 Procedure

Function SetSelected(ByVal Name As String, ByVal Selected As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

Selected

This item is True if the specified solid object is selected, otherwise it is False.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the selected status is set for the solid object specified by the Name item.

If this item is Group, the selected status is set for all solid objects in the group specified by the Name item.

If this item is SelectedObjects, the selected status is set for all selected solid objects, and the Name item is ignored.

## Remarks

This function sets the selected status for solid objects.

The function returns zero if the selected status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSolidObjectSelected()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'set solid objects selected
      ret = SapModel.SolidObj.SetSelected("ALL", True, Group)

   'update window
      ret = SapModel.View.RefreshWindow

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSelected](GetSelected_{Solid_Object}.htm)



## SetSpring {Solid Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Solid_Object/SetSpring_{Solid_Object}.htm`*

# SetSpring

## Syntax

SapObject.SapModel.SolidObj.SetSpring

## VB6 Procedure

Function SetSpring(ByVal Name As String, ByVal MyType As Long, ByVal s As Double, ByVal SimpleSpringType As Long, ByVal LinkProp As String, ByVal Face as Long, ByVal SpringLocalOneType As Long, ByVal Dir As Long, ByVal Outward As Boolean, ByRef Vec() As Double, ByVal Ang As Double, ByVal Replace As Boolean, Optional ByVal CSys As String = "Local", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing solid object or group, depending on the value of the ItemType item.

MyType

This is either 1 or 2, indicating the spring property type.

1 = Simple spring

2 = Link property

s

The simple spring stiffness per unit area of the specified solid object face. This item applies only when MyType = 1. [F/L3]

SimpleSpringType

This is 1, 2 or 3, indicating the simple spring type. This item applies only when MyType = 1.

1 = Spring resists tension and compression

2 = Spring resists compression only

3 = Spring resists tension only

LinkProp

The name of the link property assigned to the spring. This item applies only when MyType = 2.

Face

This is 1, 2, 3, 4, 5 or 6, indicating the solid object face to which the specified spring assignment applies.

SpringLocalOneType

This is 1, 2 or 3, indicating the method used to specify the spring positive local 1-axis orientation.

1 = Parallel to solid object local axis

2 = Normal to specified solid object face

3 = User specified direction vector

Dir

This is 1, 2, 3, -1, -2 or -3, indicating the solid object local axis that corresponds to the positive local 1-axis of the spring. This item applies only when SpringLocalOneType = 1.

Outward

This item is True if the spring positive local 1 axis is outward from the specified solid object face. This item applies only when SpringLocalOneType = 2.

Vec

This is an array of three values that define the direction vector of the spring positive local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when SpringLocalOneType = 3.

Ang

This is the angle that the link local 2-axis is rotated from its default orientation. This item applies only when MyType = 2. [deg]

Replace

If this item is True, all existing spring assignments to the solid object are removed before assigning the specified spring. If it is False, the specified spring is added to any existing springs already assigned to the solid object.

CSys

This is Local (meaning the solid object local coordinate system) or the name of a defined coordinate system. This item is the coordinate system in which the user specified direction vector, Vec, is specified. This item applies only when SpringLocalOneType = 3.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the solid object specified by the Name item.

If this item is Group, the assignment is made to all solid objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected solid objects, and the Name item is ignored.

## Remarks

This function makes spring assignments to solid objects. The springs are assigned to a specified solid object face.

The function returns zero if the assignments are successfully applied; otherwise it returns a nonzero value.

## VBA Example

Sub AssignSolidObjectSprings()
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
      ret = SapModel.File.NewSolidBlock(300, 400, 200, , , 2, 2, 2)

   'assign springs to solid objects
      ReDim Vec(2)
      ret = SapModel.SolidObj.SetSpring("1", 1, 1, 1, "", 1, 1, 3, True, Vec, 0, False, "Local")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Solid_Object}.htm)

[DeleteSpring](DeleteSpring_{Solid_Object}.htm)

