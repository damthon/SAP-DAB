# API Design Cold Formed

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Design/Cold_Formed

---



## GetOverwrite

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetOverwrite.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_16.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a cold formed frame
design procedure.

Item

This is an integer between 1 and 33, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Live load reduction factor

4 = Unbraced length ratio, Major

5 = Unbraced length ratio, Minor

6 = Unbraced length ratio, Lateral Torsional
Buckling

7 = Unbraced length ratio, Distortional
Buckling

8 = Effective length factor, K Major

9 = Effective length factor, K Minor

10 = Effective length factor, K Lateral
Torsional Buckling

11 = Effective length factor, K Distortional
Buckling

12 = Rotational stiffness, kPhi (Distortional
Buckling)

13 = Moment coefficient, Cm Major

14 = Moment coefficient, Cm Minor

15 = Moment coefficient, Ctf Major

16 = Moment coefficient, Ctf Minor

17 = Bending coefficient, Cb Major

18 = Bending coefficient, Cb Minor

19 = Moment factor, Alpha Major

20 = Moment factor, Alpha Minor

21 = Nonsway moment factor, B1 Major

22 = Nonsway moment factor, B1 Minor

23 = Sway moment factor, B2 Major

24 = Sway moment factor, B2 Minor

25 = Through fastened to deck

26 = Fastener eccentricity, a/b

27 = Hole diameter on web

28 = Hole length on web

29 = Hole spacing on web

30 = Asymmetric integral ratio, Major

31 = Asymmetric integral ratio, Minor

32 = Nominal bending capacity for lateral
torsional buckling, Mn33

33 = Nominal bending capacity for lateral
torsional buckling, Mn22

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program
Default

1 = Moment
Frame

2 = Braced
Frame

2 = Demand/capacity ratio limit

Value >=
0; 0 means use program determined value

3 = Live load reduction factor

Value >=
0; 0 means use a program determined value.

4 = Unbraced length ratio, Major

Value >=
0; 0 means use program determined value.

5 = Unbraced length ratio, Minor

Value >=
0; 0 means use program determined value.

6 = Unbraced length ratio, Lateral Torsional
Buckling

Value >=
0; 0 means use program determined value.

7 = Unbraced length ratio, Distortional
Buckling

Value >=
0; 0 means use program determined value.

8 = Effective length factor, K Major

Value >=
0; 0 means use program determined value.

9 = Effective length factor, K Minor

Value >=
0; 0 means use program determined value.

10 = Effective length factor, K Lateral
Torsional Buckling

Value >=
0; 0 means use program determined value.

11 = Effective length factor, K Distortional
Buckling

Value >=
0; 0 means use program determined value.

12 = Rotational stiffness, kPhi (Distortional
Buckling)

Value >=
0; 0 means use program determined value. [F]

13 = Moment coefficient, Cm Major

Value >=
0; 0 means use program determined value.

14 = Moment coefficient, Cm Minor

Value >=
0; 0 means use program determined value.

15 = Moment coefficient, Ctf Major

Value >=
0; 0 means use program determined value.

16 = Moment coefficient, Ctf Minor

Value >=
0; 0 means use program determined value.

17 = Bending coefficient, Cb Major

Value >=
0; 0 means use program determined value.

18 = Bending coefficient, Cb Minor

Value >=
0; 0 means use program determined value.

19 = Moment factor, Alpha Major

Value >=
0; 0 means use program determined value.

20 = Moment factor, Alpha Minor

Value >=
0; 0 means use program determined value.

21 = Nonsway moment factor, B1 Major

Value >=
0; 0 means use program determined value.

22 = Nonsway moment factor, B1 Minor

Value >=
0; 0 means use program determined value.

23 = Sway moment factor, B2 Major

Value >=
0; 0 means use program determined value.

24 = Sway moment factor, B2 Minor

Value >=
0; 0 means use program determined value.

25 = Through fastened to deck

0 = No.

Any other
value = Yes.

26 = Fastener eccentricity, a/b

Value >=
0; 0 means use program determined value. [L]

27 = Hole diameter on web

Value >=
0; 0 means use program determined value. [L]

28 = Hole length on web

Value >=
hole diameter on web; 0 means use program determined value. [L]

29 = Hole spacing on web

Value >=
hole length on web; 0 means use program determined value. [L]

30 = Asymmetric integral ratio, Major

Value >=
0; 0 means use program determined value.

31 = Asymmetric integral ratio, Minor

Value >=
0; 0 means use program determined value.

32 = Nominal bending capacity for lateral
torsional buckling, Mn33

Value >=
0; 0 means use program determined value. [FL]

33 = Nominal bending capacity for lateral
torsional buckling, Mn22

Value >=
0; 0 means use program determined value. [FL]

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a cold formed design
overwrite item.

The function returns zero if the item is successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignOverwriteItemAISI\_16()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name,
MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC",
Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 72, 2, 144, True, "CdC", "CdC")

   'set cold formed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-16")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start cold formed design
      ret = SapModel.DesignColdFormed.StartDesign

   'get overwrite item
      ret = SapModel.DesignColdFormed.AISI\_16.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.2.0.

## See Also

[SetOverwrite](SetOverwrite.htm)



## GetPreference

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_16.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Second order method

4 = Design provision

5 = Lateral factor

6 = Use lateral factor

7 = PhiTy resistance or OmegaTy safety factor

8 = PhiTr resistance or OmegaTr safety factor

9 = PhiC resistance or OmegaC safety factor

10 = PhiB resistance or OmegaB safety factor

11 = PhiBPipe resistance or OmegaBPipe safety factor

12 = PhiV resistance or OmegaV safety factor

13 = Time history design

14 = Pattern live load factor

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Demand/capacity ratio limit

Value > 0

3 = Second Order Method

1 = General 2nd Order

2 = Amplified 1st Order

4 = Design Provision

1 = LRFD

2 = ASD

3 = LSD

5 = Lateral Factor

Value > 0

6 = Use Lateral Factor

1 = No

2 = Yes

7 = PhiTy resistance or OmegaTy safety factor

PhiTy:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image001.png)

OmegaTy:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image003.png)

8 = PhiTr resistance or OmegaTr safety factor

PhiTr:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image001.png)

OmegaTr:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image003.png)

9 = PhiC resistance or OmegaC safety factor

PhiC:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image001.png)

OmegaC:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image003.png)

10 = PhiB resistance or OmegaB safety factor

PhiB:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image001.png)

OmegaB:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image003.png)

11 = PhiBPipe resistance or OmegaBPipe safety factor

PhiBr:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image001.png)

OmegaBr:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image003.png)

12 = PhiV or OmegaV safety factor

PhiV:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image001.png)

OmegaV:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/GetPreference_files/image003.png)

13 = Time history design

1 = Envelopes

2 = Step-by step

14 = Pattern live load factor

Value > 0

If Design Provision is 1 (LRFD) or 3 (LSD), the value of items 7 through 12 will be obtained from Phi factors. Otherwise, if Design Provision is 2 (ASD), the value of items 6 through 12 will come from Omega factors.

## Remarks

This function retrieves the value of a cold formed design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignPreferenceItemAISI\_16()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'set coldformed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-16")

   'get preference item
      ret = SapModel.DesignColdFormed.AISI\_16.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.2.0.

Added item 14 version 27.0.0.

## See Also

[SetPreference](SetPreference.htm)



## SetOverwrite

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetOverwrite.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_ASD96.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 33, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Live load reduction factor

4 = Unbraced length ratio, Major

5 = Unbraced length ratio, Minor

6 = Unbraced length ratio, Lateral Torsional
Buckling

7 = Unbraced length ratio, Distortional Buckling

8 = Effective length factor, K Major

9 = Effective length factor, K Minor

10 = Effective length factor, K Lateral Torsional
Buckling

11 = Effective length factor, K Distortional
Buckling

12 = Rotational stiffness, kPhi (Distortional
Buckling)

13 = Moment coefficient, Cm Major

14 = Moment coefficient, Cm Minor

15 = Moment coefficient, Ctf Major

16 = Moment coefficient, Ctf Minor

17 = Bending coefficient, Cb Major

18 = Bending coefficient, Cb Minor

19 = Moment factor, Alpha Major

20 = Moment factor, Alpha Minor

21 = Nonsway moment factor, B1 Major

22 = Nonsway moment factor, B1 Minor

23 = Sway moment factor, B2 Major

24 = Sway moment factor, B2 Minor

25 = Through fastened to deck

26 = Fastener eccentricity, a/b

27 = Hole diameter on web

28 = Hole length on web

29 = Hole spacing on web

30 = Asymmetric integral ratio, Major

31 = Asymmetric integral ratio, Minor

32 = Nominal bending capacity for lateral torsional
buckling, Mn33

33 = Nominal bending capacity for lateral torsional
buckling, Mn22

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program
Default

1 = Moment
Frame

2 = Braced
Frame

2 = Demand/capacity ratio limit

Value >=
0; 0 means use program determined value

3 = Live load reduction factor

Value >=
0; 0 means use a program determined value.

4 = Unbraced length ratio, Major

Value >=
0; 0 means use program determined value.

5 = Unbraced length ratio, Minor

Value >=
0; 0 means use program determined value.

6 = Unbraced length ratio, Lateral Torsional
Buckling

Value >=
0; 0 means use program determined value.

7 = Unbraced length ratio, Distortional
Buckling

Value >=
0; 0 means use program determined value.

8 = Effective length factor, K Major

Value >=
0; 0 means use program determined value.

9 = Effective length factor, K Minor

Value >=
0; 0 means use program determined value.

10 = Effective length factor, K Lateral
Torsional Buckling

Value >=
0; 0 means use program determined value.

11 = Effective length factor, K Distortional
Buckling

Value >=
0; 0 means use program determined value.

12 = Rotational stiffness, kPhi (Distortional
Buckling)

Value >=
0; 0 means use program determined value. [F]

13 = Moment coefficient, Cm Major

Value >=
0; 0 means use program determined value.

14 = Moment coefficient, Cm Minor

Value >=
0; 0 means use program determined value.

15 = Moment coefficient, Ctf Major

Value >=
0; 0 means use program determined value.

16 = Moment coefficient, Ctf Minor

Value >=
0; 0 means use program determined value.

17 = Bending coefficient, Cb Major

Value >=
0; 0 means use program determined value.

18 = Bending coefficient, Cb Minor

Value >=
0; 0 means use program determined value.

19 = Moment factor, Alpha Major

Value >=
0; 0 means use program determined value.

20 = Moment factor, Alpha Minor

Value >=
0; 0 means use program determined value.

21 = Nonsway moment factor, B1 Major

Value >=
0; 0 means use program determined value.

22 = Nonsway moment factor, B1 Minor

Value >=
0; 0 means use program determined value.

23 = Sway moment factor, B2 Major

Value >=
0; 0 means use program determined value.

24 = Sway moment factor, B2 Minor

Value >=
0; 0 means use program determined value.

25 = Through fastened to deck

0 = No.

Any other
value = Yes.

26 = Fastener eccentricity, a/b

Value >=
0; 0 means use program determined value. [L]

27 = Hole diameter on web

Value >=
0; 0 means use program determined value. [L]

28 = Hole length on web

Value >=
hole diameter on web; 0 means use program determined value. [L]

29 = Hole spacing on web

Value >=
hole length on web; 0 means use program determined value. [L]

30 = Asymmetric integral ratio, Major

Value >=
0; 0 means use program determined value.

31 = Asymmetric integral ratio, Minor

Value >=
0; 0 means use program determined value.

32 = Nominal bending capacity for lateral
torsional buckling, Mn33

Value >=
0; 0 means use program determined value. [FL]

33 = Nominal bending capacity for lateral
torsional buckling, Mn22

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
to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a cold formed design
overwrite item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignOverwriteItemAISI\_16()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name,
MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC",
Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 72, 2, 144, True, "CdC", "CdC")

   'set cold formed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-16")

   'set overwrite item
      ret = SapModel.DesignColdFormed.AISI\_16.SetOverwrite("8",
1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.2.0.

## See Also

[GetOverwrite](GetOverwrite.htm)



## SetPreference

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_16.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Second order method

4 = Design provision

5 = Lateral factor

6 = Use lateral factor

7 = PhiTy resistance or OmegaTy safety factor

8 = PhiTr resistance or OmegaTr safety factor

9 = PhiC resistance or OmegaC safety factor

10 = PhiB resistance or OmegaB safety factor

11 = PhiBPipe resistance or OmegaBPipe safety factor

12 = PhiV resistance or OmegaV safety factor

13 = Time history design

14 = Pattern live load factor

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Demand/capacity ratio limit

Value > 0

3 = Second Order Method

1 = General 2nd Order

2 = Amplified 1st Order

4 = Design Provision

1 = LRFD

2 = ASD

3 = LSD

5 = Lateral Factor

Value > 0

6 = Use Lateral Factor

1 = No

2 = Yes

7 = PhiTy resistance or OmegaTy safety factor

PhiTy:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image001.png)

OmegaTy:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image003.png)

8 = PhiTr resistance or OmegaTr safety factor

PhiTr:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image001.png)

OmegaTr:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image003.png)

9 = PhiC resistance or OmegaC safety factor

PhiC:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image001.png)

OmegaC:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image003.png)

10 = PhiB resistance or OmegaB safety factor

PhiB:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image001.png)

OmegaB:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image003.png)

11 = PhiBPipe resistance or OmegaBPipe safety factor

PhiBr:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image001.png)

OmegaBr:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image003.png)

12 = PhiV or OmegaV safety factor

PhiV:         ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image001.png)

OmegaV:   ![](../../../../assets/images/SAP2000_API_Fuctions/Design/Cold_Formed/AISI_2016/SetPreference_files/image003.png)

13 = Time history design

1 = Envelopes

2 = Step-by step

14 = Pattern live load factor

Value > 0

If Design Provision is 1 (LRFD) or 3 (LSD), Phi factors will be set to have value of items 7 through 12. Otherwise, if Design Provision is 2 (ASD), Omega factors will be set to have value of items 7 through 12.

## Remarks

This function sets the value of a cold formed design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignPreferenceItemAISI\_16()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'set coldformed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-16")

   'set preference item
      ret = SapModel.DesignColdFormed.AISI\_16.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 22.2.0.

Added item 14 version 27.0.0.

## See Also

[GetPreference](GetPreference.htm)



## GetOverwrite {Cold Formed AISI ASD96}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_ASD96/GetOverwrite_{Cold_Formed_AISI_ASD96}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_ASD96.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a cold formed frame design procedure.

Item

This is an integer between 1 and 27, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Moment coefficient, Ctf Major

10 = Moment coefficient, Ctf Minor

11 = Bending coefficient, Cb

12 = Moment factor, Alpha Major

13 = Moment factor, Alpha Minor

14 = Through fastened to deck

15 = Fastener eccentricity, a/b

16 = Hole diameter at top flange

17 = Hole diameter at bottom flange

18 = Hole diameter on web

19 = Yield stress, Fy

20 = Nominal compressive capacity, Pnc

21 = Nominal tensile capacity, Pnt

22 = Nominal bending capacity for yielding, Mn33

23 = Nominal bending capacity for yielding, Mn22

24 = Nominal bending capacity for lateral torsional buckling, Mn33

25 = Nominal bending capacity for lateral torsional buckling, Mn22

26 = Nominal shear capacity, Vn2

27 = Nominal shear capacity, Vn3

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

9 = Moment coefficient, Ctf Major

Value >= 0; 0 means use program determined value.

10 = Moment coefficient, Ctf Minor

Value >= 0; 0 means use program determined value.

11 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

12 = Moment factor, Alpha Major

Value >= 0; 0 means use program determined value.

13 = Moment factor, Alpha Minor

Value >= 0; 0 means use program determined value.

14 = Through fastened to deck

0 = No.

Any other value = Yes.

15 = Fastener eccentricity, a/b

Value >= 0; 0 means use program determined value. [L]

16 = Hole diameter at top flange

Value >= 0; 0 means use program determined value. [L]

17 = Hole diameter at bottom flange

Value >= 0; 0 means use program determined value. [L]

18 = Hole diameter on web

Value >= 0; 0 means use program determined value. [L]

19 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

20 = Nominal compressive capacity, Pnc

Value >= 0; 0 means use program determined value. [F]

21 = Nominal tensile capacity, Pnt

Value >= 0; 0 means use program determined value. [F]

22 = Nominal bending capacity for yielding, Mn33

Value >= 0; 0 means use program determined value. [FL]

23 = Nominal bending capacity for yielding, Mn22

Value >= 0; 0 means use program determined value. [FL]

24 = Nominal bending capacity for lateral torsional buckling, Mn33

Value >= 0; 0 means use program determined value. [FL]

25 = Nominal bending capacity for lateral torsional buckling, Mn22

Value >= 0; 0 means use program determined value. [FL]

26 = Nominal shear capacity, Vn2

Value >= 0; 0 means use program determined value. [F]

27 = Nominal shear capacity, Vn3

Value >= 0; 0 means use program determined value. [F]

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a cold formed design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignOverwriteItemAISI\_ASD96()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'set cold formed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-ASD96")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start cold formed design
      ret = SapModel.DesignColdFormed.StartDesign

   'get overwrite item
      ret = SapModel.DesignColdFormed.AISI\_ASD96.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Cold_Formed_AISI_ASD96}.htm)



## GetPreference {Cold Formed AISI ASD96}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_ASD96/GetPreference_{Cold_Formed_AISI_ASD96}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_ASD96.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Omega bending stiffened

4 = Omega bending unstiffened

5 = Omega bending lateral torsional buckling

6 = Omega shear slender

7 = Omega shear nonslender

8 = Omega axial tension

9 = Omega axial compression

10 = Time history design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Demand/capacity ratio limit

Value > 0

3 = Omega bending stiffened

Value > 0

4 = Omega bending unstiffened

Value > 0

5 = Omega bending lateral torsional buckling

Value > 0

6 = Omega shear slender

Value > 0

7 = Omega shear nonslender

Value > 0

8 = Omega axial tension

Value > 0

9 = Omega axial compression

Value > 0

10 = Time history design

1 = Envelopes

2 = Step-by step

## Remarks

This function retrieves the value of a cold formed design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignPreferenceItemAISI\_ASD96()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'set coldformed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-ASD96")

   'get preference item
      ret = SapModel.DesignColdFormed.AISI\_ASD96.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetPreference](SetPreference_{Cold_Formed_AISI_ASD96}.htm)



## SetOverwrite {Cold Formed AISI ASD96}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_ASD96/SetOverwrite_{Cold_Formed_AISI_ASD96}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_ASD96.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 27, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Moment coefficient, Ctf Major

10 = Moment coefficient, Ctf Minor

11 = Bending coefficient, Cb

12 = Moment factor, Alpha Major

13 = Moment factor, Alpha Minor

14 = Through fastened to deck

15 = Fastener eccentricity, a/b

16 = Hole diameter at top flange

17 = Hole diameter at bottom flange

18 = Hole diameter on web

19 = Yield stress, Fy

20 = Nominal compressive capacity, Pnc

21 = Nominal tensile capacity, Pnt

22 = Nominal bending capacity for yielding, Mn33

23 = Nominal bending capacity for yielding, Mn22

24 = Nominal bending capacity for lateral torsional buckling, Mn33

25 = Nominal bending capacity for lateral torsional buckling, Mn22

26 = Nominal shear capacity, Vn2

27 = Nominal shear capacity, Vn3

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

9 = Moment coefficient, Ctf Major

Value >= 0; 0 means use program determined value.

10 = Moment coefficient, Ctf Minor

Value >= 0; 0 means use program determined value.

11 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

12 = Moment factor, Alpha Major

Value >= 0; 0 means use program determined value.

13 = Moment factor, Alpha Minor

Value >= 0; 0 means use program determined value.

14 = Through fastened to deck

0 = No.

Any other value = Yes.

15 = Fastener eccentricity, a/b

Value >= 0; 0 means use program determined value. [L]

16 = Hole diameter at top flange

Value >= 0; 0 means use program determined value. [L]

17 = Hole diameter at bottom flange

Value >= 0; 0 means use program determined value. [L]

18 = Hole diameter on web

Value >= 0; 0 means use program determined value. [L]

19 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

20 = Nominal compressive capacity, Pnc

Value >= 0; 0 means use program determined value. [F]

21 = Nominal tensile capacity, Pnt

Value >= 0; 0 means use program determined value. [F]

22 = Nominal bending capacity for yielding, Mn33

Value >= 0; 0 means use program determined value. [FL]

23 = Nominal bending capacity for yielding, Mn22

Value >= 0; 0 means use program determined value. [FL]

24 = Nominal bending capacity for lateral torsional buckling, Mn33

Value >= 0; 0 means use program determined value. [FL]

25 = Nominal bending capacity for lateral torsional buckling, Mn22

Value >= 0; 0 means use program determined value. [FL]

26 = Nominal shear capacity, Vn2

Value >= 0; 0 means use program determined value. [F]

27 = Nominal shear capacity, Vn3

Value >= 0; 0 means use program determined value. [F]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a cold formed design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignOverwriteItemAISI\_ASD96()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'set cold formed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-ASD96")

   'set overwrite item
      ret = SapModel.DesignColdFormed.AISI\_ASD96.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Cold_Formed_AISI_ASD96}.htm)



## SetPreference {Cold Formed AISI ASD96}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_ASD96/SetPreference_{Cold_Formed_AISI_ASD96}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_ASD96.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Omega bending stiffened

4 = Omega bending unstiffened

5 = Omega bending lateral torsional buckling

6 = Omega shear slender

7 = Omega shear nonslender

8 = Omega axial tension

9 = Omega axial compression

10 = Time history design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Demand/capacity ratio limit

Value > 0

3 = Omega bending stiffened

Value > 0

4 = Omega bending unstiffened

Value > 0

5 = Omega bending lateral torsional buckling

Value > 0

6 = Omega shear slender

Value > 0

7 = Omega shear nonslender

Value > 0

8 = Omega axial tension

Value > 0

9 = Omega axial compression

Value > 0

10 = Time history design

1 = Envelopes

2 = Step-by step

## Remarks

This function sets the value of a cold formed design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignPreferenceItemAISI\_ASD96()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'set coldformed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-ASD96")

   'set preference item
      ret = SapModel.DesignColdFormed.AISI\_ASD96.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetPreference](GetPreference_{Cold_Formed_AISI_ASD96}.htm)



## GetOverwrite {Cold Formed AISI LRFD96}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_LRFD96/GetOverwrite_{Cold_Formed_AISI_LRFD96}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_LRFD96.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a cold formed frame design procedure.

Item

This is an integer between 1 and 27, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Moment coefficient, Ctf Major

10 = Moment coefficient, Ctf Minor

11 = Bending coefficient, Cb

12 = Moment factor, Alpha Major

13 = Moment factor, Alpha Minor

14 = Through fastened to deck

15 = Fastener eccentricity, a/b

16 = Hole diameter at top flange

17 = Hole diameter at bottom flange

18 = Hole diameter on web

19 = Yield stress, Fy

20 = Nominal compressive capacity, Pnc

21 = Nominal tensile capacity, Pnt

22 = Nominal bending capacity for yielding, Mn33

23 = Nominal bending capacity for yielding, Mn22

24 = Nominal bending capacity for lateral torsional buckling, Mn33

25 = Nominal bending capacity for lateral torsional buckling, Mn22

26 = Nominal shear capacity, Vn2

27 = Nominal shear capacity, Vn3

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

9 = Moment coefficient, Ctf Major

Value >= 0; 0 means use program determined value.

10 = Moment coefficient, Ctf Minor

Value >= 0; 0 means use program determined value.

11 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

12 = Moment factor, Alpha Major

Value >= 0; 0 means use program determined value.

13 = Moment factor, Alpha Minor

Value >= 0; 0 means use program determined value.

14 = Through fastened to deck

0 = No.

Any other value = Yes.

15 = Fastener eccentricity, a/b

Value >= 0; 0 means use program determined value. [L]

16 = Hole diameter at top flange

Value >= 0; 0 means use program determined value. [L]

17 = Hole diameter at bottom flange

Value >= 0; 0 means use program determined value. [L]

18 = Hole diameter on web

Value >= 0; 0 means use program determined value. [L]

19 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

20 = Nominal compressive capacity, Pnc

Value >= 0; 0 means use program determined value. [F]

21 = Nominal tensile capacity, Pnt

Value >= 0; 0 means use program determined value. [F]

22 = Nominal bending capacity for yielding, Mn33

Value >= 0; 0 means use program determined value. [FL]

23 = Nominal bending capacity for yielding, Mn22

Value >= 0; 0 means use program determined value. [FL]

24 = Nominal bending capacity for lateral torsional buckling, Mn33

Value >= 0; 0 means use program determined value. [FL]

25 = Nominal bending capacity for lateral torsional buckling, Mn22

Value >= 0; 0 means use program determined value. [FL]

26 = Nominal shear capacity, Vn2

Value >= 0; 0 means use program determined value. [F]

27 = Nominal shear capacity, Vn3

Value >= 0; 0 means use program determined value. [F]

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a cold formed design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignOverwriteItemAISI\_LRFD96()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'set cold formed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-LRFD96")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start cold formed design
      ret = SapModel.DesignColdFormed.StartDesign

   'get overwrite item
      ret = SapModel.DesignColdFormed.AISI\_LRFD96.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Cold_Formed_AISI_LRFD96}.htm)



## GetPreference {Cold Formed AISI LRFD96}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_LRFD96/GetPreference_{Cold_Formed_AISI_LRFD96}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_LRFD96.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Phi bending stiffened

4 = Phi bending unstiffened

5 = Phi bending lateral torsional buckling

6 = Phi shear slender

7 = Phi shear nonslender

8 = Phi axial tension

9 = Phi axial compression

10 = Time history design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Demand/capacity ratio limit

Value > 0

3 = Phi bending stiffened

Value > 0

4 = Phi bending unstiffened

Value > 0

5 = Phi bending lateral torsional buckling

Value > 0

6 = Phi shear slender

Value > 0

7 = Phi shear nonslender

Value > 0

8 = Phi axial tension

Value > 0

9 = Phi axial compression

Value > 0

10 = Time history design

1 = Envelopes

2 = Step-by step

## Remarks

This function retrieves the value of a cold formed design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignPreferenceItemAISI\_LRFD96()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'set coldformed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-LRFD96")

   'get preference item
      ret = SapModel.DesignColdFormed.AISI\_LRFD96.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetPreference](SetPreference_{Cold_Formed_AISI_LRFD96}.htm)



## SetOverwrite {Cold Formed AISI LRFD96}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_LRFD96/SetOverwrite_{Cold_Formed_AISI_LRFD96}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_LRFD96.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 27, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Live load reduction factor

3 = Unbraced length ratio, Major

4 = Unbraced length ratio, Minor and Lateral Torsional Buckling

5 = Effective length factor, K Major

6 = Effective length factor, K Minor

7 = Moment coefficient, Cm Major

8 = Moment coefficient, Cm Minor

9 = Moment coefficient, Ctf Major

10 = Moment coefficient, Ctf Minor

11 = Bending coefficient, Cb

12 = Moment factor, Alpha Major

13 = Moment factor, Alpha Minor

14 = Through fastened to deck

15 = Fastener eccentricity, a/b

16 = Hole diameter at top flange

17 = Hole diameter at bottom flange

18 = Hole diameter on web

19 = Yield stress, Fy

20 = Nominal compressive capacity, Pnc

21 = Nominal tensile capacity, Pnt

22 = Nominal bending capacity for yielding, Mn33

23 = Nominal bending capacity for yielding, Mn22

24 = Nominal bending capacity for lateral torsional buckling, Mn33

25 = Nominal bending capacity for lateral torsional buckling, Mn22

26 = Nominal shear capacity, Vn2

27 = Nominal shear capacity, Vn3

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

9 = Moment coefficient, Ctf Major

Value >= 0; 0 means use program determined value.

10 = Moment coefficient, Ctf Minor

Value >= 0; 0 means use program determined value.

11 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

12 = Moment factor, Alpha Major

Value >= 0; 0 means use program determined value.

13 = Moment factor, Alpha Minor

Value >= 0; 0 means use program determined value.

14 = Through fastened to deck

0 = No.

Any other value = Yes.

15 = Fastener eccentricity, a/b

Value >= 0; 0 means use program determined value. [L]

16 = Hole diameter at top flange

Value >= 0; 0 means use program determined value. [L]

17 = Hole diameter at bottom flange

Value >= 0; 0 means use program determined value. [L]

18 = Hole diameter on web

Value >= 0; 0 means use program determined value. [L]

19 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

20 = Nominal compressive capacity, Pnc

Value >= 0; 0 means use program determined value. [F]

21 = Nominal tensile capacity, Pnt

Value >= 0; 0 means use program determined value. [F]

22 = Nominal bending capacity for yielding, Mn33

Value >= 0; 0 means use program determined value. [FL]

23 = Nominal bending capacity for yielding, Mn22

Value >= 0; 0 means use program determined value. [FL]

24 = Nominal bending capacity for lateral torsional buckling, Mn33

Value >= 0; 0 means use program determined value. [FL]

25 = Nominal bending capacity for lateral torsional buckling, Mn22

Value >= 0; 0 means use program determined value. [FL]

26 = Nominal shear capacity, Vn2

Value >= 0; 0 means use program determined value. [F]

27 = Nominal shear capacity, Vn3

Value >= 0; 0 means use program determined value. [F]

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a cold formed design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignOverwriteItemAISI\_LRFD96()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'set cold formed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-LRFD96")

   'set overwrite item
      ret = SapModel.DesignColdFormed.AISI\_LRFD96.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Cold_Formed_AISI_LRFD96}.htm)



## SetPreference {Cold Formed AISI LRFD96}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/AISI_LRFD96/SetPreference_{Cold_Formed_AISI_LRFD96}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignColdFormed.AISI\_LRFD96.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Demand/capacity ratio limit

3 = Phi bending stiffened

4 = Phi bending unstiffened

5 = Phi bending lateral torsional buckling

6 = Phi shear slender

7 = Phi shear nonslender

8 = Phi axial tension

9 = Phi axial compression

10 = Time history design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Demand/capacity ratio limit

Value > 0

3 = Phi bending stiffened

Value > 0

4 = Phi bending unstiffened

Value > 0

5 = Phi bending lateral torsional buckling

Value > 0

6 = Phi shear slender

Value > 0

7 = Phi shear nonslender

Value > 0

8 = Phi axial tension

Value > 0

9 = Phi axial compression

Value > 0

10 = Time history design

1 = Envelopes

2 = Step-by step

## Remarks

This function sets the value of a cold formed design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignPreferenceItemAISI\_LRFD96()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'set coldformed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-LRFD96")

   'set preference item
      ret = SapModel.DesignColdFormed.AISI\_LRFD96.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetPreference](GetPreference_{Cold_Formed_AISI_LRFD96}.htm)



## DeleteResults {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/DeleteResults_{Cold_Formed}.htm`*

# DeleteResults

## Syntax

SapObject.SapModel.DesignColdFormed.DeleteResults

## VB6 Procedure

Function DeleteResults() As Long

## Parameters

None

## Remarks

This function deletes all cold formed frame design results.

The function returns zero if the results are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteColdFormedDesignResults()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start cold formed design
      ret = SapModel.DesignColdFormed.StartDesign

   'delete cold formed design results
      ret = SapModel.DesignColdFormed.DeleteResults

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## GetOverwrite {Euro06}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/EuroCode_3_1-3_2006/GetOverwrite_(1).htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignColdFormed.EuroCold06.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a cold-formed steel
frame design procedure.

Item

This is an integer between 1 and 34, inclusive, indicating
the overwrite item considered.

1 = Demand/capacity ratio limit

2 = Live load reduction factor

3 = Yield stress, Fy

4 = Net area to total area ratio

5 = Unbraced length ratio, y-y

6 = Unbraced length ratio, z-z

7 = Unbraced length ratio, LTB

8 = Effective length factor sway, K2y

9 = Effective length factor sway, K2z

10 = Effective length factor, K LTB

11 = Effective length factor braced, K1y

12 = Effective length factor braced, K1z

13 = Bending coefficient, C1

14 = Bending coefficient, C2

15 = Bending coefficient, C3

16 = Moment coefficient, kyy

17 = Moment coefficient, kzz

18 = Moment coefficient, kzy

19 = Moment coefficient, kyz

20 = Column buckling curve, y-y

21 = Column buckling curve, z-z

22 = Buckling curve for LTB

23 = Elastic torsional buckling force,
Ncr T

24 = Elastic torsional-flexural buckling
force, Ncr TF

25 = Compressive capacity, NRk

26 = Tensile capacity, Nt.Rd

27 = Bending capacity about the y-y axis,
MyRk

28 = Bending capacity about the z-z axis,
MzRk

29 = Shear capacity along z-z axis, Vbz.Rd

30 = Shear capacity along y-y axis, Vby.Rd

31 = Warping coefficient, kw

32 = Coordinate of load application, za

33 = Lateral-torsional buckling moment
capacity, Mcr

34 = Member buckling interaction equation

Value

The value of the considered overwrite item.

1 = Demand/capacity ratio limit

Value
>= 0; 0 means use program determined value.

2 = Live load reduction factor

Value
>= 0; 0 means use program determined value.

3 = Yield stress, Fy

Value
>= 0; 0 means use program determined value. [F/L2]

4 = Net area to total area ratio

Value
>= 0; 0 means use program default value.

5 = Unbraced length ratio, y-y

Value
>= 0; 0 means use program determined value.

6 = Unbraced length ratio, z-z

Value
>= 0; 0 means use program determined value.

7 = Unbraced length ratio, LTB

Value
>= 0; 0 means use program determined value.

8 = Effective length factor sway, K2y

Value >=
0; 0 means use program determined value.

9 = Effective length factor sway, K2z

Value
>= 0; 0 means use program determined value.

10 = Effective length factor, K LTB

Value
>= 0; 0 means use program determined value.

11 = Effective length factor braced, K1y

Value
>= 0; 0 means use program determined value.

12 = Effective length factor braced, K1z

Value
>= 0; 0 means use program determined value.

13 = Bending coefficient, C1

Value
>= 0; 0 means use program determined value.

14 = Bending coefficient, C2

Value >=
0; 0 means use program determined value.

15 = Bending coefficient, C3

Value
>= 0; 0 means use program determined value.

16 = Moment coefficient, kyy

Value
>= 0; 0 means use program determined value.

17 = Moment coefficient, kzz

Value
>= 0; 0 means use program determined value.

18 = Moment coefficient, kzy

Value
>= 0; 0 means use program determined value.

19 = Moment coefficient, kyz

Value
>= 0; 0 means use program determined value.

20 = Column buckling curve, y-y

0
= Program default

1
= a0

2
= a

3
= b

4
= c

5
= d

21 = Column buckling curve, z-z

0
= Program default

1
= a0

2
= a

3
= b

4
= c

5
= d

22 = Buckling curve for LTB

0
= Program default

1
= a0

2
= a

3
= b

4
= c

5
= d

23 = Elastic torsional buckling force,
Ncr T

Value
>= 0; 0 means use program determined value. [F]

24 = Elastic torsional-flexural buckling
force, Ncr TF

Value
>= 0; 0 means use program determined value. [F]

25 = Compressive capacity, NRk

Value
>= 0; 0 means use program determined value. [F]

26 = Tensile capacity, Nt.Rd

Value
>= 0; 0 means use program determined value. [F]

27 = Bending capacity about the y-y axis,
MyRk

Value
>= 0; 0 means use program determined value. [FL]

28 = Bending capacity about the z-z axis,
MzRk

Value
>= 0; 0 means use program determined value. [FL]

29 = Shear capacity along z-z axix, Vbz.Rd

Value
>= 0; 0 means use program determined value. [F]

30 = Shear capacity along y-y axis, Vby.Rd

Value
>= 0; 0 means use program determined value. [F]

31 = Warping coefficient, kw
(used in Mcr calculation)

0.5
=<Value =< 1; 0 means use program determined value which is defaulted
to 1.0.

32 = Coordinate of load application, za
(used in Mcr calculation)

33 = Lateral-torsional buckling moment
capacity, Mcr

Value
>= 0; 0 means use program determined value. [FL]

34 = Member buckling interaction equations

1
= Equations 6.61 and 6.62 in EN 1993-1-1:2005

2 = Equation 6.36 in EN 1993-1-3:2006 for each
axis of bending separately

3
= Equation 6.36 in EN 1993-1-3:2006 for both axes of bending simultaneously

4
= Equation 6.61 and 6.62 in EN 1993-1-1:2005 and Equation 6.36 in EN 1993-1-3:2006
for each axis of bending separately

5
= Equation 6.61 and 6.62 in EN 1993-1-1:2005 and Equation 6.36 in EN 1993-1-3:2006
for both axes of bending simultaneously

ProgDet

If this item is True, the specified value is program
determined.

## **Remarks**

This function retrieves the value of a steel design
overwrite item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## **VBA Example**

Sub GetSteelDesignOverwriteItemEuroCold06()
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
      ret = SapModel.DesignColdFormed.SetCode("Eurocode
3 1-3 2006")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignColdFormed.StartDesign

   'get overwrite item
      ret = SapModel.DesignColdFormed.EuroCold06.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 23.0.0.

Added item 34 in version 23.4.0

Changed references from major and minor axes to y-y
and z-z in version 23.4.0.

## See Also

[SetOverwrite](SetOverwrite_(1).htm)



## GetPreference {Euro06}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/EuroCode_3_1-3_2006/GetPreference_(1).htm`*

# **GetPreference**

## **Syntax**

SapObject.SapModel.DesignColdFormed.EuroCold06.GetPreference

## **VB6 Procedure**

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## **Parameters**

Item

This is an integer between 1 and 12, inclusive, indicating
the preference item considered.

1 = Country

2 = Multi-response case design

3 = Demand/capacity ratio limit

4 = Combos equation

5 = Reliability class

6 = K factor method

7 = Consider P-Delta Done

8 = GammaM0

9 = GammaM1

10 = GammaM2

11 = Pattern live load factor

12 = Member buckling interaction equations

Value

The value of the considered preference
item.

1 = Country

     1 = CEN
Default

     2 = United
Kingdom

     3 = Slovenia

     4 = Bulgaria

     5 = Norway

     7 = Sweden

     8 = Finland

     9 = Denmark

   10 = Portugal

   11 = Germany

2 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step --  All

3 = Demand/capacity ratio limit

Value > 0

4 = Combos equation

     1 = Eq. 6.10

     2 = Max of Eqs.
6.10a and 6.10b

5 = Reliability class

     1 = Class 1

     2 = Class 2

     3 = Class 3

6 = K factor method

     1 = Method 1 (Annex
A)

     2 = Method 2 (Annex
B)

7 = Consider P-Delta Done

0 = No

Any other value = Yes

8 = GammaM0

Value > 0

9 = GammaM1

Value > 0

10 = GammaM2

       Value
> 0

11 = Pattern live load factor

 Value >= 0

12
= Member buckling interaction equations

1 = Equations 6.61 and
6.62 in EN 1993-1-1:2005

2 = Equation 6.36 in EN
1993-1-3:2006 for each axis of bending separately

3
= Equation 6.36 in EN 1993-1-3:2006 for both axes of bending simultaneously

4
= Equation 6.61 and 6.62 in EN 1993-1-1:2005 and Equation 6.36 in EN 1993-1-3:2006
for each axis of bending separately

5
= Equation 6.61 and 6.62 in EN 1993-1-1:2005 and Equation 6.36 in EN 1993-1-3:2006
for both axes of bending simultaneously

## **Remarks**

This function retrieves the value of a cold-formed steel
design preference item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemEuroCold06()
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
      ret = SapModel.DesignColdFormed.SetCode("Eurocode
3 1-3 2006")

   'get preference item
      ret = SapModel.DesignColdFormed.EuroCold06.GetPreference(4,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## **Release Notes**

Initial release in version 23.0.0.

Added item 12 in version 23.4.0

## **See Also**

[SetPreference](SetPreference_(1).htm)



## SetOverwrite {Euro06}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/EuroCode_3_1-3_2006/SetOverwrite_(1).htm`*

# **SetOverwrite**

## **Syntax**

SapObject.SapModel.DesignColdFormed.EuroCold06.SetOverwrite

## **VB6 Procedure**

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## **Parameters**

Name

The name of a frame object with a cold-formed steel
frame design procedure.

Item

This is an integer between 1 and 34, inclusive, indicating
the overwrite item considered.

1 = Demand/capacity ratio limit

2 = Live load reduction factor

3 = Yield stress, Fy

4 = Net area to total area ratio

5 = Unbraced length ratio, y-y

6 = Unbraced length ratio, z-z

7 = Unbraced length ratio, LTB

8 = Effective length factor sway, K2y

9 = Effective length factor sway, K2z

10 = Effective length factor, K LTB

11 = Effective length factor braced, K1y

12 = Effective length factor braced, K1z

13 = Bending coefficient, C1

14 = Bending coefficient, C2

15 = Bending coefficient, C3

16 = Moment coefficient, kyy

17 = Moment coefficient, kzz

18 = Moment coefficient, kzy

19 = Moment coefficient, kyz

20 = Column buckling curve, y-y

21 = Column buckling curve, z-z

22 = Buckling curve for LTB

23 = Elastic torsional buckling force,
Ncr T

24 = Elastic torsional-flexural buckling
force, Ncr TF

25 = Compressive capacity, NRk

26 = Tensile capacity, Nt.Rd

27 = Bending capacity about the y-y axis,
MyRk

28 = Bending capacity about the z-z axis,
MzRk

29 = Shear capacity along z-z axis, Vbz.Rd

30 = Shear capacity along y-y axis, Vby.Rd

31 = Warping coefficient, kw

32 = Coordinate of load application, za

33 = Lateral-torsional buckling moment
capacity, Mcr

34 = Member buckling interaction equation

Value

The value of the considered overwrite item.

1 = Demand/capacity ratio limit

Value
>= 0; 0 means use program determined value.

2 = Live load reduction factor

Value
>= 0; 0 means use program determined value.

3 = Yield stress, Fy

Value
>= 0; 0 means use program determined value. [F/L2]

4 = Net area to total area ratio

Value
>= 0; 0 means use program default value.

5 = Unbraced length ratio, y-y

Value
>= 0; 0 means use program determined value.

6 = Unbraced length ratio, z-z

Value
>= 0; 0 means use program determined value.

7 = Unbraced length ratio, LTB

Value
>= 0; 0 means use program determined value.

8 = Effective length factor sway, K2y

Value >=
0; 0 means use program determined value.

9 = Effective length factor sway, K2z

Value
>= 0; 0 means use program determined value.

10 = Effective length factor, K LTB

Value
>= 0; 0 means use program determined value.

11 = Effective length factor braced, K1y

Value
>= 0; 0 means use program determined value.

12 = Effective length factor braced, K1z

Value
>= 0; 0 means use program determined value.

13 = Bending coefficient, C1

Value
>= 0; 0 means use program determined value.

14 = Bending coefficient, C2

Value >=
0; 0 means use program determined value.

15 = Bending coefficient, C3

Value
>= 0; 0 means use program determined value.

16 = Moment coefficient, kyy

Value
>= 0; 0 means use program determined value.

17 = Moment coefficient, kzz

Value
>= 0; 0 means use program determined value.

18 = Moment coefficient, kzy

Value
>= 0; 0 means use program determined value.

19 = Moment coefficient, kyz

Value
>= 0; 0 means use program determined value.

20 = Column buckling curve, y-y

0
= Program default

1
= a0

2
= a

3
= b

4
= c

5
= d

21 = Column buckling curve, z-z

0
= Program default

1
= a0

2
= a

3
= b

4
= c

5
= d

22 = Buckling curve for LTB

0
= Program default

1
= a0

2
= a

3
= b

4
= c

5
= d

23 = Elastic torsional buckling force,
Ncr T

Value
>= 0; 0 means use program determined value. [F]

24 = Elastic torsional-flexural buckling
force, Ncr TF

Value
>= 0; 0 means use program determined value. [F]

25 = Compressive capacity, NRk

Value
>= 0; 0 means use program determined value. [F]

26 = Tensile capacity, Nt.Rd

Value
>= 0; 0 means use program determined value. [F]

27 = Bending capacity about the y-y axis,
MyRk

Value
>= 0; 0 means use program determined value. [FL]

28 = Bending capacity about the z-z axis,
MzRk

Value
>= 0; 0 means use program determined value. [FL]

29 = Shear capacity along z-z axix, Vbz.Rd

Value
>= 0; 0 means use program determined value. [F]

30 = Shear capacity along y-y axis, Vby.Rd

Value
>= 0; 0 means use program determined value. [F]

31 = Warping coefficient, kw
(used in Mcr calculation)

0.5
=<Value =< 1; 0 means use program determined value which is defaulted
to 1.0.

32 = Coordinate of load application, za
(used in Mcr calculation)

33 = Lateral-torsional buckling moment
capacity, Mcr

Value
>= 0; 0 means use program determined value. [FL]

34 = Member buckling interaction equations

1
= Equations 6.61 and 6.62 in EN 1993-1-1:2005

2 = Equation 6.36 in EN 1993-1-3:2006 for each
axis of bending separately

3
= Equation 6.36 in EN 1993-1-3:2006 for both axes of bending simultaneously

4
= Equation 6.61 and 6.62 in EN 1993-1-1:2005 and Equation 6.36 in EN 1993-1-3:2006
for each axis of bending separately

5
= Equation 6.61 and 6.62 in EN 1993-1-1:2005 and Equation 6.36 in EN 1993-1-3:2006
for both axes of bending simultaneously

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

## **Remarks**

This function sets the value of a cold-formed steel
design overwrite item.

The function returns zero if the item is successfully
set; otherwise, it returns a nonzero value.

## **VBA Example**

Sub SetSteelDesignOverwriteItemEuroCold06()
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
      ret = SapModel.DesignColdFormed.SetCode("Eurocode
3 1-3 2006")

   'set overwrite item
      ret = SapModel.DesignColdFormed.EuroCold06.SetOverwrite("8",
1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## **Release Notes**

Initial release in version 23.0.0.

Added item 34 in version 23.4.0

Changed references from major and minor axes to y-y
and z-z in version 23.4.0.

## **See Also**

[GetOverwrite](GetOverwrite_(1).htm)



## SetPreference {Euro06}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/EuroCode_3_1-3_2006/SetPreference_(1).htm`*

# **SetPreference**

## **Syntax**

SapObject.SapModel.DesignColdFormed.EuroCold06.SetPreference

## **VB6 Procedure**

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## **Parameters**

Item

This is an integer between 1 and 12, inclusive, indicating
the preference item considered.

1 = Country

2 = Multi-response case design

3 = Demand/capacity ratio limit

4 = Combos equation

5 = Reliability class

6 = K factor method

7 = Consider P-Delta Done

8 = GammaM0

9 = GammaM1

10 = GammaM2

11 = Pattern live load factor

12 = Member buckling interaction equations

Value

The value of the considered preference
item.

1 = Country

     1 = CEN
Default

     2 = United
Kingdom

     3 = Slovenia

     4 = Bulgaria

     5 = Norway

     7 = Sweden

     8 = Finland

     9 = Denmark

   10 = Portugal

   11 = Germany

2 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step --  All

3 = Demand/capacity ratio limit

Value > 0

4 = Combos equation

      1 = Eq.
6.10

      2 = Max
of Eqs. 6.10a and 6.10b

5 = Reliability class

     1 = Class 1

     2 = Class 2

     3 = Class 3

6 = K factor method

     1 = Method 1 (Annex
A)

     2 = Method 2 (Annex
B)

7 = Consider P-Delta Done

0 = No

Any other value = Yes

8 = GammaM0

Value > 0

9 = GammaM1

Value > 0

10 = GammaM2

       Value
> 0

11 = Pattern live load factor

 Value >= 0

12 = Member buckling interaction
equations

1 = Equations 6.61 and
6.62 in EN 1993-1-1:2005

2 = Equation 6.36 in EN
1993-1-3:2006 for each axis of bending separately

3
= Equation 6.36 in EN 1993-1-3:2006 for both axes of bending simultaneously

4
= Equation 6.61 and 6.62 in EN 1993-1-1:2005 and Equation 6.36 in EN 1993-1-3:2006
for each axis of bending separately

5
= Equation 6.61 and 6.62 in EN 1993-1-1:2005 and Equation 6.36 in EN 1993-1-3:2006
for both axes of bending simultaneously

## **Remarks**

This function sets the value of a cold-formed steel
design preference item.

The function returns zero if the item is successfully
set; otherwise, it returns a nonzero value.

## **VBA Example**

Sub SetSteelDesignPreferenceItemEuroCold06()
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
      ret = SapModel.DesignColdFormed.SetCode("Eurocode
3 1-3 2006")

   'set preference item
      ret = SapModel.DesignColdFormed.EuroCold06.SetPreference(4,
2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## **Release Notes**

Initial release in version 23.0.0.

Added item 12 in version 23.4.0

## **See Also**

[GetPreference](GetPreference_(1).htm)



## GetCode {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/GetCode_{Cold_Formed}.htm`*

# GetCode

## Syntax

SapObject.SapModel.DesignColdFormed.GetCode

## VB6 Procedure

Function GetCode(ByRef CodeName As String) As Long

## Parameters

CodeName

This is one of the following cold formed design code
names.

AISI-ASD96

AISI-LRFD96

## Remarks

This function retrieves the cold formed design code.

The function returns zero if the code is successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignCode()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name,
MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC",
Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 72, 2, 144, True, "CdC", "CdC")

   'get cold formed design code
      ret = SapModel.DesignColdFormed.GetCode(CodeName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetCode](SetCode_{Cold_Formed}.htm)



## GetComboAutoGenerate {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/GetComboAutoGenerate_{Cold_Formed}.htm`*

# GetComboAutoGenerate

## Syntax

SapObject.SapModel.DesignColdFormed.GetComboAutoGenerate

## VB6 Procedure

Function GetComboAutoGenerate(ByRef AutoGenerate As Boolean) As Long

## Parameters

AutoGenerate

If this item is True, the option to automatically generate code-based design load combinations for cold formed frame design is turned on. If it is False, the option is turned off.

## Remarks

This function retrieves the value of the automatically generated code-based design load combinations option for cold formed frame design.

The function returns zero if the options are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignComboAutoGenerate()
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
      ret = SapModel.DesignColdFormed.GetComboAutoGenerate(AutoGenerate)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 18.1.0.

## See Also

[SetComboAutoGenerate](SetComboAutoGenerate_{Cold_Formed}.htm)



## GetComboDeflection {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/GetComboDeflection_{Cold_Formed}.htm`*

# GetComboDeflection

## Syntax

SapObject.SapModel.DesignColdFormed.GetComboDeflection

## VB6 Procedure

Function GetComboDeflection(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of load combinations selected as design combinations for cold formed deflection design.

MyName

This is an array that includes the name of each response combination selected as a design combination for cold formed deflection design.

## Remarks

This function retrieves the names of all load combinations selected as design combinations for cold formed deflection design.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignComboDeflection()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default cold formed design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(False, False, False, True)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName2)

   'select combos for cold formed deflection design
      For i = 0 To NumberNames – 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignColdFormed.SetComboDeflection(MyName2(i), Selected)
      Next i

   'get combos selected for cold formed deflection design
      ret = SapModel.DesignColdFormed.GetComboDeflection(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetComboDeflection](SetComboDeflection_{Cold_Formed}.htm)



## GetComboStrength {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/GetComboStrength_{Cold_Formed}.htm`*

# GetComboStrength

## Syntax

SapObject.SapModel.DesignColdFormed.GetComboStrength

## VB6 Procedure

Function GetComboStrength(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of load combinations selected as design combinations for cold formed strength design.

MyName

This is an array that includes the name of each response combination selected as a design combination for cold formed strength design.

## Remarks

This function retrieves the names of all load combinations selected as design combinations for cold formed strength design.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignComboStrength()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default cold formed design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(False, False, False, True)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName2)

   'select combos for cold formed strength design
      For i = 0 To NumberNames – 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignColdFormed.SetComboStrength(MyName2(i), Selected)
      Next i

   'get combos selected for cold formed strength design
      ret = SapModel.DesignColdFormed.GetComboStrength(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetComboStrength](SetComboStrength_{Cold_Formed}.htm)



## GetDesignSection {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/GetDesignSection_{Cold_Formed}.htm`*

# GetDesignSection

## Syntax

SapObject.SapModel.DesignColdFormed.GetDesignSection

## VB6 Procedure

Function GetDesignSection(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a frame object with a cold formed frame design procedure.

PropName

The name of the design section for the specified frame object.

## Remarks

This function retrieves the design section for a specified cold formed frame object.

The function returns zero if the section is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignSection()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start cold formed design
      ret = SapModel.DesignColdFormed.StartDesign

   'get design section
      ret = SapModel.DesignColdFormed.GetDesignSection("8", PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetDesignSection](SetDesignSection_{Cold_Formed}.htm)



## GetGroup {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/GetGroup_{Cold_Formed}.htm`*

# GetGroup

## Syntax

SapObject.SapModel.DesignColdFormed.GetGroup

## VB6 Procedure

Function GetGroup(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of groups selected for cold formed design.

MyName

This is an array that includes the name of each group selected for cold formed design.

## Remarks

This function retrieves the names of all groups selected for cold formed design.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignGroup()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'select group for cold formed design
      ret = SapModel.DesignColdFormed.SetGroup("ALL", True)

   'get groups selected for cold formed design
      ret = SapModel.DesignColdFormed.GetGroup(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetGroup](SetGroup_{Cold_Formed}.htm)



## GetResultsAvailable {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/GetResultsAvailable_{Cold_Formed}.htm`*

# GetResultsAvailable {Cold Formed}

## Syntax

SapObject.SapModel.DesignColdFormed.GetResultsAvailable

## VB6 Procedure

Function GetResultsAvailable() As Boolean

## Parameters

None

## Remarks

The function returns True if the cold formed frame design results are available, otherwise False.

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

  'add cold formed material

    ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

  'create new concrete frame section property

    ret = SapModel.PropFrame.SetColdC("CdC", Name, 9, 3, 0.06, 0.25, 0.5)

  'create model from template

    ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

  'run analysis

    ret = SapModel.File.Save("C:\SapAPI\x.sdb")

    ret = SapModel.Analyze.RunAnalysis

  'start cold formed design

    ret = SapModel.DesignColdFormed.StartDesign

  'check if design results are available

    ResultsAvailable = SapModel.DesignColdFormed.GetResultsAvailable

  'close Sap2000

    SapObject.ApplicationExit.False

    Set SapModel = Nothing

    Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 18.2.0.



## GetSummaryResults {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/GetSummaryResults_{Cold_Formed}.htm`*

# GetSummaryResults

## Syntax

SapObject.SapModel.DesignColdFormed.GetSummaryResults

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

This function retrieves summary results for cold formed design.

The function returns zero if the results are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetColdFormedDesignSummaryResults()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start cold formed design
      ret = SapModel.DesignColdFormed.StartDesign

   'get summary result data
      ret = SapModel.DesignColdFormed.GetSummaryResults("8", NumberItems, FrameName, Ratio, RatioType, Location, ComboName, ErrorSummary, WarningSummary)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## ResetOverwrites {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/ResetOverwrites_{Cold_Formed}.htm`*

# ResetOverwrites

## Syntax

SapObject.SapModel.DesignColdFormed.ResetOverwrites

## VB6 Procedure

Function ResetOverwrites() As Long

## Parameters

None

## Remarks

This function resets all cold formed frame design overwrites to default values.

The function returns zero if the overwrites are successfully reset; otherwise it returns a nonzero value.

The function will fail if no cold formed frame objects are present.

## VBA Example

Sub ResetColdFormedDesignOverwrites()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'reset cold formed design overwrites
      ret = SapModel.DesignColdFormed.ResetOverwrites

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## SetAutoSelectNull {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/SetAutoSelectNull_{Cold_Formed}.htm`*

# SetAutoSelectNull

## Syntax

SapObject.SapModel.DesignColdFormed.SetAutoSelectNull

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

This function removes the auto select section assignments from all specified frame objects that have a cold formed frame design procedure.

The function returns zero if the auto select section assignments are successfully removed; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedAutoSelectSectionsNull()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)
      ret = SapModel.PropFrame.SetColdC("CdC2", Name , 9, 3, 0.07, 0.25, 0.5)
      ret = SapModel.PropFrame.SetColdC("CdC3", Name , 9, 3, 0.08, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'define new auto select list frame section property
      ReDim MyName(2)
      MyName(0) = "CdC"
      MyName(1) = "CdC2"
      MyName(2) = "CdC3"
      ret = SapModel.PropFrame.SetAutoSelectColdFormed("AUTO1", 3, MyName)

   'set frame section properties
      ret = SapModel.FrameObj.SetSection("8", "AUTO1")
      ret = SapModel.FrameObj.SetSection("10", "AUTO1")

   'set frame object selected
      ret = SapModel.FrameObj.SetSelected("8", True)

   'set auto select section null
      ret = SapModel.DesignColdFormed.SetAutoSelectNull("",SelectedObjects)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## SetCode {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/SetCode_{Cold_Formed}.htm`*

# SetCode

## Syntax

SapObject.SapModel.DesignColdFormed.SetCode

## VB6 Procedure

Function SetCode(ByVal CodeName As String) As Long

## Parameters

CodeName

This is one of the following cold formed design code names.

AISI-ASD96

AISI-LRFD96

## Remarks

This function sets the cold formed design code.

The function returns zero if the code is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignCode()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144)

   'set cold formed design code
      ret = SapModel.DesignColdFormed.SetCode("AISI-LRFD96")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetCode](GetCode_{Cold_Formed}.htm)



## SetComboAutoGenerate {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/SetComboAutoGenerate_{Cold_Formed}.htm`*

# SetComboAutoGenerate

## Syntax

SapObject.SapModel.DesignColdFormed.SetComboAutoGenerate

## VB6 Procedure

Function SetComboAutoGenerate(ByVal AutoGenerate As Boolean) As Long

## Parameters

AutoGenerate

If this item is True, the option to automatically generate code-based design load combinations for cold formed frame design is turned on. If it is False, the option is turned off.

## Remarks

This function turns on or off the option to automatically generate code-based design load combinations for cold formed frame design.

The function returns zero if the options are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignComboAutoGenerate()
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
      ret = SapModel.DesignColdFormed.SetComboAutoGenerate(False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 18.1.0.

## See Also

[GetComboAutoGenerate](GetComboAutoGenerate_{Cold_Formed}.htm)



## SetComboDeflection {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/SetComboDeflection_{Cold_Formed}.htm`*

# SetComboDeflection

## Syntax

SapObject.SapModel.DesignColdFormed.SetComboDeflection

## VB6 Procedure

Function SetComboDeflection(ByVal Name As String, ByVal Selected As Boolean) As Long

## Parameters

Name

The name of an existing load combination.

Selected

If this item is True, the specified load combination is selected as a design combination for cold formed deflection design. If it is False, the combination is not selected for cold formed deflection design.

## Remarks

This function selects or deselects a load combination for cold formed deflection design.

The function returns zero if the selection status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignComboDeflection()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default cold formed design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(False, False, False, True)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName)

   'select combos for cold formed deflection design
      For i = 0 To NumberNames – 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignColdFormed.SetComboDeflection(MyName(i), Selected)
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

[GetComboDeflection](GetComboDeflection_{Cold_Formed}.htm)



## SetComboStrength {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/SetComboStrength_{Cold_Formed}.htm`*

# SetComboStrength

## Syntax

SapObject.SapModel.DesignColdFormed.SetComboStrength

## VB6 Procedure

Function SetComboStrength(ByVal Name As String, ByVal Selected As Boolean) As Long

## Parameters

Name

The name of an existing load combination.

Selected

If this item is True, the specified load combination is selected as a design combination for cold formed strength design. If it is False, the combination is not selected for cold formed strength design.

## Remarks

This function selects or deselects a load combination for cold formed strength design.

The function returns zero if the selection status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignComboStrength()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default cold formed design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(False, False, False, True)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName)

   'select combos for cold formed strength design
      For i = 0 To NumberNames – 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignColdFormed.SetComboStrength(MyName(i), Selected)
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

[GetComboStrength](GetComboStrength_{Cold_Formed}.htm)



## SetDesignSection {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/SetDesignSection_{Cold_Formed}.htm`*

# SetDesignSection

## Syntax

SapObject.SapModel.DesignColdFormed.SetDesignSection

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

This function modifies the design section for all specified frame objects that have a cold formed frame design procedure.

The function returns zero if the design section is successfully modified; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignSection()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)
      ret = SapModel.PropFrame.SetColdC("CdC2", Name , 9, 3, 0.07, 0.25, 0.5)
      ret = SapModel.PropFrame.SetColdC("CdC3", Name , 9, 3, 0.08, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'define new auto select list frame section property
      ReDim MyName(2)
      MyName(0) = "CdC"
      MyName(1) = "CdC2"
      MyName(2) = "CdC3"
      ret = SapModel.PropFrame.SetAutoSelectColdFormed("AUTO1", 3, MyName)

   'set frame section properties
      ret = SapModel.FrameObj.SetSection("8", "AUTO1")
      ret = SapModel.FrameObj.SetSection("10", "AUTO1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start cold formed design
      ret = SapModel.DesignColdFormed.StartDesign

   'set design section
      ret = SapModel.DesignColdFormed.SetDesignSection("8", "CdC3", False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetDesignSection](GetDesignSection_{Cold_Formed}.htm)



## SetGroup {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/SetGroup_{Cold_Formed}.htm`*

# SetGroup

## Syntax

SapObject.SapModel.DesignColdFormed.SetGroup

## VB6 Procedure

Function SetGroup(ByVal Name As String, ByVal Selected As Boolean) As Long

## Parameters

Name

The name of an existing group.

Selected

If this item is True, the specified group is selected as a design group for cold formed design. If it is False, the group is not selected for cold formed design.

## Remarks

This function selects or deselects a group for cold formed design.

The function returns zero if the selection status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetColdFormedDesignGroup()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'select group for cold formed design
      ret = SapModel.DesignColdFormed.SetGroup("ALL", True)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetGroup](GetGroup_{Cold_Formed}.htm)



## StartDesign {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/StartDesign_{Cold_Formed}.htm`*

# StartDesign

## Syntax

SapObject.SapModel.DesignColdFormed.StartDesign

## VB6 Procedure

Function StartDesign() As Long

## Parameters

None

## Remarks

This function starts the cold formed frame design.

The function returns zero if the cold formed frame design is successfully started; otherwise it returns a nonzero value.

The function will fail if no cold formed frame objects are present. It will also fail if analysis results are not available.

## VBA Example

Sub StartColdFormedDesign()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start cold formed design
      ret = SapModel.DesignColdFormed.StartDesign

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## VerifyPassed {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/VerifyPassed_{Cold_Formed}.htm`*

# VerifyPassed

## Syntax

SapObject.SapModel.DesignColdFormed.VerifyPassed

## VB6 Procedure

Function VerifyPassed(ByRef NumberItems As Long, ByRef n1 As Long, ByRef n2 As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of cold formed frame objects that did not pass the design check or have not yet been checked.

n1

The number of cold formed frame objects that did not pass the design check.

n2

The number of cold formed frame objects that have not yet been checked.

MyName

This is an array that includes the name of each frame object that did not pass the design check or has not yet been checked.

## Remarks

This function retrieves the names of the frame objects that did not pass the design check or have not yet been checked, if any.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub VerifyColdFormedDesignPassed()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start cold formed design
      ret = SapModel.DesignColdFormed.StartDesign

   'verify frame objects successfully designed
      ret = SapModel.DesignColdFormed.VerifyPassed(NumberItems, n1, n2, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## VerifySections {Cold Formed}

*Source file: `SAP2000_API_Fuctions/Design/Cold_Formed/VerifySections_{Cold_Formed}.htm`*

# VerifySections

## Syntax

SapObject.SapModel.DesignColdFormed.VerifySections

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

Sub VerifyColdFormedDesignSections()
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

   'add cold formed material
      ret = SapModel.PropMaterial.AddQuick(Name, MATERIAL\_COLDFORMED, , , , MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGr50)

   'create new cold formed frame section property
      ret = SapModel.PropFrame.SetColdC("CdC", Name , 9, 3, 0.06, 0.25, 0.5)

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 72, 2, 144, True, "CdC", "CdC")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start cold formed design
      ret = SapModel.DesignColdFormed.StartDesign

   'verify analysis versus design section
      ret = SapModel.DesignColdFormed.VerifySections(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

