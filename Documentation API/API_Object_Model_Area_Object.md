# API Object Model Area Object

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Object_Model/Area_Object

---



## AddByCoord {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/AddByCoord_{Area_Object}.htm`*

# AddByCoord

## Syntax

SapObject.SapModel.AreaObj.AddByCoord

## VB6 Procedure

Function AddByCoord(ByVal NumberPoints As long, ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, ByRef Name As String, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "", Optional ByVal CSys As String = "Global") As Long

## Parameters

NumberPoints

The number of points in the area abject.

x, y, z

These are arrays of x, y and z coordinates, respectively, for the corner points of the area object. The coordinates are in the coordinate system defined by the CSys item. The coordinates should be ordered to run clockwise or counter clockwise around the area object.

Name

This is the name that the program ultimately assigns to the area object. If no UserName is specified, the program assigns a default name to the area object. If a UserName is specified and that name is not used for another area object, the UserName is assigned to the area object; otherwise a default name is assigned to the area object.

PropName

This is Default, None or the name of a defined area property.

If it is Default, the program assigns a default area property to the area object. If it is None, no area property is assigned to the area object. If it is the name of a defined area property, that property is assigned to the area object.

UserName

This is an optional user specified name for the area object. If a UserName is specified and that name is already used for another area object, the program ignores the UserName.

CSys

The name of the coordinate system in which the area object point coordinates are defined.

## Remarks

This function adds a new area object, defining points at the specified coordinates.

The function returns zero if the area object is successfully added, otherwise it returns a nonzero value.

## VBA Example

Sub AddAreaObjByCoord()
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

   'add area object by coordinates
      ReDim x(5)
      ReDim y(5)
      ReDim z(5)
      x(0) = 50:   y(0) = 0
      x(1) = 100:  y(1) = 0
      x(2) = 150:  y(2) = 40
      x(3) = 100:  y(3) = 80
      x(4) = 50:   y(4) = 80
      x(5) = 0:    y(5) = 40
      ret = SapModel.AreaObj.AddByCoord(6, x, y, z, Name)

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

[AddByPoint](AddByPoint_{Area_Object}.htm)



## AddByPoint {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/AddByPoint_{Area_Object}.htm`*

# AddByPoint

## Syntax

SapObject.SapModel.AreaObj.AddByPoint

## VB6 Procedure

Function AddByPoint(ByVal NumberPoints as Long, ByRef Point() as String, ByRef Name As String, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "") As Long

## Parameters

NumberPoints

The number of points in the area abject.

Point

This is an array containing the names of the point objects that define the added area object. The point object names should be ordered to run clockwise or counter clockwise around the area object.

Name

This is the name that the program ultimately assigns for the area object. If no UserName is specified, the program assigns a default name to the area object. If a UserName is specified and that name is not used for another area object, the UserName is assigned to the area object; otherwise a default name is assigned to the area object.

PropName

This is Default, None or the name of a defined area property.

If it is Default, the program assigns a default area property to the area object. If it is None, no area property is assigned to the area object. If it is the name of a defined area property, that property is assigned to the area object.

UserName

This is an optional user specified name for the area object. If a UserName is specified and that name is already used for another area object, the program ignores the UserName.

## Remarks

This function adds a new area object whose defining points are specified by name.

The function returns zero if the area object is successfully added; otherwise it returns a nonzero value.

## VBA Example

Sub AddAreaObjByPoint()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add area object by points
      Redim Point(3)
      Point(0) = "1"
      Point(1) = "4"
      Point(2) = "5"
      Point(3) = "2"
      ret = SapModel.AreaObj.AddByPoint(4, Point, Name)

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

[AddByCoord](AddByCoord_{Area_Object}.htm)



## ChangeName {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/ChangeName_{Area_Object}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.AreaObj.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a defined area object.

NewName

The new name for the area object.

## Remarks

This function applies a new name to an area object.

The function returns zero if the new name is successfully applied, otherwise it returns a nonzero value.

## VBA Example

Sub ChangeAreaObjName()
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

   'change name
      ret = SapModel.AreaObj.ChangeName("1", "MyArea")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## Count {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/Count_{Area_Object}.htm`*

# Count

## Syntax

SapObject.SapModel.AreaObj.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None

## Remarks

This function returns a count of the area objects in the model.

## VBA Example

Sub CountAreaObjects()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'return number of area objects
      Count = SapModel.AreaObj.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## DeleteLoadGravity {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/DeleteLoadGravity_{Area_Object}.htm`*

# DeleteLoadGravity

## Syntax

SapObject.SapModel.AreaObj.DeleteLoadGravity

## VB6 Procedure

Function DeleteLoadGravity(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the area object specified by the Name item.

If this item is Group, the load assignments are deleted for all area objects in the group specified by the Name item.

If this item is SelectedObjects,the load assignments are deleted for all selected area objects, and the Name item is ignored.

## Remarks

This function deletes the gravity load assignments to the specified area objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObjectGravityLoad()
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

   'assign area object gravity loads
      ret = SapModel.AreaObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'delete area object gravity load
      ret = SapModel.AreaObj.DeleteLoadGravity("3", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Area_Object}.htm)

[SetLoadGravity](SetLoadGravity_{Area_Object}.htm)



## DeleteLoadPorePressure {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/DeleteLoadPorePressure_{Area_Object}.htm`*

# DeleteLoadPorePressure

## Syntax

SapObject.SapModel.AreaObj.DeleteLoadPorePressure

## VB6 Procedure

Function DeleteLoadPorePressure(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the area object specified by the Name item.

If this item is Group, the load assignments are deleted for all area objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected area objects, and the Name item is ignored.

## Remarks

This function deletes the pore pressure load assignments to the specified area objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObjectPorePressureLoad()
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

   'assign area object pore pressure load
      ret = SapModel.AreaObj.SetLoadPorePressure("ALL", "DEAD", .1, , , Group)

   'delete area object pore pressure load
      ret = SapModel.AreaObj.DeleteLoadPorePressure("3", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadPorePressure](GetLoadPorePressure_{Area_Object}.htm)

[SetLoadPorePressure](SetLoadPorePressure_{Area_Object}.htm)



## DeleteLoadRotate

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/DeleteLoadRotate.htm`*

# DeleteLoadRotate

## Syntax

SapObject.SapModel.AreaObj.DeleteLoadRotate

## VB6 Procedure

Function DeleteLoadRotate(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the area object specified by the Name item.

If this item is Group, the load assignments are deleted for all area objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected area objects, and the Name item is ignored.

## Remarks

This function deletes the rotate load assignments to the specified area objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObjectRotateLoad()
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

   'assign area object rotate load
      ret = SapModel.AreaObj.SetLoadRotate("ALL", "DEAD", 30, , Group)

   'delete area object rotate load
      ret = SapModel.AreaObj.DeleteLoadRotate("3", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadRotate](GetLoadRotate_{Area_Object}.htm)

[SetLoadRotate](SetLoadRotate.htm)



## DeleteLoadSurfacePressure {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/DeleteLoadSurfacePressure_{Area_Object}.htm`*

# DeleteLoadSurfacePressure

## Syntax

SapObject.SapModel.AreaObj.DeleteLoadSurfacePressure

## VB6 Procedure

Function DeleteLoadSurfacePressure(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the area object specified by the Name item.

If this item is Group, the load assignments are deleted for all area objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected area objects, and the Name item is ignored.

## Remarks

This function deletes the surface pressure load assignments to the specified area objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObjectSurfacePressureLoad()
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

   'assign area object surface pressure load
      ret = SapModel.AreaObj.SetLoadSurfacePressure("ALL", "DEAD", -1, .1, , , Group)

   'delete area object surface pressure load
      ret = SapModel.AreaObj.DeleteLoadSurfacePressure("3", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadSurfacePressure](GetLoadSurfacePressure_{Area_Object}.htm)

[SetLoadSurfacePressure](SetLoadSurfacePressure_{Area_Object}.htm)



## DeleteLoadTemperature {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/DeleteLoadTemperature_{Area_Object}.htm`*

# DeleteLoadTemperature

## Syntax

SapObject.SapModel.AreaObj.DeleteLoadTemperature

## VB6 Procedure

Function DeleteLoadTemperature(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the area object specified by the Name item.

If this item is Group, the load assignments are deleted for all area objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected area objects, and the Name item is ignored.

## Remarks

This function deletes the temperature load assignments to the specified area objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObjectTemperatureLoad()
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

   'assign area object temperature load
      ret = SapModel.AreaObj.SetLoadTemperature("All", "DEAD", 1, 50, , , Group)

   'delete area object temperature load
      ret = SapModel.AreaObj.DeleteLoadTemperature("3", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTemperature](GetLoadTemperature_{Area_Object}.htm)

[SetLoadTemperature](SetLoadTemperature_{Area_Object}.htm)



## DeleteLoadUniform

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/DeleteLoadUniform.htm`*

# DeleteLoadUniform

## Syntax

SapObject.SapModel.AreaObj.DeleteLoadUniform

## VB6 Procedure

Function DeleteLoadUniform(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the area object specified by the Name item.

If this item is Group, the load assignments are deleted for all area objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected area objects, and the Name item is ignored.

## Remarks

This function deletes the uniform load assignments to the specified area objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObjectUniformLoad()
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

   'assign area object uniform loads
      ret = SapModel.AreaObj.SetLoadUniform("ALL", "DEAD", -0.01, 2, False, "Local", Group)

   'delete area object uniform load
      ret = SapModel.AreaObj.DeleteLoadUniform("3", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadUniform](GetLoadUniform_{Area_Object}.htm)

[SetLoadUniform](SetLoadUniform.htm)



## DeleteLoadUniformToFrame

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/DeleteLoadUniformToFrame.htm`*

# DeleteLoadUniformToFrame

## Syntax

SapObject.SapModel.AreaObj.DeleteLoadUniformToFrame

## VB6 Procedure

Function DeleteLoadUniformToFrame(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the area object specified by the Name item.

If this item is Group, the load assignments are deleted for all area objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected area objects, and the Name item is ignored.

## Remarks

This function deletes the uniform to frame load assignments to the specified area objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObjectUniformToFrameLoad()
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
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 288, 2, 288)

   'assign area object uniform to frame loads
      ret = SapModel.AreaObj.SetLoadUniformToFrame("ALL", "DEAD", 0.01, 10, 2, False, "Global", Group)

   'delete area object uniform to frame load
      ret = SapModel.AreaObj.DeleteLoadUniformToFrame("8", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadUniformToFrame](GetLoadUniformToFrame.htm)

[SetLoadUniformToFrame](SetLoadUniformToFrame.htm)



## DeleteLoadWindPressure

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/DeleteLoadWindPressure.htm`*

# DeleteLoadWindPressure

## Syntax

SapObject.SapModel.AreaObj.DeleteLoadWindPressure

## VB6 Procedure

Function DeleteLoadWindPressure(ByVal Name As String,
ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object)
As Long

## Parameters

Name

The name of an existing area object or group, depending
on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType
enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted
for the area object specified by the Name item.

If this item is Group, the load assignments are deleted
for all area objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments
are deleted for all selected area objects, and the Name item is ignored.

## Remarks

This function deletes the wind pressure load assignments
to the specified area objects for the specified load pattern.

The function returns zero if the load assignments are
successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObjectWindPressureLoad()
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
      ret = SapModel.File.NewWall(2, 48,
2, 48)

   'assign area object wind pressure load
      ret = SapModel.AreaObj.SetLoadWindPressure("ALL",
"DEAD", 1, 0.8, Group)

   'delete area object wind pressure load
      ret = SapModel.AreaObj.DeleteLoadWindPressure("3",
"DEAD")

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

## See Also

[GetLoadWindPressure\_1](GetLoadWindPressure_1.htm)

[SetLoadWindPressure\_1](SetLoadWindPressure_1.htm)



## DeleteMass {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/DeleteMass_{Area_Object}.htm`*

# DeleteMass

## Syntax

SapObject.SapModel.AreaObj.DeleteMass

## VB6 Procedure

Function DeleteMass(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the mass assignments are deleted for the area object specified by the Name item.

If this item is Group, the mass assignments are deleted for all area objects in the group specified by the Name item.

If this item is SelectedObjects, the mass assignments are deleted for all selected area objects, and the Name item is ignored.

## Remarks

This function deletes the mass assignments for area objects.

The function returns zero if the mass assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObjectMass()
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

   'assign area object mass
      ret = SapModel.AreaObj.SetMass("ALL", .0001, False, Group)

   'delete area object mass
      ret = SapModel.AreaObj.DeleteMass("1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMass](GetMass_{Area_Object}.htm)

[SetMass](SetMass_{Area_Object}.htm)



## DeleteModifiers {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/DeleteModifiers_{Area_Object}.htm`*

# DeleteModifiers

## Syntax

SapObject.SapModel.AreaObj.DeleteModifiers

## VB6 Procedure

Function DeleteModifiers(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the modifier assignments are deleted for the area object specified by the Name item.

If this item is Group, the modifier assignments are deleted for all area objects in the group specified by the Name item.

If this item is SelectedObjects, the modifier assignments are deleted for all selected area objects, and the Name item is ignored.

## Remarks

This function deletes the modifier assignments for area objects.

The function returns zero if the modifier assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObjectsModifiers()
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

   'assign modifiers
      ReDim Value(9)
      For i = 0 To 9
         Value(i) = 1
      Next i
      Value(0) = 0.01
      ret = SapModel.AreaObj.SetModifiers("ALL", Value, Group)

   'delete modifiers
      ret = SapModel.AreaObj.DeleteModifiers("3")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetModifiers](GetModifiers_{Area_Object}.htm)

[SetModifiers](SetModifiers_{Area_Object}.htm)



## DeleteSpring {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/DeleteSpring_{Area_Object}.htm`*

# DeleteSpring

## Syntax

SapObject.SapModel.AreaObj.DeleteSpring

## VB6 Procedure

Function DeleteSpring(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the spring assignments are deleted for the area object specified by the Name item.

If this item is Group, the spring assignments are deleted for all area objects in the group specified by the Name item.

If this item is SelectedObjects, the spring assignments are deleted for all selected area objects, and the Name item is ignored.

## Remarks

This function deletes all spring assignments for the specified area objects.

The function returns zero if the assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObjectSprings()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign springs to area objects
      ReDim Vec(2)
      ret = SapModel.AreaObj.SetSpring("ALL", 1, 1, 1, "", -1, 1, 3, True, Vec, 0, False, "Local", Group)

   'delete springs
      ret = SapModel.AreaObj.DeleteSpring("3")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Area_Object}.htm)

[SetSpring](SetSpring_{Area_Object}.htm)



## Delete {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/Delete_{Area_Object}.htm`*

# Delete

## Syntax

SapObject.SapModel.AreaObj.Delete

## VB6 Procedure

Function Delete(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the area object specified by the Name item is deleted.

If this item is Group, all of the area objects in the group specified by the Name item are deleted.

If this item is SelectedObjects, all of the selected area objects are deleted, and the Name item is ignored.

## Remarks

The function deletes area objects.

The function returns zero if the area objects are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAreaObj()
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

   'delete area object
      ret = SapModel.AreaObj.Delete("4")

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

[AddByCoord](AddByCoord_{Area_Object}.htm)

[AddByPoint](AddByPoint_{Area_Object}.htm)



## GetAutoMesh_1 {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetAutoMesh_1_{Area_Object}.htm`*

# GetAutoMesh\_1

## Syntax

SapObject.SapModel.AreaObj.GetAutoMesh\_1

## VB6 Procedure

Function GetAutoMesh\_1(ByVal Name As String, ByRef MeshType As Long, ByRef n1 As Long, ByRef n2 As Long, ByRef MaxSize1 As Double, ByRef MaxSize2 As Double, ByRef PointOnEdgeFromLine As Boolean, ByRef PointOnEdgeFromPoint As Boolean, ByRef ExtendCookieCutLines As Boolean, ByRef Rotation As Double, ByRef MaxSizeGeneral As Double, ByRef LocalAxesOnEdge As Boolean, ByRef LocalAxesOnFace As Boolean, ByRef RestraintsOnEdge As Boolean, ByRef RestraintsOnFace As Boolean, ByRef Group As String, ByRef SubMesh As Boolean, ByRef SubMeshSize As Double, ByRef UseUserMesh As Boolean, ByRef QuadsOnlyGeneral As Boolean) As Long

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

UseUserMesh

If this item is True, the user mesh, if assigned, will be used for analysis, otherwise the auto mesh option will be used.

QuadsOnlyGeneral

If this item is True, the general mesh will be generated with quadrilateral areas only, otherwise the mesh may include triangles as necessary. This only applies when MeshType = 6.

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
      Dim QuadsOnlyGeneral As Boolean

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
      ret = SapModel.AreaObj.SetAutoMesh\_1("ALL", 1, 3, 3, , , , , , , , , , , , , , , True, False, Group)

   'get auto mesh options for area object
      ret = SapModel.AreaObj.GetAutoMesh\_1("1", MeshType, n1, n2, MaxSize1, MaxSize2, PointOnEdgeFromLine, PointOnEdgeFromPoint, ExtendCookieCutLines, Rotation, MaxSizeGeneral, LocalAxesOnEdge, LocalAxesOnFace, RestraintsOnEdge, RestraintsOnFace, MyGroup, SubMesh, SubMeshSize, UseUserMesh, QuadsOnlyGeneral)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 27.0.0

This function supersedes [GetAutoMesh {Area Object}](../../Obsolete_Functions/GetAutoMesh_{Area_Object}.htm)

## See Also

[SetAutoMesh \_1{Area Object}](SetAutoMesh__1{Area_Object}.htm)



## GetEdgeConstraint {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetEdgeConstraint_{Area_Object}.htm`*

# GetEdgeConstraint

## Syntax

SapObject.SapModel.AreaObj.GetEdgeConstraint

## VB6 Procedure

Function GetEdgeConstraint(ByVal Name As String, ByRef ConstraintExists As Boolean) As Long

## Parameters

Name

The name of an existing area object.

ConstraintExists

This item is True if an automatic edge constraint is generated by the program for the area object in the analysis model.

## Remarks

This function retrieves the generated edge constraint assignments to area objects.

The function returns zero if the assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjEdgeConstraint()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign auto edge constraint option
      ret = SapModel.AreaObj.SetEdgeConstraint("ALL", True, Group)

   'get auto edge constraint option
      ret = SapModel.AreaObj.GetEdgeConstraint("1", ConstraintExists)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetEdgeConstraint](SetEdgeConstraint_{Area_Object}.htm)



## GetElm {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetElm_{Area_Object}.htm`*

# GetElm

## Syntax

SapObject.SapModel.AreaObj.GetElm

## VB6 Procedure

Function GetElm(ByVal Name As String, ByRef nelm As Long, ByRef Elm() as String) As Long

## Parameters

Name

The name of an existing area object.

nelm

The number of area elements created from the specified area object.

Elm

An array that includes the name of a area element created from the specified area object.

## Remarks

This function retrieves the names of the area elements (analysis model area) associated with a specified area object in the object-based model.

This function returns zero if the area element information is successfully returned; otherwise it returns nonzero. An error occurs if the analysis model does not currently exist.

## VBA Example

Sub GetAreaElementInfoForAreaObject()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'create the analysis model
      ret = SapModel.Analyze.CreateAnalysisModel

   'get area element information
      ret = SapModel.AreaObj.GetElm("1", nelm, Elm)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetGUID {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetGUID_{Area_Object}.htm`*

# GetGUID

## Syntax

SapObject.SapModel.AreaObj.GetGUID

## VB6 Procedure

Function GetGUID(ByVal name As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing area object.

GUID

The GUID (Global Unique ID) for the specified area object.

## Remarks

This function retrieves the GUID for the specified area object.

This function returns zero if the area object GUID is successfully retrieved; otherwise, it returns nonzero.

## VBA Example

Sub GetAreaObjGUID()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'set program created GUID
      ret = SapObject.SapModel.AreaObj.SetGUID("1")

   'get GUID
      ret = SapObject.SapModel.AreaObj.GetGUID("1", GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetGUID](SetGUID_{Area_Object}.htm)



## GetGroupAssign {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetGroupAssign_{Area_Object}.htm`*

# GetGroupAssign

## Syntax

SapObject.SapModel.AreaObj.GetGroupAssign

## VB6 Procedure

Function GetGroupAssign(ByVal Name As String, ByRef NumberGroups As Long, ByRef Groups() As String)  As Long

## Parameters

Name

The name of an existing area object.

NumberGroups

The number of group names retrieved.

Groups

The names of the groups to which the area object is assigned.

## Remarks

This function retrieves the names of the groups to which a specified area object is assigned.

The function returns zero if the group assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectGroups()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'define new groups
      ret = SapModel.GroupDef.SetGroup("Group1")
      ret = SapModel.GroupDef.SetGroup("Group2")

   'add area object to groups
      ret = SapModel.AreaObj.SetGroupAssign("1", "Group1")
      ret = SapModel.AreaObj.SetGroupAssign("1", "Group2")

   'get area object groups
      ret = SapModel.AreaObj.GetGroupAssign("1", NumberGroups, Groups)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.0.0.

## See Also

[SetGroupAssign](SetGroupAssign_{Area_Object}.htm)



## GetLoadGravity {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetLoadGravity_{Area_Object}.htm`*

# GetLoadGravity

## Syntax

SapObject.SapModel.AreaObj.GetLoadGravity

## VB6 Procedure

Function GetLoadGravity(ByVal Name As String, ByRef NumberItems As Long, ByRef AreaName() As String, ByRef LoadPat() As String, ByRef CSys() As String, ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

NumberItems

The total number of gravity loads retrieved for the specified area objects.

AreaName

This is an array that includes the name of the area object associated with each gravity load.

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

If this item is Object, the assignments are retrieved for the area object specified by the Name item.

If this item is Group, the assignments are retrieved for all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected area objects, and the Name item is ignored.

## Remarks

This function retrieves the gravity load assignments to area objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectGravityLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim AreaName() As String
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign area object gravity loads
      ret = SapModel.AreaObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'get area object gravity load
      ret = SapModel.AreaObj.GetLoadGravity("3", NumberItems, AreaName, LoadPat, CSys, x, y, z)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadGravity](SetLoadGravity_{Area_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Area_Object}.htm)



## GetLoadPorePressure {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetLoadPorePressure_{Area_Object}.htm`*

# GetLoadPorePressure

## Syntax

SapObject.SapModel.AreaObj.GetLoadPorePressure

## VB6 Procedure

Function GetLoadPorePressure(ByVal Name As String, ByRef NumberItems As Long, ByRef AreaName() As String, ByRef LoadPat() As String, ByRef Value() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

NumberItems

The total number of pore pressure loads retrieved for the specified area objects.

AreaName

This is an array that includes the name of the area object associated with each pore pressure load.

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

If this item is Object, the assignments are retrieved for the area object specified by the Name item.

If this item is Group, the assignments are retrieved for all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected area objects, and the Name item is ignored.

## Remarks

This function retrieves the pore pressure load assignments to area objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectPorePressureLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim AreaName() As String
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign area object pore pressure load
      ret = SapModel.AreaObj.SetLoadPorePressure("ALL", "DEAD", .1, , , Group)

   'get area object pore pressure load
      ret = SapModel.AreaObj.GetLoadPorePressure("ALL", NumberItems, AreaName, LoadPat, Value, PatternName, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadPorePressure](SetLoadPorePressure_{Area_Object}.htm)

[DeleteLoadPorePressure](DeleteLoadPorePressure_{Area_Object}.htm)



## GetLoadRotate {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetLoadRotate_{Area_Object}.htm`*

# GetLoadRotate

## Syntax

SapObject.SapModel.AreaObj.GetLoadRotate

## VB6 Procedure

Function GetLoadRotate(ByVal Name As String, ByRef NumberItems As Long, ByRef AreaName() As String, ByRef LoadPat() As String, ByRef Value() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

NumberItems

The total number of rotate loads retrieved for the specified area objects.

AreaName

This is an array that includes the name of the area object associated with each rotate load.

LoadPat

This is an array that includes the name of the load pattern associated with each rotate load.

Value

This is an array that includes the angular velocity value. [Cyc/T]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the area object specified by the Name item.

If this item is Group, the assignments are retrieved for all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected area objects, and the Name item is ignored.

## Remarks

This function retrieves the rotate load assignments to area objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectRotateLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim AreaName() As String
      Dim LoadPat() As String
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

   'assign area object rotate load
      ret = SapModel.AreaObj.SetLoadRotate("ALL", "DEAD", 30, , Group)

   'get area object rotate load
      ret = SapModel.AreaObj.GetLoadRotate("ALL", NumberItems, AreaName, LoadPat, Value, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadRotate](SetLoadRotate.htm)

[DeleteLoadRotate](GetLoadRotate_{Area_Object}.htm)



## GetLoadStrain {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetLoadStrain_{Area_Object}.htm`*

# GetLoadStrain

## Syntax

SapObject.SapModel.AreaObj.GetLoadStrain

## VB6 Procedure

Function GetLoadStrain(ByVal Name As String, ByRef NumberItems As Long, ByRef AreaName() As String, ByRef LoadPat() As String, ByRef Component() As Long, ByRef Value() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

NumberItems

The total number of strain loads retrieved for the specified area objects.

AreaName

This is an array that includes the name of the area object associated with each strain load.

LoadPat

This is an array that includes the name of the load pattern associated with each strain load.

Component

This is an array that includes 1, 2, 3, 4, 5, 6, 7, 8, or 9, indicating the component associated with each strain load.

1 = Strain11

2 = Strain22

3 = Strain12

4 = Curvature11

5 = Curvature22

6 = Curvature12

7 = Strain13

8 = Strain23

9 = Strain33

Value

This is an array that includes the strain value. [L/L] for Component = 1, 2, 3, 7, 8, and 9, and [1/L] for Component = 4, 5 and 6

PatternName

This is an array that includes the joint pattern name, if any, used to specify the strain load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the area object specified by the Name item.

If this item is Group, the assignments are retrieved for all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected area objects, and the Name item is ignored.

## Remarks

This function retrieves the strain load assignments to area objects.

The function returns zero if the strain load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectStrainLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim AreaName() As String
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign area object strain load
      ret = SapModel.AreaObj.SetLoadStrain("ALL", "DEAD", 1, 0.001, , , Group)

   'get area object strain load
      ret = SapModel.AreaObj.GetLoadStrain("3", NumberItems, AreaName, LoadPat, Component, Value, PatternName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

Added Strain33 component in v19.0.0.

## See Also

[SetLoadStrain](SetLoadStrain_{Area_Object}.htm)

[DeleteLoadStrain](DeleteLoadStrain_{Area_Object}.htm)



## GetLoadSurfacePressure {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetLoadSurfacePressure_{Area_Object}.htm`*

# GetLoadSurfacePressure

## Syntax

SapObject.SapModel.AreaObj.GetLoadSurfacePressure

## VB6 Procedure

Function GetLoadSurfacePressure(ByVal Name As String, ByRef NumberItems As Long, ByRef AreaName() As String, ByRef LoadPat() As String, ByRef Face() As Long, ByRef Value() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

NumberItems

The total number of surface pressure loads retrieved for the specified area objects.

AreaName

This is an array that includes the name of the area object associated with each surface pressure load.

LoadPat

This is an array that includes the name of the load pattern associated with each surface pressure load.

Face

This is an array that includes either -1, -2 or a nonzero, positive integer, indicating the area object face to which the specified load assignment applies.

-1 = Bottom face

-2 = Top face

>0 = Edge face

Note that edge face n is from area object point n to area object point n + 1. For example, edge face 2 is from area object point 2 to area object point 3.

Value

This is an array that includes the surface pressure load value. [F/L2]

PatternName

This is an array that includes the joint pattern name, if any, used to specify the surface pressure load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the area object specified by the Name item.

If this item is Group, the assignments are retrieved for all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected area objects, and the Name item is ignored.

## Remarks

This function retrieves the surface pressure load assignments to area objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectSurfacePressureLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim AreaName() As String
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign area object surface pressure load
      ret = SapModel.AreaObj.SetLoadSurfacePressure("ALL", "DEAD", -1, .1, , , Group)

   'get area object surface pressure load
      ret = SapModel.AreaObj.GetLoadSurfacePressure("ALL", NumberItems, AreaName, LoadPat, Face, Value, PatternName, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadSurfacePressure](SetLoadSurfacePressure_{Area_Object}.htm)

[DeleteLoadSurfacePressure](DeleteLoadSurfacePressure_{Area_Object}.htm)



## GetLoadTemperature {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetLoadTemperature_{Area_Object}.htm`*

# GetLoadTemperature

## Syntax

SapObject.SapModel.AreaObj.GetLoadTemperature

## VB6 Procedure

Function GetLoadTemperature(ByVal Name As String, ByRef NumberItems As Long, ByRef AreaName() As String, ByRef LoadPat() As String, ByRef MyType() As Long, ByRef Value() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

NumberItems

The total number of temperature loads retrieved for the specified area objects.

AreaName

This is an array that includes the name of the area object associated with each temperature load.

LoadPat

This is an array that includes the name of the load pattern associated with each temperature load.

MyType

This is an array that includes either 1 or 3, indicating the type of temperature load.

1 = Temperature

3 = Temperature gradient along local 3 axis

Value

This is an array that includes the temperature load value. [T] for MyType= 1 and [T/L] for MyType= 3

PatternName

This is an array that includes the joint pattern name, if any, used to specify the temperature load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the area object specified by the Name item.

If this item is Group, the assignments are retrieved for all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected area objects, and the Name item is ignored.

## Remarks

This function retrieves the temperature load assignments to area objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectTemperatureLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim AreaName() As String
      Dim LoadPat() As String
      Dim MyType() As Long
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign area object temperature load
      ret = SapModel.AreaObj.SetLoadTemperature("All", "DEAD", 1, 50, , , Group)

   'get area object temperature load
      ret = SapModel.AreaObj.GetLoadTemperature("ALL", NumberItems, AreaName, LoadPat, MyType, Value, PatternName, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadTemperature](SetLoadTemperature_{Area_Object}.htm)

[DeleteLoadTemperature](DeleteLoadTemperature_{Area_Object}.htm)



## GetLoadUniformToFrame

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetLoadUniformToFrame.htm`*

# GetLoadUniformToFrame

## Syntax

SapObject.SapModel.AreaObj.GetLoadUniformToFrame

## VB6 Procedure

Function GetLoadUniformToFrame(ByVal Name As String,
ByRef NumberItems As Long, ByRef AreaName() As String, ByRef LoadPat()
As String, ByRef CSys() As String, ByRef Dir() As Long, ByRef Value()
As Double, ByRef DistType As Long,Optional ByVal ItemType As eItemType
= Object) As Long

## Parameters

Name

The name of an existing area object or group, depending
on the value of the ItemType item.

NumberItems

The total number of uniform loads retrieved
for the specified area objects.

AreaName

This is an array that includes the name of the area
object associated with each uniform load.

LoadPat

This is an array that includes the name of the coordinate
system in which the uniform load is specified.

CSys

This is an array that includes the name of the coordinate
system associated with each uniform load.

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

7 = Projected X direction
(does not apply when CSys is Local)

8 = Projected Y direction
(does not apply when CSys is Local)

9 = Projected Z direction
(does not apply when CSys is Local)

10 = Gravity direction
(only applies when CSys is Global)

11 = Projected Gravity
direction (only applies when CSys is Global)

The positive gravity direction (see Dir = 10 and 11)
is in the negative Global Z direction.

Value

The uniform load value. [F/L2]

DistType

This is either 1 or 2, indicating the load distribution
type.

1 = One-way load distribution

2 = Two-way load distribution

One-way distribution is parallel to the area object
local 1 axis. Two-way distribution is parallel to the area object local
1 and 2 axes.

ItemType

This is one of the following items in the eItemType
enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved
for the area object specified by the Name item.

If this item is Group, the assignments are retrieved
for all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved
for all selected area objects, and the Name item is ignored.

## Remarks

This function retrieves the uniform to frame load assignments
to area objects.

The function returns zero if the load assignments are
successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectUniformToFrameLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim AreaName() As String
      Dim LoadPat() As String
      Dim CSys() As String
      Dim Dir() As Long
      Dim Value() As Double
      Dim DistType() As Long

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
2, 144, 3, 288, 2, 288)

   'assign area object uniform to frame loads
      ret = SapModel.AreaObj.SetLoadUniformToFrame("ALL",
"DEAD", 0.01, 10, 2, False, "Global", Group)

   'get area object uniform to frame load
      ret = SapModel.AreaObj.GetLoadUniformToFrame("3",
NumberItems, AreaName, LoadPat, CSys, Dir, Value, DistType)

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

## See Also

[SetLoadUniformToFrame](SetLoadUniformToFrame.htm)

[DeleteLoadUniformToFrame](DeleteLoadUniformToFrame.htm)



## GetLoadUniform {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetLoadUniform_{Area_Object}.htm`*

# GetLoadUniform

## Syntax

SapObject.SapModel.AreaObj.GetLoadUniform

## VB6 Procedure

Function GetLoadUniform(ByVal Name As String, ByRef NumberItems As Long, ByRef AreaName() As String, ByRef LoadPat() As String, ByRef CSys() As String, ByRef Dir() As Long, ByRef Value() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

NumberItems

The total number of uniform loads retrieved for the specified area objects.

AreaName

This is an array that includes the name of the area object associated with each uniform load.

LoadPat

This is an array that includes the name of the coordinate system in which the uniform load is specified.

CSys

This is an array that includes the name of the coordinate system associated with each uniform load.

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

Value

The uniform load value. [F/L2]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the area object specified by the Name item.

If this item is Group, the assignments are retrieved for all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected area objects, and the Name item is ignored.

## Remarks

This function retrieves the uniform load assignments to area objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectUniformLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim AreaName() As String
      Dim LoadPat() As String
      Dim CSys() As String
      Dim Dir() As Long
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

   'assign area object uniform loads
      ret = SapModel.AreaObj.SetLoadUniform("ALL", "DEAD", -0.01, 2, False, "Local", Group)

   'get area object uniform load
      ret = SapModel.AreaObj.GetLoadUniform("3", NumberItems, AreaName, LoadPat, CSys, Dir, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadUniform](SetLoadUniform.htm)

[DeleteLoadUniform](DeleteLoadUniform.htm)



## GetLoadWindPressure_1

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetLoadWindPressure_1.htm`*

# GetLoadWindPressure\_1

## Syntax

SapObject.SapModel.AreaObj.GetLoadWindPressure\_1

## VB6 Procedure

Function GetLoadWindPressure(ByVal Name As String, ByRef NumberItems As Long, ByRef AreaName() As String, ByRef LoadPat() As String, ByRef MyType() As Long, ByRef Cp() As Double, ByRef DistributionType() As Long, Optional ByVal ItemType As eItemType = Object) As Long

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

DistributionType

This is either 1 or 2, indicating the distribution type.

1 = To Joints
2 = To Frames – One-way
3 = To Frames – Two-way

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
      Dim DistributionType() As Long

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
      ret = SapModel.AreaObj.SetLoadWindPressure("ALL", "DEAD", 1, 0.8, 1, Group)

   'get area object wind pressure load
      ret = SapModel.AreaObj.GetLoadWindPressure("ALL", NumberItems, AreaName, LoadPat, MyType, Cp, DistributionType, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.1.0.

## See Also

[SetLoadWindPressure\_1](SetLoadWindPressure_1.htm)

[DeleteLoadWindPressure](DeleteLoadWindPressure.htm)



## GetLocalAxesAdvanced {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetLocalAxesAdvanced_{Area_Object}.htm`*

# GetLocalAxesAdvanced

## Syntax

SapObject.SapModel.AreaObj.GetLocalAxesAdvanced

## VB6 Procedure

Function GetLocalAxesAdvanced(ByVal Name As String, ByRef Active As Boolean, ByRef Plane2 As Long, ByRef PlVectOpt As Long, ByRef PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double) As Long

## Parameters

Name

The name of an existing area object.

Active

This is True if advanced local axes exist.

Plane2

This is 31 or 32, indicating that the local plane determined by the plane reference vector is the 3-1 plane or the 3-2 plane. This item applies only when the Active item is True.

PlVectOpt

This is 1, 2, or 3, indicating the plane reference vector option. This item applies only when the Active item is True.

1 = Coordinate direction

2 = Two joints

3 = User vector

PlCSys

The coordinate system used to define the plane reference vector coordinate directions and the plane user vector. This item applies when the Active item is True and the PlVectOpt item is 1 or 3.

PlDir

This is an array dimensioned to 1 (2 integers) indicating the plane reference vector primary and secondary coordinate directions, PlDir(0) and PlDir(1) respectively, taken at the object center in the specified coordinate system and used to determine the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 1. Possible coordinate direction values are:

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

This is an array dimensioned to 1 (2 strings) indicating the labels of two joints that define the plane reference vector. Either of these joints may be specified as None to indicate the center of the specified object.  If both joints are specified as None, they are not used to define the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 2.

PlVect

This is an array dimensioned to 2 (3 doubles) that defines the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 3.

## Remarks

This function retrieves the advanced local axes assignments to area objects.

The function returns zero if the advanced local axes assignments are  retrieved successfully; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaAdvancedLocalAxes()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign area advanced local axes
      MyPlDir(0) = 2
      MyPlDir(1) = 3
      ret = SapModel.AreaObj.SetLocalAxesAdvanced("3", True, 31, 1, "Global", MyPlDir, MyPlPt, MyPlVect)

   'get area object local axis angle
      ret = SapModel.AreaObj.GetLocalAxes("3", Ang, Advanced)

   'get area advanced local axes data
      If Advanced Then
         ret = SapModel.AreaObj.GetLocalAxesAdvanced("3", Active, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect)
      End If

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

## See Also

[SetLocalAxesAdvanced](SetLocalAxesAdvanced.htm)

[SetLocalAxes](SetLocalAxes_{Area_Object}.htm)

[GetLocalAxes](GetLocalAxes_{Area_Object}.htm)



## GetLocalAxes {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetLocalAxes_{Area_Object}.htm`*

# GetLocalAxes

## Syntax

SapObject.SapModel.AreaObj.GetLocalAxes

## VB6 Procedure

Function GetLocalAxes(ByVal Name As String, ByRef Ang As Double, ByRef Advanced As Boolean) As Long

## Parameters

Name

The name of an existing area object.

Ang

This is the angle that the local 1 and 2 axes are rotated about the positive local 3 axis from the default orientation. The rotation for a positive angle appears counter clockwise when the local +3 axis is pointing toward you. [deg]

Advanced

This item is True if the area object local axes orientation was obtained using advanced local axes parameters.

## Remarks

This function retrieves the local axis angle assignment for area objects.

The function returns zero if the assignment is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectLocalAxisAngle()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'get area object local axis angle
      ret = SapModel.AreaObj.GetLocalAxes("3", Ang, Advanced)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetLocalAxes](SetLocalAxes_{Area_Object}.htm)



## GetMass {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetMass_{Area_Object}.htm`*

# GetMass

## Syntax

SapObject.SapModel.AreaObj.GetMass

## VB6 Procedure

Function GetMass(ByVal Name As String, ByRef MassOverL2 As Double) As Long

## Parameters

Name

The name of an existing area object.

MassOverL2

The mass per unit area assigned to the area object. [M/L2]

## Remarks

This function retrieves the mass per unit area assignment for area objects.

The function returns zero if the mass assignment is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectMass()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MassOverL2 As Double

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

   'assign area object mass
      ret = SapModel.AreaObj.SetMass("ALL", .0001, False, Group)

   'get area object mass assignment
      ret = SapModel.AreaObj.GetMass("1", MassOverL2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMass](SetMass_{Area_Object}.htm)

[DeleteMass](DeleteMass_{Area_Object}.htm)



## GetMatTemp {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetMatTemp_{Area_Object}.htm`*

# GetMatTemp

## Syntax

SapObject.SapModel.AreaObj.GetMatTemp

## VB6 Procedure

Function GetMatTemp(ByVal Name As String, ByRef Temp As Double, ByRef PatternName As String) As Long

## Parameters

Name

The name of an existing area object.

Temp

This is the material temperature value assigned to the area object. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the material temperature for the area object is uniform over the object at the value specified by Temp.

If PatternName is the name of a defined joint pattern, the material temperature for the area object may vary. The material temperature at each corner point around the area object perimeter is equal to the specified temperature multiplied by the pattern value at the associated point object. The material temperature at other points in the area object is calculated by interpolation from the corner points.

## Remarks

This function retrieves the material temperature assignments to area objects.

The function returns zero if the material temperature assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectMatTemp()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign material temperature
      ret = SapModel.AreaObj.SetMatTemp("ALL", 50, , Group)

   'get material temperature
      ret = SapModel.AreaObj.GetMatTemp("3", Temp, PatternName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMatTemp](SetMatTemp_{Area_Object}.htm)



## GetMaterialOverwrite {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetMaterialOverwrite_{Area_Object}.htm`*

# GetMaterialOverwrite

## Syntax

SapObject.SapModel.AreaObj.GetMaterialOverwrite

## VB6 Procedure

Function GetMaterialOverwrite(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a defined area object.

PropName

This is None, indicating that no material overwrite exists for the specified area object, or it is the name of an existing material property.

## Remarks

This function retrieves the material overwrite assigned to an area object, if any. The material property name is indicated as None if there is no material overwrite assignment.

The function returns zero if the material overwrite assignment is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaMaterialOverwrite()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign material overwrite
      ret = SapModel.AreaObj.SetMaterialOverwrite("3", "A992Fy50")

   'get material overwrite assignment
      ret = SapModel.AreaObj.GetMaterialOverwrite("3", PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMaterialOverwrite](SetMaterialOverwrite_{Area_Object}.htm)



## GetModifiers {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetModifiers_{Area_Object}.htm`*

# GetModifiers

## Syntax

SapObject.SapModel.AreaObj.GetModifiers

## VB6 Procedure

Function GetModifiers(ByVal Name As String, ByRef Value() As Double) As Long

## Parameters

Name

The name of an existing area object.

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

This function retrieves the modifier assignment for area objects. The default value for all modifiers is one.

The function returns zero if the modifier assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectModifiers()
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

   'assign modifiers
      ReDim Value(9)
      For i = 0 To 9
         Value(i) = 1
      Next i
      Value(0) = 0.01
      ret = SapModel.AreaObj.SetModifiers("ALL", Value, Group)

   'get modifiers
      ReDim Value(9)
      ret = SapModel.AreaObj.GetModifiers("3", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetModifiers](SetModifiers_{Area_Object}.htm)

[DeleteModifiers](DeleteModifiers_{Area_Object}.htm)



## GetNameList {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetNameList_{Area_Object}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.AreaObj.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of area object names retrieved by the program.

MyName

This is a one-dimensional array of area object names. The MyName array is created as a dynamic, zero-based, array by the API user:

Dim MyName() as String

The array is dimensioned to (NumberNames – 1) inside the Sap2000 program, filled with the names, and returned to the API user.

## Remarks

This function retrieves the names of all defined area objects.

The function returns zero if the names are successfully retrieved, otherwise it returns nonzero.

## VBA Example

Sub GetAreaObjectNames()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'get area object names
      ret = SapModel.AreaObj.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetNotionalSize

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetNotionalSize.htm`*

# GetNotionalSize

## Syntax

SapObject.SapModel.PropArea.GetNotionalSize

## VB6 Procedure

Function GetNotionalSize(ByVal Name As String, ByRef stype As String, ByRef Value As Double) As Long

## Parameters

Name

The name of an existing shell-type area section property.

stype

The type to define the notional size of a section. It can be:

"Auto" = Program will determine the notional size based on the average thickness of an area element.

"User" = The notional size is based on the user-defined value.

"None" = Notional size will not be considered. In other words, the time-dependent effect of this section will not be considered.

Value

For stype is "Auto", the Value represents for the scale factor to the program-determined notional size; for **stype** is “User”, the **Value** represents for the user-defined notional size [L]; for **stype** is “None”, the **Value** will not be used and can be set to 1.

## Remarks

This function retrieves the method to determine the notional size of an area section for the creep and shrinkage calculations. This function is currently worked for shell type area section.

The function returns zero if the parameters are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaPropNotionalSize()
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
   ret = SapModel.File.NewWall(2, 48, 2, 48)

'assign parameters
   stype = “Auto”
   Value = 1.1
   ret = SapModel.PropArea.SetNotionalSize("ASEC1", “Auto”, 1.1)

'get parameters
   ret = SapModel.PropArea.GetNotionalSize("ASEC1", stype, Value)

'close Sap2000
   SapObject.ApplicationExit False
   Set SapModel = Nothing
   Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.1.0

## See Also

[SetNotionalSize](SetNotionalSize.htm)



## GetOffsets {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetOffsets_{Area_Object}.htm`*

# GetOffsets

## Syntax

SapObject.SapModel.AreaObj.GetOffsets

## VB6 Procedure

Function GetOffsets(ByVal Name As String, ByRef OffsetType As Long, ByRef OffsetPattern As String, ByRef OffsetPatternSF As Double, ByRef Offset() As Double) As Long

## Parameters

Name

The name of an existing area object.

OffsetType

This is 0, 1 or 2, indicating the joint offset type.

0 = No joint offsets

1 = User defined joint offsets specified by joint pattern

2 = User defined joint offsets specified by point

OffsetPattern

This item applies only when OffsetType = 1. It is the name of the defined joint pattern that is used to calculate the joint offsets.

OffsetPatternSF

This item applies only when OffsetType = 1. It is the scale factor applied to the joint pattern when calculating the joint offsets. [L]

Offset

This item applies only when OffsetType = 2. It is an array of joint offsets for each of the points that define the area object. [L]

## Remarks

This function retrieves the joint offset assignments for area objects.

The function returns zero if the assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectJointOffsets()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i as long
      Dim OffsetType As Long
      Dim OffsetPattern As String
      Dim OffsetPatternSF As Double
      Dim Offset() As Double

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

   'assign joint offsets
      ReDim Offset(3)
      For i = 0 To 3
         Offset(i) = 12
      Next i
      ret = SapModel.AreaObj.SetOffsets("ALL", 2, "", 1, Offset, Group)

   'get joint offsets
      ret = SapModel.AreaObj.GetOffsets("3", OffsetType, OffsetPattern, OffsetPatternSF, Offset)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetOffsets](SetOffsets.htm)



## GetPoints {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetPoints_{Area_Object}.htm`*

# GetPoints

## Syntax

SapObject.SapModel.AreaObj.GetPoints

## VB6 Procedure

Function GetPoints(ByVal Name As String, ByRef NumberPoints As Long, ByRef Point() As String) As Long

## Parameters

Name

The name of a defined area object.

NumberPoints

The number of point objects that define the area object.

Point

This is an array containing the names of the point objects that define the area object. The point names are in order around the area object.

## Remarks

This function retrieves the names of the point objects that define an area object.

The function returns zero if the point object names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjPoints()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'get names of points
      ret = SapModel.AreaObj.GetPoints("1", NumberPoints, Point)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetProperty {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetProperty_{Area_Object}.htm`*

# GetProperty

## Syntax

SapObject.SapModel.AreaObj.GetProperty

## VB6 Procedure

Function GetProperty(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a defined area object.

PropName

The name of the area property assigned to the area object. This item is None if no area property is assigned to the area object.

## Remarks

This function retrieves the area property assigned to an area object.

The function returns zero if the property is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectProp()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'get area property
      ret = SapModel.AreaObj.GetProperty("1", PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetProperty](SetProperty_{Area_Object}.htm)



## GetSelectedEdge

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetSelectedEdge.htm`*

# GetSelectedEdge

## Syntax

Sap2000.AreaObj.GetSelectedEdge

## VB6 Procedure

Function GetSelectedEdge(ByVal Name As String, ByRef NumberEdges As Long, ByRef Selected() As Boolean) As Long

## Parameters

Name

The name of an existing area object.

NumberEdges

The number of edges in the specified area object.

Selected

This is an array of items that is True if the specified area object edge is selected; otherwise it is False.

Selected(0) = Selected status for edge 1

Selected(1) = Selected status for edge 2

Selected(n) = Selected status for edge (n + 1)

This array is internally dimensioned by Sap2000 to (NumberEdges – 1).

## Remarks

This function retrieves the selected status for area object edges.

The function returns zero if the selected status is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectEdgesSelectedStatus()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberEdges As Long
      Dim Selected() As Boolean

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

   'set area object edge selected
      ret = SapModel.AreaObj.SetSelectedEdge("1", 2, True)
      ret = SapModel.AreaObj.SetSelectedEdge("1", 3, True)

   'get area object edge selected status
      ret = SapModel.AreaObj.GetSelectedEdge("1", NumberEdges, Selected)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSelected](SetSelected_{Area_Object}.htm)

[GetSelected](GetSelected_{Area_Object}.htm)

[SetSelectedEdge](SetSelectedEdge.htm)



## GetSelected {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetSelected_{Area_Object}.htm`*

# GetSelected

## Syntax

Sap2000.AreaObj.GetSelected

## VB6 Procedure

Function GetSelected(ByVal Name As String, ByRef Selected As Boolean) As Long

## Parameters

Name

The name of an existing area object.

Selected

This item is True if the specified area object is selected; otherwise it is False.

## Remarks

This function retrieves the selected status for an area object.

The function returns zero if the selected status is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectSelectedStatus()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'set all area objects selected
      ret = SapModel.AreaObj.SetSelected("ALL", True, Group)

   'get area object selected status
      ret = SapModel.AreaObj.GetSelected("1", Selected)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSelected](SetSelected_{Area_Object}.htm)

[GetSelectedEdge](GetSelectedEdge.htm)

[SetSelectedEdge](SetSelectedEdge.htm)



## GetSpring {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetSpring_{Area_Object}.htm`*

# GetSpring

## Syntax

SapObject.SapModel.AreaObj.GetSpring

## VB6 Procedure

Function GetSpring(ByVal Name As String, ByRef NumberSprings As Long, ByRef MyType() As Long, ByRef s() As Double, ByRef SimpleSpringType() As Long, ByRef LinkProp() As String, ByRef Face() As Long, ByRef SpringLocalOneType() As Long, ByRef Dir() As Long, ByRef Outward() As Boolean, ByRef VecX() As Double, ByRef VecY() As Double, ByRef VecZ() As Double, ByRef CSys() As String, ByRef Ang() As Double) As Long

## Parameters

Name

The name of an existing area object.

NumberSprings

The number of spring assignments made to the specified area object.

MyType

Each value in this array is either 1 or 2, indicating the spring property type.

1 = Simple spring

2 = Link property

s

Each value in this array is the simple spring stiffness per unit area of the specified area object face. This item applies only when the corresponding MyType = 1. [F/L3]

SimpleSpringType

Each value in this array is 1, 2 or 3, indicating the simple spring type. This item applies only when the corresponding MyType = 1.

1 = Spring resists tension and compression

2 = Spring resists compression only

3 = Spring resists tension only

LinkProp

Each value in this array is the name of the link property assigned to the spring. This item applies only when the corresponding MyType = 2.

Face

Each value in this array is -1, -2 or a nonzero, positive integer, indicating the area object face to which the specified spring assignment applies.

-1 = Bottom face

-2 = Top face

>0 = Edge face

Note that edge face n is from area object point n to area object point n + 1. For example, edge face 2 is from area object point 2 to area object point 3.

SpringLocalOneType

Each value in this array is 1, 2 or 3, indicating the method used to specify the spring positive local 1-axis orientation.

1 = Parallel to area object local axis

2 = Normal to specified area object face

3 = User specified direction vector

Dir

Each value in this array is 1, 2, 3, -1, -2 or -3, indicating the area object local axis that corresponds to the positive local 1-axis of the spring. This item applies only when the corresponding SpringLocalOneType = 1.

Outward

Each value in this array is True if the spring positive local 1 axis is outward from the specified area object face. This item applies only when SpringLocalOneType = 2.

VecX

Each value in this array is the X-axis or area object local 1-axis component (depending on the CSys specified) of the user specified direction vector for the spring local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when the corresponding SpringLocalOneType = 3.

VecY

Each value in this array is the Y-axis or area object local 2-axis component (depending on the CSys specified) of the user specified direction vector for the spring local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when the corresponding SpringLocalOneType = 3.

VecZ

Each value in this array is the X-axis or area object local 3-axis component (depending on the CSys specified) of the user specified direction vector for the spring local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when the corresponding SpringLocalOneType = 3.

CSys

Each value in this array is Local (meaning the area object local coordinate system) or the name of a defined coordinate system. This item is the coordinate system in which the user specified direction vector, Vec, is specified. This item applies only when the corresponding SpringLocalOneType = 3.

Ang

Each value in this array is the angle that the link local 2-axis is rotated from its default orientation. This item applies only when the corresponding MyType = 2. [deg]

## Remarks

This function retrieves the spring assignments to an area object face.

The function returns zero if the assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectSprings()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign springs to area objects
      ReDim Vec(2)
      ret = SapModel.AreaObj.SetSpring("ALL", 1, 1, 1, "", -1, 1, 3, True, Vec, 0, False, "Local", Group)

   'get spring assignments to area objects
      ret = SapModel.AreaObj.GetSpring("1", NumberSprings, MyType, s, SimpleSpringType, LinkProp, Face, SpringLocalOneType, Dir, Outward, VecX, VecY, VecZ, CSys, Ang)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSpring](SetSpring_{Area_Object}.htm)

[DeleteSpring](DeleteSpring_{Area_Object}.htm)



## GetThickness {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetThickness_{Area_Object}.htm`*

# GetThickness

## Syntax

SapObject.SapModel.AreaObj.GetThickness

## VB6 Procedure

Function GetThickness(ByVal Name As String, ByRef ThicknessType As Long, ByRef ThicknessPattern As String, ByRef ThicknessPatternSF As Double, ByRef Thickness() As Double) As Long

## Parameters

Name

The name of an existing area object.

ThicknessType

This is 0, 1 or 2, indicating the thickness overwrite type.

0 = No thickness overwrites

1 = User defined thickness overwrites specified by joint pattern

2 = User defined thickness overwrites specified by point

ThicknessPattern

This item applies only when ThicknessType = 1. It is the name of the defined joint pattern that is used to calculate the thicknesses.

ThicknessPatternSF

This item applies only when ThicknessType = 1. It is the scale factor applied to the joint pattern when calculating the thicknesses. [L]

Thickness

This item applies only when ThicknessType = 2. It is an array of thicknesses at each of the points that define the area object. [L]

## Remarks

This function retrieves the thickness overwrite assignments for area objects.

The function returns zero if the assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectThicknessOverwrites()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i as long
      Dim ThicknessType As Long
      Dim ThicknessPattern As String
      Dim ThicknessPatternSF As Double
      Dim Thickness() As Double

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

   'assign thickness overwrites
      ReDim Thickness(3)
      For i = 0 To 3
         Thickness(i) = 11
      Next i
      ret = SapModel.AreaObj.SetThickness("ALL", 2, "", 1, Thickness, Group)

   'get thickness overwrites
      ret = SapModel.AreaObj.GetThickness("3", ThicknessType, ThicknessPattern, ThicknessPatternSF, Thickness)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetThickness](SetThickness.htm)



## GetTransformationMatrix {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/GetTransformationMatrix_{Area_Object}.htm`*

# GetTransformationMatrix

## Syntax

Sap2000.AreaObj.GetTransformationMatrix

## VB6 Procedure

Function GetTransformationMatrix(ByVal Name As String, ByRef Value() As Double,Optional ByVal IsGlobal As Boolean = True) As Long

## Parameters

Name

The name of an existing area object.

Value

Value is an array of nine direction cosines that define the transformation matrix.

The following matrix equation shows how the transformation matrix is used to convert items from the area object local coordinate system to the global coordinate system.

![](../../../assets/images/Images/Transformation%20Matrix.JPG)

In the equation, c0 through c8 are the nine values from the transformation array, (Local1, Local2, Local3) are an item (such as a load) in the object local coordinate system, and (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.

The transformation from the local coordinate system to the present coordinate system is the same as that shown above for the global system if you substitute the present system for the global system.

IsGlobal

If this item is True, the transformation matrix is between the Global coordinate system and the area object local coordinate system.

If this item is False, the transformation matrix is between the present coordinate system and the area object local coordinate system.

## Remarks

The function returns zero if the area object transformation matrix is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAreaObjectMatrix()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign area object local axis angle
      ret = SapModel.AreaObj.SetLocalAxes("3", 30)

   'get area object transformation matrix
      ReDim Value(8)
      ret = SapModel.AreaObj.GetTransformationMatrix("3", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## SetAutoMesh _1{Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetAutoMesh__1{Area_Object}.htm`*

# SetAutoMesh\_1

## Syntax

SapObject.SapModel.AreaObj.SetAutoMesh\_1

## VB6 Procedure

Function GetAutoMesh\_1(ByVal Name As String, ByRef MeshType As Long, ByRef n1 As Long, ByRef n2 As Long, ByRef MaxSize1 As Double, ByRef MaxSize2 As Double, ByRef PointOnEdgeFromLine As Boolean, ByRef PointOnEdgeFromPoint As Boolean, ByRef ExtendCookieCutLines As Boolean, ByRef Rotation As Double, ByRef MaxSizeGeneral As Double, ByRef LocalAxesOnEdge As Boolean, ByRef LocalAxesOnFace As Boolean, ByRef RestraintsOnEdge As Boolean, ByRef RestraintsOnFace As Boolean, ByRef Group As String, ByRef SubMesh As Boolean, ByRef SubMeshSize As Double, ByRef UseUserMesh As Boolean, ByRef QuadsOnlyGeneral As Boolean) As Long

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

UseUserMesh

If this item is True, the user mesh, if assigned, will be used for analysis, otherwise the auto mesh option will be used.

QuadsOnlyGeneral

If this item is True, the general mesh will be generated with quadrilateral areas only, otherwise the mesh may include triangles as necessary. This only applies when MeshType = 6.

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
      ret = SapModel.AreaObj.SetAutoMesh\_1("ALL", 1, 3, 3, , , , , , , , , , , , , , , True, False, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 27.0.0

This function supersedes [SetAutoMesh {Area Object}](../../Obsolete_Functions/SetAutoMesh_{Area_Object}.htm)

## See Also

[GetAutoMesh\_1 {Area Object}](GetAutoMesh_1_{Area_Object}.htm)



## SetEdgeConstraint {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetEdgeConstraint_{Area_Object}.htm`*

# SetEdgeConstraint

## Syntax

SapObject.SapModel.AreaObj.SetEdgeConstraint

## VB6 Procedure

Function SetEdgeConstraint(ByVal Name As String, ByVal ConstraintExists As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

ConstraintExists

This item is True if an automatic edge constraint is generated by the program for the area object in the analysis model.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function makes generated edge constraint assignments to area objects.

The function returns zero if the edge constraint option is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjAutoEdgeConstraint()
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

   'assign auto edge constraint option
      ret = SapModel.AreaObj.SetEdgeConstraint("ALL", True, Group)
      ret = SapModel.AreaObj.SetEdgeConstraint("2", False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetEdgeConstraint](GetEdgeConstraint_{Area_Object}.htm)



## SetGUID {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetGUID_{Area_Object}.htm`*

# SetGUID

## Syntax

SapObject.SapModel.AreaObj.SetGUID

## VB6 Procedure

Function SetGUID(ByVal Name As String, Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing area object.

GUID

The GUID (Global Unique ID) for the specified area object.

## Remarks

This function sets the GUID for the specified area object. If the GUID is passed in as a blank string, the program automatically creates a GUID for the object.

This function returns zero if the area object GUID is successfully set; otherwise, it returns nonzero.

## VBA Example

Sub SetAreaObjGUID()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'set program created GUID
      ret = SapObject.SapModel.AreaObj.SetGUID("1")

   'get GUID
      ret = SapObject.SapModel.AreaObj.GetGUID("1", GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[GetGUID](GetGUID_{Area_Object}.htm)



## SetGroupAssign {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetGroupAssign_{Area_Object}.htm`*

# SetGroupAssign

## Syntax

SapObject.SapModel.AreaObj.SetGroupAssign

## VB6 Procedure

Function SetGroupAssign(ByVal Name As String, ByVal GroupName As String, Optional By Val Remove As Boolean = False, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

GroupName

The name of an existing group to which the assignment is made.

Remove

If this item is False, the specified area objects are added to the group specified by the GroupName item. If it is True, the area objects are removed from the group.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the area object specified by the Name item is added or removed from the group specified by the GroupName item.

If this item is Group, all area objects in the group specified by the Name item are added or removed from the group specified by the GroupName item.

If this item is SelectedObjects, all selected area objects are added or removed from the group specified by the GroupName item, and the Name item is ignored.

## Remarks

This function adds or removes area objects from a specified group.

The function returns zero if the group assignment is successful; otherwise it returns a nonzero value.

## VBA Example

Sub AddAreaObjectsToGroup()
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

   'define new group
      ret = SapModel.GroupDef.SetGroup("Group1")

   'add area objects to group
      ret = SapModel.AreaObj.SetGroupAssign("1", "Group1")
      ret = SapModel.AreaObj.SetGroupAssign("3", "Group1")

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

[GetGroupAssign](GetGroupAssign_{Area_Object}.htm)



## SetLoadGravity {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLoadGravity_{Area_Object}.htm`*

# SetLoadGravity

## Syntax

SapObject.SapModel.AreaObj.SetLoadGravity

## VB6 Procedure

Function SetLoadGravity(ByVal Name As String, ByVal LoadPat As String, ByVal x As Double, ByVal y As Double, ByVal z As Double, Optional ByVal Replace As Boolean = True, Optional ByVal CSys As String = "Global", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

x, y, z

These are the gravity load multipliers in the x, y and z directions of the specified coordinate system.

Replace

If this item is True, all previous gravity loads, if any, assigned to the specified area object(s), in the specified load pattern, are deleted before making the new assignment.

CSys

The coordinate system in which the x, y and z multipliers are specified.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function assigns gravity load multipliers to area objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectGravityLoad()
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

   'assign area object gravity loads
      ret = SapModel.AreaObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Area_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Area_Object}.htm)



## SetLoadPorePressure {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLoadPorePressure_{Area_Object}.htm`*

# SetLoadPorePressure

## Syntax

SapObject.SapModel.AreaObj.SetLoadPorePressure

## VB6 Procedure

Function SetLoadPorePressure(ByVal Name As String, ByVal LoadPat As String, ByVal Value As Double, Optional ByVal PatternName As String = "", Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Value

This is the pore pressure value. [F/L2]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the pore pressure load for the area object is uniform over the object at the value specified by Value.

If PatternName is the name of a defined joint pattern, the pore pressure load for the area object is based on the specified pore pressure value multiplied by the pattern value at the point objects that define the area object.

Replace

If this item is True, all previous pore pressure loads, if any, assigned to the specified area object(s), in the specified load case, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function assigns pore pressure loads to area objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectPorePressureLoad()
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

   'assign area object pore pressure load
      ret = SapModel.AreaObj.SetLoadPorePressure("ALL", "DEAD", .1, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadPorePressure](GetLoadPorePressure_{Area_Object}.htm)

[DeleteLoadPorePressure](DeleteLoadPorePressure_{Area_Object}.htm)



## SetLoadRotate

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLoadRotate.htm`*

# SetLoadRotate

## Syntax

SapObject.SapModel.AreaObj.SetLoadRotate

## VB6 Procedure

Function SetLoadRotate(ByVal Name As String, ByVal LoadPat As String, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Value

This is the angular velocity. [Cyc/T]

## Remarks

This function assigns rotate loads to area objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectRotateLoad()
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

   'assign area object rotate load
      ret = SapModel.AreaObj.SetLoadRotate("ALL", "DEAD", 30, , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadRotate](GetLoadRotate_{Area_Object}.htm)

[DeleteLoadRotate](DeleteLoadRotate.htm)



## SetLoadStrain {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLoadStrain_{Area_Object}.htm`*

# SetLoadStrain

## Syntax

SapObject.SapModel.AreaObj.SetLoadStrain

## VB6 Procedure

Function SetLoadStrain(ByVal Name As String, ByVal LoadPat As String, ByVal Component As Long, ByVal Value As Double, Optional ByVal Replace As Boolean = True, Optional ByVal PatternName As String = "", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Component

This is 1, 2, 3, 4, 5, 6, 7, 8, or 9, indicating the component to which the strain load is applied.

1 = Strain11

2 = Strain22

3 = Strain12

4 = Curvature11

5 = Curvature22

6 = Curvature12

7 = Strain13

8 = Strain23

9 = Strain33

Value

This is the strain load value. [L/L] for Component = 1, 2, 3, 7, 8, and 9 and [1/L] for Component = 4, 5 and 6

Replace

If this item is True, all previous strain loads, if any, assigned to the specified area object(s), in the specified load pattern, for the specified degree of freedom, are deleted before making the new assignment.

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the strain load for the area object is uniform over the object at the value specified by Value.

If PatternName is the name of a defined joint pattern, the strain load for the area object is based on the specified strain value multiplied by the pattern value at the corner points of the area object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function assigns strain loads to area objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectStrainLoad()
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

   'assign area object strain load
      ret = SapModel.AreaObj.SetLoadStrain("ALL", "DEAD", 1, 0.001, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

Added Strain33 component in v19.0.0.

## See Also

[GetLoadStrain](GetLoadStrain_{Area_Object}.htm)

[DeleteLoadStrain](DeleteLoadStrain_{Area_Object}.htm)



## SetLoadSurfacePressure {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLoadSurfacePressure_{Area_Object}.htm`*

# SetLoadSurfacePressure

## Syntax

SapObject.SapModel.AreaObj.SetLoadSurfacePressure

## VB6 Procedure

Function SetLoadSurfacePressure(ByVal Name As String, ByVal LoadPat As String, ByVal Face As Long, ByVal Value As Double, Optional ByVal PatternName As String = "", Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Face

This is -1, -2 or a nonzero, positive integer, indicating the area object face to which the specified load assignment applies.

-1 = Bottom face

-2 = Top face

>0 = Edge face

Note that edge face n is from area object point n to area object point n + 1. For example, edge face 2 is from area object point 2 to area object point 3.

Value

This is the surface pressure value. [F/L2]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the surface pressure load for the area object face is uniform over the face at the value specified by Value.

If PatternName is the name of a defined joint pattern, the surface pressure load for the area object face is based on the specified surface pressure value multiplied by the pattern value at the point objects that are part of the face.

Replace

If this item is True, all previous surface pressure loads, if any, assigned to the specified area object(s), in the specified load case, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function assigns surface pressure loads to area objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectSurfacePressureLoad()
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

   'assign area object surface pressure load
      ret = SapModel.AreaObj.SetLoadSurfacePressure("ALL", "DEAD", -1, .1, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadSurfacePressure](GetLoadSurfacePressure_{Area_Object}.htm)

[DeleteLoadSurfacePressure](DeleteLoadSurfacePressure_{Area_Object}.htm)



## SetLoadTemperature {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLoadTemperature_{Area_Object}.htm`*

# SetLoadTemperature

## Syntax

SapObject.SapModel.AreaObj.SetLoadTemperature

## VB6 Procedure

Function SetLoadTemperature(ByVal Name As String, ByVal LoadPat As String, ByVal MyType As Long, ByVal Value As Double, Optional ByVal PatternName As String = "", Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

MyType

This is either 1 or 3, indicating the type of temperature load.

1 = Temperature

3 = Temperature gradient along local 3 axis

Value

This is the temperature change value. [T] for MyType = 1 and [T/L] for MyType = 3

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the temperature load for the area object is uniform over the object at the value specified by Value.

If PatternName is the name of a defined joint pattern the temperature load for the area object is based on the specified temperature value multiplied by the pattern value at the joints that define the area object.

Replace

If this item is True, all previous temperature loads, if any, assigned to the specified area object(s), in the specified load case, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function assigns temperature loads to area objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectTemperatureLoad()
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

   'assign area object temperature load
      ret = SapModel.AreaObj.SetLoadTemperature("All", "DEAD", 1, 50, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTemperature](GetLoadTemperature_{Area_Object}.htm)

[DeleteLoadTemperature](DeleteLoadTemperature_{Area_Object}.htm)



## SetLoadUniform

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLoadUniform.htm`*

# SetLoadUniform

## Syntax

SapObject.SapModel.AreaObj.SetLoadUniform

## VB6 Procedure

Function SetLoadUniform(ByVal Name As String, ByVal LoadPat As String, ByVal Value As Double, ByVal Dir As Long, Optional ByVal Replace As Boolean = True, Optional ByVal CSys As String = "Global", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Value

The uniform load value. [F/L2]

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

Replace

If this item is True, all previous uniform loads, if any, assigned to the specified area object(s), in the specified load pattern, are deleted before making the new assignment.

CSys

This is Local or the name of a defined coordinate system, indicating the coordinate system in which the uniform load is specified.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function assigns uniform loads to area objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectUniformLoad()
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

   'assign area object uniform loads
      ret = SapModel.AreaObj.SetLoadUniform("ALL", "DEAD", -0.01, 2, False, "Local", Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadUniform](GetLoadUniform_{Area_Object}.htm)

[DeleteLoadUniform](DeleteLoadUniform.htm)



## SetLoadUniformToFrame

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLoadUniformToFrame.htm`*

# SetLoadUniformToFrame

## Syntax

SapObject.SapModel.AreaObj.SetLoadUniformToFrame

## VB6 Procedure

Function SetLoadUniformToFrame(ByVal Name As String, ByVal LoadPat As String, ByVal Value As Double, ByVal Dir As Long, ByVal DistType As Long, Optional ByVal Replace As Boolean = True, Optional ByVal CSys As String = "Global", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Value

The uniform load value. [F/L2]

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

DistType

This is either 1 or 2, indicating the load distribution type.

1 = One-way load distribution

2 = Two-way load distribution

One-way distribution is parallel to the area object local 1 axis. Two-way distribution is parallel to the area object local 1 and 2 axes.

Replace

If this item is True, all previous uniform loads, if any, assigned to the specified area object(s), in the specified load pattern, are deleted before making the new assignment.

CSys

This is Local or the name of a defined coordinate system, indicating the coordinate system in which the uniform load is specified.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects and the Name item is ignored.

## Remarks

This function assigns uniform to frame loads to area objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectUniformToFrameLoad()
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
      ret = SapModel.File.New3DFrame(BeamSlab, 2, 144, 3, 288, 2, 288)

   'assign area object uniform to frame loads
      ret = SapModel.AreaObj.SetLoadUniformToFrame("ALL", "DEAD", 0.01, 10, 2, False, "Global", Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadUniformToFrame](GetLoadUniformToFrame.htm)

[DeleteLoadUniformToFrame](DeleteLoadUniformToFrame.htm)



## SetLoadWindPressure

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLoadWindPressure.htm`*

# SetLoadWindPressure (Note: Newer function available)

## Syntax

SapObject.SapModel.AreaObj.SetLoadWindPressure

## VB6 Procedure

Function SetLoadWindPressure(ByVal Name As String, ByVal LoadPat As String, ByVal MyType As Long, ByVal Cp As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

MyType

This is either 1 or 2, indicating the wind pressure type.

1 = Windward, pressure varies over height

2 = Other, pressure is constant over height

Cp

This is the wind pressure coefficient.

**ItemType**

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function assigns wind pressure loads to area objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectWindPressureLoad()
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

   'assign area object wind pressure load
      ret = SapModel.AreaObj.SetLoadWindPressure("ALL", "DEAD", 1, 0.8, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

The function is obsolete and has been superseded by [SetLoadWindPressure\_1](SetLoadWindPressure_1.htm) as of v22.1.0. This function is maintained for backward compatibility.

## See Also

[GetLoadWindPressure](../../Obsolete_Functions/GetLoadWindPressure.htm)

[DeleteLoadWindPressure](DeleteLoadWindPressure.htm)



## SetLoadWindPressure_1

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLoadWindPressure_1.htm`*

# SetLoadWindPressure\_1

## Syntax

SapObject.SapModel.AreaObj.SetLoadWindPressure\_1

## VB6 Procedure

Function SetLoadWindPressure(ByVal Name As String, ByVal
LoadPat As String, ByVal MyType As Long, ByVal Cp As Double, ByVal DistributionType
As Long, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending
on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

MyType

This is either 1 or 2, indicating the wind pressure
type.

1 = Windward, pressure
varies over height

2 = Other, pressure is constant
over height

Cp

This is the wind pressure coefficient.

DistributionType

This is either 1 or 2, indicating the distribution type.

1 = To Joints
2 = To Frames – One-way
3 = To Frames – Two-way

**ItemType**

This is one of the following items in the eItemType
enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the
area object specified by the Name item.

If this item is Group, the assignment is made to all
area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made
to all selected area objects, and the Name item is ignored.

## Remarks

This function assigns wind pressure loads to area objects.

The function returns zero if the loads are successfully
assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectWindPressureLoad()
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
      ret = SapModel.File.NewWall(2, 48,
2, 48)

   'assign area object wind pressure load
      ret = SapModel.AreaObj.SetLoadWindPressure("ALL",
"DEAD", 1, 0.8, 1, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.1.0.

## See Also

[GetLoadWindPressure\_1](GetLoadWindPressure_1.htm)

[DeleteLoadWindPressure](DeleteLoadWindPressure.htm)



## SetLocalAxesAdvanced {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLocalAxesAdvanced.htm`*

# SetLocalAxesAdvanced

## Syntax

SapObject.SapModel.AreaObj.SetLocalAxesAdvanced

## VB6 Procedure

Function SetLocalAxesAdvanced(ByVal Name As String, ByVal Active As Boolean, ByVal Plane2 As Long, ByVal PlVectOpt As Long, ByVal PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group depending on the value of the ItemType item.

Active

This is True if advanced local axes exist.

Plane2

This is 31 or 32, indicating that the local plane determined by the plane reference vector is the 3-1 plane or the 3-2 plane. This item applies only when the Active item is True.

PlVectOpt

This is 1, 2, or 3, indicating the plane reference vector option. This item applies only when the Active item is True.

1 = Coordinate direction

2 = Two joints

3 = User vector

PlCSys

The coordinate system used to define the plane reference vector coordinate directions and the plane user vector. This item applies when the Active item is True and the PlVectOpt item is 1 or 3.

PlDir

This is an array dimensioned to 1 (2 integers), indicating the plane reference vector primary and secondary coordinate directions, PlDir(0) and PlDir(1) respectively, taken at the object center in the specified coordinate system and used to determine the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 1. Possible coordinate direction values are:

1 = +X        -1 = -X

2 = +Y       -2 = -Y

3 = +Z        -3 = -Z

4 = +CR     -4 = -CR

5 = +CA     -5 = -CA

6 = +CZ     -6 = -CZ

7 = +SR     -7 = -SR

8 = +SA     -8 = -SA

9 = +SB     -9 = -SB

PlPt

This is an array dimensioned to 1 (2 strings) indicating the labels of two joints that define the plane reference vector. Either of these joints may be specified as None to indicate the center of the specified object.  If both joints are specified as None, they are not used to define the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 2.

PlVect

This is an array dimensioned to 2 (3 doubles) that defines the plane reference vector. This item applies when the Active item is True and the PlVectOpt item is 3.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

Selection = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is Selection, assignment is made to all selected area objects and the Name item is ignored.

## Remarks

This function assigns advanced local axes to area objects.

The function returns zero if the advanced local axes assignments are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaAdvancedLocalAxes()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign area advanced local axes
      MyPlDir(0) = 2
      MyPlDir(1) = 3
      ret = SapModel.AreaObj.SetLocalAxesAdvanced("3", True, 31, 1, "Global", MyPlDir, MyPlPt, MyPlVect)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

## See Also

[GetLocalAxesAdvanced](GetLocalAxesAdvanced_{Area_Object}.htm)

[GetLocalAxes](GetLocalAxes_{Area_Object}.htm)



## SetLocalAxes {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetLocalAxes_{Area_Object}.htm`*

# SetLocalAxes

## Syntax

SapObject.SapModel.AreaObj.SetLocalAxes

## VB6 Procedure

Function SetLocalAxes(ByVal Name As String, ByVal Ang As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

Ang

This is the angle that the local 1 and 2 axes are rotated about the positive local 3 axis from the default orientation. The rotation for a positive angle appears counter clockwise when the local +3 axis is pointing toward you. [deg]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function assigns a local axis angle to area objects.

The function returns zero if the local axis angle is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectLocalAxisAngle()
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

   'assign area object local axis angle
      ret = SapModel.AreaObj.SetLocalAxes("3", 30)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetLocalAxes](GetLocalAxes_{Area_Object}.htm)



## SetMass {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetMass_{Area_Object}.htm`*

# SetMass

## Syntax

SapObject.SapModel.AreaObj.SetMass

## VB6 Procedure

Function SetMass(ByVal Name As String, ByVal MassOverL2 As Double, Optional ByVal Replace As Boolean = False, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

MassOverL2

The mass per unit area assigned to the area object. [M/L2]

Replace

If this item is True, all existing mass assignments to the area object are removed before assigning the specified mas. If it is False, the specified mass is added to any existing mass already assigned to the area object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects and the Name item is ignored.

## Remarks

This function assigns mass per unit area to area objects.

The function returns zero if the mass is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectMass()
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

   'assign area object mass
      ret = SapModel.AreaObj.SetMass("ALL", .0001, False, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMass](GetMass_{Area_Object}.htm)

[DeleteMass](DeleteMass_{Area_Object}.htm)



## SetMatTemp {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetMatTemp_{Area_Object}.htm`*

# SetMatTemp

## Syntax

SapObject.SapModel.AreaObj.SetMatTemp

## VB6 Procedure

Function SetMatTemp(ByVal Name As String, ByVal Temp As Double, Optional ByVal PatternName As String = "", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

Temp

This is the material temperature value assigned to the area object. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the material temperature for the area object is uniform over the object at the value specified by Temp.

If PatternName is the name of a defined joint pattern, the material temperature for the area object may vary. The material temperature at each corner point around the area object perimeter is equal to the specified temperature multiplied by the pattern value at the associated point object. The material temperature at other points in the area object is calculated by interpolation from the corner points.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function assigns material temperatures to area objects.

The function returns zero if the material temperatures are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectMatTemp()
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

   'assign material temperature
      ret = SapModel.AreaObj.SetMatTemp("ALL", 50, , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMatTemp](GetMatTemp_{Area_Object}.htm)



## SetMaterialOverwrite {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetMaterialOverwrite_{Area_Object}.htm`*

# SetMaterialOverwrite

## Syntax

SapObject.SapModel.AreaObj.SetMaterialOverwrite

## VB6 Procedure

Function SetMaterialOverwrite(ByVal Name As String, ByVal PropName As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

PropName

This is None or a blank string, indicating that any existing material overwrites assigned to the specified area objects are to be removed, or it is the name of an existing material property.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function sets the material overwrite assignment for area objects.

The function returns zero if the material overwrite assignment is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaMaterialOverwrite()
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

   'assign material overwrite
      ret = SapModel.AreaObj.SetMaterialOverwrite("3", "A992Fy50")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMaterialOverwrite](GetMaterialOverwrite_{Area_Object}.htm)



## SetModifiers {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetModifiers_{Area_Object}.htm`*

# SetModifiers

## Syntax

SapObject.SapModel.AreaObj.SetModifiers

## VB6 Procedure

Function SetModifiers(ByVal Name As String, ByRef Value() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

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

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function sets the modifier assignment for area objects. The default value for all modifiers is one.

The function returns zero if the modifier assignments are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaModifiers()
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

   'assign modifiers
      ReDim Value(9)
      For i = 0 To 9
         Value(i) = 1
      Next i
      Value(0) = 0.01
      ret = SapModel.AreaObj.SetModifiers("ALL", Value, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetModifiers](GetModifiers_{Area_Object}.htm)

[DeleteModifiers](DeleteModifiers_{Area_Object}.htm)



## SetNotionalSize

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetNotionalSize.htm`*

# SetNotionalSize

## Syntax

SapObject.SapModel.PropArea.SetNotionalSize

## VB6 Procedure

Function SetNotionalSize(ByVal Name As String, ByVal stype As String, ByVal Value As Double) As Long

## Parameters

Name

The name of an existing shell-type area section property.

stype

The type to define the notional size of a section. It can be:

"Auto" = Program will determine the notional size based on the average thickness of an area element.

"User" = The notional size is based on the user-defined value.

"None" = Notional size will not be considered. In other words, the time-dependent effect of this section will not be considered.

Value

For stype is "Auto", the Value represents for the scale factor to the program-determined notional size; for **stype** is “User”, the **Value** represents for the user-defined notional size [L]; for **stype** is “None”, the **Value** will not be used and can be set to 1.

## Remarks

This function assigns the method to determine the notional size of an area section for the creep and shrinkage calculations. This function is currently worked for shell type area section.

The function returns zero if the parameters are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaPropNotionalSize()
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
   ret = SapModel.File.NewWall(2, 48, 2, 48)

'assign parameters
   stype = “Auto”
   Value = 1.1
   ret = SapModel.PropArea.SetNotionalSize("ASEC1", stype, Value)

'close Sap2000
   SapObject.ApplicationExit False
   Set SapModel = Nothing
   Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 16.1.0

## See Also

[GetNotionalSize](GetNotionalSize.htm)



## SetOffsets

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetOffsets.htm`*

# SetOffsets

## Syntax

SapObject.SapModel.AreaObj.SetOffsets

## VB6 Procedure

Function SetOffsets(ByVal Name As String, ByVal OffsetType As Long, ByVal OffsetPattern As String, ByVal OffsetPatternSF As Double, ByRef Offset() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

OffsetType

This is 0, 1 or 2, indicating the joint offset type.

0 = No joint offsets

1 = User defined joint offsets specified by joint pattern

2 = User defined joint offsets specified by point

OffsetPattern

This item applies only when OffsetType = 1. It is the name of the defined joint pattern that is used to calculate the joint offsets.

OffsetPatternSF

This item applies only when OffsetType = 1. It is the scale factor applied to the joint pattern when calculating the joint offsets. [L]

Offset

This item applies only when OffsetType = 2. It is an array of joint offsets for each of the points that define the area object. [L]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function sets the joint offset assignments for area objects.

The function returns zero if the offsets are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectJointOffsets()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i as long
      Dim Offset() As Double

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

   'assign joint offsets
      ReDim Offset(3)
      For i = 0 To 3
         Offset(i) = 12
      Next i
      ret = SapModel.AreaObj.SetOffsets("ALL", 2, "", 1, Offset, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetOffsets](GetOffsets_{Area_Object}.htm)



## SetProperty {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetProperty_{Area_Object}.htm`*

# SetProperty

## Syntax

SapObject.SapModel.AreaObj.SetProperty

## VB6 Procedure

Function SetProperty(ByVal name As String, ByVal PropName As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

PropName

This is None or the name of a area property to be assigned to the specified area object(s). None means that no property is assigned to the area object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function assigns an area property to area objects.

The function returns zero if the property is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub SetAreaObjectProp()
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

   'set area property
      ret = SapModel.AreaObj.SetProperty("4", "None")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetProperty](GetProperty_{Area_Object}.htm)



## SetSelectedEdge

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetSelectedEdge.htm`*

# SetSelectedEdge

## Syntax

Sap2000.AreaObj.SetSelectedEdge

## VB6 Procedure

Function SetSelectedEdge(ByVal Name As String, ByVal EdgeNum As Long, ByVal Selected As Boolean) As Long

## Parameters

Name

The name of an existing area object.

EdgeNum

The area object edge that is have its selected status set.

Selected

This item is True if the specified area object edge is selected; otherwise it is False.

## Remarks

This function sets the selected status for area object edges.

The function returns zero if the selected status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAreaObjectEdgeSelected()
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

   'set area object edge selected
      ret = SapModel.AreaObj.SetSelectedEdge("1", 2, True)

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

[GetSelectedEdge](GetSelectedEdge.htm)

[GetSelected](GetSelected_{Area_Object}.htm)

[SetSelected](SetSelected_{Area_Object}.htm)



## SetSelected {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetSelected_{Area_Object}.htm`*

# SetSelected

## Syntax

Sap2000.AreaObj.SetSelected

## VB6 Procedure

Function SetSelected(ByVal Name As String, ByVal Selected As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

Selected

This item is True if the specified area object is selected, otherwise it is False.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the selected status is set for the area object specified by the Name item.

If this item is Group, the selected status is set for all area objects in the group specified by the Name item.

If this item is SelectedObjects, the selected status is set for all selected area objects, and the Name item is ignored.

## Remarks

This function sets the selected status for area objects.

The function returns zero if the selected status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAreaObjectSelected()
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

   'set area objects selected
      ret = SapModel.AreaObj.SetSelected("ALL", True, Group)

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

[GetSelected](GetSelectedEdge.htm)

[GetSelectedEdge](GetSelectedEdge.htm)

[SetSelectedEdge](SetSelectedEdge.htm)



## SetSpring {Area Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetSpring_{Area_Object}.htm`*

# SetSpring

## Syntax

SapObject.SapModel.AreaObj.SetSpring

## VB6 Procedure

Function SetSpring(ByVal Name As String, ByVal MyType As Long, ByVal s As Double, ByVal SimpleSpringType As Long, ByVal LinkProp As String, ByVal Face as Long, ByVal SpringLocalOneType As Long, ByVal Dir As Long, ByVal Outward As Boolean, ByRef Vec() As Double, ByVal Ang As Double, ByVal Replace As Boolean, Optional ByVal CSys As String = "Local", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

MyType

This is either 1 or 2, indicating the spring property type.

1 = Simple spring

2 = Link property

s

The simple spring stiffness per unit area of the specified area object face. This item applies only when MyType = 1. [F/L3]

SimpleSpringType

This is 1, 2 or 3, indicating the simple spring type. This item applies only when MyType = 1.

1 = Spring resists tension and compression

2 = Spring resists compression only

3 = Spring resists tension only

LinkProp

The name of the link property assigned to the spring. This item applies only when MyType = 2.

Face

This is -1, -2 or a nonzero, positive integer indicating the area object face to which the specified spring assignment applies.

-1 = Bottom face

-2 = Top face

>0 = Edge face

Note that edge face n is from area object point n to area object point n + 1. For example, edge face 2 is from area object point 2 to area object point 3.

SpringLocalOneType

This is 1, 2 or 3, indicating the method used to specify the spring positive local 1-axis orientation.

1 = Parallel to area object local axis

2 = Normal to specified area object face

3 = User specified direction vector

Dir

This is 1, 2, 3, -1, -2 or -3, indicating the area object local axis that corresponds to the positive local 1-axis of the spring. This item applies only when SpringLocalOneType = 1.

Outward

This item is True if the spring positive local 1 axis is outward from the specified area object face. This item applies only when SpringLocalOneType = 2.

Vec

This is an array of three values that define the direction vector of the spring positive local 1-axis. The direction vector is in the coordinate system specified by the CSys item. This item applies only when SpringLocalOneType = 3.

Ang

This is the angle that the link local 2-axis is rotated from its default orientation. This item applies only when MyType = 2. [deg]

Replace

If this item is True, all existing spring assignments to the area object are removed before assigning the specified spring. If it is False, the specified spring is added to any existing springs already assigned to the area object.

CSys

This is Local (meaning the area object local coordinate system) or the name of a defined coordinate system. This item is the coordinate system in which the user specified direction vector, Vec, is specified. This item applies only when SpringLocalOneType = 3.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function makes spring assignments to area objects. The springs are assigned to a specified area object face.

The function returns zero if the assignments are successfully applied; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectSprings()
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
      ret = SapModel.File.NewWall(2, 48, 2, 48)

   'assign springs to area objects
      ReDim Vec(2)
      ret = SapModel.AreaObj.SetSpring("ALL", 1, 1, 1, "", -1, 1, 3, True, Vec, 0, False, "Local", Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Area_Object}.htm)

[DeleteSpring](DeleteSpring_{Area_Object}.htm)



## SetThickness

*Source file: `SAP2000_API_Fuctions/Object_Model/Area_Object/SetThickness.htm`*

# SetThickness

## Syntax

SapObject.SapModel.AreaObj.SetThickness

## VB6 Procedure

Function SetThickness(ByVal Name As String, ByVal ThicknessType As Long, ByVal ThicknessPattern As String, ByVal ThicknessPatternSF As Double, ByRef Thickness() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing area object or group, depending on the value of the ItemType item.

ThicknessType

This is 0, 1 or 2, indicating the thickness overwrite type.

0 = No thickness overwrites

1 = User defined thickness overwrites specified by joint pattern

2 = User defined thickness overwrites specified by point

ThicknessPattern

This item applies only when ThicknessType = 1. It is the name of the defined joint pattern that is used to calculate the thicknesses.

ThicknessPatternSF

This item applies only when ThicknessType = 1. It is the scale factor applied to the joint pattern when calculating the thicknesses. [L]

Thickness

This item applies only when ThicknessType = 2. It is an array of thicknesses at each of the points that define the area object. [L]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the area object specified by the Name item.

If this item is Group, the assignment is made to all area objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected area objects, and the Name item is ignored.

## Remarks

This function sets the thickness overwrite assignments for area objects.

The function returns zero if the thickness overwrites are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignAreaObjectThicknessOverwrites()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i as long
      Dim Thickness() As Double

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

   'assign thickness overwrites
      ReDim Thickness(3)
      For i = 0 To 3
         Thickness(i) = 11
      Next i
      ret = SapModel.AreaObj.SetThickness("ALL", 2, "", 1, Thickness, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetThickness](GetThickness_{Area_Object}.htm)

