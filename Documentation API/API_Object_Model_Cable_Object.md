# API Object Model Cable Object

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Object_Model/Cable_Object

---



## AddByCoord {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/AddByCoord_{Cable_Object}.htm`*

# AddByCoord

## Syntax

SapObject.SapModel.CableObj.AddByCoord

## VB6 Procedure

Function AddByCoord(ByVal xi As Double, ByVal yi As Double, ByVal zi As Double, ByVal xj As Double, ByVal yj As Double, ByVal zj As Double, ByRef Name As String, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "", Optional ByVal CSys As String = "Global") As Long

## Parameters

xi, yi, zi

The coordinates of the I-End of the added cable object. The coordinates are in the coordinate system defined by the CSys item.

xj, yj, zj

The coordinates of the J-End of the added cable object. The coordinates are in the coordinate system defined by the CSys item.

Name

This is the name that the program ultimately assigns for the cable object. If no UserName is specified,n the program assigns a default name to the cable object. If a UserName is specified and that name is not used for another frame, cable or tendon object, the UserName is assigned to the cable object; otherwise a default name is assigned to the cable object.

PropName

This is Default or the name of a defined cable property.

If it is Default, the program assigns a default cable property to the cable object. If it is the name of a defined cable property, that property is assigned to the cable object.

UserName

This is an optional user specified name for the cable object. If a UserName is specified and that name is already used for another cable object, the program ignores the UserName.

CSys

The name of the coordinate system in which the cable object end point coordinates are defined.

## Remarks

This function adds a new cable object whose end points are at the specified coordinates.

The function returns zero if the cable object is successfully added, otherwise it returns a nonzero value.

## VBA Example

Sub AddCableObjByCoord()
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

   'add cable object by coordinates
      ret = SapModel.CableObj.AddByCoord(-300, 0, 0, -100, 0, 124, Name)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByPoint](AddByPoint_{Cable_Object}.htm)

[SetCableData](SetCableData_{Cable_Object}.htm)



## AddByPoint {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/AddByPoint_{Cable_Object}.htm`*

# AddByPoint

## Syntax

SapObject.SapModel.CableObj.AddByPoint

## VB6 Procedure

Function AddByPoint(ByVal Point1 as String, ByVal Point2 as String, ByRef Name As String, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "") As Long

## Parameters

Point1

The name of a defined point object at the I-End of the added cable object.

Point2

The name of a defined point object at the J-End of the added cable object.

Name

This is the name that the program ultimately assigns for the cable object. If no UserName is specified, the program assigns a default name to the cable object. If a UserName is specified and that name is not used for another frame, cable or tendon object, the UserName is assigned to the cable object; otherwise a default name is assigned to the cable object.

PropName

This is Default or the name of a defined cable property.

If it is Default, the program assigns a default cable property to the cable object. If it is the name of a defined cable property, that property is assigned to the cable object.

UserName

This is an optional user specified name for the cable object. If a UserName is specified and that name is already used for another cable object, the program ignores the UserName.

## Remarks

This function adds a new cable object whose end points are specified by name.

The function returns zero if the cable object is successfully added, otherwise it returns a nonzero value.

## VBA Example

Sub AddCableObjByPoint()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Cable_Object}.htm)

[SetCableData](SetCableData_{Cable_Object}.htm)



## ChangeName {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/ChangeName_{Cable_Object}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.CableObj.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a defined cable object.

NewName

The new name for the cable object.

## Remarks

The function returns zero if the new name is successfully applied, otherwise it returns a nonzero value.

## VBA Example

Sub ChangeCableObjName()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'change name
      ret = SapModel.CableObj.ChangeName(Name, "MyCable")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## Count {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/Count_{Cable_Object}.htm`*

# Count

## Syntax

SapObject.SapModel.CableObj.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None

## Remarks

This function returns a count of the cable objects in the model.

## VBA Example

Sub CountCableObjects()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
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

   'return number of cable objects
      Count = SapModel.CableObj.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## DeleteLoadDeformation {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/DeleteLoadDeformation_{Cable_Object}.htm`*

# DeleteLoadDeformation

## Syntax

SapObject.SapModel.CableObj.DeleteLoadDeformation

## VB6 Procedure

Function DeleteLoadDeformation(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the cable object specified by the Name item.

If this item is Group, the load assignments are deleted for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected cable objects, and the Name item is ignored.

## Remarks

This function deletes the deformation load assignments to the specified cable objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteCableDeformationLoad()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable deformation loads
      ret = SapModel.CableObj.SetLoadDeformation("ALL", "DEAD", 2, Group)

   'delete cable deformation load
      ret = SapModel.CableObj.DeleteLoadDeformation(Name, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDeformation](GetLoadDeformation_{Cable_Object}.htm)

[SetLoadDeformation](SetLoadDeformation_{Cable_Object}.htm)



## DeleteLoadDistributedWithGUID {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/DeleteLoadDistributedWithGUID_{Cable_Object}.htm`*

# DeleteLoadDistributedWithGUID

## Syntax

SapObject.SapModel.CableObj.DeleteLoadDistributedWithGUID

## VB6 Procedure

Function DeleteLoadDistributedWithGUID(ByVal Name As String, ByVal GUID As String) As Long

## Parameters

Name

The name of an existing cable object.

GUID

The global unique ID of one of the distributed loads on that cable object.

## Remarks

This function deletes the distributed load assignment with the specified global unique ID for the specified cable object.

The function returns zero if the load assignment is successfully deleted, otherwise it returns a nonzero value.

## Release Notes

Initial release in version 17.2.0.

## See Also

[GetLoadDistributedWithGUID](../../../GetLoadDistributedWithGUID_{Cable_Object}.htm)

[SetLoadDistributedWithGUID](../../../SetLoadDistributedWithGUID_{Cable_Object}.htm)



## DeleteLoadDistributed {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/DeleteLoadDistributed_{Cable_Object}.htm`*

# DeleteLoadDistributed

## Syntax

SapObject.SapModel.CableObj.DeleteLoadDistributed

## VB6 Procedure

Function DeleteLoadDistributed(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the cable object specified by the Name item.

If this item is Group, the load assignments are deleted for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected cable objects, and the Name item is ignored.

## Remarks

This function deletes the distributed load assignments to the specified cable objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteCableDistributedLoad()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable distributed load
      ret = SapModel.CableObj.SetLoadDistributed(Name, "DEAD", 1, 10, 0.08)

   'delete cable distributed load
      ret = SapModel.CableObj.DeleteLoadDistributed(Name, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDistributed](GetLoadDistributed_{Cable_Object}.htm)

[SetLoadDistributed](SetLoadDistributed_{Cable_Object}.htm)



## DeleteLoadGravity {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/DeleteLoadGravity_{Cable_Object}.htm`*

# DeleteLoadGravity

## Syntax

SapObject.SapModel.CableObj.DeleteLoadGravity

## VB6 Procedure

Function DeleteLoadGravity(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the cable object specified by the Name item.

If this item is Group, the load assignments are deleted for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected cable objects, and the Name item is ignored.

## Remarks

This function deletes the gravity load assignments to the specified cable objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteCableGravityLoad()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable gravity loads
      ret = SapModel.CableObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'delete cable gravity load
      ret = SapModel.CableObj.DeleteLoadGravity(Name, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Cable_Object}.htm)

[SetLoadGravity](SetLoadGravity_{Cable_Object}.htm)



## DeleteLoadStrain {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/DeleteLoadStrain_{Cable_Object}.htm`*

# DeleteLoadStrain

## Syntax

SapObject.SapModel.CableObj.DeleteLoadStrain

## VB6 Procedure

Function DeleteLoadStrain(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the cable object specified by the Name item.

If this item is Group, the load assignments are deleted for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected cable objects, and the Name item is ignored.

## Remarks

This function deletes the strain load assignments to the specified cable objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteCableStrainLoad()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable strain load
      ret = SapModel.CableObj.SetLoadStrain(Name, "DEAD", 0.001)

   'delete cable strain load
      ret = SapModel.CableObj.DeleteLoadStrain(Name, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadStrain](GetLoadStrain_{Cable_Object}.htm)

[SetLoadStrain](SetLoadStrain_{Cable_Object}.htm)



## DeleteLoadTargetForce {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/DeleteLoadTargetForce_{Cable_Object}.htm`*

# DeleteLoadTargetForce

## Syntax

SapObject.SapModel.CableObj.DeleteLoadTargetForce

## VB6 Procedure

Function DeleteLoadTargetForce(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the cable object specified by the Name item.

If this item is Group, the load assignments are deleted for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected cable objects, and the Name item is ignored.

## Remarks

This function deletes the target force assignments to the specified cable objects for the specified load pattern.

The function returns zero if the target force assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteCableTargetForce()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable target force
      ret = SapModel.CableObj.SetLoadTargetForce(Name, "DEAD", 50, 0.5)

   'delete cable target force
      ret = SapModel.CableObj.DeleteLoadTargetForce(Name, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTargetForce](GetLoadTargetForce_{Cable_Object}.htm)

[SetLoadTargetForce](SetLoadTargetForce_{Cable_Object}.htm)



## DeleteLoadTemperature {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/DeleteLoadTemperature_{Cable_Object}.htm`*

# DeleteLoadTemperature

## Syntax

SapObject.SapModel.CableObj.DeleteLoadTemperature

## VB6 Procedure

Function DeleteLoadTemperature(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the cable object specified by the Name item.

If this item is Group, the load assignments are deleted for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected cable objects, and the Name item is ignored.

## Remarks

This function deletes the temperature load assignments to the specified cable objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteCableTemperatureLoad()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable temperature load
      ret = SapModel.CableObj.SetLoadTemperature("ALL", "DEAD", 50, , , Group)

   'delete cable temperature load
      ret = SapModel.CableObj.DeleteLoadTemperature(Name, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTemperature](GetLoadTemperature_{Cable_Object}.htm)

[SetLoadTemperature](SetLoadTemperature_{Cable_Object}.htm)



## DeleteMass {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/DeleteMass_{Cable_Object}.htm`*

# DeleteMass

## Syntax

SapObject.SapModel.CableObj.DeleteMass

## VB6 Procedure

Function DeleteMass(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the cable mass assignments are deleted for the cable object specified by the Name item.

If this item is Group, the cable mass assignments are deleted for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, the cable mass assignments are deleted for all selected cable objects, and the Name item is ignored.

## Remarks

This function deletes the cable mass assignments for cable objects.

The function returns zero if the mass assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteCableMass()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable mass
      ret = SapModel.CableObj.SetMass("ALL", .0001, False, Group)

   'delete cable mass
      ret = SapModel.CableObj.DeleteMass(Name)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMass](GetMass_{Cable_Object}.htm)

[SetMass](SetMass_{Cable_Object}.htm)



## DeleteModifiers {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/DeleteModifiers_{Cable_Object}.htm`*

# DeleteModifiers

## Syntax

SapObject.SapModel.CableObj.DeleteModifiers

## VB6 Procedure

Function DeleteModifiers(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the cable modifier assignments are deleted for the cable object specified by the Name item.

If this item is Group, the cable modifier assignments are deleted for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, the cable modifier assignments are deleted for all selected cable objects, and the Name item is ignored.

## Remarks

This function deletes the cable modifier assignments for cable objects.

The function returns zero if the modifier assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteCableModifiers()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double
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

   'assign modifiers
      ReDim Value(2)
      For i = 0 To 2
         Value(i) = 1
      Next i
      Value(0) = 100
      ret = SapModel.CableObj.SetModifiers(Name, Value)

   'delete modifiers
      ret = SapModel.CableObj.DeleteModifiers(Name)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetModifiers](GetModifiers_{Cable_Object}.htm)

[SetModifiers](SetModifiers_{Cable_Object}.htm)



## Delete {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/Delete_{Cable_Object}.htm`*

# Delete

## Syntax

SapObject.SapModel.CableObj.Delete

## VB6 Procedure

Function Delete(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the cable object specified by the Name item is deleted.

If this item is Group, the all cable objects in the group specified by the Name item are deleted.

If this item is SelectedObjects, all selected cable objects are deleted, and the Name item is ignored.

## Remarks

The function deletes cable objects.

The function returns zero if the cable objects are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteCableObj()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name1 As String
      Dim Name2 As String

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

   'add cable objects by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name1)
      ret = SapModel.CableObj.AddByPoint("5", "10", Name2)

   'delete cable object
      ret = SapModel.CableObj.Delete(Name1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Cable_Object}.htm)

[AddByPoint](AddByPoint_{Cable_Object}.htm)



## GetCableData {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetCableData_{Cable_Object}.htm`*

# GetCableData

## Syntax

SapObject.SapModel.CableObj.GetCableData

## VB6 Procedure

Function GetCableData(ByRef Name As String, ByRef CableType As Long, ByRef NumSegs As Long, ByRef Weight As Double, ByRef ProjectedLoad As Double, ByRef UseDeformedGeom As Boolean, ByRef ModelUsingFrames As Boolean, ByRef Parameter() As Double) As Long

## Parameters

Name

The name of a defined cable object.

CableType

This is 1, 2, 3, 4, 5, 6, 7, 8, or 9, indicating the cable definition parameter.

1 = Minimum tension at I-End

2 = Minimum tension at J-End

3 = Tension at I-End

4 = Tension at J-End

5 = Horizontal tension component

6 = Maximum vertical sag

7 = Low-point vertical sag

8 = Undeformed length

9 = Relative undeformed length

NumSegs

This is the number of segments into which the program internally divides the cable.

Weight

The added weight per unit length used when calculating the cable shape. [F/L]

ProjectedLoad

The projected uniform gravity load used when calculating the cable shape. [F/L]

UseDeformedGeom

If this item is True, the program uses the deformed geometry for the cable object; otherwise it uses the undeformed geometry.

ModelUsingFrames

If this item is True, the analysis model uses frame elements to model the cable instead of using cable elements.

Parameter

This is an array of parameters related to the cable shape. The array is dimensioned by Sap2000.

Parameter(0) = Tension at I-End [F]

Parameter(1) = Tension at J-End [F]

Parameter(2) = Horizontal tension component [F]

Parameter(3) = Maximum deformed vertical sag [L]

Parameter(4) = Deformed low-point vertical sag [L]

Parameter(5) = Deformed length [L]

Parameter(6) = Deformed relative length

Parameter(7) = Maximum undeformed vertical sag [L]

Parameter(8) = Undeformed low-point vertical sag [L]

Parameter(9) = Undeformed length [L]

Parameter(10) = Undeformed relative length

## Remarks

This function retrieves definition data for a specified cable object.

The function returns zero if the data is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableObjectData()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim CableType As Long
      Dim NumSegs As Long
      Dim Weight As Double
      Dim ProjectedLoad As Double
      Dim UseDeformedGeom As Boolean
      Dim ModelUsingFrames As Boolean
      Dim Parameter() As Double

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

   'get cable data
      ret = SapModel.CableObj.GetCableData(Name, CableType, NumSegs, Weight, ProjectedLoad, UseDeformedGeom, ModelUsingFrames, Parameter)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Cable_Object}.htm)

[AddByPoint](AddByPoint_{Cable_Object}.htm)

[SetCableData](SetCableData_{Cable_Object}.htm)

[GetCableGeometry](GetCableGeometry_{Cable_Object}.htm)



## GetCableGeometry {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetCableGeometry_{Cable_Object}.htm`*

# GetCableGeometry

## Syntax

SapObject.SapModel.CableObj.GetCableGeometry

## VB6 Procedure

Function GetCableGeometry(ByRef Name As String, ByRef NumberPoints As Long, ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, ByRef Sag() As Double, ByRef Dist() As Double, ByRef RD() As Double, Optional ByVal CSys As String = "Global") As Long

## Parameters

Name

The name of a defined cable object.

NumberPoints

The number of points defining the cable geometry.

x, y, z

The x, y and z coordinates of the considered point on the cable in the coordinate system specified by the CSys item. [L]

Sag

The cable vertical sag, measured from the chord, at the considered point. [L]

Distance

The distance along the cable, measured from the cable I-End, to the considered point. [L]

RD

The relative distance along the cable, measured from the cable I-End, to the considered point.

CSys

The name of the coordinate system in which the x, y and z coordinates are to be reported.

## Remarks

This function retrieves geometric data for a specified cable object.

The function returns zero if the data is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableObjectGeometry()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberPoints As Long
      Dim x() As Double
      Dim y() As Double
      Dim z() As Double
      Dim Sag() As Double
      Dim Dist() As Double
      Dim RD() As Double

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

   'get cable geometry
      ret = SapModel.CableObj.GetCableGeometry(Name, NumberPoints , x, y, z, Sag, Dist, RD)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Cable_Object}.htm)

[AddByPoint](AddByPoint_{Cable_Object}.htm)

[SetCableData](SetCableData_{Cable_Object}.htm)

[GetCableData](GetCableData_{Cable_Object}.htm)



## GetElm {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetElm_{Cable_Object}.htm`*

# GetElm

## Syntax

SapObject.SapModel.CableObj.GetElm

## VB6 Procedure

Function GetElm(ByVal Name As String, ByRef nelm As Long, ByRef Elm() as String, ByRef RDI() As Double, ByRef RDJ() As Double) As Long

## Parameters

Name

The name of an existing cable object.

nelm

The number of line elements created from the specified cable object.

Elm

An array that includes the name of a line element created from the specified cable object.

RDI

An array that includes the relative distance along the cable object to the I-End of the line element.

RDJ

An array that includes the relative distance along the cable object to the J-End of the line element.

## Remarks

This function retrieves the names of the line elements (analysis model lines) associated with a specified cable object in the object-based model. It also retrieves information about the location of the line elements along the cable object.

This function returns zero if the line element information is successfully returned; otherwise it returns nonzero. An error occurs if the analysis model does not currently exist.

## VBA Example

Sub GetLineElementInfoForCableObject()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim nelm As Long
      Dim Elm() As String
      Dim RDI() As Double
      Dim RDJ() As Double
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

   'create the analysis model
      ret = SapModel.Analyze.CreateAnalysisModel

   'get line element information
      ret = SapModel.CableObj.GetElm(Name, nelm, Elm, RDI, RDJ)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetGUID {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetGUID_{Cable_Object}.htm`*

# GetGUID

## Syntax

SapObject.SapModel.CableObj.GetGUID

## VB6 Procedure

Function GetGUID(ByVal name As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing cable object.

GUID

The GUID (Global Unique ID) for the specified cable object.

## Remarks

This function retrieves the GUID for the specified cable object.

This function returns zero if the cable object GUID is successfully retrieved; otherwise it returns nonzero.

## VBA Example

Sub GetCableObjGUID()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'set program created GUID
      ret = SapObject.SapModel.CableObj.SetGUID(Name)

   'get GUID
      ret = SapObject.SapModel.CableObj.GetGUID(Name, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetGUID](SetGUID_{Cable_Object}.htm)



## GetGroupAssign {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetGroupAssign_{Cable_Object}.htm`*

# GetGroupAssign

## Syntax

SapObject.SapModel.CableObj.GetGroupAssign

## VB6 Procedure

Function GetGroupAssign(ByVal Name As String, ByRef NumberGroups As Long, ByRef Groups() As String)  As Long

## Parameters

Name

The name of an existing cable object.

NumberGroups

The number of group names retrieved.

Groups

The names of the groups to which the cable object is assigned.

## Remarks

This function retrieves the names of the groups to which a specified cable object is assigned.

The function returns zero if the group assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableObjectGroups()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name1 As String
      Dim Name2 As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name1)
      ret = SapModel.CableObj.AddByPoint("5", "10", Name2)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name1, 7, 1, 0, 0, 24)
      ret = SapModel.CableObj.SetCableData(Name2, 7, 1, 0, 0, 24)

   'define new groups
      ret = SapModel.GroupDef.SetGroup("Group1")
      ret = SapModel.GroupDef.SetGroup("Group2")

   'add cable object to groups
      ret = SapModel.CableObj.SetGroupAssign(Name1, "Group1")
      ret = SapModel.CableObj.SetGroupAssign(Name1, "Group2")

   'get cable object groups
      ret = SapModel.CableObj.GetGroupAssign(Name1, NumberGroups, Groups)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.0.0.

## See Also

[SetGroupAssign](SetGroupAssign_{Cable_Object}.htm)



## GetLoadDeformation {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetLoadDeformation_{Cable_Object}.htm`*

# GetLoadDeformation

## Syntax

SapObject.SapModel.CableObj.GetLoadDeformation

## VB6 Procedure

Function GetLoadDeformation(ByVal Name As String, ByRef NumberItems As Long, ByRef CableName() As String, ByRef LoadPat() As String, ByRef U1() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

NumberItems

The total number of deformation loads retrieved for the specified cable objects.

CableName

This is an array that includes the name of the cable object associated with each deformation load.

LoadPat

This is an array that includes the name of the load pattern associated with each deformation load.

U1

This is an array of axial deformation load values. [L]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the cable object specified by the Name item.

If this item is Group, the assignments are retrieved for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected cable objects, and the Name item is ignored.

## Remarks

This function retrieves the deformation load assignments to cable objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableDeformationLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim CableName() As String
      Dim LoadPat() As String
      Dim U1() As Double
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

   'assign cable deformation loads
      ret = SapModel.CableObj.SetLoadDeformation("ALL", "DEAD", 2, Group)

   'get cable deformation loads
      ret = SapModel.CableObj.GetLoadDeformation(Name, NumberItems, CableName, LoadPat, U1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadDeformation](SetLoadDeformation_{Cable_Object}.htm)

[DeleteLoadDeformation](DeleteLoadDeformation_{Cable_Object}.htm)



## GetLoadDistributed {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetLoadDistributed_{Cable_Object}.htm`*

# GetLoadDistributed

## Syntax

SapObject.SapModel.CableObj.GetLoadDistributed

## VB6 Procedure

Function GetLoadDistributed(ByVal Name As String, ByRef NumberItems As Long, ByRef CableName() As String, ByRef LoadPat() As String, ByRef MyType() As Long, ByRef CSys() As String, ByRef Dir() As Long, ByRef ByRef Value() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

NumberItems

The total number of distributed loads retrieved for the specified cable objects.

CableName

This is an array that includes the name of the cable object associated with each distributed load.

LoadPat

This is an array that includes the name of the coordinate system in which the distributed loads are specified.

MyType

This is an array that includes 1 or 2, indicating the type of distributed load.

1 = Force

2 = Moment

CSys

This is an array that includes the name of the coordinate system in which each distributed load is defined. It may be Local or the name of a defined coordinate system.

Dir

This is 1, 2, 3, 4, 5, 6 or 10, indicating the direction of the load.

1 = Local 1 axis (only applies when CSys is Local)

2 = Local 2 axis (only applies when CSys is Local)

3 = Local 3 axis (only applies when CSys is Local)

4 = X direction (does not apply when CSys is Local)

5 = Y direction (does not apply when CSys is Local)

6 = Z direction (does not apply when CSys is Local)

10 = Gravity direction (only applies when CSys is Global)

The positive gravity direction (see Dir = 10) is in the negative Global Z direction.

Value

This is the load value of the distributed load. The distributed load is applied over the full length of the cable. [F/L] when MyType is 1 and [FL/L] when MyType is 2

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the cable object specified by the Name item.

If this item is Group, the assignments are retrieved for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected cable objects, and the Name item is ignored.

## Remarks

This function retrieves the distributed load assignments to cable objects. The loads are uniformly distributed over the full length of cable objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableDistributedLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim CableName() As String
      Dim LoadPat() As String
      Dim MyType() As Long
      Dim CSys() As String
      Dim Dir() As Long
      Dim Value() As Double
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

   'assign cable distributed load
      ret = SapModel.CableObj.SetLoadDistributed(Name, "DEAD", 1, 10, 0.08)

   'get cable distributed loads
      ret = SapModel.CableObj.GetLoadDistributed("ALL", NumberItems, CableName, LoadPat, MyType, CSys, Dir, Value, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadDistributed](SetLoadDistributed_{Cable_Object}.htm)

[DeleteLoadDistributed](DeleteLoadDistributed_{Cable_Object}.htm)



## GetLoadGravity {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetLoadGravity_{Cable_Object}.htm`*

# GetLoadGravity

## Syntax

SapObject.SapModel.CableObj.GetLoadGravity

## VB6 Procedure

Function GetLoadGravity(ByVal Name As String, ByRef NumberItems As Long, ByRef CableName() As String, ByRef LoadPat() As String, ByRef CSys() As String, ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

NumberItems

The total number of gravity loads retrieved for the specified cable objects.

CableName

This is an array that includes the name of the cable object associated with each gravity load.

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

If this item is Object, the assignments are retrieved for the cable object specified by the Name item.

If this item is Group, the assignments are retrieved for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected cable objects, and the Name item is ignored.

## Remarks

This function retrieves the gravity load assignments to cable objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableGravityLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim CableName() As String
      Dim LoadPat() As String
      Dim CSys() As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable gravity loads
      ret = SapModel.CableObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'get cable gravity load
      ret = SapModel.CableObj.GetLoadGravity(Name, NumberItems, CableName, LoadPat, CSys, x, y, z)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadGravity](SetLoadGravity_{Cable_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Cable_Object}.htm)



## GetLoadStrain {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetLoadStrain_{Cable_Object}.htm`*

# GetLoadStrain

## Syntax

SapObject.SapModel.CableObj.GetLoadStrain

## VB6 Procedure

Function GetLoadStrain(ByVal Name As String, ByRef NumberItems As Long, ByRef CableName() As String, ByRef LoadPat() As String, ByRef Strain() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

NumberItems

The total number of strain loads retrieved for the specified cable objects.

CableName

This is an array that includes the name of the cable object associated with each strain load.

LoadPat

This is an array that includes the name of the load pattern associated with each strain load.

Strain

This is an array that includes the axial strain value. [L/L]

PatternName

This is an array that includes the joint pattern name, if any, used to specify the strain load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the cable object specified by the Name item.

If this item is Group, the assignments are retrieved for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected cable objects, and the Name item is ignored.

## Remarks

This function retrieves the strain load assignments to cable objects.

The function returns zero if the strain load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableStrainLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim CableName() As String
      Dim LoadPat() As String
      Dim Strain() As Double
      Dim PatternName() As String
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

   'assign cable strain load
      ret = SapModel.CableObj.SetLoadStrain(Name, "DEAD", 0.001)

   'get cable strain load
      ret = SapModel.CableObj.GetLoadStrain(Name, NumberItems, CableName, LoadPat, Strain,PatternName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadStrain](SetLoadStrain_{Cable_Object}.htm)

[DeleteLoadStrain](DeleteLoadStrain_{Cable_Object}.htm)



## GetLoadTargetForce {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetLoadTargetForce_{Cable_Object}.htm`*

# GetLoadTargetForce

## Syntax

SapObject.SapModel.CableObj.GetLoadTargetForce

## VB6 Procedure

Function GetLoadTargetForce(ByVal Name As String, ByRef NumberItems As Long, ByRef CableName() As String, ByRef LoadPat() As String, ByRef P() As Double, ByRef RD() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

NumberItems

The total number of deformation loads retrieved for the specified cable objects.

CableName

This is an array that includes the name of the cable object associated with each target force.

LoadPat

This is an array that includes the name of the load pattern associated with each target force.

P

This is an array of axial target force values. [F]

RD

This is an array of the relative distances along the cable objects where the axial target force values apply.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the cable object specified by the Name item.

If this item is Group, the assignments are retrieved for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected cable objects, and the Name item is ignored.

## Remarks

This function retrieves the target force assignments to cable objects.

The function returns zero if the target force assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableTargetForce()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim CableName() As String
      Dim LoadPat() As String
      Dim P() As double
      Dim RD() As double
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

   'assign cable target force
      ret = SapModel.CableObj.SetLoadTargetForce(Name, "DEAD", 50, 0.5)

   'get cable target force
      ret = SapModel.CableObj.GetLoadTargetForce(Name, NumberItems, CableName, LoadPat, P, RD)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadTargetForce](SetLoadTargetForce_{Cable_Object}.htm)

[DeleteLoadTargetForce](DeleteLoadTargetForce_{Cable_Object}.htm)



## GetLoadTemperature {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetLoadTemperature_{Cable_Object}.htm`*

# GetLoadTemperature

## Syntax

SapObject.SapModel.CableObj.GetLoadTemperature

## VB6 Procedure

Function GetLoadTemperature(ByVal Name As String, ByRef NumberItems As Long, ByRef CableName() As String, ByRef LoadPat() As String, ByRef MyType() As Long, ByRef Val() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

NumberItems

The total number of temperature loads retrieved for the specified cable objects.

CableName

This is an array that includes the name of the cable object associated with each temperature load.

LoadPat

This is an array that includes the name of the load pattern associated with each temperature load.

Val

This is an array that includes the temperature load value. [T]

PatternName

This is an array that includes the joint pattern name, if any, used to specify the temperature load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the cable object specified by the Name item.

If this item is Group, the assignments are retrieved for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected cable objects, and the Name item is ignored.

## Remarks

This function retrieves the temperature load assignments to cable objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableTemperatureLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim CableName() As String
      Dim LoadPat() As String
      Dim Val() As Double
      Dim PatternName() As String
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

   'assign cable temperature load
      ret = SapModel.CableObj.SetLoadTemperature("ALL", "DEAD", 50, , , Group)

   'get cable temperature load
      ret = SapModel.CableObj.GetLoadTemperature("ALL", NumberItems, CableName, LoadPat, Val, PatternName, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadTemperature](SetLoadTemperature_{Cable_Object}.htm)

[DeleteLoadTemperature](DeleteLoadTemperature_{Cable_Object}.htm)



## GetMass {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetMass_{Cable_Object}.htm`*

# GetMass

## Syntax

SapObject.SapModel.CableObj.GetMass

## VB6 Procedure

Function GetMass(ByVal Name As String, ByRef MassOverL As Double) As Long

## Parameters

Name

The name of an existing cable object.

MassOverL

The mass per unit length assigned to the cable object. [M/L]

## Remarks

This function retrieves the mass per unit length assignment for cable objects.

The function returns zero if the mass assignment is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableMass()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable mass
      ret = SapModel.CableObj.SetMass("ALL", .0001, False, Group)

   'get cable mass assignment
      ret = SapModel.CableObj.GetMass(Name, MassOverL)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMass](SetMass_{Cable_Object}.htm)

[DeleteMass](DeleteMass_{Cable_Object}.htm)



## GetMatTemp {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetMatTemp_{Cable_Object}.htm`*

# GetMatTemp

## Syntax

SapObject.SapModel.CableObj.GetMatTemp

## VB6 Procedure

Function GetMatTemp(ByVal Name As String, ByRef Temp As Double, ByRef PatternName As String) As Long

## Parameters

Name

The name of an existing cable object.

Temp

This is the material temperature value assigned to the cable object. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the material temperature for the cable object is uniform along the object at the value specified by Temp.

If PatternName is the name of a defined joint pattern, the material temperature for the cable object may vary from one end to the other. The material temperature at each end of the object is equal to the specified temperature multiplied by the pattern value at the joint at the end of the cable object.

## Remarks

This function retrieves the material temperature assignments to cable objects.

The function returns zero if the material temperature assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableMatTemp()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Temp As Double
      Dim PatternName As String
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

   'assign material temperature
      ret = SapModel.CableObj.SetMatTemp("ALL", 50, , Group)

   'get material temperature
      ret = SapModel.CableObj.GetMatTemp(Name, Temp, PatternName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMatTemp](SetMatTemp_{Cable_Object}.htm)



## GetMaterialOverwrite {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetMaterialOverwrite_{Cable_Object}.htm`*

# GetMaterialOverwrite

## Syntax

SapObject.SapModel.CableObj.GetMaterialOverwrite

## VB6 Procedure

Function GetMaterialOverwrite(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a defined cable object.

PropName

This is None, indicating that no material overwrite exists for the specified cable object, or it is the name of an existing material property.

## Remarks

This function retrieves the material overwrite assigned to a cable object, if any. It returns None if there is no material overwrite assignment.

The function returns zero if the material overwrite assignment is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableMaterialOverwrite()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim PropName As String
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

   'add cable object by coordinates
      ret = SapModel.CableObj.AddByCoord(-300, 0, 0, -100, 0, 124, Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign material overwrite
      ret = SapModel.CableObj.SetMaterialOverwrite(Name, "4000Psi")

   'get material overwrite assignment
      ret = SapModel.CableObj.GetMaterialOverwrite(Name, PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMaterialOverwrite](SetMaterialOverwrite_{Cable_Object}.htm)



## GetModifiers {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetModifiers_{Cable_Object}.htm`*

# GetModifiers

## Syntax

SapObject.SapModel.CableObj.GetModifiers

## VB6 Procedure

Function GetModifiers(ByVal Name As String, ByRef Value() As Double) As Long

## Parameters

Name

The name of an existing cable object.

Value

This is an array of three unitless modifiers.

Value(0) = Cross sectional area modifier

Value(1) = Mass modifier

Value(2) = Weight modifier

## Remarks

This function retrieves the cable modifier assignment for cable objects. The default value for all modifiers is one.

The function returns zero if the modifier assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableModifiers()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double
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

   'assign modifiers
      ReDim Value(2)
      For i = 0 To 2
         Value(i) = 1
      Next i
      Value(0) = 100
      ret = SapModel.CableObj.SetModifiers(Name, Value)

   'get modifiers
      ReDim Value(2)
      ret = SapModel.CableObj.GetModifiers(Name, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetModifiers](SetModifiers_{Cable_Object}.htm)

[DeleteModifiers](DeleteModifiers_{Cable_Object}.htm)



## GetNameList {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetNameList_{Cable_Object}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.CableObj.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of cable object names retrieved by the program.

MyName

This is a one-dimensional array of cable object names. The MyName array is created as a dynamic, zero-based, array by the APIuser:

   Dim MyName() as String

The array is dimensioned to (NumberNames – 1) inside the Sap2000 program, filled with the names, and returned to the APIuser.

## Remarks

This function retrieves the names of all defined cable objects.

The function returns zero if the names are successfully retrieved, otherwise it returns nonzero.

## VBA Example

Sub GetCableObjectNames()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberNames As Long
      Dim MyName() As String
      Dim Name1 As String
      Dim Name2 As String

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
      ret = SapModel.CableObj.AddByPoint("1", "6", Name1)
      ret = SapModel.CableObj.AddByPoint("5", "10", Name2)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name1, 7, 1, 0, 0, 24)
      ret = SapModel.CableObj.SetCableData(Name2, 7, 1, 0, 0, 24)

   'get cable object names
      ret = SapModel.CableObj.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetOutputStations {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetOutputStations_{Cable_Object}.htm`*

# GetOutputStations

## Syntax

SapObject.SapModel.CableObj.GetOutputStations

## VB6 Procedure

Function GetOutputStations(ByVal Name As String, ByRef MyType As Long, ByRef MaxSegSize As Double, ByRef MinSections As Long, ByRef NoOutPutAndDesignAtElementEnds As Boolean, ByRef NoOutPutAndDesignAtPointLoads As Boolean) As Long

## Parameters

Name

The name of an existing cable object.

MyType

This is 1 or 2, indicating how the output stations are specified.

1 = maximum segment size, that is, maximum station spacing

2 = minimum number of stations

MaxSegSize

The maximum segment size, that is, the maximum station spacing. This item applies only when MyType = 1. [L]

MinSections

The minimum number of stations. This item applies only when MyType = 2.

NoOutPutAndDesignAtElementEnds

If this item is True, no additional output stations are added at the ends of line elements when the cable object is internally meshed.

NoOutPutAndDesignAtPointLoads

If this item is True, no additional output stations are added at point load locations.

## Remarks

This function retrieves cable object output station data.

The function returns zero if the data is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableOutputStationData()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyType As Long
      Dim MaxSegSize As Double
      Dim MinSections As Long
      Dim NoOutPutAndDesignAtElementEnds As Boolean
      Dim NoOutPutAndDesignAtPointLoads As Boolean
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

   'get cable output station data
      ret = SapModel.CableObj.GetOutputStations(Name, MyType, MaxSegSize, MinSections, NoOutPutAndDesignAtElementEnds, NoOutPutAndDesignAtPointLoads)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetOutputStations](SetOutputStations_{Cable_Object}.htm)



## GetPoints {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetPoints_{Cable_Object}.htm`*

# GetPoints

## Syntax

SapObject.SapModel.CableObj.GetPoints

## VB6 Procedure

Function GetPoints(ByVal Name As String, ByRef Point1 As String, ByRef Point2 As String) As Long

## Parameters

Name

The name of a defined cable object.

Point1

The name of the point object at the I-End of the specified cable object.

Point2

The name of the point object at the J-End of the specified cable object.

## Remarks

This function retrieves the names of the point objects at each end of a specified cable object.

The function returns zero if the point names are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableObjPoints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Point1 As String
      Dim Point2 As String
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

   'add cable object by coordinates
      ret = SapModel.CableObj.AddByCoord(-300, 0, 0, -100, 0, 124, Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'get names of points
      ret = SapModel.CableObj.GetPoints(Name, Point1, Point2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetProperty {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetProperty_{Cable_Object}.htm`*

# GetProperty

## Syntax

SapObject.SapModel.CableObj.GetProperty

## VB6 Procedure

Function GetProperty(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a defined cable object.

PropName

The name of the cable property assigned to the cable object.

## Remarks

This function retrieves the cable property assigned to a cable object.

The function returns zero if the cable object property is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableSectionProp()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim PropName As String
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

   'get cable property
      ret = SapModel.CableObj.GetProperty(Name, PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetProperty](SetProperty_{Cable_Object}.htm)



## GetSelected {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetSelected_{Cable_Object}.htm`*

# GetSelected

## Syntax

Sap2000.CableObj.GetSelected

## VB6 Procedure

Function GetSelected(ByVal Name As String, ByRef Selected As Boolean) As Long

## Parameters

Name

The name of an existing cable object.

Selected

This item returns True if the specified cable object is selected, otherwise it returns False.

## Remarks

This function retrieves the selected status for a cable object.

The function returns zero if the selected status is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetCableObjectSelectedStatus()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Selected As Boolean
      Dim Name1 As String
      Dim Name2 As String

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
      ret = SapModel.CableObj.AddByPoint("1", "6", Name1)
      ret = SapModel.CableObj.AddByPoint("5", "10", Name2)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name1, 7, 1, 0, 0, 24)
      ret = SapModel.CableObj.SetCableData(Name2, 7, 1, 0, 0, 24)

   'set all cables selected
      ret = SapModel.CableObj.SetSelected("All", True, Group)

   'get cable object selected status
      ret = SapModel.CableObj.GetSelected(Name1, Selected)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSelected](SetSelected_{Cable_Object}.htm)



## GetTransformationMatrix {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/GetTransformationMatrix_{Cable_Object}.htm`*

# GetTransformationMatrix

## Syntax

Sap2000.CableObj.GetTransformationMatrix

## VB6 Procedure

Function GetTransformationMatrix(ByVal Name As String, ByRef Value() As Double,Optional ByVal IsGlobal As Boolean = True) As Long

## Parameters

Name

The name of an existing cable object.

Value

Value is an array of nine direction cosines that define the transformation matrix.

The following matrix equation shows how the transformation matrix is used to convert items from the cable object local coordinate system to the global coordinate system.

![](../../../assets/images/Images/Transformation%20Matrix.JPG)

In the equation, c0 through c8 are the nine values from the transformation array, (Local1, Local2, Local3) are an item (such as a load) in the object local coordinate system, and (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.

The transformation from the local coordinate system to the present coordinate system is the same as that shown above for the global system if you substitute the present system for the global system.

IsGlobal

If this item is True, the transformation matrix is between the Global coordinate system and the cable object local coordinate system.

If this item is False, the transformation matrix is between the present coordinate system and the cable object local coordinate system.

## Remarks

The function returns zero if the cable object transformation matrix is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetCableObjectMatrix()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'get cable object transformation matrix
      ReDim Value(8)
      ret = SapModel.CableObj.GetTransformationMatrix(Name, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## SetCableData {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetCableData_{Cable_Object}.htm`*

# SetCableData

## Syntax

SapObject.SapModel.CableObj.SetCableData

## VB6 Procedure

Function SetCableData(ByVal Name As String, ByVal CableType As Long, ByVal NumSegs As Long, ByVal Weight As Double, ByVal ProjectedLoad As Double, ByVal Value As Double, Optional ByVal UseDeformedGeom As Boolean = False, Optional ByVal ModelUsingFrames As Boolean = False) As Long

## Parameters

Name

The name of a defined cable object.

CableType

This is 1, 2, 3, 4, 5, 6, 7, 8, or 9, indicating the cable definition parameter.

1 = Minimum tension at I-End

2 = Minimum tension at J-End

3 = Tension at I-End

4 = Tension at J-End

5 = Horizontal tension component

6 = Maximum vertical sag

7 = Low-point vertical sag

8 = Undeformed length

9 = Relative undeformed length

NumSegs

This is the number of segments into which the program internally divides the cable.

Weight

The added weight per unit length used when calculating the cable shape. [F/L]

ProjectedLoad

The projected uniform gravity load used when calculating the cable shape. [F/L]

Value

This is the value of the parameter used to define the cable shape. The item that Value represents depends on the CableType item.

CableType = 1: Not Used

CableType = 2: Not Used

CableType = 3: Tension at I-End [F]

CableType = 4: Tension at J-End [F]

CableType = 5: Horizontal tension component [F]

CableType = 6: Maximum vertical sag [L]

CableType = 7: Low-point vertical sag [L]

CableType = 8: Undeformed length [L]

CableType = 9: Relative undeformed length

UseDeformedGeom

If this item is True, the program uses the deformed geometry for the cable object; otherwise it uses the undeformed geometry.

ModelUsingFrames

If this item is True, the analysis model uses frame elements to model the cable instead of using cable elements.

## Remarks

This function assigns the cable definition parameters to a cable object.

The function returns zero if the cable object is successfully defined; otherwise it returns a nonzero value. If the cable object is not successfully defined, it may be deleted.

## VBA Example

Sub SetCableDefinitionData()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Modified optional arguments UseDeformedGeom and ModelUsingFrames to both be ByVal in version 12.0.1.

## See Also

[AddByCoord](AddByCoord_{Cable_Object}.htm)

[AddByPoint](AddByPoint_{Cable_Object}.htm)

[GetCableData](GetCableData_{Cable_Object}.htm)

[GetCableGeometry](GetCableGeometry_{Cable_Object}.htm)



## SetGUID {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetGUID_{Cable_Object}.htm`*

# SetGUID

## Syntax

SapObject.SapModel.CableObj.SetGUID

## VB6 Procedure

Function SetGUID(ByVal Name As String, Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing cable object.

GUID

The GUID (Global Unique ID) for the specified cable object.

## Remarks

This function sets the GUID for the specified cable object. If the GUID is passed in as a blank string, the program automatically creates a GUID for the object.

This function returns zero if the cable object GUID is successfully set; otherwise it returns nonzero.

## VBA Example

Sub SetCableObjGUID()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'set program created GUID
      ret = SapObject.SapModel.CableObj.SetGUID(Name)

   'get GUID
      ret = SapObject.SapModel.CableObj.GetGUID(Name, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[GetGUID](GetGUID_{Cable_Object}.htm)



## SetGroupAssign {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetGroupAssign_{Cable_Object}.htm`*

# SetGroupAssign

## Syntax

SapObject.SapModel.CableObj.SetGroupAssign

## VB6 Procedure

Function SetGroupAssign(ByVal Name As String, ByVal GroupName As String, Optional  By Val Remove As Boolean = False, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

GroupName

The name of an existing group to which the assignment is made.

Remove

If this item is False, the specified cable objects are added to the group specified by the GroupName item. If it is True, the cable objects are removed from the group.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the cable object specified by the Name item is added or removed from the group specified by the GroupName item.

If this item is Group, all cable objects in the group specified by the Name item are added or removed from the group specified by the GroupName item.

If this item is SelectedObjects, all selected cable objects are added or removed from the group specified by the GroupName item, and the Name item is ignored.

## Remarks

This function adds or removes cable objects from a specified group.

The function returns zero if the group assignment is successful, otherwise it returns a nonzero value.

## VBA Example

Sub AddCableObjectsToGroup()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name1 As String
      Dim Name2 As String

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
      ret = SapModel.CableObj.AddByPoint("1", "6", Name1)
      ret = SapModel.CableObj.AddByPoint("5", "10", Name2)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name1, 7, 1, 0, 0, 24)
      ret = SapModel.CableObj.SetCableData(Name2, 7, 1, 0, 0, 24)

   'define new group
      ret = SapModel.GroupDef.SetGroup("Group1")

   'add cable objects to group
      ret = SapModel.CableObj.SetGroupAssign(Name1, "Group1")
      ret = SapModel.CableObj.SetGroupAssign(Name2, "Group1")

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

[GetGroupAssign](GetGroupAssign_{Cable_Object}.htm)



## SetLoadDeformation {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetLoadDeformation_{Cable_Object}.htm`*

# SetLoadDeformation

## Syntax

SapObject.SapModel.CableObj.SetLoadDeformation

## VB6 Procedure

Function SetLoadDeformation(ByVal Name As String, ByVal LoadPat As String, ByRef d As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

d

This is the axial deformation load value. [L]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function assigns deformation loads to cable objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableDeformationLoad()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable deformation loads
      ret = SapModel.CableObj.SetLoadDeformation("ALL", "DEAD", 2, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDeformation](GetLoadDeformation_{Cable_Object}.htm)

[DeleteLoadDeformation](DeleteLoadDeformation_{Cable_Object}.htm)



## SetLoadDistributed {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetLoadDistributed_{Cable_Object}.htm`*

# SetLoadDistributed

## Syntax

SapObject.SapModel.CableObj.SetLoadDistributed

## VB6 Procedure

Function SetLoadDistributed(ByVal Name As String, ByVal LoadPat As String, ByVal MyType As Long, ByVal Dir As Long, ByVal Value As Double, Optional ByVal CSys As String = "Global", Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

MyType

This is 1 or 2, indicating the type of distributed load.

1 = Force per unit length

2 = Moment per unit length

Dir

This is 1, 2, 3, 4, 5, 6 or 10, indicating the direction of the load.

1 = Local 1 axis (only applies when CSys is Local)

2 = Local 2 axis (only applies when CSys is Local)

3 = Local 3 axis (only applies when CSys is Local)

4 = X direction (does not apply when CSys is Local)

5 = Y direction (does not apply when CSys is Local)

6 = Z direction (does not apply when CSys is Local)

10 = Gravity direction (only applies when CSys is Global)

The positive gravity direction (see Dir = 10) is in the negative Global Z direction.

Value

This is the load value of the distributed load. The distributed load is applied over the full length of the cable. [F/L] when MyType is 1 and [FL/L] when MyType is 2

CSys

This is Local or the name of a defined coordinate system. It is the coordinate system in which the loads are specified.

Replace

If this item is True, all previous loads, if any, assigned to the specified cable object(s), in the specified load pattern, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function assigns uniform distributed loads over the full length of cable objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableDistributedLoad()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable distributed load
      ret = SapModel.CableObj.SetLoadDistributed(Name, "DEAD", 1, 10, 0.08)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDistributed](GetLoadDistributed_{Cable_Object}.htm)

[DeleteLoadDistributed](../../../DeleteLoadDistributedWithGUID.htm)



## SetLoadGravity {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetLoadGravity_{Cable_Object}.htm`*

# SetLoadGravity

## Syntax

SapObject.SapModel.CableObj.SetLoadGravity

## VB6 Procedure

Function SetLoadGravity(ByVal Name As String, ByVal LoadPat As String, ByVal x As Double, ByVal y As Double, ByVal z As Double, Optional ByVal Replace As Boolean = True, Optional ByVal CSys As String = "Global", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

x, y, z

These are the gravity load multipliers in the x, y and z directions of the specified coordinate system.

Replace

If this item is True, all previous gravity loads, if any, assigned to the specified cable object(s), in the specified load pattern, are deleted before making the new assignment.

CSys

The coordinate system in which the x, y and z multipliers are specified.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function assigns gravity load multipliers to cable objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableGravityLoad()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable gravity loads
      ret = SapModel.CableObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Cable_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Cable_Object}.htm)



## SetLoadStrain {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetLoadStrain_{Cable_Object}.htm`*

# SetLoadStrain

## Syntax

SapObject.SapModel.CableObj.SetLoadStrain

## VB6 Procedure

Function SetLoadStrain(ByVal Name As String, ByVal LoadPat As String, ByVal Strain As Double, Optional ByVal Replace As Boolean = True, Optional ByVal PatternName As String = "", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Strain

This is the axial strain load value. [L/L]

Replace

If this item is True, all previous strain loads, if any, assigned to the specified cable object(s), in the specified load pattern, are deleted before making the new assignment.

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the strain load for the cable object is uniform along the object at the value specified by Strain.

If PatternName is the name of a defined joint pattern, the strain load for the cable object is based on the specified strain value multiplied by the pattern value at the joints at each end of the cable object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function assigns strain loads to cable objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableStrainLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create apModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret= SapModel.InitializeNewModel

   'create model from template
      ret= SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add cable object by points
      ret= SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret= SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable strain load
      ret= SapModel.CableObj.SetLoadStrain(Name, "DEAD", 0.001)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadStrain](GetLoadStrain_{Cable_Object}.htm)

[DeleteLoadStrain](DeleteLoadStrain_{Cable_Object}.htm)



## SetLoadTargetForce {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetLoadTargetForce_{Cable_Object}.htm`*

# SetLoadTargetForce

## Syntax

SapObject.SapModel.CableObj.SetLoadTargetForce

## VB6 Procedure

Function SetLoadTargetForce(ByVal Name As String, ByVal LoadPat As String, ByRef P As Double, ByRef RD As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

P

This is the axial target force value. [F]

RD

This is the relative distance along the cable object to the location where the target force value applies. The relative distance must be between 0 and 1, 0 <= RD <=1.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function assigns target forces to cable objects.

The function returns zero if the target forces are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableTargetForce()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable target force
      ret = SapModel.CableObj.SetLoadTargetForce(Name, "DEAD", 50, 0.5)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTargetForce](GetLoadTargetForce_{Cable_Object}.htm)

[DeleteLoadTargetForce](DeleteLoadTargetForce_{Cable_Object}.htm)



## SetLoadTemperature {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetLoadTemperature_{Cable_Object}.htm`*

# SetLoadTemperature

## Syntax

SapObject.SapModel.CableObj.SetLoadTemperature

## VB6 Procedure

Function SetLoadTemperature(ByVal Name As String, ByVal LoadPat As String, ByVal Val As Double, Optional ByVal PatternName As String = "", Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Val

This is the temperature change value. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the temperature load for the cable object is uniform along the object at the value specified by Val.

If PatternName is the name of a defined joint pattern, the temperature load for the cable object is based on the specified temperature value multiplied by the pattern value at the joints at each end of the cable object.

Replace

If this item is True, all previous temperature loads, if any, assigned to the specified cable object(s), in the specified load case, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function assigns temperature loads to cable objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableTemperatureLoad()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable temperature load
      ret = SapModel.CableObj.SetLoadTemperature("ALL", "DEAD", 50, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTemperature](GetLoadTemperature_{Cable_Object}.htm)

[DeleteLoadTemperature](DeleteLoadTemperature_{Cable_Object}.htm)



## SetMass {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetMass_{Cable_Object}.htm`*

# SetMass

## Syntax

SapObject.SapModel.CableObj.SetMass

## VB6 Procedure

Function SetMass(ByVal Name As String, ByVal MassOverL As Double, Optional ByVal Replace As Boolean = False, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

MassOverL

The mass per unit length assigned to the cable object. [M/L]

Replace

If this item is True, all existing mass assignments to the cable object are removed before assigning the specified mas. If it is False, the specified mass is added to any mass already assigned to the cable object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function assigns mass per unit length to cable objects.

The function returns zero if the mass is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableMass()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable mass
      ret = SapModel.CableObj.SetMass("ALL", .0001, False, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMass](GetMass_{Cable_Object}.htm)

[DeleteMass](DeleteMass_{Cable_Object}.htm)



## SetMatTemp {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetMatTemp_{Cable_Object}.htm`*

# SetMatTemp

## Syntax

SapObject.SapModel.CableObj.SetMatTemp

## VB6 Procedure

Function SetMatTemp(ByVal Name As String, ByVal Temp As Double, Optional ByVal PatternName As String = "", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

Temp

This is the material temperature value assigned to the cable object. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the material temperature for the cable object is uniform along the object at the value specified by Temp.

If PatternName is the name of a defined joint pattern, the material temperature for the cable object may vary from one end to the other. The material temperature at each end of the object is equal to the specified temperature multiplied by the pattern value at the joint at the end of the cable object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function assigns material temperatures to cable objects.

The function returns zero if the material temperatures are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableMatTemp()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign material temperature
      ret = SapModel.CableObj.SetMatTemp("ALL", 50, , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMatTemp](GetMatTemp_{Cable_Object}.htm)



## SetMaterialOverwrite {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetMaterialOverwrite_{Cable_Object}.htm`*

# SetMaterialOverwrite

## Syntax

SapObject.SapModel.CableObj.SetMaterialOverwrite

## VB6 Procedure

Function SetMaterialOverwrite(ByVal Name As String, ByVal PropName As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

PropName

This is None or a blank string, indicating that any existing material overwrites assigned to the specified cable objects are to be removed, or it is the name of an existing material property.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function sets the material overwrite assignment for cable objects.

The function returns zero if the material overwrite assignment is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableMaterialOverwrite()
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

   'add cable object by coordinates
      ret = SapModel.CableObj.AddByCoord(-300, 0, 0, -100, 0, 124, Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign material overwrite
      ret = SapModel.CableObj.SetMaterialOverwrite(Name, "4000Psi")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMaterialOverwrite](GetMaterialOverwrite_{Cable_Object}.htm)



## SetModifiers {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetModifiers_{Cable_Object}.htm`*

# SetModifiers

## Syntax

SapObject.SapModel.CableObj.SetModifiers

## VB6 Procedure

Function SetModifiers(ByVal Name As String, ByRef Value() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

Value

This is an array of three unitless modifiers.

Value(0) = Cross sectional area modifier

Value(1) = Mass modifier

Value(2) = Weight modifier

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function sets the cable modifier assignment for cable objects. The default value for all modifiers is one.

The function returns zero if the modifier assignments are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableModifiers()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Double
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

   'assign modifiers
      ReDim Value(2)
      For i = 0 To 2
         Value(i) = 1
      Next i
      Value(0) = 100
      ret = SapModel.CableObj.SetModifiers(Name, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetModifiers](GetModifiers_{Cable_Object}.htm)

[DeleteModifiers](DeleteModifiers_{Cable_Object}.htm)



## SetOutputStations {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetOutputStations_{Cable_Object}.htm`*

# SetOutputStations

## Syntax

SapObject.SapModel.CableObj.SetOutputStations

## VB6 Procedure

Function SetOutputStations(ByVal Name As String, ByVal MyType As Long, ByVal MaxSegSize As Double, ByVal MinSections As Long, Optional ByVal NoOutPutAndDesignAtElementEnds As Boolean, Optional ByVal NoOutPutAndDesignAtPointLoads As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

MyType

This is 1 or 2, indicating how the output stations are specified.

1 = maximum segment size, that is, maximum station spacing

2 = minimum number of stations

MaxSegSize

The maximum segment size, that is, the maximum station spacing. This item applies only when MyType = 1. [L]

MinSections

The minimum number of stations. This item applies only when MyType = 2.

NoOutPutAndDesignAtElementEnds

If this item is True, no additional output stations are added at the ends of line elements when the cable object is internally meshed.

NoOutPutAndDesignAtPointLoads

If this item is True, no additional output stations are added at point load locations.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function assigns cable object output station data.

The function returns zero if the data is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCableOutputStationData()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'assign cable output station data
      ret = SapModel.CableObj.SetOutputStations(Name, 1, 18, 0)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetOutputStations](GetOutputStations_{Cable_Object}.htm)



## SetProperty {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetProperty_{Cable_Object}.htm`*

# SetProperty

## Syntax

SapObject.SapModel.CableObj.SetProperty

## VB6 Procedure

Function SetProperty(ByVal name As String, ByVal PropName As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

PropName

The name of a cable property to be assigned to the specified cable object(s).

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the cable object specified by the Name item.

If this item is Group, the assignment is made to all cable objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected cable objects, and the Name item is ignored.

## Remarks

This function assigns a cable property to a cable object.

The function returns zero if the cable property is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub SetCableSectionProp()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim FileName As String
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

   'set cable property
      ret = SapModel.CableObj.SetProperty(Name, "CAB1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetProperty](GetProperty_{Cable_Object}.htm)



## SetSelected {Cable Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Cable_Object/SetSelected_{Cable_Object}.htm`*

# SetSelected

## Syntax

Sap2000.CableObj.SetSelected

## VB6 Procedure

Function SetSelected(ByVal Name As String, ByVal Selected As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing cable object or group, depending on the value of the ItemType item.

Selected

This item is True if the specified cable object is selected, otherwise it is False.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the selected status is set for the cable object specified by the Name item.

If this item is Group, the selected status is set for all cable objects in the group specified by the Name item.

If this item is SelectedObjects, the selected status is set for all selected cable objects, and the Name item is ignored.

## Remarks

This function sets the selected status for a cable object.

The function returns zero if the selected status is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetCableObjectSelected()
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

   'add cable object by points
      ret = SapModel.CableObj.AddByPoint("1", "6", Name)

   'set cable data
      ret = SapModel.CableObj.SetCableData(Name, 7, 1, 0, 0, 24)

   'set cable object selected
      ret = SapModel.CableObj.SetSelected(Name, True)

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

[GetSelected](GetSelected_{Cable_Object}.htm)

