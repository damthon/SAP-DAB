# API Object Model Point Object

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Object_Model/Point_Object

---



## AddCartesian

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/AddCartesian.htm`*

# AddCartesian

## Syntax

SapObject.SapModel.PointObj.AddCartesian

## VB6 Procedure

Function AddCartesian(ByVal x As Double, ByVal y As Double, ByVal z As Double, ByRef Name As String, Optional ByVal userName As String = "", Optional ByVal csys As String = "Global", Optional ByVal MergeOff As Boolean = False, Optional ByVal MergeNumber As Long = 0) As Long

## Parameters

x

The X-coordinate of the added point object in the specified coordinate system. [L]

y

The Y-coordinate of the added point object in the specified coordinate system. [L]

z

The Z-coordinate of the added point object in the specified coordinate system. [L]

Name

This is the name that the program ultimately assigns for the point object. If no UserName is specified, the program assigns a default name to the point object. If a UserName is specified and that name is not used for another point, the UserName is assigned to the point; otherwise a default name is assigned to the point.

If a point is merged with another point, this will be the name of the point object with which it was merged.

UserName

This is an optional user specified name for the point object. If a UserName is specified and that name is already used for another point object, the program ignores the UserName.

CSys

The name of the coordinate system in which the joint coordinates are defined.

MergeOff

If this item is False, a new point object that is added at the same location as an existing point object will be merged with the existing point object (assuming the two point objects have the same MergeNumber) and thus only one point object will exist at the location.

If this item is True, the points will not merge and two point objects will exist at the same location.

MergeNumber

Two points objects in the same location will merge only if their merge number assignments are the same. By default all pointobjects have a merge number of zero.

## Remarks

This function adds a point object to a model. The added point object will be tagged as a Special Point except if it was merged with another point object. Special points are allowed to exist in the model with no objects connected to them.

The function returns zero if the point object is successfully added or merged, otherwise it returns a nonzero value.

## VBA Example

Sub AddPointCartesian()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim x As Double, y As Double, z As Double
      Dim Name as String
      Dim MyName as String
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model blank from template
      ret = SapModel.File.NewBlank

   'add point object to model
      x = 12
      y = 37
      z = 0
      MyName = "A1"
      ret = SapModel.PointObj.AddCartesian(x, y, z, Name, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddCylindrical](AddCylindrical.htm)

[AddSpherical](AddSpherical.htm)

[GetCoordCartesian](GetCoordCartesian_{Point_Object}.htm)

[GetSpecialPoint](GetSpecialPoint.htm)

[SetSpecialPoint](SetSpecialPoint.htm)



## AddCylindrical

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/AddCylindrical.htm`*

# AddCylindrical

## Syntax

SapObject.SapModel.PointObj.AddCylindrical

## VB6 Procedure

Function AddCylindrical(ByVal r As Double, ByVal Theta As Double, ByVal z As Double, ByRef Name As String, Optional ByVal userName As String = "", Optional ByVal csys As String = "Global", Optional ByVal MergeOff As Boolean = False, Optional ByVal MergeNumber As Long = 0) As Long

## Parameters

r

The radius for the added point object in the specified coordinate system. [L]

Theta

The angle for the added point object in the specified coordinate system. The angle is measured in the XY plane from the positive global X axis. When looking in the XY plane with the positive Z axis pointing toward you, a positive Theta angle is counter clockwise. [deg]

z

The Z-coordinate of the added point object in the specified coordinate system. [L]

Name

This is the name that the program ultimately assigns for the point object. If no UserName is specified, the program assigns a default name to the point object. If a UserName is specified and that name is not used for another point, the UserName is assigned to the point; otherwise a default name is assigned to the point.

If a point is merged with another point, this will be the name of the point object with which it was merged.

UserName

This is an optional user specified name for the point object. If a UserName is specified and that name is already used for another point object, the program ignores the UserName.

CSys

The name of the coordinate system in which the joint coordinates are defined.

MergeOff

If this item is False, a new point object that is added at the same location as an existing point object will be merged with the existing point object (assuming the two point objects have the same MergeNumber) and thus only one point object will exist at the location.

If this item is True, the points will not merge and two point objects will exist at the same location.

MergeNumber

Two points objects in the same location will merge only if their merge number assignments are the same. By default all pointobjects have a merge number of zero.

## Remarks

This function adds a point object to a model. The added point object will be tagged as a Special Point except if it was merged with another point object. Special points are allowed to exist in the model with no objects connected to them

The function returns zero if the point object is successfully added or merged, otherwise it returns a nonzero value.

## VBA Example

Sub AddPointCylindrical()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim r As Double, Theta As Double, z As Double
      Dim Name as String
      Dim MyName as String
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model blank from template
      ret = SapModel.File.NewBlank

   'add point object to model
      r = 12
      Theta = 37
      z = 0
      MyName = "A1"
      ret = SapModel.PointObj.AddCartesian(r, Theta, z, Name, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddCartesian](AddCartesian.htm)

[AddSpherical](AddSpherical.htm)

[GetCoordCylindrical](GetCoordCylindrical_{Point_Object}.htm)

[GetSpecialPoint](GetSpecialPoint.htm)

[SetSpecialPoint](SetSpecialPoint.htm)



## AddSpherical

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/AddSpherical.htm`*

# AddSpherical

## Syntax

SapObject.SapModel.PointObj.AddSpherical

## VB6 Procedure

Function AddSpherical(ByVal r As Double, ByVal a As Double, ByVal b As Double, ByRef Name As String, Optional ByVal userName As String = "", Optional ByVal csys As String = "Global", Optional ByVal MergeOff As Boolean = False, Optional ByVal MergeNumber As Long = 0) As Long

## Parameters

r

The radius for the added point object in the specified coordinate system. [L]

a

The plan angle for the added point object in the specified coordinate system. This angle is measured in the XY plane from the positive global X axis. When looking in the XY plane with the positive Z axis pointing toward you, a positive a angle is counterclockwise. [deg]

b

The elevation angle for the added point object in the specified coordinate system. This angle is measured in an X'Z plane that is perpendicular to the XY plane with the positive X' axis oriented at angle a from the positive global X axis. Angle b is measured from the positive global Z axis. When looking in the X’Z plane with the positive Y' axis pointing toward you, a positive b angle is counter clockwise. [deg]

Name

This is the name that the program ultimately assigns for the point object. If no UserName is specified, the program assigns a default name to the point object. If a UserName is specified and that name is not used for another point, the UserName is assigned to the point; otherwise a default name is assigned to the point.

If a point is merged with another point, this will be the name of the point object with which it was merged.

UserName

This is an optional user specified name for the point object. If a UserName is specified and that name is already used for another point object, the program ignores the UserName.

CSys

The name of the coordinate system in which the joint coordinates are defined.

MergeOff

If this item is False, a new point object that is added at the same location as an existing point object will be merged with the existing point object (assuming the two point objects have the same MergeNumber) and thus only one point object will exist at the location.

If this item is True, the points will not merge and two point objects will exist at the same location.

MergeNumber

Two points objects in the same location will merge only if their merge number assignments are the same. By default all pointobjects have a merge number of zero.

## Remarks

This function adds a point object to a model. The added point object will be tagged as a Special Point except if it was merged with another point object. Special points are allowed to exist in the model with no objects connected to them

The function returns zero if the point object is successfully added or merged, otherwise it returns a nonzero value.

## VBA Example

Sub AddPointSpherical()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim r As Double, a As Double, b As Double
      Dim Name as String
      Dim MyName as String
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model blank from template
      ret = SapModel.File.NewBlank

   'add point object to model
      r = 12
      a = 37
      b = 23
      MyName = "A1"
      ret = SapModel.PointObj.AddSpherical(r, a, b, Name, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[AddCartesian](AddCartesian.htm)

[AddCylindrical](AddCylindrical.htm)

[GetCoordSpherical](GetCoordSpherical_{Point_Object}.htm)

[GetSpecialPoint](GetSpecialPoint.htm)

[SetSpecialPoint](SetSpecialPoint.htm)



## ChangeName {Point}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/ChangeName_{Point}.htm`*

# ChangeName

## Syntax

SapObject.SapModel.PointObj.ChangeName

## VB6 Procedure

Function ChangeName(ByVal Name As String, ByVal NewName As String) As Long

## Parameters

Name

The existing name of a point object.

NewName

The new name for the point object.

## Remarks

The function returns zero if the new name is successfully applied, otherwise it returns a nonzero value.

## VBA Example

Sub ChangePointName()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long

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

   'change name of point object
      ret = SapModel.PointObj.ChangeName("1", "A1")

  'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## CountConstraint {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/CountConstraint_{Point_Object}.htm`*

# CountConstraint

## Syntax

SapObject.SapModel.PointObj.CountConstraint

## VB6 Procedure

Function CountConstraint(ByRef Count As Long, Optional ByVal Name As String = "") As Long

## Parameters

Count

The number of counted constraints.

Name

This optional item is the name of an existing point object.

## Remarks

If the Name item is provided, the Count item returns the total number of constraint assignments made to the specified point object. If the Name item is not specified, or is specified as an empty string, the Count item returns the total number of constraint assignments to all point objects in the model. If the Name item is specified but it is not recognized by the program as a valid point object, an error is returned.

This function returns zero if the count is successfully completed, otherwise it returns a nonzero value.

## VBA Example

Sub CountConstraintAssignments()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long
      Dim Count as Long

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

   'add constraint definition
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1")

   'make constraint assignment
      ret = SapModel.PointObj.SetConstraint("3", "Diaph1")

   'get number of constraint assignments
      ret = SapModel.PointObj.CountConstraint(Count)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetConstraint](GetConstraint_{Point_Object}.htm)

[SetConstraint](SetConstraint.htm)

[DeleteConstraint](DeleteConstraint.htm)



## CountLoadDispl {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/CountLoadDisp_{Point_Object}.htm`*

# CountLoadDispl

## Syntax

SapObject.SapModel.PointObj.CountLoadDispl

## VB6 Procedure

Function CountLoadDispl(ByRef Count As Long, Optional ByVal Name As String = "", Optional ByVal LoadPat As String = "") As Long

## Parameters

Count

The number of counted ground displacement loads.

Name

This optional item is the name of an existing point object.

LoadPat

This optional item is the name of an existing load pattern.

## Remarks

If neither the Name item nor the LoadPat item is provided, the Count item returns the total number of ground displacement load assignments in the model.

If the Name item is provided but not the LoadPat item, the Count item returns the total number of ground displacement load assignments made for the specified point object.

If the Name item is not provided but the LoadPat item is specified, the Count item returns the total number of ground displacement load assignments made to all point objects for the specified load pattern.

If both the Name item and the LoadPat item are provided, the Count item returns the total number of ground displacement load assignments made to the specified point object for the specified load pattern.

If the Name item or the LoadPat item is provided but is not recognized by the program as valid, an error is returned.

This function returns zero if the count is successfully completed, otherwise it returns a nonzero value.

## VBA Example

Sub CountGroundDisplacementLoads()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value() As Double
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

   'add ground displacement load
      Redim Value(5)
      Value(0) = 10
      ret = SapModel.PointObj.SetLoadDispl("1", "DEAD", Value)

   'get number of ground displacement loads
      ret = SapModel.PointObj.CountLoadDispl(Count)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDispl](GetLoadDispl_{Point_Object}.htm)

[SetLoadDispl](SetLoadDispl.htm)

[DeleteLoadDispl](DeleteLoadDispl.htm)



## CountLoadForce {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/CountLoadForce_{Point_Object}.htm`*

# CountLoadForce

## Syntax

SapObject.SapModel.PointObj.CountLoadForce

## VB6 Procedure

Function CountLoadForce(ByRef Count As Long, Optional ByVal Name As String = "", Optional ByVal LoadPat As String = "") As Long

## Parameters

Count

The number of counted point loads.

Name

This optional item is the name of an existing point object.

LoadPat

This optional item is the name of an existing load pattern.

## Remarks

If neither the Name item nor the LoadPat item is provided, the Count item returns the total number of point load assignments in the model.

If the Name item is provided but not the LoadPat item, the Count item returns the total number of point load assignments made for the specified point object.

If the Name item is not provided but the LoadPat item is specified, the Count item returns the total number of point  load assignments made to all point objects for the specified load pattern.

If both the Name item and the LoadPat item are provided,n the Count item returns the total number of point load assignments made to the specified point object for the specified load pattern.

If the Name item or the LoadPat item is provided but is not recognized by the program as valid, an error is returned.

This function returns zero if the count is successfully completed, otherwise it returns a nonzero value.

## VBA Example

Sub CountPointLoads()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value() As Double
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

   'add point load
      Redim Value(5)
      Value(0) = 10
      ret = SapModel.PointObj.SetLoadForce("3", "DEAD", Value)

   'get number of point loads
      ret = SapModel.PointObj.CountLoadForce(Count)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadForce](GetLoadForce_{Point_Object}.htm)

[SetLoadForce](SetLoadForce.htm)

[DeleteLoadForce](DeleteLoadForce.htm)



## CountPanelZone

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/CountPanelZone.htm`*

# CountPanelZone

## Syntax

SapObject.SapModel.PointObj.CountPanelZone

## VB6 Procedure

Function CountPanelZone() As Long

## Parameters

None

## Remarks

This function returns the total number of panel zone assignments to point objects in the model.

## VBA Example

Sub CountPanelZones()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long
      Dim Count as Long
      Dim PropType as Long
      Dim Thickness As Double
      Dim Connectivity As Long
      Dim LocalAxisFrom As Long

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

   'add panel zone assignment
      PropType = 1 'elastic from column and doubler plate
      Thickness = 2
      Connectivity  = 0 'beams to other objects
      LocalAxisFrom = 0 'column
      ret = SapModel.PointObj.SetPanelZone("3", PropType, Thickness, 0, 0, "", Connectivity, LocalAxisFrom, 0)

   'get number of panel zone assignments
      Count = SapModel.PointObj.CountPanelZone

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetPanelZone](GetPanelZone.htm)

[SetPanelZone](SetPanelZone.htm)

[DeletePanelZone](DeletePanelZone.htm)



## CountRestraint {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/CountRestraint_{Point_Object}.htm`*

# CountRestraint

## Syntax

SapObject.SapModel.PointObj.CountRestraint

## VB6 Procedure

Function CountRestraint() As Long

## Parameters

None

## Remarks

This function returns the total number of point objects in the model with restraint assignments.

## VBA Example

Sub CountRestrainedPointObjects()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long
      Dim Count as Long

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

   'get number of restrained point objects
      Count = SapModel.PointObj.CountRestraint

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetRestraint](GetRestraint_{Point_Object}.htm)

[SetRestraint](SetRestraint.htm)

[DeleteRestraint](DeleteRestraint.htm)



## CountSpring {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/CountSpring_{Point_Object}.htm`*

# CountSpring

## Syntax

SapObject.SapModel.PointObj.CountSpring

## VB6 Procedure

Function CountSpring() As Long

## Parameters

None

## Remarks

This function returns the total number of point objects in the model with spring assignments.

## VBA Example

Sub CountSpringSupportedPointObjects()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Count As Long
      Dim i As Long
      Dim k() As Double

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

   'add joint spring assignment
      redim k(5)
      For i = 0 to 5
         k(i) = i + 1
      Next i
      ret = SapModel.PointObj.SetSpring("3", k)

   'get number of point objects with spring assignments
      Count = SapModel.PointObj.CountSpring

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Point_Object}.htm)

[SetSpring](SetSpring.htm)

[DeleteSpring](DeleteSpring_{Point_Object}.htm)



## Count {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/Count_{Point_Object}.htm`*

# Count

## Syntax

SapObject.SapModel.PointObj.Count

## VB6 Procedure

Function Count() As Long

## Parameters

None

## Remarks

This function returns the total number of point objects in the model.

## VBA Example

Sub CountPointObjects()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long
      Dim Count as Long

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

   'return number of point objects
      Count = SapModel.PointObj.Count

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## DeleteConstraint

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/DeleteConstraint.htm`*

# DeleteConstraint

## Syntax

SapObject.SapModel.PointObj.DeleteConstraint

## VB6 Procedure

Function DeleteConstraint(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of a point object or a group depending on the value selected for ItemType item.

ItemType

This is one of the following items from the eItemType enumeration.

Object = 0

Group = 1

SelectedObjects = 2

If Object is selected, the Name item refers to a point object and the constraint assignments to that point object are removed.

If Group is selected, the Name item refers to a group and the constraint assignments to all point objects in the group are removed.

If SelectedObjects is selected, the Name item is ignored and the constraint assignments to all selected point objects are removed.

## Remarks

This function deletes all constraint assignments from the specified point object(s).

The function returns zero if the constraint assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeletePointConstraints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long

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

   'add constraint definition
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1")

   'make constraint assignment
      ret = SapModel.PointObj.SetConstraint("3", "Diaph1")

   'delete constraint assignment
      ret = SapModel.PointObj.DeleteConstraint("3")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetConstraint](GetConstraint_{Point_Object}.htm)

[SetConstraint](SetConstraint.htm)



## DeleteLoadDispl

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/DeleteLoadDispl.htm`*

# DeleteLoadDispl

## Syntax

SapObject.SapModel.PointObj.DeleteLoadDispl

## VB6 Procedure

Function DeleteLoadDispl(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of a point object or a group depending on the value selected for ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items from the eItemType enumeration.

Object = 0

Group = 1

SelectedObjects = 2

If Object is selected, the Name item refers to a point object. The ground displacement load assignments, for the specified load case, made to that point object, are removed.

If Group is selected, the Name item refers to a group. The ground displacement load assignments, for the specified load pattern, made to all point objects in the group, are removed.

If SelectedObjects is selected, the Name item is ignored. The ground displacement load assignments, for the specified load pattern, made to all selected point objects, are removed.

## Remarks

This function deletes all ground displacement load assignments, for the specified load pattern, from the specified point object(s).

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeletePointDisplLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long
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

   'add ground displacement load
      Redim Value(5)
      Value(0) = 10
      ret = SapModel.PointObj.SetLoadDispl("1", "DEAD", Value)

   'delete ground displacement load
      ret = SapModel.PointObj.DeleteLoadDispl("1", "DEAD")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDispl](GetLoadDispl_{Point_Object}.htm)

[SetLoadDispl](SetLoadDispl.htm)



## DeleteLoadForce

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/DeleteLoadForce.htm`*

# DeleteLoadForce

## Syntax

SapObject.SapModel.PointObj.DeleteLoadForce

## VB6 Procedure

Function DeleteLoadForce(ByVal Name As String, ByVal LoadPat As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of a point object or a group depending on the value selected for ItemType item.

LoadPat

The name of a defined load pattern.

ItemType

This is one of the following items from the eItemType enumeration.

Object = 0

Group = 1

SelectedObjects = 2

If Object is selected, the Name item refers to a point object. The point load assignments, for the specified load pattern, made to that point object, are removed.

If Group is selected, the Name item refers to a group. The point load assignments, for the specified load pattern, made to all point objects in the group, are removed.

If SelectedObjects is selected, the Name item is ignored. The point load assignments, for the specified load pattern, made to all selected point objects, are removed.

## Remarks

This function deletes all point load assignments, for the specified load pattern, from the specified point object(s).

The function returns zero if the load assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeletePointForceLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long
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

   'add point load
      Redim Value(5)
      Value(0) = 10
      ret = SapModel.PointObj.SetLoadForce("1", "DEAD", Value)

   'delete point load
      ret = SapModel.PointObj.DeleteLoadForce("1", "DEAD")

  'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadForce](GetLoadForce_{Point_Object}.htm)

[SetLoadForce](SetLoadForce.htm)



## DeleteMass

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/DeleteMass.htm`*

# DeleteMass

## Syntax

SapObject.SapModel.PointObj.DeleteMass

## VB6 Procedure

Function DeleteMass(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of a point object or a group depending on the value selected for ItemType item.

ItemType

This is one of the following items from the eItemType enumeration.

Object = 0

Group = 1

SelectedObjects = 2

If Object is selected, the Name item refers to a point object. The mass assignments for that point object are removed.

If Group is selected, the Name item refers to a group. The mass assignments for all point objects in the group are removed.

If SelectedObjects is selected, the Name item is ignored. The mass assignments for all selected point objects are removed.

## Remarks

This function deletes all mass assignments from the specified point object(s).

The function returns zero if the mass assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeletePointMass()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long
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

   'add point mass
      Redim Value(5)
      Value(0) = 1
      ret = SapModel.PointObj.SetMass("3", Value)

   'delete point mass
      ret = SapModel.PointObj.DeleteMass("3")

  'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMass](GetMass_{Point_Object}.htm)

[SetMass](SetMass.htm)

[SetMassByVolume](SetMassByVolume.htm)

[SetMassByWeight](SetMassByWeight.htm)



## DeletePanelZone

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/DeletePanelZone.htm`*

# DeletePanelZone

## Syntax

SapObject.SapModel.PointObj.DeletePanelZone

## VB6 Procedure

Function DeletePanelZone(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of a point object or a group depending on the value selected for ItemType item.

ItemType

This is one of the following items from the eItemType enumeration.

Object = 0

Group = 1

SelectedObjects = 2

If Object is selected, the Name item refers to a point object. The panel zone assignments for that point object are removed.

If Group is selected, the Name item refers to a group. The panel zone assignments for all point objects in the group are removed.

If SelectedObjects is selected, the Name item is ignored. The panel zone assignments for all selected point objects are removed.

## Remarks

This function deletes all panel zone assignments from the specified point object(s).

The function returns zero if the panel zone assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeletePanelZone()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long
      Dim PropType as Long
      Dim Thickness As Double
      Dim Connectivity As Long
      Dim LocalAxisFrom As Long

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

   'add panel zone assignment
      PropType = 1 'elastic from column and doubler plate
      Thickness = 2
      Connectivity  = 0 'beams to other objects
      LocalAxisFrom = 0 'column
      ret = SapModel.PointObj.SetPanelZone("3", PropType, Thickness, 0, 0, "", Connectivity, LocalAxisFrom, 0)

   'delete panel zone
      ret = SapModel.PointObj.DeletePanelZone("3")

  'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetPanelZone](GetPanelZone.htm)

[SetPanelZone](SetPanelZone.htm)



## DeletePatternValue

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/DeletePatternValue.htm`*

# DeletePatternValue

## Syntax

SapObject.SapModel.PointObj.DeletePatternValue

## VB6 Procedure

Function DeletePatternValue(ByVal Name As String, ByVal PatternName As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of a point object or a group depending on the value selected for ItemType item.

PatternName

The name of a defined joint pattern.

ItemType

This is one of the following items from the eItemType enumeration.

Object = 0

Group = 1

SelectedObjects = 2

If Object is selected, the Name item refers to a point object. The joint pattern assignments, associated with the specified joint pattern, for that point object are removed.

If Group is selected, the Name item refers to a group. The joint pattern assignments, associated with the specified joint pattern, for all point objects in the group, are removed.

If SelectedObjects is selected, the Name item is ignored. The joint pattern assignments, associated with the specified joint pattern, for all selected point objects, are removed.

## Remarks

This function deletes all joint pattern assignments, associated with the specified joint pattern, from the specified point object(s).

The function returns zero if the joint pattern assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeletePointPatternAssigns()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long

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

   'add joint pattern assignment
      ret = SapModel.PointObj.SetPatternByXYZ("3", "Default", 0, 0, 10, 0)

   'delete joint pattern assignment
      ret = SapModel.PointObj.DeletePatternValue("3", "Default")

  'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetPatternValue](GetPatternValue_{Point_Object}.htm)

[SetPatternByPressure](SetPatternByPressure.htm)

[SetPatternByXYZ](SetPatternByXYZ.htm)



## DeleteRestraint

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/DeleteRestraint.htm`*

# DeleteRestraint

## Syntax

SapObject.SapModel.PointObj.DeleteRestraint

## VB6 Procedure

Function DeleteRestraint(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of a point object or a group depending on the value selected for ItemType item.

ItemType

This is one of the following items from the eItemType enumeration.

Object = 0

Group = 1

SelectedObjects = 2

If Object is selected, the Name item refers to a point object. The restraint assignments for that point object are removed.

If Group is selected, the Name item refers to a group. The restraint assignments for all point objects in the group are removed.

If SelectedObjects is selected, the Name item is ignored. The restraint assignments for all selected point objects are removed.

## Remarks

This function deletes all restraint assignments from the specified point object(s).

The function returns zero if the restraint assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeletePointRestraints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long

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

   'delete joint restraint assignment
      ret = SapModel.PointObj.DeleteRestraint("1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetRestraint](GetRestraint_{Point_Object}.htm)

[SetRestraint](SetRestraint.htm)



## DeleteSpecialPoint

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/DeleteSpecialPoint.htm`*

# DeleteSpecialPoint

## Syntax

SapObject.SapModel.PointObj.DeleteSpecialPoint

## VB6 Procedure

Function DeleteSpecialPoint(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the deletion applies to the point object specified by the Name item.

If this item is Group, the deletion applies to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the deletion applies to all selected point objects, and the Name item is ignored.

## Remarks

The function deletes special point objects that have no other objects connected to them.

The function returns zero if the function completes successfully, otherwise it returns a nonzero value.

Point objects can be deleted only if they have no other objects (e.g., frame, cable, tendon, area, solid link) connected to them. If a point object is not specified to be a Special Point, the program automatically deletes that point object when it has no other objects connected to it. If a point object is specified to be a Special Point, to delete it, first delete all other objects connected to the point and then call this function to delete the point.

## VBA Example

Sub DeleteSpecialPointObj()
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

   'set as special point
      ret = SapModel.PointObj.SetSpecialPoint("3", True)

   'delete frame objects
      ret = SapModel.FrameObj.Delete("2")
      ret = SapModel.FrameObj.Delete("8")

   'delete special point object
      ret = SapModel.PointObj.DeleteSpecialPoint("3")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetSpecialPoint](SetSpecialPoint.htm)

[GetSpecialPoint](GetSpecialPoint.htm)



## DeleteSpring {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/DeleteSpring_{Point_Object}.htm`*

# DeleteSpring

## Syntax

SapObject.SapModel.PointObj.DeleteSpring

## VB6 Procedure

Function DeleteSpring(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of a point object or a group depending on the value selected for ItemType item.

ItemType

This is one of the following items from the eItemType enumeration.

Object = 0

Group = 1

SelectedObjects = 2

If Object is selected, the Name item refers to a point object. The point spring assignments for that point object are removed.

If Group is selected, the Name item refers to a group. The point spring assignments for all point objects in the group are removed.

If SelectedObjects is selected, the Name item is ignored. The point spring assignments for all selected point objects are removed.

## Remarks

This function deletes all point spring assignments from the specified point object(s).

The function returns zero if the restraint assignments are successfully deleted, otherwise it returns a nonzero value.

## VBA Example

Sub DeletePointSprings()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim i as Long
      Dim ret As Long
      Dim k() As Double

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

   'add joint spring assignment
      redim k(5)
      For i = 0 to 5
         k(i) = i + 1
      Next i
      ret = SapModel.PointObj.SetSpring("3", k)

   'delete joint spring assignment
      ret = SapModel.PointObj.DeleteSpring("3")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Point_Object}.htm)

[GetSpringCoupled](GetSpringCoupled_{Point_Object}.htm)

[SetSpring](SetSpring.htm)

[SetSpringCoupled](SetSpringCoupled.htm)



## GetCommonTo

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetCommonTo.htm`*

# GetCommonTo

## Syntax

SapObject.SapModel.PointObj.GetCommonTo

## VB6 Procedure

Function GetCommonTo(ByVal Name As String, ByRef CommonTo As Long) As Long

## Parameters

Name

The name of a point object or a group depending on the value selected for ItemType item.

CommonTo

The total number of objects (line, area, solid and link) that connect to the specified point object.

## Remarks

This function returns the total number of objects (line, area, solid and link) that connect to the specified point object.

The function returns zero if the CommonTo is successfully calculated, otherwise it returns a nonzero value.

## VBA Example

Sub GetPointCommonTo()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim CommonTo as long

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

   'get CommonTo
      ret = SapModel.PointObj.GetCommonTo("6", CommonTo)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetConnectivity {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetConnectivity_{Point_Object}.htm`*

# GetConnectivity

## Syntax

SapObject.SapModel.PointObj.GetConnectivity

## VB6 Procedure

Function GetConnectivity(ByVal Name As String, ByRef NumberItems As Long, ByRef ObjectType() As Long, ByRef ObjectName() As String, ByRef PointNumber() As Long) As Long

## Parameters

Name

The name of an existing point object.

NumberItems

This is the total number of objects connected to the specified point object.

ObjectType

This is an array that includes the object type of each object connected to the specified point object.

2 = Frame object

3 = Cable object

4 = Tendon object

5 = Area object

6 = Solid object

7 = Link object

ObjectName

This is an array that includes the object name of each object connected to the specified point object.

PointNumber

This is an array that includes the point number within the considered object that corresponds to the specified point object.

## Remarks

This function returns a list of objects connected to a specified point object.

The function returns zero if the list is successfully filled; otherwise it returns nonzero.

## VBA Example

Sub GetPointObjectConnectivity()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems as Long
      Dim ObjectType() As Long
      Dim ObjectName() As String
      Dim PointNumber() As Long

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

   'get objects connected to point object 11
      ret = SapModel.PointObj.GetConnectivity("11", NumberItems, ObjectType, ObjectName, PointNumber)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also



## GetConstraint {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetConstraint_{Point_Object}.htm`*

# GetConstraint

## Syntax

SapObject.SapModel.PointObj.GetConstraint

## VB6 Procedure

Function GetConstraint(ByVal Name As String, ByRef NumberItems As Long, ByRef PointName() As String, ByRef ConstraintName() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object or group, depending on the value of the ItemType item.

NumberItems

This is the total number of constraint assignments returned.

PointName

This is an array that includes the name of the point object to which the specified constraint assignment applies.

ConstraintName

This is an array that includes the name of the constraint that is assigned to the point object specified by the PointName item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the constraint assignments are retrieved for the point object specified by the Name item.

If this item is Group, the constraint assignments are retrieved for all point objects in the group specified by the Name item.

If this item is SelectedObjects, the constraint assignments are retrieved for all selected point objects and the Name item is ignored.

## Remarks

This function returns a list of constraint assignments made to one or more specified point objects.

The function returns zero if the constraint name list is successfully filled, otherwise it returns nonzero.

The PointName and ConstraintName items are returned in one-dimensional arrays. Each array is created as a dynamic array by the API user. In VBA a dynamic string array is defined by:

   Dim PointName() as String

The arrays are dimensioned to (NumberItems – 1) inside the Sap2000 program, filled with values, and returned to the API user.

The arrays are zero-based. Thus the first item is at array index 0, and the last item is at array index (NumberItems - 1).

## VBA Example

Sub GetConstraintAssignments()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      dim NumberItems as Long
      Dim PointName() As String
      Dim ConstraintName() As String
      Dim i As Long

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

   'define a new constraint
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1")

   'define new constraint assignments
      For i = 4 To 16 Step 4
         ret = SapModel.PointObj.SetConstraint(Format(i), "Diaph1")
      Next i

   'get constraint assignments
      ret = SapModel.PointObj.GetConstraint("ALL", NumberItems, PointName, ConstraintName, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetConstraint](SetConstraint.htm)

[DeleteConstraint](DeleteConstraint.htm)



## GetCoordCartesian {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetCoordCartesian_{Point_Object}.htm`*

# GetCoordCartesian

## Syntax

SapObject.SapModel.PointObj.GetCoordCartesian

## VB6 Procedure

Function GetCoordCartesian(ByVal Name As String, ByRef x As Double, ByRef y As Double, ByRef z As Double, Optional ByVal Csys As String = "Global") As Long

## Parameters

Name

The name of a defined point object.

x

The X-coordinate of the specified point object in the specified coordinate system. [L]

y

The Y-coordinate of the specified point object in the specified coordinate system. [L]

z

The Z-coordinate of the specified point object in the specified coordinate system. [L]

Csys

The name of a defined coordinate system. If Csys is not specified, the Global coordinate system is assumed.

## Remarks

The function returns zero if the coordinates are successfully returned; otherwise it returns nonzero. If successful, the function returns the x, y and z coordinates of the specified point object in the Present Units. The coordinates are reported in the coordinate system specified by Csys.

## VBA Example

Sub GetPointCoordCartesian
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim x As Double, y As Double, z As Double
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'start a new template model
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'get point coordinates of the point named "1" and display in a message box
      ret = SapModel.PointObj.GetCoordCartesian("1", x, y, z)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetCoordCylindrical](GetCoordCylindrical_{Point_Object}.htm)

[GetCoordSpherical](GetCoordSpherical_{Point_Object}.htm)

[GetNameList](GetNameList_{Point_Object}.htm)



## GetCoordCylindrical {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetCoordCylindrical_{Point_Object}.htm`*

# GetCoordCylindrical

## Syntax

SapObject.SapModel.PointObj.GetCoordCylindrical

## VB6 Procedure

Function GetCoordCylindrical(ByVal Aame As String, ByRef r As Double, ByRef Theta As Double, ByRef z As Double, Optional ByVal Csys As String = "Global") As Long

## Parameters

Name

The name of a defined point object.

r

The radius for the specified point object in the specified coordinate system. [L]

Theta

The angle for the specified point object in the specified coordinate system. The angle is measured in the XY plane from the positive X axis. When looking in the XY plane with the positive Z axis pointing toward you, a positive Theta angle is counter clockwise [deg]

z

The Z-coordinate of the specified point object in the specified coordinate system. [L]

Csys

The name of a defined coordinate system. If Csys is not specified, the Global coordinate system is assumed.

## Remarks

The function returns zero if the coordinates are successfully returned; otherwise it returns nonzero. If successful, the function returns the r, theta and z coordinates of the specified point object in the Present Units. The coordinates are reported in the coordinate system specified by CSys.

## VBA Example

Sub GetPointCoordCylindrical
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim r As Double, Theta As Double, z As Double
      Dim ret As Long

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'start a new template model
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'get point coordinates of the point named "1" and display in a message box
      ret = SapModel.PointObj.GetCoordCylindrical("1", r, Theta, z)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetCoordCartesian](GetCoordCartesian_{Point_Object}.htm)

[GetCoordSpherical](GetCoordSpherical_{Point_Object}.htm)

[GetNameList](GetNameList_{Point_Object}.htm)



## GetCoordSpherical {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetCoordSpherical_{Point_Object}.htm`*

# GetCoordSpherical

## Syntax

SapObject.SapModel.PointObj.GetCoordSpherical

## VB6 Procedure

Function GetCoordSpherical(ByVal Name As String, ByRef r As Double, ByRef a As Double, ByRef b As Double, Optional ByVal CSys As String = "Global") As Long

## Parameters

Name

The name of an existing point object.

r

The radius for the point object in the specified coordinate system. [L]

a

The plan angle for the point object in the specified coordinate system. This angle is measured in the XY plane from the positive global X axis. When looking in the XY plane with the positive Z axis pointing toward you, a positive a angle is counter clockwise. [deg]

b

The elevation angle for the point object in the specified coordinate system. This angle is measured in an X'Z plane that is perpendicular to the XY plane with the positive X' axis oriented at angle a from the positive global X axis. Angle b is measured from the positive global Z axis. When looking in the X’Z plane with the positive Y' axis pointing toward you, a positive b angle is counter clockwise. [deg]

CSys

The name of the coordinate system in which the joint coordinates are returned.

## Remarks

The function returns zero if the coordinates are successfully returned; otherwise it returns nonzero. If successful, the function returns the r, a and b coordinates of the specified point object in the Present Units. The coordinates are reported in the coordinate system specified by CSys.

## VBA Example

Sub GetPointCoordSpherical()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim r As Double, a As Double, b As Double
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

   'get spherical point coordinates
      ret = SapModel.PointObj.GetCoordSpherical("5", r, a, b)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetCoordCartesian](GetCoordCartesian_{Point_Object}.htm)

[GetCoordCylindrical](GetCoordCylindrical_{Point_Object}.htm)

[GetNameList](GetNameList_{Point_Object}.htm)



## GetElm {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetElm_{Point_Object}.htm`*

# GetElm

## Syntax

SapObject.SapModel.PointObj.GetElm

## VB6 Procedure

Function GetElm(ByVal Name As String, ByRef Elm as String) As Long

## Parameters

Name

The name of an existing point object.

Elm

The name of the point element associated with the specified point object.

## Remarks

This function retrieves the name of the point element (analysis model point) associated with a specified point object in the object-based model.

This function returns zero if the point element name is successfully returned; otherwise it returns nonzero. An error occurs if the analysis model does not currently exist.

## VBA Example

Sub GetPointElementName()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'create the analysis model
      ret = SapModel.Analyze.CreateAnalysisModel

   'get point element name
      ret = SapModel.PointObj.GetElm("5", Elm)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## GetGUID {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetGUID_{Point_Object}.htm`*

# GetGUID

## Syntax

SapObject.SapModel.PointObj.GetGUID

## VB6 Procedure

Function GetGUID(ByVal name As String, ByRef GUID As String) As Long

## Parameters

Name

The name of an existing point object.

GUID

The GUID (Global Unique ID) for the specified point object.

## Remarks

This function retrieves the GUID for specified point object.

This function returns zero if the point object GUID is successfully retrieved; otherwise it returns nonzero.

## VBA Example

Sub GetPointGUID()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'set program created GUID
      ret = SapModel.PointObj.SetGUID("1")

   'get GUID
      ret = SapModel.PointObj.GetGUID("1", GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetGUID](SetGUID_{Point_Object}.htm)



## GetGroupAssign {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetGroupAssign_{Point_Object}.htm`*

# GetGroupAssign

## Syntax

SapObject.SapModel.PointObj.GetGroupAssign

## VB6 Procedure

Function GetGroupAssign(ByVal Name As String, ByRef NumberGroups As Long, ByRef Groups() As String)  As Long

## Parameters

Name

The name of an existing point object.

NumberGroups

The number of group names retrieved.

Groups

The names of the groups to which the point object is assigned.

## Remarks

This function retrieves the names of the groups to which a specified point object is assigned.

The function returns zero if the group assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetPointObjectGroups()
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

   'add point object to groups
      ret = SapModel.PointObj.SetGroupAssign("3", "Group1")
      ret = SapModel.PointObj.SetGroupAssign("3", "Group2")

   'get point object groups
      ret = SapModel.PointObj.GetGroupAssign("3", NumberGroups, Groups)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.0.0.

## See Also

[SetGroupAssign](SetGroupAssign_{Point_Object}.htm)



## GetLoadDispl {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetLoadDispl_{Point_Object}.htm`*

# GetLoadDispl

## Syntax

SapObject.SapModel.PointObj.GetLoadDispl

## VB6 Procedure

Function GetLoadDispl(ByVal Name As String, ByRef NumberItems As Long, ByRef PointName() As String, ByRef LoadPat() As String, ByRef LCStep() As Long, ByRef CSys() As String, ByRef U1() As Double, ByRef U2() As Double, ByRef U3() As Double, ByRef R1() As Double, ByRef R2() As Double, ByRef R3() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object or group, depending on the value of the ItemType item.

NumberItems

This is the total number of joint ground displacement assignments returned.

PointName

This is an array that includes the name of the point object to which the specified ground displacement assignment applies.

LoadPat

This is an array that includes the name of the load pattern for the ground displacement load.

LCStep

This is an array that includes the load pattern step for the ground displacement load. In most cases, this item does not apply and will be returned as 0.

CSys

This is an array that includes the name of the coordinate system for the ground displacement load. This is Local or the name of a defined coordinate system.

U1

This is an array that includes the assigned translational ground displacement in the local 1-axis or coordinate system X-axis direction, depending on the specified CSys. [L]

U2

This is an array that includes the assigned translational ground displacement in the local 2-axis or coordinate system Y-axis direction, depending on the specified CSys. [L]

U3

This is an array that includes the assigned translational ground displacement in the local 3-axis or coordinate system Z-axis direction, depending on the specified CSys. [L]

R1

This is an array that includes the assigned rotational ground displacement about the local 1-axis or coordinate system X-axis, depending on the specified CSys. [rad]

R2

This is an array that includes the assigned rotational ground displacement about the local 2-axis or coordinate system Y-axis, depending on the specified CSys. [rad]

R3

This is an array that includes the assigned rotational ground displacement about the local 3-axis or coordinate system Z-axis, depending on the specified CSys. [rad]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are retrieved for the point object specified by the Name item.

If this item is Group, the assignments are retrieved for all point objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are retrieved for all selected point objects, and the Name item is ignored.

## Remarks

This function retrieves the ground displacement load assignments to point objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetPointDisplLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim PointName() As String
      Dim LoadPat() As String
      Dim LCStep() As Long
      Dim CSys() As String
      Dim U1() As Double
      Dim U2() As Double
      Dim U3() As Double
      Dim R1() As Double
      Dim R2() As Double
      Dim R3() As Double
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

   'add ground displacement load
      Redim Value(5)
      Value(0) = 10
      ret = SapModel.PointObj.SetLoadDispl("1", "DEAD", Value)

   'get ground displacement load
      ret = SapModel.PointObj.GetLoadDispl("ALL", NumberItems, PointName, LoadPat, LCStep, CSys, U1, U2, U3, R1, R2, R3, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadDispl](SetLoadDispl.htm)

[DeleteLoadDispl](DeleteLoadDispl.htm)



## GetLoadForce {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetLoadForce_{Point_Object}.htm`*

# GetLoadForce

## Syntax

SapObject.SapModel.PointObj.GetLoadForce

## VB6 Procedure

Function GetLoadForce(ByVal Name As String, ByRef NumberItems As Long, ByRef PointName() As String, ByRef LoadPat() As String, ByRef LCStep() As Long, ByRef CSys() As String, ByRef F1() As Double, ByRef F2() As Double, ByRef F3() As Double, ByRef M1() As Double, ByRef M2() As Double, ByRef M3() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object or group, depending on the value of the ItemType item.

NumberItems

This is the total number of joint force load assignments returned.

PointName

This is an array that includes the name of the point object to which the specified load assignment applies.

LoadPat

This is an array that includes the name of the load pattern for the load.

LCStep

This is an array that includes the load pattern step for the load. In most cases, this item does not apply and will be returned as 0.

CSys

This is an array that includes the name of the coordinate system for the load. This is Local or the name of a defined coordinate system.

F1

This is an array that includes the assigned translational force in the local 1-axis or coordinate system X-axis direction, depending on the specified CSys. [F]

F2

This is an array that includes the assigned translational force in the local 2-axis or coordinate system Y-axis direction, depending on the specified CSys. [F]

F3

This is an array that includes the assigned translational force in the local 3-axis or coordinate system Z-axis direction, depending on the specified CSys. [F]

M1

This is an array that includes the assigned moment about the local 1-axis or coordinate system X-axis, depending on the specified CSys. [FL]

M2

This is an array that includes the assigned moment about the local 2-axis or coordinate system Y-axis, depending on the specified CSys. [FL]

M3

This is an array that includes the assigned moment about the local 3-axis or coordinate system Z-axis, depending on the specified CSys. [FL]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignments are retrieved for the point object specified by the Name item.

If this item is Group, the assignments are retrieved for all point objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignments are retrieved for all selected point objects, and the Name item is ignored.

## Remarks

This function retrieves the joint force load assignments to point objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetPointForceLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim NumberItems As Long
      Dim PointName() As String
      Dim LoadPat() As String
      Dim LCStep() As Long
      Dim CSys() As String
      Dim F1() As Double
      Dim F2() As Double
      Dim F3() As Double
      Dim M1() As Double
      Dim M2() As Double
      Dim M3() As Double
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

   'add joint force load
      Redim Value(5)
      Value(0) = 10
      ret = SapModel.PointObj.SetLoadForce("1", "DEAD", Value)

   'get joint force load
      ret = SapModel.PointObj.GetLoadForce("ALL", NumberItems, PointName, LoadPat, LCStep, CSys, F1, F2, F3, M1, M2, M3, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetLoadForce](SetLoadForce.htm)

[DeleteLoadForce](DeleteLoadForce.htm)



## GetLocalAxesAdvanced Point Object

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetLocalAxesAdvanced_Point_Object.htm`*

# GetLocalAxesAdvanced

## Syntax

SapObject.SapModel.PointObj.GetLocalAxesAdvanced

## VB6 Procedure

Function GetLocalAxesAdvanced(ByVal Name As String, ByRef Active As Boolean, ByRef AxVectOpt As Long, ByRef AxCSys As String, ByRef AxDir() As Long, ByRef AxPt() As String, ByRef AxVect() As Double, ByRef Plane2 As Long, ByRef PlVectOpt As Long, ByRef PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double) As Long

## Parameters

Name

The name of an existing point object.

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

This is 12, 13, 21, 23, 31 or 32, indicating that the local plane determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, or 3-2 plane. This item applies only when the Active item is True.

## Remarks

This function assigns advanced local axes to point objects.

The function returns zero if the advanced local axes assignments are assigned successfully; otherwise it returns a nonzero value.

## VBA Example

Sub GetPointAdvancedLocalAxes()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'assign point advanced local axes
      MyAxVect(0)=0.707
      MyAxVect(1)=0.707
      MyAxVect(2)=0
      MyPlDir(0) = 2
      MyPlDir(1) = 3
      ret = SapModel.PointObj.SetLocalAxesAdvanced("ALL", True, 3, "Global", MyAxDir, MyAxPt, MyAxVect, 12, 1, "Global", MyPlDir, MyPlPt, MyPlVect, Group)

   'get point local axes angles
      ret = SapModel.PointObj.GetLocalAxes("1", a, b, c, Advanced)

   'get point advanced local axes data
      If Advanced Then
         ret = SapModel.PointObj.GetLocalAxesAdvanced("3", Active, AxVectOpt, AxCSys, AxDir, AxPt, AxVect, Plane2, PlVectOpt, PlCSys, PlDir, PlPt, PlVect)
      End If

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

## See Also

[SetLocalAxesAdvanced](SetLocalAxesAdvanced_Point_Object.htm)

[SetLocalAxes](SetLocalAxes_{Point_Object}.htm)



## GetLocalAxes {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetLocalAxes_{Point_Object}.htm`*

# GetLocalAxes

## Syntax

SapObject.SapModel.PointObj.GetLocalAxes

## VB6 Procedure

Function GetLocalAxes(ByVal Name As String, ByRef a As Double, ByRef b As Double, ByRef c As Double, ByRef Advanced As Boolean) As Long

## Parameters

Name

The name of an existing point object.

a, b, c

The local axes of the point are defined by first setting the positive local 1, 2 and 3 axes the same as the positive global X, Y and Z axes and then doing the following: [deg]

1.    Rotate about the 3 axis by angle a.

2.    Rotate about the resulting 2 axis by angle b.

3.    Rotate about the resulting 1 axis by angle c.

Advanced

This item is True if the point object local axes orientation was obtained using advanced local axes parameters.

## Remarks

This function retrieves the local axes angles for a point object.

The function returns zero if the local axes angles are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetPointLocalAxes()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'get local axes assignments
      ret = SapModel.PointObj.GetLocalAxes("1", a, b, c, Advanced)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetLocalAxes](SetLocalAxes_{Point_Object}.htm)



## GetMass {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetMass_{Point_Object}.htm`*

# GetMass

## Syntax

SapObject.SapModel.PointObj.GetMass

## VB6 Procedure

Function GetMass(ByVal Name As String, ByRef m() As Double) As Long

## Parameters

Name

The name of an existing point object.

m

This is an array of six mass assignment values.

Value(0) = U1 [M]

Value(1) = U2 [M]

Value(2) = U3 [M]

Value(3) = R1 [ML2]

Value(4) = R2 [ML2]

Value(5) = R3 [ML2]

## Remarks

This function retrieves the point mass assignment values for a point object. The masses are always returned in the point local coordinate system.

The function returns zero if the mass is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetPointMass()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i as long
      Dim m() As Double

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

   'assign point mass
      Redim m(5)
      For i = 0 to 5
         m(i) = (i+1) / 10
      Next i
      ret = SapModel.PointObj.SetMass("3", m)

   'get point mass
      Redim m(5)
      ret = SapModel.PointObj.GetMass("3", m)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMass](SetMass.htm)

[DeleteMass](DeleteMass.htm)

[SetMassByVolume](SetMassByVolume.htm)

[SetMassByWeight](SetMassByWeight.htm)



## GetMergeNumber {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetMergeNumber_{Point_Object}.htm`*

# GetMergeNumber

## Syntax

SapObject.SapModel.PointObj.GetMergeNumber

## VB6 Procedure

Function GetMergeNumber(ByVal Name As String, ByRef MergeNumber As Long) As Long

## Parameters

Name

The name of an existing point object.

MergeNumber

The merge number assigned to the specified point object.

## Remarks

This function retrieves the merge number for a point object. By default the merge number for a point is zero. Points with different merge numbers are not automatically merged by the program.

The function returns zero if the merge number is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetPointMergeNumber()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim m As Long

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

   'set merge number
      ret = SapModel.PointObj.SetMergeNumber("3", 2)

   'get merge number
      ret = SapModel.PointObj.GetMergeNumber("3", m)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetMergeNumber](SetMergeNumber.htm)



## GetNameList {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetNameList_{Point_Object}.htm`*

# GetNameList

## Syntax

SapObject.SapModel.PointObj.GetNameList

## VB6 Procedure

Function GetNameList(ByRef NumberNames As Long, ByRef MyName() As String) As Long

## Parameters

NumberNames

The number of point object names retrieved by the program.

MyName

This is a one-dimensional array of point object names. The MyName array is created as a dynamic, zero-based, array by the API user:

   Dim MyName() as String

The array is dimensioned to (NumberNames – 1) inside the Sap2000 program, filled with the names, and returned to the API user.

## Remarks

This function retrieves the names of all defined point objects.

The function returns zero if the names are successfully retrieved, otherwise it returns nonzero.

## VBA Example

Sub GetPointObjectNames()
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

   'get point object names
      ret = SapModel.PointObj.GetNameList(NumberNames, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetCoordCartesian](GetCoordCartesian_{Point_Object}.htm)

[GetCoordCylindrical](GetCoordCylindrical_{Point_Object}.htm)



## GetPanelZone

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetPanelZone.htm`*

# GetPanelZone

## Syntax

SapObject.SapModel.PointObj.GetPanelZone

## VB6 Procedure

Function GetPanelZone(ByVal Name As String, ByRef PropType As Long, ByRef Thickness As Double, ByRef K1 As Double, ByRef K2 As Double, ByRef LinkProp As String, ByRef Connectivity As Long, ByRef LocalAxisFrom As Long, ByRef LocalAxisAngle As Double) As Long

## Parameters

Name

The name of an existing point object.

PropType

This is 0, 1, 2, or 3.

0 = Properties are elastic from column

1 = Properties are elastic from column and doubler plate

2 = Properties are from specified spring stiffnesses

3 = Properties are from a specified link property

Thickness

The thickness of the doubler plate. This item applies only when PropType = 1. [L]

K1

The spring stiffness for major axis bending (about the local 3 axis of the column and panel zone). This item applies only when PropType = 2. [FL/rad]

K2

The spring stiffness for minor axis bending (about the local 2 axis of the column and panel zone). This item applies only when PropType = 2. [FL/rad]

LinkProp

The name of the link property used to define the panel zone. This item applies only when PropType = 3.

Connectivity

This is 0 or 1.

0 = Panel zone connects beams to other objects

1 = Panel zone connects braces to other objects

LocalAxisFrom

This is 0 or 1.

0 = Panel zone local axis angle is from column

1 = Panel zone local axis angle is user defined

The LocalAxisFrom item can be 1 only when the PropType item is 3.

LocalAxisAngle

This item applies only when PropType = 3 and LocalAxisFrom = 1. It is the angle measured counter clockwise from the positive global X-axis to the local 2-axis of the panel zone. [deg]

## Remarks

This function retrieves the panel zone assignment data for a point object.

The function returns zero if the panel zone data is successfully retrieved, otherwise it returns a nonzero value.

If no panel zone assignment is made to the point object, an error is returned.

## VBA Example

Sub GetPanelZoneData()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim PropType As Long
      Dim Thickness As Double
      Dim K1 As Double
      Dim K2 As Double
      Dim LinkProp As String
      Dim Connectivity As Long
      Dim LocalAxisFrom As Long
      Dim LocalAxisAngle As Double

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

   'assign panel zone
      ret = SapModel.PointObj.SetPanelZone("3", 1, 2, 0, 0, "", 0, 0, 0)

   'get panel zone data
      ret = SapModel.PointObj.GetPanelZone("3", PropType, Thickness, K1, K2, LinkProp, Connectivity, LocalAxisFrom, LocalAxisAngle)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetPanelZone](SetPanelZone.htm)



## GetPatternValue {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetPatternValue_{Point_Object}.htm`*

# GetPatternValue

## Syntax

SapObject.SapModel.PointObj.GetPatternValue

## VB6 Procedure

Function GetPatternValue(ByVal Name As String, ByVal PatternName As String, ByRef Value As Double) As Long

## Parameters

Name

The name of an existing point object.

PatternName

The name of a defined joint pattern.

Value

The value that the specified point object has for the specified joint pattern.

## Remarks

This function retrieves the joint pattern value for a specific point object and joint pattern.

The function returns zero if the value is successfully retrieved, otherwise it returns a nonzero value.

Joint pattern values are unitless.

## VBA Example

Sub GetJointPatternData()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add joint pattern assignment
      ret = SapModel.PointObj.SetPatternByXYZ("ALL", "Default", 0, 0, 10, 0, Group)

   'get joint pattern assignment
      ret = SapModel.PointObj.GetPatternValue("3", "Default", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetPatternByPressure](SetPatternByPressure.htm)

[SetPatternByXYZ](SetPatternByXYZ.htm)

[DeletePatternValue](DeletePatternValue.htm)



## GetRestraint {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetRestraint_{Point_Object}.htm`*

# GetRestraint

## Syntax

SapObject.SapModel.PointObj.GetRestraint

## VB6 Procedure

Function GetRestraint(ByVal Name As String, ByRef Value() As Boolean) As Long

## Parameters

Name

The name of an existing point object.

Value

This is an array of six restraint values.

Value(0) = U1

Value(1) = U2

Value(2) = U3

Value(3) = R1

Value(4) = R2

Value(5) = R3

## Remarks

This function retrieves the restraint assignments for a point object. The restraint assignments are always returned in the point local coordinate system.

The function returns zero if the restraint assignments are successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetPointRestraints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value() As Boolean

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

   'get point object restraints
      Redim Value(5)
      ret = SapModel.PointObj.GetRestraint("5", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetRestraint](SetRestraint.htm)

[DeleteRestraint](DeleteRestraint.htm)



## GetSelected {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetSelected_{Point_Object}.htm`*

# GetSelected

## Syntax

SapObject.SapModel.PointObj.GetSelected

## VB6 Procedure

Function GetSelected(ByVal Name As String, ByRef Selected As Boolean) As Long

## Parameters

Name

The name of an existing point object.

Selected

This item returns True if the specified point object is selected, otherwise it returns False.

## Remarks

This function retrieves the selected status for a point object.

The function returns zero if the selected status is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetPointSelectedStatus()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'set point selected
      ret = SapModel.PointObj.SetSelected("3", True)

   'get point selected status
      ret = SapModel.PointObj.GetSelected("3", Selected)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSelected](SetSelected_{Point_Object}.htm)



## GetSpecialPoint

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetSpecialPoint.htm`*

# GetSpecialPoint

## Syntax

SapObject.SapModel.PointObj.GetSpecialPoint

## VB6 Procedure

Function GetSpecialPoint(ByVal Name As String, ByVal SpecialPoint As Boolean) As Long

## Parameters

Name

The name of an existing point object.

SpecialPoint

This item is True if the point object is specified as a special point, otherwise it is False.

## Remarks

This function retrieves the special point status for a point object.

The function returns zero if the special point status is successfully retrieved, otherwise it returns a nonzero value.

Special points are allowed to exist in the model even if no objects (line, area, solid, link) are connected to them. Points that are not special are automatically deleted if no objects connect to them.

## VBA Example

Sub GetSpecialPointStatus()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim SpecialPoint As Boolean

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

   'set as special point
      ret = SapModel.PointObj.SetSpecialPoint("3", True)

   'get special point status
      ret = SapModel.PointObj.GetSpecialPoint("3", SpecialPoint)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[SetSpecialPoint](SetSpecialPoint.htm)

[DeleteSpecialPoint](DeleteSpecialPoint.htm)



## GetSpringCoupled {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetSpringCoupled_{Point_Object}.htm`*

# GetSpringCoupled

## Syntax

SapObject.SapModel.PointObj.GetSpringCoupled

## VB6 Procedure

Function GetSpringCoupled(ByVal Name As String, ByRef k() As Double) As Long

## Parameters

Name

The name of an existing point object.

k

This is an array of twenty one spring stiffness values.

Value(0) = U1U1 [F/L]

Value(1) = U1U2 [F/L]

Value(2) = U2U2 [F/L]

Value(3) = U1U3 [F/L]

Value(4) = U2U3 [F/L]

Value(5) = U3U3 [F/L]

Value(6) = U1R1 [F/rad]

Value(7) = U2R1 [F/rad]

Value(8) = U3R1 [F/rad]

Value(9) = R1R1 [FL/rad]

Value(10) = U1R2 [F/rad]

Value(11) = U2R2 [F/rad]

Value(12) = U3R2 [F/rad]

Value(13) = R1R2 [FL/rad]

Value(14) = R2R2 [FL/rad]

Value(15) = U1R3 [F/rad]

Value(16) = U2R3 [F/rad]

Value(17) = U3R3 [F/rad]

Value(18) = R1R3 [FL/rad]

Value(19) = R2R3 [FL/rad]

Value(20) = R3R3 [FL/rad]

## Remarks

This function retrieves coupled spring stiffness assignments for a point object.

The spring stiffnesses reported are the sum of all springs assigned to the point object. The spring stiffness values are reported in the point local coordinate system.

The function returns zero if the stiffnesses are successfully retrieved, otherwise it returns a nonzero value. If no springs exist at the point object, the function returns a nonzero value.

## VBA Example

Sub GetSpringCoupled()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim k() As Double

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

   'assign coupled spring to a point
      ReDim k(20)
      k(2) = 10
      k(17) = 4
      ret = SapModel.PointObj.SetSpringCoupled("3", k)

   'get coupled spring values
      ReDim k(20)
      ret = SapModel.PointObj.GetSpringCoupled("3", k)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Point_Object}.htm)

[SetSpring](SetSpring.htm)

[SetSpringCoupled](SetSpringCoupled.htm)

[DeleteSpring](DeleteSpring_{Point_Object}.htm)

[IsSpringCoupled](IsSpringCoupled_{Point_Object}.htm)



## GetSpring {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetSpring_{Point_Object}.htm`*

# GetSpring

## Syntax

SapObject.SapModel.PointObj.GetSpring

## VB6 Procedure

Function GetSpring(ByVal Name As String, ByRef k() As Double) As Long

## Parameters

Name

The name of an existing point object.

k

This is an array of six spring stiffness values.

Value(0) = U1 [F/L]

Value(1) = U2 [F/L]

Value(2) = U3 [F/L]

Value(3) = R1 [FL/rad]

Value(4) = R2 [FL/rad]

Value(5) = R3 [FL/rad]

## Remarks

This function retrieves uncoupled spring stiffness assignments for a point object, that is, it retrieves the diagonal terms in the 6x6 spring matrix for the point object.

The spring stiffnesses reported are the sum of all springs assigned to the point object. The spring stiffness values are reported in the point local coordinate system.

The function returns zero if the stiffnesses are successfully retrieved, otherwise it returns a nonzero value. If no springs exist at the point object, the function returns a nonzero value.

## VBA Example

Sub GetSpring()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim k() As Double

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

   'assign spring to a point
      ReDim k(5)
      k(2) = 10
      ret = SapModel.PointObj.SetSpring("3", k)

   'get spring values
      ReDim k(5)
      ret = SapModel.PointObj.GetSpring("3", k)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpringCoupled](GetSpringCoupled_{Point_Object}.htm)

[SetSpring](SetSpring.htm)

[SetSpringCoupled](SetSpringCoupled.htm)

[DeleteSpring](DeleteSpring_{Point_Object}.htm)

[IsSpringCoupled](IsSpringCoupled_{Point_Object}.htm)



## GetTransformationMatrix {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/GetTransformationMatrix_{Point_Object}.htm`*

# GetTransformationMatrix

## Syntax

SapObject.SapModel.PointObj.GetTransformationMatrix

## VB6 Procedure

Function GetTransformationMatrix(ByVal Name As String, ByRef Value() As Double,Optional ByVal IsGlobal As Boolean = True) As Long

## Parameters

Name

The name of an existing point object.

Value

Value is an array of nine direction cosines that define the transformation matrix.

The following matrix equation shows how the transformation matrix is used to convert items from the point object local coordinate system to the global coordinate system.

![](../../../assets/images/Images/Transformation%20Matrix.JPG)

In the equation, c0 through c8 are the nine values from the transformation array; (Local1, Local2, Local3) are an item (such as a point load) in the point object local coordinate system; and (GlobalX, GlobalY, GlobalZ) are the same item in the global coordinate system.

The transformation from the local coordinate system to the present coordinate system is the same as that shown above for the global system if you substitute the present system for the global system.

IsGlobal

If this item is True, the transformation matrix is between the Global coordinate system and the point object local coordinate system.

If this item is False, the transformation matrix is between the present coordinate system and the point object local coordinate system.

## Remarks

The function returns zero if the point object transformation matrix is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetPointObjectMatrix()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret as Long
      Dim Value() as double

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

   'set local axes
      ret = SapModel.PointObj.SetLocalAxes("3", 33, 14, 12)

   'get point object transformation matrix
      redim Value(8)
      ret = SapModel.PointObj.GetTransformationMatrix("3", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also



## IsSpringCoupled {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/IsSpringCoupled_{Point_Object}.htm`*

# IsSpringCoupled

## Syntax

SapObject.SapModel.PointObj.IsSpringCoupled

## VB6 Procedure

Function IsSpringCoupled(ByVal Name As String, ByVal IsCoupled As Boolean) As Long

## Parameters

Name

The name of an existing point object.

IsCoupled

This item is True if the spring assigned to the specified point object is coupled, otherwise it is False.

## Remarks

This function indicates if the spring assignments to a point object are coupled, that is, if they have off-diagonal terms in the 6x6 spring matrix for the point object.

The function returns zero if the coupled status is successfully retrieved, otherwise it returns a nonzero value. If no springs exist at the point object,n the function returns a nonzero value.

## VBA Example

Sub CheckIsSpringCoupled()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim k() As Double
      Dim IsCoupled As Boolean

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

   'assign spring to a point
      ReDim k(5)
      k(2) = 10
      ret = SapModel.PointObj.SetSpring("3", k)

   'determine if spring is coupled
      ret = SapModel.PointObj.IsSpringCoupled("3", IsCoupled)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Point_Object}.htm)

[GetSpringCoupled](GetSpringCoupled_{Point_Object}.htm)

[SetSpring](SetSpring.htm)

[SetSpringCoupled](SetSpringCoupled.htm)

[DeleteSpring](DeleteSpring_{Point_Object}.htm)



## SetConstraint

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetConstraint.htm`*

# SetConstraint

## Syntax

SapObject.SapModel.PointObj.SetConstraint

## VB6 Procedure

Function SetConstraint(ByVal Name As String, ConstraintName As String, Optional ByVal ItemType As eItemType = Object, Optional ByVal Replace As Boolean = True) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

ConstraintName

The name of an existing joint constraint.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the constraint assignment is made to the point object specified by the Name item.

If this item is Group,  the constraint assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the constraint assignment is made to all selected point objects and the Name item is ignored.

Replace

If this item is True, all previous joint constraints, if any, assigned to the specified point object(s) are deleted before making the new assignment.

## Remarks

This function makes joint constraint assignments to point objects.

The function returns 0 if the assignment is successfully made, otherwise it returns nonzero.

## VBA Example

Sub SetConstraintAssignment()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long

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

   'define a new constraint
      ret = SapModel.ConstraintDef.SetDiaphragm("Diaph1")

   'define new constraint assignments
      For i = 4 To 16 Step 4
         ret = SapModel.PointObj.SetConstraint(Format(i), "Diaph1")
      Next i

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Modified optional argument Replace to be ByVal in version 12.0.1.

## See Also

[GetConstraint](GetConstraint_{Point_Object}.htm)

[DeleteConstraint](DeleteConstraint.htm)



## SetGUID {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetGUID_{Point_Object}.htm`*

# SetGUID

## Syntax

SapObject.SapModel.PointObj.SetGUID

## VB6 Procedure

Function SetGUID(ByVal Name As String, Optional ByVal GUID As String = "") As Long

## Parameters

Name

The name of an existing point object.

GUID

The GUID (Global Unique ID) for the specified point object.

## Remarks

This function sets the GUID for specified point object. If the GUID is passed in as a blank string, the program automatically creates a GUID for the object.

This function returns zero if the point object GUID is successfully set; otherwise it returns nonzero.

## VBA Example

Sub SetPointGUID()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'set program created GUID
      ret = SapModel.PointObj.SetGUID("1")

   'get GUID
      ret = SapModel.PointObj.GetGUID("1", GUID)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetGUID](GetGUID_{Point_Object}.htm)



## SetGroupAssign {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetGroupAssign_{Point_Object}.htm`*

# SetGroupAssign

## Syntax

SapObject.SapModel.PointObj.SetGroupAssign

## VB6 Procedure

Function SetGroupAssign(ByVal Name As String, ByVal GroupName As String, Optional ByVal Remove As Boolean = False, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

GroupName

The name of an existing group to which the assignment is made.

Remove

If this item is False, the specified point objects are added to the group specified by the GroupName item. If it is True, the point objects are removed from the group.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the point object specified by the Name item is added or removed from the group specified by the GroupName item.

If this item is Group, all point objects in the group specified by the Name item are added or removed from the group specified by the GroupName item.

If this item is SelectedObjects, all selected point objects are added or removed from the group specified by the GroupName item and the Name item is ignored.

## Remarks

This function adds or removes point objects from a specified group.

The function returns zero if the group assignment is successful, otherwise it returns a nonzero value.

## VBA Example

Sub AddPointObjectsToGroup()
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

   'add point objects to group
      ret = SapModel.PointObj.SetGroupAssign("3", "Group1")
      ret = SapModel.PointObj.SetGroupAssign("6", "Group1")
      ret = SapModel.PointObj.SetGroupAssign("9", "Group1")

   'select objects in group
      ret = SapModel.SelectObj.Group("Group1")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Modified optional argument Remove to be ByVal in version 12.0.1.

## See Also

[GetGroupAssign](GetGroupAssign_{Point_Object}.htm)



## SetLoadDispl

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetLoadDispl.htm`*

# SetLoadDispl

## Syntax

SapObject.SapModel.PointObj.SetLoadDispl

## VB6 Procedure

Function SetLoadDispl(ByVal Name As String, ByVal LoadPat As String, ByRef Value() As Double, Optional ByVal Replace As Boolean = False, Optional ByVal CSys As String = "Global", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

LoadPat

The name of the load pattern for the ground displacement load.

Value

This is an array of six ground displacement load values.

Value(0) = U1 [L]

Value(1) = U2 [L]

Value(2) = U3 [L]

Value(3) = R1 [rad]

Value(4) = R2 [rad]

Value(5) = R3 [rad]

Replace

If this item is True, all previous ground displacement loads, if any, assigned to the specified point object(s) in the specified load pattern are deleted before making the new assignment.

CSys

The name of the coordinate system for the considered ground displacement load. This is Local or the name of a defined coordinate system.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignment is made to the point object specified by the Name item.

If this item is Group, the load assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignment is made to all selected point objects and the Name item is ignored.

## Remarks

This function makes ground displacement load assignments to point objects.

The function returns zero if the load assignments are successfully made, otherwise it returns a nonzero value.

## VBA Example

Sub SetPointDisplLoad()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add ground displacement load
      Redim Value(5)
      Value(0) = 10
      ret = SapModel.PointObj.SetLoadDispl("1", "DEAD", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadDispl](GetLoadDispl_{Point_Object}.htm)

[DeleteLoadDispl](DeleteLoadDispl.htm)



## SetLoadForce

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetLoadForce.htm`*

# SetLoadForce

## Syntax

SapObject.SapModel.PointObj.SetLoadForce

## VB6 Procedure

Function SetLoadForce(ByVal Name As String, ByVal LoadPat As String, ByRef Value() As Double, Optional ByVal Replace As Boolean = False, Optional ByVal CSys As String = "Global", Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

LoadPat

The name of the load pattern for the point load.

Value

This is an array of six point load values.

Value(0) = F1 [F]

Value(1) = F2 [F]

Value(2) = F3 [F]

Value(3) = M1 [FL]

Value(4) = M2 [FL]

Value(5) = M3 [FL]

Replace

If this item is True, all previous point loads, if any, assigned to the specified point object(s) in the specified load pattern are deleted before making the new assignment.

CSys

The name of the coordinate system for the considered point load. This is Local or the name of a defined coordinate system.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the load assignment is made to the point object specified by the Name item.

If this item is Group, the load assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the load assignment is made to all selected point objects and the Name item is ignored.

## Remarks

This function makes point load assignments to point objects.

The function returns zero if the load assignments are successfully made, otherwise it returns a nonzero value.

## VBA Example

Sub SetPointForceLoad()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value() As Double
      Dim LoadPat As String
      Dim LCStep As Long
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'add point load
      Redim Value(5)
      Value(0) = 10
      ret = SapModel.PointObj.SetLoadForce("1", "DEAD", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetLoadForce](GetLoadForce_{Point_Object}.htm)

[DeleteLoadForce](DeleteLoadForce.htm)



## SetLocalAxesAdvanced Point Object

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetLocalAxesAdvanced_Point_Object.htm`*

# SetLocalAxesAdvanced

## Syntax

SapObject.SapModel.PointObj.SetLocalAxesAdvanced

## VB6 Procedure

Function SetLocalAxesAdvanced(ByVal Name As String, ByVal Active As Boolean, ByVal AxVectOpt As Long, ByVal AxCSys As String, ByRef AxDir() As Long, ByRef AxPt() As String, ByRef AxVect() As Double, ByVal Plane2 As Long, ByVal PlVectOpt As Long, ByVal PlCSys As String, ByRef PlDir() As Long, ByRef PlPt() As String, ByRef PlVect() As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object or group, depending on the value of the ItemType item.

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

This is 12, 13, 21, 23, 31 or 32, indicating that the local plane determined by the plane reference vector is the 1-2, 1-3, 2-1, 2-3, 3-1, 0r 3-2 plane. This item applies only when the Active item is True.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

Selection = 2

If this item is Object, the assignment is made to the point object specified by the Name item.

If this item is Group, the assignment is made to all point objects in the group specified by the Name item.

If this item is Selection, assignment is made to all selected point objects and the Name item is ignored.

## Remarks

This function assigns advanced local axes to point objects.

The function returns zero if the advanced local axes assignments are assigned successfully; otherwise it returns a nonzero value.

## VBA Example

Sub AssignPointAdvancedLocalAxes()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'assign point advanced local axes
      MyAxVect(0)=0.707
      MyAxVect(1)=0.707
      MyAxVect(2)=0
      MyPlDir(0) = 2
      MyPlDir(1) = 3
      ret = SapModel.PointObj.SetLocalAxesAdvanced("ALL", True, 3, "Global", MyAxDir, MyAxPt, MyAxVect, 12, 1, "Global", MyPlDir, MyPlPt, MyPlVect, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.00.

## See Also

[GetLocalAxesAdvanced](GetLocalAxesAdvanced_Point_Object.htm)

[GetLocalAxes](GetLocalAxes_{Point_Object}.htm)



## SetLocalAxes {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetLocalAxes_{Point_Object}.htm`*

# SetLocalAxes

## Syntax

SapObject.SapModel.PointObj.SetLocalAxes

## VB6 Procedure

Function SetLocalAxes(ByVal Name As String, ByVal a As Double, ByVal b As Double, ByVal c As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

a, b, c

The local axes of the point are defined by first setting the positive local 1, 2 and 3 axes the same as the positive global X, Y and Z axes and then doing the following: [deg]

1.    Rotate about the 3 axis by angle a.

2.    Rotate about the resulting 2 axis by angle b.

3.    Rotate about the resulting 1 axis by angle c.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the local axes assignment is made to the point object specified by the Name item.

If this item is Group, the local axes assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the local axes assignment is made to all selected point objects and the Name item is ignored.

## Remarks

This function sets the local axes angles for point objects.

The function returns zero if the local axes angles are successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetPointLocalAxes()
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

   'set local axes
      ret = SapModel.PointObj.SetLocalAxes("ALL", 90, 0, 0, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetLocalAxes](GetLocalAxes_{Point_Object}.htm)



## SetMass

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetMass.htm`*

# SetMass

## Syntax

SapObject.SapModel.PointObj.SetMass

## VB6 Procedure

Function SetMass(ByVal Name As String, ByRef m() As Double, Optional ByVal ItemType As eItemType = object, Optional ByVal IsLocalCSys As Boolean = True, Optional ByVal Replace As Boolean = False) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

m

This is an array of six mass assignment values.

Value(0) = U1 [M]

Value(1) = U2 [M]

Value(2) = U3 [M]

Value(3) = R1 [ML2]

Value(4) = R2 [ML2]

Value(5) = R3 [ML2]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the mass assignment is made to the point object specified by the Name item.

If this item is Group, the mass assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the mass assignment is made to all selected point objects and the Name item is ignored.

IsLocalCSys

If this item is True, the specified mass assignments are in the point object local coordinate system. If it is False, the assignments are in the Global coordinate system.

Replace

If this item is True, all existing point mass assignments to the specified point object(s) are deleted prior to making the assignment. If it is False, the mass assignments are added to any existing assignments.

## Remarks

This function assigns point mass to a point object.

The function returns zero if the mass is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignPointMass()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      dim i as long
      Dim m() As Double

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

   'assign point mass
      Redim m(5)
      For i = 0 to 5
         m(i) = (i+1) / 10
      Next i
      ret = SapModel.PointObj.SetMass("3", m)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMass](GetMass_{Point_Object}.htm)

[DeleteMass](DeleteMass.htm)

[SetMassByVolume](SetMassByVolume.htm)

[SetMassByWeight](SetMassByWeight.htm)



## SetMassByVolume

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetMassByVolume.htm`*

# SetMassByVolume

## Syntax

Sap2000.PointObj.SetMassByVolume

## VB6 Procedure

Function SetMassByVolume(ByVal Name As String, ByVal MatProp As String, ByRef m() As Double, Optional ByVal ItemType As eItemType = Object, Optional ByVal IsLocalCSys As Boolean = True, Optional ByVal Replace As Boolean = False) As Long

## Parameters

Name

The name of an existing point object or group, depending on the value of the ItemType item.

MatProp

The name of an existing material property.

m

This is an array of six mass assignment values.

Value(0) = U1 [L3]

Value(1) = U2 [L3]

Value(2) = U3 [L3]

Value(3) = R1 [L5]

Value(4) = R2 [L5]

Value(5) = R3 [L5]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the mass assignment is made to the point object specified by the Name item.

If this item is Group, the mass assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the mass assignment is made to all selected point objects and the Name item is ignored.

IsLocalCSys

If this item is True, the specified mass assignments are in the point object local coordinate system. If it is False, the assignments are in the Global coordinate system.

Replace

If this item is True, all existing point mass assignments to the specified point object(s) are deleted prior to making the assignment. If it is False,  the mass assignments are added to any previously existing assignments.

## Remarks

This function assigns point mass to a point object. The program calculates the mass by multiplying the specified values by the mass per unit volume of the specified material property.

The function returns zero if the mass is successfully assigned; otherwise, it returns a nonzero value.

## VBA Example

Sub AssignPointMassByVolume()
   'dimension variables
      Dim SapObject as cOAPI
      Dim ret As Long
      Dim i as long
      Dim m() As Double

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

   'assign point mass
      Redim m(5)
      For i = 0 to 5
         m(i) = 20000 \* (i+1)
      Next i
      ret = SapModel.PointObj.SetMassByVolume("3", "4000psi", m)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel= Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetMass](SetMass.htm)

[SetMassByWeight](SetMassByWeight.htm)

[GetMass](GetMass_{Point_Object}.htm)

[DeleteMass](DeleteMass.htm)



## SetMassByWeight

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetMassByWeight.htm`*

# SetMassByWeight

## Syntax

Sap2000.PointObj.SetMassByWeight

## VB6 Procedure

Function SetMassByWeight(ByVal Name As String, ByRef m() As Double, Optional ByVal ItemType As eItemType = Object, Optional ByVal IsLocalCSys As Boolean = True, Optional ByVal Replace As Boolean = False) As Long

## Parameters

Name

The name of an existing point object or group, depending on the value of the ItemType item.

m

This is an array of six mass assignment values.

Value(0) = U1 [F]

Value(1) = U2 [F]

Value(2) = U3 [F]

Value(3) = R1 [FL2]

Value(4) = R2 [FL2]

Value(5) = R3 [FL2]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the mass assignment is made to the point object specified by the Name item.

If this item is Group, the mass assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the mass assignment is made to all selected point objects and the Name item is ignored.

IsLocalCSys

If this item is True, the specified mass assignments are in the point object local coordinate system. If it is False, the assignments are in the Global coordinate system.

Replace

If this item is True, all existing point mass assignments to the specified point object(s) are deleted prior to making the assignment. If it is False, the mass assignments are added to any previously existing assignments.

## Remarks

This function assigns point mass to a point object. The program calculates the mass by dividing the specified values by the acceleration of gravity.

The function returns zero if the mass is successfully assigned; otherwise. it returns a nonzero value.

## VBA Example

Sub AssignPointMassByWeight()
   'dimension variables
      Dim SapObject as cOAPI
      Dim ret As Long
      Dim i as long
      Dim m() As Double

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

   'assign point mass
      Redim m(5)
      For i = 0 to 2
         m(i) = i+1
      Next i
      ret = SapModel.PointObj.SetMassByWeight("3", m)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel= Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 12.00.

## See Also

[SetMass](SetMass.htm)

[SetMassByVolume](SetMassByVolume.htm)

[GetMass](GetMass_{Point_Object}.htm)

[DeleteMass](DeleteMass.htm)



## SetMergeNumber

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetMergeNumber.htm`*

# SetMergeNumber

## Syntax

SapObject.SapModel.PointObj.SetMergeNumber

## VB6 Procedure

Function SetMergeNumber(ByVal Name As String, ByVal MergeNumber As Long, Optional ByVal ItemType As eItemType = object) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

MergeNumber

The merge number for the specified point object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the merge number assignment is made to the point object specified by the Name item.

If this item is Group, the merge number assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the merge number assignment is made to all selected point objects and the Name item is ignored.

## Remarks

This function assigns a merge number to a point object. By default the merge number for a point is zero. Points with different merge numbers are not automatically merged by the program.

The function returns zero if the merge number is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignPointMergeNumber()
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

   'set merge number
      ret = SapModel.PointObj.SetMergeNumber("3", 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetMergeNumber](GetMergeNumber_{Point_Object}.htm)



## SetPanelZone

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetPanelZone.htm`*

# SetPanelZone

## Syntax

SapObject.SapMdel.PointObj.SetPanelZone

## VB6 Procedure

Function SetPanelZone(ByVal Name As String, ByVal PropType As Long, ByVal Thickness As Double, ByVal K1 As Double, ByVal K2 As Double, ByVal LinkProp As String, ByVal Connectivity As Long, ByVal LocalAxisFrom As Long, ByVal LocalAxisAngle As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object.

PropType

This is 0, 1, 2, or 3.

0 = Properties are elastic from column

1 = Properties are elastic from column and doubler plate

2 = Properties are from specified spring stiffnesses

3 = Properties are from a specified link property

Thickness

The thickness of the doubler plate. This item applies only when PropType = 1. [L]

K1

The spring stiffness for major axis bending (about the local 3 axis of the column and panel zone). This item applies only when PropType = 2. [FL/rad]

K2

The spring stiffness for minor axis bending (about the local 2 axis of the column and panel zone). This item applies only when PropType = 2. [FL/rad]

LinkProp

The name of the link property used to define the panel zone. This item applies only when PropType = 3.

Connectivity

This is 0 or 1.

0 = Panel zone connects beams to other objects

1 = Panel zone connects braces to other objects

LocalAxisFrom

This is 0 or 1.

0 = Panel zone local axis angle is from column

1 = Panel zone local axis angle is user defined

The LocalAxisFrom item can be 1 only when the PropType item is 3.

LocalAxisAngle

This item applies only when PropType = 3 and LocalAxisFrom = 1. It is the angle measured counter clockwise from the positive global X-axis to the local 2-axis of the panel zone. [deg]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the panel zone assignment is made to the point object specified by the Name item.

If this item is Group, the panel zone assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the panel zone assignment is made to all selected point objects and the Name item is ignored.

## Remarks

This function makes panel zone assignments to point objects. Any existing panel zone assignments are replaced by the new assignments.

The function returns zero if the panel zone data is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignPanelZoneData()
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

   'assign panel zone
      ret = SapModel.PointObj.SetPanelZone("3", 1, 2, 0, 0, "", 0, 0, 0)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetPanelZone](GetPanelZone.htm)



## SetPatternByPressure

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetPatternByPressure.htm`*

# SetPatternByPressure

## Syntax

SapObject.SapModel.PointObj.SetPatternByPressure

## VB6 Procedure

Function SetPatternByPressure(ByVal Name As String, ByVal PatternName As String, ByVal Z As Double, ByVal w As Double, u As Double, r As Long, Optional ByVal ItemType As eItemType = Object, Optional ByVal Restriction As Long = 0, Optional ByVal Replace As Boolean = False) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

PatternName

The name of a defined joint pattern.

z

The Z coordinate at zero pressure in the present coordinate system. [L]

w

A weight per unit volume. [F/L3]

u

An added uniform force per unit area. [F/L2]

r

This is 0, 1, or 2.

0 = All values are used

1 = Negative values are set to zero

2 = Positive values are set to zero

This restriction applies ***before*** the pattern value has been added to any existing pattern value assigned to the point object.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object,  the joint pattern assignment is made to the point object specified by the Name item.

If this item is Group, the joint pattern assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the joint pattern assignment is made to all selected point objects and the Name item is ignored.

Restriction

This is 0, 1, or 2.

0 = All values are used

1 = Negative values are set to zero

2 = Positive values are set to zero

This restriction applies ***after*** the pattern value has been added to any existing pattern value assigned to the point object. This restriction applies even if there was no existing joint pattern value on the point object.

Replace

If this item is True, the joint pattern value calculated as shown in the Remarks section replaces any previous joint pattern value for the point object.

If this item is False, the joint pattern value calculated as shown in the Remarks section is added to any previous joint pattern value for the point object and then the Restriction items are checked.

## Remarks

This function sets the joint pattern value for a specified point object and joint pattern.

The joint pattern value is calculated as:

Value = [(z – zpoint) \* w] + u

where z, w and u are described in the Parameters section and zpoint is the Z coordinate of the considered point object in the present coordinate system. All appropriate unit conversions are used to calculate the value in the database units, but thereafter it is assumed to be unitless.

The function returns zero if the pattern value is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub SetJointPatternByPressure()
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

   'add joint pattern assignment
      ret = SapModel.PointObj.SetPatternByPressure("ALL", "Default", 0, 20, 1, 0, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetPatternValue](GetPatternValue_{Point_Object}.htm)

[SetPatternByXYZ](SetPatternByXYZ.htm)

[DeletePatternValue](DeletePatternValue.htm)

[GetPresentCoordSystem](../../General_Functions/GetPresentCoordSystem.htm)

[SetPresentCoordSystem](../../General_Functions/SetPresentCoordSystem.htm)



## SetPatternByXYZ

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetPatternByXYZ.htm`*

# SetPatternByXYZ

## Syntax

SapObject.Sap2000.PointObj.SetPatternByXYZ

## VB6 Procedure

Function SetPatternByXYZ(ByVal Name As String, ByVal PatternName As String, ByVal a As Double, ByVal b As Double, ByVal c As Double, ByVal d As Double, Optional ByVal ItemType As eItemType = object, Optional ByVal Restriction As Long = 0, Optional ByVal Replace As Boolean = False) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

PatternName

The name of a defined joint pattern.

a

The value a in the equation shown in the Remarks section. [1/L]

b

The value b in the equation shown in the Remarks section. [1/L]

c

The value c in the equation shown in the Remarks section. [1/L]

d

The value d in the equation shown in the Remarks section. This item is unitless.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the joint pattern assignment is made to the point object specified by the Name item.

If this item is Group, the joint pattern assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the joint pattern assignment is made to all selected point objects and the Name item is ignored.

Restriction

This is either 0, 1, or 2.

0 = All values are used

1 = Negative values are set to zero

2 = Positive values are set to zero

Replace

If this item is True, the joint pattern value calculated as shown in the Remarks section replaces any previous joint pattern value for the point object.

If this item is False, the joint pattern value calculated as shown in the Remarks section is added to any previous joint pattern value for the point object and then the Restriction items are checked.

## Remarks

This function sets the joint pattern value for a specified point object and joint pattern.

The joint pattern value is calculated as:

Value = ax + by + cz + d

where a, b, c and d are function input parameters and x, y and z are the coordinates of the considered point object in the present coordinate system

The function returns zero if the pattern value is successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub SetJointPatternByXYZ()
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

   'add joint pattern assignment
      ret = SapModel.PointObj.SetPatternByXYZ("ALL", "Default", 0, 0, 10, 0, Group)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetPatternValue](GetPatternValue_{Point_Object}.htm)

[SetPatternByPressure](SetPatternByPressure.htm)

[DeletePatternValue](DeletePatternValue.htm)

[GetPresentCoordSystem](../../General_Functions/GetPresentCoordSystem.htm)

[SetPresentCoordSystem](../../General_Functions/SetPresentCoordSystem.htm)



## SetRestraint

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetRestraint.htm`*

# SetRestraint

## Syntax

SapObject.SapModel.PointObj.SetRestraint

## VB6 Procedure

Function SetRestraint(ByVal Name As String, ByRef Value() As Boolean, Optional ByVal ItemType As eItemType = object) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

Value

This is an array of six restraint values.

Value(0) = U1

Value(1) = U2

Value(2) = U3

Value(3) = R1

Value(4) = R2

Value(5) = R3

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the restraint assignment is made to the point object specified by the Name item.

If this item is Group, the restraint assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the restraint assignment is made to all selected point objects and the Name item is ignored.

## Remarks

This function assigns the restraint assignments for a point object. The restraint assignments are always set in the point local coordinate system.

The function returns zero if the restraint assignments are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignPointRestraints()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim i As Long
      Dim Value() As Boolean

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

   'assign point object restraints
      Redim Value(5)
      For i = 0 to 5
         Value(i) = True
      Next i
      ret = SapModel.PointObj.setRestraint("1", Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetRestraint](GetRestraint_{Point_Object}.htm)

[DeleteRestraint](DeleteRestraint.htm)



## SetSelected {Point Object}

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetSelected_{Point_Object}.htm`*

# SetSelected

## Syntax

SapObject.SapModel.PointObj.SetSelected

## VB6 Procedure

Function SetSelected(ByVal Name As String, ByVal Selected As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

Selected

This item is True if the specified point object is selected, otherwise it is False.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the selected status is set for the point object specified by the Name item.

If this item is Group, the selected status is set for all point objects in the group specified by the Name item.

If this item is SelectedObjects, the selected status is set for all selected point objects and the Name item is ignored.

## Remarks

This function sets the selected status for a point object.

The function returns zero if the selected status is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetPointSelected()
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

   'set point selected
      ret = SapModel.PointObj.SetSelected("3", True)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSelected](GetSelected_{Point_Object}.htm)



## SetSpecialPoint

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetSpecialPoint.htm`*

# SetSpecialPoint

## Syntax

SapObject.SapModel.PointObj.SetSpecialPoint

## VB6 Procedure

Function SetSpecialPoint(ByVal Name As String, ByVal SpecialPoint As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

SpecialPoint

This item is True if the point object is specified as a special point, otherwise it is False.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the special point status is set for the point object specified by the Name item.

If this item is Group, the special point status is set for all point objects in the group specified by the Name item.

If this item is SelectedObjects, the special point status is set for all selected point objects and the Name item is ignored.

## Remarks

This function sets the special point status for a point object.

The function returns zero if the special point status is successfully set, otherwise it returns a nonzero value.

Special points are allowed to exist in the model even if no objects (line, area, solid, link) are connected to them. Points that are not special are automatically deleted if no objects connect to them.

## VBA Example

Sub SetSpecialPoint()
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

   'set as special point
      ret = SapModel.PointObj.SetSpecialPoint("3", True)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpecialPoint](GetSpecialPoint.htm)

[DeleteSpecialPoint](DeleteSpecialPoint.htm)



## SetSpring

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetSpring.htm`*

# SetSpring

## Syntax

SapObject.SapModel.PointObj.SetSpring

## VB6 Procedure

Function SetSpring(ByVal Name As String, ByRef k() As Double, Optional ByVal ItemType As eItemType = object, Optional ByVal IsLocalCSys As Boolean = False, Optional ByVal Replace As Boolean = False) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

k

This is an array of six spring stiffness values.

Value(0) = U1 [F/L]

Value(1) = U2 [F/L]

Value(2) = U3 [F/L]

Value(3) = R1 [FL/rad]

Value(4) = R2 [FL/rad]

Value(5) = R3 [FL/rad]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the spring assignment is made to the point object specified by the Name item.

If this item is Group, the spring assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the spring assignment is made to all selected point objects and the Name item is ignored.

IsLocalCSys

If this item is True, the specified spring assignments are in the point object local coordinate system. If it is False, the assignments are in the Global coordinate system.

Replace

If this item is True, all existing point spring assignments to the specified point object(s) are deleted prior to making the assignment. If it is False, the spring assignments are added to any existing assignments.

## Remarks

This function assigns coupled springs to a point object.

The function returns zero if the stiffnesses are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignPointSpring()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim k() As Double

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

   'assign spring to a point
      ReDim k(5)
      k(2) = 10
      ret = SapModel.PointObj.SetSpring("3", k)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Point_Object}.htm)

[GetSpringCoupled](GetSpringCoupled_{Point_Object}.htm)

[SetSpringCoupled](GetSpringCoupled_{Point_Object}.htm)

[DeleteSpring](DeleteSpring_{Point_Object}.htm)

[IsSpringCoupled](IsSpringCoupled_{Point_Object}.htm)



## SetSpringCoupled

*Source file: `SAP2000_API_Fuctions/Object_Model/Point_Object/SetSpringCoupled.htm`*

# SetSpringCoupled

## Syntax

SapObject.SapModel.PointObj.SetSpringCoupled

## VB6 Procedure

Function SetSpringCoupled(ByVal Name As String, ByRef k() As Double, Optional ByVal ItemType As eItemType = object, Optional ByVal IsLocalCSys As Boolean = False, Optional ByVal Replace As Boolean = False) As Long

## Parameters

Name

The name of an existing point object or group depending on the value of the ItemType item.

k

This is an array of twenty one spring stiffness values.

Value(0) = U1U1 [F/L]

Value(1) = U1U2 [F/L]

Value(2) = U2U2 [F/L]

Value(3) = U1U3 [F/L]

Value(4) = U2U3 [F/L]

Value(5) = U3U3 [F/L]

Value(6) = U1R1 [F/rad]

Value(7) = U2R1 [F/rad]

Value(8) = U3R1 [F/rad]

Value(9) = R1R1 [FL/rad]

Value(10) = U1R2 [F/rad]

Value(11) = U2R2 [F/rad]

Value(12) = U3R2 [F/rad]

Value(13) = R1R2 [FL/rad]

Value(14) = R2R2 [FL/rad]

Value(15) = U1R3 [F/rad]

Value(16) = U2R3 [F/rad]

Value(17) = U3R3 [F/rad]

Value(18) = R1R3 [FL/rad]

Value(19) = R2R3 [FL/rad]

Value(20) = R3R3 [FL/rad]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the spring assignment is made to the point object specified by the Name item.

If this item is Group, the spring assignment is made to all point objects in the group specified by the Name item.

If this item is SelectedObjects, the spring assignment is made to all selected point objects and the Name item is ignored.

IsLocalCSys

If this item is True, the specified spring assignments are in the point object local coordinate system. If it is False, the assignments are in the Global coordinate system.

Replace

If this item is True, all existing point spring assignments to the specified point object(s) are deleted prior to making the assignment. If it is False, the spring assignments are added to any existing assignments.

## Remarks

This function assigns coupled springs to a point object.

The function returns zero if the stiffnesses are successfully assigned, otherwise it returns a nonzero value.

## VBA Example

Sub AssignCoupledSpring()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim k() As Double

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

   'assign coupled spring to a point
      ReDim k(20)
      k(2) = 10
      k(17) = 4
      ret = SapModel.PointObj.SetSpringCoupled("3", k)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.00.

## See Also

[GetSpring](GetSpring_{Point_Object}.htm)

[GetSpringCoupled](GetSpringCoupled_{Point_Object}.htm)

[SetSpring](SetSpring.htm)

[DeleteSpring](DeleteSpring_{Point_Object}.htm)

[IsSpringCoupled](IsSpringCoupled_{Point_Object}.htm)

