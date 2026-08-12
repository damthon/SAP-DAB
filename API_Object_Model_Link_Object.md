# API Object Model Link Object

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Object_Model/Link_Object

---



## AddByCoord {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/AddByCoord_{Link_Object}.htm`*

# AddByCoord

## Syntax

SapObject.SapModel.LinkObj.AddByCoord

## VB6 Procedure

Function AddByCoord(ByVal xi As Double, ByVal yi As Double, ByVal zi As Double, ByVal xj As Double, ByVal yj As Double, ByVal zj As Double, ByRef Name As String, Optional IsSingleJoint As Boolean = False, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "", Optional ByVal CSys As String = "Global") As Long

## Parameters

xi, yi, zi

The coordinates of the I-End of the added link object. The coordinates are in the coordinate system defined by the CSys item.

xj, yj, zj

The coordinates of the J-End of the added link object. The coordinates are in the coordinate system defined by the CSys item.

These coordinates are ignored if the IsSingleJoint item is True.

Name

This is the name that the program ultimately assigns for the link object. If no UserName is specified, the program assigns a default name to the link object. If a UserName is specified and that name is not used for another link object, the UserName is assigned to the link object; otherwise a default name is assigned to the link object.

IsSingleJoint

This item is True if a one-joint link is added and False if a two-joint link is added.

PropName

This is either Default or the name of a defined link property.

If it is Default the program assigns a default link property to the link object. If it is the name of a defined link property, that property is assigned to the link object.

UserName

This is an optional user specified name for the link object. If a UserName is specified and that name is already used for another link object, the program ignores the UserName.

CSys

The name of the coordinate system in which the link object end point coordinates are defined.

## Remarks

This function adds a new link object whose end points are at the specified coordinates.

The function returns zero if the link object is successfully added; otherwise it returns a nonzero value.

## VBA Example

Sub AddLinkObjByCoord()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name1 As String
      Dim Name2 As String

   'create Sap2000 object
      Set SapObject = New Sap200015.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add link object by coordinates
      ret = SapModel.LinkObj.AddByCoord(-288, 0, 288, 0, 0, 0, Name1, True)
      ret = SapModel.LinkObj.AddByCoord(-288, 0, 0, 0, 0, 144, Name2)

   'refresh view
      ret = SapModel.View.RefreshView

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByPoint](AddByPoint_{Link_Object}.htm)



## AddByPoint {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/AddByPoint_{Link_Object}.htm`*

# AddByPoint

## Syntax

SapObject.SapModel.LinkObj.AddByPoint

## VB6 Procedure

Function AddByPoint(ByVal Point1 as String, ByVal Point2 as String, ByRef Name As String, Optional IsSingleJoint As Boolean = False, Optional ByVal PropName As String = "Default", Optional ByVal UserName As String = "") As Long

## Parameters

Point1

The name of a defined point object at the I-End of the added link object.

Point2

The name of a defined point object at the J-End of the added link object.

This item is ignored if the IsSingleJoint item is True.

Name

This is the name that the program ultimately assigns for the link object. If no UserName is specified, the program assigns a default name to the link object. If a UserName is specified and that name is not used for another link object, the UserName is assigned to the link object; otherwise a default name is assigned to the link object.

IsSingleJoint

This item is True if a one-joint link is added and False if a two-joint link is added.

PropName

This is either Default or the name of a defined link property.

If it is Default the program assigns a default link property to the link object. If it is the name of a defined link property, that property is assigned to the link object.

UserName

This is an optional user specified name for the link object. If a UserName is specified and that name is already used for another link object, the program ignores the UserName.

## Remarks

This function adds a new link object whose end points are specified by name.

The function returns zero if the link object is successfully added; otherwise it returns a nonzero value.

## VBA Example

Sub AddLinkObjByPoint()
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("3", "", Name1, True)
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name2)

   'refresh view
      ret = SapModel.View.RefreshView

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Link_Object}.htm)



## ChangeName {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/ChangeName_{Link_Object}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.LinkObj.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a defined link object.

NewName

The new name for the link object.

## Remarks

This function applies a new name to an link object.

The function returns zero if the new name is successfully applied; otherwise it returns a nonzero value.

## VBA Example

Sub ChangeLinkObjName()
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'refresh view
      ret = SapModel.View.RefreshView

   'change name
      ret = SapModel.LinkObj.ChangeName(Name, "MyLink")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## Count {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/Count_{Link_Object}.htm`*

# Count

## Syntax

SapObject.SapModel.LinkObj.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None

## Remarks

This function returns a count of the link objects in the model.

## VBA Example

Sub CountLinkObjects()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("3", "", Name1, True)
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name2)

   'refresh view
      ret = SapModel.View.RefreshView

   'get number of link objects
      Count = SapModel.LinkObj.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## DeleteLoadDeformation {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/DeleteLoadDeformation_{Link_Object}.htm`*

# DeleteLoadDeformation

## Syntax

SapObject.SapModel.LinkObj.DeleteLoadDeformation

## VB6 Procedure

Function DeleteLoadDeformation(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the link object specified by the Name item.

If this item is Group, the load assignments are deleted for all link objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected link objects, and the Name item is ignored.

## Remarks

This function deletes the deformation load assignments to the specified link objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteLinkDeformationLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DOF() As Boolean
      Dim d() As double
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name1)
      ret = SapModel.LinkObj.AddByPoint("2", "6", Name2)

   'assign link deformation loads
      ReDim DOF(5)
      ReDim d(5)
      DOF(0) = True
      D(0) = 2
      ret = SapModel.LinkObj.SetLoadDeformation("ALL", "DEAD", DOF, d, Group)

   'delete link deformation load
      ret = SapModel.LinkObj.DeleteLoadDeformation(Name1, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDeformation](GetLoadDeformation_{Link_Object}.htm)

[SetLoadDeformation](SetLoadDeformation_{Link_Object}.htm)



## DeleteLoadGravity {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/DeleteLoadGravity_{Link_Object}.htm`*

# DeleteLoadGravity

## Syntax

SapObject.SapModel.LinkObj.DeleteLoadGravity

## VB6 Procedure

Function DeleteLoadGravity(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the link object specified by the Name item.

If this item is Group, the load assignments are deleted for all link objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected link objects, and the Name item is ignored.

## Remarks

This function deletes the gravity load assignments to the specified link objects for the specified load pattern.

The function returns zero if the load assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteLinkGravityLoad()
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name1)
      ret = SapModel.LinkObj.AddByPoint("2", "6", Name2)

   'assign link gravity loads
      ret = SapModel.LinkObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'delete link gravity load
      ret = SapModel.LinkObj.DeleteLoadGravity(Name1, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Link_Object}.htm)

[SetLoadGravity](SetLoadGravity_{Link_Object}.htm)



## DeleteLoadTargetForce {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/DeleteLoadTargetForce_{Link_Object}.htm`*

# DeleteLoadTargetForce

## Syntax

SapObject.SapModel.LinkObj.DeleteLoadTargetForce

## VB6 Procedure

Function DeleteLoadTargetForce(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are deleted for the link object specified by the Name item.

If this item is Group, the load assignments are deleted for all link objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are deleted for all selected link objects, and the Name item is ignored.

## Remarks

This function deletes the target force assignments to the specified link objects for the specified load pattern.

The function returns zero if the target force assignments are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteLinkTargetForce()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DOF() As Boolean
      Dim f() As double
      Dim RD() As double
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name1)
      ret = SapModel.LinkObj.AddByPoint("2", "6", Name2)

   'assign link target force
      ReDim DOF(5)
      ReDim f(5)
      ReDim RD(5)
      DOF(0) = True
      f(0) = 50
      RD(0) = 1
      ret = SapModel.LinkObj.SetLoadTargetForce("ALL", "DEAD", DOF, f, RD, Group)

   'delete link target force
      ret = SapModel.LinkObj.DeleteLoadTargetForce(Name1, "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTargetForce](GetLoadTargetForce_{Link_Object}.htm)

[SetLoadTargetForce](SetLoadTargetForce_{Link_Object}.htm)



## Delete {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/Delete_{Link_Object}.htm`*

# Delete

## Syntax

SapObject.SapModel.LinkObj.Delete

## VB6 Procedure

Function Delete(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the link object specified by the Name item is deleted.

If this item is Group, the all link objects in the group specified by the Name item are deleted.

If this item is SelectedObjects, all selected link objects are deleted, and the Name item is ignored.

## Remarks

The function deletes link objects.

The function returns zero if the link objects are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteLinkObj()
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("3", "", Name1, True)
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name2)

   'delete area object
      ret = SapModel.LinkObj.Delete(Name1)

   'refresh view
      ret = SapModel.View.RefreshView

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddByCoord](AddByCoord_{Link_Object}.htm)

[AddByPoint](AddByPoint_{Link_Object}.htm)



## GetElm {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetElm_{Link_Object}.htm`*

# GetElm

## Syntax

SapObject.SapModel.LinkObj.GetElm

## VB6 Procedure

Function GetElm(ByVal Name As String, ByRef Elm as String) As Long

## Parameters

Name

The name of an existing link object.

Elm

The name of the link element created from the specified link object.

## Remarks

This function retrieves the name of the link element (analysis model link) associated with a specified link object in the object-based model.

This function returns zero if the link element name is successfully retrieved; otherwise it returns nonzero. An error occurs if the analysis model does not exist.

## VBA Example

Sub GetLinkElementNameForLinkObject()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim Elm As String

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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'create the analysis model
      ret = SapModel.Analyze.CreateAnalysisModel

   'get link element name
      ret = SapModel.LinkObj.GetElm(Name, Elm)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetGUID {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetGUID_{Link_Object}.htm`*

# GetGUID

## Syntax

SapObject.SapModel.LinkObj.GetGUID

## VB6 Procedure

Function GetGUID(ByVal name As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing link object.

GUID

The GUID (Global Unique ID) for the specified link object.

## Remarks

This function retrieves the GUID for the specified link object.

This function returns zero if the link object GUID is successfully retrieved; otherwise it returns nonzero.

## VBA Example

Sub GetLinkObjGUID()
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'set program created GUID
      ret = SapObject.SapModel.LinkObj.SetGUID("1")

   'get GUID
      ret = SapObject.SapModel.LinkObj.GetGUID("1", GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetGUID](SetGUID_{Link_Object}.htm)



## GetGroupAssign {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetGroupAssign_{Link_Object}.htm`*

# GetGroupAssign

## Syntax

SapObject.SapModel.LinkObj.GetGroupAssign

## VB6 Procedure

Function GetGroupAssign(ByVal Name As String, ByRef NumberGroups As Long, ByRef Groups() As String)  As Long

## Parameters

Name

The name of an existing link object.

NumberGroups

The number of group names retrieved.

Groups

The names of the groups to which the link object is assigned.

## Remarks

This function retrieves the names of the groups to which a specified link object is assigned.

The function returns zero if the group assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetLinkObjectGroups()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim Name As String
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'define new groups
      ret = SapModel.GroupDef.SetGroup("Group1")
      ret = SapModel.GroupDef.SetGroup("Group2")

   'add link object to groups
      ret = SapModel.LinkObj.SetGroupAssign(Name, "Group1")
      ret = SapModel.LinkObj.SetGroupAssign(Name, "Group2")

   'get link object groups
      ret = SapModel.LinkObj.GetGroupAssign(Name, NumberGroups, Groups)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.0.0.

## See Also

[SetGroupAssign](SetGroupAssign_{Link_Object}.htm)



## GetLoadDeformation {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetLoadDeformation_{Link_Object}.htm`*

# GetLoadDeformation

## Syntax

SapObject.SapModel.LinkObj.GetLoadDeformation

## VB6 Procedure

Function GetLoadDeformation(ByVal Name As String, ByRef NumberItems As Long, ByRef LinkName() As String, ByRef LoadPat() As String, ByRef dof1() As Boolean, ByRef dof2() As Boolean, ByRef dof3() As Boolean, ByRef dof4() As Boolean, ByRef dof5() As Boolean, ByRef dof6() As Boolean, ByRef U1() As Double, ByRef U2() As Double, ByRef U3() As Double, ByRef R1() As Double, ByRef R2() As Double, ByRef R3() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

NumberItems

The total number of deformation loads retrieved for the specified link objects.

LinkName

This is an array that includes the name of the link object associated with each deformation load.

LoadPat

This is an array that includes the name of the load pattern associated with each deformation load.

dof1, dof2, dof3, dof4, dof5, dof6

These are arrays of boolean values, indicating if the considered degree of freedom has a deformation load.

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

If this item is Object, the assignments are retrieved for the link object specified by the Name item.

If this item is Group, the assignments are retrieved for all link objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected link objects, and the Name item is ignored.

## Remarks

This function retrieves the deformation load assignments to link objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetLinkDeformationLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DOF() As Boolean
      Dim d() As double
      Dim NumberItems As Long
      Dim LinkName() As String
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'assign link deformation loads
      ReDim DOF(5)
      ReDim d(5)
      DOF(0) = True
      D(0) = 2
      ret = SapModel.LinkObj.SetLoadDeformation("ALL", "DEAD", DOF, d, Group)

   'get link deformation loads
      ret = SapModel.LinkObj.GetLoadDeformation(Name, NumberItems, LinkName, LoadPat, dof1, dof2, dof3, dof4, dof5, dof6, U1, U2, U3, R1, R2, R3)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadDeformation](SetLoadDeformation_{Link_Object}.htm)

[DeleteLoadDeformation](DeleteLoadDeformation_{Link_Object}.htm)



## GetLoadGravity {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetLoadGravity_{Link_Object}.htm`*

# GetLoadGravity

## Syntax

SapObject.SapModel.LinkObj.GetLoadGravity

## VB6 Procedure

Function GetLoadGravity(ByVal Name As String, ByRef NumberItems As Long, ByRef LinkName() As String, ByRef LoadPat() As String, ByRef CSys() As String, ByRef x() As Double, ByRef y() As Double, ByRef z() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

NumberItems

The total number of gravity loads retrieved for the specified link objects.

LinkName

This is an array that includes the name of the link object associated with each gravity load.

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

If this item is Object, the assignments are retrieved for the link object specified by the Name item.

If this item is Group, the assignments are retrieved for all link objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected link objects, and the Name item is ignored.

## Remarks

This function retrieves the gravity load assignments to link objects.

The function returns zero if the load assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetLinkGravityLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim LinkName() As String
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'assign link gravity loads
      ret = SapModel.LinkObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'get link gravity load
      ret = SapModel.LinkObj.GetLoadGravity(Name, NumberItems, LinkName, LoadPat, CSys, x, y, z)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadGravity](SetLoadGravity_{Link_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Link_Object}.htm)



## GetLoadTargetForce {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetLoadTargetForce_{Link_Object}.htm`*

# GetLoadTargetForce

## Syntax

SapObject.SapModel.LinkObj.GetLoadTargetForce

## VB6 Procedure

Function GetLoadTargetForce(ByVal Name As String, ByRef NumberItems As Long, ByRef LinkName() As String, ByRef LoadPat() As String, ByRef dof1() As Boolean, ByRef dof2() As Boolean, ByRef dof3() As Boolean, ByRef dof4() As Boolean, ByRef dof5() As Boolean, ByRef dof6() As Boolean, ByRef P() As Double, ByRef V2() As Double, ByRef V3() As Double, ByRef T() As Double, ByRef M2() As Double, ByRef M3() As Double, ByRef T1() As Double, ByRef T2() As Double, ByRef T3() As Double, ByRef T4() As Double, ByRef T5() As Double, ByRef T6() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

NumberItems

The total number of deformation loads retrieved for the specified link objects.

LinkName

This is an array that includes the name of the link object associated with each target force.

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

These are arrays of the relative distances along the link objects where the target force values apply. The relative distances specified for a given degree of freedom are applicable only if the corresponding dofn item for that degree of freedom is True.

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

If this item is Object, the assignments are retrieved for the link object specified by the Name item.

If this item is Group, the assignments are retrieved for all link objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected link objects, and the Name item is ignored.

## Remarks

This function retrieves the target force assignments to link objects.

The function returns zero if the target force assignments are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetLinkTargetForce()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim DOF() As Boolean
      Dim f() As double
      Dim RD() As double
      Dim NumberItems As Long
      Dim LinkName() As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'assign link target force
      ReDim DOF(5)
      ReDim f(5)
      ReDim RD(5)
      DOF(0) = True
      f(0) = 50
      RD(0) = 1
      ret = SapModel.LinkObj.SetLoadTargetForce(Name, "DEAD", DOF, f, RD)

   'get link target force
      ret = SapModel.LinkObj.GetLoadTargetForce(Name, NumberItems, LinkName, LoadPat, dof1, dof2, dof3, dof4, dof5, dof6, P, V2, V3, T, M2, M3, T1, T2, T3, T4, T5, T6)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadTargetForce](SetLoadTargetForce_{Link_Object}.htm)

[DeleteLoadTargetForce](DeleteLoadTargetForce_{Link_Object}.htm)



## GetLocalAxesAdvanced Link Object

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetLocalAxesAdvanced_Link_Object.htm`*

# GetLocalAxesAdvanced

## Syntax

SapObject.SapModel.LinkObj.GetLocalAxesAdvanced

## VB6 Procedure

Function GetLocalAxesAdvanced(ByVal Name As String, ByRef Active As Boolean, ByRef AxVectOpt As Long, ByRef AxCSys As String, ByRef AxDir() As Long, ByRef AxPt() As String, ByRef AxVect() As Double, ByRef Plane2 As Long, ByRef PlVectOpt As Long, ByRef PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double) As Long

## Parameters

Name

The name of an existing link object.

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

This is an array dimensioned to 1 (2 integers), indicating the axis/plane reference vector primary and secondary coordinate directions, PlDir(0) and PlDir(1) respectively, taken at the object center in the specified coordinate system and used to determine the plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 1. Possible coordinate direction values are:

1 = +X      -1 = -X

2 = +Y      -2 = -Y

3 = +Z      -3 = -Z

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

This is 12 or 13, indicating that the local plane determined by the plane reference vector is the 1-2 or 1-3 plane. This item applies only when the Active item is True.

## Remarks

This function assigns advanced local axes to link objects.

The function returns zero if the advanced local axes assignments are assigned successfully; otherwise it returns a nonzero value.

## VBA Example

Sub GetLinkAdvancedLocalAxes()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyName As String
      Dim MyAxDir(1) As Long
      Dim MyAxPt(1) As String
      Dim MyAxVect(2) As Double
      Dim MyPlDir(1) As Long
      Dim MyPlPt(1) As String
      Dim MyPlVect(2) As Double
      Dim Ang As Double
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "1", MyName)

   'assign link advanced local axes
      MyAxVect(0)=0.707
      MyAxVect(1)=0.707
      MyAxVect(2)=0
      MyPlDir(0) = 2
      MyPlDir(1) = 3
      ret = SapModel.LinkObj.SetLocalAxesAdvanced(MyName, True, 3, "Global", MyAxDir, MyAxPt, MyAxVect, 12, 1, "Global", MyPlDir, MyPlPt, MyPlVect)

   'get link local axis angle
      ret = SapModel.LinkObj.GetLocalAxes(MyName, Ang, Advanced)

   'get link advanced local axes data
      If Advanced Then
         ret = SapModel.LinkObj.GetLocalAxesAdvanced(MyName, Active, AxVectOpt, AxCSys, AxDir, AxPt, AxVect, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect)
      End If

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

## See Also

[SetLocalAxesAdvanced](SetLocalAxesAdvanced_Link_Object.htm)

[SetLocalAxes](SetLocalAxes_{Link_Object}.htm)



## GetLocalAxes {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetLocalAxes_{Link_Object}.htm`*

# GetLocalAxes

## Syntax

SapObject.SapModel.LinkObj.GetLocalAxes

## VB6 Procedure

Function GetLocalAxes(ByVal Name As String, ByRef Ang As Double, ByRef Advanced As Boolean) As Long

## Parameters

Name

The name of an existing link object.

Ang

This is the angle that the local 2 and 3 axes are rotated about the positive local 1 axis, from the default orientation or, if the Advanced item is True, from the orientation determined by the plane reference vector. The rotation for a positive angle appears counter clockwise when the local +1 axis is pointing toward you. [deg]

Advanced

This item is True if the link object local axes orientation was obtained using advanced local axes parameters.

## Remarks

This function retrieves the local axis angle assignment for link objects.

The function returns zero if the assignment is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetLinkLocalAxisAngle()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'assign link local axis angle
      ret = SapModel.LinkObj.SetLocalAxes(Name, 30)

   'get link local axis angle
      ret = SapModel.LinkObj.GetLocalAxes(Name, Ang, Advanced)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetLocalAxes](SetLocalAxes_{Link_Object}.htm)



## GetNameList {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetNameList_{Link_Object}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.LinkObj.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of link object names retrieved by the program.

MyName

This is a one-dimensional array of link object names. The MyName array is created as a dynamic, zero-based, array by the APIuser:

Dim MyName() as String

The array is dimensioned to (NumberNames – 1) inside the SAP2000 program, filled with the names, and returned to the APIuser.

## Remarks

This function retrieves the names of all defined link objects.

The function returns zero if the names are successfully retrieved; otherwise it returns nonzero.

## VBA Example

Sub GetLinkObjectNames()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("3", "", Name, True)
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'get link object names
      ret = SapModel.LinkObj.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetPoints {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetPoints_{Link_Object}.htm`*

# GetPoints

## Syntax

SapObject.SapModel.LinkObj.GetPoints

## VB6 Procedure

Function GetPoints(ByVal Name As String, ByRef Point1 As String, ByRef Point2 As String) As Long

## Parameters

Name

The name of a defined link object.

Point1

The name of the point object at the I-End of the specified link object.

Point2

The name of the point object at the J-End of the specified link object.

## Remarks

This function retrieves the names of the point objects at each end of a specified link object. If names of the two point objects are the same, the specified link object is a one-joint link object.

The function returns zero if the point names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetLinkObjPoints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add link object by coordinates
      ret = SapModel.LinkObj.AddByCoord(-288, 0, 0, 0, 0, 144, Name)

   'get names of points
      ret = SapModel.LinkObj.GetPoints(Name, Point1, Point2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetPropertyFD {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetPropertyFD_{Link_Object}.htm`*

# GetPropertyFD

## Syntax

SapObject.SapModel.LinkObj.GetPropertyFD

## VB6 Procedure

Function GetProperty(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a defined link object.

PropName

The name of the frequency dependent link property assigned to the link object. This item is None if there is no frequency dependent link property assigned to the link object.

## Remarks

This function retrieves the frequency dependent link property assigned to a link object.

The function returns zero if the property is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetLinkObjectFDProp()
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

   'open existing model
      ret = SapModel.File.OpenFile("C:\SapAPI\Example 6-012.sdb")

   'get link frequency dependent property
      ret = SapModel.LinkObj.GetPropertyFD("1", PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetProperty](SetProperty_{Link_Object}.htm)

[GetProperty](GetProperty_{Link_Object}.htm)

[SetPropertyFD](SetPropertyFD.htm)



## GetProperty {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetProperty_{Link_Object}.htm`*

# GetProperty

## Syntax

SapObject.SapModel.LinkObj.GetProperty

## VB6 Procedure

Function GetProperty(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a defined link object.

PropName

The name of the link property assigned to the link object.

## Remarks

This function retrieves the link property assigned to a link object.

The function returns zero if the property is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetLinkObjectProp()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'get link property
      ret = SapModel.LinkObj.GetProperty(Name, PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetProperty](SetProperty_{Link_Object}.htm)

[GetPropertyFD](GetPropertyFD_{Link_Object}.htm)

[SetPropertyFD](SetPropertyFD.htm)



## GetSelected {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetSelected_{Link_Object}.htm`*

# GetSelected

## Syntax

Sap2000.LinkObj.GetSelected

## VB6 Procedure

Function GetSelected(ByVal Name As String, ByRef Selected As Boolean) As Long

## Parameters

Name

The name of an existing link object.

Selected

This item is True if the specified link object is selected; otherwise it is False.

## Remarks

This function retrieves the selected status for a link object.

The function returns zero if the selected status is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetLinkObjectSelectedStatus()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'set link object selected
      ret = SapModel.LinkObj.SetSelected("ALL", True, Group)

   'get link object selected status
      ret = SapModel.LinkObj.GetSelected(Name, Selected)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSelected](SetSelected_{Link_Object}.htm)



## GetTransformationMatrix {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/GetTransformationMatrix_{Link_Object}.htm`*

# GetTransformationMatrix

## Syntax

Sap2000.LinkObj.GetTransformationMatrix

## VB6 Procedure

Function GetTransformationMatrix(ByVal Name As String, ByRef Value() As Double,Optional ByVal IsGlobal As Boolean = True) As Long

## Parameters

Name

The name of an existing link object.

Value

Value is an array of nine direction cosines that define the transformation matrix.

The following matrix equation shows how the transformation matrix is used to convert items from the link object local coordinate system to the global coordinate system.

![](../../../assets/images/Images/Transformation%20Matrix.JPG)

In the equation, c0 through c8 are the nine values from the transformation array, (Local1, Local2, Local3) are an item (such as a load) in the object local coordinate system, and (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.

The transformation from the local coordinate system to the present coordinate system is the same as that shown above for the global system if you substitute the present system for the global system.

IsGlobal

If this item is True, the transformation matrix is between the Global coordinate system and the link object local coordinate system.

If this item is False, the transformation matrix is between the present coordinate system, and the link object local coordinate system.

## Remarks

The function returns zero if the link object transformation matrix is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetLinkObjectMatrix()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'assign link object local axis angle
      ret = SapModel.LinkObj.SetLocalAxes(Name, 30)

   'get link object transformation matrix
      ReDim Value(8)
      ret = SapModel.LinkObj.GetTransformationMatrix(Name, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## SetGUID {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/SetGUID_{Link_Object}.htm`*

# SetGUID

## Syntax

SapObject.SapModel.LinkObj.SetGUID

## VB6 Procedure

Function SetGUID(ByVal Name As String, Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing link object.

GUID

The GUID (Global Unique ID) for the specified link object.

## Remarks

This function sets the GUID for the specified link object. If the GUID is passed in as a blank string, the program automatically creates a GUID for the object.

This function returns zero if the link object GUID is successfully set; otherwise it returns nonzero.

## VBA Example

Sub SetLinkObjGUID()
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'set program created GUID
      ret = SapObject.SapModel.LinkObj.SetGUID("1")

   'get GUID
      ret = SapObject.SapModel.LinkObj.GetGUID("1", GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[GetGUID](GetGUID_{Link_Object}.htm)



## SetGroupAssign {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/SetGroupAssign_{Link_Object}.htm`*

# SetGroupAssign

## Syntax

SapObject.SapModel.LinkObj.SetGroupAssign

## VB6 Procedure

Function SetGroupAssign(ByVal Name As String, ByVal GroupName As String, Optional By Val Remove As Boolean = False, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

GroupName

The name of an existing group to which the assignment is made.

Remove

If this item is False, the specified link objects are added to the group specified by the GroupName item. If it is True, the link objects are removed from the group.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the link object specified by the Name item is added or removed from the group specified by the GroupName item.

If this item is Group, all link objects in the group specified by the Name item are added or removed from the group specified by the GroupName item.

If this item is SelectedObjects, all selected link objects are added or removed from the group specified by the GroupName item, and the Name item is ignored.

## Remarks

This function adds or removes link objects from a specified group.

The function returns zero if the group assignment is successful; otherwise it returns a nonzero value.

## VBA Example

Sub AddLinkObjectsToGroup()
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'define new group
      ret = SapModel.GroupDef.SetGroup("Group1")

   'add link object to group
      ret = SapModel.LinkObj.SetGroupAssign(Name, "Group1")

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

[GetGroupAssign](GetGroupAssign_{Link_Object}.htm)



## SetLoadDeformation {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/SetLoadDeformation_{Link_Object}.htm`*

# SetLoadDeformation

## Syntax

SapObject.SapModel.LinkObj.SetLoadDeformation

## VB6 Procedure

Function SetLoadDeformation(ByVal Name As String, ByVal LoadPat As String, ByRef DOF() As Boolean, ByRef d() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

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

If this item is Object, the assignment is made to the link object specified by the Name item.

If this item is Group, the assignment is made to all link objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected link objects, and the Name item is ignored.

## Remarks

This function assigns deformation loads to link objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignLinkDeformationLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DOF() As Boolean
      Dim d() As double
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'assign link deformation loads
      ReDim DOF(5)
      ReDim d(5)
      DOF(0) = True
      D(0) = 2
      ret = SapModel.LinkObj.SetLoadDeformation("ALL", "DEAD", DOF, d, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDeformation](GetLoadDeformation_{Link_Object}.htm)

[DeleteLoadDeformation](DeleteLoadDeformation_{Link_Object}.htm)



## SetLoadGravity {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/SetLoadGravity_{Link_Object}.htm`*

# SetLoadGravity

## Syntax

SapObject.SapModel.LinkObj.SetLoadGravity

## VB6 Procedure

Function SetLoadGravity(ByVal Name As String, ByVal LoadPat As String, ByVal x As Double, ByVal y As Double, ByVal z As Double, Optional ByVal Replace As Boolean = True, Optional ByVal CSys As String = "Global", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

LoadPat

The name of a defined load pattern.

x, y, z

These are the gravity load multipliers in the x, y and z directions of the specified coordinate system.

Replace

If this item is True, all previous gravity loads, if any, assigned to the specified link object(s), in the specified load pattern, are deleted before making the new assignment.

CSys

The coordinate system in which the x, y and z multipliers are specified.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the link object specified by the Name item.

If this item is Group, the assignment is made to all link objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected link objects, and the Name item is ignored.

## Remarks

This function assigns gravity load multipliers to link objects.

The function returns zero if the loads are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignLinkGravityLoad()
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'assign link gravity loads
      ret = SapModel.LinkObj.SetLoadGravity("ALL", "DEAD", 0, 0, -1, , , Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadGravity](GetLoadGravity_{Link_Object}.htm)

[DeleteLoadGravity](DeleteLoadGravity_{Link_Object}.htm)



## SetLoadTargetForce {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/SetLoadTargetForce_{Link_Object}.htm`*

# SetLoadTargetForce

## Syntax

SapObject.SapModel.LinkObj.SetLoadTargetForce

## VB6 Procedure

Function SetLoadTargetForce(ByVal Name As String, ByVal LoadPat As String, ByRef DOF() As Boolean, ByRef f() As Double, ByRef RD() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

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

This is a array of relative distances along the link objects where the target force values apply. The relative distances specified for a given degree of freedom are applicable only if the corresponding DOF item for that degree of freedom is True. The relative distance must be between 0 and 1, 0 <= RD <=1.

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

If this item is Object, the assignment is made to the link object specified by the Name item.

If this item is Group, the assignment is made to all link objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected link objects, and the Name item is ignored.

## Remarks

This function assigns target forces to frame objects.

The function returns zero if the target forces are successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignLinkTargetForce()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim DOF() As Boolean
      Dim f() As double
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'assign link target force
      ReDim DOF(5)
      ReDim f(5)
      ReDim RD(5)
      DOF(0) = True
      f(0) = 50
      RD(0) = 1
      ret = SapModel.LinkObj.SetLoadTargetForce(Name, "DEAD", DOF, f, RD)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadTargetForce](GetLoadTargetForce_{Link_Object}.htm)

[DeleteLoadTargetForce](DeleteLoadTargetForce_{Link_Object}.htm)



## SetLocalAxesAdvanced Link Object

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/SetLocalAxesAdvanced_Link_Object.htm`*

# SetLocalAxesAdvanced

## Syntax

SapObject.SapModel.LinkObj.SetLocalAxesAdvanced

## VB6 Procedure

Function SetLocalAxesAdvanced(ByVal Name As String, ByVal Active As Boolean, ByVal AxVectOpt As Long, ByVal AxCSys As String, ByRef AxDir() As Long, ByRef AxPt() As String, ByRef AxVect() As Double, ByVal Plane2 As Long, ByVal PlVectOpt As Long, ByVal PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group depending on the value of the ItemType item.

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

This is an array dimensioned to 1 (2 integers), indicating the axis/plane reference vector primary and secondary coordinate directions, PlDir(0) and PlDir(1) respectively, taken at the object center in the specified coordinate system and used to determine the plane reference vector. This item applies when the Active item is True and the AxVectOpt/PlVectOpt item is 1. Possible coordinate direction values are:

1 = +X      -1 = -X

2 = +Y      -2 = -Y

3 = +Z      -3 = -Z

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

This is 12 or 13, indicating that the local plane determined by the plane reference vector is the 1-2 or 1-3 plane. This item applies only when the Active item is True.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

Selection = 2

If this item is Object, the assignment is made to the link object specified by the Name item.

If this item is Group, the assignment is made to all link objects in the group specified by the Name item.

If this item is Selection, assignment is made to all selected link objects and the Name item is ignored.

## Remarks

This function assigns advanced local axes to link objects.

The function returns zero if the advanced local axes assignments are assigned successfully; otherwise, it returns a nonzero value.

## VBA Example

Sub AssignLinkAdvancedLocalAxes()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyName As String
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "1", MyName)

   'assign link advanced local axes
      MyAxVect(0)=0.707
      MyAxVect(1)=0.707
      MyAxVect(2)=0
      MyPlDir(0) = 2
      MyPlDir(1) = 3
      ret = SapModel.LinkObj.SetLocalAxesAdvanced(MyName, True, 3, "Global", MyAxDir, MyAxPt, MyAxVect, 12, 1, "Global", MyPlDir, MyPlPt, MyPlVect)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

## See Also

[GetLocalAxesAdvanced](GetLocalAxesAdvanced_Link_Object.htm)

[GetLocalAxes](GetLocalAxes_{Link_Object}.htm)



## SetLocalAxes {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/SetLocalAxes_{Link_Object}.htm`*

# SetLocalAxes

## Syntax

SapObject.SapModel.LinkObj.SetLocalAxes

## VB6 Procedure

Function SetLocalAxes(ByVal Name As String, ByVal Ang As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

Ang

This is the angle that the local 2 and 3 axes are rotated about the positive local 1 axis, from the default orientation or, if the Advanced item is True, from the orientation determined by the plane reference vector. The rotation for a positive angle appears counter clockwise when the local +1 axis is pointing toward you. [deg]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the link object specified by the Name item.

If this item is Group, the assignment is made to all link objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected link objects, and the Name item is ignored.

## Remarks

This function assigns a local axis angle to link objects.

The function returns zero if the local axis angle is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub AssignLinkLocalAxisAngle()
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'assign link local axis angle
      ret = SapModel.LinkObj.SetLocalAxes(Name, 30)

   'refresh view
      ret = SapModel.View.RefreshView

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetLocalAxes](GetLocalAxes_{Link_Object}.htm)



## SetPropertyFD

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/SetPropertyFD.htm`*

# SetPropertyFD

## Syntax

SapObject.SapModel.LinkObj.SetPropertyFD

## VB6 Procedure

Function SetPropertyFD(ByVal name As String, ByVal PropName As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

PropName

This is either None or the name of a frequency dependent link property to be assigned to the specified link object(s). None means that no frequency dependent link property is assigned to the link object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the link object specified by the Name item.

If this item is Group, the assignment is made to all link objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected link objects, and the Name item is ignored.

## Remarks

This function assigns a frequency dependent link property to link objects.

The function returns zero if the property is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub SetLinkObjectFDProp()
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

   'open existing model
      ret = SapModel.File.OpenFile("C:\SapAPI\Example 6-012.sdb")

   'set link frequency dependent property
      ret = SapModel.LinkObj.SetPropertyFD("1", "None")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetProperty](SetProperty_{Link_Object}.htm)

[GetProperty](GetProperty_{Link_Object}.htm)

[GetPropertyFD](GetPropertyFD_{Link_Object}.htm)



## SetProperty {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/SetProperty_{Link_Object}.htm`*

# SetProperty

## Syntax

SapObject.SapModel.LinkObj.SetProperty

## VB6 Procedure

Function SetProperty(ByVal name As String, ByVal PropName As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

PropName

This is the name of a link property to be assigned to the specified link object(s).

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the link object specified by the Name item.

If this item is Group, the assignment is made to all link objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected link objects, and the Name item is ignored.

## Remarks

This function assigns a link property to link objects.

The function returns zero if the property is successfully assigned; otherwise it returns a nonzero value.

## VBA Example

Sub SetLinkObjectProp()
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'set link property
      ret = SapModel.LinkObj.SetProperty(Name, "Link1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetProperty](GetProperty_{Link_Object}.htm)

[GetPropertyFD](GetPropertyFD_{Link_Object}.htm)

[SetPropertyFD](SetPropertyFD.htm)



## SetSelected {Link Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Link_Object/SetSelected_{Link_Object}.htm`*

# SetSelected

## Syntax

Sap2000.LinkObj.SetSelected

## VB6 Procedure

Function SetSelected(ByVal Name As String, ByVal Selected As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing link object or group, depending on the value of the ItemType item.

Selected

This item is True if the specified link object is selected; otherwise it is False.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the selected status is set for the link object specified by the Name item.

If this item is Group, the selected status is set for all link objects in the group specified by the Name item.

If this item is SelectedObjects, the selected status is set for all selected link objects, and the Name item is ignored.

## Remarks

This function sets the selected status for link objects.

The function returns zero if the selected status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetLinkObjectSelected()
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

   'add link object by points
      ret = SapModel.LinkObj.AddByPoint("1", "5", Name)

   'set link object selected
      ret = SapModel.LinkObj.SetSelected("ALL", True, Group)

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

[GetSelected](GetSelected_{Link_Object}.htm)

