# API Design Aluminum

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Design/Aluminum

---



## GetOverwrite {Aluminum AA 2015}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/AA_2015/GetOverwrite_{Aluminum_AA_2015}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignAluminum.AA\_2015.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with aluminum frame design procedure.

Item

This is an integer between 1 and 27, inclusive, indicating the overwrite item considered.

1 = Live load reduction factor

2 = Unbraced length ratio, Major

3 = Unbraced length ratio, Minor

4 = Unbraced length, Lateral Torsional Buckling (LTB)

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Effective length factor, K LTB

8 = Bending coefficient, Cb

9 = Buckling constant for compression, k1

10 = Buckling constant for compression, k2

11 = Buckling constant for bending, k1

12 = Buckling constant for bending, k2

13 = Safety coefficient, kt

14 = Bending coefficient, C1

15 = Bending coefficient, C2

16 = Net area over gross area ratio

17 = Buckling constant, Ct

18 = Coordinate of load application, Za

19 = Demand/Capacity ratio limit

20 = Effective length factor, K1 Major

21 = Effective length factor, K1 Minor

22 = Moment coefficient factor, Cm Major

23 = Moment coefficient factor, Cm Minor

24 = Nonsway moment factor, B1 Major

25 = Nonsway moment factor, B1 Minor

26 = Sway moment factor, B2 Major

27 = Sway moment factor, B2 Minor

Value

The value of the considered overwrite item.

1 = Live load reduction factor

Value >= 0; 0 means use a program determined value.

2 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Effective length factor, K LTB

Value >= 0; 0 means use program determined value.

8 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

9 = Buckling constant for compression, k1

Value >= 0; 0 means use program determined value.

10 = Buckling constant for compression, k2

Value >= 0; 0 means use program determined value.

11 = Buckling constant for bending, k1

Value >= 0; 0 means use program determined value.

12 = Buckling constant for bending, k2

Value >= 0; 0 means use program determined value.

13 = Safety coefficient, kt

Value >= 0; 0 means use program determined value.

14 = Bending coefficient, C1

Value >= 0; 0 means use program determined value.

15 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

16 = Net area over gross area ratio

Value >= 0; 0 means use program determined value.

17 = Buckling constant, Ct

Value >= 0; 0 means use program determined value.

18 = Coordinate of load application, Za

Value >= 0; 0 means use program determined value.

19 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K1 Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K1 Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

24 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

25 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of an aluminum design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignOverwriteItemAA\_2015()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA 2015")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'get overwrite item
      ret = SapModel.DesignAluminum.AA\_2015.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.1.0

Added items 20 through 27 in version 27.0.0

## See Also

[SetOverwrite](SetOverwrite_{Aluminum_AA_2015}.htm)



## GetPreference {Aluminum AA 2015}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/AA_2015/GetPreference_{Aluminum_AA_2015}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignAluminum.AA\_2015.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 16, inclusive, indicating the preference item considered.

1 = Demand/capacity ratio limit

2 = Design Provision

3 = Lateral Factor

4 = Use Lateral Factor

5 = Bridge Type Structure

6 = PhiTy or OmegaTy safety factor

7 = PhiTr or OmegaTr safety factor

8 = PhiC or OmegaC safety factor

9 = PhiBo or OmegaBo safetyfactor

10 = PhiBr or OmegaBr safetyfactor

11 = PhicVo or OmegaVo safetyfactor

12 = PhiVr or OmegaVr safetyfactor

13 = Time history design

14 = Analysis Method

15 = Second Order Method

16 = Stiffness Reduction Method

Value

The value of the considered preference item.

1 = Demand/capacity ratio limit

Value > 0

2 = Design Provision

1 = LRFD

2 = ASD

3 = Lateral Factor

Value > 0

4 = Use Lateral Factor

1 = No

2 = Yes

5 = Bridge Type Structure

1 = No

2 = Yes

6 = PhiTy or OmegaTy safety factor

PhiTy:           0 < Value ≤ 1

OmegaTy:     1 ≤ Value

7 = PhiTr or OmegaTr safety factor

PhiTr:           0 < Value ≤ 1

OmegaTr:     1 ≤ Value

8 = PhiC or OmegaC safety factor

PhiC:           0 < Value ≤ 1

OmegaC:     1 ≤ Value

9 = PhiBo or OmegaBo safetyfactor

PhiBo:           0 < Value ≤ 1

OmegaBo:     1 ≤ Value

10 = PhiBr or OmegaBr safetyfactor

 PhiBr:           0 < Value ≤ 1

 OmegaBr:     1 ≤ Value

11 = PhicVo or OmegaVo safetyfactor

 PhiVo:           0 < Value ≤ 1

 OmegaVo:     1 ≤ Value

12 = PhiVr or OmegaVr safetyfactor

 PhiVr:           0 < Value ≤ 1

 OmegaVr:     1 ≤ Value

13 = Time history design

1 = Envelopes

2 = Step-by-step

14 = Analysis method

1 = Direct Analysis Method

2 = Effective Length

3 = Limited 1st Order

15 = Second Order Method

1 = General 2nd Order

2 = Amplified 1st Order

16 = Stiffness Reduction method

1 = Tau-b Variable

2 = Tau-b Fixed

3 = No Modification

If Design Provision is 1 (LRFD), the values of items 6 through 12 will come from the Phi factors. Otherwise, if Design Provision is 2 (ASD), the values of items 6 through 12 will come from the Omega factors.

## Remarks

This function retrieves the value of an aluminum design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignPreferenceItemAA\_2015()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA 2015")

   'get preference item
      ret = SapModel.DesignAluminum.AA\_2015.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.1.0

Added items 14 through 16 in version 27.0.0

## See Also

[SetPreference](SetPreference_{Aluminum_AA_2015}.htm)



## SetOverwrite {Aluminum AA 2015}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/AA_2015/SetOverwrite_{Aluminum_AA_2015}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignAluminum.AA\_2015.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 27, inclusive, indicating the overwrite item considered.

1 = Live load reduction factor

2 = Unbraced length ratio, Major

3 = Unbraced length ratio, Minor

4 = Unbraced length, Lateral Torsional Buckling (LTB)

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Effective length factor, K LTB

8 = Bending coefficient, Cb

9 = Buckling constant for compression, k1

10 = Buckling constant for compression, k2

11 = Buckling constant for bending, k1

12 = Buckling constant for bending, k2

13 = Safety coefficient, kt

14 = Bending coefficient, C1

15 = Bending coefficient, C2

16 = Net area over gross area ratio

17 = Buckling constant, Ct

18 = Coordinate of load application, Za

19 = Demand/Capacity ratio limit

20 = Effective length factor, K1 Major

21 = Effective length factor, K1 Minor

22 = Moment coefficient factor, Cm Major

23 = Moment coefficient factor, Cm Minor

24 = Nonsway moment factor, B1 Major

25 = Nonsway moment factor, B1 Minor

26 = Sway moment factor, B2 Major

27 = Sway moment factor, B2 Minor

Value

The value of the considered overwrite item.

1 = Live load reduction factor

Value >= 0; 0 means use a program determined value.

2 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Effective length factor, K LTB

Value >= 0; 0 means use program determined value.

8 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

9 = Buckling constant for compression, k1

Value >= 0; 0 means use program determined value.

10 = Buckling constant for compression, k2

Value >= 0; 0 means use program determined value.

11 = Buckling constant for bending, k1

Value >= 0; 0 means use program determined value.

12 = Buckling constant for bending, k2

Value >= 0; 0 means use program determined value.

13 = Safety coefficient, kt

Value >= 0; 0 means use program determined value.

14 = Bending coefficient, C1

Value >= 0; 0 means use program determined value.

15 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

16 = Net area over gross area ratio

Value >= 0; 0 means use program determined value.

17 = Buckling constant, Ct

Value >= 0; 0 means use program determined value.

18 = Coordinate of load application, Za

Value >= 0; 0 means use program determined value.

19 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K1 Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K1 Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

24 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

25 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of an aluminum design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignOverwriteItemAA\_2015()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA 2015")

   'set overwrite item
      ret = SapModel.DesignAluminum.AA\_2015.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.1.0

Added items 20 through 27 in version 27.0.0

## See Also

[GetOverwrite](GetOverwrite_{Aluminum_AA_2015}.htm)



## SetPreference {Aluminum AA 2015}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/AA_2015/SetPreference_{Aluminum_AA_2015}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignAluminum.AA\_2015.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 16, inclusive, indicating the preference item considered.

1 = Demand/capacity ratio limit

2 = Design Provision

3 = Lateral Factor

4 = Use Lateral Factor

5 = Bridge Type Structure

6 = PhiTy or OmegaTy safety factor

7 = PhiTr or OmegaTr safety factor

8 = PhiC or OmegaC safety factor

9 = PhiBo or OmegaBo safetyfactor

10 = PhiBr or OmegaBr safetyfactor

11 = PhicVo or OmegaVo safetyfactor

12 = PhiVr or OmegaVr safetyfactor

13 = Time history design

14 = Analysis Method

15 = Second Order Method

16 = Stiffness Reduction Method

Value

The value of the considered preference item.

1 = Demand/capacity ratio limit

Value > 0

2 = Design Provision

1 = LRFD

2 = ASD

3 = Lateral Factor

Value > 0

4 = Use Lateral Factor

1 = No

2 = Yes

5 = Bridge Type Structure

1 = No

2 = Yes

6 = PhiTy or OmegaTy safety factor

PhiTy:           0 < Value ≤ 1

OmegaTy:     1 ≤ Value

7 = PhiTr or OmegaTr safety factor

PhiTr:           0 < Value ≤ 1

OmegaTr:     1 ≤ Value

8 = PhiC or OmegaC safety factor

PhiC:           0 < Value ≤ 1

OmegaC:     1 ≤ Value

9 = PhiBo or OmegaBo safetyfactor

PhiBo:           0 < Value ≤ 1

OmegaBo:     1 ≤ Value

10 = PhiBr or OmegaBr safetyfactor

 PhiBr:           0 < Value ≤ 1

 OmegaBr:     1 ≤ Value

11 = PhicVo or OmegaVo safetyfactor

 PhiVo:           0 < Value ≤ 1

 OmegaVo:     1 ≤ Value

12 = PhiVr or OmegaVr safetyfactor

 PhiVr:           0 < Value ≤ 1

 OmegaVr:     1 ≤ Value

13 = Time history design

1 = Envelopes

2 = Step-by-step

14 = Analysis method

1 = Direct Analysis Method

2 = Effective Length

3 = Limited 1st Order

15 = Second Order Method

1 = General 2nd Order

2 = Amplified 1st Order

16 = Stiffness Reduction method

1 = Tau-b Variable

2 = Tau-b Fixed

3 = No Modification

If Design Provision is 1 (LRFD), the Phi factors will be set to have the values of items 6 through 12. Otherwise, if Design Provision is 2 (ASD), the Omega factors will be set to have the values of items 6 through 12.

## Remarks

This function sets the value of an aluminum design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignPreferenceItemAA\_2015()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA 2015")

   'set preference item
      ret = SapModel.DesignAluminum.AA\_2015.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.1.0

Added items 14 through 16 in version 27.0.0

## See Also

[GetPreference](GetPreference_{Aluminum_AA_2015}.htm)



## GetOverwrite {Aluminum AA 2020}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/AA_2020/GetOverwrite_{Aluminum_AA_2020}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignAluminum.AA\_2020.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with aluminum frame design procedure.

Item

This is an integer between 1 and 26, inclusive, indicating the overwrite item considered.

1 = Live load reduction factor

2 = Unbraced length ratio, Major

3 = Unbraced length ratio, Minor

4 = Unbraced length, Lateral Torsional Buckling (LTB)

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Effective length factor, K LTB

8 = Bending coefficient, Cb

9 = Buckling constant for compression, k1

10 = Buckling constant for compression, k2

11 = Buckling constant for bending, k1

12 = Buckling constant for bending, k2

13 = Safety coefficient, kt

14 = Bending coefficient, C1

15 = Bending coefficient, C2

16 = Net area over gross area ratio

17 = Coordinate of load application, Za

18 = Demand/Capacity ratio limit

19 = Effective length factor, K1 Major

20 = Effective length factor, K1 Minor

21 = Moment coefficient factor, Cm Major

22 = Moment coefficient factor, Cm Minor

23 = Nonsway moment factor, B1 Major

24 = Nonsway moment factor, B1 Minor

25 = Sway moment factor, B2 Major

26 = Sway moment factor, B2 Minor

Value

The value of the considered overwrite item.

1 = Live load reduction factor

Value >= 0; 0 means use a program determined value.

2 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Effective length factor, K LTB

Value >= 0; 0 means use program determined value.

8 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

9 = Buckling constant for compression, k1

Value >= 0; 0 means use program determined value.

10 = Buckling constant for compression, k2

Value >= 0; 0 means use program determined value.

11 = Buckling constant for bending, k1

Value >= 0; 0 means use program determined value.

12 = Buckling constant for bending, k2

Value >= 0; 0 means use program determined value.

13 = Safety coefficient, kt

Value >= 0; 0 means use program determined value.

14 = Bending coefficient, C1

Value >= 0; 0 means use program determined value.

15 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

16 = Net area over gross area ratio

Value >= 0; 0 means use program determined value.

17 = Coordinate of load application, Za

Value >= 0; 0 means use program determined value.

18 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K1 Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K1 Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

24 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

25 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of an aluminum design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignOverwriteItemAA\_2020()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA 2020")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'get overwrite item
      ret = SapModel.DesignAluminum.AA\_2020.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 23.2.0

Added items 19 through 26 in version 27.0.0

## See Also

[SetOverwrite](SetOverwrite_{Aluminum_AA_2020}.htm)



## GetPreference {Aluminum AA 2020}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/AA_2020/GetPreference_{Aluminum_AA_2020}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignAluminum.AA\_2020.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 15, inclusive, indicating the preference item considered.

1 = Demand/capacity ratio limit

2 = Design Provision

3 = Lateral Factor

4 = Use Lateral Factor

5 = PhiTy or OmegaTy safety factor

6 = PhiTr or OmegaTr safety factor

7 = PhiC or OmegaC safety factor

9 = PhiBo or OmegaBo safetyfactor

9 = PhiBr or OmegaBr safetyfactor

10 = PhicVo or OmegaVo safetyfactor

11 = PhiVr or OmegaVr safetyfactor

12 = Time history design

13 = Analysis Method

14 = Second Order Method

15 = Stiffness Reduction Method

Value

The value of the considered preference item.

1 = Demand/capacity ratio limit

Value > 0

2 = Design Provision

1 = LRFD

2 = ASD

3 = Lateral Factor

Value > 0

4 = Use Lateral Factor

1 = No

2 = Yes

5 = PhiTy or OmegaTy safety factor

PhiTy:           0 < Value ≤ 1

OmegaTy:     1 ≤ Value

6 = PhiTr or OmegaTr safety factor

PhiTr:           0 < Value ≤ 1

OmegaTr:     1 ≤ Value

7 = PhiC or OmegaC safety factor

PhiC:           0 < Value ≤ 1

OmegaC:     1 ≤ Value

8 = PhiBo or OmegaBo safetyfactor

PhiBo:           0 < Value ≤ 1

OmegaBo:     1 ≤ Value

9 = PhiBr or OmegaBr safetyfactor

 PhiBr:           0 < Value ≤ 1

 OmegaBr:     1 ≤ Value

10 = PhicVo or OmegaVo safetyfactor

 PhiVo:           0 < Value ≤ 1

 OmegaVo:     1 ≤ Value

11 = PhiVr or OmegaVr safetyfactor

 PhiVr:           0 < Value ≤ 1

 OmegaVr:     1 ≤ Value

12 = Time history design

1 = Envelopes

2 = Step-by-step

13 = Analysis method

1 = Direct Analysis Method

2 = Effective Length

3 = Limited 1st Order

14 = Second Order Method

1 = General 2nd Order

2 = Amplified 1st Order

15 = Stiffness Reduction method

1 = Tau-b Variable

2 = Tau-b Fixed

3 = No Modification

If Design Provision is 1 (LRFD), the values of items 5through 11 will come from the Phi factors. Otherwise, if Design Provision is 2 (ASD) , the values of items 5 through 11 will come from the Omega factors .

## Remarks

This function retrieves the value of an aluminum design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignPreferenceItemAA\_2020()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA 2020")

   'get preference item
      ret = SapModel.DesignAluminum.AA\_2020.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 23.2.0

Added items 13 through 15 in version 27.0.0

## See Also

[SetPreference](SetPreference_{Aluminum_AA_2020}.htm)



## SetOverwrite {Aluminum AA 2020}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/AA_2020/SetOverwrite_{Aluminum_AA_2020}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignAluminum.AA\_2020.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of a frame object with a aluminum frame design procedure.

Item

This is an integer between 1 and 26, inclusive, indicating the overwrite item considered.

1 = Live load reduction factor

2 = Unbraced length ratio, Major

3 = Unbraced length ratio, Minor

4 = Unbraced length, Lateral Torsional Buckling (LTB)

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Effective length factor, K LTB

8 = Bending coefficient, Cb

9 = Buckling constant for compression, k1

10 = Buckling constant for compression, k2

11 = Buckling constant for bending, k1

12 = Buckling constant for bending, k2

13 = Safety coefficient, kt

14 = Bending coefficient, C1

15 = Bending coefficient, C2

16 = Net area over gross area ratio

17 = Coordinate of load application, Za

18 = Demand/Capacity ratio limit

19 = Effective length factor, K1 Major

20 = Effective length factor, K1 Minor

21 = Moment coefficient factor, Cm Major

22 = Moment coefficient factor, Cm Minor

23 = Nonsway moment factor, B1 Major

24 = Nonsway moment factor, B1 Minor

25 = Sway moment factor, B2 Major

26 = Sway moment factor, B2 Minor

Value

The value of the considered overwrite item.

1 = Live load reduction factor

Value >= 0; 0 means use a program determined value.

2 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

3 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Effective length factor, K LTB

Value >= 0; 0 means use program determined value.

8 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

9 = Buckling constant for compression, k1

Value >= 0; 0 means use program determined value.

10 = Buckling constant for compression, k2

Value >= 0; 0 means use program determined value.

11 = Buckling constant for bending, k1

Value >= 0; 0 means use program determined value.

12 = Buckling constant for bending, k2

Value >= 0; 0 means use program determined value.

13 = Safety coefficient, kt

Value >= 0; 0 means use program determined value.

14 = Bending coefficient, C1

Value >= 0; 0 means use program determined value.

15 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

16 = Net area over gross area ratio

Value >= 0; 0 means use program determined value.

17 = Coordinate of load application, Za

Value >= 0; 0 means use program determined value.

18 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K1 Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K1 Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

24 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

25 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of an aluminum design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignOverwriteItemAA\_2020()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA 2020")

   'set overwrite item
      ret = SapModel.DesignAluminum.AA\_2020.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.1.0

Added items 19 through 26 in version 27.0.0

## See Also

[GetOverwrite](GetOverwrite_{Aluminum_AA_2020}.htm)



## SetPreference {Aluminum AA 2020}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/AA_2020/SetPreference_{Aluminum_AA_2020}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignAluminum.AA\_2020.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 15, inclusive, indicating the preference item considered.

1 = Demand/capacity ratio limit

2 = Design Provision

3 = Lateral Factor

4 = Use Lateral Factor

5 = PhiTy or OmegaTy safety factor

6 = PhiTr or OmegaTr safety factor

7 = PhiC or OmegaC safety factor

9 = PhiBo or OmegaBo safetyfactor

9 = PhiBr or OmegaBr safetyfactor

10 = PhicVo or OmegaVo safetyfactor

11 = PhiVr or OmegaVr safetyfactor

12 = Time history design

13 = Analysis Method

14 = Second Order Method

15 = Stiffness Reduction Method

Value

The value of the considered preference item.

1 = Demand/capacity ratio limit

Value > 0

2 = Design Provision

1 = LRFD

2 = ASD

3 = Lateral Factor

Value > 0

4 = Use Lateral Factor

1 = No

2 = Yes

5 = PhiTy or OmegaTy safety factor

PhiTy:           0 < Value ≤ 1

OmegaTy:     1 ≤ Value

6 = PhiTr or OmegaTr safety factor

PhiTr:           0 < Value ≤ 1

OmegaTr:     1 ≤ Value

7 = PhiC or OmegaC safety factor

PhiC:           0 < Value ≤ 1

OmegaC:     1 ≤ Value

8 = PhiBo or OmegaBo safetyfactor

PhiBo:           0 < Value ≤ 1

OmegaBo:     1 ≤ Value

9 = PhiBr or OmegaBr safetyfactor

 PhiBr:           0 < Value ≤ 1

 OmegaBr:     1 ≤ Value

10 = PhicVo or OmegaVo safetyfactor

 PhiVo:           0 < Value ≤ 1

 OmegaVo:     1 ≤ Value

11 = PhiVr or OmegaVr safetyfactor

 PhiVr:           0 < Value ≤ 1

 OmegaVr:     1 ≤ Value

12 = Time history design

1 = Envelopes

2 = Step-by-step

13 = Analysis method

1 = Direct Analysis Method

2 = Effective Length

3 = Limited 1st Order

14 = Second Order Method

1 = General 2nd Order

2 = Amplified 1st Order

15 = Stiffness Reduction method

1 = Tau-b Variable

2 = Tau-b Fixed

3 = No Modification

If Design Provision is 1 (LRFD), the Phi factors will be set to have the values of items 5 through 11. Otherwise, if Design Provision is 2 (ASD), the Omega factors will be set to have the values of items 5 through 11.

## Remarks

This function sets the value of an aluminum design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignPreferenceItemAA\_2020()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA 2020")

   'set preference item
      ret = SapModel.DesignAluminum.AA\_2020.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 23.2.0

Added items 13 through 15 in version 27.0.0

## See Also

[GetPreference](GetPreference_{Aluminum_AA_2020}.htm)



## DeleteResults {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/DeleteResults_{Aluminum}.htm`*

# DeleteResults

## Syntax

SapObject.SapModel.DesignAluminum.DeleteResults

## VB6 Procedure

Function DeleteResults() As Long

## Parameters

None

## Remarks

This function deletes all aluminum frame design results.

The function returns zero if the results are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteAluminumDesignResults()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'delete aluminum design results
      ret = SapModel.DesignAluminum.DeleteResults

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## GetOverwrite {Aluminum EC9 2007}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/EC_9_2007/GetOverwrite_{Aluminum_EC9_2007}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignAluminum.Eurocode\_9\_2007.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with aluminum frame design
procedure.

Item

This is an integer between 1 and 29, inclusive, indicating
the overwrite item considered.

1 = Demand/capacity ratio
limit

2 = Live load reduction
factor

3 = Net area to total area
ratio

4 = Material buckling class

5
= Unbraced length ratio, y-y

6 = Unbraced length ratio,
z-z

7 = Unbraced length ratio,
LTB

8 = Effective length factor
sway, Ky

9 = Effective length factor
sway, Kz

10 = Effective length factor,
K LTB

11 = LTB fixed end

12 = Bending coefficient,
C1

13 = Bending coefficient,
C2

14 = Bending coefficient,
C3

15 = Torsional-flexural
buckling curve

16 = Buckling curve for
LTB

17 = Tensile capacity,
Nt,Rd

18 = Elastic torsional
buckling force, NcrT

19 = Elastic torsional-flexural
buckling force, NcrTF

20 = Compressive capacity,
NRk

21 = Bending capacity about
y-y axis, MyRk

22 = Bending capacity about
z-z axis, MzRk

23 = Elastic critical moment
for lateral-torsional buckling, Mcr

24 = Shear capacity along
z-z axis, Vz.Rd

25 = Shear capacity along
y-y axis, Vy.Rd

26 = Torsion capacity,
TRd

27 = Shear stress due to
warping torsion moment,  *τw*

28 = Warping coefficient,
kw

29 = Coordinate of load
application, za

Value

The value of the considered overwrite item.

1 = Demand/capacity ratio limit

      Value
>= 0; 0 means use program determined value.

2 = Live load reduction factor

      Value
>= 0; 0 means use a program determined value.

3 = Net area to total area ratio

      Value
>= 0; 0 means use program default value.

4 = Material buckling class

     0 = Program
default

     1 = Class
A

     2 = Class
B

5 = Unbraced length ratio, y-y

      Value
>= 0; 0 means use program determined value.

6 = Unbraced length ratio, z-z

      Value
>= 0; 0 means use program determined value.

7 = Unbraced length ratio, LTB

      Value
>= 0; 0 means use program determined value.

8 = Effective length factor, Ky

      Value
>= 0; 0 means use program determined value.

9 = Effective length factor, Kz

10 = Effective length factor, K LTB

       Value
>= 0; 0 means use program determined value.

11 = LTB Fixed End

       0
= Program default

       1
= Left

       2
= Right

12 = Bending coefficient, C1

       Value
>= 0; 0 means use program determined value.

13 = Bending coefficient, C2

       Value
>= 0; 0 means use program determined value.

14 = Bending coefficient, C3

       Value
>= 0; 0 means use program determined value.

15 = Torsional-flexural buckling curve

        0
= Program default

        1
= Curve 1

        2
= Curve 2

16 = Buckling curve for LTB

        0
= Program default

        1
= Curve 1

        2
= Curve 2

17 = Tensile capacity, Nt,Rd

       Value
>= 0; 0 means use program determined value. [F]

18 = Elastic torsional buckling force,
NcrT

       Value
>= 0; 0 means use program determined value. [F]

19 = Elastic torsional-flexural buckling
force, NcrTF

       Value
>= 0; 0 means use program determined value. [F]

20 = Compressive capacity, NRk

       Value
>= 0; 0 means use program determined value. [F]

21 = Bending capacity about y-y, MyRk

       Value
>= 0; 0 means use program determined value. [FL]

22 = Bending capacity about z-z, MzRk

       Value
>= 0; 0 means use program determined value. [FL]

23 = Elastic critical moment for lateral-torsional
buckling, Mcr

       Value
>= 0; 0 means use program determined value. [FL]

24 = Shear capacity along z-z axis, Vz.Rd

       Value
>= 0; 0 means use program determined value. [F]

25 = Shear capacity along y-y  axis,
Vy.Rd

       Value
>= 0; 0 means use program determined value. [F]

26 = Torsion capacity, TRd

       Value
>= 0; 0 means use program determined value. [FL]

27 = Shear Stress due to warping torsion
moment, *τw*

       Value
>= 0; 0 means use program determined value. [F/L2]

28 = Warping coefficient, kw
(used in Mcr calculation)

       0.5
=<Value =< 1; 0 means use program determined value which is defaulted
to 1.0.

29 = Coordinate of load application, za
(used in Mcr calculation)

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of an aluminum design
overwrite item.

The function returns zero if the item is successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignOverwriteItemEurocode\_9\_2007()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("EN
1999:2007")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'get overwrite item
      ret = SapModel.DesignAluminum.Eurocode\_9\_2007.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 23.3.0

Changed references from major and minor axes to y-y
and z-z in version 23.4.0.

## See Also

[SetOverwrite](SetOverwrite_{Aluminum_EC9_2007}.htm)



## GetPreference {Aluminum EC9 2007}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/EC_9_2007/GetPreference_{Aluminum_EC9_2007}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignAluminum.Eurocode\_9\_2007.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating
the preference item considered.

1 = Country

2 = Multi-response case
design

3 = Demand/capacity ratio
limit

4 = Combos equation

5 = Reliability class

6 = GammaM1

7 = GammaM2

8 = Consider P-Delta Done

9 = Consider Torsion

10 = Pattern live load
factor

Value

The value of the considered preference item.

1
= Country

      1
= CEN Default

      2
= United Kingdom

      3
= Slovenia

      4
= Bulgaria

      5
= Norway

      7
= Sweden

      8
= Finland

      9
= Denmark

     10
= Portugal

     11
= Germany

2 = Multi-response case
design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 =
Step-by-step -- All

3 = Demand/capacity ratio
limit

  Value >
0

4 = Combos equation

   1 = Eq.
6.10

   2 = Max
of Eqs. 6.10a and 6.10b

5 = Reliability class

   1 = Class
1

   2 = Class
2

   3 = Class
3

6 = GammaM1

Value > 0

7 = GammaM2

      Value
> 0

8 = Consider P-Delta Done

0 = No

Any other value = Yes

9 = Consider Torsion

0 = No

Any other value = Yes

10 = Pattern live load
factor

  Value >=
0

## Remarks

This function retrieves the value of an aluminum design
preference item.

The function returns zero if the item is successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignPreferenceItemEurocode\_9\_2007()
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

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("EN
1999:2007")

   'get preference item
      ret = SapModel.DesignAluminum.Eurocode\_9\_2007.GetPreference(4,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 23.3.0

## See Also

[SetPreference](SetPreference_{Aluminum_EC9_2007}.htm)



## SetOverwrite {Aluminum EC9 2007}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/EC_9_2007/SetOverwrite_{Aluminum_EC9_2007}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignAluminum.Eurocode\_9\_2007.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of a frame object with aluminum frame design
procedure.

Item

This is an integer between 1 and 29, inclusive, indicating
the overwrite item considered.

1
= Demand/capacity ratio limit

2 = Live load reduction
factor

3 = Net area to total area
ratio

4 = Material buckling class

5 = Unbraced length ratio,
y-y

6 = Unbraced length ratio,
z-z

7 = Unbraced length ratio,
LTB

8 = Effective length factor
sway, Ky

9 = Effective length factor
sway, Kz

10 = Effective length factor,
K LTB

11 = LTB fixed end

12 = Bending coefficient,
C1

13 = Bending coefficient,
C2

14 = Bending coefficient,
C3

15 = Torsional-flexural
buckling curve

16 = Buckling curve for
LTB

17 = Tensile capacity,
Nt,Rd

18 = Elastic torsional
buckling force, NcrT

19 = Elastic torsional-flexural
buckling force, NcrTF

20 = Compressive capacity,
NRk

21
= Bending capacity about y-y axis, MyRk

22 = Bending capacity about
z-z axis, MzRk

23 = Elastic critical moment
for lateral-torsional buckling, Mcr

24 = Shear capacity along
z-z axis, Vz.Rd

25 = Shear capacity along
y-y axis, Vy.Rd

26 = Torsion capacity,
TRd

27 = Shear stress due to
warping torsion moment,  *τw*

28 = Warping coefficient,
kw

29 = Coordinate of load
application, za

Value

The value of the considered overwrite item.

1 = Demand/capacity ratio limit

      Value
>= 0; 0 means use program determined value.

2 = Live load reduction factor

      Value
>= 0; 0 means use a program determined value.

3 = Net area to total area ratio

      Value
>= 0; 0 means use program default value.

4 = Material buckling class

     0 = Program
default

     1 = Class
A

     2 = Class
B

5 = Unbraced length ratio, y-y

      Value
>= 0; 0 means use program determined value.

6 = Unbraced length ratio, z-z

      Value
>= 0; 0 means use program determined value.

7 = Unbraced length ratio, LTB

      Value
>= 0; 0 means use program determined value.

8 = Effective length factor, Ky

      Value
>= 0; 0 means use program determined value.

9 = Effective length factor, Kz

      Value
>= 0; 0 means use program determined value.

10 = Effective length factor, K LTB

       Value
>= 0; 0 means use program determined value.

11 = LTB Fixed End

       0
= Program default

       1
= Left

       2
= Right

12 = Bending coefficient, C1

       Value
>= 0; 0 means use program determined value.

13 = Bending coefficient, C2

       Value
>= 0; 0 means use program determined value.

14 = Bending coefficient, C3

       Value
>= 0; 0 means use program determined value.

15 = Torsional-flexural buckling curve

        0
= Program default

        1
= Curve 1

        2
= Curve 2

16 = Buckling curve for LTB

        0
= Program default

        1
= Curve 1

        2
= Curve 2

17 = Tensile capacity, Nt,Rd

       Value
>= 0; 0 means use program determined value. [F]

18 = Elastic torsional buckling force,
NcrT

       Value
>= 0; 0 means use program determined value. [F]

19 = Elastic torsional-flexural buckling
force, NcrTF

       Value
>= 0; 0 means use program determined value. [F]

20 = Compressive capacity, NRk

       Value
>= 0; 0 means use program determined value. [F]

21 = Bending capacity about y-y, MyRk

       Value
>= 0; 0 means use program determined value. [FL]

22 = Bending capacity about z-z, MzRk

       Value
>= 0; 0 means use program determined value. [FL]

23 = Elastic critical moment for lateral-torsional
buckling, Mcr

       Value
>= 0; 0 means use program determined value. [FL]

24 = Shear capacity along z-z axis, Vz.Rd

       Value
>= 0; 0 means use program determined value. [F]

25 = Shear capacity along y-y  axis,
Vy.Rd

       Value
>= 0; 0 means use program determined value. [F]

26 = Torsion capacity, TRd

       Value
>= 0; 0 means use program determined value. [FL]

27 = Shear
stress due to warping torsion moment,  *τw*

       Value
>= 0; 0 means use program determined value. [F/L2]

28 = Warping coefficient, kw
(used in Mcr calculation)

       0.5
=<Value =< 1; 0 means use program determined value which is defaulted
to 1.0.

29 = Coordinate of load application, za
(used in Mcr calculation)

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

This function sets the value of an aluminum design overwrite
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignOverwriteItemEurocode\_9\_2007()
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

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("EN
1999:2007")

   'set overwrite item
      ret = SapModel.DesignAluminum.Eurocode\_9\_2007.SetOverwrite("8",
1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 23.3.0

Changed references from major and minor axes to y-y
and z-z in version 23.4.0.

## See Also

[GetOverwrite](GetOverwrite_{Aluminum_EC9_2007}.htm)



## SetPreference {Aluminum EC9 2007}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/EC_9_2007/SetPreference_{Aluminum_EC9_2007}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignAluminum.Eurocode\_9\_2007.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating
the preference item considered.

1
= Country

2 = Multi-response case
design

3 = Demand/capacity ratio
limit

4 = Combos equation

5 = Reliability class

6 = GammaM1

7 = GammaM2

8 = Consider P-Delta Done

9 = Consider Torsion

10 = Pattern live load
factor

Value

The value of the considered preference item.

1 = Country

      1
= CEN Default

      2
= United Kingdom

      3
= Slovenia

      4
= Bulgaria

      5
= Norway

      7
= Sweden

      8
= Finland

      9
= Denmark

     10
= Portugal

     11
= Germany

2 = Multi-response case
design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 =
Step-by-step -- All

3 = Demand/capacity ratio
limit

  Value >
0

4 = Combos equation

   1 = Eq.
6.10

   2 = Max
of Eqs. 6.10a and 6.10b

5 = Reliability class

   1 = Class
1

   2 = Class
2

   3 = Class
3

6 = GammaM1

Value > 0

7 = GammaM2

      Value
> 0

8 = Consider P-Delta Done

0 = No

Any other value = Yes

9 = Consider Torsion

0 = No

Any other value = Yes

10 = Pattern live load
factor

  Value >=
0

## Remarks

This function sets the value of an aluminum design preference
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignPreferenceItemEurocode\_9\_2007()
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

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("EN
1999:2007")

   'set preference item
      ret = SapModel.DesignAluminum.Eurocode\_9\_2007.SetPreference(4,
2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 23.3.0

## See Also

[GetPreference](GetPreference_{Aluminum_EC9_2007}.htm)



## GetCode {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/GetCode_{Aluminum}.htm`*

# GetCode

## Syntax

SapObject.SapModel.DesignAluminum.GetCode

## VB6 Procedure

Function GetCode(ByRef CodeName As String) As Long

## Parameters

CodeName

This is one of the following aluminum design code names.

AA-ASD 2000

AA-LRFD 2000

## Remarks

This function retrieves the aluminum design code.

The function returns zero if the code is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignCode()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim CodeName As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'get aluminum design code
      ret = SapModel.DesignAluminum.GetCode(CodeName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetCode](SetCode_{Aluminum}.htm)



## GetComboAutoGenerate {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/GetComboAutoGenerateAluminum.htm`*

# GetComboAutoGenerate

## Syntax

SapObject.SapModel.DesignAluminum.GetComboAutoGenerate

## VB6 Procedure

Function SetComboAutoGenerate(ByRef AutoGenerate As Boolean) As Long

## Parameters

AutoGenerate

If this item is True, the option to automatically generate code-based design load combinations for aluminum frame design is turned on. If it is False, the option is turned off.

## Remarks

This function retrieves the value of the automatically generated code-based design load combinations option for aluminum frame design.

The function returns zero if the options are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignComboAutoGenerate()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim AutoGenerate As Boolean

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

   'set option to not auto generate code-based design load combinations
      ret = SapModel.DesignAluminum.GetComboAutoGenerate(AutoGenerate)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 18.1.0.

## See Also

[SetComboAutoGenerate](SetComboAutoGenerate_{Aluminum}.htm)



## GetComboDeflection {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/GetComboDeflection_{Aluminum}.htm`*

# GetComboDeflection

## Syntax

SapObject.SapModel.DesignAluminum.GetComboDeflection

## VB6 Procedure

Function GetComboDeflection(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of load combinations selected as design combinations for aluminum deflection design.

MyName

This is an array that includes the name of each response combination selected as a design combination for aluminum deflection design.

## Remarks

This function retrieves the names of all load combinations selected as design combinations for aluminum deflection design.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignComboDeflection()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim i As Long
      Dim NumberNames As Long
      Dim MyName2() As String
      Dim Selected As Boolean
      Dim NumberItems As Long
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default aluminum design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(False, False, True, False)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName2)

   'select combos for aluminum deflection design
      For i = 0 To NumberNames - 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignAluminum.SetComboDeflection(MyName2(i), Selected)
      Next i

   'get combos selected for aluminum deflection design
      ret = SapModel.DesignAluminum.GetComboDeflection(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetComboDeflection](SetComboDeflection_{Aluminum}.htm)



## GetComboStrength {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/GetComboStrength_{Aluminum}.htm`*

# GetComboStrength

## Syntax

SapObject.SapModel.DesignAluminum.GetComboStrength

## VB6 Procedure

Function GetComboStrength(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of load combinations selected as design combinations for aluminum strength design.

MyName

This is an array that includes the name of each response combination selected as a design combination for aluminum strength design.

## Remarks

This function retrieves the names of all load combinations selected as design combinations for aluminum strength design.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignComboStrength()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim i As Long
      Dim NumberNames As Long
      Dim MyName2() As String
      Dim Selected As Boolean
      Dim NumberItems As Long
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default aluminum design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(False, False, True, False)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName2)

   'select combos for aluminum strength design
      For i = 0 To NumberNames - 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignAluminum.SetComboStrength(MyName2(i), Selected)
      Next i

   'get combos selected for aluminum strength design
      ret = SapModel.DesignAluminum.GetComboStrength(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetComboStrength](SetComboStrength_{Aluminum}.htm)



## GetDesignSection {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/GetDesignSection_{Aluminum}.htm`*

# GetDesignSection

## Syntax

SapObject.SapModel.DesignAluminum.GetDesignSection

## VB6 Procedure

Function GetDesignSection(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a frame object with a aluminum frame design procedure.

PropName

The name of the design section for the specified frame object.

## Remarks

This function retrieves the design section for a specified aluminum frame object.

The function returns zero if the section is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignSection()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'get design section
      ret = SapModel.DesignAluminum.GetDesignSection("8", PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetDesignSection](SetDesignSection_{Aluminum}.htm)



## GetGroup {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/GetGroup_{Aluminum}.htm`*

# GetGroup

## Syntax

SapObject.SapModel.DesignAluminum.GetGroup

## VB6 Procedure

Function GetGroup(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of groups selected for aluminum design.

MyName

This is an array that includes the name of each group selected for aluminum design.

## Remarks

This function retrieves the names of all groups selected for aluminum design.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignGroup()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberItems As Long
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'select group for aluminum design
      ret = SapModel.DesignAluminum.SetGroup("ALL", True)

   'get groups selected for aluminum design
      ret = SapModel.DesignAluminum.GetGroup(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetGroup](SetGroup_{Aluminum}.htm)



## GetResultsAvailable {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/GetResultsAvailable_{Aluminum}.htm`*

# GetResultsAvailable {Aluminum}

## Syntax

SapObject.SapModel.DesignAluminum.GetResultsAvailable

## VB6 Procedure

Function GetResultsAvailable() As Boolean

## Parameters

None

## Remarks

The function returns True if the aluminum frame design results are available, otherwise False.

## VBA Example

Sub GetResultsAvailable()

  'dimension variables

    Dim SapObject as cOAPI

    Dim SapModel As cSapModel

    Dim ret As Long

    Dim ResultsAvailable As Boolean

  'create Sap2000 object

    Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

  'start Sap2000 application

    SapObject.ApplicationStart

  'create SapModel object

    Set SapModel = SapObject.SapModel

  'initialize model

    ret = SapModel.InitializeNewModel

  'add aluminum formed material

    ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

  'create new aluminum frame section property

    ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5 )

  'create model from template

    ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

  'run analysis

    ret = SapModel.File.Save("C:\SapAPI\x.sdb")

    ret = SapModel.Analyze.RunAnalysis

  'start aluminum design

    ret = SapModel.DesignAluminum.StartDesign

  'check if design results are available

    ResultsAvailable = SapModel.DesignAluminum.GetResultsAvailable

  'close Sap2000

    SapObject.ApplicationExit.False

    Set SapModel = Nothing

    Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 18.2.0.



## GetSummaryResults {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/GetSummaryResults_{Aluminum}.htm`*

# GetSummaryResults

## Syntax

SapObject.SapModel.DesignAluminum.GetSummaryResults

## VB6 Procedure

Function GetSummaryResults(ByVal Name As String, ByRef NumberItems As Long, ByRef FrameName() As String, ByRef Ratio() As Double, ByRef RatioType() As Long, ByRef Location() As Double, ByRef ComboName() As String, ByRef ErrorSummary() As String, ByRef WarningSummary() As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

NumberItems

The number of frame objects for which results are obtained.

FrameName

This is an array that includes each frame object name for which results are obtained.

Ratio

This is an array that includes the controlling stress or capacity ratio for each frame object.

RatioType

This is an array that includes 1, 3 or 4, indicating the controlling stress or capacity ratio type for each frame object.

1 = PMM

3 = Major shear

4 = Minor shear

Location

This is an array that includes the distance from the I-end of the frame object to the location where the controlling stress or capacity ratio occurs. [L]

ComboName

This is an array that includes the name of the design combination for which the controlling stress or capacity ratio occurs.

ErrorSummary

This is an array that includes the design error messages for the frame object, if any.

WarningSummary

This is an array that includes the design warning messages for the frame object, if any.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the design results are retrieved for the frame object specified by the Name item.

If this item is Group, the design results are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the design results are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves summary results for aluminum design.

The function returns zero if the results are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignSummaryResults()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberItems As Long
      Dim FrameName() As String
      Dim Ratio() As Double
      Dim RatioType() As Long
      Dim Location() As Double
      Dim ComboName() As String
      Dim ErrorSummary() As String
      Dim WarningSummary() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'get summary result data
      ret = SapModel.DesignAluminum.GetSummaryResults("8", NumberItems, FrameName, Ratio, RatioType, Location, ComboName, ErrorSummary, WarningSummary)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## ResetOverwrites {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/ResetOverwrites_{Aluminum}.htm`*

# ResetOverwrites

## Syntax

SapObject.SapModel.DesignAluminum.ResetOverwrites

## VB6 Procedure

Function ResetOverwrites() As Long

## Parameters

None

## Remarks

This function resets all aluminum frame design overwrites to default values.

The function returns zero if the overwrites are successfully reset; otherwise it returns a nonzero value.

The function will fail if no aluminum frame objects are present.

## VBA Example

Sub ResetAluminumDesignOverwrites()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'reset aluminum design overwrites
      ret = SapModel.DesignAluminum.ResetOverwrites

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## SetAutoSelectNull {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/SetAutoSelectNull_{Aluminum}.htm`*

# SetAutoSelectNull

## Syntax

SapObject.SapModel.DesignAluminum.SetAutoSelectNull

## VB6 Procedure

Function SetAutoSelectNull(ByVal Name As String, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function removes the auto select section assignments from all specified frame objects that have a aluminum frame design procedure.

The function returns zero if the auto select section assignments are successfully removed; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumAutoSelectSectionsNull()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section properties
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)
      ret = SapModel.PropFrame.SetISection("AI2", Name , 18, 6, 0.6, 0.3, 6, 0.6)
      ret = SapModel.PropFrame.SetISection("AI3", Name , 18, 6, 0.7, 0.3, 6, 0.7)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'define new auto select list frame section property
      ReDim MyName(2)
      MyName(0) = "AI"
      MyName(1) = "AI2"
      MyName(2) = "AI3"
      ret = SapModel.PropFrame.SetAutoSelectAluminum("AUTO1", 3, MyName)

   'set frame section properties
      ret = SapModel.FrameObj.SetSection("8", "AUTO1")
      ret = SapModel.FrameObj.SetSection("10", "AUTO1")

   'set frame object selected
      ret = SapModel.FrameObj.SetSelected("8", True)

   'set auto select section null
      ret = SapModel.DesignAluminum.SetAutoSelectNull("",SelectedObjects)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## SetCode {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/SetCode_{Aluminum}.htm`*

# SetCode

## Syntax

SapObject.SapModel.DesignAluminum.SetCode

## VB6 Procedure

Function SetCode(ByVal CodeName As String) As Long

## Parameters

CodeName

This is one of the following aluminum design code names.

AA-ASD 2000

AA-LRFD 2000

## Remarks

This function sets the aluminum design code.

The function returns zero if the code is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignCode()
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

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA-LRFD 2000")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetCode](GetCode_{Aluminum}.htm)



## SetComboAutoGenerate {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/SetComboAutoGenerate_{Aluminum}.htm`*

# SetComboAutoGenerate

## Syntax

SapObject.SapModel.DesignAluminum.SetComboAutoGenerate

## VB6 Procedure

Function SetComboAutoGenerate(ByVal AutoGenerate As Boolean) As Long

## Parameters

AutoGenerate

If this item is True, the option to automatically generate code-based design load combinations for aluminum frame design is turned on. If it is False, the option is turned off.

## Remarks

This function turns on or off the option to automatically generate code-based design load combinations for aluminum frame design.

The function returns zero if the options are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignComboAutoGenerate()
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

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'set option to not auto generate code-based design load combinations
      ret = SapModel.DesignAluminum.SetComboAutoGenerate(False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 18.1.0.

## See Also

[GetComboAutoGenerate](GetComboAutoGenerateAluminum.htm)



## SetComboDeflection {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/SetComboDeflection_{Aluminum}.htm`*

# SetComboDeflection

## Syntax

SapObject.SapModel.DesignAluminum.SetComboDeflection

## VB6 Procedure

Function SetComboDeflection(ByVal Name As String, ByVal Selected As Boolean) As Long

## Parameters

Name

The name of an existing load combination.

Selected

If this item is True, the specified load combination is selected as a design combination for aluminum deflection design. If it is False, the combination is not selected for aluminum deflection design.

## Remarks

This function selects or deselects a load combination for aluminum deflection design.

The function returns zero if the selection status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignComboDeflection()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim i As Long
      Dim NumberNames As Long
      Dim MyName() As String
      Dim Selected As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default aluminum design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(False, False, True, False)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName)

   'select combos for aluminum deflection design
      For i = 0 To NumberNames - 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignAluminum.SetComboDeflection(MyName(i), Selected)
      Next i

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetComboDeflection](GetComboDeflection_{Aluminum}.htm)



## SetComboStrength {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/SetComboStrength_{Aluminum}.htm`*

# SetComboStrength

## Syntax

SapObject.SapModel.DesignAluminum.SetComboStrength

## VB6 Procedure

Function SetComboStrength(ByVal Name As String, ByVal Selected As Boolean) As Long

## Parameters

Name

The name of an existing load combination.

Selected

If this item is True, the specified load combination is selected as a design combination for aluminum strength design. If it is False, the combination is not selected for aluminum strength design.

## Remarks

This function selects or deselects a load combination for aluminum strength design.

The function returns zero if the selection status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignComboStrength()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim i As Long
      Dim NumberNames As Long
      Dim MyName() As String
      Dim Selected As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default aluminum design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(False, False, True, False)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName)

   'select combos for aluminum strength design
      For i = 0 To NumberNames - 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignAluminum.SetComboStrength(MyName(i), Selected)
      Next i

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetComboStrength](GetComboStrength_{Aluminum}.htm)



## SetDesignSection {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/SetDesignSection_{Aluminum}.htm`*

# SetDesignSection

## Syntax

SapObject.SapModel.DesignAluminum.SetDesignSection

## VB6 Procedure

Function SetDesignSection(ByVal Name As String, ByVal PropName As String, ByVal LastAnalysis As Boolean, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

PropName

The name of an existing frame section property to be used as the design section for the specified frame objects. This item applies only when LastAnalysis = False.

LastAnalysis

If this item is True, the design section for the specified frame objects is reset to the last analysis section for the frame object. If it is False, the design section is set to that specified by PropName.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function modifies the design section for all specified frame objects that have a aluminum frame design procedure.

The function returns zero if the design section is successfully modified; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignSection()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section properties
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)
      ret = SapModel.PropFrame.SetISection("AI2", Name , 18, 6, 0.6, 0.3, 6, 0.6)
      ret = SapModel.PropFrame.SetISection("AI3", Name , 18, 6, 0.7, 0.3, 6, 0.7)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'define new auto select list frame section property
      ReDim MyName(2)
      MyName(0) = "AI"
      MyName(1) = "AI2"
      MyName(2) = "AI3"
      ret = SapModel.PropFrame.SetAutoSelectAluminum("AUTO1", 3, MyName)

   'set frame section properties
      ret = SapModel.FrameObj.SetSection("8", "AUTO1")
      ret = SapModel.FrameObj.SetSection("10", "AUTO1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'set design section
      ret = SapModel.DesignAluminum.SetDesignSection("8", "AI3", False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetDesignSection](GetDesignSection_{Aluminum}.htm)



## SetGroup {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/SetGroup_{Aluminum}.htm`*

# SetGroup

## Syntax

SapObject.SapModel.DesignAluminum.SetGroup

## VB6 Procedure

Function SetGroup(ByVal Name As String, ByVal Selected As Boolean) As Long

## Parameters

Name

The name of an existing group.

Selected

If this item is True, the specified group is selected as a design group for aluminum design. If it is False, the group is not selected for aluminum design.

## Remarks

This function selects or deselects a group for aluminum design.

The function returns zero if the selection status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignGroup()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'select group for aluminum design
      ret = SapModel.DesignAluminum.SetGroup("ALL", True)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetGroup](GetGroup_{Aluminum}.htm)



## StartDesign {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/StartDesign_{Aluminum}.htm`*

# StartDesign

## Syntax

SapObject.SapModel.DesignAluminum.StartDesign

## VB6 Procedure

Function StartDesign() As Long

## Parameters

None

## Remarks

This function starts the aluminum frame design.

The function returns zero if the aluminum frame design is successfully started; otherwise it returns a nonzero value.

The function will fail if no aluminum frame objects are present. It will also fail if analysis results are not available.

## VBA Example

Sub StartAluminumDesign()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## VerifyPassed {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/VerifyPassed_{Aluminum}.htm`*

# VerifyPassed

## Syntax

SapObject.SapModel.DesignAluminum.VerifyPassed

## VB6 Procedure

Function VerifyPassed(ByRef NumberItems As Long, ByRef n1 As Long, ByRef n2 As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of aluminum frame objects that did not pass the design check or have not yet been checked.

n1

The number of aluminum frame objects that did not pass the design check.

n2

The number of aluminum frame objects that have not yet been checked.

MyName

This is an array that includes the name of each frame object that did not pass the design check or has not yet been checked.

## Remarks

This function retrieves the names of the frame objects that did not pass the design check or have not yet been checked, if any.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub VerifyAluminumDesignPassed()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberItems As Long
      Dim n1 As Long
      Dim n2 As Long
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'verify frame objects successfully designed
      ret = SapModel.DesignAluminum.VerifyPassed(NumberItems, n1, n2, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## VerifySections {Aluminum}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/VerifySections_{Aluminum}.htm`*

# VerifySections

## Syntax

SapObject.SapModel.DesignAluminum.VerifySections

## VB6 Procedure

Function VerifySections(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of frame objects that have different analysis and design sections.

MyName

This is an array that includes the name of each frame object that has different analysis and design sections.

## Remarks

This function retrieves the names of the frame objects that have different analysis and design sections, if any.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub VerifyAluminumDesignSections()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim NumberItems As Long
      Dim MyName() As String

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'verify analysis versus design section
      ret = SapModel.DesignAluminum.VerifySections(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## GetOverwrite {Aluminum AA ASD 2000}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/aa_asd_2000/GetOverwrite_{Aluminum_AA_ASD_2000}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignAluminum.AA\_ASD\_2000.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a aluminum frame design procedure.

Item

This is an integer between 1 and 23, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Bending coefficient, Cb

10 = Buckling constant for compression, k1

11 = Buckling constant for compression, k2

12 = Buckling constant for bending, k1

13 = Buckling constant for bending, k2

14 = Safety coefficient, kt

15 = Bending coefficient, C1

16 = Bending coefficient, C2

17 = Yield stress, Fy

18 = Compressive stress, Fa

19 = Tensile stress, Ft

20 = Major bending stress, Fb3

21 = Minor bending stress, Fb2

22 = Major shear stress, Fs2

23 = Minor shear stress, Fs3

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Live load reduction factor

Value >= 0; 0 means use a program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

10 = Buckling constant for compression, k1

Value >= 0; 0 means use program determined value.

11 = Buckling constant for compression, k2

Value >= 0; 0 means use program determined value.

12 = Buckling constant for bending, k1

Value >= 0; 0 means use program determined value.

13 = Buckling constant for bending, k2

Value >= 0; 0 means use program determined value.

14 = Safety coefficient, kt

Value >= 0; 0 means use program determined value.

15 = Bending coefficient, C1

Value >= 0; 0 means use program determined value.

16 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

17 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

18 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

19 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

20 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

21 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

22 = Major shear stress, Fs2

Value >= 0; 0 means use program determined value. [F/L2]

23 = Minor shear stress, Fs3

Value >= 0; 0 means use program determined value. [F/L2]

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of an aluminum design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignOverwriteItemAA\_ASD\_2000()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA-ASD 2000")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'get overwrite item
      ret = SapModel.DesignAluminum.AA\_ASD\_2000.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Aluminum_AA_ASD_2000}.htm)



## GetPreference {Aluminum AA ASD 2000}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/aa_asd_2000/GetPreference_{Aluminum_AA_ASD_2000}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignAluminum.AA\_ASD\_2000.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 6, inclusive, indicating the preference item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Lateral factor

4 = Use lateral factor

5 = Bridge type structure

6 = Time history design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Demand/capacity ratio limit

Value > 0

3 = Lateral factor

Value > 0

4 = Use lateral factor

0 = No

Any other value = Yes

5 = Bridge type structure

0 = No

Any other value = Yes

6 = Time history design

1 = Envelopes

2 = Step-by step

## Remarks

This function retrieves the value of an aluminum design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignPreferenceItemAA\_ASD\_2000()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA-ASD 2000")

   'get preference item
      ret = SapModel.DesignAluminum.AA\_ASD\_2000.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetPreference](SetPreference_{Aluminum_AA_ASD_2000}.htm)



## SetOverwrite {Aluminum AA ASD 2000}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/aa_asd_2000/SetOverwrite_{Aluminum_AA_ASD_2000}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignAluminum.AA\_ASD\_2000.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 23, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Bending coefficient, Cb

10 = Buckling constant for compression, k1

11 = Buckling constant for compression, k2

12 = Buckling constant for bending, k1

13 = Buckling constant for bending, k2

14 = Safety coefficient, kt

15 = Bending coefficient, C1

16 = Bending coefficient, C2

17 = Yield stress, Fy

18 = Compressive stress, Fa

19 = Tensile stress, Ft

20 = Major bending stress, Fb3

21 = Minor bending stress, Fb2

22 = Major shear stress, Fs2

23 = Minor shear stress, Fs3

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Live load reduction factor

Value >= 0; 0 means use a program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

10 = Buckling constant for compression, k1

Value >= 0; 0 means use program determined value.

11 = Buckling constant for compression, k2

Value >= 0; 0 means use program determined value.

12 = Buckling constant for bending, k1

Value >= 0; 0 means use program determined value.

13 = Buckling constant for bending, k2

Value >= 0; 0 means use program determined value.

14 = Safety coefficient, kt

Value >= 0; 0 means use program determined value.

15 = Bending coefficient, C1

Value >= 0; 0 means use program determined value.

16 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

17 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

18 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

19 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

20 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

21 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

22 = Major shear stress, Fs2

Value >= 0; 0 means use program determined value. [F/L2]

23 = Minor shear stress, Fs3

Value >= 0; 0 means use program determined value. [F/L2]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of an aluminum design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignOverwriteItemAA\_ASD\_2000()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA-ASD 2000")

   'set overwrite item
      ret = SapModel.DesignAluminum.AA\_ASD\_2000.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Aluminum_AA_ASD_2000}.htm)



## SetPreference {Aluminum AA ASD 2000}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/aa_asd_2000/SetPreference_{Aluminum_AA_ASD_2000}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignAluminum.AA\_ASD\_2000.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 6, inclusive, indicating the preference item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Lateral factor

4 = Use lateral factor

5 = Bridge type structure

6 = Time history design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Demand/capacity ratio limit

Value > 0

3 = Lateral factor

Value > 0

4 = Use lateral factor

0 = No

Any other value = Yes

5 = Bridge type structure

0 = No

Any other value = Yes

6 = Time history design

1 = Envelopes

2 = Step-by step

## Remarks

This function sets the value of an aluminum design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignPreferenceItemAA\_ASD\_2000()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA-ASD 2000")

   'set preference item
      ret = SapModel.DesignAluminum.AA\_ASD\_2000.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetPreference](GetPreference_{Aluminum_AA_ASD_2000}.htm)



## GetOverwrite {Aluminum AA LRFD 2000}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/aa_lrfd_2000/GetOverwrite_{Aluminum_AA_LRFD_2000}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignAluminum.AA\_LRFD\_2000.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a aluminum frame design procedure.

Item

This is an integer between 1 and 23, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Bending coefficient, Cb

10 = Buckling constant for compression, k1

11 = Buckling constant for compression, k2

12 = Buckling constant for bending, k1

13 = Buckling constant for bending, k2

14 = Safety coefficient, kt

15 = Bending coefficient, C1

16 = Bending coefficient, C2

17 = Yield stress, Fy

18 = Compressive stress, Fa

19 = Tensile stress, Ft

20 = Major bending stress, Fb3

21 = Minor bending stress, Fb2

22 = Major shear stress, Fs2

23 = Minor shear stress, Fs3

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Live load reduction factor

Value >= 0; 0 means use a program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

10 = Buckling constant for compression, k1

Value >= 0; 0 means use program determined value.

11 = Buckling constant for compression, k2

Value >= 0; 0 means use program determined value.

12 = Buckling constant for bending, k1

Value >= 0; 0 means use program determined value.

13 = Buckling constant for bending, k2

Value >= 0; 0 means use program determined value.

14 = Safety coefficient, kt

Value >= 0; 0 means use program determined value.

15 = Bending coefficient, C1

Value >= 0; 0 means use program determined value.

16 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

17 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

18 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

19 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

20 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

21 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

22 = Major shear stress, Fs2

Value >= 0; 0 means use program determined value. [F/L2]

23 = Minor shear stress, Fs3

Value >= 0; 0 means use program determined value. [F/L2]

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of an aluminum design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignOverwriteItemAA\_LRFD\_2000()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA-LRFD 2000")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start aluminum design
      ret = SapModel.DesignAluminum.StartDesign

   'get overwrite item
      ret = SapModel.DesignAluminum.AA\_LRFD\_2000.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Aluminum_AA_LRFD_2000}.htm)



## GetPreference {Aluminum AA LRFD 2000}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/aa_lrfd_2000/GetPreference_{Aluminum_AA_LRFD_2000}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignAluminum.AA\_LRFD\_2000.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 6, inclusive, indicating the preference item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Phiy resistance factor

4 = Phib resistance factor

5 = Phic resistance factor

6 = Phiu resistance factor

7 = Phicc resistance factor

8 = Phicp resistance factor

9 = Phiv resistance factor

10 = Phivp resistance factor

11 = Phiw resistance factor

12 = Time history design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Demand/capacity ratio limit

Value > 0

3 = Phiy resistance factor

Value > 0

4 = Phib resistance factor

Value > 0

5 = Phic resistance factor

Value > 0

6 = Phiu resistance factor

Value > 0

7 = Phicc resistance factor

Value > 0

8 = Phicp resistance factor

Value > 0

9 = Phiv resistance factor

Value > 0

10 = Phivp resistance factor

Value > 0

11 = Phiw resistance factor

Value > 0

12 = Time history design

1 = Envelopes

2 = Step-by step

## Remarks

This function retrieves the value of an aluminum design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetAluminumDesignPreferenceItemAA\_LRFD\_2000()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Name As String
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA-LRFD 2000")

   'get preference item
      ret = SapModel.DesignAluminum.AA\_LRFD\_2000.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetPreference](SetPreference_{Aluminum_AA_LRFD_2000}.htm)



## SetOverwrite {Aluminum AA LRFD 2000}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/aa_lrfd_2000/SetOverwrite_{Aluminum_AA_LRFD_2000}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignAluminum.AA\_LRFD\_2000.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 23, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Bending coefficient, Cb

10 = Buckling constant for compression, k1

11 = Buckling constant for compression, k2

12 = Buckling constant for bending, k1

13 = Buckling constant for bending, k2

14 = Safety coefficient, kt

15 = Bending coefficient, C1

16 = Bending coefficient, C2

17 = Yield stress, Fy

18 = Compressive stress, Fa

19 = Tensile stress, Ft

20 = Major bending stress, Fb3

21 = Minor bending stress, Fb2

22 = Major shear stress, Fs2

23 = Minor shear stress, Fs3

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Live load reduction factor

Value >= 0; 0 means use a program determined value.

3 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

5 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

6 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

7 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

8 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

9 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

10 = Buckling constant for compression, k1

Value >= 0; 0 means use program determined value.

11 = Buckling constant for compression, k2

Value >= 0; 0 means use program determined value.

12 = Buckling constant for bending, k1

Value >= 0; 0 means use program determined value.

13 = Buckling constant for bending, k2

Value >= 0; 0 means use program determined value.

14 = Safety coefficient, kt

Value >= 0; 0 means use program determined value.

15 = Bending coefficient, C1

Value >= 0; 0 means use program determined value.

16 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

17 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

18 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

19 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

20 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

21 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

22 = Major shear stress, Fs2

Value >= 0; 0 means use program determined value. [F/L2]

23 = Minor shear stress, Fs3

Value >= 0; 0 means use program determined value. [F/L2]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of an aluminum design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignOverwriteItemAA\_LRFD\_2000()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA-LRFD 2000")

   'set overwrite item
      ret = SapModel.DesignAluminum.AA\_LRFD\_2000.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](SetOverwrite_{Aluminum_AA_LRFD_2000}.htm)



## SetPreference {Aluminum AA LRFD 2000}

*Source file: `SAP2000_API_Fuctions/Design/Aluminum/aa_lrfd_2000/SetPreference_{Aluminum_AA_LRFD_2000}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignAluminum.AA\_LRFD\_2000.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 6, inclusive, indicating the preference item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Phiy resistance factor

4 = Phib resistance factor

5 = Phic resistance factor

6 = Phiu resistance factor

7 = Phicc resistance factor

8 = Phicp resistance factor

9 = Phiv resistance factor

10 = Phivp resistance factor

11 = Phiw resistance factor

12 = Time history design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Demand/capacity ratio limit

Value > 0

3 = Phiy resistance factor

Value > 0

4 = Phib resistance factor

Value > 0

5 = Phic resistance factor

Value > 0

6 = Phiu resistance factor

Value > 0

7 = Phicc resistance factor

Value > 0

8 = Phicp resistance factor

Value > 0

9 = Phiv resistance factor

Value > 0

10 = Phivp resistance factor

Value > 0

11 = Phiw resistance factor

Value > 0

12 = Time history design

1 = Envelopes

2 = Step-by step

## Remarks

This function sets the value of an aluminum design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetAluminumDesignPreferenceItemAA\_LRFD\_2000()
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

   'add aluminum material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_ALUMINUM, , , MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6)

   'create new aluminum frame section property
      ret = SapModel.PropFrame.SetISection("AI", Name , 18, 6, 0.5, 0.3, 6, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288, True, "AI", "AI")

   'set aluminum design code
      ret = SapModel.DesignAluminum.SetCode("AA-LRFD 2000")

   'set preference item
      ret = SapModel.DesignAluminum.AA\_LRFD\_2000.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetPreference](GetPreference_{Aluminum_AA_LRFD_2000}.htm)

