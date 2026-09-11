# API Definitions Concrete Shell Design Requests

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Definitions/Concrete_Shell_Design_Requests

---



## Add {Concrete Shell Design List}

*Source file: `SAP2000_API_Fuctions/Definitions/Concrete_Shell_Design_Requests/Add_{Concrete_Shell_Design_List}.htm`*

# Add {Concrete Shell Design List}

## Syntax

SapObject.SapModel.DesignConcreteShell.DesignRequest.Add

## VB6 Procedure

Function Add(ByVal RequestName As String, ByVal GroupList() As String, ByVal ComboList() As String, ByVal AutoCombo As Boolean, ByVal AutoComboCaseList() As String) As Long

## Parameters

RequestName

The name of a new concrete shell design request. It may be the same as any existing design request.

GroupList

This is an array that has the name of the groups to be added in the new design request.

ComboList

This is an array that has the name of the load combinations to be added in the new design request.

AutoCombo

If this item is True, the code-based design load combinations for concrete shell design are automatically generated based on the list of load cases in the AutoComboCaseList and included in the design request. If it is False, the code-based design load combinations will not be included in the design request.

AutoComboCaseList

This is an array that has the name of the load cases used to automatically generate code-based design load combinations.

## Remarks

This function adds a new concrete shell design request.

The function returns zero if the design request is successfully removed; otherwise it returns a nonzero value.

The function will fail if the RequestName does not exist.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub AddConcreteShellDesignRequest()
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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fluid", eLoadPatternType.EarthHydrostatic)

'add point load

Dim LoadValue() As Double

ReDim LoadValue(5)

LoadValue(1) = 10

ret = SapModel.PointObj.SetLoadForce("14", "DEAD", LoadValue)

'add combo

ret = SapModel.RespCombo.Add("COMB1", 1)

ret = SapModel.RespCombo.Add("COMB2", 1)

ret = SapModel.RespCombo.Add("COMB3", 1)

ret = SapModel.RespCombo.Add("COMB4", 1)

'add load case to combo

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.1)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.2)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.3)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.4)

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

‘create concrete shell design request

Dim RequestName As String

Dim GroupList() As String

Dim ComboList() As String

Dim AutoCombo As Boolean

Dim AutoComboCaseList() As String

Dim NewName As String

Dim NumberRequest As Integer

Dim RequestList() As String

Dim NumberGroup As Integer

Dim NumberCombo As Integer

RequestName = "R1"

ReDim RequestList(1)

RequestList(0) = ""

RequestList(1) = ""

ReDim GroupList(1)

ReDim ComboList(1)

ReDim AutoComboCaseList(2)

GroupList(1) = "GROUP1"

ComboList(1) = "COMB1"

AutoCombo = True

AutoComboCaseList(1) = "DEAD"

AutoComboCaseList(2) = "Fluid"

‘add new concrete shell design request

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0

## See Also



## ChangeName {Concrete Shell Design Request}

*Source file: `SAP2000_API_Fuctions/Definitions/Concrete_Shell_Design_Requests/ChangeName_{Concrete_Shell_Design_Request}.htm`*

# ChangeName {Concrete Shell Design Request}

## Syntax

SapObject.SapModel.DesignConcreteShell.DesignRequest.ChangeName

## VB6 Procedure

Function ChangeName(ByVal RequestName As String, ByVal NewRequestName As String) As Long

## Parameters

RequestName

The name of an existing design request.

NewRequestName

The new name the design request will be changed to.

## Remarks

This function changes the name of a concrete shell design request.

The function returns zero if the name is successfully changed; otherwise it returns a nonzero value.

The function will fail if the RequestName does not exist or NewName is nothing.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub ChangeDesignRequestName()
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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fluid", eLoadPatternType.EarthHydrostatic)

'add point load

Dim LoadValue() As Double

ReDim LoadValue(5)

LoadValue(1) = 10

ret = SapModel.PointObj.SetLoadForce("14", "DEAD", LoadValue)

'add combo

ret = SapModel.RespCombo.Add("COMB1", 1)

ret = SapModel.RespCombo.Add("COMB2", 1)

ret = SapModel.RespCombo.Add("COMB3", 1)

ret = SapModel.RespCombo.Add("COMB4", 1)

'add load case to combo

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.1)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.2)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.3)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.4)

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

‘create design request

Dim RequestName As String

Dim GroupList() As String

Dim ComboList() As String

Dim AutoCombo As Boolean

Dim AutoComboCaseList() As String

Dim NewName As String

Dim NumberRequest As Integer

Dim RequestList() As String

Dim NumberGroup As Integer

Dim NumberCombo As Integer

RequestName = "R1"

ReDim RequestList(1)

RequestList(0) = ""

RequestList(1) = ""

ReDim GroupList(1)

ReDim ComboList(1)

ReDim AutoComboCaseList(2)

GroupList(1) = "GROUP1"

ComboList(1) = "COMB1"

AutoCombo = True

AutoComboCaseList(1) = "DEAD"

AutoComboCaseList(2) = "Fluid"

‘add new design request

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

‘change design request name

NewName = "R11"

ret = SapModel.DesignConcreteShell.DesignRequest.ChangeName(RequestName, NewName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0

## See Also



## Delete {Concrete Shell Design Request}

*Source file: `SAP2000_API_Fuctions/Definitions/Concrete_Shell_Design_Requests/Delete_{Concrete_Shell_Design_Request}.htm`*

# Delete

## Syntax

SapObject.SapModel.DesignConcreteShell.DesignRequest.Delete

## VB6 Procedure

Function Delete(ByVal Name As String) As Long

## Parameters

RequestName

The name of an existing concrete shell design request that is to be removed.

## Remarks

This function deletes a concrete shell design request.

The function returns zero if the design request is successfully removed; otherwise it returns a nonzero value.

The function will fail if the RequestName does not exist.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub DeleteDesignRequest()
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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fluid", eLoadPatternType.EarthHydrostatic)

'add point load

Dim LoadValue() As Double

ReDim LoadValue(5)

LoadValue(1) = 10

ret = SapModel.PointObj.SetLoadForce("14", "DEAD", LoadValue)

'add combo

ret = SapModel.RespCombo.Add("COMB1", 1)

ret = SapModel.RespCombo.Add("COMB2", 1)

ret = SapModel.RespCombo.Add("COMB3", 1)

ret = SapModel.RespCombo.Add("COMB4", 1)

'add load case to combo

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.1)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.2)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.3)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.4)

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

Dim RequestName As String

Dim GroupList() As String

Dim ComboList() As String

Dim AutoCombo As Boolean

Dim AutoComboCaseList() As String

Dim NewName As String

Dim NumberRequest As Integer

Dim RequestList() As String

Dim NumberGroup As Integer

Dim NumberCombo As Integer

RequestName = "R1"

ReDim RequestList(1)

RequestList(0) = ""

RequestList(1) = ""

ReDim GroupList(1)

ReDim ComboList(1)

ReDim AutoComboCaseList(2)

GroupList(1) = "GROUP1"

ComboList(1) = "COMB1"

AutoCombo = True

AutoComboCaseList(1) = "DEAD"

AutoComboCaseList(2) = "Fluid"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

ret = SapModel.DesignConcreteShell.DesignRequest.Delete(RequestName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0

## See Also



## Get Combo List {Concrete Shell Design Request}

*Source file: `SAP2000_API_Fuctions/Definitions/Concrete_Shell_Design_Requests/Get_Combo_List_{Concrete_Shell_Design_Request}.htm`*

# GetComboList {Concrete Shell Design Request}

## Syntax

SapObject.SapModel.DesignConcreteShell.DesignRequest.GetComboList

## VB6 Procedure

Function GetComboList (ByVal RequestName As String, ByRef NumberCombo As Integer, ByRef ComboList() As String) As Long

## Parameters

RequestName

The name of an existing concrete shell design request whose group information is to be retrieved.

NumberCombo

The number of load combinations in the design request.

ComboList

This is an array containing the name of all the load combinations in the design request.

## Remarks

This function retrieves the list of load combinations in a design request.

The function returns zero if the list of load combinations in the design request is successfully retrieved; otherwise it returns a nonzero value.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub GetGroupList ()
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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fluid", eLoadPatternType.EarthHydrostatic)

'add point load

Dim LoadValue() As Double

ReDim LoadValue(5)

LoadValue(1) = 10

ret = SapModel.PointObj.SetLoadForce("14", "DEAD", LoadValue)

'add combo

ret = SapModel.RespCombo.Add("COMB1", 1)

ret = SapModel.RespCombo.Add("COMB2", 1)

ret = SapModel.RespCombo.Add("COMB3", 1)

ret = SapModel.RespCombo.Add("COMB4", 1)

'add load case to combo

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.1)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.2)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.3)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.4)

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

Dim RequestName As String

Dim GroupList() As String

Dim ComboList() As String

Dim AutoCombo As Boolean

Dim AutoComboCaseList() As String

Dim NewName As String

Dim NumberRequest As Integer

Dim RequestList() As String

Dim NumberGroup As Integer

Dim NumberCombo As Integer

RequestName = "R1"

ReDim RequestList(1)

RequestList(0) = ""

RequestList(1) = ""

ReDim GroupList(1)

ReDim ComboList(1)

ReDim AutoComboCaseList(2)

GroupList(1) = "GROUP1"

ComboList(1) = "COMB1"

AutoCombo = True

AutoComboCaseList(1) = "DEAD"

AutoComboCaseList(2) = "Fluid"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

NewName = "R11"

ret = SapModel.DesignConcreteShell.DesignRequest.ChangeName(RequestName, NewName)

RequestName = "R2"

GroupList(1) = "GROUP2"

ComboList(1) = "COMB2"

AutoCombo = False

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

RequestName = "R123"

ReDim GroupList(3)

ReDim ComboList(3)

GroupList(1) = "GROUP1"

GroupList(2) = "GROUP2"

GroupList(3) = "GROUP3"

ComboList(1) = "COMB1"

ComboList(2) = "COMB2"

ComboList(3) = "COMB3"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetRequestList(NumberRequest, RequestList)

RequestName = "R123"

ReDim GroupList(0)

ReDim ComboList(0)

ret = SapModel.DesignConcreteShell.DesignRequest.GetGroupList(RequestName, NumberGroup, GroupList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetComboList(RequestName, NumberCombo, ComboList)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0

## See Also



## Get Group List {Concrete Shell Design Request}

*Source file: `SAP2000_API_Fuctions/Definitions/Concrete_Shell_Design_Requests/Get_Group_List_{Concrete_Shell_Design_Request}.htm`*

# GetGroupList {Concrete Shell Design Request}

## Syntax

SapObject.SapModel.DesignConcreteShell.DesignRequest.GetGroupList

## VB6 Procedure

Function  GetGroupList (ByVal RequestName As String, ByRef NumberGroup As Integer, ByRef GroupList() As String) As Long

## Parameters

RequestName

The name of an existing concrete shell design request whose group information is to be retrieved.

NumberGroup

The number of groups in the design request.

GroupList

This is an array containing the name of all the groups in the design request.

## Remarks

This function retrieves the list of all the groups in a design request.

The function returns zero if the list of groups in the design request is successfully retrieved; otherwise it returns a nonzero value.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub GetGroupList ()
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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fluid", eLoadPatternType.EarthHydrostatic)

'add point load

Dim LoadValue() As Double

ReDim LoadValue(5)

LoadValue(1) = 10

ret = SapModel.PointObj.SetLoadForce("14", "DEAD", LoadValue)

'add combo

ret = SapModel.RespCombo.Add("COMB1", 1)

ret = SapModel.RespCombo.Add("COMB2", 1)

ret = SapModel.RespCombo.Add("COMB3", 1)

ret = SapModel.RespCombo.Add("COMB4", 1)

'add load case to combo

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.1)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.2)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.3)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.4)

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

Dim RequestName As String

Dim GroupList() As String

Dim ComboList() As String

Dim AutoCombo As Boolean

Dim AutoComboCaseList() As String

Dim NewName As String

Dim NumberRequest As Integer

Dim RequestList() As String

Dim NumberGroup As Integer

Dim NumberCombo As Integer

RequestName = "R1"

ReDim RequestList(1)

RequestList(0) = ""

RequestList(1) = ""

ReDim GroupList(1)

ReDim ComboList(1)

ReDim AutoComboCaseList(2)

GroupList(1) = "GROUP1"

ComboList(1) = "COMB1"

AutoCombo = True

AutoComboCaseList(1) = "DEAD"

AutoComboCaseList(2) = "Fluid"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

NewName = "R11"

ret = SapModel.DesignConcreteShell.DesignRequest.ChangeName(RequestName, NewName)

RequestName = "R2"

GroupList(1) = "GROUP2"

ComboList(1) = "COMB2"

AutoCombo = False

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

RequestName = "R123"

ReDim GroupList(3)

ReDim ComboList(3)

GroupList(1) = "GROUP1"

GroupList(2) = "GROUP2"

GroupList(3) = "GROUP3"

ComboList(1) = "COMB1"

ComboList(2) = "COMB2"

ComboList(3) = "COMB3"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetRequestList(NumberRequest, RequestList)

RequestName = "R123"

ReDim GroupList(0)

ReDim ComboList(0)

ret = SapModel.DesignConcreteShell.DesignRequest.GetGroupList(RequestName, NumberGroup, GroupList)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0

## See Also



## Get Request List {Concrete Shell Design Request}

*Source file: `SAP2000_API_Fuctions/Definitions/Concrete_Shell_Design_Requests/Get_Request_List_{Concrete_Shell_Design_Request}.html`*

# GetRequestList {Concrete Shell Design Request}

## Syntax

SapObject.SapModel.DesignConcreteShell.DesignRequest.GetRequestList

## VB6 Procedure

Function GetRequestList (ByRef NumberRequest As Integer, ByRef RequestList() As String) As Long

## Parameters

NumberRequest

The number of design requests existing in the model.

RequestList

This is an array containing the name of all the design requests existing in the model.

## Remarks

This function retrieves the list of design requests in the model.

The function returns zero if the list of design request is successfully retrieved; otherwise it returns a nonzero value.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub GetDesignRequestList ()
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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fluid", eLoadPatternType.EarthHydrostatic)

'add point load

Dim LoadValue() As Double

ReDim LoadValue(5)

LoadValue(1) = 10

ret = SapModel.PointObj.SetLoadForce("14", "DEAD", LoadValue)

'add combo

ret = SapModel.RespCombo.Add("COMB1", 1)

ret = SapModel.RespCombo.Add("COMB2", 1)

ret = SapModel.RespCombo.Add("COMB3", 1)

ret = SapModel.RespCombo.Add("COMB4", 1)

'add load case to combo

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.1)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.2)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.3)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.4)

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

Dim RequestName As String

Dim GroupList() As String

Dim ComboList() As String

Dim AutoCombo As Boolean

Dim AutoComboCaseList() As String

Dim NewName As String

Dim NumberRequest As Integer

Dim RequestList() As String

Dim NumberGroup As Integer

Dim NumberCombo As Integer

RequestName = "R1"

ReDim RequestList(1)

RequestList(0) = ""

RequestList(1) = ""

ReDim GroupList(1)

ReDim ComboList(1)

ReDim AutoComboCaseList(2)

GroupList(1) = "GROUP1"

ComboList(1) = "COMB1"

AutoCombo = True

AutoComboCaseList(1) = "DEAD"

AutoComboCaseList(2) = "Fluid"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

NewName = "R11"

ret = SapModel.DesignConcreteShell.DesignRequest.ChangeName(RequestName, NewName)

RequestName = "R2"

GroupList(1) = "GROUP2"

ComboList(1) = "COMB2"

AutoCombo = False

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

RequestName = "R123"

ReDim GroupList(3)

ReDim ComboList(3)

GroupList(1) = "GROUP1"

GroupList(2) = "GROUP2"

GroupList(3) = "GROUP3"

ComboList(1) = "COMB1"

ComboList(2) = "COMB2"

ComboList(3) = "COMB3"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetRequestList(NumberRequest, RequestList)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0

## See Also



## SetAutoCombo {Concrete Shell Design Request}

*Source file: `SAP2000_API_Fuctions/Definitions/Concrete_Shell_Design_Requests/SetAutoCombo_{Concrete_Shell_Design_Request}.htm`*

# SetAutoCombo {Concrete Shell Design List}

## Syntax

SapObject.SapModel.DesignConcreteShell.DesignRequest.SetAutoCombo

## VB6 Procedure

Function SetAutoCombo(ByVal RequestName As String, ByVal AutoComboCaseList() As String) As Long

## Parameters

RequestName

The name of an existing concrete shell design request to which the  automatically-generated code-based load combination is to be added.

AutoComboCaseList

This is an array containing the name of the load cases included in the automatically-generated code-based load combination to be created.

## Remarks

This function adds automatically-generated code-based load combination to a design request.

The function returns zero if the automatically-generated code-based load combinations are successfully created; otherwise it returns a nonzero value.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub SetAutoCombo()
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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fluid", eLoadPatternType.EarthHydrostatic)

'add point load

Dim LoadValue() As Double

ReDim LoadValue(5)

LoadValue(1) = 10

ret = SapModel.PointObj.SetLoadForce("14", "DEAD", LoadValue)

'add combo

ret = SapModel.RespCombo.Add("COMB1", 1)

ret = SapModel.RespCombo.Add("COMB2", 1)

ret = SapModel.RespCombo.Add("COMB3", 1)

ret = SapModel.RespCombo.Add("COMB4", 1)

'add load case to combo

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.1)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.2)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.3)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.4)

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

Dim RequestName As String

Dim GroupList() As String

Dim ComboList() As String

Dim AutoCombo As Boolean

Dim AutoComboCaseList() As String

Dim NewName As String

Dim NumberRequest As Integer

Dim RequestList() As String

Dim NumberGroup As Integer

Dim NumberCombo As Integer

RequestName = "R1"

ReDim RequestList(1)

RequestList(0) = ""

RequestList(1) = ""

ReDim GroupList(1)

ReDim ComboList(1)

ReDim AutoComboCaseList(2)

GroupList(1) = "GROUP1"

ComboList(1) = "COMB1"

AutoCombo = True

AutoComboCaseList(1) = "DEAD"

AutoComboCaseList(2) = "Fluid"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

NewName = "R11"

ret = SapModel.DesignConcreteShell.DesignRequest.ChangeName(RequestName, NewName)

RequestName = "R2"

GroupList(1) = "GROUP2"

ComboList(1) = "COMB2"

AutoCombo = False

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

RequestName = "R123"

ReDim GroupList(3)

ReDim ComboList(3)

GroupList(1) = "GROUP1"

GroupList(2) = "GROUP2"

GroupList(3) = "GROUP3"

ComboList(1) = "COMB1"

ComboList(2) = "COMB2"

ComboList(3) = "COMB3"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetRequestList(NumberRequest, RequestList)

RequestName = "R123"

ReDim GroupList(0)

ReDim ComboList(0)

ret = SapModel.DesignConcreteShell.DesignRequest.GetGroupList(RequestName, NumberGroup, GroupList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetComboList(RequestName, NumberCombo, ComboList)

ReDim GroupList(2)

GroupList(1) = "GROUP3"

GroupList(2) = "GROUP4"

ret = SapModel.DesignConcreteShell.DesignRequest.SetGroup(RequestName, GroupList)

ReDim ComboList(2)

ComboList(1) = "COMB3"

ComboList(2) = "COMB4"

ret = SapModel.DesignConcreteShell.DesignRequest.SetCombo(RequestName, ComboList)

‘set auto combo

Dim AutoComboCaseList1() As String

ReDim AutoComboCaseList1(2)

AutoComboCaseList1(1) = "DEAD"

AutoComboCaseList1(2) = "Fluid"

RequestName = "R2"

ret = SapModel.DesignConcreteShell.DesignRequest.SetAutoCombo(RequestName, AutoComboCaseList1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0

## See Also



## SetCombo {Concrete Shell Design List}

*Source file: `SAP2000_API_Fuctions/Definitions/Concrete_Shell_Design_Requests/SetCombo_{Concrete_Shell_Design_List}.htm`*

# SetCombo {Concrete Shell Design List}

## Syntax

SapObject.SapModel.DesignConcreteShell.DesignRequest.SetCombo

## VB6 Procedure

Function SetCombo(ByVal RequestName As String, ByVal ComboList() As String) As Long

## Parameters

RequestName

The name of an existing concrete shell design request to which the list of load combinations is to be added.

ComboList

This is an array that has the name of the load combinations to be added in the new design request.

## Remarks

This function adds load combinations into a concrete shell design request.

The function returns zero if the load combinations are successfully included in the design request; otherwise it returns a nonzero value.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub SetCombo()
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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fluid", eLoadPatternType.EarthHydrostatic)

'add point load

Dim LoadValue() As Double

ReDim LoadValue(5)

LoadValue(1) = 10

ret = SapModel.PointObj.SetLoadForce("14", "DEAD", LoadValue)

'add combo

ret = SapModel.RespCombo.Add("COMB1", 1)

ret = SapModel.RespCombo.Add("COMB2", 1)

ret = SapModel.RespCombo.Add("COMB3", 1)

ret = SapModel.RespCombo.Add("COMB4", 1)

'add load case to combo

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.1)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.2)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.3)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.4)

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

Dim RequestName As String

Dim GroupList() As String

Dim ComboList() As String

Dim AutoCombo As Boolean

Dim AutoComboCaseList() As String

Dim NewName As String

Dim NumberRequest As Integer

Dim RequestList() As String

Dim NumberGroup As Integer

Dim NumberCombo As Integer

RequestName = "R1"

ReDim RequestList(1)

RequestList(0) = ""

RequestList(1) = ""

ReDim GroupList(1)

ReDim ComboList(1)

ReDim AutoComboCaseList(2)

GroupList(1) = "GROUP1"

ComboList(1) = "COMB1"

AutoCombo = True

AutoComboCaseList(1) = "DEAD"

AutoComboCaseList(2) = "Fluid"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

NewName = "R11"

ret = SapModel.DesignConcreteShell.DesignRequest.ChangeName(RequestName, NewName)

RequestName = "R2"

GroupList(1) = "GROUP2"

ComboList(1) = "COMB2"

AutoCombo = False

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

RequestName = "R123"

ReDim GroupList(3)

ReDim ComboList(3)

GroupList(1) = "GROUP1"

GroupList(2) = "GROUP2"

GroupList(3) = "GROUP3"

ComboList(1) = "COMB1"

ComboList(2) = "COMB2"

ComboList(3) = "COMB3"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetRequestList(NumberRequest, RequestList)

RequestName = "R123"

ReDim GroupList(0)

ReDim ComboList(0)

ret = SapModel.DesignConcreteShell.DesignRequest.GetGroupList(RequestName, NumberGroup, GroupList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetComboList(RequestName, NumberCombo, ComboList)

ReDim GroupList(2)

GroupList(1) = "GROUP3"

GroupList(2) = "GROUP4"

ret = SapModel.DesignConcreteShell.DesignRequest.SetGroup(RequestName, GroupList)

ReDim ComboList(2)

ComboList(1) = "COMB3"

ComboList(2) = "COMB4"

ret = SapModel.DesignConcreteShell.DesignRequest.SetCombo(RequestName, ComboList)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0

## See Also



## SetGroup {Concrete Shell Design List}

*Source file: `SAP2000_API_Fuctions/Definitions/Concrete_Shell_Design_Requests/SetGroup_{Concrete_Shell_Design_List}.htm`*

# SetGroup {Concrete Shell Design List}

## Syntax

SapObject.SapModel.DesignConcreteShell.DesignRequest.SetGroup

## VB6 Procedure

Function SetGroup(ByVal RequestName As String, ByVal GroupList() As String) As Long

## Parameters

RequestName

The name of an existing concrete shell design request to which the list of groups is to be added.

GroupList

This is an array that has the name of the groups to be added in the new design request.

## Remarks

This function deletes a concrete shell design request.

The function returns zero if the groups are successfully included in the design request; otherwise it returns a nonzero value.

The function is not applicable for the Eurocode 2-2004 concrete shell design code.

## VBA Example

Sub SetGroup()
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

ret = SapModel.InitializeNewModel(eUnits.kip\_in\_F)

'create a wall model from template

ret = SapModel.File.NewWall(6, 4, 6, 4)

'initialize new material property

ret = SapModel.PropMaterial.SetMaterial("Rebar", eMatType.Rebar)

'assign other properties

ret = SapModel.PropMaterial.SetORebar\_1("Rebar", 62, 93, 70, 102, 2, 2, 0.02, 0.1, -0.1, False)

'set new area property

ret = SapModel.PropArea.SetShell\_1("A1", 1, True, "4000Psi", 0, 16, 16)

'set area property design parameters

ret = SapModel.PropArea.SetShellDesign("A1", "Rebar", 2, 2, 3, 2.5, 3.5)

'set area property

ret = SapModel.AreaObj.SetProperty("4", "A1")

'define new group

ret = SapModel.GroupDef.SetGroup("GROUP1")

ret = SapModel.GroupDef.SetGroup("GROUP2")

ret = SapModel.GroupDef.SetGroup("GROUP3")

ret = SapModel.GroupDef.SetGroup("GROUP4")

ret = SapModel.AreaObj.SetGroupAssign("1", "GROUP1")

ret = SapModel.AreaObj.SetGroupAssign("2", "GROUP2")

ret = SapModel.AreaObj.SetGroupAssign("3", "GROUP3")

ret = SapModel.AreaObj.SetGroupAssign("4", "GROUP4")

'add new load pattern

ret = SapModel.LoadPatterns.Add("Fluid", eLoadPatternType.EarthHydrostatic)

'add point load

Dim LoadValue() As Double

ReDim LoadValue(5)

LoadValue(1) = 10

ret = SapModel.PointObj.SetLoadForce("14", "DEAD", LoadValue)

'add combo

ret = SapModel.RespCombo.Add("COMB1", 1)

ret = SapModel.RespCombo.Add("COMB2", 1)

ret = SapModel.RespCombo.Add("COMB3", 1)

ret = SapModel.RespCombo.Add("COMB4", 1)

'add load case to combo

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.1)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.2)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.3)

ret = SapModel.RespCombo.SetCaseList("COMB1", eCNameType.LoadCase, "DEAD", 1.4)

'set concrete shell design code

ret = SapModel.DesignConcreteShell.SetCode("ACI 350-20")

Dim RequestName As String

Dim GroupList() As String

Dim ComboList() As String

Dim AutoCombo As Boolean

Dim AutoComboCaseList() As String

Dim NewName As String

Dim NumberRequest As Integer

Dim RequestList() As String

Dim NumberGroup As Integer

Dim NumberCombo As Integer

RequestName = "R1"

ReDim RequestList(1)

RequestList(0) = ""

RequestList(1) = ""

ReDim GroupList(1)

ReDim ComboList(1)

ReDim AutoComboCaseList(2)

GroupList(1) = "GROUP1"

ComboList(1) = "COMB1"

AutoCombo = True

AutoComboCaseList(1) = "DEAD"

AutoComboCaseList(2) = "Fluid"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

NewName = "R11"

ret = SapModel.DesignConcreteShell.DesignRequest.ChangeName(RequestName, NewName)

RequestName = "R2"

GroupList(1) = "GROUP2"

ComboList(1) = "COMB2"

AutoCombo = False

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

RequestName = "R123"

ReDim GroupList(3)

ReDim ComboList(3)

GroupList(1) = "GROUP1"

GroupList(2) = "GROUP2"

GroupList(3) = "GROUP3"

ComboList(1) = "COMB1"

ComboList(2) = "COMB2"

ComboList(3) = "COMB3"

ret = SapModel.DesignConcreteShell.DesignRequest.Add(RequestName, GroupList, ComboList, AutoCombo, AutoComboCaseList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetRequestList(NumberRequest, RequestList)

RequestName = "R123"

ReDim GroupList(0)

ReDim ComboList(0)

ret = SapModel.DesignConcreteShell.DesignRequest.GetGroupList(RequestName, NumberGroup, GroupList)

ret = SapModel.DesignConcreteShell.DesignRequest.GetComboList(RequestName, NumberCombo, ComboList)

ReDim GroupList(2)

GroupList(1) = "GROUP3"

GroupList(2) = "GROUP4"

ret = SapModel.DesignConcreteShell.DesignRequest.SetGroup(RequestName, GroupList)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.0.0

## See Also

