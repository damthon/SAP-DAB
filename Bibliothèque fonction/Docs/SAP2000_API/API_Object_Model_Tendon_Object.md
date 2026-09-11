# API Object Model Tendon Object

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Object_Model/Tendon_Object

---



## AddByCoord {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/AddByCoord_{Tendon_Object}.htm`*

# AddByCoord

## Syntax

SapObject.SapModel.TendonObj.AddByCoord

## VB6 Procedure

Function AddByCoord(ByVal xi As Double, ByVal yi As Double, ByVal zi As Double, ByVal xj As Double, ByVal yj As Double, ByVal zj As Double, ByRef Name As String, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "", Optional ByVal CSys As String = "Global") As Long

## Parameters

xi, yi, zi

The coordinates of the I-End of the added tendon object. The coordinates are in the coordinate system defined by the CSys item.

xj, yj, zj

The coordinates of the J-End of the added tendon object. The coordinates are in the coordinate system defined by the CSys item.

Name

This is the name that the program ultimately assigns for the tendon object. If no UserName is specified, the program assigns a default name to the tendon object. If a UserName is specified and that name is not used for another frame, cable or tendon object, the UserName is assigned to the tendon object; otherwise a default name is assigned to the tendon object.

PropName

This is Default, None or the name of a defined tendon property.

If it is Default, the program assigns a default tendon property to the tendon object. If it is None, no tendon property is assigned to the tendon object. If it is the name of a defined tendon property, that property is assigned to the tendon object.

UserName

This is an optional user specified name for the tendon object. If a UserName is specified and that name is already used for another tendon object, the program ignores the UserName.

CSys

The name of the coordinate system in which the tendon object end point coordinates are defined.

## Remarks

This function adds a new tendon object whose end points are at the specified coordinates.

The function returns zero if the tendon object is successfully added, otherwise it returns a nonzero value.

## VBA Example

Sub AddTendonObjByCoord()
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

   'add tendon object by coordinates
      ret = SapModel.TendonObj.AddByCoord(-288, 0, 288, 288, 0, 288, Name)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByPoint](AddByPoint_{Tendon_Object}.htm)

[SetTendonData](SetTendonData.htm)



## AddByPoint {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/AddByPoint_{Tendon_Object}.htm`*

# AddByPoint

## Syntax

SapObject.SapModel.TendonObj.AddByPoint

## VB6 Procedure

Function AddByPoint(ByVal Point1 as String, ByVal Point2 as String, ByRef Name As String, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "") As Long

## Parameters

Point1

The name of a defined point object at the I-End of the added tendon object.

Point2

The name of a defined point object at the J-End of the added tendon object.

Name

This is the name that the program ultimately assigns for the tendon object. If no UserName is specified, the program assigns a default name to the tendon object. If a UserName is specified and that name is not used for another frame, cable or tendon object, the UserName is assigned to the tendon object; otherwise a default name is assigned to the tendon object.

PropName

This is Default, None or the name of a defined tendon property.

If it is Default, the program assigns a default tendon property to the tendon object. If it is None, no tendon property is assigned to the tendon object. If it is the name of a defined tendon property, that property is assigned to the tendon object.

UserName

This is an optional user specified name for the tendon object. If a UserName is specified and that name is already used for another tendon object, the program ignores the UserName.

## Remarks

This function adds a new tendon object whose end points are specified by name.

The function returns zero if the tendon object is successfully added, otherwise it returns a nonzero value.

## VBA Example

Sub AddTendonObjByPoint()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Tendon_Object}.htm)

[SetTendonData](SetTendonData.htm)



## ChangeName {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/ChangeName_{Tendon_Object}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.TendonObj.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a defined tendon object.

NewName

The new name for the tendon object.

## Remarks

The function returns zero if the new name is successfully applied, otherwise it returns a nonzero value.

## VBA Example

Sub ChangeTendonObjName()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'change name
      ret = SapModel.TendonObj.ChangeName(Name, "MyTendon")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## Count {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/Count_{Tendon_Object}.htm`*

# Count

## Syntax

SapObject.SapModel.TendonObj.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None

## Remarks

This function returns a count of the tendon objects in the model.

## VBA Example

Sub CountTendonObjects()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'return number of tendon objects
      Count = SapModel.TendonObj.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## DeleteLoadDeformation {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/DeleteLoadDeformation_{Tendon_Object}.htm`*

# DeleteLoadDeformation

## Syntax

SapObject.SapModel.TendonObj.DeleteLoadDeformation

## VB6 Procedure

Function DeleteLoadDeformation(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the tendon object specified by the Name item.

If this item is Group, the load assignments are deleted for all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected tendon objects and the Name item is ignored.

## Remarks

This function deletes the deformation load assignments to the specified tendon objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteTendonDeformationLoad()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon deformation loads
      ret = SapModel.TendonObj.SetLoadDeformation("ALL", "DEAD", 2, Group)

   'delete tendon deformation load
      ret = SapModel.TendonObj.DeleteLoadDeformation(Name, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDeformation](GetLoadDeformation_{Tendon_Object}.htm)

[SetLoadDeformation](SetLoadDeformation_{Tendon_Object}.htm)



## DeleteLoadForceStress {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/DeleteLoadForceStress_{Tendon_Object}.htm`*

# DeleteLoadForceStress

## Syntax

SapObject.SapModel.TendonObj.DeleteLoadForceStress

## VB6 Procedure

Function DeleteLoadForceStress(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the tendon object specified by the Name item.

If this item is Group, the load assignments are deleted for all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected tendon objects, and the Name item is ignored.

## Remarks

This function deletes the tendon force/stress load assignments to the specified tendon objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteTendonForceLoad()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon force load
      ret = SapModel.TendonObj.SetLoadForceStress("ALL", "DEAD", 1, 0, 100, 0.15, 8.333E-05, 0.25, 3, 5, 7, 5, , Group)

   'delete tendon force load
      ret = SapModel.TendonObj.DeleteLoadForceStress(Name, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadForceStress](GetLoadForceStress.htm)

[SetLoadForceStress](SetLoadForceStress.htm)



## DeleteLoadGravity {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/DeleteLoadGravity_{Tendon_Object}.htm`*

# DeleteLoadGravity

## Syntax

SapObject.SapModel.TendonObj.DeleteLoadGravity

## VB6 Procedure

Function DeleteLoadGravity(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the tendon object specified by the Name item.

If this item is Group, the load assignments are deleted for all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected tendon objects, and the Name item is ignored.

## Remarks

This function deletes the gravity load assignments to the specified tendon objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteTendonGravityLoad()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon gravity loads
      ret = SapModel.TendonObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'delete tendon gravity load
      ret = SapModel.TendonObj.DeleteLoadGravity(Name, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Tendon_Object}.htm)

[SetLoadGravity](SetLoadGravity_{Tendon_Object}.htm)



## DeleteLoadStrain {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/DeleteLoadStrain_{Tendon_Object}.htm`*

# DeleteLoadStrain

## Syntax

SapObject.SapModel.TendonObj.DeleteLoadStrain

## VB6 Procedure

Function DeleteLoadStrain(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the tendon object specified by the Name item.

If this item is Group, the load assignments are deleted for all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected tendon objects, and the Name item is ignored.

## Remarks

This function deletes the strain load assignments to the specified tendon objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteTendonStrainLoad()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon strain load
      ret = SapModel.TendonObj.SetLoadStrain(Name, "DEAD", 0.001)

   'delete tendon strain load
      ret = SapModel.TendonObj.DeleteLoadStrain(Name, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadStrain](GetLoadStrain_{Tendon_Object}.htm)

[SetLoadStrain](SetLoadStrain_{Tendon_Object}.htm)



## DeleteLoadTemperature {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/DeleteLoadTemperature_{Tendon_Object}.htm`*

# DeleteLoadTemperature

## Syntax

SapObject.SapModel.TendonObj.DeleteLoadTemperature

## VB6 Procedure

Function DeleteLoadTemperature(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the tendon object specified by the Name item.

If this item is Group, the load assignments are deleted for all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected tendon objects, and the Name item is ignored.

## Remarks

This function deletes the temperature load assignments to the specified tendon objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteTendonTemperatureLoad()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon temperature load
      ret = SapModel.TendonObj.SetLoadTemperature("ALL", "DEAD", 50, , , Group)

   'delete tendon temperature load
      ret = SapModel.TendonObj.DeleteLoadTemperature(Name, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTemperature](GetLoadTemperature_{Tendon_Object}.htm)

[SetLoadTemperature](SetLoadTemperature_{Tendon_Object}.htm)



## Delete {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/Delete_{Tendon_Object}.htm`*

# Delete

## Syntax

SapObject.SapModel.TendonObj.Delete

## VB6 Procedure

Function Delete(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the tendon object specified by the Name item is deleted.

If this item is Group, all of the tendon objects in the group specified by the Name item are deleted.

If this item is SelectedObjects, all selected tendon objects are deleted, and the Name item is ignored.

## Remarks

The function deletes tendon objects.

The function returns zero if the tendon objects are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeleteTendonObj()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon objects by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name1)
      ret = SapModel.TendonObj.AddByPoint("2", "8", Name2)

   'update view
      ret = SapModel.View.RefreshView(0, False)

   'delete tendon object
      ret = SapModel.TendonObj.Delete(Name1)

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

[AddByCoord](AddByCoord_{Tendon_Object}.htm)

[AddByPoint](AddByPoint_{Tendon_Object}.htm)



## GetDiscretization {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetDiscretization_{Tendon_Object}.htm`*

# GetDiscretization

## Syntax

SapObject.SapModel.TendonObj.GetDiscretization

## VB6 Procedure

Function GetDiscretization(ByVal Name As String, ByRef Value As Double) As Long

## Parameters

Name

The name of an existing tendon object.

Value

The maximum discretization length for the tendon. [L]

## Remarks

This function retrieves the maximum discretization length assignment for tendon objects.

The function returns zero if the assignment is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonMaxDiscretizationLength()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'get tendon maximum discretization length
      ret = SapModel.TendonObj.GetDiscretization(Name, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetDiscretization](SetDiscretization.htm)



## GetElm {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetElm_{Tendon_Object}.htm`*

# GetElm

## Syntax

SapObject.SapModel.TendonObj.GetElm

## VB6 Procedure

Function GetElm(ByVal Name As String, ByRef nelm As Long, ByRef Elm() as String, ByRef RDI() As Double, ByRef RDJ() As Double) As Long

## Parameters

Name

The name of an existing tendon object.

nelm

The number of line elements created from the specified tendon object.

Elm

An array that includes the name of a line element created from the specified tendon object.

RDI

An array that includes the relative distance along the tendon object to the I-End of the line element.

RDJ

An array that includes the relative distance along the tendon object to the J-End of the line element.

## Remarks

This function retrieves the names of the line elements (analysis model lines) associated with a specified tendon object in the object-based model. It also retrieves information about the location of the line elements along the tendon object.

This function returns zero if the line element information is successfully returned; otherwise it returns nonzero. An error occurs if the analysis model does not currently exist.

## VBA Example

Sub GetLineElementInfoForTendonObject()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon force load
      ret = SapModel.TendonObj.SetLoadForceStress("ALL", "DEAD", 1, 0, 100, 0.15, 8.333E-05, 0.25, 3, 5, 7, 5, , Group)

   'create the analysis model
      ret = SapModel.Analyze.CreateAnalysisModel

   'get line element information
      ret = SapModel.TendonObj.GetElm(Name, nelm, Elm, RDI, RDJ)

   'Note:  The above returns 0 elements because the tendon is specified to be modelled using loads, not elements

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetGUID {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetGUID_{Tendon_Object}.htm`*

# GetGUID

## Syntax

SapObject.SapModel.TendonObj.GetGUID

## VB6 Procedure

Function GetGUID(ByVal name As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing tendon object.

GUID

The GUID (Global Unique ID) for the specified tendon object.

## Remarks

This function retrieves the GUID for the specified tendon object.

This function returns zero if the tendon object GUID is successfully retrieved; otherwise it returns nonzero.

## VBA Example

Sub GetTendonObjGUID()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'set program created GUID
      ret = SapObject.SapModel.TendonObj.SetGUID(Name)

   'get GUID
      ret = SapObject.SapModel.TendonObj.GetGUID(Name, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetGUID](SetGUID_{Tendon_Object}.htm)



## GetGroupAssign {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetGroupAssign_{Tendon_Object}.htm`*

# GetGroupAssign

## Syntax

SapObject.SapModel.TendonObj.GetGroupAssign

## VB6 Procedure

Function GetGroupAssign(ByVal Name As String, ByRef NumberGroups As Long, ByRef Groups() As String) ) As Long

## Parameters

Name

The name of an existing tendon object.

NumberGroups

The number of group names retrieved.

Groups

The names of the groups to which the tendon object is assigned.

## Remarks

This function retrieves the names of the groups to which a specified tendon object is assigned.

The function returns zero if the group assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonObjectGroups()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name1 As String
      Dim Name2 As String
      Dim NumberPoints As Long
      Dim MyType() As Long
      Dim x() As Double
      Dim y() As Double
      Dim z() As Double
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name1)
      ret = SapModel.TendonObj.AddByPoint("2", "8", Name2)

   'set tendon geometry
      NumberPoints = 3
      ReDim MyType(NumberPoints - 1)
      ReDim x(NumberPoints - 1)
      ReDim y(NumberPoints - 1)
      ReDim z(NumberPoints - 1)
      MyType(0) = 1
      MyType(1) = 7
      MyType(2) = 6
      x(0) = 0:  y(0) = 0
      x(1) = 288:  y(1) = -12
      x(2) = 576:  y(2) = 0
      ret = SapModel.TendonObj.SetTendonData(Name1, NumberPoints, MyType, x, y, z, "Local")
      ret = SapModel.TendonObj.SetTendonData(Name2, NumberPoints, MyType, x, y, z, "Local")

   'define new groups
      ret = SapModel.GroupDef.SetGroup("Group1")

      ret = SapModel.GroupDef.SetGroup("Group2")

   'add tendon object to groups
      ret = SapModel.TendonObj.SetGroupAssign(Name2, "Group1")
      ret = SapModel.TendonObj.SetGroupAssign(Name2, "Group2")

   'get tendon object groups
      ret = SapModel.TendonObj.GetGroupAssign(Name2, NumberGroups, Groups)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v. 20.0.0.

## See Also

[SetGroupAssign](SetGroupAssign_{Tendon_Object}.htm)



## GetLoadDeformation {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetLoadDeformation_{Tendon_Object}.htm`*

# GetLoadDeformation

## Syntax

SapObject.SapModel.TendonObj.GetLoadDeformation

## VB6 Procedure

Function GetLoadDeformation(ByVal Name As String, ByRef NumberItems As Long, ByRef TendonName() As String, ByRef LoadPat() As String, ByRef U1() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

NumberItems

The total number of deformation loads retrieved for the specified tendon objects.

TendonName

This is an array that includes the name of the tendon object associated with each deformation load.

LoadPat

This is an array that includes the name of the load pattern associated with each deformation load.

U1

This is an array of axial deformation load values. [L]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the tendon object specified by the Name item.

If this item is Group, the assignments are retrieved for all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected tendon objects, and the Name item is ignored.

## Remarks

This function retrieves the deformation load assignments to tendon objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonDeformationLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim TendonName() As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon deformation loads
      ret = SapModel.TendonObj.SetLoadDeformation("ALL", "DEAD", 2, Group)

   'get tendon deformation loads
      ret = SapModel.TendonObj.GetLoadDeformation(Name, NumberItems, TendonName, LoadPat, U1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadDeformation](SetLoadDeformation_{Tendon_Object}.htm)

[DeleteLoadDeformation](DeleteLoadDeformation_{Tendon_Object}.htm)



## GetLoadForceStress

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetLoadForceStress.htm`*

# GetLoadForceStress

## Syntax

SapObject.SapModel.TendonObj.GetLoadForceStress

## VB6 Procedure

Function GetLoadForceStress(ByVal Name As String, ByRef NumberItems As Long, ByRef TendonName() As String, ByRef LoadPat() As String, ByRef JackFrom() As Long, ByRef LoadType() As Long, ByRef Value() As Double, ByRef CurvatureCoeff() As Double, ByRef WobbleCoeff() As Double, ByRef LossAnchorage() As Double, ByRef LossShortening() As Double, ByRef LossCreep() As Double, ByRef LossShrinkage() As Double, ByRef LossSteelRelax() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

NumberItems

The total number of temperature loads retrieved for the specified tendon objects.

TendonName

This is an array that includes the name of the tendon object associated with each temperature load.

LoadPat

This is an array that includes the name of the load pattern associated with each temperature load.

JackFrom

This is an array that includes 1, 2 or 3, indicating how the tendon is jacked.

1 = Tendon jacked from I-End

2 = Tendon jacked from J-End

3 = Tendon jacked from both ends

LoadType

This is an array that includes either 0 or 1, indicating how the type of load.

0 = Force

1 = Stress

Value

This is an array that includes the load value. [F] when LoadType is 0, and [F/L2] when Loadtype is 1

CurvatureCoeff

This is an array that includes the curvature coefficient used when calculating friction losses.

WobbleCoeff

This is an array that includes the wobble coefficient used when calculating friction losses. [1/L]

LossAnchorage

This is an array that includes the anchorage set slip. [L]

LossShortening

This is an array that includes the tendon stress loss due to elastic shortening. [F/L2]

LossCreep

This is an array that includes the tendon stress loss due to creep. [F/L2]

LossShrinkage

This is an array that includes the tendon stress loss due to shrinkage. [F/L2]

LossSteelRelax

This is an array that includes the tendon stress loss due to tendon steel relaxation. [F/L2]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the tendon object specified by the Name item.

If this item is Group, the assignments are retrieved for all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected tendon objects, and the Name item is ignored.

## Remarks

This function retrieves the force/stress load assignments to tendon objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonForceLoad()
   'dimensionvariables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberItems As Long
      Dim TendonName() As String
      Dim LoadPat() As String
      Dim JackFrom() As Long
      Dim LoadType() As Long
      Dim Value() As Double
      Dim CurvatureCoeff() As Double
      Dim WobbleCoeff() As Double
      Dim LossAnchorage() As Double
      Dim LossShortening() As Double
      Dim LossCreep() As Double
      Dim LossShrinkage() As Double
      Dim LossSteelRelax() As Double

   'createSap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'startSap2000 application
      SapObject.ApplicationStart

   'createSapModel object
      Set SapModel = SapObject.SapModel

   'initializemodel
      ret = SapModel.InitializeNewModel

   'createmodel from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon force load
      ret = SapModel.TendonObj.SetLoadForceStress("ALL", "DEAD", 1, 0, 100, 0.15, 8.333E-05, 0.25, 3, 5, 7, 5, , Group)

   'get tendon force load
      ret = SapModel.TendonObj.GetLoadForceStress(Name, NumberItems, TendonName, LoadPat, JackFrom, LoadType, Value, CurvatureCoeff, WobbleCoeff, LossAnchorage, LossShortening, LossCreep, LossShrinkage, LossSteelRelax)

   'closeSap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadForceStress](SetLoadForceStress.htm)

[DeleteLoadForceStress](DeleteLoadForceStress_{Tendon_Object}.htm)



## GetLoadGravity {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetLoadGravity_{Tendon_Object}.htm`*

# GetLoadGravity

## Syntax

SapObject.SapModel.TendonObj.GetLoadGravity

## VB6 Procedure

Function GetLoadGravity(ByVal Name As String, ByRef NumberItems As Long, ByRef TendonName() As String, ByRef LoadPat() As String, ByRef CSys() As String, ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

NumberItems

The total number of gravity loads retrieved for the specified tendon objects.

TendonName

This is an array that includes the name of the tendon object associated with each gravity load.

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

If this item is Object, the assignments are retrieved for the tendon object specified by the Name item.

If this item is Group, the assignments are retrieved for all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected tendon objects, and the Name item is ignored.

## Remarks

This function retrieves the gravity load assignments to tendon objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonGravityLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim TendonName() As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon gravity loads
      ret = SapModel.TendonObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'get tendon gravity load
      ret = SapModel.TendonObj.GetLoadGravity(Name, NumberItems, TendonName, LoadPat, CSys, x, y, z)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadGravity](SetLoadGravity_{Tendon_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Tendon_Object}.htm)



## GetLoadStrain {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetLoadStrain_{Tendon_Object}.htm`*

# GetLoadStrain

## Syntax

SapObject.SapModel.TendonObj.GetLoadStrain

## VB6 Procedure

Function GetLoadStrain(ByVal Name As String, ByRef NumberItems As Long, ByRef TendonName() As String, ByRef LoadPat() As String, ByRef Strain() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

NumberItems

The total number of strain loads retrieved for the specified tendon objects.

TendonName

This is an array that includes the name of the tendon object associated with each strain load.

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

If this item is Object, the assignments are retrieved for the tendon object specified by the Name item.

If this item is Group, the assignments are retrieved for all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected tendon objects, and the Name item is ignored.

## Remarks

This function retrieves the strain load assignments to tendon objects.

The function returns zero if the strain load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonStrainLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim TendonName() As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon strain load
      ret = SapModel.TendonObj.SetLoadStrain(Name, "DEAD", 0.001)

   'get tendon strain load
      ret = SapModel.TendonObj.GetLoadStrain(Name, NumberItems, TendonName, LoadPat, Strain, PatternName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadStrain](SetLoadStrain_{Tendon_Object}.htm)

[DeleteLoadStrain](DeleteLoadStrain_{Tendon_Object}.htm)



## GetLoadTemperature {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetLoadTemperature_{Tendon_Object}.htm`*

# GetLoadTemperature

## Syntax

SapObject.SapModel.TendonObj.GetLoadTemperature

## VB6 Procedure

Function GetLoadTemperature(ByVal Name As String, ByRef NumberItems As Long, ByRef TendonName() As String, ByRef LoadPat() As String, ByRef MyType() As Long, ByRef Val() As Double, ByRef PatternName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

NumberItems

The total number of temperature loads retrieved for the specified tendon objects.

TendonName

This is an array that includes the name of the tendon object associated with each temperature load.

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

If this item is Object, the assignments are retrieved for the tendon object specified by the Name item.

If this item is Group, the assignments are retrieved for all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected tendon objects, and the Name item is ignored.

## Remarks

This function retrieves the temperature load assignments to tendon objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonTemperatureLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim TendonName() As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon temperature load
      ret = SapModel.TendonObj.SetLoadTemperature("ALL", "DEAD", 50, , , Group)

   'get tendon temperature load
      ret = SapModel.TendonObj.GetLoadTemperature("ALL", NumberItems, TendonName, LoadPat, Val, PatternName, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadTemperature](SetLoadTemperature_{Tendon_Object}.htm)

[DeleteLoadTemperature](DeleteLoadTemperature_{Tendon_Object}.htm)



## GetLoadedGroup

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetLoadedGroup.htm`*

# GetLoadedGroup

## Syntax

SapObject.SapModel.TendonObj.GetLoadedGroup

## VB6 Procedure

Function GetLoadedGroup(ByVal Name As String, ByRef GroupName As String) As Long

## Parameters

Name

The name of an existing tendon object.

GroupName

This is the name of an existing group. All objects in the specified group can be loaded by the tendon.

## Remarks

This function retrieves the loaded group for tendon objects. A tendon object transfers its load to any object that is in the specified group.

The function returns zero if the assignment is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonLoadedGroup()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim GroupName As String
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'get tendon loaded group
      ret = SapModel.TendonObj.GetLoadedGroup(Name, GroupName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetLoadedGroup](SetLoadedGroup.htm)



## GetLocalAxes {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetLocalAxes_{Tendon_Object}.htm`*

# GetLocalAxes

## Syntax

SapObject.SapModel.TendonObj.GetLocalAxes

## VB6 Procedure

Function GetLocalAxes(ByVal Name As String, ByRef Ang As Double) As Long

## Parameters

Name

The name of an existing tendon object.

Ang

This is the angle that the local 2 and 3 axes are rotated about the positive local 1 axis, from the default orientation. The rotation for a positive angle appears counter clockwise when the local +1 axis is pointing toward you. [deg]

## Remarks

This function retrieves the tendon local axis angle assignment for tendon objects.

The function returns zero if the assignment is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonLocalAxisAngle()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Ang As Double
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon local axis angle
      ret = SapModel.TendonObj.SetLocalAxes(Name, 30)

   'get tendon local axis angle
      ret = SapModel.TendonObj.GetLocalAxes(Name, Ang)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetLocalAxes](SetLocalAxes_{Tendon_Object}.htm)



## GetMatTemp {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetMatTemp_{Tendon_Object}.htm`*

# GetMatTemp

## Syntax

SapObject.SapModel.TendonObj.GetMatTemp

## VB6 Procedure

Function GetMatTemp(ByVal Name As String, ByRef Temp As Double, ByRef PatternName As String) As Long

## Parameters

Name

The name of an existing tendon object.

Temp

This is the material temperature value assigned to the tendon object. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the material temperature for the tendon object is uniform along the object at the value specified by Temp.

If PatternName is the name of a defined joint pattern, the material temperature for the tendon object may vary from one end to the other. The material temperature at each end of the object is equal to the specified temperature multiplied by the pattern value at the joint at the end of the tendon object.

## Remarks

This function retrieves the material temperature assignments to tendon objects.

The function returns zero if the material temperature assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonMatTemp()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign material temperature
      ret = SapModel.TendonObj.SetMatTemp("ALL", 50, , Group)

   'get material temperature
      ret = SapModel.TendonObj.GetMatTemp(Name, Temp, PatternName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMatTemp](SetMatTemp_{Tendon_Object}.htm)



## GetNameList {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetNameList_{Tendon_Object}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.TendonObj.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of tendon object names retrieved by the program.

MyName

This is a one-dimensional array of tendon object names. The MyName array is created as a dynamic, zero-based, array by the APIuser:

   Dim MyName() as String

The array is dimensioned to (NumberNames – 1) inside the Sap2000 program, filled with the names, and returned to the APIuser.

## Remarks

This function retrieves the names of all defined tendon objects.

The function returns zero if the names are successfully retrieved, otherwise it returns nonzero.

## VBA Example

Sub GetTendonObjectNames()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberNames As Long
      Dim MyName() As String
      Dim NumberPoints As Long
      Dim MyType() As Long
      Dim x() As Double
      Dim y() As Double
      Dim z() As Double
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name1)
      ret = SapModel.TendonObj.AddByPoint("2", "8", Name2)

   'set tendon geometry
      NumberPoints = 3
      ReDim MyType(NumberPoints - 1)
      ReDim x(NumberPoints - 1)
      ReDim y(NumberPoints - 1)
      ReDim z(NumberPoints - 1)
      MyType(0) = 1
      MyType(1) = 7
      MyType(2) = 6
      x(0) = 0:  y(0) = 0
      x(1) = 288:  y(1) = -12
      x(2) = 576:  y(2) = 0
      ret = SapModel.TendonObj.SetTendonData(Name1, NumberPoints, MyType, x, y, z, "Local")
      ret = SapModel.TendonObj.SetTendonData(Name2, NumberPoints, MyType, x, y, z, "Local")

   'get tendon object names
      ret = SapModel.TendonObj.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetPoints {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetPoints_{Tendon_Object}.htm`*

# GetPoints

## Syntax

SapObject.SapModel.TendonObj.GetPoints

## VB6 Procedure

Function GetPoints(ByVal Name As String, ByRef Point1 As String, ByRef Point2 As String) As Long

## Parameters

Name

The name of a defined tendon object.

Point1

The name of the point object at the I-End of the specified tendon object.

Point2

The name of the point object at the J-End of the specified tendon object.

## Remarks

This function retrieves the names of the point objects at each end of a specified tendon object.

The function returns zero if the point names are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonObjPoints()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by coordinates
      ret = SapModel.TendonObj.AddByCoord(-288, 0, 288, 288, 0, 288, Name)

   'get names of points
      ret = SapModel.TendonObj.GetPoints(Name, Point1, Point2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetProperty {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetProperty_{Tendon_Object}.htm`*

# GetProperty

## Syntax

SapObject.SapModel.TendonObj.GetProperty

## VB6 Procedure

Function GetProperty(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a defined tendon object.

PropName

The name of the tendon property assigned to the tendon object.

## Remarks

This function retrieves the tendon property assigned to a tendon object.

The function returns zero if the tendon object property is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonProp()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'get tendon section property
      ret = SapModel.TendonObj.GetProperty(Name, PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetProperty](SetProperty_{Tendon_Object}.htm)



## GetSelected {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetSelected_{Tendon_Object}.htm`*

# GetSelected

## Syntax

Sap2000.TendonObj.GetSelected

## VB6 Procedure

Function GetSelected(ByVal Name As String, ByRef Selected As Boolean) As Long

## Parameters

Name

The name of an existing tendon object.

Selected

This item returns True if the specified tendon object is selected, otherwise it returns False.

## Remarks

This function retrieves the selected status for a tendon object.

The function returns zero if the selected status is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonObjectSelectedStatus()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name1)
      ret = SapModel.TendonObj.AddByPoint("2", "8", Name2)

   'set all tendons selected
      ret = SapModel.TendonObj.SetSelected("All", True, Group)

   'get tendon object selected status
      ret = SapModel.TendonObj.GetSelected(Name1, Selected)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSelected](SetSelected_Tendon_Object}.htm)



## GetTCLimits {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetTCLimits_{Tendon_Object}.htm`*

# GetTCLimits

## Syntax

SapObject.SapModel.TendonObj.GetTCLimits

## VB6 Procedure

Function GetTCLimits(ByVal Name As String, ByRef LimitCompressionExists As Boolean, ByRef LimitCompression As Double, ByRef LimitTensionExists As Boolean, ByRef LimitTension As Double) As Long

## Parameters

Name

The name of an existing tendon object.

LimitCompressionExists

This item is True if a compression force limit exists for the tendon object.

LimitCompression

The compression force limit for the tendon object. [F]

LimitTensionExists

This item is True if a tension force limit exists for the tendon object.

LimitTension

The tension force limit for the tendon object. [F]

## Remarks

This function retrieves the tension/compression force limit assignments to tendon objects.

The function returns zero if the assignments are successfully retrieved, otherwise it returns a nonzero value.

Note that the tension and compression limits are used in nonlinear analyses only.

## VBA Example

Sub GetTendonTCLimits()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tension/compression limits
      ret = SapModel.TendonObj.SetTCLimits(Name, True, 0, True, 100)

   'get tension/compression limits
      ret = SapModel.TendonObj.GetTCLimits(Name, LimitCompressionExists, LimitCompression, LimitTensionExists, LimitTension)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetTCLimits](SetTCLimits_{Tendon_Object}.htm)



## GetTendonData

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetTendonData.htm`*

# GetTendonData

## Syntax

SapObject.SapModel.TendonObj.GetTendonData

## VB6 Procedure

Function GetTendonData(ByVal Name As String, ByRef NumberPoints As Long, ByRef MyType() As Long, ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, Optional ByVal CSys As String = "Global") As Long

## Parameters

Name

The name of a defined tendon object.

NumberPoints

The number of items used to define the tendon geometry.

MyType

This is an array of values that are 1, 3, 6, 7, 8, or 9, indicating the tendon geometry definition parameter for the specified point.

1 = Start of tendon

2 = The segment preceding the point is linear

6 = The specified point is the end of a parabola

7 = The specified point is an intermediate point on a parabola

8 = The specified point is the end of a circle

9 = The specified point is an intermediate point on a parabola

The first point always has a MyType value of 1.

MyType of 6 through 9 is based on using three points to calculate a parabolic or circular arc. MyType 6 and 8 use the specified point and the two previous points as the three points. MyType 7 and 9 use the specified point and the points just before and after the specified point as the three points.

x

This is an array of the X (or local 1) coordinate of each point in the coordinate system specified by CSys. [L]

y

This is an array of the Y (or local 2) coordinate of each point in the coordinate system specified by CSys. [L]

z

This is an array of the Z (or local 3) coordinate of each point in the coordinate system specified by CSys. [L]

CSys

This is the coordinate system in which the x, y and z coordinate parameters are defined. It is Local or the name of a defined coordinate system.

Local means that the point coordinates are in the local system of the specified tendon object with the origin assumed to be at the I-End of the tendon.

## Remarks

This function retrieves the tendon geometric definition parameters for a tendon object.

The function returns zero if the tendon object parameters are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonGeometryDefinitionData()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberPoints As Long
      Dim MyType() As Long
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by coordinates
      ret = SapModel.TendonObj.AddByCoord(-288, 0, 288, 288, 0, 288, Name)

   'set tendon geometry
      NumberPoints = 3
      ReDim MyType(NumberPoints - 1)
      ReDim x(NumberPoints - 1)
      ReDim y(NumberPoints - 1)
      ReDim z(NumberPoints - 1)
      MyType(0) = 1
      MyType(1) = 7
      MyType(2) = 6
      x(0) = 0:  y(0) = 0
      x(1) = 288:  y(1) = -12
      x(2) = 576:  y(2) = 0
      ret = SapModel.TendonObj.SetTendonData(Name, NumberPoints, MyType, x, y, z, "Local")

   'update view
      ret = SapModel.View.RefreshView(0, False)

   'get tendon geometry definition data
      ReDim MyType(0)
      ReDim x(0)
      ReDim y(0)
      ReDim z(0)
      ret = SapModel.TendonObj.GetTendonData(Name, NumberPoints, MyType, x, y, z, "Global")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetTendonData](SetTendonData.htm)

[GetTendonGeometry](GetTendonGeometry.htm)



## GetTendonGeometry

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetTendonGeometry.htm`*

# GetTendonGeometry

## Syntax

SapObject.SapModel.TendonObj.GetTendonGeometry

## VB6 Procedure

Function GetTendonGeometry(ByVal Name As String, ByRef NumberPoints As Long, ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, Optional ByVal CSys As String = "Global") As Long

## Parameters

Name

The name of a defined tendon object.

NumberPoints

The number of items used to define the discretized tendon geometry.

x

This is an array of the X (or local 1) coordinate of each point in the coordinate system specified by CSys. [L]

y

This is an array of the Y (or local 2) coordinate of each point in the coordinate system specified by CSys. [L]

z

This is an array of the Z (or local 3) coordinate of each point in the coordinate system specified by CSys. [L]

CSys

This is the coordinate system in which the x, y and z coordinate parameters are defined. It is Local or the name of a defined coordinate system.

Local means that the point coordinates are in the local system of the specified tendon object with the origin assumed to be at the I-End of the tendon.

## Remarks

This function retrieves tendon object discretized geometry, that is, it retrieves the coordinates of the points along the discretized tendon.

The function returns zero if the tendon object discretized geometry is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonDiscretizedGeometry()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberPoints As Long
      Dim MyType() As Long
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by coordinates
      ret = SapModel.TendonObj.AddByCoord(-288, 0, 288, 288, 0, 288, Name)

   'set tendon geometry
      NumberPoints = 3
      ReDim MyType(NumberPoints – 1)
      ReDim x(NumberPoints – 1)
      ReDim y(NumberPoints – 1)
      ReDim z(NumberPoints – 1)
      MyType(0) = 1
      MyType(1) = 7
      MyType(2) = 6
      x(0) = 0:  y(0) = 0
      x(1) = 288:  y(1) = -12
      x(2) = 576:  y(2) = 0
      ret = SapModel.TendonObj.SetTendonData(Name, NumberPoints, MyType, x, y, z, "Local")

   'update view
      ret = SapModel.View.RefreshView(0, False)

   'get tendon discretized geometry
      ReDim x(0)
      ReDim y(0)
      ReDim z(0)
      ret = SapModel.TendonObj.GetTendonGeometry(Name, NumberPoints, x, y, z, "Global")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetTendonData](GetTendonData.htm)

[SetTendonData](SetTendonData.htm)



## GetTransformationMatrix {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/GetTransformationMatrix_{Tendon_Object}.htm`*

# GetTransformationMatrix

## Syntax

Sap2000.TendonObj.GetTransformationMatrix

## VB6 Procedure

Function GetTransformationMatrix(ByVal Name As String, ByRef Value() As Double,Optional ByVal IsGlobal As Boolean = True) As Long

## Parameters

Name

The name of an existing tendon object.

Value

Value is an array of nine direction cosines that define the transformation matrix.

The following matrix equation shows how the transformation matrix is used to convert items from the tendon object local coordinate system to the global coordinate system.

![](../../../assets/images/Images/Transformation%20Matrix.JPG)

In the equation, c0 through c8 are the nine values from the transformation array, (Local1, Local2, Local3) are an item (such as a load) in the object local coordinate system, and (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.

The transformation from the local coordinate system to the present coordinate system is the same as that shown above for the global system if you substitute the present system for the global system.

IsGlobal

If this item is True, the transformation matrix is between the Global coordinate system and the tendon object local coordinate system.

If this item is False, the transformation matrix is between the present coordinate system and the tendon object local coordinate system.

## Remarks

The function returns zero if the tendon object transformation matrix is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetTendonObjectMatrix()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon local axis angle
      ret = SapModel.TendonObj.SetLocalAxes(Name, 30)

   'get tendon object transformation matrix
      ReDim Value(8)
      ret = SapModel.TendonObj.GetTransformationMatrix(Name, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## SetDiscretization

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetDiscretization.htm`*

# SetDiscretization

## Syntax

SapObject.SapModel.TendonObj.SetDiscretization

## VB6 Procedure

Function SetDiscretization(ByVal Name As String, ByVal Ang As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

Value

The maximum discretization length for the tendon. [L]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the tendon object specified by the Name item.

If this item is Group, the assignment is made to all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected tendon objects, and the Name item is ignored.

## Remarks

This function assigns a maximum discretization length to tendon objects.

The function returns zero if the discretization length is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignTendonMaxDiscretizationLength()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon maximum discretization length
      ret = SapModel.TendonObj.SetDiscretization(Name, 12)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetDiscretization](GetDiscretization_{Tendon_Object}.htm)



## SetGUID {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetGUID_{Tendon_Object}.htm`*

# SetGUID

## Syntax

SapObject.SapModel.TendonObj.SetGUID

## VB6 Procedure

Function SetGUID(ByVal Name As String, Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing tendon object.

GUID

The GUID (Global Unique ID) for the specified tendon object.

## Remarks

This function sets the GUID for the specified tendon object. If the GUID is passed in as a blank string, the program automatically creates a GUID for the object.

This function returns zero if the tendon object GUID is successfully set; otherwise it returns nonzero.

## VBA Example

Sub SetTendonObjGUID()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'set program created GUID
      ret = SapObject.SapModel.TendonObj.SetGUID(Name)

   'get GUID
      ret = SapObject.SapModel.TendonObj.GetGUID(Name, GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[GetGUID](GetGUID_{Tendon_Object}.htm)



## SetGroupAssign {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetGroupAssign_{Tendon_Object}.htm`*

# SetGroupAssign

## Syntax

SapObject.SapModel.TendonObj.SetGroupAssign

## VB6 Procedure

Function SetGroupAssign(ByVal Name As String, ByVal GroupName As String, Optional By Val Remove As Boolean = False, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

GroupName

The name of an existing group to which the assignment is made.

Remove

If this item is False, the specified tendon objects are added to the group specified by the GroupName item. If it is True, the tendon objects are removed from the group.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the tendon object specified by the Name item is added or removed from the group specified by the GroupName item.

If this item is Group, all tendon objects in the group specified by the Name item are added or removed from the group specified by the GroupName item.

If this item is SelectedObjects, all selected tendon objects are added or removed from the group specified by the GroupName item, and the Name item is ignored.

## Remarks

This function adds or removes tendon objects from a specified group.

The function returns zero if the group assignment is successful, otherwise it returns a nonzero value.

## VBA Example

Sub AddTendonObjectsToGroup()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name1 As String
      Dim Name2 As String
      Dim NumberPoints As Long
      Dim MyType() As Long
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name1)
      ret = SapModel.TendonObj.AddByPoint("2", "8", Name2)

   'set tendon geometry
      NumberPoints = 3
      ReDim MyType(NumberPoints - 1)
      ReDim x(NumberPoints - 1)
      ReDim y(NumberPoints - 1)
      ReDim z(NumberPoints - 1)
      MyType(0) = 1
      MyType(1) = 7
      MyType(2) = 6
      x(0) = 0:  y(0) = 0
      x(1) = 288:  y(1) = -12
      x(2) = 576:  y(2) = 0
      ret = SapModel.TendonObj.SetTendonData(Name1, NumberPoints, MyType, x, y, z, "Local")
      ret = SapModel.TendonObj.SetTendonData(Name2, NumberPoints, MyType, x, y, z, "Local")

   'define new group
      ret = SapModel.GroupDef.SetGroup("Group1")

   'add tendon objects to group
      ret = SapModel.TendonObj.SetGroupAssign(Name1, "Group1")
      ret = SapModel.TendonObj.SetGroupAssign(Name2, "Group1")

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

[GetGroupAssign](GetGroupAssign_{Tendon_Object}.htm)



## SetLoadDeformation {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetLoadDeformation_{Tendon_Object}.htm`*

# SetLoadDeformation

## Syntax

SapObject.SapModel.TendonObj.SetLoadDeformation

## VB6 Procedure

Function SetLoadDeformation(ByVal Name As String, ByVal LoadPat As String, ByRef d As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

d

This is the axial deformation load value. [L]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the tendon object specified by the Name item.

If this item is Group, the assignment is made to all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected tendon objects and the Name item is ignored.

## Remarks

This function assigns deformation loads to tendon objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignTendonDeformationLoad()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon deformation loads
      ret = SapModel.TendonObj.SetLoadDeformation("ALL", "DEAD", 2, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDeformation](GetLoadDeformation_{Tendon_Object}.htm)

[DeleteLoadDeformation](DeleteLoadDeformation_{Tendon_Object}.htm)



## SetLoadForceStress

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetLoadForceStress.htm`*

# SetLoadForceStress

## Syntax

SapObject.SapModel.TendonObj.SetLoadForceStress

## VB6 Procedure

Function SetLoadForceStress(ByVal Name As String, ByVal LoadPat As String, ByVal JackFrom As Long, ByVal LoadType As Long, ByVal Value As Double, ByVal CurvatureCoeff As Double, ByVal WobbleCoeff As Double, ByVal LossAnchorage As Double, ByVal LossShortening As Double, ByVal LossCreep As Double, ByVal LossShrinkage As Double, ByVal LossSteelRelax As Double, Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

JackFrom

This is 1, 2 or 3, indicating how the tendon is jacked.

1 = Tendon jacked from I-End

2 = Tendon jacked from J-End

3 = Tendon jacked from both ends

LoadType

This is either 0 or 1, indicating how the type of load.

0 = Force

1 = Stress

Value

This is the load value. [F] whenLoadType is 0, and [F/L2] when Loadtype is 1

CurvatureCoeff

The curvature coefficient used when calculating friction losses.

WobbleCoeff

The wobble coefficient used when calculating friction losses. [1/L]

LossAnchorage

The anchorage set slip. [L]

LossShortening

The tendon stress loss due to elastic shortening. [F/L2]

LossCreep

The tendon stress loss due to creep. [F/L2]

LossShrinkage

The tendon stress loss due to shrinkage. [F/L2]

LossSteelRelax

The tendon stress loss due to tendon steel relaxation. [F/L2]

Replace

If this item is True, all previous force/stress loads, if any, assigned to the specified tendon object(s), in the specified load case, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the tendon object specified by the Name item.

If this item is Group, the assignment is made to all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected tendon objects, and the Name item is ignored.

## Remarks

This function assigns force/stress loads to tendon objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignTendonForceLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String

   'createSap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon force load
      ret = SapModel.TendonObj.SetLoadForceStress("ALL", "DEAD", 1, 0, 100, 0.15, 8.333E-05, 0.25, 3, 5, 7, 5, , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadForceStress](GetLoadForceStress.htm)

[DeleteLoadForceStress](DeleteLoadForceStress_{Tendon_Object}.htm)



## SetLoadGravity {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetLoadGravity_{Tendon_Object}.htm`*

# SetLoadGravity

## Syntax

SapObject.SapModel.TendonObj.SetLoadGravity

## VB6 Procedure

Function SetLoadGravity(ByVal Name As String, ByVal LoadPat As String, ByVal x As Double, ByVal y As Double, ByVal z As Double, Optional ByVal Replace As Boolean = True, Optional ByVal CSys As String = "Global", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

x, y, z

These are the gravity load multipliers in the x, y and z directions of the specified coordinate system.

Replace

If this item is True, all previous gravity loads, if any, assigned to the specified tendon object(s), in the specified load pattern, are deleted before making the new assignment.

CSys

The coordinate system in which the x, y and z multipliers are specified.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the tendon object specified by the Name item.

If this item is Group, the assignment is made to all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected tendon objects and the Name item is ignored.

## Remarks

This function assigns gravity load multipliers to tendon objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignTendonGravityLoad()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon gravity loads
      ret = SapModel.TendonObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Tendon_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Tendon_Object}.htm)



## SetLoadStrain {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetLoadStrain_{Tendon_Object}.htm`*

# SetLoadStrain

## Syntax

SapObject.SapModel.TendonObj.SetLoadStrain

## VB6 Procedure

Function SetLoadStrain(ByVal Name As String, ByVal LoadPat As String, ByVal Strain As Double, Optional ByVal Replace As Boolean = True, Optional ByVal PatternName As String = "", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Strain

This is the axial strain load value. [L/L]

Replace

If this item is True, all previous strain loads, if any, assigned to the specified tendon object(s), in the specified load pattern, are deleted before making the new assignment.

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the strain load for the tendon object is uniform along the object at the value specified by Strain.

If PatternName is the name of a defined joint pattern, the strain load for the tendon object is based on the specified strain value multiplied by the pattern value at the joints at each end of the tendon object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the tendon object specified by the Name item.

If this item is Group,  the assignment is made to all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected tendon objects, and the Name item is ignored.

## Remarks

This function assigns strain loads to tendon objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignTendonStrainLoad()
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
      ret= SapModel.InitializeNewModel

   'create model from template
      ret= SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret= SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon strain load
      ret= SapModel.TendonObj.SetLoadStrain(Name, "DEAD", 0.001)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadStrain](GetLoadStrain_{Tendon_Object}.htm)

[DeleteLoadStrain](DeleteLoadStrain_{Tendon_Object}.htm)



## SetLoadTemperature {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetLoadTemperature_{Tendon_Object}.htm`*

# SetLoadTemperature

## Syntax

SapObject.SapModel.TendonObj.SetLoadTemperature

## VB6 Procedure

Function SetLoadTemperature(ByVal Name As String, ByVal LoadPat As String, ByVal Val As Double, Optional ByVal PatternName As String = "", Optional ByVal Replace As Boolean = True, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

Val

This is the temperature change value. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the temperature load for the tendon object is uniform along the object at the value specified by Val.

If PatternName is the name of a defined joint pattern, the temperature load for the tendon object is based on the specified temperature value multiplied by the pattern value at the joints at each end of the tendon object.

Replace

If this item is True, all previous temperature loads, if any, assigned to the specified tendon object(s), in the specified load case, are deleted before making the new assignment.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the tendon object specified by the Name item.

If this item is Group, the assignment is made to all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected tendon objects, and the Name item is ignored.

## Remarks

This function assigns temperature loads to tendon objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignTendonTemperatureLoad()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon temperature load
      ret = SapModel.TendonObj.SetLoadTemperature("ALL", "DEAD", 50, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTemperature](GetLoadTemperature_{Tendon_Object}.htm)

[DeleteLoadTemperature](DeleteLoadTemperature_{Tendon_Object}.htm)



## SetLoadedGroup

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetLoadedGroup.htm`*

# SetLoadedGroup

## Syntax

SapObject.SapModel.TendonObj.SetLoadedGroup

## VB6 Procedure

Function SetLoadedGroup(ByVal Name As String, ByVal GroupName As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

GroupName

This is the name of an existing group. All objects in the specified group can be loaded by the tendon.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the tendon object specified by the Name item.

If this item is Group, the assignment is made to all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected tendon objects, and the Name item is ignored.

## Remarks

This function makes the loaded group assignment to tendon objects. A tendon object transfers its load to any object that is in the specified group.

The function returns zero if the group is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignTendonLoadedGroup()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon loaded group
      ret = SapModel.TendonObj.SetLoadedGroup(Name, "ALL")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetLoadedGroup](GetLoadedGroup.htm)



## SetLocalAxes {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetLocalAxes_{Tendon_Object}.htm`*

# SetLocalAxes

## Syntax

SapObject.SapModel.TendonObj.SetLocalAxes

## VB6 Procedure

Function SetLocalAxes(ByVal Name As String, ByVal Ang As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

Ang

This is the angle that the local 2 and 3 axes are rotated about the positive local 1 axis, from the default orientation. The rotation for a positive angle appears counter clockwise when the local +1 axis is pointing toward you. [deg]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the tendon object specified by the Name item.

If this item is Group, the assignment is made to all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected tendon objects, and the Name item is ignored.

## Remarks

This function assigns a local axis angle to tendon objects.

The function returns zero if the local axis angle is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignTendonLocalAxisAngle()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tendon local axis angle
      ret = SapModel.TendonObj.SetLocalAxes(Name, 30)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetLocalAxes](GetLocalAxes_{Tendon_Object}.htm)



## SetMatTemp {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetMatTemp_{Tendon_Object}.htm`*

# SetMatTemp

## Syntax

SapObject.SapModel.TendonObj.SetMatTemp

## VB6 Procedure

Function SetMatTemp(ByVal Name As String, ByVal Temp As Double, Optional ByVal PatternName As String = "", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

Temp

This is the material temperature value assigned to the tendon object. [T]

PatternName

This is blank or the name of a defined joint pattern. If it is blank, the material temperature for the tendon object is uniform along the object at the value specified by Temp.

If PatternName is the name of a defined joint pattern, the material temperature for the tendon object may vary from one end to the other. The material temperature at each end of the object is equal to the specified temperature multiplied by the pattern value at the joint at the end of the tendon object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the tendon object specified by the Name item.

If this item is Group, the assignment is made to all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected tendon objects, and the Name item is ignored.

## Remarks

This function assigns material temperatures to tendon objects.

The function returns zero if the material temperatures are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignTendonMatTemp()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign material temperature
      ret = SapModel.TendonObj.SetMatTemp("ALL", 50, , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMatTemp](GetMatTemp_{Tendon_Object}.htm)



## SetProperty {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetProperty_{Tendon_Object}.htm`*

# SetProperty

## Syntax

SapObject.SapModel.TendonObj.SetProperty

## VB6 Procedure

Function SetProperty(ByVal name As String, ByVal PropName As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

PropName

This is None or the name of a tendon property to be assigned to the specified tendon object(s). None means that no property is assigned to the tendon.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the tendon object specified by the Name item.

If this item is Group, the assignment is made to all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected tendon objects, and the Name item is ignored.

## Remarks

This function assigns a tendon property to a tendon object.

The function returns zero if the tendon property is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub SetTendonProp()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'set tendon property
      ret = SapModel.TendonObj.SetProperty(Name, "TEN1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetProperty](GetProperty_{Tendon_Object}.htm)



## SetSelected {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetSelected_Tendon_Object}.htm`*

# SetSelected

## Syntax

Sap2000.TendonObj.SetSelected

## VB6 Procedure

Function SetSelected(ByVal Name As String, ByVal Selected As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

Selected

This item is True if the specified tendon object is selected, otherwise it is False.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the selected status is set for the tendon object specified by the Name item.

If this item is Group, the selected status is set for all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, the selected status is set for all selected tendon objects, and the Name item is ignored.

## Remarks

This function sets the selected status for a tendon object.

The function returns zero if the selected status is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetTendonObjectSelected()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'set tendon object selected
      ret = SapModel.TendonObj.SetSelected(Name, True)

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

[GetSelected](GetSelected_{Tendon_Object}.htm)



## SetTCLimits {Tendon Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetTCLimits_{Tendon_Object}.htm`*

# SetTCLimits

## Syntax

SapObject.SapModel.TendonObj.SetTCLimits

## VB6 Procedure

Function SetTCLimits(ByVal Name As String, ByVal LimitCompressionExists As Boolean, ByVal LimitCompression As Double, ByVal LimitTensionExists As Boolean, ByVal LimitTension As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing tendon object or group, depending on the value of the ItemType item.

LimitCompressionExists

This item is True if a compression force limit exists for the tendon object.

LimitCompression

The compression force limit for the tendon object. [F]

LimitTensionExists

This item is True if a tension force limit exists for the tendon object.

LimitTension

The tension force limit for the tendon object. [F]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the tendon object specified by the Name item.

If this item is Group, the assignment is made to all tendon objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected tendon objects and the Name item is ignored.

## Remarks

This function makes tension/compression force limit assignments to tendon objects.

The function returns zero if the assignments are successfully applied, otherwise it returns a nonzero value.

Note that the tension and compression limits are used in nonlinear analyses only.

## VBA Example

Sub AssignTendonTCLimits()
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

   'add tendon object by points
      ret = SapModel.TendonObj.AddByPoint("3", "9", Name)

   'assign tension/compression limits
      ret = SapModel.TendonObj.SetTCLimits(Name, True, 0, True, 100)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetTCLimits](GetTCLimits_{Tendon_Object}.htm)



## SetTendonData

*Source file: `SAP2000_API_Fuctions/Object_Model/Tendon_Object/SetTendonData.htm`*

# SetTendonData

## Syntax

SapObject.SapModel.TendonObj.SetTendonData

## VB6 Procedure

Function SetTendonData(ByVal Name As String, ByVal NumberPoints As Long, ByRef MyType() As Long, ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, Optional ByVal CSys As String = "Global") As Long

## Parameters

Name

The name of a defined tendon object.

NumberPoints

The number of items used to define the tendon geometry.

MyType

This is an array of values that are 1, 3, 6, 7, 8, or 9, indicating the tendon geometry definition parameter for the specified point.

1 = Start of tendon

2 = The segment preceding the point is linear

6 = The specified point is the end of a parabola

7 = The specified point is an intermediate point on a parabola

8 = The specified point is the end of a circle

9 = The specified point is an intermediate point on a parabola

The first point should always have a MyType value of 1. If it is not equal to 1, the program uses 1 anyway.

MyType of 6 through 9 is based on using three points to calculate a parabolic or circular arc. MyType 6 and 8 use the specified point and the two previous points as the three points. MyType 7 and 9 use the specified point and the points just before and after the specified point as the three points.

x

This is an array of the X (or local 1) coordinate of each point in the coordinate system specified by CSys. [L]

y

This is an array of the Y (or local 2) coordinate of each point in the coordinate system specified by CSys. [L]

z

This is an array of the Z (or local 3) coordinate of each point in the coordinate system specified by CSys. [L]

CSys

This is the coordinate system in which the x, y and z coordinate parameters are defined. It is Local or the name of a defined coordinate system.

Local means that the point coordinates are in the local system of the specified tendon object with the origin assumed to be at the I-End of the tendon.

## Remarks

This function assigns the tendon geometric definition parameters to a tendon object.

The function returns zero if the tendon object is successfully defined, otherwise it returns a nonzero value. If the tendon object is not successfully defined, it may be deleted.

## VBA Example

Sub SetTendonGeometryData()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberPoints As Long
      Dim MyType() As Long
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add tendon object by coordinates
      ret = SapModel.TendonObj.AddByCoord(-288, 0, 288, 288, 0, 288, Name)

   'set tendon geometry
      NumberPoints = 3
      ReDim MyType(NumberPoints - 1)
      ReDim x(NumberPoints - 1)
      ReDim y(NumberPoints - 1)
      ReDim z(NumberPoints - 1)
      MyType(0) = 1
      MyType(1) = 7
      MyType(2) = 6
      x(0) = 0:  y(0) = 0
      x(1) = 288:  y(1) = -12
      x(2) = 576:  y(2) = 0
      ret = SapModel.TendonObj.SetTendonData(Name, NumberPoints, MyType, x, y, z, "Local")

   'update view
      ret = SapModel.View.RefreshView(0, False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Tendon_Object}.htm)

[AddByPoint](AddByPoint_{Tendon_Object}.htm)

[GetTendonData](GetTendonData.htm)

[GetTendonGeometry](GetTendonGeometry.htm)

