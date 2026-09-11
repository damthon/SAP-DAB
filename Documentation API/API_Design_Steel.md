# API Design Steel

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Design/Steel

---



## GetOverwrite {Steel AISC 360 05/IBC 2006}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360-05_IBC_2006/GetOverwrite_{Steel_AISC_360_05_IBC_2006}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_05\_IBC2006.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 43, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor

20 = Unbraced length ratio, Lateral Torsional Buckling

21 = Effective length factor, K1 Major

22 = Effective length factor, K1 Minor

23 = Effective length factor, K2 Major

24 = Effective length factor, K2 Minor

25 = Effective length factor, K Lateral Torsional Buckling

26 = Moment coefficient, Cm Major

27 = Moment coefficient, Cm Minor

28 = Bending coefficient, Cb

29 = Nonsway moment factor, B1 Major

30 = Nonsway moment factor, B1 Minor

31 = Sway moment factor, B2 Major

32 = Sway moment factor, B2 Minor

33 = Reduce HSS thickness

34 = HSS welding type

35 = Yield stress, Fy

36 = Expected to specified Fy ratio, Ry

37 = Compressive capacity, Pnc

38 = Tensile capacity, Pnt

39 = Major bending capacity, Mn3

40 = Minor bending capacity, Mn2

41 = Major shear capacity, Vn2

42 = Minor shear capacity, Vn3

43 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program default

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]}

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L}

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

20 = Unbraced length ratio, Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K1 Major

Value >= 0; 0 means use program determined value.

22 = Effective length factor, K1 Minor

Value >= 0; 0 means use program determined value.

23 = Effective length factor, K2 Major

Value >= 0; 0 means use program determined value.

24 = Effective length factor, K2 Minor

Value >= 0; 0 means use program determined value.

25 = Effective length factor, K Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

26 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

27 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

28 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

29 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

30 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

31 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

32 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

33 = Reduce HSS thickness

0 = Program default

1 = No

2 = Yes

34 = HSS welding type

0 = Program default

1 = ERW

2 = SAW

35 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

36 = Expected to specified Fy ratio, Ry

Value >= 0; 0 means use program determined value.

37 = Compressive capacity, Pnc

Value >= 0; 0 means use program determined value. [F]

38 = Tensile capacity, Pnt

Value >= 0; 0 means use program determined value. [F]

39 = Major bending capacity, Mn3

Value >= 0; 0 means use program determined value. [FL]

40 = Minor bending capacity, Mn2

Value >= 0; 0 means use program determined value. [FL]

41 = Major shear capacity, Vn2

Value >= 0; 0 means use program determined value. [F]

42 = Minor shear capacity, Vn3

Value >= 0; 0 means use program determined value. [F]

43 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAISC360\_05\_IBC2006()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC360-05/IBC2006")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.AISC360\_05\_IBC2006.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_AISC_360_05_IBC_2006}.htm)



## GetPreference {Steel AISC 360 05/IBC 2006}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360-05_IBC_2006/GetPreference_{Steel_AISC_360_05_IBC_2006}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_05\_IBC2006.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 35, inclusive, indicating
the preference item considered.

1 = Framing type

2 = Seismic design category

3 = Design provision

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

5 = Notional load coefficient

6 = Phi or Omega for bending

7 = Phi or Omega for compression

8 = Phi or Omega for tension
yielding

9 = Phi or Omega for tension
fracture

10 = Phi or Omega for
shear

11 = Phi or Omega for
shear short webbed rolled I

12 = Phi or Omega for
torsion

13 = Ignore seismic code

14 = Ignore special seismic
load

15 = Doubler plate is
plug welded

16 = HSS welding type

17 = Reduce HSS thickness

18 = Consider deflection

19 = DL deflection limit,
L/Value

20 = SDL + LL deflection
limit, L/Value

21 = LL deflection limit,
L/Value

22 = Total load deflection
limit, L/Value

23 = Total camber limit,
L/Value

24 = Pattern live load
factor

25 = Demand/capacity ratio
limit

26 = Multi-response case design

27 = Analysis Method

28 = Second Order Method

29 = Stiffness Reduction Method

30 = Importance Factor

31 = Design Systems Rho

32 = Design Systems Sds

33 = Design Systems R

34 = Design Systems Omega0

35 = Design Systems Cd

Value

The value of the considered preference item.

1 = Framing type

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Design provision

1 = LRFD

2 = ASD

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

1 = Gen 2nd Order Elastic

2 = 2nd Order By Amp
1st Order

3 = Limited 1st Order
Elastic

4 = DAM Gen 2nd Order
Taub Variable

5 = DAM Gen 2nd Order
Taub Fixed

6 = DAM Amp 1st Order
Taub Variable

7 = DAM Amp 1st Order
Taub Fixed

5 = Notional load coefficient

Value > 0

6 = Phi or Omega for bending

Value > 0

7 = Phi or Omega for compression

Value > 0

8 = Phi or Omega for tension
yielding

Value > 0

9 = Phi or Omega for tension
fracture

Value > 0

10 = Phi or Omega for
shear

Value > 0

11 = Phi or Omega for
shear short webbed rolled I

Value > 0

12 = Phi or Omega for
torsion

Value > 0

13 = Ignore seismic code

0 = No

Any other value = Yes

14 = Ignore special seismic
load

0 = No

Any other value = Yes

15 = Doubler plate is
plug welded

0 = No

Any other value = Yes

16 = HSS welding type

1 = ERW

2 = SAW

17 = Reduce HSS thickness

0 = No

Any other value = Yes

18 = Consider deflection

0 = No

Any other value = Yes

19 = DL deflection limit,
L/Value

Value > 0

20 = SDL + LL deflection
limit, L/Value

Value > 0

21 = LL deflection limit,
L/Value

Value > 0

22 = Total load deflection
limit, L/Value

Value > 0

23 = Total camber limit,
L/Value

Value > 0

24 = Pattern live load
factor

Value >= 0

25 = Demand/capacity ratio
limit

Value > 0

26 = Multi-response case
design

  1 = Envelopes

  2 = Step-by-step

  3 = Last
step

  4 = Envelopes
-- All

  5 = Step-by-step
-- All

27 = Analysis Method

1 = Direct Analysis

2 = Effective Length

3 = Limited 1st Order

28 = Second Order Method

1 = General 2nd Order

2 = Amplified 1st Order

29 = Stiffness Reduction
Method

1 = Tau-b variable

2 = Tau-b Fixed

3 = No Modification

30 = Importance Factor

Value > 0

31 = Design System Rho

Value > 0

32 = Design System Sds

Value >= 0

33 = Design System R

Value > 0

34 = Design System Omega0

Value > 0

35 = Design System Cd

Value > 0

## Remarks

This function retrieves the value of a steel design
preference item.

The function returns zero if the item is successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemAISC360\_05\_IBC2006()
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
      ret = SapModel.DesignSteel.SetCode("AISC360-05/IBC2006")

   'get preference item
      ret = SapModel.DesignSteel.AISC360\_05\_IBC2006.GetPreference(1,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added items 27, 28, and 29, and noted Item 4 is obsolete
in Version 12.00.

Changed Time history design item to Multi-response case
design and added additional values in version 15.0.1.

Added items 30 through 35 in v17.3.0.

v23.2.0
- modified items 6 through 12 to allow phi or omega, depending on the
design provision value (item 3).

## See Also

[SetPreference](SetPreference_{Steel_AISC_360_05_IBC_2006}.htm)



## SetOverwrite {Steel AISC 360 05/IBC 2006}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360-05_IBC_2006/SetOverwrite_{Steel_AISC_360_05_IBC_2006}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_05\_IBC2006.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 43, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor

20 = Unbraced length ratio, Lateral Torsional Buckling

21 = Effective length factor, K1 Major

22 = Effective length factor, K1 Minor

23 = Effective length factor, K2 Major

24 = Effective length factor, K2 Minor

25 = Effective length factor, K Lateral Torsional Buckling

26 = Moment coefficient, Cm Major

27 = Moment coefficient, Cm Minor

28 = Bending coefficient, Cb

29 = Nonsway moment factor, B1 Major

30 = Nonsway moment factor, B1 Minor

31 = Sway moment factor, B2 Major

32 = Sway moment factor, B2 Minor

33 = Reduce HSS thickness

34 = HSS welding type

35 = Yield stress, Fy

36 = Expected to specified Fy ratio, Ry

37 = Compressive capacity, Pnc

38 = Tensile capacity, Pnt

39 = Major bending capacity, Mn3

40 = Minor bending capacity, Mn2

41 = Major shear capacity, Vn2

42 = Minor shear capacity, Vn3

43 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program default

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]}

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L}

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

20 = Unbraced length ratio, Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K1 Major

Value >= 0; 0 means use program determined value.

22 = Effective length factor, K1 Minor

Value >= 0; 0 means use program determined value.

23 = Effective length factor, K2 Major

Value >= 0; 0 means use program determined value.

24 = Effective length factor, K2 Minor

Value >= 0; 0 means use program determined value.

25 = Effective length factor, K Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

26 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

27 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

28 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

29 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

30 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

31 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

32 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

33 = Reduce HSS thickness

0 = Program default

1 = No

2 = Yes

34 = HSS welding type

0 = Program default

1 = ERW

2 = SAW

35 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

36 = Expected to specified Fy ratio, Ry

Value >= 0; 0 means use program determined value.

37 = Compressive capacity, Pnc

Value >= 0; 0 means use program determined value. [F]

38 = Tensile capacity, Pnt

Value >= 0; 0 means use program determined value. [F]

39 = Major bending capacity, Mn3

Value >= 0; 0 means use program determined value. [FL]

40 = Minor bending capacity, Mn2

Value >= 0; 0 means use program determined value. [FL]

41 = Major shear capacity, Vn2

Value >= 0; 0 means use program determined value. [F]

42 = Minor shear capacity, Vn3

Value >= 0; 0 means use program determined value. [F]

43 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAISC360\_05\_IBC2006()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC360-05/IBC2006")

   'set overwrite item
      ret = SapModel.DesignSteel.AISC360\_05\_IBC2006.SetOverwrite("8", 1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_AISC_360_05_IBC_2006}.htm)



## SetPreference {Steel AISC 360 05/IBC 2006}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360-05_IBC_2006/SetPreference_{Steel_AISC_360_05_IBC_2006}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_05\_IBC2006.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 35, inclusive, indicating
the preference item considered.

1 = Framing type

2 = Seismic design category

3 = Design provision

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

5 = Notional load coefficient

6 = Phi or Omega for bending

7 = Phi or Omega for compression

8 = Phi or Omega for tension
yielding

9 = Phi or Omega for tension
fracture

10 = Phi or Omega for
shear

11 = Phi or Omega for
shear short webbed rolled I

12 = Phi or Omega for
torsion

13 = Ignore seismic code

14 = Ignore special seismic
load

15 = Doubler plate is
plug welded

16 = HSS welding type

17 = Reduce HSS thickness

18 = Consider deflection

19 = DL deflection limit,
L/Value

20 = SDL + LL deflection
limit, L/Value

21 = LL deflection limit,
L/Value

22 = Total load deflection
limit, L/Value

23 = Total camber limit,
L/Value

24 = Pattern live load
factor

25 = Demand/capacity ratio
limit

26 = Multi-response case design
27 = Analysis Method
28 = Second Order Method
29 = Stiffness Reduction Method

30 = Importance Factor

31 = Design Systems Rho

32 = Design Systems Sds

33 = Design Systems R

34 = Design Systems Omega0

35 = Design Systems Cd

Value

The value of the considered preference item.

1 = Framing type

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Design provision

1 = LRFD

2 = ASD

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

1 = Gen 2nd Order Elastic

2 = 2nd Order By Amp
1st Order

3 = Limited 1st Order
Elastic

4 = DAM Gen 2nd Order
Taub Variable

5 = DAM Gen 2nd Order
Taub Fixed

6 = DAM Amp 1st Order
Taub Variable

7 = DAM Amp 1st Order
Taub Fixed

5 = Notional load coefficient

Value > 0

6 = Phi or Omega for bending

Value > 0

7 = Phi or Omega for compression

Value > 0

8 = Phi or Omega for tension
yielding

Value > 0

9 = Phi or Omega for tension
fracture

Value > 0

10 = Phi or Omega for
shear

Value > 0

11 = Phi or Omega for
shear short webbed rolled I

Value > 0

12 = Phi or Omega for
torsion

Value > 0

13 = Ignore seismic code

0 = No

Any other value = Yes

14 = Ignore special seismic
load

0 = No

Any other value = Yes

15 = Doubler plate is
plug welded

0 = No

Any other value = Yes

16 = HSS welding type

1 = ERW

2 = SAW

17 = Reduce HSS thickness

0 = No

Any other value = Yes

18 = Consider deflection

0 = No

Any other value = Yes

19 = DL deflection limit,
L/Value

Value > 0

20 = SDL + LL deflection
limit, L/Value

Value > 0

21 = LL deflection limit,
L/Value

Value > 0

22 = Total load deflection
limit, L/Value

Value > 0

23 = Total camber limit,
L/Value

Value > 0

24 = Pattern live load
factor

Value >= 0

25 = Demand/capacity ratio
limit

Value > 0

26 = Multi-response case
design

  1 = Envelopes

  2 = Step-by-step

  3 = Last
step

  4 = Envelopes
-- All

  5 = Step-by-step
-- All

27 =  Analysis Method

1 = Direct Analysis

2 = Effective Length

3 = Limited 1st Order

28 =  Second Order
Method

1 = General 2nd Order

2 = Amplified 1st Order

29 =  Stiffness Reduction
Method

1 = Tau-b variable

2 = Tau-b Fixed

3 = No Modification

30 = Importance Factor

Value > 0

31 = Design System Rho

Value > 0

32 = Design System Sds

Value >= 0

33 = Design System R

Value > 0

34 = Design System Omega0

Value > 0

35 = Design System Cd

Value > 0

## Remarks

This function sets the value of a steel design preference
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAISC360\_05\_IBC2006()
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
      ret = SapModel.DesignSteel.SetCode("AISC360-05/IBC2006")

   'set preference item
      ret = SapModel.DesignSteel.AISC360\_05\_IBC2006.SetPreference(1,
7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Added items 27, 28, and 29, and noted Item 4 is obsolete
in Version 12.00.

Changed Time history design item to Multi-response case
design and added additional values in version 15.0.1.

Added items 30 through 35 in v17.3.0.

v23.2.0
- modified items 6 through 12 to allow phi or omega, depending on the
design provision value (item 3).

## See Also

[GetPreference](GetPreference_{Steel_AISC_360_05_IBC_2006}.htm)



## GetOverwrite {Steel AISC 360-10}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360_10/GetOverwrite_{Steel_AISC360_10}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_10.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 43, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor

20 = Unbraced length ratio, Lateral Torsional Buckling

21 = Effective length factor, K1 Major

22 = Effective length factor, K1 Minor

23 = Effective length factor, K2 Major

24 = Effective length factor, K2 Minor

25 = Effective length factor, K Lateral Torsional Buckling

26 = Moment coefficient, Cm Major

27 = Moment coefficient, Cm Minor

28 = Bending coefficient, Cb

29 = Nonsway moment factor, B1 Major

30 = Nonsway moment factor, B1 Minor

31 = Sway moment factor, B2 Major

32 = Sway moment factor, B2 Minor

33 = Reduce HSS thickness

34 = HSS welding type

35 = Yield stress, Fy

36 = Expected to specified Fy ratio, Ry

37 = Compressive capacity, Pnc

38 = Tensile capacity, Pnt

39 = Major bending capacity, Mn3

40 = Minor bending capacity, Mn2

41 = Major shear capacity, Vn2

42 = Minor shear capacity, Vn3

43 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program default

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]}

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L}

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

20 = Unbraced length ratio, Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K1 Major

Value >= 0; 0 means use program determined value.

22 = Effective length factor, K1 Minor

Value >= 0; 0 means use program determined value.

23 = Effective length factor, K2 Major

Value >= 0; 0 means use program determined value.

24 = Effective length factor, K2 Minor

Value >= 0; 0 means use program determined value.

25 = Effective length factor, K Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

26 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

27 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

28 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

29 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

30 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

31 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

32 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

33 = Reduce HSS thickness

0 = Program default

1 = No

2 = Yes

34 = HSS welding type

0 = Program default

1 = ERW

2 = SAW

35 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

36 = Expected to specified Fy ratio, Ry

Value >= 0; 0 means use program determined value.

37 = Compressive capacity, Pnc

Value >= 0; 0 means use program determined value. [F]

38 = Tensile capacity, Pnt

Value >= 0; 0 means use program determined value. [F]

39 = Major bending capacity, Mn3

Value >= 0; 0 means use program determined value. [FL]

40 = Minor bending capacity, Mn2

Value >= 0; 0 means use program determined value. [FL]

41 = Major shear capacity, Vn2

Value >= 0; 0 means use program determined value. [F]

42 = Minor shear capacity, Vn3

Value >= 0; 0 means use program determined value. [F]

43 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAISC360\_10()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC360-10")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.AISC360\_10.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also

[SetOverwrite](SetOverwrite_{Steel_AISC_360-10}.htm)



## GetPreference {Steel AISC 360-10}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360_10/GetPreference_{Steel_AISC_360-10}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_10.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 35, inclusive, indicating
the preference item considered.

1 = Framing type

2 = Seismic design category

3 = Design provision

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

5 = Notional load coefficient

6 = Phi or Omega for bending

7 = Phi or Omega for compression

8 = Phi or Omega for tension
yielding

9 = Phi or Omega for tension
fracture

10 = Phi or Omega for
shear

11 = Phi or Omega for
shear short webbed rolled I

12 = Phi or Omega for
torsion

13 = Ignore seismic code

14 = Ignore special seismic
load

15 = Doubler plate is
plug welded

16 = HSS welding type

17 = Reduce HSS thickness

18 = Consider deflection

19 = DL deflection limit,
L/Value

20 = SDL + LL deflection
limit, L/Value

21 = LL deflection limit,
L/Value

22 = Total load deflection
limit, L/Value

23 = Total camber limit,
L/Value

24 = Pattern live load
factor

25 = Demand/capacity ratio
limit

26 = Multi-response case design

27 = Analysis Method

28 = Second Order Method

29 = Stiffness Reduction Method

30 = Importance Factor

31 = Design Systems Rho

32 = Design Systems Sds

33 = Design Systems R

34 = Design Systems Omega0

35 = Design Systems Cd

Value

The value of the considered preference item.

1 = Framing type

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Design provision

1 = LRFD

2 = ASD

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

1 = Gen 2nd Order Elastic

2 = 2nd Order By Amp
1st Order

3 = Limited 1st Order
Elastic

4 = DAM Gen 2nd Order
Taub Variable

5 = DAM Gen 2nd Order
Taub Fixed

6 = DAM Amp 1st Order
Taub Variable

7 = DAM Amp 1st Order
Taub Fixed

5 = Notional load coefficient

Value > 0

6 = Phi or Omega for bending

Value > 0

7 = Phi or Omega for compression

Value > 0

8 = Phi or Omega for tension
yielding

Value > 0

9 = Phi or Omega for tension
fracture

Value > 0

10 = Phi or Omega for
shear

Value > 0

11 = Phi or Omega for
shear short webbed rolled I

Value > 0

12 = Phi or Omega for
torsion

Value > 0

13 = Ignore seismic code

0 = No

Any other value = Yes

14 = Ignore special seismic
load

0 = No

Any other value = Yes

15 = Doubler plate is
plug welded

0 = No

Any other value = Yes

16 = HSS welding type

1 = ERW

2 = SAW

17 = Reduce HSS thickness

0 = No

Any other value = Yes

18 = Consider deflection

0 = No

Any other value = Yes

19 = DL deflection limit,
L/Value

Value > 0

20 = SDL + LL deflection
limit, L/Value

Value > 0

21 = LL deflection limit,
L/Value

Value > 0

22 = Total load deflection
limit, L/Value

Value > 0

23 = Total camber limit,
L/Value

Value > 0

24 = Pattern live load
factor

Value >= 0

25 = Demand/capacity ratio
limit

Value > 0

26 = Multi-response case
design

  1 = Envelopes

  2 = Step-by-step

  3 = Last
step

  4 = Envelopes
-- All

  5 = Step-by-step
-- All

27 = Analysis Method

1 = Direct Analysis

2 = Effective Length

3 = Limited 1st Order

28 = Second Order Method

1 = General 2nd Order

2 = Amplified 1st Order

29 = Stiffness Reduction
Method

1 = Tau-b variable

2 = Tau-b Fixed

3 = No Modification

30 = Importance Factor

Value > 0

31 = Design System Rho

Value > 0

32 = Design System Sds

Value >= 0

33 = Design System R

Value > 0

34 = Design System Omega0

Value > 0

35 = Design System Cd

Value > 0

## Remarks

This function retrieves the value of a steel design
preference item.

The function returns zero if the item is successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemAISC360\_10()
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
      ret = SapModel.DesignSteel.SetCode("AISC360-10")

   'get preference item
      ret = SapModel.DesignSteel.AISC360\_10.GetPreference(1,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 16.0.0.

Added items 30 through 35 in v17.3.0.

v23.2.0
- modified items 6 through 12 to allow phi or omega, depending on the
design provision value (item 3).

## See Also

[SetPreference](SetPreference_{Steel_AISC_360-10}.htm)



## SetOverwrite {Steel AISC 360-10}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360_10/SetOverwrite_{Steel_AISC_360-10}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_10.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending
on the value of the ItemType item.

Item

This is an integer between 1 and 43, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit,
L/Value

6 = SDL + LL deflection
limit, L/Value

7 = LL deflection limit,
L/Value

8 = Total load deflection
limit, L/Value

9 = Total camber limit,
L/Value

10 = DL deflection limit,
absolute

11 = SDL + LL deflection
limit, absolute

12 = LL deflection limit,
absolute

13 = Total load deflection
limit, absolute

14 = Total camber limit,
absolute

15 = Specified camber

16 = Net area to total
area ratio

17 = Live load reduction
factor

18 = Unbraced length ratio,
Major

19 = Unbraced length ratio,
Minor

20 = Unbraced length ratio,
Lateral Torsional Buckling

21 = Effective length
factor, K1 Major

22 = Effective length
factor, K1 Minor

23 = Effective length
factor, K2 Major

24 = Effective length
factor, K2 Minor

25 = Effective length
factor, K Lateral Torsional Buckling

26 = Moment coefficient,
Cm Major

27 = Moment coefficient,
Cm Minor

28 = Bending coefficient,
Cb

29 = Nonsway moment factor,
B1 Major

30 = Nonsway moment factor,
B1 Minor

31 = Sway moment factor,
B2 Major

32 = Sway moment factor,
B2 Minor

33 = Reduce HSS thickness

34 = HSS welding type

35 = Yield stress, Fy

36 = Expected to specified
Fy ratio, Ry

37 = Compressive capacity,
Pnc

38 = Tensile capacity,
Pnt

39 = Major bending capacity,
Mn3

40 = Minor bending capacity,
Mn2

41 = Major shear capacity,
Vn2

42 = Minor shear capacity,
Vn3

43 = Demand/capacity ratio
limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Omega0

Value >= 0; 0 means
use a program determined value.

3 = Consider deflection

0 = Program default

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

6 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

7 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

8 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

9 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

10 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

11 = SDL + LL deflection
limit, absolute

Value >= 0; 0 means
no check for this item. [L]

12 = LL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

13 = Total load deflection
limit, absolute

Value >= 0; 0 means
no check for this item. [L]}

14 = Total camber limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

15 = Specified camber

Value >= 0. [L}

16 = Net area to total
area ratio

Value >= 0; 0 means
use program default value.

17 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

18 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value.

19 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value.

20 = Unbraced length ratio,
Lateral Torsional Buckling

Value >= 0; 0 means
use program determined value.

21 = Effective length
factor, K1 Major

Value >= 0; 0 means
use program determined value.

22 = Effective length
factor, K1 Minor

Value >= 0; 0 means
use program determined value.

23 = Effective length
factor, K2 Major

Value >= 0; 0 means
use program determined value.

24 = Effective length
factor, K2 Minor

Value >= 0; 0 means
use program determined value.

25 = Effective length
factor, K Lateral Torsional Buckling

Value >= 0; 0 means
use program determined value.

26 = Moment coefficient,
Cm Major

Value >= 0; 0 means
use program determined value.

27 = Moment coefficient,
Cm Minor

Value >= 0; 0 means
use program determined value.

28 = Bending coefficient,
Cb

Value >= 0; 0 means
use program determined value.

29 = Nonsway moment factor,
B1 Major

Value >= 0; 0 means
use program determined value.

30 = Nonsway moment factor,
B1 Minor

Value >= 0; 0 means
use program determined value.

31 = Sway moment factor,
B2 Major

Value >= 0; 0 means
use program determined value.

32 = Sway moment factor,
B2 Minor

Value >= 0; 0 means
use program determined value.

33 = Reduce HSS thickness

0 = Program default

1 = No

2 = Yes

34 = HSS welding type

0 = Program default

1 = ERW

2 = SAW

35 = Yield stress, Fy

Value >= 0; 0 means
use program determined value. [F/L2]

36 = Expected to specified
Fy ratio, Ry

Value >= 0; 0 means
use program determined value.

37 = Compressive capacity,
Pnc

Value >= 0; 0 means
use program determined value. [F]

38 = Tensile capacity,
Pnt

Value >= 0; 0 means
use program determined value. [F]

39 = Major bending capacity,
Mn3

Value >= 0; 0 means
use program determined value. [FL]

40 = Minor bending capacity,
Mn2

Value >= 0; 0 means
use program determined value. [FL]

41 = Major shear capacity,
Vn2

Value >= 0; 0 means
use program determined value. [F]

42 = Minor shear capacity,
Vn3

Value >= 0; 0 means
use program determined value. [F]

43 = Demand/capacity ratio
limit

Value >= 0; 0 means use
program determined value.

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

## Remarks

This function sets the value of a steel design overwrite
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAISC360\_10()
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
      ret = SapModel.DesignSteel.SetCode("AISC360-10")

   'set overwrite item
      ret = SapModel.DesignSteel.AISC360\_10.SetOverwrite("8",
1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 16.0.0.

## See Also

[GetOverwrite](GetOverwrite_{Steel_AISC360_10}.htm)



## SetPreference {Steel AISC 360-10}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360_10/SetPreference_{Steel_AISC_360-10}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_10.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 35, inclusive, indicating
the preference item considered.

1 = Framing type

2 = Seismic design category

3 = Design provision

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

5 = Notional load coefficient

6 = Phi or Omega for bending

7 = Phi or Omega for compression

8 = Phi or Omega for tension
yielding

9 = Phi or Omega for tension
fracture

10 = Phi or Omega for
shear

11 = Phi or Omega for
shear short webbed rolled I

12 = Phi or Omega for
torsion

13 = Ignore seismic code

14 = Ignore special seismic
load

15 = Doubler plate is
plug welded

16 = HSS welding type

17 = Reduce HSS thickness

18 = Consider deflection

19 = DL deflection limit,
L/Value

20 = SDL + LL deflection
limit, L/Value

21 = LL deflection limit,
L/Value

22 = Total load deflection
limit, L/Value

23 = Total camber limit,
L/Value

24 = Pattern live load
factor

25 = Demand/capacity ratio
limit

26 = Multi-response case design
27 = Analysis Method
28 = Second Order Method
29 = Stiffness Reduction Method

30 = Importance Factor

31 = Design Systems Rho

32 = Design Systems Sds

33 = Design Systems R

34 = Design Systems Omega0

35 = Design Systems Cd

Value

The value of the considered preference item.

1 = Framing type

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Design provision

1 = LRFD

2 = ASD

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

1 = Gen 2nd Order Elastic

2 = 2nd Order By Amp
1st Order

3 = Limited 1st Order
Elastic

4 = DAM Gen 2nd Order
Taub Variable

5 = DAM Gen 2nd Order
Taub Fixed

6 = DAM Amp 1st Order
Taub Variable

7 = DAM Amp 1st Order
Taub Fixed

5 = Notional load coefficient

Value > 0

6 = Phi or Omega for bending

Value > 0

7 = Phi or Omega for compression

Value > 0

8 = Phi or Omega for tension
yielding

Value > 0

9 = Phi or Omega for tension
fracture

Value > 0

10 = Phi or Omega for
shear

Value > 0

11 = Phi or Omega for
shear short webbed rolled I

Value > 0

12 = Phi or Omega for
torsion

Value > 0

13 = Ignore seismic code

0 = No

Any other value = Yes

14 = Ignore special seismic
load

0 = No

Any other value = Yes

15 = Doubler plate is
plug welded

0 = No

Any other value = Yes

16 = HSS welding type

1 = ERW

2 = SAW

17 = Reduce HSS thickness

0 = No

Any other value = Yes

18 = Consider deflection

0 = No

Any other value = Yes

19 = DL deflection limit,
L/Value

Value > 0

20 = SDL + LL deflection
limit, L/Value

Value > 0

21 = LL deflection limit,
L/Value

Value > 0

22 = Total load deflection
limit, L/Value

Value > 0

23 = Total camber limit,
L/Value

Value > 0

24 = Pattern live load
factor

Value >= 0

25 = Demand/capacity ratio
limit

Value > 0

26 = Multi-response case
design

  1 = Envelopes

  2 = Step-by-step

  3 = Last
step

  4 = Envelopes
-- All

  5 = Step-by-step
-- All

27 =  Analysis Method

1 = Direct Analysis

2 = Effective Length

3 = Limited 1st Order

28 =  Second Order
Method

1 = General 2nd Order

2 = Amplified 1st Order

29 =  Stiffness Reduction
Method

1 = Tau-b variable

2 = Tau-b Fixed

3 = No Modification

30 = Importance Factor

Value > 0

31 = Design System Rho

Value > 0

32 = Design System Sds

Value >= 0

33 = Design System R

Value > 0

34 = Design System Omega0

Value > 0

35 = Design System Cd

Value > 0

## Remarks

This function sets the value of a steel design preference
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAISC360\_10()
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
      ret = SapModel.DesignSteel.SetCode("AISC360-10")

   'set preference item
      ret = SapModel.DesignSteel.AISC360\_10.SetPreference(1,
7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 16.0.0.

Added items 30 through 35 in v17.3.0.

v23.2.0
- modified items 6 through 12 to allow phi or omega, depending on the
design provision value (item 3).

## See Also

[GetPreference](GetPreference_{Steel_AISC_360-10}.htm)



## GetOverwrite {AISC 360-16}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360_16/GetOverwrite_{AISC_360-16}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_16.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design
procedure.

Item

This is an integer between 1 and 43, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit,
L/Value

6 = SDL + LL deflection
limit, L/Value

7 = LL deflection limit,
L/Value

8 = Total load deflection
limit, L/Value

9 = Total camber limit,
L/Value

10 = DL deflection limit,
absolute

11 = SDL + LL deflection
limit, absolute

12 = LL deflection limit,
absolute

13 = Total load deflection
limit, absolute

14 = Total camber limit,
absolute

15 = Specified camber

16 = Net area to total
area ratio

17 = Live load reduction
factor

18 = Unbraced length ratio,
Major

19 = Unbraced length ratio,
Minor

20 = Unbraced length ratio,
Lateral Torsional Buckling

21 = Effective length
factor, K1 Major

22 = Effective length
factor, K1 Minor

23 = Effective length
factor, K2 Major

24 = Effective length
factor, K2 Minor

25 = Effective length
factor, K Lateral Torsional Buckling

26 = Moment coefficient,
Cm Major

27 = Moment coefficient,
Cm Minor

28 = Bending coefficient,
Cb

29 = Nonsway moment factor,
B1 Major

30 = Nonsway moment factor,
B1 Minor

31 = Sway moment factor,
B2 Major

32 = Sway moment factor,
B2 Minor

33 = Reduce HSS thickness

34 = HSS welding type

35 = Yield stress, Fy

36 = Expected to specified
Fy ratio, Ry

37 = Compressive capacity,
Pnc

38 = Tensile capacity,
Pnt

39 = Major bending capacity,
Mn3

40 = Minor bending capacity,
Mn2

41 = Major shear capacity,
Vn2

42 = Minor shear capacity,
Vn3

43 = Demand/capacity ratio
limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Omega0

Value >= 0; 0 means
use a program determined value.

3 = Consider deflection

0 = Program default

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

6 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

7 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

8 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

9 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

10 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

11 = SDL + LL deflection
limit, absolute

Value >= 0; 0 means
no check for this item. [L]

12 = LL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

13 = Total load deflection
limit, absolute

Value >= 0; 0 means
no check for this item. [L]}

14 = Total camber limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

15 = Specified camber

Value >= 0. [L}

16 = Net area to total
area ratio

Value >= 0; 0 means
use program default value.

17 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

18 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value.

19 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value.

20 = Unbraced length ratio,
Lateral Torsional Buckling

Value >= 0; 0 means
use program determined value.

21 = Effective length
factor, K1 Major

Value >= 0; 0 means
use program determined value.

22 = Effective length
factor, K1 Minor

Value >= 0; 0 means
use program determined value.

23 = Effective length
factor, K2 Major

Value >= 0; 0 means
use program determined value.

24 = Effective length
factor, K2 Minor

Value >= 0; 0 means
use program determined value.

25 = Effective length
factor, K Lateral Torsional Buckling

Value >= 0; 0 means
use program determined value.

26 = Moment coefficient,
Cm Major

Value >= 0; 0 means
use program determined value.

27 = Moment coefficient,
Cm Minor

Value >= 0; 0 means
use program determined value.

28 = Bending coefficient,
Cb

Value >= 0; 0 means
use program determined value.

29 = Nonsway moment factor,
B1 Major

Value >= 0; 0 means
use program determined value.

30 = Nonsway moment factor,
B1 Minor

Value >= 0; 0 means
use program determined value.

31 = Sway moment factor,
B2 Major

Value >= 0; 0 means
use program determined value.

32 = Sway moment factor,
B2 Minor

Value >= 0; 0 means
use program determined value.

33 = Reduce HSS thickness

0 = Program default

1 = No

2 = Yes

34 = HSS welding type

0 = Program default

1 = ERW

2 = SAW

35 = Yield stress, Fy

Value >= 0; 0 means
use program determined value. [F/L2]

36 = Expected to specified
Fy ratio, Ry

Value >= 0; 0 means
use program determined value.

37 = Compressive capacity,
Pnc

Value >= 0; 0 means
use program determined value. [F]

38 = Tensile capacity,
Pnt

Value >= 0; 0 means
use program determined value. [F]

39 = Major bending capacity,
Mn3

Value >= 0; 0 means
use program determined value. [FL]

40 = Minor bending capacity,
Mn2

Value >= 0; 0 means
use program determined value. [FL]

41 = Major shear capacity,
Vn2

Value >= 0; 0 means
use program determined value. [F]

42 = Minor shear capacity,
Vn3

Value >= 0; 0 means
use program determined value. [F]

43 = Demand/capacity ratio
limit

Value >= 0; 0 means use
program determined value.

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a steel design
overwrite item.

The function returns zero if the item is successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAISC360\_16()
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
      ret = SapModel.DesignSteel.SetCode("AISC360-16")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.AISC360\_16.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.0.0.

## See Also

[SetOverwrite](SetOverwrite_{AISC360-16}.htm)



## GetPreferences {AISC 360-16}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360_16/GetPreferences_{AISC_360-16}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_16.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 35, inclusive, indicating
the preference item considered.

1 = Framing type

2 = Seismic design category

3 = Design provision

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

5 = Notional load coefficient

6 = Phi or Omega for bending

7 = Phi or Omega for compression

8 = Phi or Omega for tension
yielding

9 = Phi or Omega for tension
fracture

10 = Phi or Omega for
shear

11 = Phi or Omega for
shear short webbed rolled I

12 = Phi or Omega for
torsion

13 = Ignore seismic code

14 = Ignore special seismic
load

15 = Doubler plate is
plug welded

16 = HSS welding type

17 = Reduce HSS thickness

18 = Consider deflection

19 = DL deflection limit,
L/Value

20 = SDL + LL deflection
limit, L/Value

21 = LL deflection limit,
L/Value

22 = Total load deflection
limit, L/Value

23 = Total camber limit,
L/Value

24 = Pattern live load
factor

25 = Demand/capacity ratio
limit

26 = Multi-response case design

27 = Analysis Method

28 = Second Order Method

29 = Stiffness Reduction Method

30 = Importance Factor

31 = Design Systems Rho

32 = Design Systems Sds

33 = Design Systems R

34 = Design Systems Omega0

35 = Design Systems Cd

Value

The value of the considered preference item.

1 = Framing type

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Design provision

1 = LRFD

2 = ASD

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

1 = Gen 2nd Order Elastic

2 = 2nd Order By Amp
1st Order

3 = Limited 1st Order
Elastic

4 = DAM Gen 2nd Order
Taub Variable

5 = DAM Gen 2nd Order
Taub Fixed

6 = DAM Amp 1st Order
Taub Variable

7 = DAM Amp 1st Order
Taub Fixed

5 = Notional load coefficient

Value > 0

6 = Phi or Omega for bending

Value > 0

7 = Phi or Omega for compression

Value > 0

8 = Phi or Omega for tension
yielding

Value > 0

9 = Phi or Omega for tension
fracture

Value > 0

10 = Phi or Omega for
shear

Value > 0

11 = Phi or Omega for
shear short webbed rolled I

Value > 0

12 = Phi or Omega for
torsion

Value > 0

13 = Ignore seismic code

0 = No

Any other value = Yes

14 = Ignore special seismic
load

0 = No

Any other value = Yes

15 = Doubler plate is
plug welded

0 = No

Any other value = Yes

16 = HSS welding type

1 = ERW

2 = SAW

17 = Reduce HSS thickness

0 = No

Any other value = Yes

18 = Consider deflection

0 = No

Any other value = Yes

19 = DL deflection limit,
L/Value

Value > 0

20 = SDL + LL deflection
limit, L/Value

Value > 0

21 = LL deflection limit,
L/Value

Value > 0

22 = Total load deflection
limit, L/Value

Value > 0

23 = Total camber limit,
L/Value

Value > 0

24 = Pattern live load
factor

Value >= 0

25 = Demand/capacity ratio
limit

Value > 0

26 = Multi-response case
design

  1 = Envelopes

  2 = Step-by-step

  3 = Last
step

  4 = Envelopes
-- All

  5 = Step-by-step
-- All

27 = Analysis Method

1 = Direct Analysis

2 = Effective Length

3 = Limited 1st Order

28 = Second Order Method

1 = General 2nd Order

2 = Amplified 1st Order

29 = Stiffness Reduction
Method

1 = Tau-b variable

2 = Tau-b Fixed

3 = No Modification

30 = Importance Factor

Value > 0

31 = Design System Rho

Value > 0

32 = Design System Sds

Value >= 0

33 = Design System R

Value > 0

34 = Design System Omega0

Value > 0

35 = Design System Cd

Value > 0

## Remarks

This function retrieves the value of a steel design
preference item.

The function returns zero if the item is successfully
retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemAISC360\_16()
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
      ret = SapModel.DesignSteel.SetCode("AISC360-16")

   'get preference item
      ret = SapModel.DesignSteel.AISC360\_16.GetPreference(1,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version v20.0.0

v23.2.0
- modified items 6 through 12 to allow phi or omega, depending on the
design provision value (item 3).

## See Also

[SetPreference](SetPreferences_{AISC_360-16}.htm)



## SetOverwrite {AISC360-16}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360_16/SetOverwrite_{AISC360-16}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_16.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending
on the value of the ItemType item.

Item

This is an integer between 1 and 43, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit,
L/Value

6 = SDL + LL deflection
limit, L/Value

7 = LL deflection limit,
L/Value

8 = Total load deflection
limit, L/Value

9 = Total camber limit,
L/Value

10 = DL deflection limit,
absolute

11 = SDL + LL deflection
limit, absolute

12 = LL deflection limit,
absolute

13 = Total load deflection
limit, absolute

14 = Total camber limit,
absolute

15 = Specified camber

16 = Net area to total
area ratio

17 = Live load reduction
factor

18 = Unbraced length ratio,
Major

19 = Unbraced length ratio,
Minor

20 = Unbraced length ratio,
Lateral Torsional Buckling

21 = Effective length
factor, K1 Major

22 = Effective length
factor, K1 Minor

23 = Effective length
factor, K2 Major

24 = Effective length
factor, K2 Minor

25 = Effective length
factor, K Lateral Torsional Buckling

26 = Moment coefficient,
Cm Major

27 = Moment coefficient,
Cm Minor

28 = Bending coefficient,
Cb

29 = Nonsway moment factor,
B1 Major

30 = Nonsway moment factor,
B1 Minor

31 = Sway moment factor,
B2 Major

32 = Sway moment factor,
B2 Minor

33 = Reduce HSS thickness

34 = HSS welding type

35 = Yield stress, Fy

36 = Expected to specified
Fy ratio, Ry

37 = Compressive capacity,
Pnc

38 = Tensile capacity,
Pnt

39 = Major bending capacity,
Mn3

40 = Minor bending capacity,
Mn2

41 = Major shear capacity,
Vn2

42 = Minor shear capacity,
Vn3

43 = Demand/capacity ratio
limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Omega0

Value >= 0; 0 means
use a program determined value.

3 = Consider deflection

0 = Program default

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

6 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

7 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

8 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

9 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

10 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

11 = SDL + LL deflection
limit, absolute

Value >= 0; 0 means
no check for this item. [L]

12 = LL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

13 = Total load deflection
limit, absolute

Value >= 0; 0 means
no check for this item. [L]}

14 = Total camber limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

15 = Specified camber

Value >= 0. [L}

16 = Net area to total
area ratio

Value >= 0; 0 means
use program default value.

17 = Live load reduction
factor

Value >= 0; 0 means
use program determined value.

18 = Unbraced length ratio,
Major

Value >= 0; 0 means
use program determined value.

19 = Unbraced length ratio,
Minor

Value >= 0; 0 means
use program determined value.

20 = Unbraced length ratio,
Lateral Torsional Buckling

Value >= 0; 0 means
use program determined value.

21 = Effective length
factor, K1 Major

Value >= 0; 0 means
use program determined value.

22 = Effective length
factor, K1 Minor

Value >= 0; 0 means
use program determined value.

23 = Effective length
factor, K2 Major

Value >= 0; 0 means
use program determined value.

24 = Effective length
factor, K2 Minor

Value >= 0; 0 means
use program determined value.

25 = Effective length
factor, K Lateral Torsional Buckling

Value >= 0; 0 means
use program determined value.

26 = Moment coefficient,
Cm Major

Value >= 0; 0 means
use program determined value.

27 = Moment coefficient,
Cm Minor

Value >= 0; 0 means
use program determined value.

28 = Bending coefficient,
Cb

Value >= 0; 0 means
use program determined value.

29 = Nonsway moment factor,
B1 Major

Value >= 0; 0 means
use program determined value.

30 = Nonsway moment factor,
B1 Minor

Value >= 0; 0 means
use program determined value.

31 = Sway moment factor,
B2 Major

Value >= 0; 0 means
use program determined value.

32 = Sway moment factor,
B2 Minor

Value >= 0; 0 means
use program determined value.

33 = Reduce HSS thickness

0 = Program default

1 = No

2 = Yes

34 = HSS welding type

0 = Program default

1 = ERW

2 = SAW

35 = Yield stress, Fy

Value >= 0; 0 means
use program determined value. [F/L2]

36 = Expected to specified
Fy ratio, Ry

Value >= 0; 0 means
use program determined value.

37 = Compressive capacity,
Pnc

Value >= 0; 0 means
use program determined value. [F]

38 = Tensile capacity,
Pnt

Value >= 0; 0 means
use program determined value. [F]

39 = Major bending capacity,
Mn3

Value >= 0; 0 means
use program determined value. [FL]

40 = Minor bending capacity,
Mn2

Value >= 0; 0 means
use program determined value. [FL]

41 = Major shear capacity,
Vn2

Value >= 0; 0 means
use program determined value. [F]

42 = Minor shear capacity,
Vn3

Value >= 0; 0 means
use program determined value. [F]

43 = Demand/capacity ratio
limit

Value >= 0; 0 means use
program determined value.

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

## Remarks

This function sets the value of a steel design overwrite
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAISC360\_16()
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
      ret = SapModel.DesignSteel.SetCode("AISC360-16")

   'set overwrite item
      ret = SapModel.DesignSteel.AISC360\_16.SetOverwrite("8",
1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.0.0.

## See Also

[GetOverwrite](GetOverwrite_{AISC_360-16}.htm)



## SetPreferences {AISC 360-16}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_360_16/SetPreferences_{AISC_360-16}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC360\_16.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 35, inclusive, indicating
the preference item considered.

1 = Framing type

2 = Seismic design category

3 = Design provision

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

5 = Notional load coefficient

6 = Phi or Omega for bending

7 = Phi or Omega for compression

8 = Phi or Omega for tension
yielding

9 = Phi or Omega for tension
fracture

10 = Phi or Omega for
shear

11 = Phi or Omega for
shear short webbed rolled I

12 = Phi or Omega for
torsion

13 = Ignore seismic code

14 = Ignore special seismic
load

15 = Doubler plate is
plug welded

16 = HSS welding type

17 = Reduce HSS thickness

18 = Consider deflection

19 = DL deflection limit,
L/Value

20 = SDL + LL deflection
limit, L/Value

21 = LL deflection limit,
L/Value

22 = Total load deflection
limit, L/Value

23 = Total camber limit,
L/Value

24 = Pattern live load
factor

25 = Demand/capacity ratio
limit

26 = Multi-response case design
27 = Analysis Method
28 = Second Order Method
29 = Stiffness Reduction Method

30 = Importance Factor

31 = Design Systems Rho

32 = Design Systems Sds

33 = Design Systems R

34 = Design Systems Omega0

35 = Design Systems Cd

Value

The value of the considered preference item.

1 = Framing type

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Design provision

1 = LRFD

2 = ASD

4 = Analysis method (Obsolete,
replaced by 27, 28, and 29)

1 = Gen 2nd Order Elastic

2 = 2nd Order By Amp
1st Order

3 = Limited 1st Order
Elastic

4 = DAM Gen 2nd Order
Taub Variable

5 = DAM Gen 2nd Order
Taub Fixed

6 = DAM Amp 1st Order
Taub Variable

7 = DAM Amp 1st Order
Taub Fixed

5 = Notional load coefficient

Value > 0

6 = Phi or Omega for bending

Value > 0

7 = Phi or Omega for compression

Value > 0

8 = Phi or Omega for tension
yielding

Value > 0

9 = Phi or Omega for tension
fracture

Value > 0

10 = Phi or Omega for
shear

Value > 0

11 = Phi or Omega for
shear short webbed rolled I

Value > 0

12 = Phi or Omega for
torsion

Value > 0

13 = Ignore seismic code

0 = No

Any other value = Yes

14 = Ignore special seismic
load

0 = No

Any other value = Yes

15 = Doubler plate is
plug welded

0 = No

Any other value = Yes

16 = HSS welding type

1 = ERW

2 = SAW

17 = Reduce HSS thickness

0 = No

Any other value = Yes

18 = Consider deflection

0 = No

Any other value = Yes

19 = DL deflection limit,
L/Value

Value > 0

20 = SDL + LL deflection
limit, L/Value

Value > 0

21 = LL deflection limit,
L/Value

Value > 0

22 = Total load deflection
limit, L/Value

Value > 0

23 = Total camber limit,
L/Value

Value > 0

24 = Pattern live load
factor

Value >= 0

25 = Demand/capacity ratio
limit

Value > 0

26 = Multi-response case
design

  1 = Envelopes

  2 = Step-by-step

  3 = Last
step

  4 = Envelopes
-- All

  5 = Step-by-step
-- All

27 =  Analysis Method

1 = Direct Analysis

2 = Effective Length

3 = Limited 1st Order

28 =  Second Order
Method

1 = General 2nd Order

2 = Amplified 1st Order

29 =  Stiffness Reduction
Method

1 = Tau-b variable

2 = Tau-b Fixed

3 = No Modification

30 = Importance Factor

Value > 0

31 = Design System Rho

Value > 0

32 = Design System Sds

Value >= 0

33 = Design System R

Value > 0

34 = Design System Omega0

Value > 0

35 = Design System Cd

Value > 0

## Remarks

This function sets the value of a steel design preference
item.

The function returns zero if the item is successfully
set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAISC360\_16()
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
      ret = SapModel.DesignSteel.SetCode("AISC360-16")

   'set preference item
      ret = SapModel.DesignSteel.AISC360\_16.SetPreference(1,
7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.0.0

v23.2.0 - modified items
6 through 12 to allow phi or omega, depending on the design provision
value (item 3).

## See Also

[GetPreference](GetPreferences_{AISC_360-16}.htm)



## GetOverwrite {Steel AISC ASD01}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_ASD01/GetOverwrite_{Steel_AISC_ASD01}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC\_ASD01.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 32, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Moment coefficient, Cm Major

23 = Moment coefficient, Cm Minor

24 = Bending coefficient, Cb

25 = Yield stress, Fy

26 = Compressive stress, Fa

27 = Tensile stress, Ft

28 = Major bending stress, Fb3

29 = Minor bending stress, Fb2

30 = Major shear stress, Fv2

31 = Minor shear stress, Fv3

32 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = OMF

2 = IMF

3 = SMF

4 = OCBF

5 = SCBF

6 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L]

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

24 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

25 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

26 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

27 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

28 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

29 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

30 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

31 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

32 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAISC\_ASD01()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-ASD01")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.AISC\_ASD01.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_AISC_ASD01}.htm)



## GetPreference {Steel AISC ASD01}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_ASD01/GetPreference_{Steel_AISC_ASD01}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC\_ASD01.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1   = Framing type

2   = Seismic design capacity

3   = Ignore seismic code

4   = Ignore special seismic load

5   = Isdoubler plate plug-welded

6   = Consider deflection

 7   = DL deflection limit, L/Value

 8   = SDL + LL deflection limit, L/Value

9   = LL deflection limit, L/Value

10 = Total deflection limit, L/Value

11 = Total camber limit, L/Value

12 = Pattern live load factor

13 = Demand/capacity ratio limit

14 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = OMF

2 = IMF

3 = SMF

4 = OCBF

5 = SCBF

6 = EBF

2 = Seismic design capacity

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Ignore seismic code

 0 = No

 Any other value = Yes

4 = Ignore special seismic load

 0 = No

 Any other value = Yes

5 = Isdoubler plate plug-welded

 0 = No

 Any other value = Yes

6 = Consider deflection

 0 = No

 Any other value = Yes

7 = DL DLdeflection limit, L/Value

Value > 0

8 = SDL + LL deflection limit, L/Value

Value > 0

9 = LL deflection limit, L/Value

Value > 0

10 = Total deflection limit, L/Value

Value > 0

11 = Total camber limit, L/Value

Value > 0

12 = Pattern live load factor

Value >= 0

13 = Demand/capacity ratio limit

Value > 0

14 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemAISC\_ASD01 ()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-ASD01")

   'get preference item
      ret = SapModel.DesignSteel.AISC\_ASD01.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_AISC_ASD01}.htm)



## SetOverwrite {Steel AISC ASD01}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_ASD01/SetOverwrite_{Steel_AISC_ASD01}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC\_ASD01.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 32, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Moment coefficient, Cm Major

23 = Moment coefficient, Cm Minor

24 = Bending coefficient, Cb

25 = Yield stress, Fy

26 = Compressive stress, Fa

27 = Tensile stress, Ft

28 = Major bending stress, Fb3

29 = Minor bending stress, Fb2

30 = Major shear stress, Fv2

31 = Minor shear stress, Fv3

32 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = OMF

2 = IMF

3 = SMF

4 = OCBF

5 = SCBF

6 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L]

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

24 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

25 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

26 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

27 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

28 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

29 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

30 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

31 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

32 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects= 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAISC\_ASD01()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-ASD01")

   'set overwrite item
      ret = SapModel.DesignSteel.AISC\_ASD01.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_AISC_ASD01}.htm)



## SetPreference {Steel AISC ASD01}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_ASD01/SetPreference_{Steel_AISC_ASD01}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC\_ASD01.SetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1 = Framing type

2 = Seismic design capacity

3 = Ignore seismic code

4 = Ignore special seismic load

5 = Isdoubler plate plug-welded

6 = Consider deflection

7 = DL deflection limit, L/Value

8 = SDL + LL deflection limit, L/Value

9 = LL deflection limit, L/Value

10 = Total deflection limit, L/Value

11 = Total camber limit, L/Value

12 = Pattern live load factor

13 = Demand/capacity ratio limit

14 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = OMF

2 = IMF

3 = SMF

4 = OCBF

5 = SCBF

6 = EBF

2 = Seismic design capacity

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Ignore seismic code

 0 = No

 Any other value = Yes

4 = Ignore special seismic load

 0 = No

 Any other value = Yes

5 = Is doubler plate plug-welded

 0 = No

 Any other value = Yes

6 = Consider deflection

 0 = No

 Any other value = Yes

 7 = DL DLdeflection limit, L/Value

 Value > 0

8 = SDL + LL deflection limit, L/Value

Value > 0

9 = LL deflection limit, L/Value

Value > 0

10 = Total deflection limit, L/Value

Value > 0

11 = Total camber limit, L/Value

Value > 0

12 = Pattern live load factor

Value >= 0

13 = Demand/capacity ratio limit

Value > 0

14 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAISC\_ASD01()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject= New Sap2000v16.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel= SapObject.SapModel

   'initialize model
      ret= SapModel.InitializeNewModel

   'create model from template
      ret= SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret= SapModel.DesignSteel.SetCode("AISC-ASD01")

   'set preference item
      ret= SapModel.DesignSteel.AISC\_ASD01.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel= Nothing
      Set SapObject= Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_AISC_ASD01}.htm)



## GetOverwrite {Steel AISC ASD89}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_ASD89/GetOverwrite_{Steel_AISC_ASD89}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC\_ASD89.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 31, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Yield stress, Fy

25 = Compressive stress, Fa

26 = Tensile stress, Ft

27 = Major bending stress, Fb3

28 = Minor bending stress, Fb2

29 = Major shear stress, Fv2

30 = Minor shear stress, Fv3

31 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Brace Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

25 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

26 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

27 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

28 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

29 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

30 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

31 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAISC\_ASD89()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-ASD89")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.AISC\_ASD89.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_AISC_ASD89}.htm)



## GetPreference {Steel AISC ASD89}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_ASD89/GetPreference_{Steel_AISC_ASD89}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC\_ASD89.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Framing type

2 = Lateral factor

3 = Consider deflection

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit

6 = LL deflection limit, L/Value

7 = Total deflection limit, L/Value

8 = Total camber limit, L/Value

9 = Pattern live load factor

10 = Demand/capacity ratio limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Lateral factor

Value > 0

3 = Consider deflection

 0 = No

 Any other value = Yes

4 = DL deflection limit, L/Value

Value > 0

5 = SDL + LL deflection limit

Value > 0

6 = LL deflection limit, L/Value

Value > 0

7 = Total deflection limit, L/Value

Value > 0

8 = Total camber limit, L/Value

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Demand/capacity ratio limit

Value > 0

11 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemAISC\_ASD89()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-ASD89")

   'get preference item
      ret = SapModel.DesignSteel.AISC\_ASD89.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_AISC_ASD89}.htm)



## SetOverwrite {Steel AISC ASD89}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_ASD89/SetOverwrite_{Steel_AISC_ASD89}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC\_ASD89.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 31, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Yield stress, Fy

25 = Compressive stress, Fa

26 = Tensile stress, Ft

27 = Major bending stress, Fb3

28 = Minor bending stress, Fb2

29 = Major shear stress, Fv2

30 = Minor shear stress, Fv3

31 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Brace Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral TorsionalBuckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

25 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

26 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

27 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

28 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

29 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

30 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

31 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemASIC\_ASD89()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-ASD89")

   'set overwrite item
      ret = SapModel.DesignSteel.AISC\_ASD89.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_AISC_ASD89}.htm)



## SetPreference {Steel AISC ASD89}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_ASD89/SetPreference_{Steel_AISC_ASD89}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC\_ASD89.SetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Framing type

2 = Lateral factor

3 = Consider deflection

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit

6 = LL deflection limit, L/Value

7 = Total deflection limit, L/Value

8 = Total camber limit, L/Value

9 = Pattern live load factor

10 = Demand/capacity ratio limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Lateral factor

Value > 0

3 = Consider deflection

 0 = No

 Any other value = Yes

4 = DL deflection limit, L/Value

Value > 0

5 = SDL + LL deflection limit

Value > 0

6 = LL deflection limit, L/Value

Value > 0

7 = Total deflection limit, L/Value

Value > 0

8 = Total camber limit, L/Value

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Demand/capacity ratio limit

Value > 0

11 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAISC\_ASD89()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-ASD89")

   'set preference item
      ret = SapModel.DesignSteel.AISC\_ASD89.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_AISC_ASD89}.htm)



## GetOverwrite {Steel AISC LRFD93}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_LRFD93/GetOverwrite_{Steel_AISC_LRFD93}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC\_LRFD93.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 35, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Non-sway moment factor, B1 Major

25 = Non-sway moment factor, B1 Minor

26 = Sway moment factor, B2 Major

27 = Sway moment factor, B2 Minor

28 = Yield stress, Fy

29 = Compressive capacity, phi\*Pnc

30 = Tensile capacity, phi\*Pnt

31 = Major bending capacity, phi\*Mn3

32 = Minor bending capacity, phi\*Mn2

33 = Major shear capacity, phi\*Vn2

34 = Minor shear capacity, phi\*Vn3

35 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Non-sway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

25 = Non-sway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

28 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

29 = Compressive capacity, phi\*Pnc

Value >= 0; 0 means use program determined value. [F]

30 = Tensile capacity, phi\*Pnt

Value >= 0; 0 means use program determined value. [F]

31 = Major bending capacity, phi\*Mn3

Value >= 0; 0 means use program determined value. [FL]

32 = Minor bending capacity, phi\*Mn2

Value >= 0; 0 means use program determined value. [FL]

33 = Major shear capacity, phi\*Vn2

Value >= 0; 0 means use program determined value. [F]

34 = Minor shear capacity, phi\*Vn3

Value >= 0; 0 means use program determined value. [F]

35 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAISC\_LRFD93()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-LRFD93")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.AISC\_LRFD93.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_AISC_LRFD93}.htm)



## GetPreference {Steel AISC LRFD93}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_LRFD93/GetPreference_{Steel_AISC_LRFD93}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC\_LRFD93.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 15, inclusive, indicating the preference item considered.

1 = Framing type

2 = Phi bending

3 = Phi compression

4 = Phi tension

5 = Phi shear

6 = Phi compression, angle

7 = Consider deflection

8 = DL deflection limit, L/Value

9 = SDL + LL deflection limit, L/Value

10 = LL deflection limit, L/Value

11 = Total deflection limit, L/Value

12 = Total camber limit, L/Value

13 = Pattern live load factor

14 = Demand/capacity ratio limit

15 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Phi bending

Value > 0

3 = Phi compression

 Value > 0

4 = Phi tension

Value > 0

5 = Phi shear

Value > 0

6 = Phi compression, angle

Value > 0

7 = Consider deflection

0 = No

Any other value = Yes

8 = DL deflection limit, L/Value

 Value > 0

9 = SDL + LL deflection limit, L/Value

 Value > 0

10 = LL deflection limit, L/Value

Value > 0

11 = Total deflection limit, L/Value

Value > 0

12 = Total camber limit, L/Value

Value > 0

13 = Pattern live load factor

Value >= 0

14 = Demand/capacity ratio limit

Value > 0

15 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemAISC\_LRFD93()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-LRFD93")

   'get preference item
      ret = SapModel.DesignSteel.AISC\_LRFD93.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_AISC_LRFD93}.htm)



## SetOverwrite {Steel AISC LRFD93}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_LRFD93/SetOverwrite_{Steel_AISC_LRFD93}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC\_LRFD93.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 35, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Non-sway moment factor, B1 Major

25 = Non-sway moment factor, B1 Minor

26 = Sway moment factor, B2 Major

27 = Sway moment factor, B2 Minor

28 = Yield stress, Fy

29 = Compressive capacity, phi\*Pnc

30 = Tensile capacity, phi\*Pnt

31 = Major bending capacity, phi\*Mn3

32 = Minor bending capacity, phi\*Mn2

33 = Major shear capacity, phi\*Vn2

34 = Minor shear capacity, phi\*Vn3

35 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

25 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

28 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

29 = Compressive capacity, phi\*Pnc

Value >= 0; 0 means use program determined value. [F]

30 = Tensile capacity, phi\*Pnt

Value >= 0; 0 means use program determined value. [F]

31 = Major bending capacity, phi\*Mn3

Value >= 0; 0 means use program determined value. [FL]

32 = Minor bending capacity, phi\*Mn2

Value >= 0; 0 means use program determined value. [FL]

33 = Major shear capacity, phi\*Vn2

Value >= 0; 0 means use program determined value. [F]

34 = Minor shear capacity, phi\*Vn3

Value >= 0; 0 means use program determined value. [F]

35 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects= 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAISC\_LRFD93()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-LRFD93")

   'set overwrite item
      ret = SapModel.DesignSteel.AISC\_LRFD93.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_AISC_LRFD93}.htm)



## SetPreference {Steel AISC LRFD93}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AISC_LRFD93/SetPreference_{Steel_AISC_LRFD93}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC\_LRFD93.SetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 15, inclusive, indicating the preference item considered.

1 = Framing type

2 = Phi bending

3 = Phi compression

4 = Phi tension

5 = Phi shear

6 = Phi compression, angle

7 = Consider deflection

8 = DL deflection limit, L/Value

9 = SDL + LL deflection limit, L/Value

10 = LL deflection limit, L/Value

11 = Total deflection limit, L/Value

12 = Total camber limit, L/Value

13 = Pattern live load factor

14 = Demand/capacity ratio limit

15 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Phi bending

Value > 0

3 = Phi compression

Value > 0

4 = Phi tension

Value > 0

5 = Phi shear

Value > 0

6 = Phi compression, angle

Value > 0

7 = Consider deflection

0 = No

Any other value = Yes

8 = DL deflection limit, L/Value

Value > 0

9 = SDL + LL deflection limit, L/Value

Value > 0

10 = LL deflection limit, L/Value

  Value > 0

11 = Total deflection limit, L/Value

  Value > 0

12 = Total camber limit, L/Value

Value > 0

13 = Pattern live load factor

Value >= 0

14 = Demand/capacity ratio limit

Value > 0

15 = Multi-response case design

 1 = Envelopes

 2 = Step-by-step

 3 = Last step

 4 = Envelopes -- All

 5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAISC\_LRFD93 ()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-LRFD93")

   'set preference item
      ret = SapModel.DesignSteel.AISC\_LRFD93.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_AISC_LRFD93}.htm)



## GetOverwrite {API_4F_2020}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_4F_2020/GetOverwrite_{API_4F_2020}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.API\_4F\_2020.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 43, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor

20 = Unbraced length ratio, Lateral Torsional Buckling

21 = Effective length factor, K1 Major

22 = Effective length factor, K1 Minor

23 = Effective length factor, K2 Major

24 = Effective length factor, K2 Minor

25 = Effective length factor, K Lateral Torsional Buckling

26 = Moment coefficient, Cm Major

27 = Moment coefficient, Cm Minor

28 = Bending coefficient, Cb

29 = Nonsway moment factor, B1 Major

30 = Nonsway moment factor, B1 Minor

31 = Sway moment factor, B2 Major

32 = Sway moment factor, B2 Minor

33 = Reduce HSS thickness

34 = HSS welding type

35 = Yield stress, Fy

36 = Expected to specified Fy ratio, Ry

37 = Compressive capacity, Pnc

38 = Tensile capacity, Pnt

39 = Major bending capacity, Mn3

40 = Minor bending capacity, Mn2

41 = Major shear capacity, Vn2

42 = Minor shear capacity, Vn3

43 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program default

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]}

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L}

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

20 = Unbraced length ratio, Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K1 Major

Value >= 0; 0 means use program determined value.

22 = Effective length factor, K1 Minor

Value >= 0; 0 means use program determined value.

23 = Effective length factor, K2 Major

Value >= 0; 0 means use program determined value.

24 = Effective length factor, K2 Minor

Value >= 0; 0 means use program determined value.

25 = Effective length factor, K Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

26 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

27 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

28 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

29 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

30 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

31 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

32 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

33 = Reduce HSS thickness

0 = Program default

1 = No

2 = Yes

34 = HSS welding type

0 = Program default

1 = ERW

2 = SAW

35 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

36 = Expected to specified Fy ratio, Ry

Value >= 0; 0 means use program determined value.

37 = Compressive capacity, Pnc

Value >= 0; 0 means use program determined value. [F]

38 = Tensile capacity, Pnt

Value >= 0; 0 means use program determined value. [F]

39 = Major bending capacity, Mn3

Value >= 0; 0 means use program determined value. [FL]

40 = Minor bending capacity, Mn2

Value >= 0; 0 means use program determined value. [FL]

41 = Major shear capacity, Vn2

Value >= 0; 0 means use program determined value. [F]

42 = Minor shear capacity, Vn3

Value >= 0; 0 means use program determined value. [F]

43 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAPI\_4F\_2020()
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
ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'set steel design code
ret = SapModel.DesignSteel.SetCode("API 4F-2020")

'run analysis
ret = SapModel.File.Save("C:\SapAPI\x.sdb")
ret = SapModel.Analyze.RunAnalysis

'start steel design
ret = SapModel.DesignSteel.StartDesign

'get overwrite item
ret = SapModel.DesignSteel.API\_4F\_2020.GetOverwrite("8", 1, Value, ProgDet)

'close Sap2000
SapObject.ApplicationExit False
Set SapModel = Nothing
Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.2.0

## See Also

[SetOverwrite](SetOverwrite_{API_4F_2020}.htm)



## GetPreferences {API_4F_2020}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_4F_2020/GetPreferences_{API_4F_2020}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.API\_4F\_2020.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 32, inclusive, indicating the preference item considered.

1 = Framing type

2 = Seismic design category

3 = Importance Factor

4 = Design Systems Rho

5 = Design Systems Sds

6 = Design Systems R

7 = Design Systems Omega0

8 = Design Systems Cd

9 = Analysis Method

10 = Second Order Method

11 = Stiffness Reduction Method

12 = Omega for bending

13 = Omega for compression

14 = Omega for tension yielding

15 = Omega for tension fracture

16 = Omega for shear

17 = Omega for shear short webbed rolled I

18 = Omega for torsion

19 = Ignore seismic code

20 = Ignore special seismic load

21 = Doubler plate is plug welded

22 = HSS welding type

23 = Reduce HSS thickness

24 = Consider deflection

25 = DL deflection limit, L/Value

26 = SDL + LL deflection limit, L/Value

27 = LL deflection limit, L/Value

28 = Total load deflection limit, L/Value

29 = Total camber limit, L/Value

30 = Pattern live load factor

31 = Demand/capacity ratio limit

32 =Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Importance Factor

Value > 0

4 = Design System Rho

Value > 0

5 = Design System Sds

Value >= 0

6 = Design System R

Value > 0

7 = Design System Omega0

Value > 0

8 = Design System Cd

Value > 0

9 = Analysis Method

1 = Direct Analysis

2 = Effective Length

3 = Limited 1st Order

10 = Second Order Method

1 = General 2nd Order

2 = Amplified 1st Order

11 = Stiffness Reduction Method

1 = Tau-b variable

2 = Tau-b Fixed

3 = No Modification

12 = Omega for bending

Value > 0

13 = Omega for compression

Value > 0

14 = Omega for tension yielding

Value > 0

15 = Omega for tension fracture

Value > 0

16 = Omega for shear

Value > 0

17 = Omega for shear short webbed rolled I

Value > 0

18 = Omega for torsion

Value > 0

19 = Ignore seismic code

0 = No

Any other value = Yes

20 = Ignore special seismic load

0 = No

Any other value = Yes

21 = Doubler plate is plug welded

0 = No

Any other value = Yes

22 = HSS welding type

1 = ERW

2 = SAW

23 = Reduce HSS thickness

0 = No

Any other value = Yes

24 = Consider deflection

0 = No

Any other value = Yes

25 = DL deflection limit, L/Value

Value > 0

26 = SDL + LL deflection limit, L/Value

Value > 0

27 = LL deflection limit, L/Value

Value > 0

28 = Total load deflection limit, L/Value

Value > 0

29 = Total camber limit, L/Value

Value > 0

30 = Pattern live load factor

Value >= 0

31 = Demand/capacity ratio limit

Value > 0

32 = Multi-response case design

 1 = Envelopes

 2 = Step-by-step

 3 = Last step

 4 = Envelopes -- All

 5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemAPI\_4F\_2020()
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
ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'set steel design code
ret = SapModel.DesignSteel.SetCode("API 4F-2020")

'get preference item
ret = SapModel.DesignSteel.API\_4F\_2020.GetPreference(1, Value)

'close Sap2000
SapObject.ApplicationExit False
Set SapModel = Nothing
Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.2.0

## See Also

[SetPreference](SetPreferences_{API_4F_2020}.htm)



## SetOverwrite {API_4F_2020}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_4F_2020/SetOverwrite_{API_4F_2020}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.API\_4F\_2020.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 43, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor

20 = Unbraced length ratio, Lateral Torsional Buckling

21 = Effective length factor, K1 Major

22 = Effective length factor, K1 Minor

23 = Effective length factor, K2 Major

24 = Effective length factor, K2 Minor

25 = Effective length factor, K Lateral Torsional Buckling

26 = Moment coefficient, Cm Major

27 = Moment coefficient, Cm Minor

28 = Bending coefficient, Cb

29 = Nonsway moment factor, B1 Major

30 = Nonsway moment factor, B1 Minor

31 = Sway moment factor, B2 Major

32 = Sway moment factor, B2 Minor

33 = Reduce HSS thickness

34 = HSS welding type

35 = Yield stress, Fy

36 = Expected to specified Fy ratio, Ry

37 = Compressive capacity, Pnc

38 = Tensile capacity, Pnt

39 = Major bending capacity, Mn3

40 = Minor bending capacity, Mn2

41 = Major shear capacity, Vn2

42 = Minor shear capacity, Vn3

43 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program default

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]}

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L}

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

20 = Unbraced length ratio, Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K1 Major

Value >= 0; 0 means use program determined value.

22 = Effective length factor, K1 Minor

Value >= 0; 0 means use program determined value.

23 = Effective length factor, K2 Major

Value >= 0; 0 means use program determined value.

24 = Effective length factor, K2 Minor

Value >= 0; 0 means use program determined value.

25 = Effective length factor, K Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

26 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

27 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

28 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

29 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

30 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

31 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

32 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

33 = Reduce HSS thickness

0 = Program default

1 = No

2 = Yes

34 = HSS welding type

0 = Program default

1 = ERW

2 = SAW

35 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

36 = Expected to specified Fy ratio, Ry

Value >= 0; 0 means use program determined value.

37 = Compressive capacity, Pnc

Value >= 0; 0 means use program determined value. [F]

38 = Tensile capacity, Pnt

Value >= 0; 0 means use program determined value. [F]

39 = Major bending capacity, Mn3

Value >= 0; 0 means use program determined value. [FL]

40 = Minor bending capacity, Mn2

Value >= 0; 0 means use program determined value. [FL]

41 = Major shear capacity, Vn2

Value >= 0; 0 means use program determined value. [F]

42 = Minor shear capacity, Vn3

Value >= 0; 0 means use program determined value. [F]

43 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAPI\_4F\_2020()
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

'set steel design code
ret = SapModel.DesignSteel.SetCode("API 4F-2020")

'set overwrite item
ret = SapModel.DesignSteel.API\_4F\_2020.SetOverwrite("8", 1, 7)

'close Sap2000
SapObject.ApplicationExit False
Set SapModel = Nothing
Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.2.0

## See Also

[GetOverwrite](GetOverwrite_{API_4F_2020}.htm)



## SetPreferences {API_4F_2020}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_4F_2020/SetPreferences_{API_4F_2020}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.API\_4F\_2020.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 32, inclusive, indicating the preference item considered.

1 = Framing type

2 = Seismic design category

3 = Importance Factor

4 = Design Systems Rho

5 = Design Systems Sds

6 = Design Systems R

7 = Design Systems Omega0

8 = Design Systems Cd

9 = Analysis Method

10 = Second Order Method

11 = Stiffness Reduction Method

12 = Omega for bending

13 = Omega for compression

14 = Omega for tension yielding

15 = Omega for tension fracture

16 = Omega for shear

17 = Omega for shear short webbed rolled I

18 = Omega for torsion

19 = Ignore seismic code

20 = Ignore special seismic load

21 = Doubler plate is plug welded

22 = HSS welding type

23 = Reduce HSS thickness

24 = Consider deflection

25 = DL deflection limit, L/Value

26 = SDL + LL deflection limit, L/Value

27 = LL deflection limit, L/Value

28 = Total load deflection limit, L/Value

29 = Total camber limit, L/Value

30 = Pattern live load factor

31 = Demand/capacity ratio limit

32 =Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = SMF

2 = IMF

3 = OMF

4 = SCBF

5 = OCBF

6 = OCBFI

7 = EBF

2 = Seismic design category

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Importance Factor

Value > 0

4 = Design System Rho

Value > 0

5 = Design System Sds

Value >= 0

6 = Design System R

Value > 0

7 = Design System Omega0

Value > 0

8 = Design System Cd

Value > 0

9 = Analysis Method

1 = Direct Analysis

2 = Effective Length

3 = Limited 1st Order

10 = Second Order Method

1 = General 2nd Order

2 = Amplified 1st Order

11 = Stiffness Reduction Method

1 = Tau-b variable

2 = Tau-b Fixed

3 = No Modification

12 = Omega for bending

Value > 0

13 = Omega for compression

Value > 0

14 = Omega for tension yielding

Value > 0

15 = Omega for tension fracture

Value > 0

16 = Omega for shear

Value > 0

17 = Omega for shear short webbed rolled I

Value > 0

18 = Omega for torsion

Value > 0

19 = Ignore seismic code

0 = No

Any other value = Yes

20 = Ignore special seismic load

0 = No

Any other value = Yes

21 = Doubler plate is plug welded

0 = No

Any other value = Yes

22 = HSS welding type

1 = ERW

2 = SAW

23 = Reduce HSS thickness

0 = No

Any other value = Yes

24 = Consider deflection

0 = No

Any other value = Yes

25 = DL deflection limit, L/Value

Value > 0

26 = SDL + LL deflection limit, L/Value

Value > 0

27 = LL deflection limit, L/Value

Value > 0

28 = Total load deflection limit, L/Value

Value > 0

29 = Total camber limit, L/Value

Value > 0

30 = Pattern live load factor

Value >= 0

31 = Demand/capacity ratio limit

Value > 0

32 = Multi-response case design

 1 = Envelopes

 2 = Step-by-step

 3 = Last step

 4 = Envelopes -- All

 5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAPI\_4F\_2020()
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

'set steel design code
ret = SapModel.DesignSteel.SetCode("API 4F-2020")

'set preference item
ret = SapModel.DesignSteel.API\_4F\_2020.SetPreference(1, 7)

'close Sap2000
SapObject.ApplicationExit False
Set SapModel = Nothing
Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.2.0

## See Also

[GetPreference](GetPreferences_{API_4F_2020}.htm)



## GetOverwrite {Steel API RP2A LRFD97}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_LRFD97/GetOverwrite_{Steel_API_RP2A_LRFD97}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_LRFD97.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 37, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Non-sway moment factor, B1 Major

25 = Non-sway moment factor, B1 Minor

26 = Sway moment factor, B2 Major

27 = Sway moment factor, B2 Minor

28 = Pressure equalized

29 = External pressure

30 = Yield stress, Fy

31 = Compressive capacity, phi\*Pnc

32 = Tensile capacity, phi\*Pnt

33 = Major bending capacity, phi\*Mn3

34 = Minor bending capacity, phi\*Mn2

35 = Major shear capacity, phi\*Vn2

36 = Minor shear capacity, phi\*Vn3

37 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Non-sway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

25 = Non-sway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

28 = Pressure equalized

0 = Program Determined

1 = No

2 = Yes

29 = External pressure. [F/L2]

Any value OK; Positive generates hoop compression and negative generates hoop tension. [F/L2]

30 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

31 = Compressive capacity, phi\*Pnc

Value >= 0; 0 means use program determined value. [F]

32 = Tensile capacity, phi\*Pnt

Value >= 0; 0 means use program determined value. [F]

33 = Major bending capacity, phi\*Mn3

Value >= 0; 0 means use program determined value. [FL]

34 = Minor bending capacity, phi\*Mn2

Value >= 0; 0 means use program determined value. [FL]

35 = Major shear capacity, phi\*Vn2

Value >= 0; 0 means use program determined value. [F]

36 = Minor shear capacity, phi\*Vn3

Value >= 0; 0 means use program determined value. [F]

37 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAPI\_RP2A\_LRFD97()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("API RP2A-LRFD 97")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.API\_RP2A\_LRFD97.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Modified Item 29 in version 14.1.0.

## See Also

[SetOverwrite](SetOverwrite_{Steel_API_RP2A_LRFD97}.htm)



## GetPreference {Steel API RP2A LRFD97}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_LRFD97/GetPreference_{Steel_API_RP2A_LRFD97}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_LRFD97.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Framing type

2 = Tubular joint punching load method

3 = Consider deflection

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total deflection limit, L/Value

8 = Total camber limit, L/Value

9 = Pattern live load factor

10 = Demand/capacity ratio limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Tubular joint punching load method

1 = Punching Shear

2 = Nominal Load

3 = Consider deflection

0 = No

Any other value = Yes

4 = DL deflection limit, L/Value

Value > 0

5 = SDL + LL deflection limit, L/Value

Value > 0

6 = LL deflection limit, L/Value

Value > 0

7 = Total deflection limit, L/Value

Value > 0

8 = Total camber limit, L/Value

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Demand/capacity ratio limit

 Value > 0

11 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemAPI\_RP2A\_LRFD97 ()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("API RP2A-LRFD 97")

   'get preference item
      ret = SapModel.DesignSteel.API\_RP2A\_LRFD97.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_API_RP2A_LRFD97}.htm)



## SetOverwrite {Steel API RP2A LRFD97}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_LRFD97/SetOverwrite_{Steel_API_RP2A_LRFD97}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_LRFD97.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemTypeitem.

Item

This is an integer between 1 and 37, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Non-sway moment factor, B1 Major

25 = Non-sway moment factor, B1 Minor

26 = Sway moment factor, B2 Major

27 = Sway moment factor, B2 Minor

28 = Pressure equalized

29 = External pressure

30 = Yield stress, Fy

31 = Compressive capacity, phi\*Pnc

32 = Tensile capacity, phi\*Pnt

33 = Major bending capacity, phi\*Mn3

34 = Minor bending capacity, phi\*Mn2

35 = Major shear capacity, phi\*Vn2

36 = Minor shear capacity, phi\*Vn3

37 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Non-sway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

25 = Non-sway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

28 = Pressure equalized

0 = Program Determined

1 = No

2 = Yes

29 = External pressure

Any value OK; Positive generates hoop compression and negative generates hoop tension. [F/L2]

30 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

31 = Compressive capacity, phi\*Pnc

Value >= 0; 0 means use program determined value. [F]

32 = Tensile capacity, phi\*Pnt

Value >= 0; 0 means use program determined value. [F]

33 = Major bending capacity, phi\*Mn3

Value >= 0; 0 means use program determined value. [FL]

34 = Minor bending capacity, phi\*Mn2

Value >= 0; 0 means use program determined value. [FL]

35 = Major shear capacity, phi\*Vn2

Value >= 0; 0 means use program determined value. [F]

36 = Minor shear capacity, phi\*Vn3

Value >= 0; 0 means use program determined value. [F]

37 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAPI\_RP2A\_LRFD97()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("API RP2A-LRFD 97")

   'set overwrite item
      ret = SapModel.DesignSteel.API\_RP2A\_LRFD97.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Modified Item 29 in version 14.1.0.

## See Also

[GetOverwrite](GetOverwrite_{Steel_API_RP2A_LRFD97}.htm)



## SetPreference {Steel API RP2A LRFD97}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_LRFD97/SetPreference_{Steel_API_RP2A_LRFD97}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_LRFD97.SetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Framing type

2 = Tubular joint punching load method

3 = Consider deflection

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total deflection limit, L/Value

8 = Total camber limit, L/Value

9 = Pattern live load factor

10 = Demand/capacity ratio limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Tubular joint punching load method

1 = Punching Shear

2 = Nominal Load

3 = Consider deflection

 0 = No

 Any other value = Yes

4 = DL deflection limit, L/Value

Value > 0

5 = SDL + LL deflection limit, L/Value

Value > 0

6 = LL deflection limit, L/Value

Value > 0

7 = Total deflection limit, L/Value

Value > 0

8 = Total camber limit, L/Value

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Demand/capacity ratio limit

Value > 0

11 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAPI\_RP2A\_LRFD97()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject= New Sap2000v16.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel= SapObject.SapModel

   'initialize model
      ret= SapModel.InitializeNewModel

   'create model from template
      ret= SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret= SapModel.DesignSteel.SetCode("API RP2A-LRFD 97")

   'set preference item
      ret= SapModel.DesignSteel.API\_RP2A\_LRFD97.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel= Nothing
      Set SapObject= Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_API_RP2A_LRFD97}.htm)



## GetOverwrite {Steel API RP2A WSD2000}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_WSD2000/GetOverwrite_{Steel_API_RP2A_WSD2000}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_WSD2000.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 33, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral TorsionalBuckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Pressure equalized

25 = External pressure

26 = Yield stress, Fy

27 = Compressive stress, Fa

28 = Tensile stress, Ft

29 = Major bending stress, Fb3

30 = Minor bending stress, Fb2

31 = Major shear stress, Fv2

32 = Minor shear stress, Fv3

33 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Pressure equalized

0 = Program Determined

1 = No

2 = Yes

25 = External pressure

Any value OK; Positive generates hoop compression and negative generates hoop tension.. [F/L2]

26 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

27 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

28 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

29 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

30 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

31 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

32 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

33 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAPI\_RP2A\_WSD2000()
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

   'createSapModelobject
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("API RP2A-WSD2000")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.API\_RP2A\_WSD2000.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Modified Item 25 in version 14.1.0.

## See Also

[SetOverwrite](SetOverwrite_{Steel_API_RP2A_WSD2000}.htm)



## GetPreference {Steel API RP2A WSD2000}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_WSD2000/GetPreference_{Steel_API_RP2A_WSD2000}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_WSD2000.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 12, inclusive, indicating the preference item considered.

1 = Framing type

2 = Tubular joint punching load method

3 = Lateral factor, L/Value

4 = Consider deflection

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total deflection limit, L/Value

9 = Total camber limit, L/Value

10 = Pattern live load factor

11 = Demand/capacity ratio limit

12 = Multi-response case design

13 = Code supplements

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Tubular joint punching load method

1 = Punching Shear

2 = Nominal Load

3 = Lateral Factor

Value > 0

4 = Consider deflection

0 = No

Any other value = Yes

5 = DL deflection limit, L/Value

Value > 0

6 = SDL + LL deflection limit, L/Value

Value > 0

7 = LL deflection limit, L/Value

Value > 0

8 = Total deflection limit, L/Value

Value > 0

9 = Total camber limit, L/Value

Value > 0

10 = Pattern live load factor

Value >= 0

11 = Demand/capacity ratio limit

Value > 0

12 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

13 = Code supplements

1 = None

2 = Supplements 2 and 3

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemAPI\_RP2A\_WSD2000()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("API RP2A-WSD2000")

   'get preference item
      ret = SapModel.DesignSteel.API\_RP2A\_WSD2000.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

Added code supplements item in version 16.1.0.

## See Also

[SetPreference](SetPreference_{Stl_API_RP2A_WSD2000}.htm)



## SetOverwrite {Steel API RP2A WSD2000}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_WSD2000/SetOverwrite_{Steel_API_RP2A_WSD2000}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_WSD2000.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 33, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Pressure equalized

25 = External pressure

26 = Yield stress, Fy

27 = Compressive stress, Fa

28 = Tensile stress, Ft

29 = Major bending stress, Fb3

30 = Minor bending stress, Fb2

31 = Major shear stress, Fv2

32 = Minor shear stress, Fv3

33 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Pressure equalized

0 = Program Determined

1 = No

2 = Yes

25 = External pressure

Any value OK; Positive generates hoop compression and negative generates hoop tension. [F/L2]

26 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

27 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

28 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

29 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

30 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

31 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

32 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

33 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAPI\_RP2A\_WSD2000()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("API RP2A-WSD2000")

   'set overwrite item
      ret = SapModel.DesignSteel.API\_RP2A\_WSD2000.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Modified Item 25 in version 14.1.0.

## See Also

[GetOverwrite](GetOverwrite_{Steel_API_RP2A_WSD2000}.htm)



## SetPreference {Seetl API RP2A WSD2000}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_WSD2000/SetPreference_{Stl_API_RP2A_WSD2000}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_WSD2000.SetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 12, inclusive, indicating the preference item considered.

1 = Framing type

2 = Tubular joint punching load method

3 = Lateral factor, L/Value

4 = Consider deflection

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total deflection limit, L/Value

9 = Total camber limit, L/Value

10 = Pattern live load factor

11 = Demand/capacity ratio limit

12 = Multi-response case design

13 = Code supplements

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Tubular joint punching load method

1 = Punching Shear

2 = Nominal Load

3 = Lateral factor

Value > 0

4 = Consider deflection

0 = No

Any other value = Yes

5 = DL deflection limit, L/Value

Value > 0

6 = SDL + LL deflection limit, L/Value

Value > 0

7 = LL deflection limit, L/Value

Value > 0

8 = Total deflection limit, L/Value

Value > 0

9 = Total camber limit, L/Value

Value >= 0

10 = Pattern live load factor

Value >= 0

11 = Demand/capacity ratio limit

Value > 0

12 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

13 = Code supplements

1 = None

2 = Supplements 2 and 3

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAPI\_RP2A\_WSD2000()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject= New Sap2000v16.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel= SapObject.SapModel

   'initialize model
      ret= SapModel.InitializeNewModel

   'create model from template
      ret= SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret= SapModel.DesignSteel.SetCode("API RP2A-WSD2000")

   'set preference item
      ret= SapModel.DesignSteel.API\_RP2A\_WSD2000.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel= Nothing
      Set SapObject= Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

Added code supplements item in version 16.1.0.

## See Also

[GetPreference](GetPreference_{Steel_API_RP2A_WSD2000}.htm)



## GetOverwrite {Steel API RP2A WSD2014}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_WSD2014/GetOverwrite_{Steel_API_RP2A_WSD2014}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_WSD2014.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 33, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral TorsionalBuckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Pressure equalized

25 = External pressure

26 = Yield stress, Fy

27 = Compressive stress, Fa

28 = Tensile stress, Ft

29 = Major bending stress, Fb3

30 = Minor bending stress, Fb2

31 = Major shear stress, Fv2

32 = Minor shear stress, Fv3

33 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Pressure equalized

0 = Program Determined

1 = No

2 = Yes

25 = External pressure

Any value OK; Positive generates hoop compression and negative generates hoop tension.. [F/L2]

26 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

27 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

28 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

29 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

30 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

31 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

32 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

33 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAPI\_RP2A\_WSD2014()
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

   'createSapModelobject
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("API RP2A-WSD2014")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.API\_RP2A\_WSD2014.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 19.1.0.

## See Also

[SetOverwrite](SetOverwrite_{Steel_API_RP2A_WSD2014}.htm)



## GetPreference {Steel API RP2A WSD2014}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_WSD2014/GetPreference_{Steel_API_RP2A_WSD2014}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_WSD2014.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Framing type

2 = Lateral factor, L/Value

3 = Consider deflection

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total deflection limit, L/Value

8 = Total camber limit, L/Value

9 = Pattern live load factor

10 = Demand/capacity ratio limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Lateral Factor

Value > 0

3 = Consider deflection

0 = No

Any other value = Yes

4 = DL deflection limit, L/Value

Value > 0

5 = SDL + LL deflection limit, L/Value

Value > 0

6 = LL deflection limit, L/Value

Value > 0

7 = Total deflection limit, L/Value

Value > 0

8 = Total camber limit, L/Value

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Demand/capacity ratio limit

Value > 0

11 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemAPI\_RP2A\_WSD2014()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("API RP2A-WSD2014")

   'get preference item
      ret = SapModel.DesignSteel.API\_RP2A\_WSD2014.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 19.1.0.

## See Also

[SetPreference](SetPreference_{Steel_API_RP2A_WSD2014}.htm)



## SetOverwrite {Steel API RP2A WSD2014}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_WSD2014/SetOverwrite_{Steel_API_RP2A_WSD2014}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_WSD2014.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 33, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Pressure equalized

25 = External pressure

26 = Yield stress, Fy

27 = Compressive stress, Fa

28 = Tensile stress, Ft

29 = Major bending stress, Fb3

30 = Minor bending stress, Fb2

31 = Major shear stress, Fv2

32 = Minor shear stress, Fv3

33 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Pressure equalized

0 = Program Determined

1 = No

2 = Yes

25 = External pressure

Any value OK; Positive generates hoop compression and negative generates hoop tension. [F/L2]

26 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

27 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

28 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

29 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

30 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

31 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

32 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

33 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAPI\_RP2A\_WSD2014()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("API RP2A-WSD2014")

   'set overwrite item
      ret = SapModel.DesignSteel.API\_RP2A\_WSD2000.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 19.1.0.

## See Also

[GetOverwrite](GetOverwrite_{Steel_API_RP2A_WSD2014}.htm)



## SetPreference {Steel API RP2A WSD2014}

*Source file: `SAP2000_API_Fuctions/Design/Steel/API_RP2A_WSD2014/SetPreference_{Steel_API_RP2A_WSD2014}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.API\_RP2A\_WSD2000.SetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Framing type

2 = Lateral factor, L/Value

3 = Consider deflection

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total deflection limit, L/Value

8 = Total camber limit, L/Value

9 = Pattern live load factor

10 = Demand/capacity ratio limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Lateral Factor

Value > 0

3 = Consider deflection

0 = No

Any other value = Yes

4 = DL deflection limit, L/Value

Value > 0

5 = SDL + LL deflection limit, L/Value

Value > 0

6 = LL deflection limit, L/Value

Value > 0

7 = Total deflection limit, L/Value

Value > 0

8 = Total camber limit, L/Value

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Demand/capacity ratio limit

Value > 0

11 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAPI\_RP2A\_WSD2014()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

   'create Sap2000 object
      Set SapObject= New Sap2000v16.SapObject

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel= SapObject.SapModel

   'initialize model
      ret= SapModel.InitializeNewModel

   'create model from template
      ret= SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret= SapModel.DesignSteel.SetCode("API RP2A-WSD2014")

   'set preference item
      ret= SapModel.DesignSteel.API\_RP2A\_WSD2014.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel= Nothing
      Set SapObject= Nothing
End Sub

## Release Notes

Initial release in version 19.1.0.

## See Also

[GetPreference](GetPreference_{Steel_API_RP2A_WSD2014}.htm)



## GetOverwrite {Steel ASCE 10-97}

*Source file: `SAP2000_API_Fuctions/Design/Steel/ASCE_10-97/GetOverwrite_{Steel_ASCE_10-97}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.ASCE\_10\_97.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 31, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Yield stress, Fy

25 = Compressive capacity, Pac

26 = Tensile capacity, Pat

27 = Major bending capacity, Ma3

28 = Minor bending capacity, Ma2

29 = Major shear stress, Fv2

30 = Minor shear stress, Fv3

31 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Brace Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

25 = Compressive capacity, Pac

Value >= 0; 0 means use program determined value. [F]

26 = Tensile capacity, Pat

Value >= 0; 0 means use program determined value. [F]

27 = Major bending capacity, Ma3

Value >= 0; 0 means use program determined value. [FL]

28 = Minor bending capacity, Ma2

Value >= 0; 0 means use program determined value. [FL]

29 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

30 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

31 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemASCE\_10\_97()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("ASCE 10-97")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.ASCE\_10\_97.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_ASCE_10-97}.htm)



## GetPreference {Steel ASCE 10-97}

*Source file: `SAP2000_API_Fuctions/Design/Steel/ASCE_10-97/GetPreference_{Steel_ASCE_10-97}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.ASCE\_10\_97.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Consider deflection

3 = DL deflection limit, L/Value

4 = SDL + LL deflection limit, L/Value

5 = LL deflection limit, L/Value

6 = Total deflection limit, L/Value

7 = Total camber limit, L/Value

8 = Pattern live load factor

9 = Demand/capacity ratio limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = No

Any other value = Yes

3 = DL deflection limit, L/Value

Value > 0

4 = SDL + LL deflection limit, L/Value

Value > 0

5 = LL deflection limit, L/Value

Value > 0

6 = Total deflection limit, L/Value

Value > 0

7 = Total camber limit, L/Value

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Demand/capacity ratio limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemASCE\_10\_97()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("ASCE 10-97")

   'get preference item
      ret = SapModel.DesignSteel.ASCE\_10\_97.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_ASCE_10-97}.htm)



## SetOverwrite {Steel ASCE 10-97}

*Source file: `SAP2000_API_Fuctions/Design/Steel/ASCE_10-97/SetOverwrite_{Steel_ASCE_10-97}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.ASCE\_10\_97.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 31, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Cm Major

22 = Moment coefficient, Cm Minor

23 = Bending coefficient, Cb

24 = Yield stress, Fy

25 = Compressive capacity, Pac

26 = Tensile capacity, Pat

27 = Major bending capacity, Ma3

28 = Minor bending capacity, Ma2

29 = Major shear stress, Fv2

30 = Minor shear stress, Fv3

31 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Brace Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

24 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

25 = Compressive capacity, Pac

Value >= 0; 0 means use program determined value. [F]

26 = Tensile capacity, Pat

Value >= 0; 0 means use program determined value. [F]

27 = Major bending capacity, Ma3

Value >= 0; 0 means use program determined value. [FL]

28 = Minor bending capacity, Ma2

Value >= 0; 0 means use program determined value. [FL]

29 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

30 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

31 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemASCE\_10\_97()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("ASCE 10-97")

   'set overwrite item
      ret = SapModel.DesignSteel. ASCE\_10\_97.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_ASCE_10-97}.htm)



## SetPreference {Steel ASCE 10-97}

*Source file: `SAP2000_API_Fuctions/Design/Steel/ASCE_10-97/SetPreference_{Steel_ASCE_10-97}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.ASCE\_10\_97.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Consider deflection

3 = DL deflection limit, L/Value

4 = SDL + LL deflection limit, L/Value

5 = LL deflection limit, L/Value

6 = Total deflection limit, L/Value

7 = Total camber limit, L/Value

8 = Pattern live load factor

9 = Demand/capacity ratio limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = No

Any other value = Yes

3 = DL deflection limit, L/Value

Value > 0

4 = SDL + LL deflection limit, L/Value

Value > 0

5 = LL deflection limit, L/Value

Value > 0

6 = Total deflection limit, L/Value

Value > 0

7 = Total camber limit, L/Value

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Demand/capacity ratio limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemASCE\_10\_97()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("ASCE 10-97")

   'set preference item
      ret = SapModel.DesignSteel.ASCE\_10\_97.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

GetPreference



## GetOverwrite {Steel AS 4100-1998}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AS_4100-1998/GetOverwrite_{Steel_AS_4100-1998}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Australian\_AS4100\_1998.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 46, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Steel type

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor

20 = Unbraced length ratio, Lateral Torsional Buckling

21 = Effective length factor, Ke Major Braced

22 = Effective length factor, Ke Minor Braced

23 = Effective length factor, Ke Major Sway

24 = Effective length factor, Ke Minor Sway

25 = Twist restraint factor for LTB (kt)

26 = lateral rotation restraint factor (kr)

27 = Load height factor for LTB (kl)

28 = Moment coefficient, Cm Major

29 = Moment coefficient, Cm Minor

30 = Moment modification factor, Alpha\_m

31 = Slender reduction factor, Alpha\_s

32 = Nonsway moment factor, Db Major

33 = Nonsway moment factor, Db Minor

34 = Sway moment factor, Ds Major

35 = Sway moment factor, Ds Minor

36 = Form factor, Kf

37 = Axial capacity correction factor, Kt

38 = Yield stress, Fy

39 = Compressive capacity, Nc

40 = Tensile capacity, Nt

41 = Major bending capacity, Ms33

42 = Minor bending capacity, Ms22

43 = Major bending capacity, Mb33

44 = Major shear capacity, Vu2

45 = Minor shear capacity, Vu3

46 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Moment frame

2 = Braced frame

2 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

3 = Consider deflection

0 = No

Any other value = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]}

14 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

  Value >= 0. [L}

16 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

17 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

20 = Unbraced length ratio, Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

21 = Effective length factor, Ke Major Braced

  Value >= 0; 0 means use program determined value.

22 = Effective length factor, Ke Minor Braced

  Value >= 0; 0 means use program determined value.

23 = Effective length factor, Ke Major Sway

  Value >= 0; 0 means use program determined value.

24 = Effective length factor, Ke Minor Sway

  Value >= 0; 0 means use program determined value.

25 = Twist restraint factor for LTB (kt)

  Value >= 0; 0 means use program determined value.

26 = Lateral rotation restraint factor (kr)

  Value >= 0; 0 means use program determined value.

27 = Load height factor for LTB (kl)

  Value >= 0; 0 means use program determined value.

28 = Moment coefficient, Cm Major

  Value >= 0; 0 means use program determined value.

29 = Moment coefficient, Cm Minor

  Value >= 0; 0 means use program determined value.

30 = Moment modification factor, Alpha\_m

  Value >= 0; 0 means use program determined value.

31 = Slender reduction factor, Alpha\_s

  Value >= 0; 0 means use program determined value.

32 = Nonsway moment factor, Db Major

  Value >= 0; 0 means use program determined value.

33 = Nonsway moment factor, Db Minor

  Value >= 0; 0 means use program determined value.

34 = Sway moment factor, Bs Major

  Value >= 0; 0 means use program determined value.

35 = Sway moment factor, Bs Minor

  Value >= 0; 0 means use program determined value.

36 = Form factor, Kf

  Value >= 0; 0 means use program determined value.

37 = Axial capacity correction factor, Kt

  Value >= 0; 0 means use program determined value.

38 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

39 = Compressive capacity, Nc

  Value >= 0; 0 means use program determined value. [F]

40 = Tensile capacity, Nt

  Value >= 0; 0 means use program determined value. [F]

41 = Major bending capacity, Ms33

  Value >= 0; 0 means use program determined value. [FL]

42 = Minor bending capacity, Ms22

  Value >= 0; 0 means use program determined value. [FL]

43 = Minor bending capacity, Mb33

  Value >= 0; 0 means use program determined value. [FL]

44 = Major shear capacity, Vu2

  Value >= 0; 0 means use program determined value. [F]

45 = Minor shear capacity, Vu3

  Value >= 0; 0 means use program determined value. [F]

46 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ProgDet

If this item is True then the specified value is program determined.

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAustralian\_AS4100\_1998()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

'   start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AS 4100-1998")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Australian\_AS4100\_1998.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[SetOverwrite](SetOverwrite_{Steel_AS_4100-1998}.htm)



## GetPreference {Steel AS 4100-1998}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AS_4100-1998/GetPreference_{Steel_AS_4100-1998}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Australian\_AS4100\_1998.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 17, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Structural analysis method

4 = Steel type

5 = Capacity factor, Phi bending

6 = Capacity factor, Phi compression

7 = Capacity factor, Phi tension yielding

8 = Capacity factor, Phi tension fracture

9 = Capacity factor, Phi shear

10 = Consider deflection

11 = DL deflection limit, L/Value

12 = SDL + LL deflection limit, L/Value

13 = LL deflection limit, L/Value

14 = Total load deflection limit, L/Value

15 = Total camber limit, L/Value

16 = Pattern live load factor

17 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Moment frame

2 = Braced frame

3 = Structural analysis method

1 = General 2nd Order

2 = Amplified 1st Order

4 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

5 = Capacity factor, Phi bending

Value > 0

6 = Capacity factor, Phi compression

Value > 0

7 = Capacity factor, Phi tension yielding

Value > 0

8 = Capacity factor, Phi tension fracture

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Consider deflection

  0 = No

  Any other value = Yes

11 = DL deflection limit, L/Value

  Value > 0

12 = SDL + LL deflection limit, L/Value

  Value > 0

13 = LL deflection limit, L/Value

  Value > 0

14 = Total load deflection limit, L/Value

  Value > 0

15 = Total camber limit, L/Value

  Value > 0

16 = Pattern live load factor

  Value >= 0

17 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItem Australian\_AS4100\_1998()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AS 4100-1998")

   'get preference item
      ret = SapModel.DesignSteel.Australian\_AS4100\_1998.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_AS_4100-1998}.htm)



## SetOverwrite {Steel AS 4100-1998}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AS_4100-1998/SetOverwrite_{Steel_AS_4100-1998}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Australian\_AS4100\_1998.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 46, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Steel type

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor

20 = Unbraced length ratio, Lateral Torsional Buckling

21 = Effective length factor, Ke Major Braced

22 = Effective length factor, Ke Minor Braced

23 = Effective length factor, Ke Major Sway

24 = Effective length factor, Ke Minor Sway

25 = Twist restraint factor for LTB (kt)

26 = lateral rotation restraint factor (kr)

27 = Load height factor for LTB (kl)

28 = Moment coefficient, Cm Major

29 = Moment coefficient, Cm Minor

30 = Moment modification factor, Alpha\_m

31 = Slender reduction factor, Alpha\_s

32 = Nonsway moment factor, Db Major

33 = Nonsway moment factor, Db Minor

34 = Sway moment factor, Ds Major

35 = Sway moment factor, Ds Minor

36 = Form factor, Kf

37 = Axial capacity correction factor, Kt

38 = Yield stress, Fy

39 = Compressive capacity, Nc

40 = Tensile capacity, Nt

41 = Major bending capacity, Ms33

42 = Minor bending capacity, Ms22

43 = Major bending capacity, Mb33

44 = Major shear capacity, Vu2

45 = Minor shear capacity, Vu3

46 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Moment frame

2 = Braced frame

2 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

3 = Consider deflection

0 = No

Any other value = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]}

14 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

  Value >= 0. [L}

16 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

17 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

20 = Unbraced length ratio, Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

21 = Effective length factor, Ke Major Braced

  Value >= 0; 0 means use program determined value.

22 = Effective length factor, Ke Minor Braced

  Value >= 0; 0 means use program determined value.

23 = Effective length factor, Ke Major Sway

  Value >= 0; 0 means use program determined value.

24 = Effective length factor, Ke Minor Sway

  Value >= 0; 0 means use program determined value.

25 = Twist restraint factor for LTB (kt)

  Value >= 0; 0 means use program determined value.

26 = Lateral rotation restraint factor (kr)

  Value >= 0; 0 means use program determined value.

27 = Load height factor for LTB (kl)

  Value >= 0; 0 means use program determined value.

28 = Moment coefficient, Cm Major

  Value >= 0; 0 means use program determined value.

29 = Moment coefficient, Cm Minor

  Value >= 0; 0 means use program determined value.

30 = Moment modification factor, Alpha\_m

  Value >= 0; 0 means use program determined value.

31 = Slender reduction factor, Alpha\_s

  Value >= 0; 0 means use program determined value.

32 = Nonsway moment factor, Db Major

  Value >= 0; 0 means use program determined value.

33 = Nonsway moment factor, Db Minor

  Value >= 0; 0 means use program determined value.

34 = Sway moment factor, Bs Major

  Value >= 0; 0 means use program determined value.

35 = Sway moment factor, Bs Minor

  Value >= 0; 0 means use program determined value.

36 = Form factor, Kf

  Value >= 0; 0 means use program determined value.

37 = Axial capacity correction factor, Kt

  Value >= 0; 0 means use program determined value.

38 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

39 = Compressive capacity, Nc

  Value >= 0; 0 means use program determined value. [F]

40 = Tensile capacity, Nt

  Value >= 0; 0 means use program determined value. [F]

41 = Major bending capacity, Ms33

  Value >= 0; 0 means use program determined value. [FL]

42 = Minor bending capacity, Ms22

  Value >= 0; 0 means use program determined value. [FL]

43 = Minor bending capacity, Mb33

  Value >= 0; 0 means use program determined value. [FL]

44 = Major shear capacity, Vu2

  Value >= 0; 0 means use program determined value. [F]

45 = Minor shear capacity, Vu3

  Value >= 0; 0 means use program determined value. [F]

46 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAustralian\_AS4100\_1998 ()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AS 4100-1998")

   'set overwrite item
   ret = SapModel.DesignSteel.Australian\_AS4100\_1998.SetOverwrite("8", 1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[GetOverwrite](GetOverwrite_{Steel_AS_4100-1998}.htm)



## SetPreference {Steel AS 4100-1998}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AS_4100-1998/SetPreference_{Steel_AS_4100-1998}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Australian\_AS4100\_1998.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 17, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Structural analysis method

4 = Steel type

5 = Capacity factor, Phi bending

6 = Capacity factor, Phi compression

7 = Capacity factor, Phi tension yielding

8 = Capacity factor, Phi tension fracture

9 = Capacity factor, Phi shear

10 = Consider deflection

11 = DL deflection limit, L/Value

12 = SDL + LL deflection limit, L/Value

13 = LL deflection limit, L/Value

14 = Total load deflection limit, L/Value

15 = Total camber limit, L/Value

16 = Pattern live load factor

17 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Moment frame

2 = Braced frame

3 = Structural analysis method

1 = General 2nd Order

2 = Amplified 1st Order

4 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

5 = Capacity factor, Phi bending

Value > 0

6 = Capacity factor, Phi compression

Value > 0

7 = Capacity factor, Phi tension yielding

Value > 0

8 = Capacity factor, Phi tension fracture

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Consider deflection

0 = No

Any other value = Yes

11 = DL deflection limit, L/Value

  Value > 0

12 = SDL + LL deflection limit, L/Value

  Value > 0

13 = LL deflection limit, L/Value

  Value > 0

14 = Total load deflection limit, L/Value

  Value > 0

15 = Total camber limit, L/Value

  Value > 0

16 = Pattern live load factor

  Value >= 0

17 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAustralian\_AS4100\_1998()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AS 4100-1998")

   'set preference item
      ret = SapModel.DesignSteel.Australian\_AS4100\_1998.SetPreference(1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_AS_4100-1998}.htm)



## GetOverwrite {Steel AS 4100-2020}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AS_4100-2020/GetOverwrite_{Steel_AS_4100-2020}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Australian\_AS4100\_2020.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design
procedure.

Item

This is an integer between 1 and 46, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Steel type

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit,
L/Value

6 = SDL + LL deflection
limit, L/Value

7 = LL deflection limit,
L/Value

8 = Total load deflection
limit, L/Value

9 = Total camber limit,
L/Value

10 = DL deflection limit,
absolute

11 = SDL + LL deflection
limit, absolute

12 = LL deflection limit,
absolute

13 = Total load deflection
limit, absolute

14 = Total camber limit,
absolute

15 = Specified camber

16 = Net area to total
area ratio

17 = Live load reduction
factor

18 = Unbraced length ratio,
Major

19 = Unbraced length ratio,
Minor

20 = Unbraced length ratio,
Lateral Torsional Buckling

21 = Effective length
factor, Ke Major Braced

22 = Effective length
factor, Ke Minor Braced

23 = Effective length
factor, Ke Major Sway

24 = Effective length
factor, Ke Minor Sway

25 = Twist restraint factor
for LTB (kt)

26 = lateral rotation
restraint factor (kr)

27 = Load height factor
for LTB (kl)

28 = Moment coefficient,
Cm Major

29 = Moment coefficient,
Cm Minor

30 = Moment modification
factor, Alpha\_m

31 = Slender reduction
factor, Alpha\_s

32 = Nonsway moment factor,
Db Major

33 = Nonsway moment factor,
Db Minor

34 = Sway moment factor,
Ds Major

35 = Sway moment factor,
Ds Minor

36 = Form factor, Kf

37 = Axial capacity correction
factor, Kt

38 = Yield stress, Fy

39 = Compressive capacity,
Nc

40 = Tensile capacity,
Nt

41 = Major bending capacity,
Ms33

42 = Minor bending capacity,
Ms22

43 = Major bending capacity,
Mb33

44 = Major shear capacity,
Vu2

45 = Minor shear capacity,
Vu3

46 = Demand/capacity ratio
limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Moment frame

2 = Braced frame

2 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

3 = Consider deflection

0 = No

Any other value = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

6 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

7 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

8 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

9 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

10 = DL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

11 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

12 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]}

14 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

15 = Specified camber

  Value >=
0. [L}

16 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

17 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
Major

  Value >=
0; 0 means use program determined value.

19 = Unbraced length ratio,
Minor

  Value >=
0; 0 means use program determined value.

20 = Unbraced length ratio,
Lateral Torsional Buckling

  Value >=
0; 0 means use program determined value.

21 = Effective length
factor, Ke Major Braced

  Value >=
0; 0 means use program determined value.

22 = Effective length
factor, Ke Minor Braced

  Value >=
0; 0 means use program determined value.

23 = Effective length
factor, Ke Major Sway

  Value >=
0; 0 means use program determined value.

24 = Effective length
factor, Ke Minor Sway

  Value >=
0; 0 means use program determined value.

25 = Twist restraint factor
for LTB (kt)

  Value >=
0; 0 means use program determined value.

26 = Lateral rotation
restraint factor (kr)

  Value >=
0; 0 means use program determined value.

27 = Load height factor
for LTB (kl)

  Value >=
0; 0 means use program determined value.

28 = Moment coefficient,
Cm Major

  Value >=
0; 0 means use program determined value.

29 = Moment coefficient,
Cm Minor

  Value >=
0; 0 means use program determined value.

30 = Moment modification
factor, Alpha\_m

  Value >=
0; 0 means use program determined value.

31 = Slender reduction
factor, Alpha\_s

  Value >=
0; 0 means use program determined value.

32 = Nonsway moment factor,
Db Major

  Value >=
0; 0 means use program determined value.

33 = Nonsway moment factor,
Db Minor

  Value >=
0; 0 means use program determined value.

34 = Sway moment factor,
Bs Major

  Value >=
0; 0 means use program determined value.

35 = Sway moment factor,
Bs Minor

  Value >=
0; 0 means use program determined value.

36 = Form factor, Kf

  Value >=
0; 0 means use program determined value.

37 = Axial capacity correction
factor, Kt

  Value >=
0; 0 means use program determined value.

38 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

39 = Compressive capacity,
Nc

  Value >=
0; 0 means use program determined value. [F]

40 = Tensile capacity,
Nt

  Value >=
0; 0 means use program determined value. [F]

41 = Major bending capacity,
Ms33

  Value >=
0; 0 means use program determined value. [FL]

42 = Minor bending capacity,
Ms22

  Value >=
0; 0 means use program determined value. [FL]

43 = Minor bending capacity,
Mb33

  Value >=
0; 0 means use program determined value. [FL]

44 = Major shear capacity,
Vu2

  Value >=
0; 0 means use program determined value. [F]

45 = Minor shear capacity,
Vu3

  Value >=
0; 0 means use program determined value. [F]

46 = Demand/capacity ratio
limit

  Value >=
0; 0 means use program determined value.

ProgDet

If this item is True then the specified value is program
determined.

## Remarks

This function retrieves the value of a steel design
preference item.

The function returns zero if the item is successfully
retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAustralian\_AS4100\_2020()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double
      Dim ProgDet As Boolean

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

'   start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame,
2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AS
4100-2020")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Australian\_AS4100\_2020.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.0

## See Also

[SetOverwrite](SetOverwrite_{Steel_AS_4100-2020}.htm)



## GetPreference {Steel AS 4100-2020}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AS_4100-2020/GetPreference_{Steel_AS_4100-2020}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Australian\_AS4100\_2020.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 17, inclusive, indicating
the preference item considered.

1 = Multi-response case
design

2 = Framing type

3 = Structural analysis
method

4 = Steel type

5 = Capacity factor, Phi
bending

6 = Capacity factor, Phi
compression

7 = Capacity factor, Phi
tension yielding

8 = Capacity factor, Phi
tension fracture

9 = Capacity factor, Phi
shear

10 = Consider deflection

11 = DL deflection limit,
L/Value

12 = SDL + LL deflection
limit, L/Value

13 = LL deflection limit,
L/Value

14 = Total load deflection
limit, L/Value

15 = Total camber limit,
L/Value

16 = Pattern live load
factor

17 = Demand/capacity ratio
limit

Value

The value of the considered preference item.

1 = Multi-response case
design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Moment frame

2 = Braced frame

3 = Structural analysis
method

1 = General 2nd Order

2 = Amplified 1st Order

4 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

5 = Capacity factor, Phi
bending

Value > 0

6 = Capacity factor, Phi
compression

Value > 0

7 = Capacity factor, Phi
tension yielding

Value > 0

8 = Capacity factor, Phi
tension fracture

Value > 0

9 = Capacity factor, Phi
shear

Value > 0

10 = Consider deflection

  0 = No

  Any other
value = Yes

11 = DL deflection limit,
L/Value

  Value >
0

12 = SDL + LL deflection
limit, L/Value

  Value >
0

13 = LL deflection limit,
L/Value

  Value >
0

14 = Total load deflection
limit, L/Value

  Value >
0

15 = Total camber limit,
L/Value

  Value >
0

16 = Pattern live load
factor

  Value >=
0

17 = Demand/capacity ratio
limit

  Value >
0

## Remarks

This function retrieves the value of a steel design
preference item.

The function returns zero if the item is successfully
retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItem Australian\_AS4100\_2020()
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
      ret = SapModel.DesignSteel.SetCode("AS
4100-2020")

   'get preference item
      ret = SapModel.DesignSteel.Australian\_AS4100\_2020.GetPreference(1,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.0

## See Also

[SetPreference](SetPreference_{Steel_AS_4100-2020}.htm)



## SetOverwrite {Steel AS 4100-2020}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AS_4100-2020/SetOverwrite_{Steel_AS_4100-2020}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Australian\_AS4100\_2020.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 46, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Steel type

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit,
L/Value

6 = SDL + LL deflection
limit, L/Value

7 = LL deflection limit,
L/Value

8 = Total load deflection
limit, L/Value

9 = Total camber limit,
L/Value

10 = DL deflection limit,
absolute

11 = SDL + LL deflection
limit, absolute

12 = LL deflection limit,
absolute

13 = Total load deflection
limit, absolute

14 = Total camber limit,
absolute

15 = Specified camber

16 = Net area to total
area ratio

17 = Live load reduction
factor

18 = Unbraced length ratio,
Major

19 = Unbraced length ratio,
Minor

20 = Unbraced length ratio,
Lateral Torsional Buckling

21 = Effective length
factor, Ke Major Braced

22 = Effective length
factor, Ke Minor Braced

23 = Effective length
factor, Ke Major Sway

24 = Effective length
factor, Ke Minor Sway

25 = Twist restraint factor
for LTB (kt)

26 = lateral rotation
restraint factor (kr)

27 = Load height factor
for LTB (kl)

28 = Moment coefficient,
Cm Major

29 = Moment coefficient,
Cm Minor

30 = Moment modification
factor, Alpha\_m

31 = Slender reduction
factor, Alpha\_s

32 = Nonsway moment factor,
Db Major

33 = Nonsway moment factor,
Db Minor

34 = Sway moment factor,
Ds Major

35 = Sway moment factor,
Ds Minor

36 = Form factor, Kf

37 = Axial capacity correction
factor, Kt

38 = Yield stress, Fy

39 = Compressive capacity,
Nc

40 = Tensile capacity,
Nt

41 = Major bending capacity,
Ms33

42 = Minor bending capacity,
Ms22

43 = Major bending capacity,
Mb33

44 = Major shear capacity,
Vu2

45 = Minor shear capacity,
Vu3

46 = Demand/capacity ratio
limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Moment frame

2 = Braced frame

2 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

3 = Consider deflection

0 = No

Any other value = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

6 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

7 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

8 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

9 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

10 = DL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

11 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

12 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]}

14 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

15 = Specified camber

  Value >=
0. [L}

16 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

17 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
Major

  Value >=
0; 0 means use program determined value.

19 = Unbraced length ratio,
Minor

  Value >=
0; 0 means use program determined value.

20 = Unbraced length ratio,
Lateral Torsional Buckling

  Value >=
0; 0 means use program determined value.

21 = Effective length
factor, Ke Major Braced

  Value >=
0; 0 means use program determined value.

22 = Effective length
factor, Ke Minor Braced

  Value >=
0; 0 means use program determined value.

23 = Effective length
factor, Ke Major Sway

  Value >=
0; 0 means use program determined value.

24 = Effective length
factor, Ke Minor Sway

  Value >=
0; 0 means use program determined value.

25 = Twist restraint factor
for LTB (kt)

  Value >=
0; 0 means use program determined value.

26 = Lateral rotation
restraint factor (kr)

  Value >=
0; 0 means use program determined value.

27 = Load height factor
for LTB (kl)

  Value >=
0; 0 means use program determined value.

28 = Moment coefficient,
Cm Major

  Value >=
0; 0 means use program determined value.

29 = Moment coefficient,
Cm Minor

  Value >=
0; 0 means use program determined value.

30 = Moment modification
factor, Alpha\_m

  Value >=
0; 0 means use program determined value.

31 = Slender reduction
factor, Alpha\_s

  Value >=
0; 0 means use program determined value.

32 = Nonsway moment factor,
Db Major

  Value >=
0; 0 means use program determined value.

33 = Nonsway moment factor,
Db Minor

  Value >=
0; 0 means use program determined value.

34 = Sway moment factor,
Bs Major

  Value >=
0; 0 means use program determined value.

35 = Sway moment factor,
Bs Minor

  Value >=
0; 0 means use program determined value.

36 = Form factor, Kf

  Value >=
0; 0 means use program determined value.

37 = Axial capacity correction
factor, Kt

  Value >=
0; 0 means use program determined value.

38 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

39 = Compressive capacity,
Nc

  Value >=
0; 0 means use program determined value. [F]

40 = Tensile capacity,
Nt

  Value >=
0; 0 means use program determined value. [F]

41 = Major bending capacity,
Ms33

  Value >=
0; 0 means use program determined value. [FL]

42 = Minor bending capacity,
Ms22

  Value >=
0; 0 means use program determined value. [FL]

43 = Minor bending capacity,
Mb33

  Value >=
0; 0 means use program determined value. [FL]

44 = Major shear capacity,
Vu2

  Value >=
0; 0 means use program determined value. [F]

45 = Minor shear capacity,
Vu3

  Value >=
0; 0 means use program determined value. [F]

46 = Demand/capacity ratio
limit

  Value >=
0; 0 means use program determined value.

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

## Remarks

This function sets the value of a steel design overwrite
item.

The function returns zero if the item is successfully
set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAustralian\_AS4100\_2020
()
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
      ret = SapModel.DesignSteel.SetCode("AS
4100-2020")

   'set overwrite item
   ret = SapModel.DesignSteel.Australian\_AS4100\_2020.SetOverwrite("8",
1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.0

## See Also

[GetOverwrite](GetOverwrite_{Steel_AS_4100-2020}.htm)



## SetPreference {Steel AS 4100-2020}

*Source file: `SAP2000_API_Fuctions/Design/Steel/AS_4100-2020/SetPreference_{Steel_AS_4100-2020}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Australian\_AS4100\_2020.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 17, inclusive, indicating
the preference item considered.

1 = Multi-response case
design

2 = Framing type

3 = Structural analysis
method

4 = Steel type

5 = Capacity factor, Phi
bending

6 = Capacity factor, Phi
compression

7 = Capacity factor, Phi
tension yielding

8 = Capacity factor, Phi
tension fracture

9 = Capacity factor, Phi
shear

10 = Consider deflection

11 = DL deflection limit,
L/Value

12 = SDL + LL deflection
limit, L/Value

13 = LL deflection limit,
L/Value

14 = Total load deflection
limit, L/Value

15 = Total camber limit,
L/Value

16 = Pattern live load
factor

17 = Demand/capacity ratio
limit

Value

The value of the considered preference item.

1 = Multi-response case
design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Moment frame

2 = Braced frame

3 = Structural analysis
method

1 = General 2nd Order

2 = Amplified 1st Order

4 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

5 = Capacity factor, Phi
bending

Value > 0

6 = Capacity factor, Phi
compression

Value > 0

7 = Capacity factor, Phi
tension yielding

Value > 0

8 = Capacity factor, Phi
tension fracture

Value > 0

9 = Capacity factor, Phi
shear

Value > 0

10 = Consider deflection

0 = No

Any other value = Yes

11 = DL deflection limit,
L/Value

  Value >
0

12 = SDL + LL deflection
limit, L/Value

  Value >
0

13 = LL deflection limit,
L/Value

  Value >
0

14 = Total load deflection
limit, L/Value

  Value >
0

15 = Total camber limit,
L/Value

  Value >
0

16 = Pattern live load
factor

  Value >=
0

17 = Demand/capacity ratio
limit

  Value >
0

## Remarks

This function sets the value of a steel design preference
item.

The function returns zero if the item is successfully
set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAustralian\_AS4100\_2020()
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
      ret = SapModel.DesignSteel.SetCode("AS
4100-2020")

   'set preference item
      ret = SapModel.DesignSteel.Australian\_AS4100\_2020.SetPreference(1,
7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.0

## See Also

[GetPreference](GetPreference_{Steel_AS_4100-2020}.htm)



## GetOverwrite {Steel BS5950 2000}

*Source file: `SAP2000_API_Fuctions/Design/Steel/BS5950_2000/GetOverwrite_{Steel_BS5950_2000}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.BS5950\_2000.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 32, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Uniform moment factor, m Major

22 = Uniform moment factor, m Minor

23 = Eqv. uniform moment factor, mLT

24 = Yield stress, Fy

25 = Compressive capacity, Pc

26 = Tensile capacity, Pt

27 = Major bending capacity, Mc3

28 = Minor bending capacity, Mc2

29 = Buckling resistance moment, Mb

30 = Major shear capacity, Pv2

31 = Minor shear capacity, Pv3

32 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Uniform moment factor, m Major

Value >= 0; 0 means use program determined value.

22 = Uniform moment factor, m Minor

Value >= 0; 0 means use program determined value.

23 = Eqv. Uniform moment factor, mLT

Value >= 0; 0 means use program determined value.

24 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

25 = Compressive capacity, Pc

Value >= 0; 0 means use program determined value. [F]

26 = Tensile capacity, Pt

Value >= 0; 0 means use program determined value. [F]

27 = Major bending capacity, Mc3

Value >= 0; 0 means use program determined value. [FL]

28 = Minor bending capacity, Mc2

Value >= 0; 0 means use program determined value. [FL]

29 = Buckling resistance moment, Mb

Value >= 0; 0 means use program determined value. [FL]

30 = Major shear capacity, Pv2

Value >= 0; 0 means use program determined value. [F]

31 = Minor shear capacity, Pv3

Value >= 0; 0 means use program determined value. [F]

32 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemBS5950\_2000()
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

   'createSapModelobject
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("BS5950 2000")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.BS5950\_2000.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_BS5950_2000}.htm)



## GetPreference {Steel BS5950 2000}

*Source file: `SAP2000_API_Fuctions/Design/Steel/BS5950_2000/GetPreference_{Steel_BS5950_2000}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.BS5950\_2000.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Consider deflection

3 = DL deflection limit, L/Value

4 = SDL + LL deflection limit, L/Value

5 = LL deflection limit, L/Value

6 = Total deflection limit, L/Value

7 = Total camber limit, L/Value

8 = Pattern live load factor

9 = Demand/capacity ratio limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = No

Any other value = Yes

3 = DL deflection limit, L/Value

Value > 0

4 = SDL + LL deflection limit, L/Value

Value > 0

5 = LL deflection limit, L/Value

Value > 0

6 = Total deflection limit, L/Value

Value > 0

7 = Total camber limit, L/Value

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Demand/capacity ratio limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemBS5950\_2000()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("BS5950 2000")

   'get preference item
      ret = SapModel.DesignSteel.BS5950\_2000.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_BS5950_2000}.htm)



## SetOverwrite {Steel BS5950 2000}

*Source file: `SAP2000_API_Fuctions/Design/Steel/BS5950_2000/SetOverwrite_{Steel_BS5950_2000}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.BS5950\_2000.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 32, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Uniform moment factor, m Major

22 = Uniform moment factor, m Minor

23 = Eqv. uniform moment factor, mLT

24 = Yield stress, Fy

25 = Compressive capacity, Pc

26 = Tensile capacity, Pt

27 = Major bending capacity, Mc3

28 = Minor bending capacity, Mc2

29 = Buckling resistance moment, Mb

30 = Major shear capacity, Pv2

31 = Minor shear capacity, Pv3

32 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Uniform moment factor, m Major

Value >= 0; 0 means use program determined value.

22 = Uniform moment factor, m Minor

Value >= 0; 0 means use program determined value.

23 = Eqv. Uniform moment factor, mLT

Value >= 0; 0 means use program determined value.

24 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

25 = Compressive capacity, Pc

Value >= 0; 0 means use program determined value. [F]

26 = Tensile capacity, Pt

Value >= 0; 0 means use program determined value. [F]

27 = Major bending capacity, Mc3

Value >= 0; 0 means use program determined value. [FL]

28 = Minor bending capacity, Mc2

Value >= 0; 0 means use program determined value. [FL]

29 = Buckling resistance moment, Mb

Value >= 0; 0 means use program determined value. [FL]

30 = Major shear capacity, Pv2

Value >= 0; 0 means use program determined value. [F]

31 = Minor shear capacity, Pv3

Value >= 0; 0 means use program determined value. [F]

32 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemBS5950\_2000()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("BS5950 2000")

   'set overwrite item
      ret = SapModel.DesignSteel.BS5950\_2000.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_BS5950_2000}.htm)



## SetPreference {Steel BS5950 2000}

*Source file: `SAP2000_API_Fuctions/Design/Steel/BS5950_2000/SetPreference_{Steel_BS5950_2000}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.BS5950\_2000.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Consider deflection

3 = DL deflection limit, L/Value

4 = SDL + LL deflection limit, L/Value

5 = LL deflection limit, L/Value

6 = Total deflection limit, L/Value

7 = Total camber limit, L/Value

8 = Pattern live load factor

9 = Demand/capacity ratio limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = No

Any other value = Yes

3 = DL deflection limit, L/Value

Value > 0

4 = SDL + LL deflection limit, L/Value

Value > 0

5 = LL deflection limit, L/Value

Value > 0

6 = Total deflection limit, L/Value

Value > 0

7 = Total camber limit, L/Value

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Demand/capacity ratio limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemBS5950\_2000()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("BS5950 2000")

   'set preference item
      ret = SapModel.DesignSteel.BS5950\_2000.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_BS5950_2000}.htm)



## GetOverwrite {Steel BS5950 90}

*Source file: `SAP2000_API_Fuctions/Design/Steel/BS5950_90/GetOverwrite_{Steel_BS5950_90}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.BS5950\_90.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 32, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Uniform moment factor, m Major

22 = Uniform moment factor, m Minor

23 = Slenderness correction factor, n

24 = Yield stress, Fy

25 = Compressive capacity, Pc

26 = Tensile capacity, Pt

27 = Major bending capacity, Mc3

28 = Minor bending capacity, Mc2

29 = Buckling resistance moment, Mb

30 = Major shear capacity, Pv2

31 = Minor shear capacity, Pv3

32 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Uniform moment factor, m Major

Value >= 0; 0 means use program determined value.

22 = Uniform moment factor, m Minor

Value >= 0; 0 means use program determined value.

23 = Slenderness correction factor, n

Value >= 0; 0 means use program determined value.

24 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

25 = Compressive capacity, Pc

Value >= 0; 0 means use program determined value. [F]

26 = Tensile capacity, Pt

Value >= 0; 0 means use program determined value. [F]

27 = Major bending capacity, Mc3

Value >= 0; 0 means use program determined value. [FL]

28 = Minor bending capacity, Mc2

Value >= 0; 0 means use program determined value. [FL]

29 = Buckling resistance moment, Mb

Value >= 0; 0 means use program determined value. [FL]

30 = Major shear capacity, Pv2

Value >= 0; 0 means use program determined value. [F]

31 = Minor shear capacity, Pv3

Value >= 0; 0 means use program determined value. [F]

32 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemBS5950\_90()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("BS5950 90")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.BS5950\_90.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_BS5950_90}.htm)



## GetPreference {Steel BS5950 90}

*Source file: `SAP2000_API_Fuctions/Design/Steel/BS5950_90/GetPreference_{Steel_BS5950_90}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.BS5950\_90.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Consider deflection

3 = DL deflection limit, L/Value

4 = SDL + LL deflection limit, L/Value

5 = LL deflection limit, L/Value

6 = Total deflection limit, L/Value

7 = Total camber limit, L/Value

8 = Pattern live load factor

9 = Demand/capacity ratio limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = No

Any other value = Yes

3 = DL deflection limit, L/Value

Value > 0

4 = SDL + LL deflection limit, L/Value

Value > 0

5 = LL deflection limit, L/Value

Value > 0

6 = Total deflection limit, L/Value

Value > 0

7 = Total camber limit, L/Value

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Demand/capacity ratio limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemBS5950\_90()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("BS5950 90")

   'get preference item
      ret = SapModel.DesignSteel.BS5950\_90.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_BS5950_90}.htm)



## SetOverwrite {Steel BS5950 90}

*Source file: `SAP2000_API_Fuctions/Design/Steel/BS5950_90/SetOverwrite_{Steel_BS5950_90}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.BS5950\_90.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 32, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Uniform moment factor, m Major

22 = Uniform moment factor, m Minor

23 = Slenderness correction factor, n

24 = Yield stress, Fy

25 = Compressive capacity, Pc

26 = Tensile capacity, Pt

27 = Major bending capacity, Mc3

28 = Minor bending capacity, Mc2

29 = Buckling resistance moment, Mb

30 = Major shear capacity, Pv2

31 = Minor shear capacity, Pv3

32 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Uniform moment factor, m Major

Value >= 0; 0 means use program determined value.

22 = Uniform moment factor, m Minor

Value >= 0; 0 means use program determined value.

23 = Slenderness correction factor, n

Value >= 0; 0 means use program determined value.

24 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

25 = Compressive capacity, Pc

Value >= 0; 0 means use program determined value. [F]

26 = Tensile capacity, Pt

Value >= 0; 0 means use program determined value. [F]

27 = Major bending capacity, Mc3

Value >= 0; 0 means use program determined value. [FL]

28 = Minor bending capacity, Mc2

Value >= 0; 0 means use program determined value. [FL]

29 = Buckling resistance moment, Mb

Value >= 0; 0 means use program determined value. [FL]

30 = Major shear capacity, Pv2

Value >= 0; 0 means use program determined value. [F]

31 = Minor shear capacity, Pv3

Value >= 0; 0 means use program determined value. [F]

32 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemBS5950\_90()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("BS5950 90")

   'set overwrite item
      ret = SapModel.DesignSteel.BS5950\_90.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_BS5950_90}.htm)



## SetPreference {Steel BS5950 90}

*Source file: `SAP2000_API_Fuctions/Design/Steel/BS5950_90/SetPreference_{Steel_BS5950_90}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.BS5950\_90.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Consider deflection

3 = DL deflection limit, L/Value

4 = SDL + LL deflection limit, L/Value

5 = LL deflection limit, L/Value

6 = Total deflection limit, L/Value

7 = Total camber limit, L/Value

8 = Pattern live load factor

9 = Demand/capacity ratio limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = No

Any other value = Yes

3 = DL deflection limit, L/Value

Value > 0

4 = SDL + LL deflection limit, L/Value

Value > 0

5 = LL deflection limit, L/Value

Value > 0

6 = Total deflection limit, L/Value

Value > 0

7 = Total camber limit, L/Value

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Demand/capacity ratio limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemBS5950\_90()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("BS5950 90")

   'set preference item
      ret = SapModel.DesignSteel.BS5950\_90.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_BS5950_90}.htm)



## GetOverwrite {Steel CAN CSA S16-01}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CAN_CSA_S16-01/GetOverwrite_{Steel_CAN_CSA_S16-01}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_01.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 39, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor LTB

19 = Unbraced length ratio, Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Effective length factor, K LTB

23 = Moment coefficient, Omega1 Major

24 = Moment coefficient, Omega1 Minor

25 = Bending coefficient, Omega2

26 = Nonsway moment factor, U1 Major

27 = Nonsway moment factor, U1 Minor

28 = Sway moment factor, U2 Major

29 = Sway moment factor, U2 Minor

30 = Parameter for compressive resistance, n

31 = Yield stress, Fy

32 = Expected to specified Fy ratio, Ry

33 = Compressive resistance, Cr

34 = Tensile resistance, Tr

35 = Major bending resistance, Mr3

36 = Minor bending resistance, Mr2

37 = Major shear resistance, Vr2

38 = Minor shear resistance, Vr3

39 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

2 = Consider deflection

0 = No

Any other value = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]}

13 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

  Value >= 0. [L}

15 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

16 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

  Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

  Value >= 0; 0 means use program determined value.

22 = Effective length factor, K LTB

  Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Omega1 Major

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, Omega1 Minor

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, Omega2

  Value >= 0; 0 means use program determined value.

26 = Nonsway moment factor, U1 Major

  Value >= 0; 0 means use program determined value.

27 = Nonsway moment factor, U1 Minor

  Value >= 0; 0 means use program determined value.

28 = Sway moment factor, U2 Major

  Value >= 0; 0 means use program determined value.

29 = Sway moment factor, U2 Minor

  Value >= 0; 0 means use program determined value.

30 = Parameter for compressive resistance, n

  Value >= 0; 0 means use program determined value.

31 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

32 = Expected to specified Fy ratio, Ry

  Value >= 0; 0 means use program determined value. [F/L2]=

33 = Compressive resistance, Cr

  Value >= 0; 0 means use program determined value. [F]

34 = Tensile resistance, Tr

  Value >= 0; 0 means use program determined value. [F]

35 = Major bending resistance, Mr3

  Value >= 0; 0 means use program determined value. [FL]

36 = Minor bending resistance, Mr2

  Value >= 0; 0 means use program determined value. [FL]

37 = Major shear resistance, Vr2

  Value >= 0; 0 means use program determined value. [F]

38 = Minor shear resistance, Vr3

  Value >= 0; 0 means use program determined value. [F]

39 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemCanadian\_S16\_01 ()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CAN/CSA-S16-01")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Canadian\_S16\_01.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[SetOverwrite](SetOverwrite_{Steel_CAN_CSA_S16-01}.htm)



## GetPreference {Steel CAN CSA S16-01}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CAN_CSA_S16-01/GetPreference_{Steel_CAN_CSA_S16-01}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_01.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 21, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

4 = Ductility related modification factor, Rd

5 = Overstrength related modification factor, Ro

6 = Capacity factor, Phi bending

7 = Capacity factor, Phi compression

8 = Capacity factor, Phi tension

9 = Capacity factor, Phi shear

10 = Slender section modification

11 = Ignore seismic code

12 = Ignore special seismic load

13 = Doubler plate is plug welded

14 = Consider deflection

15 = DL deflection limit, L/Value

16 = SDL + LL deflection limit, L/Value

17 = LL deflection limit, L/Value

18 = Total load deflection limit, L/Value

19 = Total camber limit, L/Value

20 = Pattern live load factor

21 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

Value > 0

4 = Ductility related modification factor, Rd

Value > 0

5 = Overstrength related modification factor, Ro

Value > 0

6 = Capacity factor, Phi bending

Value > 0

7 = Capacity factor, Phi compression

Value > 0

8 = Capacity factor, Phi tension

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Slender section modification

  1 = Modified geometry

  2 = modified Fy

11 = Ignore seismic code

  0 = No

  Any other value = Yes

12 = Ignore special seismic load

  0 = No

  Any other value = Yes

13 = Doubler plate is plug welded

  0 = No

  Any other value = Yes

14 = Consider deflection

  0 = No

  Any other value = Yes

15 = DL deflection limit, L/Value

  Value > 0

16 = SDL + LL deflection limit, L/Value

  Value > 0

17 = LL deflection limit, L/Value

  Value > 0

18 = Total load deflection limit, L/Value

  Value > 0

19 = Total camber limit, L/Value

  Value > 0

20 = Pattern live load factor

  Value >= 0

21 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemCanadian\_S16\_01 ()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CAN/CSA-S16-01")

   'get preference item
      ret = SapModel.DesignSteel.Canadian\_S16\_01.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_CAN_CSA_S16-01}.htm)



## SetOverwrite {Steel CAN CSA S16-01}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CAN_CSA_S16-01/SetOverwrite_{Steel_CAN_CSA_S16-01}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_01.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 39, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor LTB

19 = Unbraced length ratio, Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Effective length factor, K LTB

23 = Moment coefficient, Omega1 Major

24 = Moment coefficient, Omega1 Minor

25 = Bending coefficient, Omega2

26 = Nonsway moment factor, U1 Major

27 = Nonsway moment factor, U1 Minor

28 = Sway moment factor, U2 Major

29 = Sway moment factor, U2 Minor

30 = Parameter for compressive resistance, n

31 = Yield stress, Fy

32 = Expected to specified Fy ratio, Ry

33 = Compressive resistance, Cr

34 = Tensile resistance, Tr

35 = Major bending resistance, Mr3

36 = Minor bending resistance, Mr2

37 = Major shear resistance, Vr2

38 = Minor shear resistance, Vr3

39 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

2 = Consider deflection

0 = No

Any other value = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]}

13 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

  Value >= 0. [L}

15 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

16 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

  Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

  Value >= 0; 0 means use program determined value.

22 = Effective length factor, K LTB

  Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Omega1 Major

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, Omega1 Minor

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, Omega2

  Value >= 0; 0 means use program determined value.

26 = Nonsway moment factor, U1 Major

  Value >= 0; 0 means use program determined value.

27 = Nonsway moment factor, U1 Minor

  Value >= 0; 0 means use program determined value.

28 = Sway moment factor, U2 Major

  Value >= 0; 0 means use program determined value.

29 = Sway moment factor, U2 Minor

  Value >= 0; 0 means use program determined value.

30 = Parameter for compressive resistance, n

  Value >= 0; 0 means use program determined value.

31 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

32 = Expected to specified Fy ratio, Ry

  Value >= 0; 0 means use program determined value. [F/L2]=

33 = Compressive resistance, Cr

  Value >= 0; 0 means use program determined value. [F]

34 = Tensile resistance, Tr

  Value >= 0; 0 means use program determined value. [F]

35 = Major bending resistance, Mr3

  Value >= 0; 0 means use program determined value. [FL]

36 = Minor bending resistance, Mr2

  Value >= 0; 0 means use program determined value. [FL]

37 = Major shear resistance, Vr2

  Value >= 0; 0 means use program determined value. [F]

38 = Minor shear resistance, Vr3

  Value >= 0; 0 means use program determined value. [F]

39 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemCanadian\_S16\_01 ()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CAN/CSA-S16-01")

   'set overwrite item
      ret = SapModel.DesignSteel.Canadian\_S16\_01.SetOverwrite("8", 1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[GetOverwrite](GetOverwrite_{Steel_CAN_CSA_S16-01}.htm)



## SetPreference {Steel CAN CSA S16-01}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CAN_CSA_S16-01/SetPreference_{Steel_CAN_CSA_S16-01}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_01.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 21, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

4 = Ductility related modification factor, Rd

5 = Overstrength related modification factor, Ro

6 = Capacity factor, Phi bending

7 = Capacity factor, Phi compression

8 = Capacity factor, Phi tension

9 = Capacity factor, Phi shear

10 = Slender section modification

11 = Ignore seismic code

12 = Ignore special seismic load

13 = Doubler plate is plug welded

14 = Consider deflection

15 = DL deflection limit, L/Value

16 = SDL + LL deflection limit, L/Value

17 = LL deflection limit, L/Value

18 = Total load deflection limit, L/Value

19 = Total camber limit, L/Value

20 = Pattern live load factor

21 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

Value > 0

4 = Ductility related modification factor, Rd

Value > 0

5 = Overstrength related modification factor, Ro

Value > 0

6 = Capacity factor, Phi bending

Value > 0

7 = Capacity factor, Phi compression

Value > 0

8 = Capacity factor, Phi tension

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Slender section modification

  1 = Modified geometry

  2 = modified Fy

11 = Ignore seismic code

  0 = No

  Any other value = Yes

12 = Ignore special seismic load

  0 = No

  Any other value = Yes

13 = Doubler plate is plug welded

  0 = No

  Any other value = Yes

14 = Consider deflection

  0 = No

  Any other value = Yes

15 = DL deflection limit, L/Value

  Value > 0

16 = SDL + LL deflection limit, L/Value

  Value > 0

17 = LL deflection limit, L/Value

  Value > 0

18 = Total load deflection limit, L/Value

  Value > 0

19 = Total camber limit, L/Value

  Value > 0

20 = Pattern live load factor

  Value >= 0

21 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemCanadian\_S16\_01 ()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CAN/CSA-S16-01")

   'set preference item
      ret = SapModel.DesignSteel.Canadian\_S16\_01.SetPreference(1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_CAN_CSA_S16-01}.htm)



## GetOverwrite {Steel CISC 95}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CISC_95/GetOverwrite_{Steel_CISC_95}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.CISC\_95.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 35, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Omega1 Major

22 = Moment coefficient, Omega1 Minor

23 = Bending coefficient, Cb

24 = Non-sway moment factor, U1 Major

25 = Non-sway moment factor, U1 Minor

26 = Sway moment factor, U2 Major

27 = Sway moment factor, U2 Minor

28 = Yield stress, Fy

29 = Compressive capacity, Cr

30 = Tensile capacity, Tr

31 = Major bending capacity, Mr3

32 = Minor bending capacity, Mr2

33 = Major shear capacity, Vr2

34 = Minor shear capacity, Vr3

35 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Omega1 Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Omega1 Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Omega2

Value >= 0; 0 means use program determined value.

24 = Nonsway moment factor, U1 Major

Value >= 0; 0 means use program determined value.

25 = Nonsway moment factor, U1 Minor

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, U2 Major

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, U2 Minor

Value >= 0; 0 means use program determined value.

28 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

29 = Compressive capacity, Cr

Value >= 0; 0 means use program determined value. [F]

30 = Tensile capacity, Tr

Value >= 0; 0 means use program determined value. [F]

31 = Major bending capacity, Mr3

Value >= 0; 0 means use program determined value. [FL]

32 = Minor bending capacity, Mr2

Value >= 0; 0 means use program determined value. [FL]

33 = Major shear capacity, Vr2

Value >= 0; 0 means use program determined value. [F]

34 = Minor shear capacity, Vr3

Value >= 0; 0 means use program determined value. [F]

35 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemCISC\_95()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CISC 95")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.CISC\_95.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_CISC_95}.htm)



## GetPreference {Steel CISC 95}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CISC_95/GetPreference_{Steel_CISC_95}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.CISC\_95.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1 = Framing type

2 = Phi bending

3 = Phi compression

4 = Phi tension

5 = Phi shear

6 = Consider deflection

7 = DL deflection limit, L/Value

8 = SDL + LL deflection limit, L/Value

9 = LL deflection limit, L/Value

10 = Total deflection limit, L/Value

11 = Total camber limit, L/Value

12 = Pattern live load factor

13 = Demand/capacity ratio limit

14 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Phi bending

Value > 0

3 = Phi compression

Value > 0

4 = Phi tension

Value > 0

5 = Phi shear

Value > 0

6 = Consider deflection

0 = No

Any other value = Yes

7 = DL deflection limit, L/Value

Value > 0

8 = SDL + LL deflection limit, L/Value

Value > 0

9 = LL deflection limit, L/Value

Value > 0

10 = Total load deflection limit, L/Value

Value > 0

11 = Total camber limit, L/Value

Value > 0

12 = Pattern live load factor

Value >= 0

13 = Demand/capacity ratio limit

Value > 0

14 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemCISC\_95()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CISC 95")

   'get preference item
      ret = SapModel.DesignSteel.CISC\_95.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_CISC_95}.htm)



## SetOverwrite {Steel CISC 95}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CISC_95/SetOverwrite_{Steel_CISC_95}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.CISC\_95.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 35, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, Omega1 Major

22 = Moment coefficient, Omega1 Minor

23 = Bending coefficient, Cb

24 = Non-sway moment factor, U1 Major

25 = Non-sway moment factor, U1 Minor

26 = Sway moment factor, U2 Major

27 = Sway moment factor, U2 Minor

28 = Yield stress, Fy

29 = Compressive capacity, Cr

30 = Tensile capacity, Tr

31 = Major bending capacity, Mr3

32 = Minor bending capacity, Mr2

33 = Major shear capacity, Vr2

34 = Minor shear capacity, Vr3

35 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, Omega1 Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Omega1 Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, Omega2

Value >= 0; 0 means use program determined value.

24 = Non-sway moment factor, U1 Major

Value >= 0; 0 means use program determined value.

25 = Non-sway moment factor, U1 Minor

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, U2 Major

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, U2 Minor

Value >= 0; 0 means use program determined value.

28 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

29 = Compressive capacity, Cr

Value >= 0; 0 means use program determined value. [F]

30 = Tensile capacity, Tr

Value >= 0; 0 means use program determined value. [F]

31 = Major bending capacity, Mr3

Value >= 0; 0 means use program determined value. [FL]

32 = Minor bending capacity, Mr2

Value >= 0; 0 means use program determined value. [FL]

33 = Major shear capacity, Vr2

Value >= 0; 0 means use program determined value. [F]

34 = Minor shear capacity, Vr3

Value >= 0; 0 means use program determined value. [F]

35 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemCISC\_95()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CISC 95")

   'set overwrite item
      ret = SapModel.DesignSteel.CISC\_95.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_CISC_95}.htm)



## SetPreference {Steel CISC 95}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CISC_95/SetPreference_{Steel_CISC_95}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.CISC\_95.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1 = Framing type

2 = Phi bending

3 = Phi compression

4 = Phi tension

5 = Phi shear

6 = Consider deflection

7 = DL deflection limit, L/Value

8 = SDL + LL deflection limit, L/Value

9 = LL deflection limit, L/Value

10 = Total deflection limit, L/Value

11 = Total camber limit, L/Value

12 = Pattern live load factor

13 = Demand/capacity ratio limit

14 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = Phi bending

Value > 0

3 = Phi compression

Value > 0

4 = Phi tension

Value > 0

5 = Phi shear

Value > 0

6 = Consider deflection

0 = No

Any other value = Yes

7 = DL deflection limit, L/Value

Value > 0

8 = SDL + LL deflection limit, L/Value

Value > 0

9 = LL deflection limit, L/Value

Value > 0

10 = Total load deflection limit, L/Value

Value > 0

11 = Total camber limit, L/Value

Value > 0

12 = Pattern live load factor

Value >= 0

13 = Demand/capacity ratio limit

Value > 0

14 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemCISC\_95()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CISC 95")

   'set preference item
      ret = SapModel.DesignSteel.CISC\_95.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_CISC_95}.htm)



## GetOverwrite {Steel CSA S16-09}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-09/GetOverwrite_{Steel_CSA_S16-09}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_09.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design
procedure.

Item

This is an integer between 1 and 41, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit,
L/Value

5 = SDL + LL deflection
limit, L/Value

6 = LL deflection limit,
L/Value

7 = Total load deflection
limit, L/Value

8 = Total camber limit,
L/Value

9 = DL deflection limit,
absolute

10 = SDL + LL deflection
limit, absolute

11 = LL deflection limit,
absolute

12 = Total load deflection
limit, absolute

13 = Total camber limit,
absolute

14 = Specified camber

15 = Net area to total
area ratio

16 = Live load reduction
factor

17 = Unbraced length ratio,
Major

18 = Unbraced length ratio,
Minor LTB

19 = Unbraced length ratio,
Lateral Torsional Buckling

20 = Effective length
factor, K Major

21 = Effective length
factor, K Minor

22 = Effective length
factor, K LTB

23 = Moment coefficient,
Omega1 Major

24 = Moment coefficient,
Omega1 Minor

25 = Bending coefficient,
Omega2

26 = Nonsway moment factor,
U1 Major

27 = Nonsway moment factor,
U1 Minor

28 = Sway moment factor,
U2 Major

29 = Sway moment factor,
U2 Minor

30 = Parameter for compressive
resistance, n

31 = Yield stress, Fy

32 = Expected to specified
Fy ratio, Ry

33
= Compressive resistance, Cr

34 = Tensile resistance,
Tr

35 = Major bending resistance,
Mr3

36 = Minor bending resistance,
Mr2

37 = Major shear resistance,
Vr2

38 = Minor shear resistance,
Vr3

39 = Demand/capacity ratio
limit

40 = Is HSS sections class
H?

41 = Warping torsional
constant Cw

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

2 = Consider deflection

0 = No

Any other value = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

5 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

6 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

7 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

8 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

9 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

10 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

11 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

12 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

14 = Specified camber

  Value >=
0. [L]

15 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

16 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

17 = Unbraced length ratio,
Major

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
Minor

  Value >=
0; 0 means use program determined value.

19 = Unbraced length ratio,
Lateral Torsional Buckling

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor, K Major

  Value >=
0; 0 means use program determined value.

21 = Effective length
factor, K Minor

  Value >=
0; 0 means use program determined value.

22 = Effective length
factor, K LTB

  Value >=
0; 0 means use program determined value.

23 = Moment coefficient,
Omega1 Major

  Value >=
0; 0 means use program determined value.

24 = Moment coefficient,
Omega1 Minor

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
Omega2

  Value >=
0; 0 means use program determined value.

26 = Nonsway moment factor,
U1 Major

  Value >=
0; 0 means use program determined value.

27 = Nonsway moment factor,
U1 Minor

  Value >=
0; 0 means use program determined value.

28 = Sway moment factor,
U2 Major

  Value >=
0; 0 means use program determined value.

29 = Sway moment factor,
U2 Minor

  Value >=
0; 0 means use program determined value.

30 = Parameter for compressive
resistance, n

  Value >=
0; 0 means use program determined value.

31 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

32 = Expected to specified
Fy ratio, Ry

  Value >=
0; 0 means use program determined value. [F/L2]=

33 = Compressive resistance,
Cr

  Value >=
0; 0 means use program determined value. [F]

34 = Tensile resistance,
Tr

  Value >=
0; 0 means use program determined value. [F]

35 = Major bending resistance,
Mr3

  Value >=
0; 0 means use program determined value. [FL]

36 = Minor bending resistance,
Mr2

  Value >=
0; 0 means use program determined value. [FL]

37 = Major shear resistance,
Vr2

  Value >=
0; 0 means use program determined value. [F]

38 = Minor shear resistance,
Vr3

  Value >=
0; 0 means use program determined value. [F]

39 = Demand/capacity ratio
limit

  Value >=
0; 0 means use program determined value.

40 = Is HSS sections class
H?

  0 = Program
Determined

  1 = No

  2 = Yes

41 = Warping torsional
constant Cw

  Value >=
0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a steel design
overwrite item.

The function returns zero if the item is successfully
retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemCanadian\_S16\_09 ()
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
      ret = SapModel.DesignSteel.SetCode("CSA-S16-09")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Canadian\_S16\_09.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

Item 40 (Is HSS section class H?) added in version 24.1.0

Added item 41 in version 25.1.0

## See Also

[SetOverwrite](SetOverwrite_{Steel_CSA_S16-09}.htm)



## GetPreference {Steel CSA S16-09}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-09/GetPreference_{Steel_CSA_S16-09}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_09.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 21, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

4 = Ductility related modification factor, Rd

5 = Overstrength related modification factor, Ro

6 = Capacity factor, Phi bending

7 = Capacity factor, Phi compression

8 = Capacity factor, Phi tension

9 = Capacity factor, Phi shear

10 = Slender section modification

11 = Ignore seismic code

12 = Ignore special seismic load

13 = Doubler plate is plug welded

14 = Consider deflection

15 = DL deflection limit, L/Value

16 = SDL + LL deflection limit, L/Value

17 = LL deflection limit, L/Value

18 = Total load deflection limit, L/Value

19 = Total camber limit, L/Value

20 = Pattern live load factor

21 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

Value > 0

4 = Ductility related modification factor, Rd

Value > 0

5 = Overstrength related modification factor, Ro

Value > 0

6 = Capacity factor, Phi bending

Value > 0

7 = Capacity factor, Phi compression

Value > 0

8 = Capacity factor, Phi tension

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Slender section modification

  1 = Modified geometry

  2 = modified Fy

11 = Ignore seismic code

  0 = No

  Any other value = Yes

12 = Ignore special seismic load

  0 = No

  Any other value = Yes

13 = Doubler plate is plug welded

  0 = No

  Any other value = Yes

14 = Consider deflection

  0 = No

  Any other value = Yes

15 = DL deflection limit, L/Value

  Value > 0

16 = SDL + LL deflection limit, L/Value

  Value > 0

17 = LL deflection limit, L/Value

  Value > 0

18 = Total load deflection limit, L/Value

  Value > 0

19 = Total camber limit, L/Value

  Value > 0

20 = Pattern live load factor

  Value >= 0

21 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemCanadian\_S16\_09 ()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CSA-S16-09")

   'get preference item
      ret = SapModel.DesignSteel.Canadian\_S16\_09.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_CSA_S16-09}.htm)



## SetOverwrite {Steel CSA S16-09}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-09/SetOverwrite_{Steel_CSA_S16-09}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_09.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 41, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit,
L/Value

5 = SDL + LL deflection
limit, L/Value

6 = LL deflection limit,
L/Value

7 = Total load deflection
limit, L/Value

8 = Total camber limit,
L/Value

9 = DL deflection limit,
absolute

10 = SDL + LL deflection
limit, absolute

11 = LL deflection limit,
absolute

12 = Total load deflection
limit, absolute

13 = Total camber limit,
absolute

14 = Specified camber

15 = Net area to total
area ratio

16 = Live load reduction
factor

17 = Unbraced length ratio,
Major

18 = Unbraced length ratio,
Minor LTB

19 = Unbraced length ratio,
Lateral Torsional Buckling

20 = Effective length
factor, K Major

21 = Effective length
factor, K Minor

22 = Effective length
factor, K LTB

23 = Moment coefficient,
Omega1 Major

24 = Moment coefficient,
Omega1 Minor

25 = Bending coefficient,
Omega2

26 = Nonsway moment factor,
U1 Major

27 = Nonsway moment factor,
U1 Minor

28 = Sway moment factor,
U2 Major

29 = Sway moment factor,
U2 Minor

30 = Parameter for compressive
resistance, n

31 = Yield stress, Fy

32 = Expected to specified
Fy ratio, Ry

33
= Compressive resistance, Cr

34
= Tensile resistance, Tr

35 = Major bending resistance,
Mr3

36 = Minor bending resistance,
Mr2

37 = Major shear resistance,
Vr2

38 = Minor shear resistance,
Vr3

39 = Demand/capacity ratio
limit

40 = Is HSS sections class
H?

41 = Warping torsional
constant Cw

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

2 = Consider deflection

0 = No

Any other value = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

5 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

6 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

7 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

8 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

9 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

10 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

11 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

12 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

14 = Specified camber

  Value >=
0. [L]

15 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

16 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

17 = Unbraced length ratio,
Major

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
Minor

  Value >=
0; 0 means use program determined value.

19 = Unbraced length ratio,
Lateral Torsional Buckling

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor, K Major

  Value >=
0; 0 means use program determined value.

21 = Effective length
factor, K Minor

  Value >=
0; 0 means use program determined value.

22 = Effective length
factor, K LTB

  Value >=
0; 0 means use program determined value.

23 = Moment coefficient,
Omega1 Major

  Value >=
0; 0 means use program determined value.

24 = Moment coefficient,
Omega1 Minor

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
Omega2

  Value >=
0; 0 means use program determined value.

26 = Nonsway moment factor,
U1 Major

  Value >=
0; 0 means use program determined value.

27 = Nonsway moment factor,
U1 Minor

  Value >=
0; 0 means use program determined value.

28 = Sway moment factor,
U2 Major

  Value >=
0; 0 means use program determined value.

29 = Sway moment factor,
U2 Minor

  Value >=
0; 0 means use program determined value.

30 = Parameter for compressive
resistance, n

  Value >=
0; 0 means use program determined value.

31 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

32 = Expected to specified
Fy ratio, Ry

  Value >=
0; 0 means use program determined value. [F/L2]=

33 = Compressive resistance,
Cr

  Value >=
0; 0 means use program determined value. [F]

34 = Tensile resistance,
Tr

  Value >=
0; 0 means use program determined value. [F]

35 = Major bending resistance,
Mr3

  Value >=
0; 0 means use program determined value. [FL]

36 = Minor bending resistance,
Mr2

  Value >=
0; 0 means use program determined value. [FL]

37 = Major shear resistance,
Vr2

  Value >=
0; 0 means use program determined value. [F]

38 = Minor shear resistance,
Vr3

  Value >=
0; 0 means use program determined value. [F]

39 = Demand/capacity ratio
limit

  Value >=
0; 0 means use program determined value.

40 = Is HSS sections class
H?

  0 = Program
Determined

  1 = No

  2 = Yes

41 = Warping torsional
constant Cw

  Value >=
0; 0 means use program determined value.

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

## Remarks

This function sets the value of a steel design overwrite
item.

The function returns zero if the item is successfully
set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemCanadian\_S16\_09 ()
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
      ret = SapModel.DesignSteel.SetCode("CSA-S16-09")

   'set overwrite item
      ret = SapModel.DesignSteel.Canadian\_S16\_09.SetOverwrite("8",
1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

Item 40 (Is HSS section class H?) added in version 24.1.0

Added item 41 in version 25.1.0

## See Also

[GetOverwrite](GetOverwrite_{Steel_CSA_S16-09}.htm)



## SetPreference {Steel CSA S16-09}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-09/SetPreference_{Steel_CSA_S16-09}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_09.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 21, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

4 = Ductility related modification factor, Rd

5 = Overstrength related modification factor, Ro

6 = Capacity factor, Phi bending

7 = Capacity factor, Phi compression

8 = Capacity factor, Phi tension

9 = Capacity factor, Phi shear

10 = Slender section modification

11 = Ignore seismic code

12 = Ignore special seismic load

13 = Doubler plate is plug welded

14 = Consider deflection

15 = DL deflection limit, L/Value

16 = SDL + LL deflection limit, L/Value

17 = LL deflection limit, L/Value

18 = Total load deflection limit, L/Value

19 = Total camber limit, L/Value

20 = Pattern live load factor

21 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

Value > 0

4 = Ductility related modification factor, Rd

Value > 0

5 = Overstrength related modification factor, Ro

Value > 0

6 = Capacity factor, Phi bending

Value > 0

7 = Capacity factor, Phi compression

Value > 0

8 = Capacity factor, Phi tension

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Slender section modification

  1 = Modified geometry

  2 = modified Fy

11 = Ignore seismic code

  0 = No

  Any other value = Yes

12 = Ignore special seismic load

  0 = No

  Any other value = Yes

13 = Doubler plate is plug welded

  0 = No

  Any other value = Yes

14 = Consider deflection

  0 = No

  Any other value = Yes

15 = DL deflection limit, L/Value

  Value > 0

16 = SDL + LL deflection limit, L/Value

  Value > 0

17 = LL deflection limit, L/Value

  Value > 0

18 = Total load deflection limit, L/Value

  Value > 0

19 = Total camber limit, L/Value

  Value > 0

20 = Pattern live load factor

  Value >= 0

21 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemCanadian\_S16\_09 ()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CSA-S16-09")

   'set preference item
      ret = SapModel.DesignSteel.Canadian\_S16\_09.SetPreference(1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_CSA_S16-09}.htm)



## GetOverwrite {Steel CSA S16-14}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-14/GetOverwrite_{Steel_CSA_S16-14}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_14.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design
procedure.

Item

This is an integer between 1 and 41, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit,
L/Value

5 = SDL + LL deflection
limit, L/Value

6 = LL deflection limit,
L/Value

7 = Total load deflection
limit, L/Value

8 = Total camber limit,
L/Value

9 = DL deflection limit,
absolute

10 = SDL + LL deflection
limit, absolute

11 = LL deflection limit,
absolute

12 = Total load deflection
limit, absolute

13 = Total camber limit,
absolute

14 = Specified camber

15 = Net area to total
area ratio

16 = Live load reduction
factor

17 = Unbraced length ratio,
Major

18 = Unbraced length ratio,
Minor LTB

19 = Unbraced length ratio,
Lateral Torsional Buckling

20 = Effective length
factor, K Major

21 = Effective length
factor, K Minor

22 = Effective length
factor, K LTB

23 = Moment coefficient,
Omega1 Major

24 = Moment coefficient,
Omega1 Minor

25 = Bending coefficient,
Omega2

26 = Nonsway moment factor,
U1 Major

27 = Nonsway moment factor,
U1 Minor

28 = Sway moment factor,
U2 Major

29 = Sway moment factor,
U2 Minor

30 = Parameter for compressive
resistance, n

31 = Yield stress, Fy

32 = Expected to specified
Fy ratio, Ry

33
= Compressive resistance, Cr

34 = Tensile resistance,
Tr

35 = Major bending resistance,
Mr3

36 = Minor bending resistance,
Mr2

37 = Major shear resistance,
Vr2

38 = Minor shear resistance,
Vr3

39 = Demand/capacity ratio
limit

40 = Is HSS sections class
H?

41 = Warping torsional
constant Cw

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

2 = Consider deflection

0 = No

Any other value = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

5 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

6 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

7 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

8 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

9 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

10 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

11 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

12 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

14 = Specified camber

  Value >=
0. [L]

15 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

16 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

17 = Unbraced length ratio,
Major

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
Minor

  Value >=
0; 0 means use program determined value.

19 = Unbraced length ratio,
Lateral Torsional Buckling

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor, K Major

  Value >=
0; 0 means use program determined value.

21 = Effective length
factor, K Minor

  Value >=
0; 0 means use program determined value.

22 = Effective length
factor, K LTB

  Value >=
0; 0 means use program determined value.

23 = Moment coefficient,
Omega1 Major

  Value >=
0; 0 means use program determined value.

24 = Moment coefficient,
Omega1 Minor

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
Omega2

  Value >=
0; 0 means use program determined value.

26 = Nonsway moment factor,
U1 Major

  Value >=
0; 0 means use program determined value.

27 = Nonsway moment factor,
U1 Minor

  Value >=
0; 0 means use program determined value.

28 = Sway moment factor,
U2 Major

  Value >=
0; 0 means use program determined value.

29 = Sway moment factor,
U2 Minor

  Value >=
0; 0 means use program determined value.

30 = Parameter for compressive
resistance, n

  Value >=
0; 0 means use program determined value.

31 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

32 = Expected to specified
Fy ratio, Ry

  Value >=
0; 0 means use program determined value. [F/L2]=

33 = Compressive resistance,
Cr

  Value >=
0; 0 means use program determined value. [F]

34 = Tensile resistance,
Tr

  Value >=
0; 0 means use program determined value. [F]

35 = Major bending resistance,
Mr3

  Value >=
0; 0 means use program determined value. [FL]

36 = Minor bending resistance,
Mr2

  Value >=
0; 0 means use program determined value. [FL]

37 = Major shear resistance,
Vr2

  Value >=
0; 0 means use program determined value. [F]

38 = Minor shear resistance,
Vr3

  Value >=
0; 0 means use program determined value. [F]

39 = Demand/capacity ratio
limit

  Value >=
0; 0 means use program determined value.

40 = Is HSS sections class
H?

  0 = Program
Determined

  1 = No

  2 = Yes

41 = Warping torsional
constant Cw

  Value >=
0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a steel design
overwrite item.

The function returns zero if the item is successfully
retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemCanadian\_S16\_14 ()
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
      ret = SapModel.DesignSteel.SetCode("CSA
S16-14")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Canadian\_S16\_14.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.1.0

Added item 41 in version 25.1.0

## See Also

[SetOverwrite](SetOverwrite_{Steel_CSA_S16-14}.htm)



## GetPreference {Steel CSA S16-14}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-14/GetPreference_{Steel_CSA_S16-14}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_14.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 21, inclusive, indicating
the preference item considered.

1 = Multi-response case
design

2 = Framing type

3
= Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

4 = Ductility related
modification factor, Rd

5 = Overstrength related
modification factor, Ro

6 = Capacity factor, Phi
bending

7 = Capacity factor, Phi
compression

8 = Capacity factor, Phi
tension

9 = Capacity factor, Phi
shear

10 = Slender section modification

11 = Ignore seismic code

12 = Ignore special seismic
load

13 = Doubler plate is
plug welded

14 = Consider deflection

15 = DL deflection limit,
L/Value

16 = SDL + LL deflection
limit, L/Value

17 = LL deflection limit,
L/Value

18 = Total load deflection
limit, L/Value

19 = Total camber limit,
L/Value

20 = Pattern live load
factor

21 = Demand/capacity ratio
limit

Value

The value of the considered preference item.

1 = Multi-response case
design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

3
= Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

Value > 0

4 = Ductility related
modification factor, Rd

Value > 0

5 = Overstrength related
modification factor, Ro

Value > 0

6 = Capacity factor, Phi
bending

Value > 0

7 = Capacity factor, Phi
compression

Value > 0

8 = Capacity factor, Phi
tension

Value > 0

9 = Capacity factor, Phi
shear

Value > 0

10
= Slender section modification

  1 = Modified
geometry

  2 = modified
Fy

11
= Ignore seismic code

  0 = No

  Any other
value = Yes

12
= Ignore special seismic load

  0 = No

  Any other
value = Yes

13 = Doubler plate is
plug welded

  0 = No

  Any other
value = Yes

14 = Consider deflection

  0 = No

  Any other
value = Yes

15 = DL deflection limit,
L/Value

  Value >
0

16 = SDL + LL deflection
limit, L/Value

  Value >
0

17 = LL deflection limit,
L/Value

  Value >
0

18 = Total load deflection
limit, L/Value

  Value >
0

19 = Total camber limit,
L/Value

  Value >
0

20 = Pattern live load
factor

  Value >=
0

21 = Demand/capacity ratio
limit

  Value >
0

## Remarks

This function retrieves the value of a steel design
preference item.

The function returns zero if the item is successfully
retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemCanadian\_S16\_14 ()
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
      ret = SapModel.DesignSteel.SetCode("CSA S16-14")

   'get preference item
      ret = SapModel.DesignSteel.Canadian\_S16\_14.GetPreference(1,
Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.1.0

## See Also

[SetPreference](SetPreference_{Steel_CSA_S16-14}.htm)



## SetOverwrite {Steel CSA S16-14}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-14/SetOverwrite_{Steel_CSA_S16-14}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_14.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 41, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit,
L/Value

5 = SDL + LL deflection
limit, L/Value

6 = LL deflection limit,
L/Value

7 = Total load deflection
limit, L/Value

8 = Total camber limit,
L/Value

9 = DL deflection limit,
absolute

10 = SDL + LL deflection
limit, absolute

11 = LL deflection limit,
absolute

12 = Total load deflection
limit, absolute

13 = Total camber limit,
absolute

14 = Specified camber

15 = Net area to total
area ratio

16 = Live load reduction
factor

17 = Unbraced length ratio,
Major

18 = Unbraced length ratio,
Minor LTB

19 = Unbraced length ratio,
Lateral Torsional Buckling

20 = Effective length
factor, K Major

21 = Effective length
factor, K Minor

22 = Effective length
factor, K LTB

23 = Moment coefficient,
Omega1 Major

24 = Moment coefficient,
Omega1 Minor

25 = Bending coefficient,
Omega2

26 = Nonsway moment factor,
U1 Major

27 = Nonsway moment factor,
U1 Minor

28 = Sway moment factor,
U2 Major

29 = Sway moment factor,
U2 Minor

30 = Parameter for compressive
resistance, n

31 = Yield stress, Fy

32 = Expected to specified
Fy ratio, Ry

33
= Compressive resistance, Cr

34
= Tensile resistance, Tr

35 = Major bending resistance,
Mr3

36 = Minor bending resistance,
Mr2

37 = Major shear resistance,
Vr2

38 = Minor shear resistance,
Vr3

39 = Demand/capacity ratio
limit

40 = Is HSS sections class
H?

41 = Warping torsional
constant Cw

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

2 = Consider deflection

0 = No

Any other value = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

5 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

6 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

7 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

8 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

9 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

10 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

11 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

12 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

14 = Specified camber

  Value >=
0. [L]

15 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

16 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

17 = Unbraced length ratio,
Major

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
Minor

  Value >=
0; 0 means use program determined value.

19 = Unbraced length ratio,
Lateral Torsional Buckling

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor, K Major

  Value >=
0; 0 means use program determined value.

21 = Effective length
factor, K Minor

  Value >=
0; 0 means use program determined value.

22 = Effective length
factor, K LTB

  Value >=
0; 0 means use program determined value.

23 = Moment coefficient,
Omega1 Major

  Value >=
0; 0 means use program determined value.

24 = Moment coefficient,
Omega1 Minor

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
Omega2

  Value >=
0; 0 means use program determined value.

26 = Nonsway moment factor,
U1 Major

  Value >=
0; 0 means use program determined value.

27 = Nonsway moment factor,
U1 Minor

  Value >=
0; 0 means use program determined value.

28 = Sway moment factor,
U2 Major

  Value >=
0; 0 means use program determined value.

29 = Sway moment factor,
U2 Minor

  Value >=
0; 0 means use program determined value.

30 = Parameter for compressive
resistance, n

  Value >=
0; 0 means use program determined value.

31 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

32 = Expected to specified
Fy ratio, Ry

  Value >=
0; 0 means use program determined value. [F/L2]=

33 = Compressive resistance,
Cr

  Value >=
0; 0 means use program determined value. [F]

34 = Tensile resistance,
Tr

  Value >=
0; 0 means use program determined value. [F]

35 = Major bending resistance,
Mr3

  Value >=
0; 0 means use program determined value. [FL]

36 = Minor bending resistance,
Mr2

  Value >=
0; 0 means use program determined value. [FL]

37 = Major shear resistance,
Vr2

  Value >=
0; 0 means use program determined value. [F]

38 = Minor shear resistance,
Vr3

  Value >=
0; 0 means use program determined value. [F]

39 = Demand/capacity ratio
limit

  Value >=
0; 0 means use program determined value.

40 = Is HSS sections class
H?

  0 = Program
Determined

  1 = No

  2 = Yes

41 = Warping torsional
constant Cw

  Value >=
0; 0 means use program determined value.

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

## Remarks

This function sets the value of a steel design overwrite
item.

The function returns zero if the item is successfully
set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemCanadian\_S16\_14 ()
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
      ret = SapModel.DesignSteel.SetCode("CSA
S16-14")

   'set overwrite item
      ret = SapModel.DesignSteel.Canadian\_S16\_14.SetOverwrite("8",
1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.1.0

Added item 41 in version 25.1.0

## See Also

[GetOverwrite](GetOverwrite_{Steel_CSA_S16-14}.htm)



## SetPreference {Steel CSA S16-14}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-14/SetPreference_{Steel_CSA_S16-14}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_14.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value
As Double) As Long

## Parameters

Item

This is an integer between 1 and 21, inclusive, indicating
the preference item considered.

1 = Multi-response case
design

2 = Framing type

3
= Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

4 = Ductility related
modification factor, Rd

5 = Overstrength related
modification factor, Ro

6 = Capacity factor, Phi
bending

7 = Capacity factor, Phi
compression

8 = Capacity factor, Phi
tension

9 = Capacity factor, Phi
shear

10 = Slender section modification

11 = Ignore seismic code

12 = Ignore special seismic
load

13 = Doubler plate is
plug welded

14 = Consider deflection

15 = DL deflection limit,
L/Value

16 = SDL + LL deflection
limit, L/Value

17 = LL deflection limit,
L/Value

18 = Total load deflection
limit, L/Value

19 = Total camber limit,
L/Value

20 = Pattern live load
factor

21 = Demand/capacity ratio
limit

Value

The value of the considered preference item.

1 = Multi-response case
design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

3 = Spectral Acceleration
Ratio, Ie\*Fa\*Sa(0.2)

Value > 0

4 = Ductility related
modification factor, Rd

Value > 0

5 = Overstrength related
modification factor, Ro

Value > 0

6 = Capacity factor, Phi
bending

Value > 0

7 = Capacity factor, Phi
compression

Value > 0

8 = Capacity factor, Phi
tension

Value > 0

9 = Capacity factor, Phi
shear

Value > 0

10
= Slender section modification

  1 = Modified
geometry

  2 = modified
Fy

11
= Ignore seismic code

  0 = No

  Any other
value = Yes

12
= Ignore special seismic load

  0 = No

  Any other
value = Yes

13 = Doubler plate is
plug welded

  0 = No

  Any other
value = Yes

14 = Consider deflection

  0 = No

  Any other
value = Yes

15 = DL deflection limit,
L/Value

  Value >
0

16 = SDL + LL deflection
limit, L/Value

  Value >
0

17 = LL deflection limit,
L/Value

  Value >
0

18 = Total load deflection
limit, L/Value

  Value >
0

19 = Total camber limit,
L/Value

  Value >
0

20 = Pattern live load
factor

  Value >=
0

21 = Demand/capacity ratio
limit

  Value >
0

## Remarks

This function sets the value of a steel design preference
item.

The function returns zero if the item is successfully
set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemCanadian\_S16\_14 ()
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
      ret = SapModel.DesignSteel.SetCode("CSA S16-14")

   'set preference item
      ret = SapModel.DesignSteel.Canadian\_S16\_14.SetPreference(1,
7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.1.0

## See Also

[GetPreference](GetPreference_{Steel_CSA_S16-14}.htm)



## GetOverwrite {Steel CSA S16-19}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-19/GetOverwrite_{Steel_CSA_S16-19}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_19.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design
procedure.

Item

This is an integer between 1 and 41, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit,
L/Value

5 = SDL + LL deflection
limit, L/Value

6 = LL deflection limit,
L/Value

7 = Total load deflection
limit, L/Value

8 = Total camber limit,
L/Value

9 = DL deflection limit,
absolute

10 = SDL + LL deflection
limit, absolute

11 = LL deflection limit,
absolute

12 = Total load deflection
limit, absolute

13 = Total camber limit,
absolute

14 = Specified camber

15 = Net area to total
area ratio

16 = Live load reduction
factor

17 = Unbraced length ratio,
Major

18 = Unbraced length ratio,
Minor LTB

19 = Unbraced length ratio,
Lateral Torsional Buckling

20 = Effective length
factor, K Major

21 = Effective length
factor, K Minor

22 = Effective length
factor, K LTB

23 = Moment coefficient,
Omega1 Major

24 = Moment coefficient,
Omega1 Minor

25 = Bending coefficient,
Omega2

26 = Nonsway moment factor,
U1 Major

27 = Nonsway moment factor,
U1 Minor

28 = Sway moment factor,
U2 Major

29 = Sway moment factor,
U2 Minor

30 = Parameter for compressive
resistance, n

31 = Yield stress, Fy

32 = Expected to specified
Fy ratio, Ry

33
= Compressive resistance, Cr

34 = Tensile resistance,
Tr

35 = Major bending resistance,
Mr3

36 = Minor bending resistance,
Mr2

37 = Major shear resistance,
Vr2

38 = Minor shear resistance,
Vr3

39 = Demand/capacity ratio
limit

40 = Is HSS sections class
H?

41 = Warping torsional
constant Cw

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

2 = Consider deflection

0 = No

Any other value = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

5 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

6 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

7 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

8 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

9 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

10 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

11 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

12 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

14 = Specified camber

  Value >=
0. [L]

15 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

16 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

17 = Unbraced length ratio,
Major

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
Minor

  Value >=
0; 0 means use program determined value.

19 = Unbraced length ratio,
Lateral Torsional Buckling

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor, K Major

  Value >=
0; 0 means use program determined value.

21 = Effective length
factor, K Minor

  Value >=
0; 0 means use program determined value.

22 = Effective length
factor, K LTB

  Value >=
0; 0 means use program determined value.

23 = Moment coefficient,
Omega1 Major

  Value >=
0; 0 means use program determined value.

24 = Moment coefficient,
Omega1 Minor

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
Omega2

  Value >=
0; 0 means use program determined value.

26 = Nonsway moment factor,
U1 Major

  Value >=
0; 0 means use program determined value.

27 = Nonsway moment factor,
U1 Minor

  Value >=
0; 0 means use program determined value.

28 = Sway moment factor,
U2 Major

  Value >=
0; 0 means use program determined value.

29 = Sway moment factor,
U2 Minor

  Value >=
0; 0 means use program determined value.

30 = Parameter for compressive
resistance, n

  Value >=
0; 0 means use program determined value.

31 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

32 = Expected to specified
Fy ratio, Ry

  Value >=
0; 0 means use program determined value. [F/L2]=

33 = Compressive resistance,
Cr

  Value >=
0; 0 means use program determined value. [F]

34 = Tensile resistance,
Tr

  Value >=
0; 0 means use program determined value. [F]

35 = Major bending resistance,
Mr3

  Value >=
0; 0 means use program determined value. [FL]

36 = Minor bending resistance,
Mr2

  Value >=
0; 0 means use program determined value. [FL]

37 = Major shear resistance,
Vr2

  Value >=
0; 0 means use program determined value. [F]

38 = Minor shear resistance,
Vr3

  Value >=
0; 0 means use program determined value. [F]

39 = Demand/capacity ratio
limit

  Value >=
0; 0 means use program determined value.

40 = Is HSS sections class
H?

  0 = Program
Determined

  1 = No

  2 = Yes

41 = Warping torsional
constant Cw

  Value >=
0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a steel design
overwrite item.

The function returns zero if the item is successfully
retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemCanadian\_S16\_19 ()
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
      ret = SapModel.DesignSteel.SetCode("CSA
S16-19")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Canadian\_S16\_19.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.1.0

Added item 41 in version 25.1.0

## See Also

[SetOverwrite](SetOverwrite_{Steel_CSA_S16-19}.htm)



## GetPreference {Steel CSA S16-19}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-19/GetPreference_{Steel_CSA_S16-19}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_19.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 25, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

4 = Ductility related modification factor, Rd

5 = Overstrength related modification factor, Ro

6 = Capacity factor, Phi bending

7 = Capacity factor, Phi compression

8 = Capacity factor, Phi tension

9 = Capacity factor, Phi shear

10 = Slender section modification

11 = Ignore seismic code

12 = Ignore special seismic load

13 = Doubler plate is plug welded

14 = Consider deflection

15 = DL deflection limit, L/Value

16 = SDL + LL deflection limit, L/Value

17 = LL deflection limit, L/Value

18 = Total load deflection limit, L/Value

19 = Total camber limit, L/Value

20 = Pattern live load factor

21 = Demand/capacity ratio limit

22 = Seismic Design Category

23 = Analysis Method

24 = Second Order Method

25 = Stiffness Reduction Method

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

Value > 0

4 = Ductility related modification factor, Rd

Value > 0

5 = Overstrength related modification factor, Ro

Value > 0

6 = Capacity factor, Phi bending

Value > 0

7 = Capacity factor, Phi compression

Value > 0

8 = Capacity factor, Phi tension

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Slender section modification

  1 = Modified geometry

  2 = modified Fy

11 = Ignore seismic code

  0 = No

  Any other value = Yes

12 = Ignore special seismic load

  0 = No

  Any other value = Yes

13 = Doubler plate is plug welded

  0 = No

  Any other value = Yes

14 = Consider deflection

  0 = No

  Any other value = Yes

15 = DL deflection limit, L/Value

  Value > 0

16 = SDL + LL deflection limit, L/Value

  Value > 0

17 = LL deflection limit, L/Value

  Value > 0

18 = Total load deflection limit, L/Value

  Value > 0

19 = Total camber limit, L/Value

  Value > 0

20 = Pattern live load factor

  Value >= 0

21 = Demand/capacity ratio limit

  Value > 0

22 = Seismic Design Category

  1 = SC0

  2 = SC1

  3 = SC2

  4 = SC3

  5 = SC4

22 = Seismic Design Category

  1 = SC0

  2 = SC1

  3 = SC2

23 = Analysis Method

  1 = Direct Analysis

  2 = Effective Length

  3 = Limited 1st Order

24 = Second Order Method

  1 = General 2nd order

  2 = Amplified 1st order

25 = Stiffness Reduction Method

  1 = Tau-b variable

  2 = Tau-b variable

  3 = No Modification

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemCanadian\_S16\_19 ()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CSA S16-19")

   'get preference item
      ret = SapModel.DesignSteel.Canadian\_S16\_19.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.1.0

Added items 23, 24, and 25 in version 27.0.0

## See Also

[SetPreference](SetPreference_{Steel_CSA_S16-19}.htm)



## SetOverwrite {Steel CSA S16-19}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-19/SetOverwrite_{Steel_CSA_S16-19}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_19.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 41, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit,
L/Value

5 = SDL + LL deflection
limit, L/Value

6 = LL deflection limit,
L/Value

7 = Total load deflection
limit, L/Value

8 = Total camber limit,
L/Value

9 = DL deflection limit,
absolute

10 = SDL + LL deflection
limit, absolute

11 = LL deflection limit,
absolute

12 = Total load deflection
limit, absolute

13 = Total camber limit,
absolute

14 = Specified camber

15 = Net area to total
area ratio

16 = Live load reduction
factor

17 = Unbraced length ratio,
Major

18 = Unbraced length ratio,
Minor LTB

19 = Unbraced length ratio,
Lateral Torsional Buckling

20 = Effective length
factor, K Major

21 = Effective length
factor, K Minor

22 = Effective length
factor, K LTB

23 = Moment coefficient,
Omega1 Major

24 = Moment coefficient,
Omega1 Minor

25 = Bending coefficient,
Omega2

26 = Nonsway moment factor,
U1 Major

27 = Nonsway moment factor,
U1 Minor

28 = Sway moment factor,
U2 Major

29 = Sway moment factor,
U2 Minor

30 = Parameter for compressive
resistance, n

31 = Yield stress, Fy

32 = Expected to specified
Fy ratio, Ry

33
= Compressive resistance, Cr

34
= Tensile resistance, Tr

35 = Major bending resistance,
Mr3

36 = Minor bending resistance,
Mr2

37 = Major shear resistance,
Vr2

38 = Minor shear resistance,
Vr3

39 = Demand/capacity ratio
limit

40 = Is HSS sections class
H?

41 = Warping torsional
constant Cw

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

2 = Consider deflection

0 = No

Any other value = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

5 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

6 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

7 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

8 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

9 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

10 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

11 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

12 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

14 = Specified camber

  Value >=
0. [L]

15 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

16 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

17 = Unbraced length ratio,
Major

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
Minor

  Value >=
0; 0 means use program determined value.

19 = Unbraced length ratio,
Lateral Torsional Buckling

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor, K Major

  Value >=
0; 0 means use program determined value.

21 = Effective length
factor, K Minor

  Value >=
0; 0 means use program determined value.

22 = Effective length
factor, K LTB

  Value >=
0; 0 means use program determined value.

23 = Moment coefficient,
Omega1 Major

  Value >=
0; 0 means use program determined value.

24 = Moment coefficient,
Omega1 Minor

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
Omega2

  Value >=
0; 0 means use program determined value.

26 = Nonsway moment factor,
U1 Major

  Value >=
0; 0 means use program determined value.

27 = Nonsway moment factor,
U1 Minor

  Value >=
0; 0 means use program determined value.

28 = Sway moment factor,
U2 Major

  Value >=
0; 0 means use program determined value.

29 = Sway moment factor,
U2 Minor

  Value >=
0; 0 means use program determined value.

30 = Parameter for compressive
resistance, n

  Value >=
0; 0 means use program determined value.

31 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

32 = Expected to specified
Fy ratio, Ry

  Value >=
0; 0 means use program determined value. [F/L2]=

33 = Compressive resistance,
Cr

  Value >=
0; 0 means use program determined value. [F]

34 = Tensile resistance,
Tr

  Value >=
0; 0 means use program determined value. [F]

35 = Major bending resistance,
Mr3

  Value >=
0; 0 means use program determined value. [FL]

36 = Minor bending resistance,
Mr2

  Value >=
0; 0 means use program determined value. [FL]

37 = Major shear resistance,
Vr2

  Value >=
0; 0 means use program determined value. [F]

38 = Minor shear resistance,
Vr3

  Value >=
0; 0 means use program determined value. [F]

39 = Demand/capacity ratio
limit

  Value >=
0; 0 means use program determined value.

40 = Is HSS sections class
H?

  0 = Program
Determined

  1 = No

  2 = Yes

41 = Warping torsional
constant Cw

  Value >=
0; 0 means use program determined value.

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

## Remarks

This function sets the value of a steel design overwrite
item.

The function returns zero if the item is successfully
set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemCanadian\_S16\_19 ()
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
      ret = SapModel.DesignSteel.SetCode("CSA
S16-19")

   'set overwrite item
      ret = SapModel.DesignSteel.Canadian\_S16\_19.SetOverwrite("8",
1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.1.0

Added item 41 in version 25.1.0

## See Also

[GetOverwrite](GetOverwrite_{Steel_CSA_S16-19}.htm)



## SetPreference {Steel CSA S16-19}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-19/SetPreference_{Steel_CSA_S16-19}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_19.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 25, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

4 = Ductility related modification factor, Rd

5 = Overstrength related modification factor, Ro

6 = Capacity factor, Phi bending

7 = Capacity factor, Phi compression

8 = Capacity factor, Phi tension

9 = Capacity factor, Phi shear

10 = Slender section modification

11 = Ignore seismic code

12 = Ignore special seismic load

13 = Doubler plate is plug welded

14 = Consider deflection

15 = DL deflection limit, L/Value

16 = SDL + LL deflection limit, L/Value

17 = LL deflection limit, L/Value

18 = Total load deflection limit, L/Value

19 = Total camber limit, L/Value

20 = Pattern live load factor

21 = Demand/capacity ratio limit

22 = Seismic Design Category

23 = Analysis Method

24 = Second Order Method

25 = Stiffness Reduction Method

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

Value > 0

4 = Ductility related modification factor, Rd

Value > 0

5 = Overstrength related modification factor, Ro

Value > 0

6 = Capacity factor, Phi bending

Value > 0

7 = Capacity factor, Phi compression

Value > 0

8 = Capacity factor, Phi tension

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Slender section modification

  1 = Modified geometry

  2 = modified Fy

11 = Ignore seismic code

  0 = No

  Any other value = Yes

12 = Ignore special seismic load

  0 = No

  Any other value = Yes

13 = Doubler plate is plug welded

  0 = No

  Any other value = Yes

14 = Consider deflection

  0 = No

  Any other value = Yes

15 = DL deflection limit, L/Value

  Value > 0

16 = SDL + LL deflection limit, L/Value

  Value > 0

17 = LL deflection limit, L/Value

  Value > 0

18 = Total load deflection limit, L/Value

  Value > 0

19 = Total camber limit, L/Value

  Value > 0

20 = Pattern live load factor

  Value >= 0

21 = Demand/capacity ratio limit

  Value > 0

22 = Seismic Design Category

  1 = SC0

  2 = SC1

  3 = SC2

  4 = SC3

  5 = SC4

23 = Analysis Method

  1 = Direct Analysis

  2 = Effective Length

  3 = Limited 1st Order

24 = Second Order Method

  1 = General 2nd order

  2 = Amplified 1st order

25 = Stiffness Reduction Method

  1 = Tau-b variable

  2 = Tau-b variable

  3 = No Modification

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemCanadian\_S16\_19 ()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CSA S16-19")

   'set preference item
      ret = SapModel.DesignSteel.Canadian\_S16\_19.SetPreference(1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 24.1.0

Added items 23, 24, and 25 in version 27.0.0

## See Also

[GetPreference](GetPreference_{Steel_CSA_S16-19}.htm)



## GetOverwrite {Steel CSA S16-24}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-24/GetOverwrite_{Steel_CSA_S16-24}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_24.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 41, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor LTB

19 = Unbraced length ratio, Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Effective length factor, K LTB

23 = Moment coefficient, Omega1 Major

24 = Moment coefficient, Omega1 Minor

25 = Bending coefficient, Omega2

26 = Nonsway moment factor, U1 Major

27 = Nonsway moment factor, U1 Minor

28 = Sway moment factor, U2 Major

29 = Sway moment factor, U2 Minor

30 = Parameter for compressive resistance, n

31 = Yield stress, Fy

32 = Expected to specified Fy ratio, Ry

33 = Compressive resistance, Cr

34 = Tensile resistance, Tr

35 = Major bending resistance, Mr3

36 = Minor bending resistance, Mr2

37 = Major shear resistance, Vr2

38 = Minor shear resistance, Vr3

39 = Demand/capacity ratio limit

40 = Is HSS sections class H?

41 = Warping torsional constant Cw

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

2 = Consider deflection

0 = No

Any other value = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

  Value >= 0. [L]

15 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

16 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

  Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

  Value >= 0; 0 means use program determined value.

22 = Effective length factor, K LTB

  Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Omega1 Major

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, Omega1 Minor

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, Omega2

  Value >= 0; 0 means use program determined value.

26 = Nonsway moment factor, U1 Major

  Value >= 0; 0 means use program determined value.

27 = Nonsway moment factor, U1 Minor

  Value >= 0; 0 means use program determined value.

28 = Sway moment factor, U2 Major

  Value >= 0; 0 means use program determined value.

29 = Sway moment factor, U2 Minor

  Value >= 0; 0 means use program determined value.

30 = Parameter for compressive resistance, n

  Value >= 0; 0 means use program determined value.

31 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

32 = Expected to specified Fy ratio, Ry

  Value >= 0; 0 means use program determined value. [F/L2]=

33 = Compressive resistance, Cr

  Value >= 0; 0 means use program determined value. [F]

34 = Tensile resistance, Tr

  Value >= 0; 0 means use program determined value. [F]

35 = Major bending resistance, Mr3

  Value >= 0; 0 means use program determined value. [FL]

36 = Minor bending resistance, Mr2

  Value >= 0; 0 means use program determined value. [FL]

37 = Major shear resistance, Vr2

  Value >= 0; 0 means use program determined value. [F]

38 = Minor shear resistance, Vr3

  Value >= 0; 0 means use program determined value. [F]

39 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

40 = Is HSS sections class H?

  0 = Program Determined

  1 = No

  2 = Yes

41 = Warping torsional constant Cw

  Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemCanadian\_S16\_24 ()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CSA S16-24")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Canadian\_S16\_24.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 27.0.0

## See Also

[SetOverwrite](SetOverwrite_{Steel_CSA_S16-24}.htm)



## GetPreference {Steel CSA S16-24}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-24/GetPreference_{Steel_CSA_S16-24}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_24.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 21, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

4 = Ductility related modification factor, Rd

5 = Overstrength related modification factor, Ro

6 = Capacity factor, Phi bending

7 = Capacity factor, Phi compression

8 = Capacity factor, Phi tension

9 = Capacity factor, Phi shear

10 = Ignore seismic code

11 = Ignore special seismic load

12 = Doubler plate is plug welded

13 = Consider deflection

14 = DL deflection limit, L/Value

15 = SDL + LL deflection limit, L/Value

16 = LL deflection limit, L/Value

17 = Total load deflection limit, L/Value

18 = Total camber limit, L/Value

19 = Pattern live load factor

20 = Demand/capacity ratio limit

21 = Seismic Design Category

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

Value > 0

4 = Ductility related modification factor, Rd

Value > 0

5 = Overstrength related modification factor, Ro

Value > 0

6 = Capacity factor, Phi bending

Value > 0

7 = Capacity factor, Phi compression

Value > 0

8 = Capacity factor, Phi tension

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Ignore seismic code

  0 = No

  Any other value = Yes

11 = Ignore special seismic load

  0 = No

  Any other value = Yes

12 = Doubler plate is plug welded

  0 = No

  Any other value = Yes

13 = Consider deflection

  0 = No

  Any other value = Yes

14 = DL deflection limit, L/Value

  Value > 0

15 = SDL + LL deflection limit, L/Value

  Value > 0

16 = LL deflection limit, L/Value

  Value > 0

17 = Total load deflection limit, L/Value

  Value > 0

1 = Total camber limit, L/Value

  Value > 0

19 = Pattern live load factor

  Value >= 0

20 = Demand/capacity ratio limit

  Value > 0

21 = Seismic Design Category

  1 = SC0

  2 = SC1

  3 = SC2

  4 = SC3

  5 = SC4

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemCanadian\_S16\_24 ()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CSA S16-24")

   'get preference item
      ret = SapModel.DesignSteel.Canadian\_S16\_24.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 27.0.0

## See Also

[SetPreference](SetPreference_{Steel_CSA_S16-24}.htm)



## SetOverwrite {Steel CSA S16-24}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-24/SetOverwrite_{Steel_CSA_S16-24}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_24.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 41, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor LTB

19 = Unbraced length ratio, Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Effective length factor, K LTB

23 = Moment coefficient, Omega1 Major

24 = Moment coefficient, Omega1 Minor

25 = Bending coefficient, Omega2

26 = Nonsway moment factor, U1 Major

27 = Nonsway moment factor, U1 Minor

28 = Sway moment factor, U2 Major

29 = Sway moment factor, U2 Minor

30 = Parameter for compressive resistance, n

31 = Yield stress, Fy

32 = Expected to specified Fy ratio, Ry

33 = Compressive resistance, Cr

34 = Tensile resistance, Tr

35 = Major bending resistance, Mr3

36 = Minor bending resistance, Mr2

37 = Major shear resistance, Vr2

38 = Minor shear resistance, Vr3

39 = Demand/capacity ratio limit

40 = Is HSS sections class H?

41 = Warping torsional constant Cw

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

2 = Consider deflection

0 = No

Any other value = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

  Value >= 0. [L]

15 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

16 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

  Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

  Value >= 0; 0 means use program determined value.

22 = Effective length factor, K LTB

  Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Omega1 Major

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, Omega1 Minor

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, Omega2

  Value >= 0; 0 means use program determined value.

26 = Nonsway moment factor, U1 Major

  Value >= 0; 0 means use program determined value.

27 = Nonsway moment factor, U1 Minor

  Value >= 0; 0 means use program determined value.

28 = Sway moment factor, U2 Major

  Value >= 0; 0 means use program determined value.

29 = Sway moment factor, U2 Minor

  Value >= 0; 0 means use program determined value.

30 = Parameter for compressive resistance, n

  Value >= 0; 0 means use program determined value.

31 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

32 = Expected to specified Fy ratio, Ry

  Value >= 0; 0 means use program determined value. [F/L2]=

33 = Compressive resistance, Cr

  Value >= 0; 0 means use program determined value. [F]

34 = Tensile resistance, Tr

  Value >= 0; 0 means use program determined value. [F]

35 = Major bending resistance, Mr3

  Value >= 0; 0 means use program determined value. [FL]

36 = Minor bending resistance, Mr2

  Value >= 0; 0 means use program determined value. [FL]

37 = Major shear resistance, Vr2

  Value >= 0; 0 means use program determined value. [F]

38 = Minor shear resistance, Vr3

  Value >= 0; 0 means use program determined value. [F]

39 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

40 = Is HSS sections class H?

  0 = Program Determined

  1 = No

  2 = Yes

41 = Warping torsional constant Cw

  Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemCanadian\_S16\_24 ()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CSA S16-24")

   'set overwrite item
      ret = SapModel.DesignSteel.Canadian\_S16\_24.SetOverwrite("8", 1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 27.0.0

## See Also

[GetOverwrite](GetOverwrite_{Steel_CSA_S16-24}.htm)



## SetPreference {Steel CSA S16-24}

*Source file: `SAP2000_API_Fuctions/Design/Steel/CSA_S16-24/SetPreference_{Steel_CSA_S16-24}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Canadian\_S16\_24.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 21, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

4 = Ductility related modification factor, Rd

5 = Overstrength related modification factor, Ro

6 = Capacity factor, Phi bending

7 = Capacity factor, Phi compression

8 = Capacity factor, Phi tension

9 = Capacity factor, Phi shear

10 = Ignore seismic code

11 = Ignore special seismic load

12 = Doubler plate is plug welded

13 = Consider deflection

14 = DL deflection limit, L/Value

15 = SDL + LL deflection limit, L/Value

16 = LL deflection limit, L/Value

17 = Total load deflection limit, L/Value

18 = Total camber limit, L/Value

19 = Pattern live load factor

20 = Demand/capacity ratio limit

21 = Seismic Design Category

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Type LD MRF

2 = Type MD MRF

3 = Type D MRF

4 = Type LD CBF(V)

5 = Type LD CBF(TC)

6 = Type LD CBF(TO)

7 = Type LD CBF(OT)

8 = Type MD CBF(V)

9 = Type MD CBF(TC)

10 = Type MD CBF(TO)

11 = Type MD CBF(OT)

12 = EBF

13 = Cantilever Column

14 = Conventional MF

15 = Conventional BF

3 = Spectral Acceleration Ratio, Ie\*Fa\*Sa(0.2)

Value > 0

4 = Ductility related modification factor, Rd

Value > 0

5 = Overstrength related modification factor, Ro

Value > 0

6 = Capacity factor, Phi bending

Value > 0

7 = Capacity factor, Phi compression

Value > 0

8 = Capacity factor, Phi tension

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Ignore seismic code

  0 = No

  Any other value = Yes

11 = Ignore special seismic load

  0 = No

  Any other value = Yes

12 = Doubler plate is plug welded

  0 = No

  Any other value = Yes

13 = Consider deflection

  0 = No

  Any other value = Yes

14 = DL deflection limit, L/Value

  Value > 0

15 = SDL + LL deflection limit, L/Value

  Value > 0

16 = LL deflection limit, L/Value

  Value > 0

17 = Total load deflection limit, L/Value

  Value > 0

1 = Total camber limit, L/Value

  Value > 0

19 = Pattern live load factor

  Value >= 0

20 = Demand/capacity ratio limit

  Value > 0

21 = Seismic Design Category

  1 = SC0

  2 = SC1

  3 = SC2

  4 = SC3

  5 = SC4

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemCanadian\_S24 ()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("CSA S16-24")

   'set preference item
      ret = SapModel.DesignSteel.Canadian\_S24.SetPreference(1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 27.0.0

## See Also

[GetPreference](GetPreference_{Steel_CSA_S16-24}.htm)



## GetOverwrite {Steel Chinese 2010}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Chinese_2010/GetOverwrite_{Steel_Chinese_2010}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Chinese\_2010.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 51, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Element type

3 = Is transfer column

4 = Seismic magnification factor

5 = Is rolled section

6 = Is flange edge cut by gas

7 = Is both end pinned

8 = Ignore b/t check

9 = Classify beam as flexo-compression member

10 = Is beam top loaded

11 = Consider deflection

12 = Deflection check type

13 = DL deflection limit, L/Value

14 = SDL + LL deflection limit, L/Value

15 = LL deflection limit, L/Value

16 = Total load deflection limit, L/Value

17 = Total camber limit, L/Value

18 = DL deflection limit, absolute

19 = SDL + LL deflection limit, absolute

20 = LL deflection limit, absolute

21 = Total load deflection limit, absolute

22 = Total camber limit, absolute

23 = Specified camber

24 = Net area to total area ratio

25 = Live load reduction factor

26 = Unbraced length ratio, Major

27 = Unbraced length ratio, Minor Lateral Torsional Buckling

28 = Effective length factor, Mue Major

29 = Effective length factor, Mue Minor

30 = Moment coefficient, Beta\_m Major

31 = Moment coefficient, Beta\_m Minor

32 = Moment coefficient, Beta\_t Major

33 = Moment coefficient, Beta\_t Minor

34 = Axial stability coefficient, Phi Major

35 = Axial stability coefficient, Phi Minor

36 = Flexural stability coeff, Phi\_bMajor

37 = Flexural stability coeff, Phi\_bMinor

38 = Plasticity factor, Gamma Major

39 = Plasticity factor, Gamma Minor

40 = Section influence coefficient, Eta

41 = B/C capacity factor, Eta

42 = Euler moment factor, Delta Major

43 = Euler moment factor, Delta Minor

44 = Yield stress, Fy

45 = Allowable normal stress, f

46 = Allowable shear stress, fv

47 = Consider fictitious shear

48 = Demand/capacity ratio limit

49 = Dual system magnification factor

50 = Lo/r limit in compression

51 = L/r limit in tension

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Sway Moment Frame, SMF

2 = Concentrically Braced Frame, CBF

3 = Eccentrically Braced Frame, EBF

4 = NonSway Moment Frame, NMF

2 = Element type

0 = Program Determined

1 = Column

2 = Beam

3 = Brace

4 = Truss

3 = Is transfer column

0 = Program Determined

1 = No

2 = Yes

4 = Seismic magnification factor

Value >= 0; 0 means no check for this item.

5 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

6 = Is flange edge cut by gas

0 = Program Determined

1 = No

2 = Yes

7 = Is both end pinned

0 = Program Determined

1 = No

2 = Yes

8 = Ignore b/t check

0 = Program Determined

1 = No

2 = Yes

9 = Classify beam as flexo-compression member

0 = Program Determined

1 = No

2 = Yes

10 = Is beam top loaded

0 = Program Determined

1 = No

2 = Yes

11 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

12 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

13 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

14 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

15 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

16 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

17 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

18 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

19 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

20 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

21 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

22 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

23 = Specified camber

Value >= 0. [L]

24 = Net area to total area ratio

Value >= 0; 0 means use program default value.

25 = Live load reduction factor

Value >= 0; 0 means use program determined value.

26 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

27 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

28 = Effective length factor, Mue Major

Value >= 0; 0 means use program determined value.

29 = Effective length factor, Mue Minor

Value >= 0; 0 means use program determined value.

30 = Moment coefficient, Beta\_m Major

Value >= 0; 0 means use program determined value.

31 = Moment coefficient, Beta\_m Minor

Value >= 0; 0 means use program determined value.

32 = Moment coefficient, Beta\_t Major

Value >= 0; 0 means use program determined value.

33 = Moment coefficient, Beta\_t Minor

Value >= 0; 0 means use program determined value.

34 = Axial stability coefficient, Phi Major

Value >= 0; 0 means use program determined value.

35 = Axial stability coefficient, Phi Minor

Value >= 0; 0 means use program determined value.

36 = Flexural stability coefficient, Phi\_b Major

Value >= 0; 0 means use program determined value.

37 = Flexural stability coefficient, Phi\_b Minor

Value >= 0; 0 means use program determined value.

38 = Plasticity factor, Gamma Major

Value >= 0; 0 means use program determined value.

39 = Plasticity factor, Gamma Minor

Value >= 0; 0 means use program determined value.

40 = Section influence coefficient, Eta

Value >= 0; 0 means use program determined value.

41 = B/C capacity factor, Eta

Value >= 0; 0 means use program determined value.

42 = Euler moment factor, Delta Major

Value >= 0; 0 means use program determined value.

43 = Euler moment factor, Delta Minor

Value >= 0; 0 means use program determined value.

44 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

45 = Allowable normal stress, f

Value >= 0; 0 means use program determined value. [F/L2]

46 = Allowable shear stress, fv

Value >= 0; 0 means use program determined value. [F/L2]

47 = Consider fictitious shear

0 = Program Determined

1 = No

2 = Yes

48 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

49 = Dual system magnification factor

        Value >= 0; 0 means use program default value.

50 = Lo/r limit in compression

        Value >= 0; 0 means use program determined value.

51 = L/r limit in tension

        Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemChinese\_2010()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Chinese 2010")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Chinese\_2010.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.2.

## See Also

[SetOverwrite](SetOverwrite_{Steel_Chinese_2010}.htm)



## GetPreference {Steel Chinese 2010}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Chinese_2010/GetPreference_{Steel_Chinese_2010}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Chinese\_2010.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1 = Framing type

2 = Gamma0

3 = Ignore b/t check

4 = Classify beam as flexo compression member

5 = Consider deflection

6 = DL deflection limit, L/Value

7 = SDL + LL deflection limit, L/Value

8 = LL deflection limit, L/Value

9 = Total load deflection limit, L/Value

10 = Total camber limit, L/Value

11 = Pattern live load factor

12 = Demand/capacity ratio limit

13 = Multi-response case design

14 = Is tall building?

15 = Seismic Design Grade

Value

The value of the considered preference item.

1 = Framing type

0 = As specified in preferences

1 = Sway Moment Frame, SMF

2 = Concentrically Braced Frame, CBF

3 = Eccentrically Braced Frame, EBF

4 = NonSway Moment Frame, NMF

2 = Gamma0

Value > 0

3 = Ignore b/t check

0 = No

Any other value = Yes

4 = Classify beam as flexo compression member

0 = No

Any other value = Yes

5 = Consider deflection

0 = No

Any other value = Yes

6 = DL deflection limit, L/Value

Value > 0

7 = SDL + LL deflection limit, L/Value

Value > 0

8 = LL deflection limit, L/Value

Value > 0

9 = Total load deflection limit, L/Value

Value > 0

10 = Total camber limit, L/Value

Value > 0

11 = Pattern live load factor

Value >= 0

12 = Demand/capacity ratio limit

Value > 0

13 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

14 = Tall building

0 = No

1 = Yes

15 = Seismic Design Grade

1 = Grade I

2 = Grade II

3 = Grade III

4 = Grade IV

5 = Non Seismic

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemChinese\_2010()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim Value As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'createSapModelobject
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Chinese 2010")

   'get preference item
      ret = SapModel.DesignSteel.Chinese\_2010.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.2.

Added Seismic Design Grade preference item in v18.0.0.

## See Also

[SetPreference](SetPreference_{Steel_Chinese_2010}.htm)



## SetOverwrite {Steel Chinese 2010}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Chinese_2010/SetOverwrite_{Steel_Chinese_2010}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Chinese\_2010.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Item

This is an integer between 1 and 51, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Element type

3 = Is transfer column

4 = Seismic magnification factor

5 = Is rolled section

6 = Is flange edge cut by gas

7 = Is both end pinned

8 = Ignore b/t check

9 = Classify beam as flexo-compression member

10 = Is beam top loaded

11 = Consider deflection

12 = Deflection check type

13 = DL deflection limit, L/Value

14 = SDL + LL deflection limit, L/Value

15 = LL deflection limit, L/Value

16 = Total load deflection limit, L/Value

17 = Total camber limit, L/Value

18 = DL deflection limit, absolute

19 = SDL + LL deflection limit, absolute

20 = LL deflection limit, absolute

21 = Total load deflection limit, absolute

22 = Total camber limit, absolute

23 = Specified camber

24 = Net area to total area ratio

25 = Live load reduction factor

26 = Unbraced length ratio, Major

27 = Unbraced length ratio, Minor Lateral TorsionalBuckling

28 = Effective length factor, Mue Major

29 = Effective length factor, Mue Minor

30 = Moment coefficient, Beta\_m Major

31 = Moment coefficient, Beta\_m Minor

32 = Moment coefficient, Beta\_t Major

33 = Moment coefficient, Beta\_t Minor

34 = Axial stability coefficient, Phi Major

35 = Axial stability coefficient, Phi Minor

36 = Flexural stability coeff, Phi\_bMajor

37 = Flexural stability coeff, Phi\_bMinor

38 = Plasticity factor, Gamma Major

39 = Plasticity factor, Gamma Minor

40 = Section influence coefficient, Eta

41 = B/C capacity factor, Eta

42 = Euler moment factor, Delta Major

43 = Euler moment factor, Delta Minor

44 = Yield stress, Fy

45 = Allowable normal stress, f

46 = Allowable shear stress, fv

47 = Consider fictitious shear

48 = Demand/capacity ratio limit

49 = Dual system magnification factor

50 = Lo/r limit in compression

51 = L/r limit in tension

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Sway Moment Frame, SMF

2 = Concentrically Braced Frame, CBF

3 = Eccentrically Braced Frame, EBF

4 = NonSway Moment Frame, NMF

2 = Element type

0 = Program Determined

1 = Column

2 = Beam

3 = Brace

4 = Truss

3 = Is transfer column

0 = Program Determined

1 = No

2 = Yes

4 = Seismic magnification factor

Value >= 0; 0 means no check for this item.

5 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

6 = Is flange edge cut by gas

0 = Program Determined

1 = No

2 = Yes

7 = Is both end pinned

0 = Program Determined

1 = No

2 = Yes

8 = Ignore b/t check

0 = Program Determined

1 = No

2 = Yes

9 = Classify beam as flexo-compression member

0 = Program Determined

1 = No

2 = Yes

10 = Is beam top loaded

0 = Program Determined

1 = No

2 = Yes

11 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

12 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

13 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

14 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

15 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

16 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

17 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

18 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

19 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

20 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

21 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

22 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

23 = Specified camber

Value >= 0. [L]

24 = Net area to total area ratio

Value >= 0; 0 means use program default value.

25 = Live load reduction factor

Value >= 0; 0 means use program determined value.

26 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

27 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

28 = Effective length factor, Mue Major

Value >= 0; 0 means use program determined value.

29 = Effective length factor, Mue Minor

Value >= 0; 0 means use program determined value.

30 = Moment coefficient, Beta\_m Major

Value >= 0; 0 means use program determined value.

31 = Moment coefficient, Beta\_m Minor

Value >= 0; 0 means use program determined value.

32 = Moment coefficient, Beta\_t Major

Value >= 0; 0 means use program determined value.

33 = Moment coefficient, Beta\_t Minor

Value >= 0; 0 means use program determined value.

34 = Axial stability coefficient, Phi Major

Value >= 0; 0 means use program determined value.

35 = Axial stability coefficient, Phi Minor

Value >= 0; 0 means use program determined value.

36 = Flexural stability coefficient, Phi\_b Major

Value >= 0; 0 means use program determined value.

37 = Flexural stability coefficient, Phi\_b Minor

Value >= 0; 0 means use program determined value.

38 = Plasticity factor, Gamma Major

Value >= 0; 0 means use program determined value.

39 = Plasticity factor, Gamma Minor

Value >= 0; 0 means use program determined value.

40 = Section influence coefficient, Eta

Value >= 0; 0 means use program determined value.

41 = B/C capacity factor, Eta

Value >= 0; 0 means use program determined value.

42 = Euler moment factor, Delta Major

Value >= 0; 0 means use program determined value.

43 = Euler moment factor, Delta Minor

Value >= 0; 0 means use program determined value.

44 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

45 = Allowable normal stress, f

Value >= 0; 0 means use program determined value. [F/L2]

46 = Allowable shear stress, fv

Value >= 0; 0 means use program determined value. [F/L2]

47 = Consider fictitious shear

0 = Program Determined

1 = No

2 = Yes

48 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value

49 = Dual system magnification factor

        Value >= 0; 0 means use program default value.

50 = Lo/r limit in compression

        Value >= 0; 0 means use program determined value.

51 = L/r limit in tension

        Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects= 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemChinese\_2010()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Chinese 2010")

   'set overwrite item
      ret = SapModel.DesignSteel.Chinese\_2010.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.2.

## See Also

[GetOverwrite](GetOverwrite_{Steel_Chinese_2010}.htm)



## SetPreference {Steel Chinese 2010}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Chinese_2010/SetPreference_{Steel_Chinese_2010}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Chinese\_2010.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 14, inclusive, indicating the preference item considered.

1 = Framing type

2 = Gamma0

3 = Ignore b/t check

4 = Classify beam as flexo compression member

5 = Consider deflection

6 = DL deflection limit, L/Value

7 = SDL + LL deflection limit, L/Value

8 = LL deflection limit, L/Value

9 = Total load deflection limit, L/Value

10 = Total camber limit, L/Value

11 = Pattern live load factor

12 = Demand/capacity ratio limit

13 = Multi-response case design

14 = Is tall building?

15 = Seismic Design Grade

Value

The value of the considered preference item.

1 = Framing type

0 = As specified in preferences

1 = Sway Moment Frame, SMF

2 = Concentrically Braced Frame, CBF

3 = Eccentrically Braced Frame, EBF

4 = NonSway Moment Frame, NMF

2 = Gamma0

Value > 0

3 = Ignore b/t check

0 = No

Any other value = Yes

4 = Classify beam as flexo compression member

0 = No

Any other value = Yes

5 = Consider deflection

0 = No

Any other value = Yes

6 = DL deflection limit, L/Value

Value > 0

7 = SDL + LL deflection limit, L/Value

Value > 0

8 = LL deflection limit, L/Value

Value > 0

9 = Total load deflection limit, L/Value

Value > 0

10 = Total camber limit, L/Value

Value > 0

11 = Pattern live load factor

Value >= 0

12 = Demand/capacity ratio limit

Value > 0

13 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

14 = Tall building

        0 = No

        1 = Yes

15 = Seismic Design Grade

1 = Grade I

2 = Grade II

3 = Grade III

4 = Grade IV

5 = Non Seismic

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemChinese\_2010()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Chinese 2010")

   'set preference item
      ret = SapModel.DesignSteel.Chinese\_2010.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.2.

Added Seismic Design Grade preference item in v18.0.0.

## See Also

[GetPreference](GetPreference_{Steel_Chinese_2010}.htm)



## DeleteResults {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/DeleteResults_{Steel}.htm`*

# DeleteResults

## Syntax

SapObject.SapModel.DesignSteel.DeleteResults

## VB6 Procedure

Function DeleteResults() As Long

## Parameters

None

## Remarks

This function deletes all steel frame design results.

The function returns zero if the results are successfully deleted; otherwise it returns a nonzero value.

## VBA Example

Sub DeleteSteelDesignResults()
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

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'delete steel design results
      ret = SapModel.DesignSteel.DeleteResults

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## BeamDesignForces

*Source file: `SAP2000_API_Fuctions/Design/Steel/Design_Forces/BeamDesignForces.htm`*

# BeamDesignForces

## Syntax

SapObject.SapModel.DesignResults.DesignForces.BeamDesignForces

## VB6 Procedure

Function BeamDesignForces (

ByVal Name As String,

ByRef NumberResults As Long,

ByRef FrameName As String(),

ByRef ComboName As String (),

ByRef Station As Double (),

ByRef P As Double(),

ByRef V2 As Double(),

ByRef V3 As Double(),

ByRef T As Double(),

ByRef M2 As Double(),

ByRef M3 As Double(),

Optional ItemType As eItemType = eItemType.Objects) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the *ItemType* item.

NumberResults

The number of results, this is the length of all output arrays

FrameName

The frame unique name associated with each result

ComboName

The load combination for which the results are reported

Station

The location, measured from the I-end of the frame object, where the results are reported [L]

P

The design axial force in the frame object local 1-axis direction [F]

V2

The design shear force in the frame object local 2-axis direction [F]

V3

The design shear force in the frame object local 3-axis direction [F]

T

The design torsional moment about the frame object local 1-axis [FL]

M2

The design bending moment about the frame object local 2-axis [FL]

M3

The design bending moment about the frame object local 3-axis [FL]

ItemType [Optional]

This is one of the following items in the eItemType enumeration:

* Object = 0
* Group = 1
* SelectedObjects = 2

If this item is Objects, results are retrieved for the frame object specified by the Name item. This is the default.

If this item is Group, results are retrieved for all frame objects specified by the Name item.

If this item is SelectedObjects, results are retrieved for all selected frame objects and the Name item is ignored.

## Remarks

This function retrieves design forces for an existing designed beam.

The function returns zero if the forces are successfully recovered, otherwise it returns a nonzero value.

## VBA Example

Sub GetBeamDesignForces()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim NumberResults As Long

      Dim FrameName() As String

      Dim ComboName() As String

      Dim Station() As Double

      Dim P() As Double

      Dim V2() As Double

      Dim V3() As Double

Dim T() As Double

      Dim M2() As Double

      Dim M3() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(e2DFrameType\_PortalFrame, 3, 124, 3, 200)

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'run design
      ret = SapModel.DesignSteel.StartDesign

   'get beam design forces
      ret = SapModel.DesignResults.DesignForces.BeamDesignForces(“15”, NumberResults, FrameName, ComboName, Station, P, V2, V3, T, M2, M3, eItemType\_Objects)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.2



## BraceDesignForces

*Source file: `SAP2000_API_Fuctions/Design/Steel/Design_Forces/BraceDesignForces.htm`*

# BraceDesignForces

## Syntax

SapObject.SapModel.DesignResults.DesignForces.BraceDesignForces

## VB6 Procedure

Function BraceDesignForces (

ByVal Name As String,

ByRef NumberResults As Long,

ByRef FrameName As String(),

ByRef ComboName As String (),

ByRef Station As Double (),

ByRef P As Double(),

ByRef V2 As Double(),

ByRef V3 As Double(),

ByRef T As Double(),

ByRef M2 As Double(),

ByRef M3 As Double(),

Optional ItemType As eItemType = eItemType.Objects) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the *ItemType* item.

NumberResults

The number of results, this is the length of all output arrays

FrameName

The frame unique name associated with each result

ComboName

The load combination for which the results are reported

Station

The location, measured from the I-end of the frame object, where the results are reported [L]

P

The design axial force in the frame object local 1-axis direction [F]

V2

The design shear force in the frame object local 2-axis direction [F]

V3

The design shear force in the frame object local 3-axis direction [F]

T

The design torsional moment about the frame object local 1-axis [FL]

M2

The design bending moment about the frame object local 2-axis [FL]

M3

The design bending moment about the frame object local 3-axis [FL]

ItemType [Optional]

This is one of the following items in the eItemType enumeration:

* Object = 0
* Group = 1
* SelectedObjects = 2

If this item is Objects, results are retrieved for the frame object specified by the Name item. This is the default.

If this item is Group, results are retrieved for all frame objects specified by the Name item.

If this item is SelectedObjects, results are retrieved for all selected frame objects and the Name item is ignored.

## Remarks

This function retrieves design forces for an existing designed brace.

The function returns zero if the forces are successfully recovered, otherwise it returns a nonzero value.

## VBA Example

Sub  GetBraceDesignForces()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim NumberResults As Long

      Dim FrameName() As String

      Dim ComboName() As String

      Dim Station() As Double

      Dim P() As Double

      Dim V2() As Double

      Dim V3() As Double

Dim T() As Double

      Dim M2() As Double

      Dim M3() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(e2DFrameType\_PortalFrame, 3, 124, 3, 200)

   'add brace

      Dim BraceName As String

      ret = SapModel.FrameObj.AddByPoint.("3","6", BraceName)

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'run design
      ret = SapModel.DesignSteel.StartDesign

   'get brace design forces
      ret = SapModel.DesignResults.DesignForces.BraceDesignForces(BraceName, NumberResults, FrameName, ComboName, Station, P, V2, V3, T, M2, M3, eItemType\_Objects)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.2



## ColumnDesignForces

*Source file: `SAP2000_API_Fuctions/Design/Steel/Design_Forces/ColumnDesignForces.htm`*

# ColumnDesignForces

## Syntax

SapObject.SapModel.DesignResults.DesignForces.ColumnDesignForces

## VB6 Procedure

Function ColumnDesignForces (

ByVal Name As String,

ByRef NumberResults As Long,

ByRef FrameName As String(),

ByRef ComboName As String (),

ByRef Station As Double (),

ByRef P As Double(),

ByRef V2 As Double(),

ByRef V3 As Double(),

ByRef T As Double(),

ByRef M2 As Double(),

ByRef M3 As Double(),

Optional ItemType As eItemType = eItemType.Objects) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the *ItemType* item.

NumberResults

The number of results, this is the length of all output arrays

FrameName

The frame unique name associated with each result

ComboName

The load combination for which the results are reported

Station

The location, measured from the I-end of the frame object, where the results are reported [L]

P

The design axial force in the frame object local 1-axis direction [F]

V2

The design shear force in the frame object local 2-axis direction [F]

V3

The design shear force in the frame object local 3-axis direction [F]

T

The design torsional moment about the frame object local 1-axis [FL]

M2

The design bending moment about the frame object local 2-axis [FL]

M3

The design bending moment about the frame object local 3-axis [FL]

ItemType [Optional]

This is one of the following items in the eItemType enumeration:

* Object = 0
* Group = 1
* SelectedObjects = 2

If this item is Objects, results are retrieved for the frame object specified by the Name item. This is the default.

If this item is Group, results are retrieved for all frame objects specified by the Name item.

If this item is SelectedObjects, results are retrieved for all selected frame objects and the Name item is ignored.

## Remarks

This function retrieves design forces for an existing designed column.

The function returns zero if the forces are successfully recovered, otherwise it returns a nonzero value.

## VBA Example

Sub GetColumnDesignForces()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim NumberResults As Long

      Dim FrameName() As String

      Dim ComboName() As String

      Dim Station() As Double

      Dim P() As Double

      Dim V2() As Double

      Dim V3() As Double

Dim T() As Double

      Dim M2() As Double

      Dim M3() As Double

   'create Sap2000 object
      Set SapObject = CreateObject("CSI.SAP2000.API.SapObject")

   'start Sap2000 application
      SapObject.ApplicationStart

   'create SapModel object
      Set SapModel = SapObject.SapModel

   'initialize model
      ret = SapModel.InitializeNewModel

   'create model from template
      ret = SapModel.File.New2DFrame(e2DFrameType\_PortalFrame, 3, 124, 3, 200)

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'run design
      ret = SapModel.DesignSteel.StartDesign

   'get column design forces
      ret = SapModel.DesignResults.DesignForces.ColumnDesignForces(“1”, NumberResults, FrameName, ComboName, Station, P, V2, V3, T, M2, M3, eItemType\_Objects)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.2



## GetOverwrite {Steel EN 1993-1-1:2022}

*Source file: `SAP2000_API_Fuctions/Design/Steel/EN1993-1-1-2022/GetOverwrite_{Steel_EN_1993-1-1_2022}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.EN1993\_1\_1\_2022.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 56, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, y-y

18 = Unbraced length ratio, z-z

19 = Effective length factor, Ky

20 = Effective length factor, Kz

21 = Moment coefficient, kyy

22 = Moment coefficient, kzz

23 = Bending coefficient, C1

24 = Moment coefficient, kzy

25 = Moment coefficient, kyz

26 = Yield stress, Fy

27 = Compressive capacity, Nc.Rd

28 = Tensile capacity, Nt.Rd

29 = Bending capacity about y-y axis,Mcy.Rd

30 = Bending capacity about z-z axis Mcz.Rd

31 = Buckling resistance moment, Mb.Rd

32 = Shear capacity along z-z axis, Vz.Rd

33 = Shear capacity along y-y axis, Vy.Rd

34 = Demand/capacity ratio limit

35 = Section class

36 = Column buckling curve, y-y

37 = Column buckling curve, z-z

38 = Buckling curve for LTB

39 = System overstrength factor, Omega

40 = Is rolled section

41 = Unbraced length ratio, LTB

42 = (this parameters is not currently used)

43 = (this parameters is not currently used)

44 = Effective length factor, K LTB

45 = Material overstrength factor, GammaOV

46 = Warping constant, Iw

47 = Elastic torsional buckling force, Ncr T

48 = Elastic torsional-flexural buckling force, Ncr TF

49 = Bending coefficient, C2

50 = Bending coefficient, C3

51 = Warping coefficient, kw

52 = Coordinate of load application, za

53 = Shear center coordinate, zs

54 = Elastic critical moment for lateral-torsional buckling, Mcr

55 = Consider combined bending, shear and axial

56 = Bending Coefficients C1, C2, C3 Option

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = DCH MRF (Ductility Class High – Moment Frame)

2 = DCM MRF (Ductility Class Medium – Moment Frame)

3 = DCL MRF (Ductility Class Low – Moment Frame)

4 = DCH CBF (Ductility Class High – Concentrically Braced Frame)

5 = DCM CBF (Ductility Class Medium – Concentrically Braced Frame)

6 = DCL CBF (Ductility Class Low – Concentrically Braced Frame)

7 = DCH EBF (Ductility Class High – Eccentrically Braced Frame)

8 = DCM EBF (Ductility Class Medium – Eccentrically Braced Frame)

9 = DCL EBF (Ductility Class Low – Eccentrically Braced Frame)

10 = Inverted pendulum structure

11 = Secondary

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

  Value >= 0. [L]

15 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

16 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, y-y

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, z-z

  Value >= 0; 0 means use program determined value.

19 = Effective length factor sway, K2y

  Value >= 0; 0 means use program determined value.

20 = Effective length factor sway, K2z

  Value >= 0; 0 means use program determined value.

21 = Moment coefficient, kyy

  Value >= 0; 0 means use program determined value.

22 = Moment coefficient, kzz

  Value >= 0; 0 means use program determined value.

23 = Bending coefficient, C1

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, kzy

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, kyz

  Value >= 0; 0 means use program determined value.

26 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

27 = Compressive capacity, Nc.Rd

  Value >= 0; 0 means use program determined value. [F]

28 = Tensile capacity, Nt.Rd

  Value >= 0; 0 means use program determined value. [F]

29 = Bending capacity about y-y axis, Mcy.Rd

  Value >= 0; 0 means use program determined value. [FL]

30 = Bending capacity about z-z axis, Mcz.Rd

  Value >= 0; 0 means use program determined value. [FL]

31 = Buckling resistance moment, Mb.Rd

  Value >= 0; 0 means use program determined value. [FL]

32 = Shear capacity along z-z axis, Vz.Rd

  Value >= 0; 0 means use program determined value. [F]

33 = Shear capacity along y-y axis, Vy.Rd

  Value >= 0; 0 means use program determined value. [F]

34 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

35 = Section class

0 = Program default

1 = Class 1

2 = Class 2

3 = Class 3

4 = Class 4

36 = Column buckling curve, y-y

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

37 = Column buckling curve, z-z

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

38 = Buckling curve for LTB

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

39 = System overstrength factor, Omega

Value >= 0; 0 means use program determined value.

40 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

41 = Unbraced length ratio, LTB

Value >= 0; 0 means use program determined value.

42 = Effective length factor braced, K1y

Value >= 0; 0 means use program determined value.

43 = Effective length factor braced, K1z

Value >= 0; 0 means use program determined value.

44 = Effective length factor, K LTB

Value >= 0; 0 means use program determined value.

45 = Material overstrength factor, GammaOV

Value >= 0; 0 means use program determined value.

46 = Warping constant, Iw

Value >= 0; 0 means use program determined value. [L6]

47 = Elastic torsional buckling force, Ncr T

Value >= 0; 0 means use program determined value. [F]

48 = Elastic torsional-flexural buckling force, Ncr TF

Value >= 0; 0 means use program determined value. [F]

49 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

50 = Bending coefficient, C3

Value >= 0; 0 means use program determined value.

51 = Warping coefficient, kw (used in Mcr calculation)

0.5 =<Value =< 1; 0 means use program determined value which is defaulted to 1.0.

52 = Coordinate of load application, za (used in Mcr calculation)

53 = Shear center coordinate, zs (used in Mcr calculation)

54 = Elastic critical moment for lateral-torsional buckling, Mcr

Value >= 0; 0 means use program determined value. [FL]

55 = Consider combined bending, shear and axial

0 = Program Determined

1 = No

2 = Yes

56 = Bending Coefficients C1, C2, C3 Option

0 = Method 1 - ENV 1993-1-1:1992

1 = Method 2 - General

2 = Method 3 - User Defined

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemEN1993\_1\_1\_2022()

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
ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'set steel design code
ret = SapModel.DesignSteel.SetCode("EN 1993-1-1:2022")

'run analysis
ret = SapModel.File.Save("C:\SapAPI\x.sdb")
ret = SapModel.Analyze.RunAnalysis

'start steel design
ret = SapModel.DesignSteel.StartDesign

'get overwrite item
ret = SapModel.DesignSteel.EN1993\_1\_1\_2022.GetOverwrite("8", 1, Value, ProgDet)

'close Sap2000
SapObject.ApplicationExit False
Set SapModel = Nothing
Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.1.0

Added item 55 in version 26.3.0

Added item 56 in version 27.1.0

## See Also

[SetOverwrite](SetOverwrite_{Steel_EN_1993-1-1_2022}.htm)



## GetPreference {Steel EN 1993-1-1:2022}

*Source file: `SAP2000_API_Fuctions/Design/Steel/EN1993-1-1-2022/GetPreference_{Steel_EN_1993-1-1_2022}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.EN1993\_1\_1\_2022.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 24, inclusive, indicating the preference item considered.

1 = Country

2 = Combos equation

3 = Reliability class

4 = Analysis Method

5 = Multi-response case design

6 = Framing type

7 = Behavior factor, q

8 = System overstrength factor, Omega

9 = Consider P-Delta Done

10 = Consider torsion

11 = GammaM0

12 = GammaM1

13 = GammaM2

14 = Ignore seismic code

15 = Ignore special seismic load

16 = Doubler plate is plug-welded

17 = Consider deflection

18 = DL deflection limit, L/Value

19 = SDL + LL deflection limit, L/Value

20 = LL deflection limit, L/Value

21 = Total deflection limit, L/Value

22 = Total camber limit, L/Value

23 = Pattern live load factor

24 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Country

   1 = CEN Default

   2 = United Kingdom

   3 = Slovenia

   4 = Bulgaria

   5 = Norway

   7 = Sweden

   8 = Finland

   9 = Denmark

 10 = Portugal

 11 = Germany

2 = Combos equation

   1 = 1 = Eq. 6.10

   2 = Max of Eqs. 6.10a and 6.10b

3 = Reliability class

   1 = Class 1

   2 = Class 2

   3 = Class 3

4 = Analysis Method

   1 = EM

   2 = M0

   3 = M1

   4 = M2

   5 = M3

   6 = M4

   7 = M5

5 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step --  All

6 = Framing type

1 = DCH MRF (Ductility Class High - Moment Frame)

2 = DCM MRF (Ductility Class Medium - Moment Frame)

3 = DCL MRF (Ductility Class Low - Moment Frame)

4 = DCH CBF (Ductility Class High - Concentrically Braced Frame)

5 = DCH CBF (Ductility Class Medium - Concentrically Braced Frame)

6 = DCH CBF (Ductility Class Low - Concentrically Braced Frame)

7 = DCH EBF (Ductility Class High - Eccentrically Braced Frame)

8 = DCM EBF (Ductility Class Medium - Eccentrically Braced Frame)

9 = DCL EBF (Ductility Class Low - Eccentrically Braced Frame)

10 = Inverted pendulum structure

11 = Secondary

7 = Behavior factor, q

Value > 0

8 = System overstrength factor, Omega

Value > 0

9 = Consider P-Delta Done

0 = No

Any other value = Yes

10 = Consider torsion

0 = No

Any other value = Yes

11 = GammaM0

Value > 0

12 = GammaM1

Value > 0

13 = GammaM2

      Value > 0

14 = Ignore seismic code

0 = No

Any other value = Yes

15 = Ignore special seismic load

0 = No

Any other value = Yes

16 = Doubler plate is plug-welded

0 = No

Any other value = Yes

17 = Consider deflection

0 = No

Any other value = Yes

18 = DL deflection limit, L/Value

Value > 0

19 = SDL + LL deflection limit, L/Value

  Value > 0

20 = LL deflection limit, L/Value

  Value > 0

21 = Total deflection limit, L/Value

  Value > 0

22 = Total camber limit, L/Value

  Value > 0

23 = Pattern live load factor

  Value >= 0

24 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemEN1993\_1\_1\_2022()
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
ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

'set steel design code
ret = SapModel.DesignSteel.SetCode("EN 1993-1-1:2022")

'get preference item
ret = SapModel.DesignSteel.EN1993\_1\_1\_2022.GetPreference(4, Value)

'close Sap2000
SapObject.ApplicationExit False
Set SapModel = Nothing
Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.1.0

## See Also

[SetPreference](SetPreference_{Steel_EN_1993-1-1_2022}.htm)



## SetOverwrite {Steel EN 1993-1-1:2022}

*Source file: `SAP2000_API_Fuctions/Design/Steel/EN1993-1-1-2022/SetOverwrite_{Steel_EN_1993-1-1_2022}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.EN1993\_1\_1\_2022.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 56, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, y-y

18 = Unbraced length ratio, z-z

19 = Effective length factor, Ky

20 = Effective length factor, Kz

21 = Moment coefficient, kyy

22 = Moment coefficient, kzz

23 = Bending coefficient, C1

24 = Moment coefficient, kzy

25 = Moment coefficient, kyz

26 = Yield stress, Fy

27 = Compressive capacity, Nc.Rd

28 = Tensile capacity, Nt.Rd

29 = Bending capacity about y-y axis,Mcy.Rd

30 = Bending capacity about z-z axis Mcz.Rd

31 = Buckling resistance moment, Mb.Rd

32 = Shear capacity along z-z axis, Vz.Rd

33 = Shear capacity along y-y axis, Vy.Rd

34 = Demand/capacity ratio limit

35 = Section class

36 = Column buckling curve, y-y

37 = Column buckling curve, z-z

38 = Buckling curve for LTB

39 = System overstrength factor, Omega

40 = Is rolled section

41 = Unbraced length ratio, LTB

42 = (This parameter is not currently used)

43 = (This parameter is not currently used)

44 = Effective length factor, K LTB

45 = Material overstrength factor, GammaOV

46 = Warping constant, Iw

47 = Elastic torsional buckling force, Ncr T

48 = Elastic torsional-flexural buckling force, Ncr TF

49 = Bending coefficient, C2

50 = Bending coefficient, C3

51 = Warping coefficient, kw

52 = Coordinate of load application, za (used in Mcr calculation)

53 = Shear center coordinate, zs (used in Mcr calculation)

54 = Elastic critical moment for lateral-torsional buckling, Mcr

55 = Consider combined bending, shear and axial

56 = Bending Coefficients C1, C2, C3 Option

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = DCH MRF (Ductility Class High – Moment Frame)

2 = DCM MRF (Ductility Class Medium – Moment Frame)

3 = DCL MRF (Ductility Class Low – Moment Frame)

4 = DCH CBF (Ductility Class High – Concentrically Braced Frame)

5 = DCM CBF (Ductility Class Medium – Concentrically Braced Frame)

6 = DCL CBF (Ductility Class Low – Concentrically Braced Frame)

7 = DCH EBF (Ductility Class High – Eccentrically Braced Frame)

8 = DCM EBF (Ductility Class Medium – Eccentrically Braced Frame)

9 = DCL EBF (Ductility Class Low – Eccentrically Braced Frame)

10 = Inverted pendulum structure

11 = Secondary

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, y-y

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, z-z

  Value >= 0; 0 means use program determined value.

19 = Effective length factor sway, Ky

  Value >= 0; 0 means use program determined value.

20 = Effective length factor sway, Kz

  Value >= 0; 0 means use program determined value.

21 = Moment coefficient, kyy

  Value >= 0; 0 means use program determined value.

22 = Moment coefficient, kzz

  Value >= 0; 0 means use program determined value.

23 = Bending coefficient, C1

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, kzy

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, kyz

  Value >= 0; 0 means use program determined value.

26 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

27 = Compressive capacity, Nc.Rd

  Value >= 0; 0 means use program determined value. [F]

28 = Tensile capacity, Nt.Rd

  Value >= 0; 0 means use program determined value. [F]

29 = Bending capacity about y-y axis, Mcy.Rd

  Value >= 0; 0 means use program determined value. [FL]

30 = Bending capacity about z-z axis, Mcz.Rd

  Value >= 0; 0 means use program determined value. [FL]

31 = Buckling resistance moment, Mb.Rd

  Value >= 0; 0 means use program determined value. [FL]

32 = Shear capacity along z-z axis, Vz.Rd

  Value >= 0; 0 means use program determined value. [F]

33 = Shear capacity along y-y axis, Vy.Rd

  Value >= 0; 0 means use program determined value. [F]

34 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

35 = Section class

0 = Program default

1 = Class 1

2 = Class 2

3 = Class 3

4 = Class 4

36 = Column buckling curve, y-y

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

37 = Column buckling curve, z-z

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

38 = Buckling curve for LTB

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

39 = System overstrength factor, Omega

Value >= 0; 0 means use program determined value.

40 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

41 = Unbraced length ratio, LTB

Value >= 0; 0 means use program determined value.

42 = (Entries for this parameter are currently ignored)

43 = (Entries for this parameter are currently ignored)

44 = Effective length factor, K LTB

Value >= 0; 0 means use program determined value.

45 = Material overstrength factor, GammaOV

Value >= 0; 0 means use program determined value.

46 = Warping constant, Iw

Value >= 0; 0 means use program determined value. [L6]

47 = Elastic torsional buckling force, Ncr T

Value >= 0; 0 means use program determined value. [F]

48 = Elastic torsional-flexural buckling force, Ncr TF

Value >= 0; 0 means use program determined value. [F]

49 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

50 = Bending coefficient, C3

Value >= 0; 0 means use program determined value.

51 = Warping coefficient, kw (used in Mcr calculation)

0.5 =<Value =< 1; 0 means use program determined value which is defaulted to 1.0.

52 = Coordinate of load application, za (used in Mcr calculation)

53 = Shear center coordinate, zs (used in Mcr calculation)

54 = Elastic critical moment for lateral-torsional buckling, Mcr

Value >= 0; 0 means use program determined value. [FL]

55 = Consider combined bending, shear and axial

0 = Program Determined

1 = No

2 = Yes

56 = Bending Coefficients C1, C2, C3 Option

0 = Method 1 - ENV 1993-1-1:1992

1 = Method 2 - General

2 = Method 3 - User Defined

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## VBA Example

Sub SetSteelDesignOverwriteItemEN1993\_1\_1\_2022()
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

'set steel design code
ret = SapModel.DesignSteel.SetCode("EN 1993-1-1:2022")

'set overwrite item
ret = SapModel.DesignSteel.EN1993\_1\_1\_2022.SetOverwrite("8", 1, 2)

'close Sap2000
SapObject.ApplicationExit False
Set SapModel = Nothing
Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.1.0

Added item 55 in version 26.3.0

Added item 56 in version 27.1.0

## See Also

[GetOverwrite](GetOverwrite_{Steel_EN_1993-1-1_2022}.htm)



## SetPreference {Steel EN 1993-1-1:2022}

*Source file: `SAP2000_API_Fuctions/Design/Steel/EN1993-1-1-2022/SetPreference_{Steel_EN_1993-1-1_2022}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.EN1993\_1\_1\_2022.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 16, inclusive, indicating the preference item considered.

1 = Country

2 = Combos equation

3 = Reliability class

4 = Analysis Method

5 = Multi-response case design

6 = Framing type

7 = Behavior factor, q

8 = System overstrength factor, Omega

9 = Consider P-Delta Done

10 = Consider torsion

11 = GammaM0

12 = GammaM1

13 = GammaM2

14 = Ignore seismic code

15 = Ignore special seismic load

16 = Doubler plate is plug-welded

17 = Consider deflection

18 = DL deflection limit, L/Value

19 = SDL + LL deflection limit, L/Value

20 = LL deflection limit, L/Value

21 = Total deflection limit, L/Value

22 = Total camber limit, L/Value

23 = Pattern live load factor

24 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Country

   1 = CEN Default

   2 = United Kingdom

   3 = Slovenia

   4 = Bulgaria

   5 = Norway

   7 = Sweden

   8 = Finland

   9 = Denmark

 10 = Portugal

 11 = Germany

2 = Combos equation

   1 = 1 = Eq. 6.10

   2 = Max of Eqs. 6.10a and 6.10b

3 = Reliability class

   1 = Class 1

   2 = Class 2

   3 = Class 3

4 = Analysis Method

   1 = EM

   2 = M0

   3 = M1

   4 = M2

   5 = M3

   6 = M4

   7 = M5

5 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step --  All

6 = Framing type

1 = DCH MRF (Ductility Class High - Moment Frame)

2 = DCM MRF (Ductility Class Medium - Moment Frame)

3 = DCL MRF (Ductility Class Low - Moment Frame)

4 = DCH CBF (Ductility Class High - Concentrically Braced Frame)

5 = DCH CBF (Ductility Class Medium - Concentrically Braced Frame)

6 = DCH CBF (Ductility Class Low - Concentrically Braced Frame)

7 = DCH EBF (Ductility Class High - Eccentrically Braced Frame)

8 = DCM EBF (Ductility Class Medium - Eccentrically Braced Frame)

9 = DCL EBF (Ductility Class Low - Eccentrically Braced Frame)

10 = Inverted pendulum structure

11 = Secondary

7 = Behavior factor, q

Value > 0

8 = System overstrength factor, Omega

Value > 0

9 = Consider P-Delta Done

0 = No

Any other value = Yes

10 = Consider torsion

0 = No

Any other value = Yes

11 = GammaM0

Value > 0

12 = GammaM1

Value > 0

13 = GammaM2

      Value > 0

14 = Ignore seismic code

0 = No

Any other value = Yes

15 = Ignore special seismic load

0 = No

Any other value = Yes

16 = Doubler plate is plug-welded

0 = No

Any other value = Yes

17 = Consider deflection

0 = No

Any other value = Yes

18 = DL deflection limit, L/Value

Value > 0

19 = SDL + LL deflection limit, L/Value

  Value > 0

20 = LL deflection limit, L/Value

  Value > 0

21 = Total deflection limit, L/Value

  Value > 0

22 = Total camber limit, L/Value

  Value > 0

23 = Pattern live load factor

  Value >= 0

24 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemEN1993\_1\_1\_2022()
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

'set steel design code
ret = SapModel.DesignSteel.SetCode("EN 1993-1-1:2022")

'set preference item
ret = SapModel.DesignSteel.EN1993\_1\_1\_2022.SetPreference(4, 2)

'close Sap2000
SapObject.ApplicationExit False
Set SapModel = Nothing
Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 26.1.0

## See Also

[GetPreference](GetPreference_{Steel_EN_1993-1-1_2022}.htm)



## GetOverwrite {Steel EN 1993-1-1:2005}

*Source file: `SAP2000_API_Fuctions/Design/Steel/EN_1993_1_1_2005_(Formerly_Eurocode_3-2005)/GetOverwrite_{Steel_EN_1993-1-1_2005}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.EN1993\_1\_1\_2005.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 56, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, y-y

18 = Unbraced length ratio, z-z

19 = Effective length factor, K2y

20 = Effective length factor, K2z

21 = Moment coefficient, kyy

22 = Moment coefficient, kzz

23 = Bending coefficient, C1

24 = Moment coefficient, kzy

25 = Moment coefficient, kyz

26 = Yield stress, Fy

27 = Compressive capacity, Nc.Rd

28 = Tensile capacity, Nt.Rd

29 = Bending capacity about y-y axis,Mcy.Rd

30 = Bending capacity about z-z axis Mcz.Rd

31 = Buckling resistance moment, Mb.Rd

32 = Shear capacity along z-z axis, Vz.Rd

33 = Shear capacity along y-y axis, Vy.Rd

34 = Demand/capacity ratio limit

35 = Section class

36 = Column buckling curve, y-y

37 = Column buckling curve, z-z

38 = Buckling curve for LTB

39 = System overstrength factor, Omega

40 = Is rolled section

41 = Unbraced length ratio, LTB

42 = Effective length factor braced, K1y

43 = Effective length factor braced, K1z

44 = Effective length factor, K LTB

45 = Material overstrength factor, GammaOV

46 = Warping constant, Iw

47 = Elastic torsional buckling force, Ncr T

48 = Elastic torsional-flexural buckling force, Ncr TF

49 = Bending coefficient, C2

50 = Bending coefficient, C3

51 = Warping coefficient, kw

52 = Coordinate of load application, za

53 = Shear center coordinate, zs

54 = Elastic critical moment for lateral-torsional buckling, Mcr

55 =(this parameters is not currently used)

56 = Bending Coefficients C1, C2, C3 Option

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = DCH MRF (Ductility Class High – Moment Frame)

2 = DCM MRF (Ductility Class Medium – Moment Frame)

3 = DCL MRF (Ductility Class Low – Moment Frame)

4 = DCH CBF (Ductility Class High – Concentrically Braced Frame)

5 = DCM CBF (Ductility Class Medium – Concentrically Braced Frame)

6 = DCL CBF (Ductility Class Low – Concentrically Braced Frame)

7 = DCH EBF (Ductility Class High – Eccentrically Braced Frame)

8 = DCM EBF (Ductility Class Medium – Eccentrically Braced Frame)

9 = DCL EBF (Ductility Class Low – Eccentrically Braced Frame)

10 = Inverted pendulum structure

11 = Secondary

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

  Value >= 0. [L]

15 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

16 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, y-y

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, z-z

  Value >= 0; 0 means use program determined value.

19 = Effective length factor sway, K2y

  Value >= 0; 0 means use program determined value.

20 = Effective length factor sway, K2z

  Value >= 0; 0 means use program determined value.

21 = Moment coefficient, kyy

  Value >= 0; 0 means use program determined value.

22 = Moment coefficient, kzz

  Value >= 0; 0 means use program determined value.

23 = Bending coefficient, C1

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, kzy

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, kyz

  Value >= 0; 0 means use program determined value.

26 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

27 = Compressive capacity, Nc.Rd

  Value >= 0; 0 means use program determined value. [F]

28 = Tensile capacity, Nt.Rd

  Value >= 0; 0 means use program determined value. [F]

29 = Bending capacity about y-y axis, Mcy.Rd

  Value >= 0; 0 means use program determined value. [FL]

30 = Bending capacity about z-z axis, Mcz.Rd

  Value >= 0; 0 means use program determined value. [FL]

31 = Buckling resistance moment, Mb.Rd

  Value >= 0; 0 means use program determined value. [FL]

32 = Shear capacity along z-z axis, Vz.Rd

  Value >= 0; 0 means use program determined value. [F]

33 = Shear capacity along y-y axis, Vy.Rd

  Value >= 0; 0 means use program determined value. [F]

34 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

35 = Section class

0 = Program default

1 = Class 1

2 = Class 2

3 = Class 3

4 = Class 4

36 = Column buckling curve, y-y

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

37 = Column buckling curve, z-z

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

38 = Buckling curve for LTB

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

39 = System overstrength factor, Omega

Value >= 0; 0 means use program determined value.

40 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

41 = Unbraced length ratio, LTB

Value >= 0; 0 means use program determined value.

42 = Effective length factor braced, K1y

Value >= 0; 0 means use program determined value.

43 = Effective length factor braced, K1z

Value >= 0; 0 means use program determined value.

44 = Effective length factor, K LTB

Value >= 0; 0 means use program determined value.

45 = Material overstrength factor, GammaOV

Value >= 0; 0 means use program determined value.

46 = Warping constant, Iw

Value >= 0; 0 means use program determined value. [L6]

47 = Elastic torsional buckling force, Ncr T

Value >= 0; 0 means use program determined value. [F]

48 = Elastic torsional-flexural buckling force, Ncr TF

Value >= 0; 0 means use program determined value. [F]

49 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

50 = Bending coefficient, C3

Value >= 0; 0 means use program determined value.

51 = Warping coefficient, kw (used in Mcr calculation)

0.5 =<Value =< 1; 0 means use program determined value which is defaulted to 1.0.

52 = Coordinate of load application, za (used in Mcr calculation)

53 = Shear center coordinate, zs (used in Mcr calculation)

54 = Elastic critical moment for lateral-torsional buckling, Mcr

Value >= 0; 0 means use program determined value. [FL]

55 = (this parameter is not currently used)

56 = Bending Coefficients C1, C2, C3 Option

0 = Method 1 - ENV 1993-1-1:1992

1 = Method 2 - General

2 = Method 3 - User Defined

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemEN1993\_1\_1\_2005()

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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("EN 1993-1-1:2005")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.EN1993\_1\_1\_2005.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.1.0

Added item 56 in version 27.1.0

## See Also

[SetOverwrite](SetOverwrite_{Steel_EN_1993-1-1_2005}.htm)



## GetPreference {Steel EN 1993-1-1:2005}

*Source file: `SAP2000_API_Fuctions/Design/Steel/EN_1993_1_1_2005_(Formerly_Eurocode_3-2005)/GetPreference_{Steel_EN_1993-1-1_2005}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.EN1993\_1\_1\_2005.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 24, inclusive, indicating the preference item considered.

1 = Country

2 = Combos equation

3 = Reliability class

4 = K factor method

5 = Multi-response case design

6 = Framing type

7 = Behavior factor, q

8 = System overstrength factor, Omega

9 = Consider P-Delta Done

10 = Consider torsion

11 = GammaM0

12 = GammaM1

13 = GammaM2

14 = Ignore seismic code

15 = Ignore special seismic load

16 = Doubler plate is plug-welded

17 = Consider deflection

18 = DL deflection limit, L/Value

19 = SDL + LL deflection limit, L/Value

20 = LL deflection limit, L/Value

21 = Total deflection limit, L/Value

22 = Total camber limit, L/Value

23 = Pattern live load factor

24 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Country

   1 = CEN Default

   2 = United Kingdom

   3 = Slovenia

   4 = Bulgaria

   5 = Norway

   7 = Sweden

   8 = Finland

   9 = Denmark

 10 = Portugal

 11 = Germany

2 = Combos equation

   1 = 1 = Eq. 6.10

   2 = Max of Eqs. 6.10a and 6.10b

3 = Reliability class

   1 = Class 1

   2 = Class 2

   3 = Class 3

4 = K factor method

   1 = Method 1 (Annex A)

   2 = Method 2 (Annex B)

5 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step --  All

6 = Framing type

1 = DCH MRF (Ductility Class High - Moment Frame)

2 = DCM MRF (Ductility Class Medium - Moment Frame)

3 = DCL MRF (Ductility Class Low - Moment Frame)

4 = DCH CBF (Ductility Class High - Concentrically Braced Frame)

5 = DCH CBF (Ductility Class Medium - Concentrically Braced Frame)

6 = DCH CBF (Ductility Class Low - Concentrically Braced Frame)

7 = DCH EBF (Ductility Class High - Eccentrically Braced Frame)

8 = DCM EBF (Ductility Class Medium - Eccentrically Braced Frame)

9 = DCL EBF (Ductility Class Low - Eccentrically Braced Frame)

10 = Inverted pendulum structure

11 = Secondary

7 = Behavior factor, q

Value > 0

8 = System overstrength factor, Omega

Value > 0

9 = Consider P-Delta Done

0 = No

Any other value = Yes

10 = Consider torsion

0 = No

Any other value = Yes

11 = GammaM0

Value > 0

12 = GammaM1

Value > 0

13 = GammaM2

      Value > 0

14 = Ignore seismic code

0 = No

Any other value = Yes

15 = Ignore special seismic load

0 = No

Any other value = Yes

16 = Doubler plate is plug-welded

0 = No

Any other value = Yes

17 = Consider deflection

0 = No

Any other value = Yes

18 = DL deflection limit, L/Value

Value > 0

19 = SDL + LL deflection limit, L/Value

  Value > 0

20 = LL deflection limit, L/Value

  Value > 0

21 = Total deflection limit, L/Value

  Value > 0

22 = Total camber limit, L/Value

  Value > 0

23 = Pattern live load factor

  Value >= 0

24 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemEN1993\_1\_1\_2005()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("EN 1993-1-1:2005")

   'get preference item
      ret = SapModel.DesignSteel.EN1993\_1\_1\_2005.GetPreference(4, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.1.0

## See Also

[SetPreference](SetPreference_{Steel_EN_1993-1-1_2005}.htm)



## SetOverwrite {Steel EN 1993-1-1:2005}

*Source file: `SAP2000_API_Fuctions/Design/Steel/EN_1993_1_1_2005_(Formerly_Eurocode_3-2005)/SetOverwrite_{Steel_EN_1993-1-1_2005}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.EN1993\_1\_1\_2005.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 56, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, y-y

18 = Unbraced length ratio, z-z

19 = Effective length factor, K2y

20 = Effective length factor, K2z

21 = Moment coefficient, kyy

22 = Moment coefficient, kzz

23 = Bending coefficient, C1

24 = Moment coefficient, kzy

25 = Moment coefficient, kyz

26 = Yield stress, Fy

27 = Compressive capacity, Nc.Rd

28 = Tensile capacity, Nt.Rd

29 = Bending capacity about y-y axis,Mcy.Rd

30 = Bending capacity about z-z axis Mcz.Rd

31 = Buckling resistance moment, Mb.Rd

32 = Shear capacity along z-z axis, Vz.Rd

33 = Shear capacity along y-y axis, Vy.Rd

34 = Demand/capacity ratio limit

35 = Section class

36 = Column buckling curve, y-y

37 = Column buckling curve, z-z

38 = Buckling curve for LTB

39 = System overstrength factor, Omega

40 = Is rolled section

41 = Unbraced length ratio, LTB

42 = Effective length factor braced, K1y

43 = Effective length factor braced, K1z

44 = Effective length factor, K LTB

45 = Material overstrength factor, GammaOV

46 = Warping constant, Iw

47 = Elastic torsional buckling force, Ncr T

48 = Elastic torsional-flexural buckling force, Ncr TF

49 = Bending coefficient, C2

50 = Bending coefficient, C3

51 = Warping coefficient, kw

52 = Coordinate of load application, za (used in Mcr calculation)

53 = Shear center coordinate, zs (used in Mcr calculation)

54 = Elastic critical moment for lateral-torsional buckling, Mcr

55 =(this parameters is not currently used)

56 = Bending Coefficients C1, C2, C3 Option

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = DCH MRF (Ductility Class High – Moment Frame)

2 = DCM MRF (Ductility Class Medium – Moment Frame)

3 = DCL MRF (Ductility Class Low – Moment Frame)

4 = DCH CBF (Ductility Class High – Concentrically Braced Frame)

5 = DCM CBF (Ductility Class Medium – Concentrically Braced Frame)

6 = DCL CBF (Ductility Class Low – Concentrically Braced Frame)

7 = DCH EBF (Ductility Class High – Eccentrically Braced Frame)

8 = DCM EBF (Ductility Class Medium – Eccentrically Braced Frame)

9 = DCL EBF (Ductility Class Low – Eccentrically Braced Frame)

10 = Inverted pendulum structure

11 = Secondary

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, y-y

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, z-z

  Value >= 0; 0 means use program determined value.

19 = Effective length factor sway, K2y

  Value >= 0; 0 means use program determined value.

20 = Effective length factor sway, K2z

  Value >= 0; 0 means use program determined value.

21 = Moment coefficient, kyy

  Value >= 0; 0 means use program determined value.

22 = Moment coefficient, kzz

  Value >= 0; 0 means use program determined value.

23 = Bending coefficient, C1

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, kzy

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, kyz

  Value >= 0; 0 means use program determined value.

26 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

27 = Compressive capacity, Nc.Rd

  Value >= 0; 0 means use program determined value. [F]

28 = Tensile capacity, Nt.Rd

  Value >= 0; 0 means use program determined value. [F]

29 = Bending capacity about y-y axis, Mcy.Rd

  Value >= 0; 0 means use program determined value. [FL]

30 = Bending capacity about z-z axis, Mcz.Rd

  Value >= 0; 0 means use program determined value. [FL]

31 = Buckling resistance moment, Mb.Rd

  Value >= 0; 0 means use program determined value. [FL]

32 = Shear capacity along z-z axis, Vz.Rd

  Value >= 0; 0 means use program determined value. [F]

33 = Shear capacity along y-y axis, Vy.Rd

  Value >= 0; 0 means use program determined value. [F]

34 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

35 = Section class

0 = Program default

1 = Class 1

2 = Class 2

3 = Class 3

4 = Class 4

36 = Column buckling curve, y-y

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

37 = Column buckling curve, z-z

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

38 = Buckling curve for LTB

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

39 = System overstrength factor, Omega

Value >= 0; 0 means use program determined value.

40 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

41 = Unbraced length ratio, LTB

Value >= 0; 0 means use program determined value.

42 = Effective length factor braced, K1y

Value >= 0; 0 means use program determined value.

43 = Effective length factor braced, K1z

Value >= 0; 0 means use program determined value.

44 = Effective length factor, K LTB

Value >= 0; 0 means use program determined value.

45 = Material overstrength factor, GammaOV

Value >= 0; 0 means use program determined value.

46 = Warping constant, Iw

Value >= 0; 0 means use program determined value. [L6]

47 = Elastic torsional buckling force, Ncr T

Value >= 0; 0 means use program determined value. [F]

48 = Elastic torsional-flexural buckling force, Ncr TF

Value >= 0; 0 means use program determined value. [F]

49 = Bending coefficient, C2

Value >= 0; 0 means use program determined value.

50 = Bending coefficient, C3

Value >= 0; 0 means use program determined value.

51 = Warping coefficient, kw (used in Mcr calculation)

0.5 =<Value =< 1; 0 means use program determined value which is defaulted to 1.0.

52 = Coordinate of load application, za (used in Mcr calculation)

53 = Shear center coordinate, zs (used in Mcr calculation)

54 = Elastic critical moment for lateral-torsional buckling, Mcr

Value >= 0; 0 means use program determined value. [FL]

55 = (this parameter is not currently used)

56 = Bending Coefficients C1, C2, C3 Option

0 = Method 1 - ENV 1993-1-1:1992

1 = Method 2 - General

2 = Method 3 - User Defined

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemEN1993\_1\_1\_2005()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("EN 1993-1-1:2005")

   'set overwrite item
      ret = SapModel.DesignSteel.EN1993\_1\_1\_2005.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.1.0

Added item 56 in version 27.1.0

## See Also

[GetOverwrite](GetOverwrite_{Steel_EN_1993-1-1_2005}.htm)



## SetPreference {Steel EN 1993-1-1:2005}

*Source file: `SAP2000_API_Fuctions/Design/Steel/EN_1993_1_1_2005_(Formerly_Eurocode_3-2005)/SetPreference_{Steel_EN_1993-1-1_2005}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.EN1993\_1\_1\_2005.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 16, inclusive, indicating the preference item considered.

1 = Country

2 = Combos equation

3 = Reliability class

4 = K factor method

5 = Multi-response case design

6 = Framing type

7 = Behavior factor, q

8 = System overstrength factor, Omega

9 = Consider P-Delta Done

10 = Consider torsion

11 = GammaM0

12 = GammaM1

13 = GammaM2

14 = Ignore seismic code

15 = Ignore special seismic load

16 = Doubler plate is plug-welded

17 = Consider deflection

18 = DL deflection limit, L/Value

19 = SDL + LL deflection limit, L/Value

20 = LL deflection limit, L/Value

21 = Total deflection limit, L/Value

22 = Total camber limit, L/Value

23 = Pattern live load factor

24 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Country

   1 = CEN Default

   2 = United Kingdom

   3 = Slovenia

   4 = Bulgaria

   5 = Norway

   7 = Sweden

   8 = Finland

   9 = Denmark

 10 = Portugal

 11 = Germany

2 = Combos equation

   1 = 1 = Eq. 6.10

   2 = Max of Eqs. 6.10a and 6.10b

3 = Reliability class

   1 = Class 1

   2 = Class 2

   3 = Class 3

4 = K factor method

   1 = Method 1 (Annex A)

   2 = Method 2 (Annex B)

5 = Multi-response case design

1 = Envelopes

2 = Step-by-step

3 = Last step

4 = Envelopes -- All

5 = Step-by-step --  All

6 = Framing type

1 = DCH MRF (Ductility Class High - Moment Frame)

2 = DCM MRF (Ductility Class Medium - Moment Frame)

3 = DCL MRF (Ductility Class Low - Moment Frame)

4 = DCH CBF (Ductility Class High - Concentrically Braced Frame)

5 = DCH CBF (Ductility Class Medium - Concentrically Braced Frame)

6 = DCH CBF (Ductility Class Low - Concentrically Braced Frame)

7 = DCH EBF (Ductility Class High - Eccentrically Braced Frame)

8 = DCM EBF (Ductility Class Medium - Eccentrically Braced Frame)

9 = DCL EBF (Ductility Class Low - Eccentrically Braced Frame)

10 = Inverted pendulum structure

11 = Secondary

7 = Behavior factor, q

Value > 0

8 = System overstrength factor, Omega

Value > 0

9 = Consider P-Delta Done

0 = No

Any other value = Yes

10 = Consider torsion

0 = No

Any other value = Yes

11 = GammaM0

Value > 0

12 = GammaM1

Value > 0

13 = GammaM2

      Value > 0

14 = Ignore seismic code

0 = No

Any other value = Yes

15 = Ignore special seismic load

0 = No

Any other value = Yes

16 = Doubler plate is plug-welded

0 = No

Any other value = Yes

17 = Consider deflection

0 = No

Any other value = Yes

18 = DL deflection limit, L/Value

Value > 0

19 = SDL + LL deflection limit, L/Value

  Value > 0

20 = LL deflection limit, L/Value

  Value > 0

21 = Total deflection limit, L/Value

  Value > 0

22 = Total camber limit, L/Value

  Value > 0

23 = Pattern live load factor

  Value >= 0

24 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemEN1993\_1\_1\_2005()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("EN 1993-1-1:2005")

   'set preference item
      ret = SapModel.DesignSteel.EN1993\_1\_1\_2005.SetPreference(4, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 25.1.0

## See Also

[GetPreference](GetPreference_{Steel_EN_1993-1-1_2005}.htm)



## GetOverwrite {Steel Eurocode 3-1993}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Eurocode_3-1993/GetOverwrite_{Steel_Eurocode_3-1993}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.EUROCODE\_3\_1993.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 36, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, k Major

22 = Moment coefficient, k Minor

23 = Bending coefficient, C1

24 = Moment coefficient, k Lateral Torsional Buckling

25 = Non-sway moment factor

26 = Sway moment factor, Psi Major

27 = Sway moment factor, Psi Minor

28 = Yield stress, Fy

29 = Compressive capacity, Nc.Rd

30 = Tensile capacity, Nt.Rd

31 = Major bending capacity, Mc3.Rd

32 = Minor bending capacity, Mc2.Rd

33 = Buckling resistance moment, Mb.Rd

34 = Major shear capacity, V2.Rd

35 = Minor shear capacity, V3.RD

36 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, k Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, k Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, C1

Value >= 0; 0 means use program determined value.

24 = Moment coefficient, k Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

25 = Non-sway moment factor

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, Psi Major

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, Psi Minor

Value >= 0; 0 means use program determined value.

28 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

29 = Compressive capacity, Nc.Rd

Value >= 0; 0 means use program determined value. [F]

30 = Tensile capacity, Nt.Rd

Value >= 0; 0 means use program determined value. [F]

31 = Major bending capacity, Mc3.Rd

Value >= 0; 0 means use program determined value. [FL]

32 = Minor bending capacity, Mc2.Rd

Value >= 0; 0 means use program determined value. [FL]

33 = Buckling resistance moment, Mb.Rd

Value >= 0; 0 means use program determined value. [FL]

34 = Major shear capacity, Vn2.Rd

Value >= 0; 0 means use program determined value. [F]

35 = Minor shear capacity, Vn3.RD

Value >= 0; 0 means use program determined value. [F]

36 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemEUROCODE\_3\_1993()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("EUROCODE 3-1993")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.EUROCODE\_3\_1993.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_Eurocode_3-1993}.htm)



## GetPreference {Steel Eurocode 3-1993}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Eurocode_3-1993/GetPreference_{Steel_Eurocode_3-1993}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.EUROCODE\_3\_1993.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 12, inclusive, indicating the preference item considered.

1 = Framing type

2 = GammaM0

3 = GammeM1

4 = Consider deflection

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total deflection limit, L/Value

9 = Total camber limit, L/Value

10 = Pattern live load factor

11 = Demand/capacity ratio limit

12 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = GammaM0

Value > 0

3 = GammeM1

Value > 0

4 = Consider deflection

0 = No

Any other value = Yes

5 = DL deflection limit, L/Value

Value > 0

6 = SDL + LL deflection limit, L/Value

Value > 0

7 = LL deflection limit, L/Value

Value > 0

8 = Total deflection limit, L/Value

Value > 0

9 = Total camber limit, L/Value

Value > 0

10 = Pattern live load factor

Value >= 0

11 = Demand/capacity ratio limit

Value > 0

12 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemEUROCODE\_3\_1993()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("EUROCODE 3-1993")

   'get preference item
      ret = SapModel.DesignSteel.EUROCODE\_3\_1993.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_Eurocode_3-1993}.htm)



## SetOverwrite {Steel Eurocode 3-1993}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Eurocode_3-1993/SetOverwrite_{Steel_Eurocode_3-1993}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.EUROCODE\_3\_1993.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 36, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, k Major

22 = Moment coefficient, k Minor

23 = Bending coefficient, C1

24 = Moment coefficient, k Lateral Torsional Buckling

25 = Non-sway moment factor

26 = Sway moment factor, Psi Major

27 = Sway moment factor, Psi Minor

28 = Yield stress, Fy

29 = Compressive capacity, Nc.Rd

30 = Tensile capacity, Nt.Rd

31 = Major bending capacity, Mc3.Rd

32 = Minor bending capacity, Mc2.Rd

33 = Buckling resistance moment, Mb.Rd

34 = Major shear capacity, V2.Rd

35 = Minor shear capacity, V3.RD

36 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

21 = Moment coefficient, k Major

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, k Minor

Value >= 0; 0 means use program determined value.

23 = Bending coefficient, C1

Value >= 0; 0 means use program determined value.

24 = Moment coefficient, k Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

25 = Non-sway moment factor

Value >= 0; 0 means use program determined value.

26 = Sway moment factor, Psi Major

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, Psi Minor

Value >= 0; 0 means use program determined value.

28 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

29 = Compressive capacity, Nc.Rd

Value >= 0; 0 means use program determined value. [F]

30 = Tensile capacity, Nt.Rd

Value >= 0; 0 means use program determined value. [F]

31 = Major bending capacity, Mc3.Rd

Value >= 0; 0 means use program determined value. [FL]

32 = Minor bending capacity, Mc2.Rd

Value >= 0; 0 means use program determined value. [FL]

33 = Buckling resistance moment, Mb.Rd

Value >= 0; 0 means use program determined value. [FL]

34 = Major shear capacity, Vn2.Rd

Value >= 0; 0 means use program determined value. [F]

35 = Minor shear capacity, Vn3.RD

Value >= 0; 0 means use program determined value. [F]

36 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects= 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemEUROCODE\_3\_1993()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("EUROCODE 3-1993")

   'set overwrite item
      ret = SapModel.DesignSteel.EUROCODE\_3\_1993.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_Eurocode_3-1993}.htm)



## SetPreference {Steel Eurocode 3-1993}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Eurocode_3-1993/SetPreference_{Steel_Eurocode_3-1993}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.EUROCODE\_3\_1993.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 12, inclusive, indicating the preference item considered.

1 = Framing type

2 = GammaM0

3 = GammeM1

4 = Consider deflection

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total deflection limit, L/Value

9 = Total camber limit, L/Value

10 = Pattern live load factor

11 = Demand/capacity ratio limit

12 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Moment Frame

2 = Braced Frame

2 = GammaM0

Value > 0

3 = GammeM1

Value > 0

4 = Consider deflection

0 = No

Any other value = Yes

5 = DL deflection limit, L/Value

Value > 0

6 = SDL + LL deflection limit, L/Value

Value > 0

7 = LL deflection limit, L/Value

Value > 0

8 = Total deflection limit, L/Value

Value > 0

9 = Total camber limit, L/Value

Value > 0

10 = Pattern live load factor

Value >= 0

11 = Demand/capacity ratio limit

Value > 0

12 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemEUROCODE\_3\_1993()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("EUROCODE 3-1993")

   'set preference item
      ret = SapModel.DesignSteel.EUROCODE\_3\_1993.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_Eurocode_3-1993}.htm)



## GetCode {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetCode_{Steel}.htm`*

# GetCode

## Syntax

SapObject.SapModel.DesignSteel.GetCode

## VB6 Procedure

Function GetCode(ByRef CodeName As String) As Long

## Parameters

CodeName

This is one of the following steel design code names.

AASHTO LRFD 2007

AISC-ASD89

AISC 360-10

AISC360-05/IBC2006

AISC-LRFD93

API RP2A-LRFD 97

API RP2A-WSD2000

API RP2A-WSD2014

AS 4100-1998
ASCE 10-97

BS5950 2000

Chinese 2010
CSA S16-19
CSA S16-14
CSA-S16-09

EN 1993-1-1:2005 (formerly EUROCODE 3-2005)

Indian IS 800-2007

Italian NTC 2008

Italian UNI 10011

KBC 2009

Norsok N-004 2013

NZS 3404-1997

SP 16.13330.2011

## Remarks

This function retrieves the steel design code.

The function returns zero if the code is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignCode()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim CodeName As String

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

   'get steel design code
      ret = SapModel.DesignSteel.GetCode(CodeName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Modified list of codes contained in the CodeName Parameter in version 15.0.1.

Added Norsok N-004 2013 in version 16.1.0.

Updated list of code names in version 17.3.0.

Removed older codes which have been removed from the program in v18.0.0.

Updated list of available codes in v19.1.0.

## See Also

[SetCode](SetCode_{Steel}.htm)



## GetComboAutoGenerate {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetComboAutoGenerate_{Steel}.htm`*

# GetComboAutoGenerate

## Syntax

SapObject.SapModel.DesignSteel.GetComboAutoGenerate

## VB6 Procedure

Function GetComboAutoGenerate(ByRef AutoGenerate As Boolean) As Long

## Parameters

AutoGenerate

If this item is True, the option to automatically generate code-based design load combinations for steel frame design is turned on. If it is False, the option is turned off.

## Remarks

This function retrieves the value of the automatically generated code-based design load combinations option for steel frame design.

The function returns zero if the options are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignComboAutoGenerate()
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
      ret = SapModel.DesignSteel.GetComboAutoGenerate(AutoGenerate)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 18.1.0.

## See Also

[SetComboAutoGenerate](SetComboAutoGenerate{Steel}.htm)



## GetComboDeflection {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetComboDeflection_{Steel}.htm`*

# GetComboDeflection

## Syntax

SapObject.SapModel.DesignSteel.GetComboDeflection

## VB6 Procedure

Function GetComboDeflection(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of load combinations selected as design combinations for steel deflection design.

MyName

This is an array that includes the name of each response combination selected as a design combination for steel deflection design.

## Remarks

This function retrieves the names of all load combinations selected as design combinations for steel deflection design.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignComboDeflection()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default steel design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(True, False, False, False)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName2)

   'select combos for steel deflection design
      For i = 0 To NumberNames - 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignSteel.SetComboDeflection(MyName2(i), Selected)
      Next i

   'get combos selected for steel deflection design
      ret = SapModel.DesignSteel.GetComboDeflection(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetComboDeflection](SetComboDeflection_{Steel}.htm)



## GetComboStrength {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetComboStrength_{Steel}.htm`*

# GetComboStrength

## Syntax

SapObject.SapModel.DesignSteel.GetComboStrength

## VB6 Procedure

Function GetComboStrength(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of load combinations selected as design combinations for steel strength design.

MyName

This is an array that includes the name of each response combination selected as a design combination for steel strength design.

## Remarks

This function retrieves the names of all load combinations selected as design combinations for steel strength design.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignComboStrength()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default steel design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(True, False, False, False)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName2)

   'select combos for steel strength design
      For i = 0 To NumberNames - 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignSteel.SetComboStrength(MyName2(i), Selected)
      Next i

   'get combos selected for steel strength design
      ret = SapModel.DesignSteel.GetComboStrength(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetComboStrength](SetComboStrength_{Steel}.htm)



## GetDesignSection {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetDesignSection_{Steel}.htm`*

# GetDesignSection

## Syntax

SapObject.SapModel.DesignSteel.GetDesignSection

## VB6 Procedure

Function GetDesignSection(ByVal Name As String, ByRef PropName As String) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

PropName

The name of the design section for the specified frame object.

## Remarks

This function retrieves the design section for a specified steel frame object.

The function returns zero if the section is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignSection()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyName() As String
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

   'import new frame section properties
      ret = SapModel.PropFrame.ImportProp("W18X35", "A992Fy50", "AISC16.XML", "W18X35")
      ret = SapModel.PropFrame.ImportProp("W18X40", "A992Fy50", "AISC16.XML", "W18X40")
      ret = SapModel.PropFrame.ImportProp("W18X46", "A992Fy50", "AISC16.XML", "W18X46")

   'define new auto select list frame section property
      ReDim MyName(2)
      MyName(0) = "W18X35"
      MyName(1) = "W18X40"
      MyName(2) = "W18X46"
      ret = SapModel.PropFrame.SetAutoSelectSteel("AUTO1", 3, MyName)

   'set frame section properties
      ret = SapModel.FrameObj.SetSection("8", "AUTO1")
      ret = SapModel.FrameObj.SetSection("10", "AUTO1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get design section
      ret = SapModel.DesignSteel.GetDesignSection("8", PropName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetDesignSection](SetDesignSection_{Steel}.htm)



## GetDetailResultsText

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetDetailResultsText.htm`*

# GetDetailResultsText

## **Syntax**

SapObject.SapModel.DesignSteel.GetDetailResultsText

## **VB6 Procedure**

Public Function GetDetailResultsText(ByVal Name As String, ByVal ItemType As eItemType, ByVal Table As Long, ByVal Field As String, ByRef NumberItems As Long, FrameName() As String, Text() As String) As Long

## **Parameters**

**Name**

The name of an existing frame object or group, depending on the value of the ItemType item.

**ItemType**

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the design results are retrieved for the frame object specified by the Name item.

If this item is Group, the design results are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the design results are retrieved for all selected frame objects, and the Name item is ignored.

**Table**

The table ID of the steel design output database Tables. The table names are input as the representative table numbers and are code-based. Please see the following appendix.

**Field**

The field name with TEXT output data type in the specified steel design result database Tables. The Field Names need to be the exactly same as the names in the specified steel design output database tables except the case is insensitive.

**NumberItems**

The number of frame objects for which results are obtained.

**FrameName**

The frame object names for which results are obtained.

**Text**

The design results with TEXT output data type of the request field in the request table for the specified frame objects.

## **Remarks**

This function retrieves the design results from steel design output database tables. Note that the summary table of all design codes is not included in this function.

The function returns zero if the results are successfully retrieved; otherwise it returns a nonzero value.

## **VBA Example**

Sub GetSteelDesignDetailResultsText ()

'dimension variables

Dim SapObject as cOAPI

Dim SapModel As cSapModelDim ret As Long

Dim NumberItems As Long

Dim FrameName() As String

Dim Text() As String

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

'run analysis

ret = SapModel.File.Save("C:\SapAPI\x.sdb")

ret = SapModel.Analyze.RunAnalysis

'start steel design

ret = SapModel.DesignSteel.SetCode("AISC360-05/IBC2006")

ret = SapModel.DesignSteel.StartDesign

'get summary result data

ret = SapModel.DesignSteel. GetDetailResultsText("8", 0, 2, "DesignSect", NumberItems, FrameName(), Text())

'close Sap2000SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## **Release Notes**

Initial release in version 16.0.0.

## **See Also**

[GetDetailResultsValue](GetDetailResultsValue.htm)

## **Appendix – The available table index for selected design codes**

"AISC360-05/IBC2006"

  2:  "Steel Design 2 - PMM Details - AISC360-05-IBC2006"

  3:  "Steel Design 3 - Shear Details - AISC360-05-IBC2006"

  4:  "Steel Design 4 - Continuity Plates - AISC360-05-IBC2006"

  5:  "Steel Design 5 - Doubler Plates - AISC360-05-IBC2006"

  6:  "Steel Design 6 - Beam/Column Ratios - AISC360-05-IBC2006"

  7:  "Steel Design 7 - Beam Shear Forces - AISC360-05-IBC2006"

  8:  "Steel Design 8 - Brace Max Axial Load - AISC360-05-IBC2006"

  9:  "Steel Design 9 - Decision Parameters - AISC360-05-IBC2006"

"AISC-ASD89"

  2:  "Steel Design 2 - PMM Details - AISC-ASD89"

  3:  "Steel Design 3 - Shear Details - AISC-ASD89"

  4:  "Steel Design 4 - Continuity Plates - AISC-ASD89"

  5:  "Steel Design 5 - Doubler Plates - AISC-ASD89"

  6:  "Steel Design 6 - Beam/Column Ratios - AISC-ASD89"

  7:  "Steel Design 7 - Beam Shear Forces - AISC-ASD89"

  8:  "Steel Design 8 - Brace Max Axial Load - AISC-ASD89"

"AISC-ASD01"

  2:  "Steel Design 2 - PMM Details - AISC-ASD01"

  3:  "Steel Design 3 - Shear Details - AISC-ASD01"

  4:  "Steel Design 4 - Continuity Plates - AISC-ASD01"

  5:  "Steel Design 5 - Doubler Plates - AISC-ASD01"

  6:  "Steel Design 6 - Beam/Column Ratios - AISC-ASD01"

  7:  "Steel Design 7 - Beam Shear Forces - AISC-ASD01"

  8:  "Steel Design 8 - Brace Max Axial Load - AISC-ASD01"

"AISC-LRFD99"

  2:  "Steel Design 2 - PMM Details - AISC-LRFD99"

  3:  "Steel Design 3 - Shear Details - AISC-LRFD99"

  4:  "Steel Design 4 - Continuity Plates - AISC-LRFD99"

  5:  "Steel Design 5 - Doubler Plates - AISC-LRFD99"

  6:  "Steel Design 6 - Beam/Column Ratios - AISC-LRFD99"

  7:  "Steel Design 7 - Beam Shear Forces - AISC-LRFD99"

  8:  "Steel Design 8 - Brace Max Axial Load - AISC-LRFD99"

"AISC-LRFD93"

  2:  "Steel Design 2 - PMM Details - AISC-LRFD93"

  3:  "Steel Design 3 - Shear Details - AISC-LRFD93"

  4:  "Steel Design 4 - Continuity Plates - AISC-LRFD93"

  5:  "Steel Design 5 - Doubler Plates - AISC-LRFD93"

  6:  "Steel Design 6 - Beam/Column Ratios - AISC-LRFD93"

  7:  "Steel Design 7 - Beam Shear Forces - AISC-LRFD93"

  8:  "Steel Design 8 - Brace Max Axial Load - AISC-LRFD93"

"AASHTO LRFD 2007"

  2:  "Steel Design 2 - PMM Details - AASHTO-LRFD-2007"

  3:  "Steel Design 3 - Shear Details - AASHTO-LRFD-2007"

  4:  "Steel Design 4 - Continuity Plates - AASHTO-LRFD-2007"

  5:  "Steel Design 5 - Doubler Plates - AASHTO-LRFD-2007"

  6:  "Steel Design 6 - Beam/Column Ratios - AASHTO-LRFD-2007"

  7:  "Steel Design 7 - Beam Shear Forces - AASHTO-LRFD-2007"

  8:  "Steel Design 8 - Brace Max Axial Load - AASHTO-LRFD-2007"

"API RP2A-LRFD 97"

  2:  "Steel Design 2 - PMM Details - API RP2A-LRFD 97"

  3:  "Steel Design 2 - PMM Details for Pipes - API RP2A-LRFD 97"

  4:  "Steel Design 3 - Shear Details - API RP2A-LRFD 97"

  5:  "Steel Design 4 - Continuity Plates - API RP2A-LRFD 97"

  6:  "Steel Design 5 - Doubler Plates - API RP2A-LRFD 97"

  7:  "Steel Design 6 - Beam/Column Ratios - API RP2A-LRFD 97"

  8:  "Steel Design 7 - Beam Shear Forces - API RP2A-LRFD 97"

  9:  "Steel Design 8 - Brace Max Axial Load - API RP2A-LRFD 97"

"API RP2A-WSD2000"

  2:  "Steel Design 2 - PMM Details - API RP2A-WSD2000"

  3:  "Steel Design 2 - PMM Details for Pipes - API RP2A-WSD2000"

  4:  "Steel Design 3 - Shear Details - API RP2A-WSD2000"

  5:  "Steel Design 4 - Continuity Plates - API RP2A-WSD2000"

  6:  "Steel Design 5 - Doubler Plates - API RP2A-WSD2000"

  7:  "Steel Design 6 - Beam/Column Ratios - API RP2A-WSD2000"

  8:  "Steel Design 7 - Beam Shear Forces - API RP2A-WSD2000"

  9:  "Steel Design 8 - Brace Max Axial Load - API RP2A-WSD2000"

"AS 4100-1998"

  2:  "Steel Design 2 - PMM Details - AS 4100-1998"

  3:  "Steel Design 3 - Shear Details - AS 4100-1998"

  4:  "Steel Design 4 - Continuity Plates - AS 4100-1998"

  5:  "Steel Design 5 - Doubler Plates - AS 4100-1998"

  6:  "Steel Design 6 - Beam/Column Ratios - AS 4100-1998"

  7:  "Steel Design 7 - Beam Shear Forces - AS 4100-1998"

  8:  "Steel Design 8 - Brace Max Axial Load - AS 4100-1998"

"ASCE 10-97"

  2:  "Steel Design 2 - PMM Details - ASCE 10-97"

  3:  "Steel Design 2 - PMM Details for Angles - ASCE 10-97"

  4:  "Steel Design 3 - Shear Details - ASCE 10-97"

  5:  "Steel Design 3 - Shear Details for Angles - ASCE 10-97"

  6:  "Steel Design 4 - Continuity Plates - ASCE 10-97"

  7:  "Steel Design 5 - Doubler Plates - ASCE 10-97"

  8:  "Steel Design 6 - Beam/Column Ratios - ASCE 10-97"

  9:  "Steel Design 7 - Beam Shear Forces - ASCE 10-97"

  10: "Steel Design 8 - Brace Max Axial Load - ASCE 10-97"

"EUROCODE 3-1993"

  2:  "Steel Design 2 - PMM Details - EUROCODE 3-1993"

  3:  "Steel Design 3 - Shear Details - EUROCODE 3-1993"

  4:  "Steel Design 4 - Continuity Plates - EUROCODE 3-1993"

  5:  "Steel Design 5 - Doubler Plates - EUROCODE 3-1993"

  6:  "Steel Design 6 - Beam/Column Ratios - EUROCODE 3-1993"

  7:  "Steel Design 7 - Beam Shear Forces - EUROCODE 3-1993"

  8:  "Steel Design 8 - Brace Max Axial Load - EUROCODE 3-1993"

"Eurocode 3-2005"

  2:  "Steel Design 2 - PMM Details - Eurocode 3-2005"

  3:  "Steel Design 3 - Shear Details - Eurocode 3-2005"

  4:  "Steel Design 4 - Continuity Plates - Eurocode 3-2005"

  5:  "Steel Design 5 - Doubler Plates - Eurocode 3-2005"

  6:  "Steel Design 6 - Beam/Column Ratios - Eurocode 3-2005"

  7:  "Steel Design 7 - Beam Shear Forces - Eurocode 3-2005"

  8:  "Steel Design 8 - Brace Max Axial Load - Eurocode 3-2005"

"Indian IS 800:2007"

  2:  "Steel Design 2 - PMM Details - Indian IS 800:2007"

  3:  "Steel Design 3 - Shear Details - Indian IS 800:2007"

  4:  "Steel Design 4 - Continuity Plates - Indian IS 800:2007"

  5:  "Steel Design 5 - Doubler Plates - Indian IS 800:2007"

  6:  "Steel Design 6 - Beam/Column Ratios - Indian IS 800:2007"

  7:  "Steel Design 7 - Beam Shear Forces - Indian IS 800:2007"

  8:  "Steel Design 8 - Brace Max Axial Load - Indian IS 800:2007"

"Italian UNI 10011"

  2:  "Steel Design 2 - PMM Details - Italian UNI 10011"

  3:  "Steel Design 3 - Shear Details - Italian UNI 10011"

  4:  "Steel Design 4 - Continuity Plates - Italian UNI 10011"

  5:  "Steel Design 5 - Doubler Plates - Italian UNI 10011"

  6:  "Steel Design 6 - Beam/Column Ratios - Italian UNI 10011"

  7:  "Steel Design 7 - Beam Shear Forces - Italian UNI 10011"

  8:  "Steel Design 8 - Brace Max Axial Load - Italian UNI 10011"

"NZS 3404-1997"

  2:  "Steel Design 2 - PMM Details - NZS 3404-1997"

  3:  "Steel Design 3 - Shear Details - NZS 3404-1997"

  4:  "Steel Design 4 - Continuity Plates - NZS 3404-1997"

  5:  "Steel Design 5 - Doubler Plates - NZS 3404-1997"

  6:  "Steel Design 6 - Beam/Column Ratios - NZS 3404-1997"

  7:  "Steel Design 7 - Beam Shear Forces - NZS 3404-1997"

  8:  "Steel Design 8 - Brace Max Axial Load - NZS 3404-1997"

"Norsok N-004"

  2:  "Steel Design 2 - PMM Details - Norsok N-004"

  3:  "Steel Design 2 - PMM Details for Pipes - Norsok N-004"

  4:  "Steel Design 3 - Shear Details - Norsok N-004"

  5:  "Steel Design 4 - Continuity Plates - Norsok N-004"

  6:  "Steel Design 5 - Doubler Plates - Norsok N-004"

  7:  "Steel Design 6 - Beam/Column Ratios - Norsok N-004"

  8:  "Steel Design 7 - Beam Shear Forces - Norsok N-004"

  9:  "Steel Design 8 - Brace Max Axial Load - Norsok N-004"

"UBC97-ASD"

  2:  "Steel Design 2 - PMM Details - UBC97-ASD"

  3:  "Steel Design 3 - Shear Details - UBC97-ASD"

  4:  "Steel Design 4 - Continuity Plates - UBC97-ASD"

  5:  "Steel Design 5 - Doubler Plates - UBC97-ASD"

  6:  "Steel Design 6 - Beam/Column Ratios - UBC97-ASD"

  7:  "Steel Design 7 - Beam Shear Forces - UBC97-ASD"

  8:  "Steel Design 8 - Brace Max Axial Load - UBC97-ASD"

"UBC97-LRFD"

  2:  "Steel Design 2 - PMM Details - UBC97-LRFD"

  3:  "Steel Design 3 - Shear Details - UBC97-LRFD"

  4:  "Steel Design 4 - Continuity Plates - UBC97-LRFD"

  5:  "Steel Design 5 - Doubler Plates - UBC97-LRFD"

  6:  "Steel Design 6 - Beam/Column Ratios - UBC97-LRFD"

  7:  "Steel Design 7 - Beam Shear Forces - UBC97-LRFD"

  8:  "Steel Design 8 - Brace Max Axial Load - UBC97-LRFD"



## GetDetailResultsValue

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetDetailResultsValue.htm`*

# **GetDetailResultsValue**

## **Syntax**

SapObject.SapModel.DesignSteel.GetDetailResultsValue

## **VB6 Procedure**

Public Function GetDetailResultsValue(ByVal Name As String, ByVal ItemType As eItemType, ByVal Table As Long, ByVal Field As String, ByRef NumberItems As Long, FrameName() As String, Text() As String) As Long

## **Parameters**

**Name**

The name of an existing frame object or group, depending on the value of the ItemType item.

**ItemType**

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the design results are retrieved for the frame object specified by the Name item.

If this item is Group, the design results are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, the design results are retrieved for all selected frame objects, and the Name item is ignored.

**Table**

The table ID of the steel design output database Tables. The table names are input as the representative table numbers and are code-based. Please see the following appendix.

**Field**

The field name with Numerical output data type in the specified steel design result database Tables. The Field Names need to be the exactly same as the names in the specified steel design output database tables except the case is insensitive.

**NumberItems**

The number of frame objects for which results are obtained.

**FrameName**

The frame object names for which results are obtained.

**Value**

The design results with Numerical output data type of the request field in the request table for the specified frame objects.

## **Remarks**

This function retrieves the design results from steel design output database tables. Note that the summary table of all design codes is not included in this function.

The function returns zero if the results are successfully retrieved; otherwise it returns a nonzero value.

## **VBA Example**

Sub GetSteelDesignDetailResultsValue ()
'dimension variables

Dim SapObject As Sap2000v16.SapObject

Dim SapModel As cSapModel

Dim ret As Long

Dim NumberItems As Long

Dim FrameName() As String

Dim Text() As String

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

'run analysis

ret = SapModel.File.Save("C:\SapAPI\x.sdb")

ret = SapModel.Analyze.RunAnalysis

'start steel design

ret = SapModel.DesignSteel.SetCode("AISC360-05/IBC2006")

ret = SapModel.DesignSteel.StartDesign

'get summary result data

ret = SapModel.DesignSteel. GetDetailResultsValue("8", 0, 2, "Pr", NumberItems, FrameName(), Value())

'close Sap2000

SapObject.ApplicationExit False

Set SapModel = Nothing

Set SapObject = Nothing

End Sub

## **Release Notes**

Initial release in version 16.0.0.

## **See Also**

[GetDetailResultsText](GetDetailResultsText.htm)

## **Appendix – The available table index for selected design codes**

"AISC360-05/IBC2006"

  2:  "Steel Design 2 - PMM Details - AISC360-05-IBC2006"

  3:  "Steel Design 3 - Shear Details - AISC360-05-IBC2006"

  4:  "Steel Design 4 - Continuity Plates - AISC360-05-IBC2006"

  5:  "Steel Design 5 - Doubler Plates - AISC360-05-IBC2006"

  6:  "Steel Design 6 - Beam/Column Ratios - AISC360-05-IBC2006"

  7:  "Steel Design 7 - Beam Shear Forces - AISC360-05-IBC2006"

  8:  "Steel Design 8 - Brace Max Axial Load - AISC360-05-IBC2006"

  9:  "Steel Design 9 - Decision Parameters - AISC360-05-IBC2006"

"AISC-ASD89"

  2:  "Steel Design 2 - PMM Details - AISC-ASD89"

  3:  "Steel Design 3 - Shear Details - AISC-ASD89"

  4:  "Steel Design 4 - Continuity Plates - AISC-ASD89"

  5:  "Steel Design 5 - Doubler Plates - AISC-ASD89"

  6:  "Steel Design 6 - Beam/Column Ratios - AISC-ASD89"

  7:  "Steel Design 7 - Beam Shear Forces - AISC-ASD89"

  8:  "Steel Design 8 - Brace Max Axial Load - AISC-ASD89"

"AISC-ASD01"

  2:  "Steel Design 2 - PMM Details - AISC-ASD01"

  3:  "Steel Design 3 - Shear Details - AISC-ASD01"

  4:  "Steel Design 4 - Continuity Plates - AISC-ASD01"

  5:  "Steel Design 5 - Doubler Plates - AISC-ASD01"

  6:  "Steel Design 6 - Beam/Column Ratios - AISC-ASD01"

  7:  "Steel Design 7 - Beam Shear Forces - AISC-ASD01"

  8:  "Steel Design 8 - Brace Max Axial Load - AISC-ASD01"

"AISC-LRFD99"

  2:  "Steel Design 2 - PMM Details - AISC-LRFD99"

  3:  "Steel Design 3 - Shear Details - AISC-LRFD99"

  4:  "Steel Design 4 - Continuity Plates - AISC-LRFD99"

  5:  "Steel Design 5 - Doubler Plates - AISC-LRFD99"

  6:  "Steel Design 6 - Beam/Column Ratios - AISC-LRFD99"

  7:  "Steel Design 7 - Beam Shear Forces - AISC-LRFD99"

  8:  "Steel Design 8 - Brace Max Axial Load - AISC-LRFD99"

"AISC-LRFD93"

  2:  "Steel Design 2 - PMM Details - AISC-LRFD93"

  3:  "Steel Design 3 - Shear Details - AISC-LRFD93"

  4:  "Steel Design 4 - Continuity Plates - AISC-LRFD93"

  5:  "Steel Design 5 - Doubler Plates - AISC-LRFD93"

  6:  "Steel Design 6 - Beam/Column Ratios - AISC-LRFD93"

  7:  "Steel Design 7 - Beam Shear Forces - AISC-LRFD93"

  8:  "Steel Design 8 - Brace Max Axial Load - AISC-LRFD93"

"AASHTO LRFD 2007"

  2:  "Steel Design 2 - PMM Details - AASHTO-LRFD-2007"

  3:  "Steel Design 3 - Shear Details - AASHTO-LRFD-2007"

  4:  "Steel Design 4 - Continuity Plates - AASHTO-LRFD-2007"

  5:  "Steel Design 5 - Doubler Plates - AASHTO-LRFD-2007"

  6:  "Steel Design 6 - Beam/Column Ratios - AASHTO-LRFD-2007"

  7:  "Steel Design 7 - Beam Shear Forces - AASHTO-LRFD-2007"

  8:  "Steel Design 8 - Brace Max Axial Load - AASHTO-LRFD-2007"

"API RP2A-LRFD 97"

  2:  "Steel Design 2 - PMM Details - API RP2A-LRFD 97"

  3:  "Steel Design 2 - PMM Details for Pipes - API RP2A-LRFD 97"

  4:  "Steel Design 3 - Shear Details - API RP2A-LRFD 97"

  5:  "Steel Design 4 - Continuity Plates - API RP2A-LRFD 97"

  6:  "Steel Design 5 - Doubler Plates - API RP2A-LRFD 97"

  7:  "Steel Design 6 - Beam/Column Ratios - API RP2A-LRFD 97"

  8:  "Steel Design 7 - Beam Shear Forces - API RP2A-LRFD 97"

  9:  "Steel Design 8 - Brace Max Axial Load - API RP2A-LRFD 97"

"API RP2A-WSD2000"

  2:  "Steel Design 2 - PMM Details - API RP2A-WSD2000"

  3:  "Steel Design 2 - PMM Details for Pipes - API RP2A-WSD2000"

  4:  "Steel Design 3 - Shear Details - API RP2A-WSD2000"

  5:  "Steel Design 4 - Continuity Plates - API RP2A-WSD2000"

  6:  "Steel Design 5 - Doubler Plates - API RP2A-WSD2000"

  7:  "Steel Design 6 - Beam/Column Ratios - API RP2A-WSD2000"

  8:  "Steel Design 7 - Beam Shear Forces - API RP2A-WSD2000"

  9:  "Steel Design 8 - Brace Max Axial Load - API RP2A-WSD2000"

"AS 4100-1998"

  2:  "Steel Design 2 - PMM Details - AS 4100-1998"

  3:  "Steel Design 3 - Shear Details - AS 4100-1998"

  4:  "Steel Design 4 - Continuity Plates - AS 4100-1998"

  5:  "Steel Design 5 - Doubler Plates - AS 4100-1998"

  6:  "Steel Design 6 - Beam/Column Ratios - AS 4100-1998"

  7:  "Steel Design 7 - Beam Shear Forces - AS 4100-1998"

  8:  "Steel Design 8 - Brace Max Axial Load - AS 4100-1998"

"ASCE 10-97"

  2:  "Steel Design 2 - PMM Details - ASCE 10-97"

  3:  "Steel Design 2 - PMM Details for Angles - ASCE 10-97"

  4:  "Steel Design 3 - Shear Details - ASCE 10-97"

  5:  "Steel Design 3 - Shear Details for Angles - ASCE 10-97"

  6:  "Steel Design 4 - Continuity Plates - ASCE 10-97"

  7:  "Steel Design 5 - Doubler Plates - ASCE 10-97"

  8:  "Steel Design 6 - Beam/Column Ratios - ASCE 10-97"

  9:  "Steel Design 7 - Beam Shear Forces - ASCE 10-97"

  10: "Steel Design 8 - Brace Max Axial Load - ASCE 10-97"

"EUROCODE 3-1993"

  2:  "Steel Design 2 - PMM Details - EUROCODE 3-1993"

  3:  "Steel Design 3 - Shear Details - EUROCODE 3-1993"

  4:  "Steel Design 4 - Continuity Plates - EUROCODE 3-1993"

  5:  "Steel Design 5 - Doubler Plates - EUROCODE 3-1993"

  6:  "Steel Design 6 - Beam/Column Ratios - EUROCODE 3-1993"

  7:  "Steel Design 7 - Beam Shear Forces - EUROCODE 3-1993"

  8:  "Steel Design 8 - Brace Max Axial Load - EUROCODE 3-1993"

"Eurocode 3-2005"

  2:  "Steel Design 2 - PMM Details - Eurocode 3-2005"

  3:  "Steel Design 3 - Shear Details - Eurocode 3-2005"

  4:  "Steel Design 4 - Continuity Plates - Eurocode 3-2005"

  5:  "Steel Design 5 - Doubler Plates - Eurocode 3-2005"

  6:  "Steel Design 6 - Beam/Column Ratios - Eurocode 3-2005"

  7:  "Steel Design 7 - Beam Shear Forces - Eurocode 3-2005"

  8:  "Steel Design 8 - Brace Max Axial Load - Eurocode 3-2005"

"Indian IS 800:2007"

  2:  "Steel Design 2 - PMM Details - Indian IS 800:2007"

  3:  "Steel Design 3 - Shear Details - Indian IS 800:2007"

  4:  "Steel Design 4 - Continuity Plates - Indian IS 800:2007"

  5:  "Steel Design 5 - Doubler Plates - Indian IS 800:2007"

  6:  "Steel Design 6 - Beam/Column Ratios - Indian IS 800:2007"

  7:  "Steel Design 7 - Beam Shear Forces - Indian IS 800:2007"

  8:  "Steel Design 8 - Brace Max Axial Load - Indian IS 800:2007"

"Italian UNI 10011"

  2:  "Steel Design 2 - PMM Details - Italian UNI 10011"

  3:  "Steel Design 3 - Shear Details - Italian UNI 10011"

  4:  "Steel Design 4 - Continuity Plates - Italian UNI 10011"

  5:  "Steel Design 5 - Doubler Plates - Italian UNI 10011"

  6:  "Steel Design 6 - Beam/Column Ratios - Italian UNI 10011"

  7:  "Steel Design 7 - Beam Shear Forces - Italian UNI 10011"

  8:  "Steel Design 8 - Brace Max Axial Load - Italian UNI 10011"

"NZS 3404-1997"

  2:  "Steel Design 2 - PMM Details - NZS 3404-1997"

  3:  "Steel Design 3 - Shear Details - NZS 3404-1997"

  4:  "Steel Design 4 - Continuity Plates - NZS 3404-1997"

  5:  "Steel Design 5 - Doubler Plates - NZS 3404-1997"

  6:  "Steel Design 6 - Beam/Column Ratios - NZS 3404-1997"

  7:  "Steel Design 7 - Beam Shear Forces - NZS 3404-1997"

  8:  "Steel Design 8 - Brace Max Axial Load - NZS 3404-1997"

"Norsok N-004"

  2:  "Steel Design 2 - PMM Details - Norsok N-004"

  3:  "Steel Design 2 - PMM Details for Pipes - Norsok N-004"

  4:  "Steel Design 3 - Shear Details - Norsok N-004"

  5:  "Steel Design 4 - Continuity Plates - Norsok N-004"

  6:  "Steel Design 5 - Doubler Plates - Norsok N-004"

  7:  "Steel Design 6 - Beam/Column Ratios - Norsok N-004"

  8:  "Steel Design 7 - Beam Shear Forces - Norsok N-004"

  9:  "Steel Design 8 - Brace Max Axial Load - Norsok N-004"

"UBC97-ASD"

  2:  "Steel Design 2 - PMM Details - UBC97-ASD"

  3:  "Steel Design 3 - Shear Details - UBC97-ASD"

  4:  "Steel Design 4 - Continuity Plates - UBC97-ASD"

  5:  "Steel Design 5 - Doubler Plates - UBC97-ASD"

  6:  "Steel Design 6 - Beam/Column Ratios - UBC97-ASD"

  7:  "Steel Design 7 - Beam Shear Forces - UBC97-ASD"

  8:  "Steel Design 8 - Brace Max Axial Load - UBC97-ASD"

"UBC97-LRFD"

  2:  "Steel Design 2 - PMM Details - UBC97-LRFD"

  3:  "Steel Design 3 - Shear Details - UBC97-LRFD"

  4:  "Steel Design 4 - Continuity Plates - UBC97-LRFD"

  5:  "Steel Design 5 - Doubler Plates - UBC97-LRFD"

  6:  "Steel Design 6 - Beam/Column Ratios - UBC97-LRFD"

  7:  "Steel Design 7 - Beam Shear Forces - UBC97-LRFD"

  8:  "Steel Design 8 - Brace Max Axial Load - UBC97-LRFD"



## GetGroup {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetGroup_{Steel}.htm`*

# GetGroup

## Syntax

SapObject.SapModel.DesignSteel.GetGroup

## VB6 Procedure

Function GetGroup(ByRef NumberItems As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of groups selected for steel design.

MyName

This is an array that includes the name of each group selected for steel design.

## Remarks

This function retrieves the names of all groups selected for steel design.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignGroup()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'select group for steel design
      ret = SapModel.DesignSteel.SetGroup("ALL", True)

   'get groups selected for steel design
      ret = SapModel.DesignSteel.GetGroup(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetGroup](SetGroup_{Steel}.htm)



## GetResultsAvailable {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetResultsAvailable_{Steel}.htm`*

# GetResultsAvailable {Steel}

## Syntax

SapObject.SapModel.DesignSteel.GetResultsAvailable

## VB6 Procedure

Function GetResultsAvailable() As Boolean

## Parameters

None

## Remarks

The function returns True if the steel frame design results are available, otherwise False.

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

  'create model from template

    ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

  'run analysis

    ret = SapModel.File.Save("C:\SapAPI\x.sdb")

    ret = SapModel.Analyze.RunAnalysis

  'start steel design

    ret = SapModel.DesignSteel.StartDesign

  'check if design results are available

    ResultsAvailable = SapModel.DesignSteel.GetResultsAvailable

  'close Sap2000

    SapObject.ApplicationExit.False

    Set SapModel = Nothing

    Set SapObject = Nothing

End Sub

## Release Notes

Initial release in version 18.2.0.



## GetSummaryResults {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetSummaryResults_{Steel}.htm`*

# GetSummaryResults

## Syntax

SapObject.SapModel.DesignSteel.GetSummaryResults

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

This is an array that includes 1, 2, 3, 4, 5 or 6, indicating the controlling stress or capacity ratio type for each frame object.

1 = PMM

2 = Major shear

3 = Minor shear

4 = Major beam-column capacity ratio

5 = Minor beam-column capacity ratio

6 = Other

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

This function retrieves summary results for steel design.

The function returns zero if the results are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignSummaryResults()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get summary result data
      ret = SapModel.DesignSteel.GetSummaryResults("8", NumberItems, FrameName, Ratio, RatioType, Location, ComboName, ErrorSummary, WarningSummary)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## GetTargetDispl

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetTargetDispl.htm`*

# GetTargetDispl

## Syntax

SapObject.SapModel.DesignSteel.GetTargetDispl

## VB6 Procedure

Function GetTargetDispl(ByRef NumberItems As Long, ByRef LoadCase() As String, ByRef Point() As String, ByRef Displ() As Double, ByRef Active As Boolean) As Long

## Parameters

NumberItems

The number of lateral displacement targets specified.

LoadCase

This is an array that includes the name of the static linear load case associated with each lateral displacement target.

Point

This is an array that includes the name of the point object associated to which the lateral displacement target applies.

Displ

This is an array that includes the lateral displacement target. [L]

Active

If this item is True, all specified lateral displacement targets are active. If it is False, they are inactive.

## Remarks

This function retrieves lateral displacement targets for steel design.

The function returns zero if the targets are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignTargetDispl()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyLCase() As String
      Dim MyPoint() As String
      Dim MyDispl() As Double
      Dim NumberItems As Long
      Dim LoadCase() As String
      Dim Point() As String
      Dim Displ() As Double
      Dim Active As Boolean

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
      ret = SapModel.LoadPatterns.Add("EQX", LTYPE\_QUAKE)

   'assign UBC97 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetUBC97("EQX", 1, 0.05, 1, 0.035, 0, False, 0, 0, 1, 3, 0.4, 0, 0, 1, 3, 5, 0, 0, 1.15, 6)

   'set target displacement data
      ReDim MyLCase(0)
      ReDim MyPoint(0)
      ReDim MyDispl(0)
      MyLCase(0) = "EQX"
      MyPoint(0) = "3"
      MyDispl(0) = 0.4
      ret = SapModel.DesignSteel.SetTargetDispl(1, MyLCase, MyPoint, MyDispl)

   'get target displacement data
      ret = SapModel.DesignSteel.GetTargetDispl(NumberItems, LoadCase, Point, Displ, Active)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetTargetDispl](SetTargetDispl.htm)



## GetTargetPeriod

*Source file: `SAP2000_API_Fuctions/Design/Steel/GetTargetPeriod.htm`*

# GetTargetPeriod

## Syntax

SapObject.SapModel.DesignSteel.GetTargetPeriod

## VB6 Procedure

Function GetTargetPeriod(ByRef NumberItems As Long, ByRef ModalCase As String, ByRef Mode() As Long, ByRef Period() As Double, ByRef Active As Boolean) As Long

## Parameters

NumberItems

The number of lateral displacement targets specified.

ModalCase

The name of the modal load case for which the target periods apply.

Mode

This is an array that includes the mode number associated with each target period.

Period

This is an array that includes the target periods. [s]

Active

If this item is True, all specified target periods are active. If it is False, they are inactive.

## Remarks

This function retrieves time period targets for steel design.

The function returns zero if the targets are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignTargetPeriod()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyMode() As Long
      Dim MyPeriod() As Double
      Dim NumberItems As Long
      Dim ModalCase As String
      Dim Mode() As Long
      Dim Period() As Double
      Dim Active As Boolean

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

   'set target period data
      ReDim MyLCase(0)
      ReDim MyMode(1)
      ReDim MyPeriod(1)
      MyMode(0) = 1
      MyPeriod(0) = 0.6
      MyMode(1) = 2
      MyPeriod(1) = 0.5
      ret = SapModel.DesignSteel.SetTargetPeriod(2, "MODAL", MyMode, MyPeriod)

   'get target period data
      ret = SapModel.DesignSteel.GetTargetPeriod(NumberItems, ModalCase, Mode, Period, Active)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[SetTargetPeriod](SetTargetPeriod.htm)



## GetOverwrite {Steel Indian IS 800-1998}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Indian_IS_800-1998/GetOverwrite_{Steel_Indian_IS_800-1998}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.INDIAN\_IS\_800\_1998.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 34, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor

19 = Unbraced length ratio, Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Effective length factor, K Lateral Torsional Buckling

23 = Moment coefficient, Cm Major

24 = Moment coefficient, Cm Minor

25 = Yield stress, Fy

26 = Allowable compressive stress, Sigma\_ac

27 = Allowable tensile stress, Sigma\_at

28 = Allowable major bending stress, Sigma\_bc33

29 = Allowable minor bending stress, Sigma\_bc22

30 = Major average shear stress, Tau\_va2

31 = Minor average shear stress, Tau\_va3

32 = Maximum elastic shear stress, Tau\_vm

33 = Allowable effective stress, Sigma\_e

34 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway Frame

2 = Nonsway Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

22 = Effective length factor, K Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

24 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

25 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

26 = Allowable compressive stress, Sigma\_ac

Value >= 0; 0 means use program determined value. [F/L2]

27 = Allowable tensile stress, Sigma\_at

Value >= 0; 0 means use program determined value. [F/L2]

28 = Allowable major bending stress, Sigma\_bc33

Value >= 0; 0 means use program determined value. [F/L2]

29 = Allowable minor bending stress, Sigma\_bc22

Value >= 0; 0 means use program determined value. [F/L2]

30 = Major average shear stress, Tau\_va2

Value >= 0; 0 means use program determined value. [F/L2]

31 = Minor average shear stress, Tau\_va3

Value >= 0; 0 means use program determined value. [F/L2]

32 = Maximum elastic shear stress, Tau\_vm

Value >= 0; 0 means use program determined value. [F/L2]

33 = Allowable effective stress, Sigma\_e

Value >= 0; 0 means use program determined value. [F/L2]

34 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemINDIAN\_IS\_800\_1998()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Indian IS:800-1998")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.INDIAN\_IS\_800\_1998.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_Indian_IS_800-1998}.htm)



## GetPreference {Steel Indian IS 800-1998}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Indian_IS_800-1998/GetPreference_{Steel_Indian_IS_800-1998}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Indian\_IS:800\_1998.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Framing type

2 = Lateral factor

3 = Consider deflection

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total deflection limit, L/Value

8 = Total camber limit, L/Value

9 = Pattern live load factor

10 = Demand/capacity ratio limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Sway Frame

2 = Nonsway Frame

2 = Lateral factor

Value > 0

3 = Consider deflection

0 = No

Any other value = Yes

4 = DL deflection limit, L/Value

Value > 0

5 = SDL + LL deflection limit, L/Value

Value > 0

6 = LL deflection limit, L/Value

Value > 0

7 = Total deflection limit, L/Value

Value > 0

8 = Total camber limit, L/Value

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Demand/capacity ratio limit

Value > 0

11 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemIndian\_IS\_800\_1998()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Indian IS:800-1998")

   'get preference item
      ret = SapModel.DesignSteel.Indian\_IS\_800\_1998.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_Indian_IS_800-1998}.htm)



## SetOverwrite {Steel Indian IS 800-1998}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Indian_IS_800-1998/SetOverwrite_{Steel_Indian_IS_800-1998}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.INDIAN\_IS\_800\_1998.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 34, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor

19 = Unbraced length ratio, Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Effective length factor, K Lateral Torsional Buckling

23 = Moment coefficient, Cm Major

24 = Moment coefficient, Cm Minor

25 = Yield stress, Fy

26 = Allowable compressive stress, Sigma\_ac

27 = Allowable tensile stress, Sigma\_at

28 = Allowable major bending stress, Sigma\_bc33

29 = Allowable minor bending stress, Sigma\_bc22

30 = Major average shear stress, Tau\_va2

31 = Minor average shear stress, Tau\_va3

32 = Maximum elastic shear stress, Tau\_vm

33 = Allowable effective stress, Sigma\_e

34 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway Frame

2 = Nonsway Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

Value >= 0. [L]

15 = Net area to total area ratio

Value >= 0; 0 means use program default value.

16 = Live load reduction factor

Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

22 = Effective length factor, K Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

24 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

25 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

26 = Allowable compressive stress, Sigma\_ac

Value >= 0; 0 means use program determined value. [F/L2]

27 = Allowable tensile stress, Sigma\_at

Value >= 0; 0 means use program determined value. [F/L2]

28 = Allowable major bending stress, Sigma\_bc33

Value >= 0; 0 means use program determined value. [F/L2]

29 = Allowable minor bending stress, Sigma\_bc22

Value >= 0; 0 means use program determined value. [F/L2]

30 = Major average shear stress, Tau\_va2

Value >= 0; 0 means use program determined value. [F/L2]

31 = Minor average shear stress, Tau\_va3

Value >= 0; 0 means use program determined value. [F/L2]

32 = Maximum elastic shear stress, Tau\_vm

Value >= 0; 0 means use program determined value. [F/L2]

33 = Allowable effective stress, Sigma\_e

Value >= 0; 0 means use program determined value. [F/L2]

34 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemINDIAN\_IS\_800\_1998()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Indian IS:800-1998")

   'set overwrite item
      ret = SapModel.DesignSteel.INDIAN\_IS\_800\_1998.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_Indian_IS_800-1998}.htm)



## SetPreference {Steel Indian IS 800-1998}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Indian_IS_800-1998/SetPreference_{Steel_Indian_IS_800-1998}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Indian\_IS:800\_1998.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 11, inclusive, indicating the preference item considered.

1 = Framing type

2 = Lateral factor

3 = Consider deflection

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total deflection limit, L/Value

8 = Total camber limit, L/Value

9 = Pattern live load factor

10 = Demand/capacity ratio limit

11 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Sway Frame

2 = Nonsway Frame

2 = Lateral factor

Value > 0

3 = Consider deflection

0 = No

Any other value = Yes

4 = DL deflection limit, L/Value

Value > 0

5 = SDL + LL deflection limit, L/Value

Value > 0

6 = LL deflection limit, L/Value

Value > 0

7 = Total deflection limit, L/Value

Value > 0

8 = Total camber limit, L/Value

Value > 0

9 = Pattern live load factor

Value >= 0

10 = Demand/capacity ratio limit

Value > 0

11 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemIndian\_IS\_800\_1998()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Indian IS:800-1998")

   'set preference item
      ret = SapModel.DesignSteel.Indian\_IS\_800\_1998.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_Indian_IS_800-1998}.htm)



## GetOverwrite {Steel Indian IS 800-2007}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Indian_IS_800_2007/GetOverwrite_{Steel_Indian_IS_800-2007}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Indian\_IS\_800\_2007.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 44, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Section class

3 = Column buckling curve (z-z)

4 = Column buckling curve (y-y)

5 = Is rolled section

6 = Consider deflection

7 = Deflection check type

8 = DL deflection limit, L/Value

9 = SDL + LL deflection limit, L/Value

10 = LL deflection limit, L/Value

11 = Total load deflection limit, L/Value

12 = Total camber limit, L/Value

13 = DL deflection limit, absolute

14 = SDL + LL deflection limit, absolute

15 = LL deflection limit, absolute

16 = Total load deflection limit, absolute

17 = Total camber limit, absolute

18 = Specified camber

19 = Net area to total area ratio

20 = Live load reduction factor

21 = Unbraced length ratio, Major

22 = Unbraced length ratio, Minor

23 = Unbraced length ratio, Lateral Torsional Buckling

24 = Effective length factor Braced, K1 Major

25 = Effective length factor Braced, K1 Minor

26 = Effective length factor Sway, K2 Major

27 = Effective length factor Sway, K2 Minor

28 = Effective length factor, K Lateral Torsional Buckling

29 = Bending coefficient, C1

30 = Uniform moment factor, Cmz

31 = Uniform moment factor, Cmy

32 = Uniform moment factor, CmLT

33 = Moment coefficient, kz

34 = Moment coefficient, ky

35 = Moment coefficient, k\_LT

36 = Yield stress, Fy

37 = Compressive capacity, Pd

38 = Tensile capacity, Td

39 = Major bending capacity, Mdz

40 = Minor bending capacity, Mdy

41 = Critical buckling moment, Mcr

42 = Major shear capacity, Vdy

43 = Minor shear capacity, Vdz

44 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = SMF

2 = OMF

3 = SCBF

4 = OCBF

5 = EBF

6 = Secondary

2 = Section class

1 = Class 1 (Plastic)

2 = Class 2 (Compact)

3 = Class 3 (Semicompact)

4 = Class 4 (Slender)

3 = Column buckling curve (z-z)

1 = a

2 = b

3 = c

4 = d

4 = Column buckling curve (y-y)

1 = a

2 = b

3 = c

4 = d

5 = Is rolled section

      Value >= 0; 0 means use program default value

6 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

7 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

8 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

10 = LL deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

11 = Total load deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

12 = Total camber limit, L/Value

  Value >= 0; 0 means no check for this item.

13 = DL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

15 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

16 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

17 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

18 = Specified camber

  Value >= 0. [L]

19 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

20 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

21 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

22 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

23 = Unbraced length ratio, Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

24 = Effective length factor Braced, K1 Major

  Value >= 0; 0 means use program determined value.

25 = Effective length factor Braced, K1 Minor

  Value >= 0; 0 means use program determined value.

26 = Effective length factor Sway, K2 Major

  Value >= 0; 0 means use program determined value.

27 = Effective length Sway factor, K2 Minor

  Value >= 0; 0 means use program determined value.

28 = Effective length factor, K Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

29 = Bending coefficient, C1

  Value >= 0; 0 means use program determined value.

30 = Uniform moment factor, Cmz

  Value >= 0; 0 means use program determined value.

31 = Uniform moment factor, Cmy

  Value >= 0; 0 means use program determined value.

32 = Uniform moment factor, CmLT

  Value >= 0; 0 means use program determined value.

33 = Moment coefficient, kz

  Value >= 0; 0 means use program determined value.

34 = Moment coefficient, ky

  Value >= 0; 0 means use program determined value.

35 = Moment coefficient, k\_LT

  Value >= 0; 0 means use program determined value.

36 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

37 = Compressive capacity, Pd

  Value >= 0; 0 means use program determined value. [F]

38 = Tensile capacity, Td

  Value >= 0; 0 means use program determined value. [F]

39 = Major bending capacity, Mdz

  Value >= 0; 0 means use program determined value. [F-L]

40 = Minor bending capacity, Mdy

  Value >= 0; 0 means use program determined value. [F-L]

41 = Critical buckling moment, Mcr

  Value >= 0; 0 means use program determined value. [F-L]

42 = Major shear capacity, Vdy

  Value >= 0; 0 means use program determined value. [F]

43 = Minor shear capacity, Vdz

  Value >= 0; 0 means use program determined value. [F]

44 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ProgDet

If this item is True then the specified value is program determined.

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemINDIAN\_IS\_800\_2007()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Indian IS:800-2007")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.INDIAN\_IS\_800\_2007.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[SetOverwrite](SetOverwrite_{Steel_Indian_IS_800-2007}.htm)



## GetPreference {Steel Indian IS 800-2007}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Indian_IS_800_2007/GetPreference_{Steel_Indian_IS_800-2007}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Indian\_IS\_800\_2007.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 18, inclusive, indicating the preference item considered.

1 = Framing type

2 = Importance factor

3 = Seismic Zone

4 = Consider P-delta Done

5 = GammaM0

6 = GammaM1

7 = Ignore sseismic code

8 = Ignore special seismic load

9 = Is doubler plate plug-welded

10 = Consider deflection

11 = DL deflection limit, L/Value

12 = SDL + LL deflection limit, L/Value

13 = LL deflection limit, L/Value

14 = Total deflection limit, L/Value

15 = Total camber limit, L/Value

16 = Pattern live load factor

17 = Demand/capacity ratio limit

18 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = SMF

2 = OMF

3 = SCBF

4 = OCBF

5 = EBF

6 = Secondary

2 = Importance factor

Value > 0

3 = Seismic Zone

1 = Zone I

2 = Zone II

3 = Zone III

4 = Zone IV

5 = Zone V

4 = Consider P-delta Done

0 = No

Any other value = Yes

5 = GammaM0

Value > 0

6 = GammaM1

Value > 0

7 = Ignore sseismic code

0 = No

Any other value = Yes

8 = Ignore special seismic load

0 = No

Any other value = Yes

9 = Is doubler plate plug-welded

0 = No

Any other value = Yes

10 = Consider deflection

 0 = No

 Any other value = Yes

11 = DL deflection limit, L/Value

  Value > 0

12 = SDL + LL deflection limit, L/Value

  Value > 0

13 = LL deflection limit, L/Value

  Value > 0

14 = Total deflection limit, L/Value

  Value > 0

15 = Total camber limit, L/Value

  Value > 0

16 = Pattern live load factor

  Value >= 0

17 = Demand/capacity ratio limit

  Value > 0

18 = Time history design

  1 = Envelopes

  2 = Step-by step

  3 = Last step

  4 = Envelopes - All

  5 = Step-by step - All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemIndian\_IS\_800\_2007()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Indian IS 800:2007")

   'get preference item
      ret = SapModel.DesignSteel.Indian\_IS\_800\_2007.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_Indian_IS_800-2007}.htm)



## SetOverwrite {Steel Indian IS 800-2007}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Indian_IS_800_2007/SetOverwrite_{Steel_Indian_IS_800-2007}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Indian\_IS\_800\_2007.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 44, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Section class

3 = Column buckling curve (z-z)

4 = Column buckling curve (y-y)

5 = Is rolled section

6 = Consider deflection

7 = Deflection check type

8 = DL deflection limit, L/Value

9 = SDL + LL deflection limit, L/Value

10 = LL deflection limit, L/Value

11 = Total load deflection limit, L/Value

12 = Total camber limit, L/Value

13 = DL deflection limit, absolute

14 = SDL + LL deflection limit, absolute

15 = LL deflection limit, absolute

16 = Total load deflection limit, absolute

17 = Total camber limit, absolute

18 = Specified camber

19 = Net area to total area ratio

20 = Live load reduction factor

21 = Unbraced length ratio, Major

22 = Unbraced length ratio, Minor

23 = Unbraced length ratio, Lateral Torsional Buckling

24 = Effective length factor Braced, K1 Major

25 = Effective length factor Braced, K1 Minor

26 = Effective length factor Sway, K2 Major

27 = Effective length factor Sway, K2 Minor

28 = Effective length factor, K Lateral Torsional Buckling

29 = Bending coefficient, C1

30 = Uniform moment factor, Cmz

31 = Uniform moment factor, Cmy

32 = Uniform moment factor, CmLT

33 = Moment coefficient, kz

34 = Moment coefficient, ky

35 = Moment coefficient, k\_LT

36 = Yield stress, Fy

37 = Compressive capacity, Pd

38 = Tensile capacity, Td

39 = Major bending capacity, Mdz

40 = Minor bending capacity, Mdy

41 = Critical buckling moment, Mcr

42 = Major shear capacity, Vdy

43 = Minor shear capacity, Vdz

44 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = SMF

2 = OMF

3 = SCBF

4 = OCBF

5 = EBF

6 = Secondary

2 = Section class

1 = Class 1 (Plastic)

2 = Class 2 (Compact)

3 = Class 3 (Semicompact)

4 = Class 4 (Slender)

3 = Column buckling curve (z-z)

1 = a

2 = b

3 = c

4 = d

4 = Column buckling curve (y-y)

1 = a

2 = b

3 = c

4 = d

5 = Is rolled section

      Value >= 0; 0 means use program default value

6 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

7 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

8 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

10 = LL deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

11 = Total load deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

12 = Total camber limit, L/Value

  Value >= 0; 0 means no check for this item.

13 = DL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

15 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

16 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

17 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

18 = Specified camber

  Value >= 0. [L]

19 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

20 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

21 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

22 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

23 = Unbraced length ratio, Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

24 = Effective length factor Braced, K1 Major

  Value >= 0; 0 means use program determined value.

25 = Effective length factor Braced, K1 Minor

  Value >= 0; 0 means use program determined value.

26 = Effective length factor Sway, K2 Major

  Value >= 0; 0 means use program determined value.

27 = Effective length Sway factor, K2 Minor

  Value >= 0; 0 means use program determined value.

28 = Effective length factor, K Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

29 = Bending coefficient, C1

  Value >= 0; 0 means use program determined value.

30 = Uniform moment factor, Cmz

  Value >= 0; 0 means use program determined value.

31 = Uniform moment factor, Cmy

  Value >= 0; 0 means use program determined value.

32 = Uniform moment factor, CmLT

  Value >= 0; 0 means use program determined value.

33 = Moment coefficient, kz

  Value >= 0; 0 means use program determined value.

34 = Moment coefficient, ky

  Value >= 0; 0 means use program determined value.

35 = Moment coefficient, k\_LT

  Value >= 0; 0 means use program determined value.

36 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

37 = Compressive capacity, Pd

  Value >= 0; 0 means use program determined value. [F]

38 = Tensile capacity, Td

  Value >= 0; 0 means use program determined value. [F]

39 = Major bending capacity, Mdz

  Value >= 0; 0 means use program determined value. [F-L]

40 = Minor bending capacity, Mdy

  Value >= 0; 0 means use program determined value. [F-L]

41 = Critical buckling moment, Mcr

  Value >= 0; 0 means use program determined value. [F-L]

42 = Major shear capacity, Vdy

  Value >= 0; 0 means use program determined value. [F]

43 = Minor shear capacity, Vdz

  Value >= 0; 0 means use program determined value. [F]

44 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemINDIAN\_IS\_800\_2007()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Indian IS:800-2007")

   'set overwrite item
      ret = SapModel.DesignSteel.INDIAN\_IS\_800\_2007.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[GetOverwrite](GetOverwrite_{Steel_Indian_IS_800-2007}.htm)



## SetPreference {Steel Indian IS 800-2007}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Indian_IS_800_2007/SetPreference_{Steel_Indian_IS_800-2007}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Indian\_IS\_800\_2007.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 18, inclusive, indicating the preference item considered.

1 = Framing type

2 = Importance factor

3 = Seismic Zone

4 = Consider P-delta Done

5 = GammaM0

6 = GammaM1

7 = Ignore seismic code

8 = Ignore special seismic load

9 = Is doubler plate plug-welded

10 = Consider deflection

11 = DL deflection limit, L/Value

12 = SDL + LL deflection limit, L/Value

13 = LL deflection limit, L/Value

14 = Total deflection limit, L/Value

15 = Total camber limit, L/Value

16 = Pattern live load factor

17 = Demand/capacity ratio limit

18 = Multi-response case design

Value

The value of the considered preference item.

The value of the considered preference item.

1 = Framing type

1 = SMF

2 = OMF

3 = SCBF

4 = OCBF

5 = EBF

6 = Secondary

2 = Importance factor

Value > 0

3 = Seismic Zone

1 = Zone I

2 = Zone II

3 = Zone III

4 = Zone IV

5 = Zone V

4 = Consider P-delta Done

0 = No

Any other value = Yes

5 = GammaM0

Value > 0

6 = GammaM1

Value > 0

7 = Ignore sseismic code

0 = No

Any other value = Yes

8 = Ignore special seismic load

0 = No

Any other value = Yes

9 = Is doubler plate plug-welded

0 = No

Any other value = Yes

10 = Consider deflection

 0 = No

 Any other value = Yes

11 = DL deflection limit, L/Value

  Value > 0

12 = SDL + LL deflection limit, L/Value

  Value > 0

13 = LL deflection limit, L/Value

  Value > 0

14 = Total deflection limit, L/Value

  Value > 0

15 = Total camber limit, L/Value

  Value > 0

16 = Pattern live load factor

  Value >= 0

17 = Demand/capacity ratio limit

  Value > 0

18 = Time history design

  1 = Envelopes

  2 = Step-by step

  3 = Last step

  4 = Envelopes - All

  5 = Step-by step - All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemIndian\_IS\_800\_2007()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Indian IS:800-2007")

   'set preference item
      ret = SapModel.DesignSteel.Indian\_IS\_800\_2007.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_Indian_IS_800-2007}.htm)



## GetOverwrite {Steel Italian UNI 10011}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Italian_UNI_10011/GetOverwrite_{Steel_Italian_UNI_10011}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.ITALIAN\_UNI\_10011.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 26, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Axial load amplification(Omega)

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

20 = Effective length factor, Beta Major

21 = Effective length factor, Beta Minor

22 = Moment coefficient, Meq/Mmax Major

23 = Moment coefficient, Meq/Mmax Minor

24 = LTB moment coefficient (Omega1)

25 = Yield stress, Fy

26 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway Frame

2 = NonSway Frame

2 = Axial load amplification(Omega)

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L]

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Meq/Mmax Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Meq/Mmax Minor

Value >= 0; 0 means use program determined value.

24 = LTB moment coefficient (Omega1)

Value >= 0; 0 means use program determined value.

25 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

26 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemITALIAN\_UNI\_10011()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("ITALIAN UNI 10011")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.ITALIAN\_UNI\_10011.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_Italian_UNI_10011}.htm)



## GetPreference {Steel Italian UNI 10011}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Italian_UNI_10011/GetPreference_{Steel_Italian_UNI_10011}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Italian\_UNI\_10011.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Consider deflection

3 = DL deflection limit, L/Value

4 = SDL + LL deflectionlimit, L/Value

5 = LL deflection limit, L/Value

6 = Total deflectionlimit, L/Value

7 = Total camber limit, L/Value

8 = Pattern live load factor

9 = Demand/capacity ratio limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Sway Frame

2 = NonSway Frame

2 = Consider deflection

0 = No

Any other value = Yes

3 = DL deflection limit, L/Value

Value > 0

4 = SDL + LL deflection limit, L/Value

Value > 0

5 = LL deflection limit, L/Value

Value > 0

6 = Total deflection limit, L/Value

Value > 0

7 = Total camber limit, L/Value

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Demand/capacity ratio limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemItalian\_UNI\_10011()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Italian UNI 10011")

   'get preference item
      ret = SapModel.DesignSteel.Italian\_UNI\_10011.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_Italian_UNI_10011}.htm)



## SetOverwrite {Steel Italian UNI 10011}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Italian_UNI_10011/SetOverwrite_{Steel_Italian_UNI_10011}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.ITALIAN\_UNI\_10011.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemType item.

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 26, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Axial load amplification(Omega)

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor Lateral TorsionalBuckling

20 = Effective length factor, Beta Major

21 = Effective length factor, Beta Minor

22 = Moment coefficient, Meq/Mmax Major

23 = Moment coefficient, Meq/Mmax Minor

24 = LTB moment coefficient (Omega1)

25 = Yield stress, Fy

26 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Sway Frame

2 = NonSway Frame

2 = Axial load amplification(Omega)

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L]

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor Lateral TorsionalBuckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, Beta Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, Beta Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Meq/Mmax Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Meq/Mmax Minor

Value >= 0; 0 means use program determined value.

24 = LTB moment coefficient (Omega1)

Value >= 0; 0 means use program determined value.

25 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

26 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjectst, assignment is made to all selected frame objects, and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemITALIAN\_UNI\_10011()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("ITALIAN UNI 10011")

   'set overwrite item
      ret = SapModel.DesignSteel.ITALIAN\_UNI\_10011.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_Italian_UNI_10011}.htm)



## SetPreference {Steel Italian UNI 10011}

*Source file: `SAP2000_API_Fuctions/Design/Steel/Italian_UNI_10011/SetPreference_{Steel_Italian_UNI_10011}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Italian\_UNI\_10011.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 10, inclusive, indicating the preference item considered.

1 = Framing type

2 = Consider deflection

3 = DL deflection limit, L/Value

4 = SDL + LL deflectionlimit, L/Value

5 = LL deflection limit, L/Value

6 = Total deflectionlimit, L/Value

7 = Total camber limit, L/Value

8 = Pattern live load factor

9 = Demand/capacity ratio limit

10 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Sway Frame

2 = NonSway Frame

2 = Consider deflection

0 = No

Any other value = Yes

3 = DL deflection limit, L/Value

Value > 0

4 = SDL + LL deflection limit, L/Value

Value > 0

5 = LL deflection limit, L/Value

Value > 0

6 = Total deflection limit, L/Value

Value > 0

7 = Total camber limit, L/Value

Value > 0

8 = Pattern live load factor

Value >= 0

9 = Demand/capacity ratio limit

Value > 0

10 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemItalian\_UNI\_10011()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Italian UNI 10011")

   'set preference item
      ret = SapModel.DesignSteel.Italian\_UNI\_10011.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_Italian_UNI_10011}.htm)



## GetOverwrite {NTC_2008}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NTC_2008/GetOverwrite_{NTC_2008}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Italian\_NTC\_2008.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design
procedure.

Item

This is an integer between 1 and 54, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit,
L/Value

5 = SDL + LL deflection
limit, L/Value

6 = LL deflection limit,
L/Value

7 = Total load deflection
limit, L/Value

8 = Total camber limit,
L/Value

9 = DL deflection limit,
absolute

10 = SDL + LL deflection
limit, absolute

11 = LL deflection limit,
absolute

12 = Total load deflection
limit, absolute

13 = Total camber limit,
absolute

14 = Specified camber

15 = Net area to total
area ratio

16 = Live load reduction
factor

17 = Unbraced length ratio,
y-y

18 = Unbraced length ratio,
z-z

19 = Effective length
factor, K2y

20 = Effective length
factor, K2z

21 = Moment coefficient,
kyy

22 = Moment coefficient,
kzz

23 = Bending coefficient,
Ψ

24
= Moment coefficient, kzy

25
= Moment coefficient, kyz

26 = Yield stress, Fy

27 = Compressive capacity,
Nc.Rd

28 = Tensile capacity,
Nt.Rd

29 = Bending capacity
about y-y axis,Mcy.Rd

30 = Bending capacity
about z-z axis Mcz.Rd

31 = Buckling resistance
moment, Mb.Rd

32 = Shear capacity along
z-z axis, Vz.Rd

33 = Shear capacity along
y-y axis, Vy.Rd

34 = Demand/capacity ratio
limit

35 = Section class

36 = Column buckling curve,
y-y

37 = Column buckling curve,
z-z

38 = Buckling curve for LTB

39 = System overstrength factor,
Omega

40 = Is rolled section

41 = Unbraced length ratio,
LTB

42 = Effective length factor
braced, K1y

43 = Effective length factor
braced, K1z

44 = Effective length factor,
K LTB

45 = Material overstrength
factor, GammaRd

46 = Warping constant, Iw

47 = Elastic torsional buckling
force, Ncr T

48 = Elastic torsional-flexural
buckling force, Ncr TF

49
= Bending coefficient, C2

50 = Bending coefficient, C3

51 = Warping coefficient, kw

52 = Coordinate of load
application, za

53
= Shear center coordinate, zs

54
= Elastic critical moment for lateral-torsional buckling, Mcr

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = DCH-MRF

2 = DCL-MRF

3 = DCH-CBF

4 = DCL-CBF

5 = DCH-EBF

6 = DCL-EBF

7 = InvPendulum

8 = NonDissipative

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

5 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

6 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

7 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

8 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

9 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

10 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

11 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

12 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

14 = Specified camber

  Value >=
0. [L]

15 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

16 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

17 = Unbraced length ratio,
y-y

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
z-z

  Value >=
0; 0 means use program determined value.

19 = Effective length
factor sway, K2y

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor sway, K2z

  Value >=
0; 0 means use program determined value.

21 = Moment coefficient,
kyy

  Value >=
0; 0 means use program determined value.

22 = Moment coefficient,
kzz

  Value >=
0; 0 means use program determined value.

23 = Bending coefficient,
Ψ

  Value >=
0; 0 means use program determined value.

24 = Moment coefficient,
kzy

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
kyz

  Value >=
0; 0 means use program determined value.

26 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

27 = Compressive capacity,
Nc.Rd

  Value >=
0; 0 means use program determined value. [F]

28 = Tensile capacity,
Nt.Rd

  Value >=
0; 0 means use program determined value. [F]

29 = Bending capacity
about y-y axis, Mcy.Rd

  Value >=
0; 0 means use program determined value. [FL]

30 = Bending capacity
about z-z axis, Mcz.Rd

  Value >=
0; 0 means use program determined value. [FL]

31 = Buckling resistance
moment, Mb.Rd

  Value >=
0; 0 means use program determined value. [FL]

32 = Shear capacity along
z-z axis, Vz.Rd

  Value >=
0; 0 means use program determined value. [F]

33 = Shear capacity along
y-y axis, Vy.Rd

  Value >=
0; 0 means use program determined value. [F]

34 = Demand/capacity ratio
limit

  Value >= 0;
0 means use program determined value.

35 = Section class

0 = Program default

1 = Class 1

2 = Class 2

3 = Class 3

4 = Class 4

36 = Column buckling curve,
y-y

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

37 = Column buckling curve,
z-z

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

38
= Buckling curve for LTB

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

39 = System overstrength factor,
Omega

Value >= 0; 0 means use
program determined value.

40 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

41 = Unbraced length ratio,
LTB

Value >= 0; 0 means use
program determined value.

42 = Effective length factor
braced, K1y

Value >= 0; 0 means use
program determined value.

43 = Effective length factor
braced, K1z

Value >= 0; 0 means use
program determined value.

44 = Effective length factor,
K LTB

Value >= 0; 0 means use
program determined value.

45 = Material overstrength
factor, GammaRd

Value >= 0; 0 means use
program determined value.

46 = Warping constant, Iw

Value >= 0; 0 means use
program determined value. [L6]

47 = Elastic torsional buckling
force, Ncr T

Value >= 0; 0 means use
program determined value. [F]

48 = Elastic torsional-flexural
buckling force, Ncr TF

Value >= 0; 0 means
use program determined value. [F]

49
= Bending coefficient, C2

Value >= 0; 0 means
use program determined value.

50 = Bending coefficient,
C3

Value >= 0; 0 means
use program determined value.

51 = Warping coefficient,
kw (used in Mcr calculation)

0.5 =<Value =<
1; 0 means use program determined value which is defaulted to 1.0.

52 = Coordinate
of load application, za (used in Mcr calculation)

53
= Shear center coordinate, zs (used in Mcr calculation)

54
= Elastic critical moment for lateral-torsional buckling, Mcr

Value >=
0; 0 means use program determined value. [FL]

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a steel design
overwrite item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemItalian\_NTC\_2008()
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
      ret = SapModel.DesignSteel.SetCode("Italian
NTC 2008")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Italian\_NTC\_2008.GetOverwrite("8",
1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

Added items 49 - 52 in v22.0.0

Added items 53 - 54 in v22.0.0

Changed references from major and minor axes to y-y
and z-z in version 23.4.0.

## See Also

SetOverwrite



## GetPreference {NTC_2008}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NTC_2008/GetPreference_{NTC_2008}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Italian\_NTC\_2008.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 3 and 23, inclusive, indicating the preference item considered.

3 = Method Used for Buckling in P-M-M

4 = Framing type

5 = GammaM0

6 = GammeM1

7 = GammaM2

8 = Consider deflection

9 = DL deflection limit, L/Value

10 = SDL + LL deflection limit, L/Value

11 = LL deflection limit, L/Value

12 = Total deflection limit, L/Value

13 = Total camber limit, L/Value

14 = Pattern live load factor

15 = Demand/capacity ratio limit

16 = Multi-Response Case Design

17 = Behavior Factor, q0

18 = System Overstrength Factor, W

19 = Consider P-Delta

20 = Consider Torsion

21 = Ignore Seismic Code

22 = Ignore Special Seismic Load

23 = Is Doubler Plate Plug-Welded

Value

The value of the considered preference item.

3 = K factor method

   1 = Method A

   2 = Method B (default)

   3 = Both

4 = Framing type

1 = DCH-MRF (Default)

2 = DCL-MRF

3 = DCH-CBF

4 = DCL-CBF

5 = DCH-EBF

6 = DCL-EBF

7 = InvPendulum

8 = NonDissipative

5 = GammaM0

Default = 1.05, Value > 0

6 = GammaM1

Default = 1.05, Value > 0

7 = GammaM2

      Default = 1.25, Value > 0

8 = Consider deflection

Default = No = 1, Yes = 2

9 = DL deflection limit, L/Value

Default = 120, Value > 0

10 = SDL + LL deflection limit, L/Value

  Default = 120, Value > 0

11 = LL deflection limit, L/Value

  Default = 360, Value > 0

12 = Total deflection limit, L/Value

  Default = 240, Value > 0

13 = Total camber limit, L/Value

  Default = 240, Value > 0

14 = Pattern live load factor

  Default = 0, Value >= 0

15 = Demand/capacity ratio limit

  Default = 0.95, Value > 0

16 = Multi-response case design

  1 = Envelopes (Default)

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

17 = Behavior Factor, q0

  Default = 4, Value > 0

18 = System Overstrength Factor, W

  Default = 1.0, Value > 0

19 = Consider P-Delta

        Default = No = 1, Yes = 2

20 = Consider Torsion

        Default = No = 1, Yes = 2

21 = Ignore Seismic Code

        Default = No = 1, Yes = 2

22 = Ignore Special Seismic Load

        Default = No = 1, Yes = 2

23 = Is Doubler Plate Plug-Welded

  No = 1, Default = Yes = 2

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemItalian\_NTC\_2008()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Italian NTC 2008")

   'get preference item
      ret = SapModel.DesignSteel.Italian\_NTC\_2008.GetPreference(4, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.1.0.

## See Also

SetPreference



## SetOverwrite {NTC_2008}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NTC_2008/SetOverwrite_{NTC_2008}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Italian\_NTC\_2008.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType =
Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 54, inclusive, indicating
the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit,
L/Value

5 = SDL + LL deflection
limit, L/Value

6 = LL deflection limit,
L/Value

7 = Total load deflection
limit, L/Value

8 = Total camber limit,
L/Value

9 = DL deflection limit,
absolute

10 = SDL + LL deflection
limit, absolute

11 = LL deflection limit,
absolute

12 = Total load deflection
limit, absolute

13 = Total camber limit,
absolute

14 = Specified camber

15 = Net area to total
area ratio

16 = Live load reduction
factor

17 = Unbraced length ratio,
y-y

18 = Unbraced length ratio,
z-z

19 = Effective length
factor, K2y

20 = Effective length
factor, K2z

21 = Moment coefficient,
kyy

22 = Moment coefficient,
kzz

23 = Bending coefficient,
Ψ

24
= Moment coefficient, kzy

25
= Moment coefficient, kyz

26 = Yield stress, Fy

27 = Compressive capacity,
Nc.Rd

28 = Tensile capacity,
Nt.Rd

29 = Bending capacity
about y-y axis,Mcy.Rd

30 = Bending capacity
about z-z axis Mcz.Rd

31 = Buckling resistance
moment, Mb.Rd

32 = Shear capacity along
z-z axis, Vz.Rd

33 = Shear capacity along
y-y axis, Vy.Rd

34 = Demand/capacity ratio
limit

35 = Section class

36 = Column buckling curve,
y-y

37 = Column buckling curve,
z-z

38 = Buckling curve for LTB

39 = System overstrength factor,
Omega

40 = Is rolled section

41 = Unbraced length ratio,
LTB

42 = Effective length factor
braced, K1y

43 = Effective length factor
braced, K1z

44 = Effective length factor,
K LTB

45 = Material overstrength
factor, GammaRd

46 = Warping constant, Iw

47 = Elastic torsional buckling
force, Ncr T

48 = Elastic torsional-flexural
buckling force, Ncr TF

49
= Bending coefficient, C2

50 = Bending coefficient, C3

51 = Warping coefficient, kw

52 = Coordinate of load
application, za

53
= Shear center coordinate, zs

54
= Elastic critical moment for lateral-torsional buckling, Mcr

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = DCH-MRF

2 = DCL-MRF

3 = DCH-CBF

4 = DCL-CBF

5 = DCH-EBF

6 = DCL-EBF

7 = InvPendulum

8 = NonDissipative

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

5 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

6 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

7 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

8 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

9 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

10 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

11 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

12 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

14 = Specified camber

  Value >=
0. [L]

15 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

16 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

17 = Unbraced length ratio,
y-y

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
z-z

  Value >=
0; 0 means use program determined value.

19 = Effective length
factor sway, K2y

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor sway, K2z

  Value >=
0; 0 means use program determined value.

21 = Moment coefficient,
kyy

  Value >=
0; 0 means use program determined value.

22 = Moment coefficient,
kzz

  Value >=
0; 0 means use program determined value.

23 = Bending coefficient,
Ψ

  Value >=
0; 0 means use program determined value.

24 = Moment coefficient,
kzy

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
kyz

  Value >=
0; 0 means use program determined value.

26 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

27 = Compressive capacity,
Nc.Rd

  Value >=
0; 0 means use program determined value. [F]

28 = Tensile capacity,
Nt.Rd

  Value >=
0; 0 means use program determined value. [F]

29 = Bending capacity
about y-y axis, Mcy.Rd

  Value >=
0; 0 means use program determined value. [FL]

30 = Bending capacity
about z-z axis, Mcz.Rd

  Value >=
0; 0 means use program determined value. [FL]

31 = Buckling resistance
moment, Mb.Rd

  Value >=
0; 0 means use program determined value. [FL]

32 = Shear capacity along
z-z axis, Vz.Rd

  Value >=
0; 0 means use program determined value. [F]

33 = Shear capacity along
y-y axis, Vy.Rd

  Value >=
0; 0 means use program determined value. [F]

34 = Demand/capacity ratio
limit

  Value >= 0;
0 means use program determined value.

35 = Section class

0 = Program default

1 = Class 1

2 = Class 2

3 = Class 3

4 = Class 4

36 = Column buckling curve,
y-y

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

37 = Column buckling curve,
z-z

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

38
= Buckling curve for LTB

0 = Program default

1 = a0

2 = a

3 = b

4 = c

5 = d

39 = System overstrength factor,
Omega

Value >= 0; 0 means use
program determined value.

40 = Is rolled section

0 = Program Determined

1 = No

2 = Yes

41 = Unbraced length ratio,
LTB

Value >= 0; 0 means use
program determined value.

42 = Effective length factor
braced, K1y

Value >= 0; 0 means use
program determined value.

43 = Effective length factor
braced, K1z

Value >= 0; 0 means use
program determined value.

44 = Effective length factor,
K LTB

Value >= 0; 0 means use
program determined value.

45 = Material overstrength
factor, GammaRd

Value >= 0; 0 means use
program determined value.

46 = Warping constant, Iw

Value >= 0; 0 means use
program determined value. [L6]

47 = Elastic torsional buckling
force, Ncr T

Value >= 0; 0 means use
program determined value. [F]

48 = Elastic torsional-flexural
buckling force, Ncr TF

Value >= 0; 0 means
use program determined value. [F]

49
= Bending coefficient, C2

Value >= 0; 0 means
use program determined value.

50 = Bending coefficient,
C3

Value >= 0; 0 means
use program determined value.

51 = Warping coefficient,
kw (used in Mcr calculation)

0.5 =<Value =<
1; 0 means use program determined value which is defaulted to 1.0.

52 = Coordinate
of load application, za (used in Mcr calculation)

53
= Shear center coordinate, zs (used in Mcr calculation)

54
= Elastic critical moment for lateral-torsional buckling, Mcr

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
to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite
item.

The function returns zero if the item is successfully
set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemItalian\_NTC\_2008()
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
      ret = SapModel.DesignSteel.SetCode("Italian
NTC 2008")

   'set overwrite item
      ret = SapModel.DesignSteel.Italian\_NTC\_2008.SetOverwrite("8",
1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

Added items 49 - 52 in v22.0.0

Added items 53 - 54 in v22.0.0

Changed references from major and minor axes to y-y
and z-z in version 23.4.0.

## See Also

[GetOverwrite](GetOverwrite_{NTC_2008}.htm)



## SetPreference {NTC_2008}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NTC_2008/SetPreference_{NTC_2008}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Italian\_NTC\_2008.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 3 and 23, inclusive, indicating the preference item considered.

3 = Method Used for Buckling in P-M-M

4 = Framing type

5 = GammaM0

6 = GammeM1

7 = GammaM2

8 = Consider deflection

9 = DL deflection limit, L/Value

10 = SDL + LL deflection limit, L/Value

11 = LL deflection limit, L/Value

12 = Total deflection limit, L/Value

13 = Total camber limit, L/Value

14 = Pattern live load factor

15 = Demand/capacity ratio limit

16 = Multi-Response Case Design

17 = Behavior Factor, q0

18 = System Overstrength Factor, W

19 = Consider P-Delta

20 = Consider Torsion

21 = Ignore Seismic Code

22 = Ignore Special Seismic Load

23 = Is Doubler Plate Plug-Welded

Value

The value of the considered preference item.

3 = K factor method

   1 = Method A

   2 = Method B (default)

   3 = Both

4 = Framing type

1 = DCH-MRF (Default)

2 = DCL-MRF

3 = DCH-CBF

4 = DCL-CBF

5 = DCH-EBF

6 = DCL-EBF

7 = InvPendulum

8 = NonDissipative

5 = GammaM0

Default = 1.05, Value > 0

6 = GammaM1

Default = 1.05, Value > 0

7 = GammaM2

      Default = 1.25, Value > 0

8 = Consider deflection

Default = No = 1, Yes = 2

9 = DL deflection limit, L/Value

Default = 120, Value > 0

10 = SDL + LL deflection limit, L/Value

  Default = 120, Value > 0

11 = LL deflection limit, L/Value

  Default = 360, Value > 0

12 = Total deflection limit, L/Value

  Default = 240, Value > 0

13 = Total camber limit, L/Value

  Default = 240, Value > 0

14 = Pattern live load factor

  Default = 0, Value >= 0

15 = Demand/capacity ratio limit

  Default = 0.95, Value > 0

16 = Multi-response case design

  1 = Envelopes (Default)

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

17 = Behavior Factor, q0

  Default = 4, Value > 0

18 = System Overstrength Factor, W

  Default = 1.0, Value > 0

19 = Consider P-Delta

        Default = No = 1, Yes = 2

20 = Consider Torsion

        Default = No = 1, Yes = 2

21 = Ignore Seismic Code

        Default = No = 1, Yes = 2

22 = Ignore Special Seismic Load

        Default = No = 1, Yes = 2

23 = Is Doubler Plate Plug-Welded

  No = 1, Default = Yes = 2

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemItalian\_NTC\_2008()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Italian NTC 2008")

   'set preference item
      ret = SapModel.DesignSteel.Italian\_NTC\_2008.SetPreference(4, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

## See Also

[GetPreference](GetPreference_{NTC_2008}.htm)



## GetOverwrite {NTC_2018}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NTC_2018/GetOverwrite_{NTC_2018}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Italian\_NTC\_2018.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item
As Long, ByRef textValue As String, ByRef numericValue As Double, ByRef
ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design
procedure.

Item

This is an integer between 1 and 55, inclusive, indicating
the overwrite item considered.

1 = Current Design Section

2 = Framing type

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit,
L/Value

6 = SDL + LL deflection
limit, L/Value

7 = LL deflection limit,
L/Value

8 = Total load deflection
limit, L/Value

9 = Total camber limit,
L/Value

10 = DL deflection limit,
absolute

11 = SDL + LL deflection
limit, absolute

12 = LL deflection limit,
absolute

13 = Total load deflection
limit, absolute

14 = Total camber limit,
absolute

15 = Specified camber

16 = Net area to total
area ratio

17 = Live load reduction
factor

18 = Unbraced length ratio,
y-y

19 = Unbraced length ratio,
z-z

20 = Effective length
factor, K2y

21 = Effective length
factor, K2z

22 = Moment coefficient,
kyy

23 = Moment coefficient,
kzz

24 = Bending coefficient,
Ψ

25
= Moment coefficient, kzy

26
= Moment coefficient, kyz

27 = Yield stress, Fy

28 = Compressive capacity,
Nc.Rd

29 = Tensile capacity,
Nt.Rd

30 = Bending capacity
about y-y axis,Mcy.Rd

31 = Bending capacity
about z-z axis Mcz.Rd

32 = Buckling resistance
moment, Mb.Rd

33 = Shear capacity along
z-z axis, Vz.Rd

34 = Shear capacity along
y-y axis, Vy.RD

35 = Demand/capacity ratio
limit

36 = Section class

37 = Column buckling curve,
y-y

38 = Column buckling curve,
z-z

39 = Buckling curve for LTB

40 = System overstrength factor,
Omega

41 = Is rolled section

42 = Unbraced length ratio,
LTB

43 = Effective length factor
braced, K1y

44 = Effective length factor
braced, K1z

45 = Effective length factor,
K LTB

46 = Material overstrength
factor, GammaRd

47 = Warping constant, Iw

48 = Elastic torsional buckling
force, Ncr T

49 = Elastic torsional-flexural
buckling force, Ncr TF

50
= Bending coefficient, C2

51 = Bending coefficient,
C3

52 = Warping coefficient,
kw

53 = Coordinate of load
application, za

54
= Shear center coordinate, zs

55
= Elastic critical moment for lateral-torsional buckling, Mcr

Value

The value of the considered overwrite item.

1 = Current design section

      0 or "Program
Determined"

      String corresponding
to desired shape overwrite, e.g. "W14x26" or "W14X26".

2 = Framing type

0 or "Program Default"

1 or "DCH-MRF"

2 or "DCL-MRF"

3 or "DCH-CBF"

4 or "DCL-CBF"

5 or "DCH-EBF"

6 or "DCL-EBF"

7 or "InvPendulum"

8 or "NonDissipative"

3 = Consider deflection

0 or "Program Default"

1 or "No"

2 or "Yes"

4 = Deflection check type

0 or "Program Default"

1 or "Ratio"

2 or "Absolute"

3 or "Both"

5 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

6 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

7 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

8 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

9 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

10 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

11 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

12 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

14 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

15 = Specified camber

  Value >=
0. [L]

16 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

17 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
y-y

  Value >=
0; 0 means use program determined value.

19 = Unbraced length ratio,
z-z

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor sway, K2y

  Value >=
0; 0 means use program determined value.

21 = Effective length
factor sway,K2z

  Value >=
0; 0 means use program determined value.

22 = Moment coefficient,
kyy

  Value >=
0; 0 means use program determined value.

23 = Moment coefficient,
kzz

  Value >=
0; 0 means use program determined value.

24 = Bending coefficient,
Ψ

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
kzy

  Value >=
0; 0 means use program determined value.

26 = Moment coefficient,
kyz

  Value >=
0; 0 means use program determined value.

27 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

28 = Compressive capacity,
Nc.Rd

  Value >=
0; 0 means use program determined value. [F]

29 = Tensile capacity,
Nt.Rd

  Value >=
0; 0 means use program determined value. [F]

30 = Bending capacity
about y-y axis, Mcy.Rd

  Value >=
0; 0 means use program determined value. [FL]

31 = Bending capacity
about z-z axis, Mcz.Rd

  Value >=
0; 0 means use program determined value. [FL]

32 = Buckling resistance
moment, Mb.Rd

  Value >=
0; 0 means use program determined value. [FL]

33 = Shear capacity along
z-z axis, Vz.Rd

  Value >=
0; 0 means use program determined value. [F]

34 = Shear capacity along
y-y axis, Vy.Rd

  Value >=
0; 0 means use program determined value. [F]

35 = Demand/capacity ratio
limit

  Value >= 0;
0 means use program determined value.

36 = Section class

0 or "Program default"

1 or "Class 1"

2 or "Class 2"

3 or "Class 3"

4 or "Class 4"

37 = Column buckling curve,
y-y

0 or "Program default"

1 or "a0"

2 or "a"

3 or "b"

4 or "c"

5 or "d"

38 = Column buckling curve,
z-z

0 or "Program default"

1 or "a0"

2 or "a"

3 or "b"

4 or "c"

5 or "d"

39 = Buckling curve for LTB

0 or "Program default"

1 or "a0"

2 or "a"

3 or "b"

4 or "c"

5 or "d"

40 = System overstrength factor,
Omega

Value >= 0; 0 means use
program determined value.

41 = Is rolled section

0 or "Program Determined"

1 or "No"

2 or "Yes"

42 = Unbraced length ratio,
LTB

Value >= 0; 0 means use
program determined value.

43 = Effective length factor
braced, K1y

Value >= 0; 0 means use
program determined value.

44 = Effective length factor
braced, K1yz

Value >= 0; 0 means use
program determined value.

45 = Effective length factor,
K LTB

Value >= 0; 0 means use
program determined value.

46 = Material overstrength
factor, GammaRd

Value >= 0; 0 means use
program determined value.

47 = Warping constant, Iw

Value >= 0; 0 means use
program determined value. [L6]

48 = Elastic torsional buckling
force, Ncr T

Value >= 0; 0 means use
program determined value. [F]

49 = Elastic torsional-flexural
buckling force, Ncr TF

Value >= 0; 0 means
use program determined value. [F]

50
= Bending coefficient, C2

Value >= 0; 0 means
use program determined value.

51 = Bending coefficient,
C3

Value >= 0; 0 means
use program determined value.

52 = Warping coefficient,
kw (used in Mcr calculation)

0.5 =<Value =<
1; 0 means use program determined value which is defaulted to 1.0.

53 = Coordinate of load
application, za (used in Mcr calculation)

54 = Shear center coordinate,
zs (used in Mcr calculation)

55
= Elastic critical moment for lateral-torsional buckling, Mcr

Value >=
0; 0 means use program determined value. [FL]

ProgDet

If this item is True, the specified value is program
determined.

## Remarks

This function retrieves the value of a steel design
preference item.

The function returns zero if the item is successfully
retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemItalian\_NTC\_2018()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim textValue As
String
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
      ret = SapModel.DesignSteel.SetCode("Italian
NTC 2018")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Italian\_NTC\_2018.GetOverwrite("8",
2, textValue, numericValue, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

Added items 50 - 53 in v22.0.0

Added items 54 - 55 in v22.0.0

Changed references from major and minor axes to y-y
and z-z in version 23.4.0.

## See Also

[SetOverwrite](SetOverwrite_{NTC_2018}.htm)



## GetPreference {NTC_2018}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NTC_2018/GetPreference_{NTC_2018}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Italian\_NTC\_2018.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef textValue As String, ByRef numericValue As Double) As Long

## Parameters

Item

This is an integer between 3 and 23, inclusive, indicating the preference item considered.

3 = Method Used for Buckling in P-M-M

4 = Framing type

5 = GammaM0

6 = GammeM1

7 = GammaM2

8 = Consider deflection

9 = DL deflection limit, L/Value

10 = SDL + LL deflection limit, L/Value

11 = LL deflection limit, L/Value

12 = Total deflection limit, L/Value

13 = Total camber limit, L/Value

14 = Pattern live load factor

15 = Demand/capacity ratio limit

16 = Multi-Response Case Design

17 = Behavior Factor, q0

18 = System Overstrength Factor, W

19 = Consider P-Delta

20 = Consider Torsion

21 = Ignore Seismic Code

22 = Ignore Special Seismic Load

23 = Is Doubler Plate Plug-Welded

Value

The value of the considered preference item.

3 = K factor method

1 or "Method A"

2 or "Method B" - Default

3 or "Both"

4 =  Framing type

1 or "DCH-MRF"

2 or "DCL-MRF"

3 or "DCH-CBF"

4 or "DCL-CBF"

5 or "DCH-EBF"

6 or "DCL-EBF"

7 or "InvPendulum"

8 or "Non Dissipative" - (Default)

5 = GammaM0

Default = 1.05, Value > 0

6 = GammaM1

Default = 1.05, Value > 0

7 = GammaM2

      Default = 1.25, Value > 0

8 = Consider deflection

1 or "No" - Default

2 or "Yes"

9 = DL deflection limit, L/Value

Default = 0, Value > 0

10 = SDL + LL deflection limit, L/Value

  Default = 0, Value > 0

11 = LL deflection limit, L/Value

  Default = 300, Value > 0

12 = Total deflection limit, L/Value

  Default = 0, Value > 0

13 = Total camber limit, L/Value

  Default = 250, Value > 0

14 = Pattern live load factor

  Default = 0, Value >= 0

15 = Demand/capacity ratio limit

  Default = 1.0, Value > 0

16 = Multi-response case design

  1 or "Envelopes" - (Default)

  2 or "Step-by-step"

  3 or "Last step"

  4 or "Envelopes -- All"

  5 or "Step-by-step -- All"

17 = Behavior Factor, q0

  Default = 1, Value > 0

18 = System Overstrength Factor, W

  Default = 1.0, Value > 0

19 = Consider P-Delta

        1 or "No" - Default

        2 or "Yes"

20 = Consider Torsion

        1 or "No" - Default

        2 or "Yes"

21 = Ignore Seismic Code

        1 or "No" - Default

        2 or "Yes"

22 = Ignore Special Seismic Load

        1 or "No" - Default

        2 or "Yes"

23 = Is Doubler Plate Plug-Welded

  1 or "No" - Default

        2 or "Yes"

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemItalian\_NTC\_2018()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long

      Dim textValue As String
      Dim numericValue As Double

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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Italian NTC 2018")

   'get preference item
      ret = SapModel.DesignSteel.Italian\_NTC\_2018.GetPreference(4, textValue, numericValue)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.1.0.

## See Also

[SetPreference](SetPreference_{NTC_2018}.htm)



## SetOverwrite {NTC_2018}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NTC_2018/SetOverwrite_{NTC_2018}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Italian\_NTC\_2018.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item
As Long, ByVal textValue As String, ByVal numericValue As Double, Optional
ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending
on the value of the ItemType item.

Item

This is an integer between 1 and 55, inclusive, indicating
the overwrite item considered.

1 = Current Design Section

2 = Framing type

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit,
L/Value

6 = SDL + LL deflection
limit, L/Value

7 = LL deflection limit,
L/Value

8 = Total load deflection
limit, L/Value

9 = Total camber limit,
L/Value

10 = DL deflection limit,
absolute

11 = SDL + LL deflection
limit, absolute

12 = LL deflection limit,
absolute

13 = Total load deflection
limit, absolute

14 = Total camber limit,
absolute

15 = Specified camber

16 = Net area to total
area ratio

17 = Live load reduction
factor

18 = Unbraced length ratio,
y-y

19 = Unbraced length ratio,
z-z

20 = Effective length
factor, K2y

21 = Effective length
factor, K2z

22 = Moment coefficient,
kyy

23 = Moment coefficient,
kzz

24 = Bending coefficient,
Ψ

25
= Moment coefficient, kzy

26
= Moment coefficient, kyz

27 = Yield stress, Fy

28 = Compressive capacity,
Nc.Rd

29 = Tensile capacity,
Nt.Rd

30 = Bending capacity
about y-y axis,Mcy.Rd

31 = Bending capacity
about z-z axis Mcz.Rd

32 = Buckling resistance
moment, Mb.Rd

33 = Shear capacity along
z-z axis, Vz.Rd

34 = Shear capacity along
y-y axis, Vy.RD

35 = Demand/capacity ratio
limit

36 = Section class

37 = Column buckling curve,
y-y

38 = Column buckling curve,
z-z

39 = Buckling curve for LTB

40 = System overstrength factor,
Omega

41 = Is rolled section

42 = Unbraced length ratio,
LTB

43 = Effective length factor
braced, K1y

44 = Effective length factor
braced, K1z

45 = Effective length factor,
K LTB

46 = Material overstrength
factor, GammaRd

47 = Warping constant, Iw

48 = Elastic torsional buckling
force, Ncr T

49 = Elastic torsional-flexural
buckling force, Ncr TF

50
= Bending coefficient, C2

51 = Bending coefficient,
C3

52 = Warping coefficient,
kw

53 = Coordinate of load
application, za

54
= Shear center coordinate, zs

55
= Elastic critical moment for lateral-torsional buckling, Mcr

Value

The value of the considered overwrite item.

1 = Current design section

      0 or "Program
Determined"

      String corresponding
to desired shape overwrite, e.g. "W14x26" or "W14X26".

2 = Framing type

0 or "Program Default"

1 or "DCH-MRF"

2 or "DCL-MRF"

3 or "DCH-CBF"

4 or "DCL-CBF"

5 or "DCH-EBF"

6 or "DCL-EBF"

7 or "InvPendulum"

8 or "NonDissipative"

3 = Consider deflection

0 or "Program Default"

1 or "No"

2 or "Yes"

4 = Deflection check type

0 or "Program Default"

1 or "Ratio"

2 or "Absolute"

3 or "Both"

5 = DL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

6 = SDL + LL deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

7 = LL deflection limit,
L/Value

Value >= 0; 0 means
no check for this item.

8 = Total load deflection
limit, L/Value

Value >= 0; 0 means
no check for this item.

9 = Total camber limit,
L/Value

Value >= 0; 0 means
no check for this item.

10 = DL deflection limit,
absolute

Value >= 0; 0 means
no check for this item. [L]

11 = SDL + LL deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

12 = LL deflection limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

13 = Total load deflection
limit, absolute

  Value >=
0; 0 means no check for this item. [L]

14 = Total camber limit,
absolute

  Value >=
0; 0 means no check for this item. [L]

15 = Specified camber

  Value >=
0. [L]

16 = Net area to total
area ratio

  Value >=
0; 0 means use program default value.

17 = Live load reduction
factor

  Value >=
0; 0 means use program determined value.

18 = Unbraced length ratio,
y-y

  Value >=
0; 0 means use program determined value.

19 = Unbraced length ratio,
z-z

  Value >=
0; 0 means use program determined value.

20 = Effective length
factor sway, K2y

  Value >=
0; 0 means use program determined value.

21 = Effective length
factor sway,K2z

  Value >=
0; 0 means use program determined value.

22 = Moment coefficient,
kyy

  Value >=
0; 0 means use program determined value.

23 = Moment coefficient,
kzz

  Value >=
0; 0 means use program determined value.

24 = Bending coefficient,
Ψ

  Value >=
0; 0 means use program determined value.

25 = Moment coefficient,
kzy

  Value >=
0; 0 means use program determined value.

26 = Moment coefficient,
kyz

  Value >=
0; 0 means use program determined value.

27 = Yield stress, Fy

  Value >=
0; 0 means use program determined value. [F/L2]

28 = Compressive capacity,
Nc.Rd

  Value >=
0; 0 means use program determined value. [F]

29 = Tensile capacity,
Nt.Rd

  Value >=
0; 0 means use program determined value. [F]

30 = Bending capacity
about y-y axis, Mcy.Rd

  Value >=
0; 0 means use program determined value. [FL]

31 = Bending capacity
about z-z axis, Mcz.Rd

  Value >=
0; 0 means use program determined value. [FL]

32 = Buckling resistance
moment, Mb.Rd

  Value >=
0; 0 means use program determined value. [FL]

33 = Shear capacity along
z-z axis, Vz.Rd

  Value >=
0; 0 means use program determined value. [F]

34 = Shear capacity along
y-y axis, Vy.Rd

  Value >=
0; 0 means use program determined value. [F]

35 = Demand/capacity ratio
limit

  Value >= 0;
0 means use program determined value.

36 = Section class

0 or "Program default"

1 or "Class 1"

2 or "Class 2"

3 or "Class 3"

4 or "Class 4"

37 = Column buckling curve,
y-y

0 or "Program default"

1 or "a0"

2 or "a"

3 or "b"

4 or "c"

5 or "d"

38 = Column buckling curve,
z-z

0 or "Program default"

1 or "a0"

2 or "a"

3 or "b"

4 or "c"

5 or "d"

39 = Buckling curve for LTB

0 or "Program default"

1 or "a0"

2 or "a"

3 or "b"

4 or "c"

5 or "d"

40 = System overstrength factor,
Omega

Value >= 0; 0 means use
program determined value.

41 = Is rolled section

0 or "Program Determined"

1 or "No"

2 or "Yes"

42 = Unbraced length ratio,
LTB

Value >= 0; 0 means use
program determined value.

43 = Effective length factor
braced, K1y

Value >= 0; 0 means use
program determined value.

44 = Effective length factor
braced, K1yz

Value >= 0; 0 means use
program determined value.

45 = Effective length factor,
K LTB

Value >= 0; 0 means use
program determined value.

46 = Material overstrength
factor, GammaRd

Value >= 0; 0 means use
program determined value.

47 = Warping constant, Iw

Value >= 0; 0 means use
program determined value. [L6]

48 = Elastic torsional buckling
force, Ncr T

Value >= 0; 0 means use
program determined value. [F]

49 = Elastic torsional-flexural
buckling force, Ncr TF

Value >= 0; 0 means
use program determined value. [F]

50
= Bending coefficient, C2

Value >= 0; 0 means
use program determined value.

51 = Bending coefficient,
C3

Value >= 0; 0 means
use program determined value.

52 = Warping coefficient,
kw (used in Mcr calculation)

0.5 =<Value =<
1; 0 means use program determined value which is defaulted to 1.0.

53 = Coordinate of load
application, za (used in Mcr calculation)

54 = Shear center coordinate,
zs (used in Mcr calculation)

55
= Elastic critical moment for lateral-torsional buckling, Mcr

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
to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite
item.

The function returns zero if the item is successfully
set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemItalian\_NTC\_2018()
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
      ret = SapModel.DesignSteel.SetCode("Italian
NTC 2018")

   'set overwrite item
      ret = SapModel.DesignSteel.Italian\_NTC\_2018.SetOverwrite("8",
2, "DCH-CBF", 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

Added items 50 - 53 in v22.0.0

Added items 54 - 55 in v22.0.0

Changed references from major and minor axes to y-y
and z-z in version 23.4.0.

## See Also

[GetOverwrite](GetOverwrite_{NTC_2018}.htm)



## SetPreference {NTC_2018}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NTC_2018/SetPreference_{NTC_2018}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Italian\_NTC\_2018.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal textValue As String, ByVal numericValue As Double) As Long

## Parameters

Item

This is an integer between 3 and 23, inclusive, indicating the preference item considered.

3 = Method Used for Buckling in P-M-M

4 = Framing type

5 = GammaM0

6 = GammeM1

7 = GammaM2

8 = Consider deflection

9 = DL deflection limit, L/Value

10 = SDL + LL deflection limit, L/Value

11 = LL deflection limit, L/Value

12 = Total deflection limit, L/Value

13 = Total camber limit, L/Value

14 = Pattern live load factor

15 = Demand/capacity ratio limit

16 = Multi-Response Case Design

17 = Behavior Factor, q0

18 = System Overstrength Factor, W

19 = Consider P-Delta

20 = Consider Torsion

21 = Ignore Seismic Code

22 = Ignore Special Seismic Load

23 = Is Doubler Plate Plug-Welded

Value

The value of the considered preference item.

3 = K factor method

1 or "Method A"

2 or "Method B" - Default

3 or "Both"

4 = Framing type

1 or "DCH-MRF"

2 or "DCL-MRF"

3 or "DCH-CBF"

4 or "DCL-CBF"

5 or "DCH-EBF"

6 or "DCL-EBF"

7 or "InvPendulum"

8 or "Non Dissipative" - (Default)

5 = GammaM0

Default = 1.05, Value > 0

6 = GammaM1

Default = 1.05, Value > 0

7 = GammaM2

      Default = 1.25, Value > 0

8 = Consider deflection

1 or "No" - Default

2 or "Yes"

9 = DL deflection limit, L/Value

Default = 0, Value > 0

10 = SDL + LL deflection limit, L/Value

  Default = 0, Value > 0

11 = LL deflection limit, L/Value

  Default = 300, Value > 0

12 = Total deflection limit, L/Value

  Default = 0, Value > 0

13 = Total camber limit, L/Value

  Default = 250, Value > 0

14 = Pattern live load factor

  Default = 0, Value >= 0

15 = Demand/capacity ratio limit

  Default = 1.0, Value > 0

16 = Multi-response case design

  1 or "Envelopes" - (Default)

  2 or "Step-by-step"

  3 or "Last step"

  4 or "Envelopes -- All"

  5 or "Step-by-step -- All"

17 = Behavior Factor, q0

  Default = 1, Value > 0

18 = System Overstrength Factor, W

  Default = 1.0, Value > 0

19 = Consider P-Delta

        1 or "No" - Default

        2 or "Yes"

20 = Consider Torsion

        1 or "No" - Default

        2 or "Yes"

21 = Ignore Seismic Code

        1 or "No" - Default

        2 or "Yes"

22 = Ignore Special Seismic Load

        1 or "No" - Default

        2 or "Yes"

23 = Is Doubler Plate Plug-Welded

  1 or "No" - Default

        2 or "Yes"

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemItalian\_NTC\_2018()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Italian NTC 2018")

   'set preference item
      ret = SapModel.DesignSteel.Italian\_NTC\_2018.SetPreference(4, "DCL-MRF", 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

## See Also

[GetPreference](GetPreference_{NTC_2018}.htm)



## GetOverwrite {Steel NewZealand NZS 3404-1997}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NZS_3404-1997/GetOverwrite_{Steel_NewZealand_NZS_3404-1997}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.NewZealand\_NZS3404\_1997.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 46, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Steel type

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor

20 = Unbraced length ratio, Lateral Torsional Buckling

21 = Effective length factor, Ke Major Braced

22 = Effective length factor, Ke Minor Braced

23 = Effective length factor, Ke Major Sway

24 = Effective length factor, Ke Minor Sway

25 = Twist restraint factor for LTB (kt)

26 = lateral rotation restraint factor (kr)

27 = Load height factor for LTB (kl)

28 = Moment coefficient, Cm Major

29 = Moment coefficient, Cm Minor

30 = Moment modification factor, Alpha\_m

31 = Slender reduction factor, Alpha\_s

32 = Nonsway moment factor, Db Major

33 = Nonsway moment factor, Db Minor

34 = Sway moment factor, Ds Major

35 = Sway moment factor, Ds Minor

36 = Form factor, Kf

37 = Axial capacity correction factor, Kt

38 = Yield stress, Fy

39 = Compressive capacity, Nc

40 = Tensile capacity, Nt

41 = Major bending capacity, Ms33

42 = Minor bending capacity, Ms22

43 = Major bending capacity, Mb33

44 = Major shear capacity, Vu2

45 = Minor shear capacity, Vu3

46 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Moment frame

2 = Braced frame

2 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

3 = Consider deflection

0 = No

Any other value = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]}

14 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

  Value >= 0. [L}

16 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

17 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

20 = Unbraced length ratio, Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

21 = Effective length factor, Ke Major Braced

  Value >= 0; 0 means use program determined value.

22 = Effective length factor, Ke Minor Braced

  Value >= 0; 0 means use program determined value.

23 = Effective length factor, Ke Major Sway

  Value >= 0; 0 means use program determined value.

24 = Effective length factor, Ke Minor Sway

  Value >= 0; 0 means use program determined value.

25 = Twist restraint factor for LTB (kt)

  Value >= 0; 0 means use program determined value.

26 = Lateral rotation restraint factor (kr)

  Value >= 0; 0 means use program determined value.

27 = Load height factor for LTB (kl)

  Value >= 0; 0 means use program determined value.

28 = Moment coefficient, Cm Major

  Value >= 0; 0 means use program determined value.

29 = Moment coefficient, Cm Minor

  Value >= 0; 0 means use program determined value.

30 = Moment modification factor, Alpha\_m

  Value >= 0; 0 means use program determined value.

31 = Slender reduction factor, Alpha\_s

  Value >= 0; 0 means use program determined value.

32 = Nonsway moment factor, Db Major

  Value >= 0; 0 means use program determined value.

33 = Nonsway moment factor, Db Minor

  Value >= 0; 0 means use program determined value.

34 = Sway moment factor, Bs Major

  Value >= 0; 0 means use program determined value.

35 = Sway moment factor, Bs Minor

  Value >= 0; 0 means use program determined value.

36 = Form factor, Kf

  Value >= 0; 0 means use program determined value.

37 = Axial capacity correction factor, Kt

  Value >= 0; 0 means use program determined value.

38 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

39 = Compressive capacity, Nc

  Value >= 0; 0 means use program determined value. [F]

40 = Tensile capacity, Nt

  Value >= 0; 0 means use program determined value. [F]

41 = Major bending capacity, Ms33

  Value >= 0; 0 means use program determined value. [FL]

42 = Minor bending capacity, Ms22

  Value >= 0; 0 means use program determined value. [FL]

43 = Minor bending capacity, Mb33

  Value >= 0; 0 means use program determined value. [FL]

44 = Major shear capacity, Vu2

  Value >= 0; 0 means use program determined value. [F]

45 = Minor shear capacity, Vu3

  Value >= 0; 0 means use program determined value. [F]

46 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemNewZealand\_NZS3404\_1997 ()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("NZS 3404-1997")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.NewZealand\_NZS3404\_1997.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[SetOverwrite](SetOverwrite_{Steel_NewZealand_NZS_3404-1997}.htm)



## GetPreference {Steel NewZealand NZS 3404-1997}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NZS_3404-1997/GetPreference_{Steel_NewZealand_NZS_3404-1997}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.NewZealand\_NZS3404\_1997.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 17, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Structural analysis method

4 = Steel type

5 = Capacity factor, Phi bending

6 = Capacity factor, Phi compression

7 = Capacity factor, Phi tension yielding

8 = Capacity factor, Phi tension fracture

9 = Capacity factor, Phi shear

10 = Consider deflection

11 = DL deflection limit, L/Value

12 = SDL + LL deflection limit, L/Value

13 = LL deflection limit, L/Value

14 = Total load deflection limit, L/Value

15 = Total camber limit, L/Value

16 = Pattern live load factor

17 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Moment frame

2 = Braced frame

3 = Structural analysis method

1 = General 2nd Order

2 = Amplified 1st Order

4 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

5 = Capacity factor, Phi bending

Value > 0

6 = Capacity factor, Phi compression

Value > 0

7 = Capacity factor, Phi tension yielding

Value > 0

8 = Capacity factor, Phi tension fracture

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Consider deflection

  0 = No

  Any other value = Yes

11 = DL deflection limit, L/Value

  Value > 0

12 = SDL + LL deflection limit, L/Value

  Value > 0

13 = LL deflection limit, L/Value

  Value > 0

14 = Total load deflection limit, L/Value

  Value > 0

15 = Total camber limit, L/Value

  Value > 0

16 = Pattern live load factor

  Value >= 0

17 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved, otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemNewZealand\_NZS3404\_1997 ()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("NZS 3404-1997")

   'get preference item
      ret = SapModel.DesignSteel.NewZealand\_NZS3404\_1997.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_NewZealand_NZS_3404-1997}.htm)



## SetOverwrite {Steel NewZealand NZS 3404-1997}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NZS_3404-1997/SetOverwrite_{Steel_NewZealand_NZS_3404-1997}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.NewZealand\_NZS3404\_1997.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 46, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Steel type

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor

20 = Unbraced length ratio, Lateral Torsional Buckling

21 = Effective length factor, Ke Major Braced

22 = Effective length factor, Ke Minor Braced

23 = Effective length factor, Ke Major Sway

24 = Effective length factor, Ke Minor Sway

25 = Twist restraint factor for LTB (kt)

26 = lateral rotation restraint factor (kr)

27 = Load height factor for LTB (kl)

28 = Moment coefficient, Cm Major

29 = Moment coefficient, Cm Minor

30 = Moment modification factor, Alpha\_m

31 = Slender reduction factor, Alpha\_s

32 = Nonsway moment factor, Db Major

33 = Nonsway moment factor, Db Minor

34 = Sway moment factor, Ds Major

35 = Sway moment factor, Ds Minor

36 = Form factor, Kf

37 = Axial capacity correction factor, Kt

38 = Yield stress, Fy

39 = Compressive capacity, Nc

40 = Tensile capacity, Nt

41 = Major bending capacity, Ms33

42 = Minor bending capacity, Ms22

43 = Major bending capacity, Mb33

44 = Major shear capacity, Vu2

45 = Minor shear capacity, Vu3

46 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Moment frame

2 = Braced frame

2 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

3 = Consider deflection

0 = No

Any other value = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]}

14 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

  Value >= 0. [L}

16 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

17 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

20 = Unbraced length ratio, Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

21 = Effective length factor, Ke Major Braced

  Value >= 0; 0 means use program determined value.

22 = Effective length factor, Ke Minor Braced

  Value >= 0; 0 means use program determined value.

23 = Effective length factor, Ke Major Sway

  Value >= 0; 0 means use program determined value.

24 = Effective length factor, Ke Minor Sway

  Value >= 0; 0 means use program determined value.

25 = Twist restraint factor for LTB (kt)

  Value >= 0; 0 means use program determined value.

26 = Lateral rotation restraint factor (kr)

  Value >= 0; 0 means use program determined value.

27 = Load height factor for LTB (kl)

  Value >= 0; 0 means use program determined value.

28 = Moment coefficient, Cm Major

  Value >= 0; 0 means use program determined value.

29 = Moment coefficient, Cm Minor

  Value >= 0; 0 means use program determined value.

30 = Moment modification factor, Alpha\_m

  Value >= 0; 0 means use program determined value.

31 = Slender reduction factor, Alpha\_s

  Value >= 0; 0 means use program determined value.

32 = Nonsway moment factor, Db Major

  Value >= 0; 0 means use program determined value.

33 = Nonsway moment factor, Db Minor

  Value >= 0; 0 means use program determined value.

34 = Sway moment factor, Bs Major

  Value >= 0; 0 means use program determined value.

35 = Sway moment factor, Bs Minor

  Value >= 0; 0 means use program determined value.

36 = Form factor, Kf

  Value >= 0; 0 means use program determined value.

37 = Axial capacity correction factor, Kt

  Value >= 0; 0 means use program determined value.

38 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

39 = Compressive capacity, Nc

  Value >= 0; 0 means use program determined value. [F]

40 = Tensile capacity, Nt

  Value >= 0; 0 means use program determined value. [F]

41 = Major bending capacity, Ms33

  Value >= 0; 0 means use program determined value. [FL]

42 = Minor bending capacity, Ms22

  Value >= 0; 0 means use program determined value. [FL]

43 = Minor bending capacity, Mb33

  Value >= 0; 0 means use program determined value. [FL]

44 = Major shear capacity, Vu2

  Value >= 0; 0 means use program determined value. [F]

45 = Minor shear capacity, Vu3

  Value >= 0; 0 means use program determined value. [F]

46 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAustralian\_AS4100\_1998 ()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("NZS 3404-1997")

   'set overwrite item
      ret = SapModel.DesignSteel.NewZealand\_NZS3404\_1997.SetOverwrite("8", 1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[GetOverwrite](GetOverwrite_{Steel_NewZealand_NZS_3404-1997}.htm)



## SetPreference {Steel NewZealand NZS 3404-1997}

*Source file: `SAP2000_API_Fuctions/Design/Steel/NZS_3404-1997/SetPreference_{Steel_NewZealand_NZS_3404-1997}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.NewZealand\_NZS3404\_1997.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 17, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Structural analysis method

4 = Steel type

5 = Capacity factor, Phi bending

6 = Capacity factor, Phi compression

7 = Capacity factor, Phi tension yielding

8 = Capacity factor, Phi tension fracture

9 = Capacity factor, Phi shear

10 = Consider deflection

11 = DL deflection limit, L/Value

12 = SDL + LL deflection limit, L/Value

13 = LL deflection limit, L/Value

14 = Total load deflection limit, L/Value

15 = Total camber limit, L/Value

16 = Pattern live load factor

17 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Multi-response case design

1 = Envelopes

2 = Step-by step

3 = Last step

4 = Envelopes - All

5 = Step-by step - All

2 = Framing type

1 = Moment frame

2 = Braced frame

3 = Structural analysis method

1 = General 2nd Order

2 = Amplified 1st Order

4 = Steel type

1 = Hot rolled

2 = Hot finished

3 = Cold form

4 = Stress relieved

5 = Lightly welded

6 = Heavily welded

5 = Capacity factor, Phi bending

Value > 0

6 = Capacity factor, Phi compression

Value > 0

7 = Capacity factor, Phi tension yielding

Value > 0

8 = Capacity factor, Phi tension fracture

Value > 0

9 = Capacity factor, Phi shear

Value > 0

10 = Consider deflection

  0 = No

  Any other value = Yes

11 = DL deflection limit, L/Value

  Value > 0

12 = SDL + LL deflection limit, L/Value

  Value > 0

13 = LL deflection limit, L/Value

  Value > 0

14 = Total load deflection limit, L/Value

  Value > 0

15 = Total camber limit, L/Value

  Value > 0

16 = Pattern live load factor

  Value >= 0

17 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set, otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemNewZealand\_NZS3404\_1997 ()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("NZS 3404-1997")

   'set preference item
      ret = SapModel.DesignSteel.NewZealand\_NZS3404\_1997.SetPreference(1, 7)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_NewZealand_NZS_3404-1997}.htm)



## GetOverwrite (Steel Norsok N-004)

*Source file: `SAP2000_API_Fuctions/Design/Steel/Norsok_N-004/GetOverwrite_(Steel_Norosk_N-004).htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Norsok\_N004.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 36, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, k Major

22 = Moment coefficient, k Minor

23 = Bending coefficient, C1

24 = Moment coefficient, kzy

25 = Moment coefficient, kyz

26 = Pressure equalized

27 = External pressure

28 = Yield stress, Fy

29 = Compressive capacity, Nc.Rd

30 = Tensile capacity, Nt.Rd

31 = Major bending capacity, Mc3.Rd

32 = Minor bending capacity, Mc2.Rd

33 = Buckling resistance moment, Mb.Rd

34 = Major shear capacity, V2.Rd

35 = Minor shear capacity, V3.RD

36 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

  Value >= 0. [L]

15 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

16 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

  Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

  Value >= 0; 0 means use program determined value.

21 = Moment coefficient, k Major

  Value >= 0; 0 means use program determined value.

22 = Moment coefficient, k Minor

  Value >= 0; 0 means use program determined value.

23 = Bending coefficient, C1

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, kzy

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, kyz

  Value >= 0; 0 means use program determined value.

26 = Pressure equalized

  0 = Program Determined

  1 = No

  2 = Yes

27 = External pressure

  Any value OK; Positive generates hoop compression and negative generates hoop tension. [F/L2]

28 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

29 = Compressive capacity, Nc.Rd

  Value >= 0; 0 means use program determined value. [F]

30 = Tensile capacity, Nt.Rd

  Value >= 0; 0 means use program determined value. [F]

31 = Major bending capacity, Mc3.Rd

  Value >= 0; 0 means use program determined value. [FL]

32 = Minor bending capacity, Mc2.Rd

  Value >= 0; 0 means use program determined value. [FL]

33 = Buckling resistance moment, Mb.Rd

  Value >= 0; 0 means use program determined value. [FL]

34 = Major shear capacity, V2.Rd

  Value >= 0; 0 means use program determined value. [F]

35 = Minor shear capacity, V3.RD

  Value >= 0; 0 means use program determined value. [F]

36 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemNorsok\_N004()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Norsok N-004")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Norsok\_N004.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.1.0.

## See Also

[SetOverwrite](SetOverwrite_(Steel_Norosk_N-004).htm)



## GetPreference (Steel Norsok N-004)

*Source file: `SAP2000_API_Fuctions/Design/Steel/Norsok_N-004/GetPreference_(Steel_Norosk_N-004).htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Norsok\_N004.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 16, inclusive, indicating the preference item considered.

1 = Combos equation

2 = K factor method

3 = Pressure interaction method

4 = Framing type

5 = GammaM0

6 = GammeM1

7 = GammaM2

8 = Consider deflection

9 = DL deflection limit, L/Value

10 = SDL + LL deflection limit, L/Value

11 = LL deflection limit, L/Value

12 = Total deflection limit, L/Value

13 = Total camber limit, L/Value

14 = Pattern live load factor

15 = Demand/capacity ratio limit

16 = Multi-response case design

Value

The value of the considered preference item.

1 = Combos equation

      1 = 1 = Eq. 6.10

      2 = Max of Eqs. 6.10a and 6.10b

2 = K factor method

      1 = Method 1 (Annex A)

      2 = Method 2 (Annex B)

3 = Pressure interaction method

      1 = Method A

      2 = Method B

4 = Framing type

1 = Moment Frame

2 = Braced Frame

5 = GammaM0

 Value > 0

6 = GammeM1

 Value > 0

7 = GammeM2

      Value > 0

8 = Consider deflection

0 = No

Any other value = Yes

9 = DL deflection limit, L/Value

Value > 0

10 = SDL + LL deflection limit, L/Value

  Value > 0

11 = LL deflection limit, L/Value

  Value > 0

12 = Total deflection limit, L/Value

  Value > 0

13 = Total camber limit, L/Value

  Value > 0

14 = Pattern live load factor

  Value >= 0

15 = Demand/capacity ratio limit

  Value > 0

16 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemNorsok\_N004()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Norsok N-004")

   'get preference item
      ret = SapModel.DesignSteel.Norsok\_N004.GetPreference(4, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.1.0.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_(Steel_Norosk_N-004).htm)



## SetOverwrite (Steel Norsok N-004)

*Source file: `SAP2000_API_Fuctions/Design/Steel/Norsok_N-004/SetOverwrite_(Steel_Norosk_N-004).htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Norsok\_N004.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 36, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, k Major

22 = Moment coefficient, k Minor

23 = Bending coefficient, C1

24 = Moment coefficient, kzy

25 = Moment coefficient, kyz

26 = Pressure equalized

27 = External pressure

28 = Yield stress, Fy

29 = Compressive capacity, Nc.Rd

30 = Tensile capacity, Nt.Rd

31 = Major bending capacity, Mc3.Rd

32 = Minor bending capacity, Mc2.Rd

33 = Buckling resistance moment, Mb.Rd

34 = Major shear capacity, V2.Rd

35 = Minor shear capacity, V3.RD

36 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

  Value >= 0. [L]

15 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

16 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

  Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

  Value >= 0; 0 means use program determined value.

21 = Moment coefficient, k Major

  Value >= 0; 0 means use program determined value.

22 = Moment coefficient, k Minor

  Value >= 0; 0 means use program determined value.

23 = Bending coefficient, C1

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, kzy

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, kyz

  Value >= 0; 0 means use program determined value.

26 = Pressure equalized

 0 = Program Determined

 1 = No

 2 = Yes

27 = External pressure

  Any value OK; Positive generates hoop compression and negative generates hoop tension. [F/L2]

28 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

29 = Compressive capacity, Nc.Rd

  Value >= 0; 0 means use program determined value. [F]

30 = Tensile capacity, Nt.Rd

  Value >= 0; 0 means use program determined value. [F]

31 = Major bending capacity, Mc3.Rd

  Value >= 0; 0 means use program determined value. [FL]

32 = Minor bending capacity, Mc2.Rd

  Value >= 0; 0 means use program determined value. [FL]

33 = Buckling resistance moment, Mb.Rd

  Value >= 0; 0 means use program determined value. [FL]

34 = Major shear capacity, V2.Rd

  Value >= 0; 0 means use program determined value. [F]

35 = Minor shear capacity, V3.RD

  Value >= 0; 0 means use program determined value. [F]

36 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemNorsok\_N004()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Norsok N-004")

   'set overwrite item
      ret = SapModel.DesignSteel.Norsok\_N004.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.1.0.

## See Also

[GetOverwrite](GetOverwrite_(Steel_Norosk_N-004).htm)



## SetPreference (Steel Norsok N-004)

*Source file: `SAP2000_API_Fuctions/Design/Steel/Norsok_N-004/SetPreference_(Steel_Norosk_N-004).htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Norsok\_N004.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 16, inclusive, indicating the preference item considered.

1 = Combos equation

2 = K factor method

3 = Pressure interaction method

4 = Framing type

5 = GammaM0

6 = GammeM1

7 = GammaM2

8 = Consider deflection

9 = DL deflection limit, L/Value

10 = SDL + LL deflection limit, L/Value

11 = LL deflection limit, L/Value

12 = Total deflection limit, L/Value

13 = Total camber limit, L/Value

14 = Pattern live load factor

15 = Demand/capacity ratio limit

16 = Multi-response case design

Value

The value of the considered preference item.

1 = Combos equation

      1 = 1 = Eq. 6.10

      2 = Max of Eqs. 6.10a and 6.10b

2 = K factor method

      1 = Method 1 (Annex A)

      2 = Method 2 (Annex B)

3 = Pressure interaction method

     1 = Method A

     2 = Method B

4 = Framing type

1 = Moment Frame

2 = Braced Frame

5 = GammaM0

Value > 0

6 = GammeM1

 Value > 0

7 = GammeM2

      Value > 0

8 = Consider deflection

0 = No

Any other value = Yes

9 = DL deflection limit, L/Value

Value > 0

10 = SDL + LL deflection limit, L/Value

  Value > 0

11 = LL deflection limit, L/Value

  Value > 0

12 = Total deflection limit, L/Value

  Value > 0

13 = Total camber limit, L/Value

  Value > 0

14 = Pattern live load factor

  Value >= 0

15 = Demand/capacity ratio limit

  Value > 0

16 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemNorsok\_N004()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Norsok N-004")

   'set preference item
      ret = SapModel.DesignSteel.Norsok\_N004.SetPreference(4, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 14.1.0.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_(Steel_Norosk_N-004).htm)



## SetPreference (Steel Norsok N-0042013)

*Source file: `SAP2000_API_Fuctions/Design/Steel/Norsok_N-004_2013/GetOverwrite_(Steel_Norsok_N-0042013).htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.Norsok\_N0042013.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 16, inclusive, indicating the preference item considered.

1 = Combos equation

2 = K factor method

3 = Pressure interaction method

4 = Framing type

5 = GammaM0

6 = GammeM1

7 = GammaM2

8 = Consider deflection

9 = DL deflection limit, L/Value

10 = SDL + LL deflection limit, L/Value

11 = LL deflection limit, L/Value

12 = Total deflection limit, L/Value

13 = Total camber limit, L/Value

14 = Pattern live load factor

15 = Demand/capacity ratio limit

16 = Multi-response case design

Value

The value of the considered preference item.

1 = Combos equation

      1 = 1 = Eq. 6.10

      2 = Max of Eqs. 6.10a and 6.10b

2 = K factor method

      1 = Method 1 (Annex A)

      2 = Method 2 (Annex B)

3 = Pressure interaction method

     1 = Method A

     2 = Method B

4 = Framing type

1 = Moment Frame

2 = Braced Frame

5 = GammaM0

Value > 0

6 = GammeM1

 Value > 0

7 = GammeM2

      Value > 0

8 = Consider deflection

0 = No

Any other value = Yes

9 = DL deflection limit, L/Value

Value > 0

10 = SDL + LL deflection limit, L/Value

  Value > 0

11 = LL deflection limit, L/Value

  Value > 0

12 = Total deflection limit, L/Value

  Value > 0

13 = Total camber limit, L/Value

  Value > 0

14 = Pattern live load factor

  Value >= 0

15 = Demand/capacity ratio limit

  Value > 0

16 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemNorsok\_N0042013()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Norsok N-004 2013")

   'set preference item
      ret = SapModel.DesignSteel.Norsok\_N0042013.SetPreference(4, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 16.1.0.

## See Also

[GetPreference](../Norsok_N-004/GetPreference_(Steel_Norosk_N-004).htm)



## GetOverwrite (Steel Norsok N-0042013)

*Source file: `SAP2000_API_Fuctions/Design/Steel/Norsok_N-004_2013/GetOverwrite_(Steel_Norsok_N-004_2013.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Norsok\_N0042013.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 36, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, k Major

22 = Moment coefficient, k Minor

23 = Bending coefficient, C1

24 = Moment coefficient, kzy

25 = Moment coefficient, kyz

26 = Pressure equalized

27 = External pressure

28 = Yield stress, Fy

29 = Compressive capacity, Nc.Rd

30 = Tensile capacity, Nt.Rd

31 = Major bending capacity, Mc3.Rd

32 = Minor bending capacity, Mc2.Rd

33 = Buckling resistance moment, Mb.Rd

34 = Major shear capacity, V2.Rd

35 = Minor shear capacity, V3.RD

36 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

  Value >= 0. [L]

15 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

16 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

  Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

  Value >= 0; 0 means use program determined value.

21 = Moment coefficient, k Major

  Value >= 0; 0 means use program determined value.

22 = Moment coefficient, k Minor

  Value >= 0; 0 means use program determined value.

23 = Bending coefficient, C1

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, kzy

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, kyz

  Value >= 0; 0 means use program determined value.

26 = Pressure equalized

  0 = Program Determined

  1 = No

  2 = Yes

27 = External pressure

  Any value OK; Positive generates hoop compression and negative generates hoop tension. [F/L2]

28 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

29 = Compressive capacity, Nc.Rd

  Value >= 0; 0 means use program determined value. [F]

30 = Tensile capacity, Nt.Rd

  Value >= 0; 0 means use program determined value. [F]

31 = Major bending capacity, Mc3.Rd

  Value >= 0; 0 means use program determined value. [FL]

32 = Minor bending capacity, Mc2.Rd

  Value >= 0; 0 means use program determined value. [FL]

33 = Buckling resistance moment, Mb.Rd

  Value >= 0; 0 means use program determined value. [FL]

34 = Major shear capacity, V2.Rd

  Value >= 0; 0 means use program determined value. [F]

35 = Minor shear capacity, V3.RD

  Value >= 0; 0 means use program determined value. [F]

36 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemNorsok\_N0042013()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Norsok N-004 2013")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.Norsok\_N0042013.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 16.1.0.

## See Also

[SetOverwrite](../Norsok_N-004/SetOverwrite_(Steel_Norosk_N-004).htm)



## GetPreference (Steel Norsok N-0042013)

*Source file: `SAP2000_API_Fuctions/Design/Steel/Norsok_N-004_2013/GetPreference_(Steel_Norsok_N-0042013.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.Norsok\_N0042013.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 16, inclusive, indicating the preference item considered.

1 = Combos equation

2 = K factor method

3 = Pressure interaction method

4 = Framing type

5 = GammaM0

6 = GammeM1

7 = GammaM2

8 = Consider deflection

9 = DL deflection limit, L/Value

10 = SDL + LL deflection limit, L/Value

11 = LL deflection limit, L/Value

12 = Total deflection limit, L/Value

13 = Total camber limit, L/Value

14 = Pattern live load factor

15 = Demand/capacity ratio limit

16 = Multi-response case design

Value

The value of the considered preference item.

1 = Combos equation

      1 = 1 = Eq. 6.10

      2 = Max of Eqs. 6.10a and 6.10b

2 = K factor method

      1 = Method 1 (Annex A)

      2 = Method 2 (Annex B)

3 = Pressure interaction method

      1 = Method A

      2 = Method B

4 = Framing type

1 = Moment Frame

2 = Braced Frame

5 = GammaM0

 Value > 0

6 = GammeM1

 Value > 0

7 = GammeM2

      Value > 0

8 = Consider deflection

0 = No

Any other value = Yes

9 = DL deflection limit, L/Value

Value > 0

10 = SDL + LL deflection limit, L/Value

  Value > 0

11 = LL deflection limit, L/Value

  Value > 0

12 = Total deflection limit, L/Value

  Value > 0

13 = Total camber limit, L/Value

  Value > 0

14 = Pattern live load factor

  Value >= 0

15 = Demand/capacity ratio limit

  Value > 0

16 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemNorsok\_N0042013()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Norsok N-004 2013")

   'get preference item
      ret = SapModel.DesignSteel.Norsok\_N0042013.GetPreference(4, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 16.1.0.

## See Also

[SetPreference](../Norsok_N-004/SetPreference_(Steel_Norosk_N-004).htm)



## SetOverwrite (Steel Norsok N-0042013)

*Source file: `SAP2000_API_Fuctions/Design/Steel/Norsok_N-004_2013/SetOverwrite_(Steel_Norsok_N-0042013).htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.Norsok\_N0042013.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 36, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Consider deflection

3 = Deflection check type

4 = DL deflection limit, L/Value

5 = SDL + LL deflection limit, L/Value

6 = LL deflection limit, L/Value

7 = Total load deflection limit, L/Value

8 = Total camber limit, L/Value

9 = DL deflection limit, absolute

10 = SDL + LL deflection limit, absolute

11 = LL deflection limit, absolute

12 = Total load deflection limit, absolute

13 = Total camber limit, absolute

14 = Specified camber

15 = Net area to total area ratio

16 = Live load reduction factor

17 = Unbraced length ratio, Major

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

19 = Effective length factor, K Major

20 = Effective length factor, K Minor

21 = Moment coefficient, k Major

22 = Moment coefficient, k Minor

23 = Bending coefficient, C1

24 = Moment coefficient, kzy

25 = Moment coefficient, kyz

26 = Pressure equalized

27 = External pressure

28 = Yield stress, Fy

29 = Compressive capacity, Nc.Rd

30 = Tensile capacity, Nt.Rd

31 = Major bending capacity, Mc3.Rd

32 = Minor bending capacity, Mc2.Rd

33 = Buckling resistance moment, Mb.Rd

34 = Major shear capacity, V2.Rd

35 = Minor shear capacity, V3.RD

36 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = As specified in preferences

1 = Moment Frame

2 = Braced Frame

2 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

3 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

4 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

5 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

9 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

10 = SDL + LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

11 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

12 = Total load deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

13 = Total camber limit, absolute

  Value >= 0; 0 means no check for this item. [L]

14 = Specified camber

  Value >= 0. [L]

15 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

16 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

17 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Minor Lateral Torsional Buckling

  Value >= 0; 0 means use program determined value.

19 = Effective length factor, K Major

  Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Minor

  Value >= 0; 0 means use program determined value.

21 = Moment coefficient, k Major

  Value >= 0; 0 means use program determined value.

22 = Moment coefficient, k Minor

  Value >= 0; 0 means use program determined value.

23 = Bending coefficient, C1

  Value >= 0; 0 means use program determined value.

24 = Moment coefficient, kzy

  Value >= 0; 0 means use program determined value.

25 = Moment coefficient, kyz

  Value >= 0; 0 means use program determined value.

26 = Pressure equalized

 0 = Program Determined

 1 = No

 2 = Yes

27 = External pressure

  Any value OK; Positive generates hoop compression and negative generates hoop tension. [F/L2]

28 = Yield stress, Fy

  Value >= 0; 0 means use program determined value. [F/L2]

29 = Compressive capacity, Nc.Rd

  Value >= 0; 0 means use program determined value. [F]

30 = Tensile capacity, Nt.Rd

  Value >= 0; 0 means use program determined value. [F]

31 = Major bending capacity, Mc3.Rd

  Value >= 0; 0 means use program determined value. [FL]

32 = Minor bending capacity, Mc2.Rd

  Value >= 0; 0 means use program determined value. [FL]

33 = Buckling resistance moment, Mb.Rd

  Value >= 0; 0 means use program determined value. [FL]

34 = Major shear capacity, V2.Rd

  Value >= 0; 0 means use program determined value. [F]

35 = Minor shear capacity, V3.RD

  Value >= 0; 0 means use program determined value. [F]

36 = Demand/capacity ratio limit

  Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemNorsok\_N0042013()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("Norsok N-004 2013")

   'set overwrite item
      ret = SapModel.DesignSteel.Norsok\_N0042013.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 16.1.0.

## See Also

[GetOverwrite](../Norsok_N-004/GetOverwrite_(Steel_Norosk_N-004).htm)ype topic text here.



## ResetOverwrites {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/ResetOverwrites_{Steel}.htm`*

# ResetOverwrites

## Syntax

SapObject.SapModel.DesignSteel.ResetOverwrites

## VB6 Procedure

Function ResetOverwrites() As Long

## Parameters

None

## Remarks

This function resets all steel frame design overwrites to default values.

The function returns zero if the overwrites are successfully reset; otherwise it returns a nonzero value.

The function will fail if no steel frame objects are present.

## VBA Example

Sub ResetSteelDesignOverwrites()
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

   'reset steel design overwrites
      ret = SapModel.DesignSteel.ResetOverwrites

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## GetOverwrite {SP_16-13330-2011}

*Source file: `SAP2000_API_Fuctions/Design/Steel/SP_16-13330-2011/GetOverwrite_{SP63_16-13330-2011}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.SP\_16\_13330\_2011.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 37, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Section Class

3 = Service Factor, GammaC

4 = Service Factor, GammaU

5 = Factor for L-Shapes , GammaC1

6 = Column buckling curve major

7 = Column buckling curve minor

8 = Is rolled section?

9 = Is beam top loaded?

10 = Consider Deflection

11 = Deflection check type

12 = DL deflection limit, L/Value

13 = SDL+LL deflection limit, L/Value

14 = LL deflection limit, L/Value

15 = Total deflection limit, L/Value

16 = Total-camber limit, L/Value

17 = DL deflection limit, absolute

18 = SDL+LL deflection limit, absolute

19 = LL deflection limit, absolute

20 = Total deflection limit, absolute

21 = Total-camber deflection limit, absolute

22 = Specified camber

23 = Net area to total area ratio

24 = Live load reduction factor

25 = Unbraced length ratio, Major

26 = Unbraced length ratio, Minor

27 = Unbraced length ratio, LTB

28 = Effective length factor, K1 Major

29 = Effective length factor, K1 Minor

30 = Effective length factor, K2 Major

31 = Effective length factor, K2 Minor

32 = Effective length factor, LTB

33 = Characteristic strength, Ryn

34 = Design yield strength, Ry

35 = Design fracture strength, Ru

36 = Design shear strength, Rs

37 = Demand/capacity ratio, limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Section Class

0 = Program Determined

1 = Class 1

2 = Class 2

3 = Class 3

4 = Class 4

3 = Service Factor, GammaC

Value >= 0; 0 means use program determined value.

4 = Service Factor, GammaU

Value >= 0; 0 means use program determined value.

5 = Factor for L-Shapes , GammaC1

Value >= 0; 0 means use program determined value.

6 = Column buckling curve major

0 = Program Determined

1 = a

2 = b

3 = c

7 = Column buckling curve minor

0 = Program Determined

1 = a

2 = b

3 = c

8 = Is rolled section?

0 = Program Determined

1 = No

2 = Yes

9 = Is beam top loaded?

0 = Program Determined

1 = No

2 = Yes

10 = Consider Deflection

0 = Program Determined

1 = No

2 = Yes

11 = Deflection check type

0 = Program Determined

1 = Ratio

2 = Absolute

3 = Both

12 = DL deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

13 = SDL+LL deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

14 = LL deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

15 = Total deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

16 = Total-camber limit, L/Value

  Value >= 0; 0 means no check for this item.

17 = DL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

18 = SDL+LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

19 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

20 = Total deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

21 = Total-camber deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

22 = Specified camber

  Value >= 0. [L]

23 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

24 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

25 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

26 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

27 = Unbraced length ratio, LTB

  Value >= 0; 0 means use program determined value.

28 = Effective length factor, K1 Major

  Value >= 0; 0 means use program determined value.

29 = Effective length factor, K1 Minor

  Value >= 0; 0 means use program determined value.

30 = Effective length factor, K2 Major

  Value >= 0; 0 means use program determined value.

31 = Effective length factor, K2 Minor

  Value >= 0; 0 means use program determined value.

32 = Effective length factor, LTB

  Value >= 0; 0 means use program determined value.

33 = Characteristic strength, Ryn

  Value >= 0; 0 means use program determined value. [F/L2]

34 = Design yield strength, Ry

  Value >= 0; 0 means use program determined value. [F/L2]

35 = Design fracture strength, Ru

Value >= 0; 0 means use program determined value. [F/L2]

36 = Design shear strength, Rs

Value >= 0; 0 means use program determined value. [F/L2]

37 = Demand/capacity ratio, limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemSP16\_13330\_2011()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("SP 16.13330.2011")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.SP16\_13330\_2011.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

## See Also

[SetOverwrite](SetOverwrite_{SP_16-13330-2011}.htm)



## GetPreference {SP_16-13330-2011}

*Source file: `SAP2000_API_Fuctions/Design/Steel/SP_16-13330-2011/GetPreference_{SP_16-13330-2011}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.SP\_16\_13330\_2011.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 15, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Section class

4 = GammaM

5 = GammaC

6 = GammaU

7 = GammaC1

8 = Consider deflection

9 = DL deflection limit, L/Value

10 = SDL + LL deflection limit, L/Value

11 = LL deflection limit, L/Value

12 = Total load deflection limit, L/Value

13 = Total camber limit, L/Value

14 = Pattern live load factor

15 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Multi-response case design

   1 = Envelopes

   2 = Step-by-step

   3 = Last step

   4 = Envelopes -- All

   5 = Step-by-step -- All

2 = Framing type

   1 = Moment frame

   2 = Braced frame

3 = Section class

   1 = Class 1

   2 = Class 2

   3 = Class 3

   4 = Class 4

4 = GammaM

Value > 0

5 = GammaC

Value > 0

6 = GammaU

Value > 0

7 = GammaC1

      Value > 0

8 = Consider deflection

0 = No

Any other value = Yes

9 = DL deflection limit, L/Value

Value > 0

10 = SDL + LL deflection limit, L/Value

  Value > 0

11 = LL deflection limit, L/Value

  Value > 0

12 = Total deflection limit, L/Value

  Value > 0

13 = Total camber limit, L/Value

  Value > 0

14 = Pattern live load factor

  Value >= 0

15 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemSP\_16\_13330\_2011()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("SP 16.13330.2011")

   'get preference item
      ret = SapModel.DesignSteel.SP\_16\_13330\_2011.GetPreference(4, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.1.0.

## See Also

[SetPreference](SetPreference_{SP_16-13330-2011}.htm)



## SetOverwrite {SP_16-13330-2011}

*Source file: `SAP2000_API_Fuctions/Design/Steel/SP_16-13330-2011/SetOverwrite_{SP_16-13330-2011}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.SP\_16\_13330\_2011.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByVal ItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 37, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Section Class

3 = Service Factor, GammaC

4 = Service Factor, GammaU

5 = Factor for L-Shapes , GammaC1

6 = Column buckling curve major

7 = Column buckling curve minor

8 = Is rolled section?

9 = Is beam top loaded?

10 = Consider Deflection

11 = Deflection check type

12 = DL deflection limit, L/Value

13 = SDL+LL deflection limit, L/Value

14 = LL deflection limit, L/Value

15 = Total deflection limit, L/Value

16 = Total-camber limit, L/Value

17 = DL deflection limit, absolute

18 = SDL+LL deflection limit, absolute

19 = LL deflection limit, absolute

20 = Total deflection limit, absolute

21 = Total-camber deflection limit, absolute

22 = Specified camber

23 = Net area to total area ratio

24 = Live load reduction factor

25 = Unbraced length ratio, Major

26 = Unbraced length ratio, Minor

27 = Unbraced length ratio, LTB

28 = Effective length factor, K1 Major

29 = Effective length factor, K1 Minor

30 = Effective length factor, K2 Major

31 = Effective length factor, K2 Minor

32 = Effective length factor, LTB

33 = Characteristic strength, Ryn

34 = Design yield strength, Ry

35 = Design fracture strength, Ru

36 = Design shear strength, Rs

37 = Demand/capacity ratio, limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Moment Frame

2 = Braced Frame

2 = Section Class

0 = Program Determined

1 = Class 1

2 = Class 2

3 = Class 3

4 = Class 4

3 = Service Factor, GammaC

Value >= 0; 0 means use program determined value.

4 = Service Factor, GammaU

Value >= 0; 0 means use program determined value.

5 = Factor for L-Shapes , GammaC1

Value >= 0; 0 means use program determined value.

6 = Column buckling curve major

0 = Program Determined

1 = a

2 = b

3 = c

7 = Column buckling curve minor

0 = Program Determined

1 = a

2 = b

3 = c

8 = Is rolled section?

0 = Program Determined

1 = No

2 = Yes

9 = Is beam top loaded?

0 = Program Determined

1 = No

2 = Yes

10 = Consider Deflection

0 = Program Determined

1 = No

2 = Yes

11 = Deflection check type

0 = Program Determined

1 = Ratio

2 = Absolute

3 = Both

12 = DL deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

13 = SDL+LL deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

14 = LL deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

15 = Total deflection limit, L/Value

  Value >= 0; 0 means no check for this item.

16 = Total-camber limit, L/Value

  Value >= 0; 0 means no check for this item.

17 = DL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

18 = SDL+LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

19 = LL deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

20 = Total deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

21 = Total-camber deflection limit, absolute

  Value >= 0; 0 means no check for this item. [L]

22 = Specified camber

  Value >= 0. [L]

23 = Net area to total area ratio

  Value >= 0; 0 means use program default value.

24 = Live load reduction factor

  Value >= 0; 0 means use program determined value.

25 = Unbraced length ratio, Major

  Value >= 0; 0 means use program determined value.

26 = Unbraced length ratio, Minor

  Value >= 0; 0 means use program determined value.

27 = Unbraced length ratio, LTB

  Value >= 0; 0 means use program determined value.

28 = Effective length factor, K1 Major

  Value >= 0; 0 means use program determined value.

29 = Effective length factor, K1 Minor

  Value >= 0; 0 means use program determined value.

30 = Effective length factor, K2 Major

  Value >= 0; 0 means use program determined value.

31 = Effective length factor, K2 Minor

  Value >= 0; 0 means use program determined value.

32 = Effective length factor, LTB

  Value >= 0; 0 means use program determined value.

33 = Characteristic strength, Ryn

  Value >= 0; 0 means use program determined value. [F/L2]

34 = Design yield strength, Ry

  Value >= 0; 0 means use program determined value. [F/L2]

35 = Design fracture strength, Ru

Value >= 0; 0 means use program determined value. [F/L2]

36 = Design shear strength, Rs

Value >= 0; 0 means use program determined value. [F/L2]

37 = Demand/capacity ratio, limit

Value >= 0; 0 means use program determined value.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignment is made to the frame object specified by the Name item.

If this item is Group, the assignment is made to all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignment is made to all selected frame objects and the Name item is ignored.

## Remarks

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise, it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemSP16\_13330\_2011()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("SP 16.13330.2011")

   'set overwrite item
      ret = SapModel.DesignSteel.SP16\_13330\_2011.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in v20.1.0.

## See Also

[GetOverwrite](GetOverwrite_{SP63_16-13330-2011}.htm)



## SetPreference {SP_16-13330-2011}

*Source file: `SAP2000_API_Fuctions/Design/Steel/SP_16-13330-2011/SetPreference_{SP_16-13330-2011}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.SP\_16\_13330\_2011.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 15, inclusive, indicating the preference item considered.

1 = Multi-response case design

2 = Framing type

3 = Section class

4 = GammaM

5 = GammaC

6 = GammaU

7 = GammaC1

8 = Consider deflection

9 = DL deflection limit, L/Value

10 = SDL + LL deflection limit, L/Value

11 = LL deflection limit, L/Value

12 = Total load deflection limit, L/Value

13 = Total camber limit, L/Value

14 = Pattern live load factor

15 = Demand/capacity ratio limit

Value

The value of the considered preference item.

1 = Multi-response case design

   1 = Envelopes

   2 = Step-by-step

   3 = Last step

   4 = Envelopes -- All

   5 = Step-by-step -- All

2 = Framing type

   1 = Moment frame

   2 = Braced frame

3 = Section class

   1 = Class 1

   2 = Class 2

   3 = Class 3

   4 = Class 4

4 = GammaM

Value > 0

5 = GammaC

Value > 0

6 = GammaU

Value > 0

7 = GammaC1

      Value > 0

8 = Consider deflection

0 = No

Any other value = Yes

9 = DL deflection limit, L/Value

Value > 0

10 = SDL + LL deflection limit, L/Value

  Value > 0

11 = LL deflection limit, L/Value

  Value > 0

12 = Total deflection limit, L/Value

  Value > 0

13 = Total camber limit, L/Value

  Value > 0

14 = Pattern live load factor

  Value >= 0

15 = Demand/capacity ratio limit

  Value > 0

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise, it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemSP\_16\_13330\_2011()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("SP 16.13330.2011")

   'set preference item
      ret = SapModel.DesignSteel.SP\_16\_13330\_2011.SetPreference(4, 1.1)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 20.1.0.

## See Also

[GetPreference](GetPreference_{SP_16-13330-2011}.htm)



## SetAutoSelectNull {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/SetAutoSelectNull_{Steel}.htm`*

# SetAutoSelectNull

## Syntax

SapObject.SapModel.DesignSteel.SetAutoSelectNull

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

This function removes the auto select section assignments from all specified frame objects that have a steel frame design procedure.

The function returns zero if the auto select section assignments are successfully removed; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelAutoSelectSectionsNull()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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

   'import new frame section properties
      ret = SapModel.PropFrame.ImportProp("W18X35", "A992Fy50", "AISC16.XML", "W18X35")
      ret = SapModel.PropFrame.ImportProp("W18X40", "A992Fy50", "AISC16.XML", "W18X40")
      ret = SapModel.PropFrame.ImportProp("W18X46", "A992Fy50", "AISC16.XML", "W18X46")

   'define new auto select list frame section property
      ReDim MyName(2)
      MyName(0) = "W18X35"
      MyName(1) = "W18X40"
      MyName(2) = "W18X46"
      ret = SapModel.PropFrame.SetAutoSelectSteel("AUTO1", 3, MyName)

   'set frame section properties
      ret = SapModel.FrameObj.SetSection("8", "AUTO1")
      ret = SapModel.FrameObj.SetSection("10", "AUTO1")

   'set frame object selected
      ret = SapModel.FrameObj.SetSelected("8", True)

   'set auto select section null
      ret = SapModel.DesignSteel.SetAutoSelectNull("",SelectedObjects)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## SetCode {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/SetCode_{Steel}.htm`*

# SetCode

## Syntax

SapObject.SapModel.DesignSteel.SetCode

## VB6 Procedure

Function SetCode(ByVal CodeName As String) As Long

## Parameters

CodeName

This is one of the following steel design code names.

AASHTO LRFD 2007

AISC-ASD89

AISC 360-10

AISC360-05/IBC2006

AISC-LRFD93

API RP2A-LRFD 97

API RP2A-WSD2000

API RP2A-WSD2014

AS 4100-1998
ASCE 10-97

BS5950 2000

Chinese 2010
CSA S16-19
CSA S16-14
CSA-S16-09

EN 1993-1-1:2005 (formerly EUROCODE 3-2005)

Indian IS 800-2007

Italian NTC 2008

Italian UNI 10011

KBC 2009

Norsok N-004 2013

NZS 3404-1997

SP 16.13330.2011

## Remarks

This function sets the steel design code.

The function returns zero if the code is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignCode()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC 360-10")

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

In version 14.1.0, added Norway as a Country parameter.

Added Norsok N-004 2013 in version 16.1.0.

Updated list of code names in version 17.3.0.

Removed older codes which have been removed from the program in v18.0.0.

Updated list of available codes in v19.1.0.

## See Also

[GetCode](GetCode_{Steel}.htm)



## SetComboAutoGenerate{Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/SetComboAutoGenerate{Steel}.htm`*

# SetComboAutoGenerate

## Syntax

SapObject.SapModel.DesignSteel.SetComboAutoGenerate

## VB6 Procedure

Function SetComboAutoGenerate(ByVal AutoGenerate As Boolean) As Long

## Parameters

AutoGenerate

If this item is True, the option to automatically generate code-based design load combinations for steel frame design is turned on. If it is False, the option is turned off.

## Remarks

This function turns on or off the option to automatically generate code-based design load combinations for steel frame design.

The function returns zero if the options are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignComboAutoGenerate()
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
      ret = SapModel.DesignSteel.SetComboAutoGenerate(False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 18.1.0.

## See Also

[GetComboAutoGenerate](GetComboAutoGenerate_{Steel}.htm)



## SetComboDeflection {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/SetComboDeflection_{Steel}.htm`*

# SetComboDeflection

## Syntax

SapObject.SapModel.DesignSteel.SetComboDeflection

## VB6 Procedure

Function SetComboDeflection(ByVal Name As String, ByVal Selected As Boolean) As Long

## Parameters

Name

The name of an existing load combination.

Selected

If this item is True, the specified load combination is selected as a design combination for steel deflection design. If it is False, the combination is not selected for steel deflection design.

## Remarks

This function selects or deselects a load combination for steel deflection design.

The function returns zero if the selection status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignComboDeflection()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default steel design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(True, False, False, False)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName)

   'select combos for steel deflection design
      For i = 0 To NumberNames - 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignSteel.SetComboDeflection(MyName(i), Selected)
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

[GetComboDeflection](GetComboDeflection_{Steel}.htm)



## SetComboStrength {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/SetComboStrength_{Steel}.htm`*

# SetComboStrength

## Syntax

SapObject.SapModel.DesignSteel.SetComboStrength

## VB6 Procedure

Function SetComboStrength(ByVal Name As String, ByVal Selected As Boolean) As Long

## Parameters

Name

The name of an existing load combination.

Selected

If this item is True, the specified load combination is selected as a design combination for steel strength design. If it is False, the combination is not selected for steel strength design.

## Remarks

This function selects or deselects a load combination for steel strength design.

The function returns zero if the selection status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignComboStrength()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'add load pattern
      ret = SapModel.LoadPatterns.Add("LIVE", LTYPE\_LIVE)

   'add default steel design combos
      ret = SapModel.RespCombo.AddDesignDefaultCombos(True, False, False, False)

   'get combo names
      ret = SapModel.RespCombo.GetNameList(NumberNames, MyName)

   'select combos for steel strength design
      For i = 0 To NumberNames - 1
         If i = 0 Then Selected = True Else Selected = False
         ret = SapModel.DesignSteel.SetComboStrength(MyName(i), Selected)
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

[GetComboStrength](GetComboStrength_{Steel}.htm)



## SetDesignSection {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/SetDesignSection_{Steel}.htm`*

# SetDesignSection

## Syntax

SapObject.SapModel.DesignSteel.SetDesignSection

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

This function modifies the design section for all specified frame objects that have a steel frame design procedure.

The function returns zero if the design section is successfully modified; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignSection()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
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

   'import new frame section properties
      ret = SapModel.PropFrame.ImportProp("W18X35", "A992Fy50", "AISC16.XML", "W18X35")
      ret = SapModel.PropFrame.ImportProp("W18X40", "A992Fy50", "AISC16.XML", "W18X40")
      ret = SapModel.PropFrame.ImportProp("W18X46", "A992Fy50", "AISC16.XML", "W18X46")

   'define new auto select list frame section property
      ReDim MyName(2)
      MyName(0) = "W18X35"
      MyName(1) = "W18X40"
      MyName(2) = "W18X46"
      ret = SapModel.PropFrame.SetAutoSelectSteel("AUTO1", 3, MyName)

   'set frame section properties
      ret = SapModel.FrameObj.SetSection("8", "AUTO1")
      ret = SapModel.FrameObj.SetSection("10", "AUTO1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'set design section
      ret = SapModel.DesignSteel.SetDesignSection("8", "W18X46", False)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetDesignSection](GetDesignSection_{Steel}.htm)



## SetGroup {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/SetGroup_{Steel}.htm`*

# SetGroup

## Syntax

SapObject.SapModel.DesignSteel.SetGroup

## VB6 Procedure

Function SetGroup(ByVal Name As String, ByVal Selected As Boolean) As Long

## Parameters

Name

The name of an existing group.

Selected

If this item is True, the specified group is selected as a design group for steel design. If it is False, the group is not selected for steel design.

## Remarks

This function selects or deselects a group for steel design.

The function returns zero if the selection status is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignGroup()
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

   'select group for steel design
      ret = SapModel.DesignSteel.SetGroup("ALL", True)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetGroup](GetGroup_{Steel}.htm)



## SetTargetDispl

*Source file: `SAP2000_API_Fuctions/Design/Steel/SetTargetDispl.htm`*

# SetTargetDispl

## Syntax

SapObject.SapModel.DesignSteel.SetTargetDispl

## VB6 Procedure

Function SetTargetDispl(ByVal NumberItems As Long, ByRef LoadCase() As String, ByRef Point() As String, ByRef Displ() As Double, Optional ByVal Active As Boolean = True) As Long

## Parameters

NumberItems

The number of lateral displacement targets specified.

LoadCase

This is an array that includes the name of the static linear load case associated with each lateral displacement target.

Point

This is an array that includes the name of the point object associated to which the lateral displacement target applies.

Displ

This is an array that includes the lateral displacement target. [L]

Active

If this item is True, all specified lateral displacement targets are active. If it is False, they are inactive.

## Remarks

This function sets lateral displacement targets for steel design.

The function returns zero if the targets are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignTargetDispl()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyLCase() As String
      Dim MyPoint() As String
      Dim MyDispl() As Double

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
      ret = SapModel.LoadPatterns.Add("EQX", LTYPE\_QUAKE)

   'assign UBC97 parameters
      ret = SapModel.LoadPatterns.AutoSeismic.SetUBC97("EQX", 1, 0.05, 1, 0.035, 0, False, 0, 0, 1, 3, 0.4, 0, 0, 1, 3, 5, 0, 0, 1.15, 6)

   'set target displacement data
      ReDim MyLCase(0)
      ReDim MyPoint(0)
      ReDim MyDispl(0)
      MyLCase(0) = "EQX"
      MyPoint(0) = "3"
      MyDispl(0) = 0.4
      ret = SapModel.DesignSteel.SetTargetDispl(1, MyLCase, MyPoint, MyDispl)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetTargetDispl](GetTargetDispl.htm)



## SetTargetPeriod

*Source file: `SAP2000_API_Fuctions/Design/Steel/SetTargetPeriod.htm`*

# SetTargetPeriod

## Syntax

SapObject.SapModel.DesignSteel.SetTargetPeriod

## VB6 Procedure

Function SetTargetPeriod(ByVal NumberItems As Long, ByVal ModalCase As String, ByRef Mode() As Long, ByRef Period() As Double, Optional ByVal Active As Boolean = True) As Long

## Parameters

NumberItems

The number of lateral displacement targets specified.

ModalCase

The name of the modal load case for which the target periods apply.

Mode

This is an array that includes the mode number associated with each target period.

Period

This is an array that includes the target periods. [s]

Active

If this item is True, all specified target periods are active. If it is False, they are inactive.

## Remarks

This function sets time period targets for steel design.

The function returns zero if the targets are successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignTargetPeriod()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyMode() As Long
      Dim MyPeriod() As Double

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

   'set target period data
      ReDim MyLCase(0)
      ReDim MyMode(1)
      ReDim MyPeriod(1)
      MyMode(0) = 1
      MyPeriod(0) = 0.6
      MyMode(1) = 2
      MyPeriod(1) = 0.5
      ret = SapModel.DesignSteel.SetTargetPeriod(2, "MODAL", MyMode, MyPeriod)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

## See Also

[GetTargetPeriod](GetTargetPeriod.htm)



## StartDesign {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/StartDesign_{Steel}.htm`*

# StartDesign

## Syntax

SapObject.SapModel.DesignSteel.StartDesign

## VB6 Procedure

Function StartDesign() As Long

## Parameters

None

## Remarks

This function starts the steel frame design.

The function returns zero if the steel frame design is successfully started; otherwise it returns a nonzero value.

The function will fail if no steel frame objects are present. It will also fail if analysis results are not available.

## VBA Example

Sub StartSteelDesign()
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

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## GetOverwrite {Steel UBC97-ASD}

*Source file: `SAP2000_API_Fuctions/Design/Steel/UBC97-ASD/GetOverwrite_{Steel_UBC97-ASD}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.UBC97\_ASD.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRef ProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 32, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Moment coefficient, Cm Major

23 = Moment coefficient, Cm Minor

24 = Bending coefficient, Cb

25 = Yield stress, Fy

26 = Compressive stress, Fa

27 = Tensile stress, Ft

28 = Major bending stress, Fb3

29 = Minor bending stress, Fb2

30 = Major shear stress, Fv2

31 = Minor shear stress, Fv3

32 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ordinary MRF

2 = Special MRF

3 = Braced Frame

4 = Special CBF

5 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L]

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

24 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

25 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

26 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

27 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

28 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

29 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

30 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

31 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

32 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemUBC97\_ASD()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("UBC97-ASD")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.UBC97\_ASD.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_UBC97-ASD}.htm)



## GetPreference {Steel UBC97-ASD}

*Source file: `SAP2000_API_Fuctions/Design/Steel/UBC97-ASD/GetPreference_{Steel_UBC97-ASD}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.UBC97\_ASD.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 12, inclusive, indicating the preference item considered.

1 = Framing type

2 = Seismic zone

3 = Lateral factor

4 = Consider deflection

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total deflection limit, L/Value

9 = Total camber limit, L/Value

10 = Pattern live load factor

11 = Demand/capacity ratio limit

12 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Ordinary MRF

2 = Special MRF

3 = Braced Frame

4 = Special CBF

5 = EBF

2 = Seismic zone

1 = Zone 0

2 = Zone 1

3 = Zone 2

4 = Zone 3

5 = Zone 4

3 = Lateral factor

Value > 0

4 = Consider deflection

0 = No

Any other value = Yes

5 = DL deflection limit, L/Value5

Value > 0

6 = SDL + LL deflection limit, L/Value

Value > 0

7 = LL deflection limit, L/Value

Value > 0

8 = Total deflection limit, L/Value

Value > 0

9 = Total camber limit, L/Value

Value > 0

10 = Pattern live load factor

Value >= 0

11 = Demand/capacity ratio limit

Value > 0

12 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemUBC97\_ASD()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("UBC97-ASD")

   'get preference item
      ret = SapModel.DesignSteel.UBC97\_ASD.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_UBC97-ASD}.htm)



## SetOverwrite {Steel UBC97-ASD}

*Source file: `SAP2000_API_Fuctions/Design/Steel/UBC97-ASD/SetOverwrite_{Steel_UBC97-ASD}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.UBC97\_ASD.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group, depending on the value of the ItemTypeitem.

Item

This is an integer between 1 and 32, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Moment coefficient, Cm Major

23 = Moment coefficient, Cm Minor

24 = Bending coefficient, Cb

25 = Yield stress, Fy

26 = Compressive stress, Fa

27 = Tensile stress, Ft

28 = Major bending stress, Fb3

29 = Minor bending stress, Fb2

30 = Major shear stress, Fv2

31 = Minor shear stress, Fv3

32 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ordinary MRF

2 = Special MRF

3 = Braced Frame

4 = Special CBF

5 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L]

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

24 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

25 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

26 = Compressive stress, Fa

Value >= 0; 0 means use program determined value. [F/L2]

27 = Tensile stress, Ft

Value >= 0; 0 means use program determined value. [F/L2]

28 = Major bending stress, Fb3

Value >= 0; 0 means use program determined value. [F/L2]

29 = Minor bending stress, Fb2

Value >= 0; 0 means use program determined value. [F/L2]

30 = Major shear stress, Fv2

Value >= 0; 0 means use program determined value. [F/L2]

31 = Minor shear stress, Fv3

Value >= 0; 0 means use program determined value. [F/L2]

32 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemUBC97\_ASD()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("UBC97-ASD")

   'set overwrite item
      ret = SapModel.DesignSteel.UBC97\_ASD.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_UBC97-ASD}.htm)



## SetPreference {Steel UBC97-ASD}

*Source file: `SAP2000_API_Fuctions/Design/Steel/UBC97-ASD/SetPreference_{Steel_UBC97-ASD}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.UBC97\_ASD.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 12, inclusive, indicating the preference item considered.

1 = Framing type

2 = Seismic zone

3 = Lateral factor

4 = Consider deflection

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total deflection limit, L/Value

9 = Total camber limit, L/Value

10 = Pattern live load factor

11 = Demand/capacity ratio limit

12 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Ordinary MRF

2 = Special MRF

3 = Braced Frame

4 = Special CBF

5 = EBF

2 = Seismic zone

1 = Zone 0

2 = Zone 1

3 = Zone 2

4 = Zone 3

5 = Zone 4

3 = Lateral factor

Value > 0

4 = Consider deflection

0 = No

Any other value = Yes

5 = DL limit, L/Value

Value > 0

6 = Super DL + LL limit, L/Value

Value > 0

7 = Live load limit, L/Value

Value > 0

8 = Total limit, L/Value

Value > 0

9 = Total camber limit, L/Value

Value > 0

10 = Pattern live load factor

Value >= 0

11 = Demand/capacity ratio limit

Value > 0

12 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemUBC97\_ASD()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("UBC97-ASD")

   'set preference item
      ret = SapModel.DesignSteel.UBC97\_ASD.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_UBC97-ASD}.htm)



## GetOverwrite {Steel UBC97-LRFD}

*Source file: `SAP2000_API_Fuctions/Design/Steel/UBC97-LRFD/GetOverwrite_{Steel_UBC97-LRFD}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.UBC97\_LRFD.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 36, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Moment coefficient, Cm Major

23 = Moment coefficient, Cm Minor

24 = Bending coefficient, Cb

25 = Non-sway moment factor, B1 Major

26 = Non-sway moment factor, B1 Minor

27 = Sway moment factor, B2 Major

28 = Sway moment factor, B2 Minor

29 = Yield stress, Fy

30 = Compressive capacity, phi\*Pnc

31 = Tensile capacity, phi\*Pnt

32 = Major bending capacity, phi\*Mn3

33 = Minor bending capacity, phi\*Mn2

34 = Major shear capacity, phi\*Vn2

35 = Minor shear capacity, phi\*Vn3

36 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ordinary MRF

2 = Special MRF

3 = Braced Frame

4 = Special CBF

5 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L]

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

24 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

25 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

26 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

28 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

29 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

30 = Compressive capacity, phi\*Pnc

Value >= 0; 0 means use program determined value. [F]

31 = Tensile capacity, phi\*Pnt

Value >= 0; 0 means use program determined value. [F]

32 = Major bending capacity, phi\*Mn3

Value >= 0; 0 means use program determined value. [FL]

33 = Minor bending capacity, phi\*Mn2

Value >= 0; 0 means use program determined value. [FL]

34 = Major shear capacity, phi\*Vn2

Value >= 0; 0 means use program determined value. [F]

35 = Minor shear capacity, phi\*Vn3

Value >= 0; 0 means use program determined value. [F]

36 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemUBC97\_LRFD()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("UBC97-LRFD")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.UBC97\_LRFD.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_UBC97-LRFD}.htm)



## GetPreference {Steel UBC97-LRFD}

*Source file: `SAP2000_API_Fuctions/Design/Steel/UBC97-LRFD/GetPreference_{Steel_UBC97-LRFD}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.UBC97\_LRFD.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 12, inclusive, indicating the preference item considered.

1 = Framing type

2 = Importance factor

3 = Seismic zone

4 = Phi bending

5 = Phi compression

6 = Phi tension

7 = Phi shear

8 = Phi compression angle

9 = Consider deflection

10 = DL deflection limit, L/Value

11 = SDL + LL deflection limit, L/Value

12 = LL deflection limit, L/Value

13 = Total deflection limit, L/Value

14 = Total camber limit, L/Value

15 = Pattern live load factor

16 = Demand/capacity ratio limit

17 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Ordinary MRF

2 = Special MRF

3 = Braced Frame

4 = Special CBF

5 = EBF

2 = Importance factor

Value > 0

3 = Seismic zone

1 = Zone 0

2 = Zone 1

3 = Zone 2

4 = Zone 3

5 = Zone 4

3 = Lateral factor

Value > 0

4 = Phi bending

   Value > 0

5 = Phi compression

Value > 0

6 = Phi tension

Value > 0

7 = Phi shear

Value > 0

8 = Phi compression angle

Value > 0

9 = Consider deflection

0 = No

Any other value = Yes

10 = DL deflection limit, L/Value

Value > 0

11 = SDL + LL deflection limit, L/Value

Value > 0

12 = LL deflection limit, L/Value

Value > 0

13 = Total deflection limit, L/Value

Value > 0

14 = Total camber limit, L/Value

Value > 0

15 = Pattern live load factor

Value >= 0

16 = Demand/capacity ratio limit

Value > 0

17 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemUBC97\_LRFD()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("UBC97-LRFD")

   'get preference item
      ret = SapModel.DesignSteel.UBC97\_LRFD.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_UBC97-LRFD}.htm)



## SetOverwrite {Steel UBC97-LRFD}

*Source file: `SAP2000_API_Fuctions/Design/Steel/UBC97-LRFD/SetOverwrite_{Steel_UBC97-LRFD}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.UBC97\_LRFD.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 36, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Moment coefficient, Cm Major

23 = Moment coefficient, Cm Minor

24 = Bending coefficient, Cb

25 = Non-sway moment factor, B1 Major

26 = Non-sway moment factor, B1 Minor

27 = Sway moment factor, B2 Major

28 = Sway moment factor, B2 Minor

29 = Yield stress, Fy

30 = Compressive capacity, phi\*Pnc

31 = Tensile capacity, phi\*Pnt

32 = Major bending capacity, phi\*Mn3

33 = Minor bending capacity, phi\*Mn2

34 = Major shear capacity, phi\*Vn2

35 = Minor shear capacity, phi\*Vn3

36 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = Ordinary MRF

2 = Special MRF

3 = Braced Frame

4 = Special CBF

5 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L]

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

24 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

25 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

26 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

28 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

29 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

30 = Compressive capacity, phi\*Pnc

Value >= 0; 0 means use program determined value. [F]

31 = Tensile capacity, phi\*Pnt

Value >= 0; 0 means use program determined value. [F]

32 = Major bending capacity, phi\*Mn3

Value >= 0; 0 means use program determined value. [FL]

33 = Minor bending capacity, phi\*Mn2

Value >= 0; 0 means use program determined value. [FL]

34 = Major shear capacity, phi\*Vn2

Value >= 0; 0 means use program determined value. [F]

35 = Minor shear capacity, phi\*Vn3

Value >= 0; 0 means use program determined value. [F]

36 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemUBC97\_LRFD()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("UBC97-LRFD")

   'set overwrite item
      ret = SapModel.DesignSteel.UBC97\_LRFD.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_UBC97-LRFD}.htm)



## SetPreference {Steel UBC97-LRFD}

*Source file: `SAP2000_API_Fuctions/Design/Steel/UBC97-LRFD/SetPreference_{Steel_UBC97-LRFD}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.UBC97\_LRFD.SetPreference

## VB6 Procedure

Function SetPreference(ByVal Item As Long, ByVal Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 17, inclusive, indicating the preference item considered.

1 = Framing type

2 = Importance factor

3 = Seismic zone

4 = Phi bending

5 = Phi compression

6 = Phi tension

7 = Phi shear

8 = Phi compression angle

9 = Consider deflection

10 = DL deflection limit, L/Value

11 = SDL + LL limit, L/Value

12 = Live load limit, L/Value

13 = Total limit, L/Value

14 = Total camber limit, L/Value

15 = Pattern live load factor

16 = Demand/capacity ratio limit

17 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = Ordinary MRF

2 = Special MRF

3 = Braced Frame

4 = Special CBF

5 = EBF

2 = Importance factor

Value > 0

3 = Seismic zone

1 = Zone 0

2 = Zone 1

3 = Zone 2

4 = Zone 3

5 = Zone 4

3 = Lateral factor

Value > 0

4 = Phi bending

Value > 0

5 = Phi compression

Value > 0

6 = Phi tension

Value > 0

7 = Phi shear

Value > 0

8 = Phi compression angle

Value > 0

9 = Consider deflection

0 = No

Any other value = Yes

10 = DL limit, L/Value

Value > 0

11 = Super DL + LL limit, L/Value

Value > 0

12 = Live load limit, L/Value

Value > 0

13 = Total limit, L/Value

Value > 0

14 = Total camber limit, L/Value

Value > 0

15 = Pattern live load factor

Value >= 0

16 = Demand/capacity ratio limit

Value > 0

17 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemUBC97\_LRFD()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("UBC97-LRFD")

   'set preference item
      ret = SapModel.DesignSteel.UBC97\_LRFD.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_UBC97-LRFD}.htm)



## VerifyPassed {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/VerifyPassed_{Stee).htm`*

# VerifyPassed

## Syntax

SapObject.SapModel.DesignSteel.VerifyPassed

## VB6 Procedure

Function VerifyPassed(ByRef NumberItems As Long, ByRef n1 As Long, ByRef n2 As Long, ByRef MyName() As String) As Long

## Parameters

NumberItems

The number of steel frame objects that did not pass the design check or have not yet been checked.

n1

The number of steel frame objects that did not pass the design check.

n2

The number of steel frame objects that have not yet been checked.

MyName

This is an array that includes the name of each frame object that did not pass the design check or has not yet been checked.

## Remarks

This function retrieves the names of the frame objects that did not pass the design check or have not yet been checked, if any.

The function returns zero if the names are successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub VerifySteelDesignPassed()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyName2() As String
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

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'import new frame section properties
      ret = SapModel.PropFrame.ImportProp("W18X35", "A992Fy50", "AISC16.XML", "W18X35")
      ret = SapModel.PropFrame.ImportProp("W18X40", "A992Fy50", "AISC16.XML", "W18X40")
      ret = SapModel.PropFrame.ImportProp("W18X46", "A992Fy50", "AISC16.XML", "W18X46")

   'define new auto select list frame section property
      ReDim MyName2(2)
      MyName2(0) = "W18X35"
      MyName2(1) = "W18X40"
      MyName2(2) = "W18X46"
      ret = SapModel.PropFrame.SetAutoSelectSteel("AUTO1", 3, MyName2)

   'set frame section properties
      ret = SapModel.FrameObj.SetSection("8", "AUTO1")
      ret = SapModel.FrameObj.SetSection("10", "AUTO1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'verify frame objects successfully designed
      ret = SapModel.DesignSteel.VerifyPassed(NumberItems, n1, n2, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## VerifySections {Steel}

*Source file: `SAP2000_API_Fuctions/Design/Steel/VerifySections_{Steel}.htm`*

# VerifySections

## Syntax

SapObject.SapModel.DesignSteel.VerifySections

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

Sub VerifySteelDesignSections()
   'dimension variables
      Dim SapObject as cOAPI
      Dim SapModel As cSapModel
      Dim ret As Long
      Dim MyName2() As String
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

   'create model from template
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'import new frame section properties
      ret = SapModel.PropFrame.ImportProp("W18X35", "A992Fy50", "AISC16.XML", "W18X35")
      ret = SapModel.PropFrame.ImportProp("W18X40", "A992Fy50", "AISC16.XML", "W18X40")
      ret = SapModel.PropFrame.ImportProp("W18X46", "A992Fy50", "AISC16.XML", "W18X46")

   'define new auto select list frame section property
      ReDim MyName2(2)
      MyName2(0) = "W18X35"
      MyName2(1) = "W18X40"
      MyName2(2) = "W18X46"
      ret = SapModel.PropFrame.SetAutoSelectSteel("AUTO1", 3, MyName2)

   'set frame section properties
      ret = SapModel.FrameObj.SetSection("8", "AUTO1")
      ret = SapModel.FrameObj.SetSection("10", "AUTO1")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'verify analysis versus design section
      ret = SapModel.DesignSteel.VerifySections(NumberItems, MyName)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also



## GetOverwrite {Steel AISC LRFD99}

*Source file: `SAP2000_API_Fuctions/Design/Steel/aisc_lrfd99/GetOverwrite_{Steel_AISC_LRFD99}.htm`*

# GetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC\_LRFD99.GetOverwrite

## VB6 Procedure

Function GetOverwrite(ByVal Name As String, ByVal Item As Long, ByRef Value As Double, ByRefProgDet As Boolean) As Long

## Parameters

Name

The name of a frame object with a steel frame design procedure.

Item

This is an integer between 1 and 37, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Moment coefficient, Cm Major

23 = Moment coefficient, Cm Minor

24 = Bending coefficient, Cb

25 = Non-sway moment factor, B1 Major

26 = Non-sway moment factor, B1 Minor

27 = Sway moment factor, B2 Major

28 = Sway moment factor, B2 Minor

29 = Yield stress, Fy

30 = Expected to specified Fy ratio, Ry

31 = Compressive capacity, phi\*Pnc

32 = Tensile capacity, phi\*Pnt

33 = Major bending capacity, phi\*Mn3

34 = Minor bending capacity, phi\*Mn2

35 = Major shear capacity, phi\*Vn2

36 = Minor shear capacity, phi\*Vn3

37 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = OMF

2 = IMF

3 = SMF

4 = OCBF

5 = SCBF

6 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L]

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

24 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

25 = Non-sway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

26 = Non-sway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

28 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

29 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

30 = Expected to specified Fy ratio, Ry

Value >= 0; 0 means use program determined value.

31 = Compressive capacity, phi\*Pnc

Value >= 0; 0 means use program determined value. [F]

32 = Tensile capacity, phi\*Pnt

Value >= 0; 0 means use program determined value. [F]

33 = Major bending capacity, phi\*Mn3

Value >= 0; 0 means use program determined value. [FL]

34 = Minor bending capacity, phi\*Mn2

Value >= 0; 0 means use program determined value. [FL]

35 = Major shear capacity, phi\*Vn2

Value >= 0; 0 means use program determined value. [F]

36 = Minor shear capacity, phi\*Vn3

Value >= 0; 0 means use program determined value. [F]

37 = Demand/capacity ratio limit

Value >= 0; 0 means use program determined value.

ProgDet

If this item is True, the specified value is program determined.

## Remarks

This function retrieves the value of a steel design overwrite item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignOverwriteItemAISC\_LRFD99()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-LRFD99")

   'run analysis
      ret = SapModel.File.Save("C:\SapAPI\x.sdb")
      ret = SapModel.Analyze.RunAnalysis

   'start steel design
      ret = SapModel.DesignSteel.StartDesign

   'get overwrite item
      ret = SapModel.DesignSteel.AISC\_LRFD99.GetOverwrite("8", 1, Value, ProgDet)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[SetOverwrite](SetOverwrite_{Steel_AISC_LRFD99}.htm)



## GetPreference {Steel AISC LRFD99}

*Source file: `SAP2000_API_Fuctions/Design/Steel/aisc_lrfd99/GetPreference_{Steel_AISC_LRFD99}.htm`*

# GetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC\_LRFD99.GetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 21, inclusive, indicating the preference item considered.

1 = Framing type

2 = Seismic design capacity

3 = Phi bending

4 = Phi compression

5 = Phi tension - yielding

6 = Phi tension - fracture

7 = Phi shear

8 = Phi shear - torsion

9 = Phi compression, angle

10 = Ignore seismic code

11 = Ignore special seismic code

12 = Is doubler plate plug-welded

13 = Consider deflection

14 = DL deflection limit, L/Value

15 = SDL + LL deflection limit, L/Value

16 = LL deflection limit, L/Value

17 = Total deflection limit, L/Value

18 = Total camber limit, L/Value

19 = Pattern live load factor

20 = Demand capacity ratio limit

21 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = OMF

2 = IMF

3 = SMF

4 = OCBF

5 = SCBF

6 = EBF

2 = Seismic design capacity

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Phi bending

 Value > 0

4 = Phi compression

Value > 0

5 = Phi tension – yielding

Value > 0

6 = Phi tension - fracture

Value > 0

7 = Phi shear

Value > 0

8 = Phi shear - torsion

Value > 0

9 = Phi compression, angle

Value > 0

10 = Ignore seismic code

0 = No

Any other value = Yes

11 = Ignore special seismic code

0 = No

Any other value = Yes

12 = Is doubler plate plug-welded

0 = No

Any other value = Yes

13 = Consider deflection

0 = No

Any other value = Yes

14 = DL deflection limit, L/Value

Value > 0

15 = SDL + LL deflection limit, L/Value

Value > 0

16 = LL deflection limit, L/Value

Value > 0

17 = Total deflection limit, L/Value

Value > 0

18 = Total camber limit, L/Value

Value > 0

19 = Pattern live load factor

Value >= 0

20 = Demand capacity ratio limit

Value > 0

21 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function retrieves the value of a steel design preference item.

The function returns zero if the item is successfully retrieved; otherwise it returns a nonzero value.

## VBA Example

Sub GetSteelDesignPreferenceItemAISC\_LRFD99()
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
      ret = SapModel.File.New2DFrame(PortalFrame, 2, 144, 2, 288)

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-LRFD99")

   'get preference item
      ret = SapModel.DesignSteel.AISC\_LRFD99.GetPreference(1, Value)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[SetPreference](SetPreference_{Steel_AISC_LRFD99}.htm)



## SetOverwrite {Steel AISC LRFD99}

*Source file: `SAP2000_API_Fuctions/Design/Steel/aisc_lrfd99/SetOverwrite_{Steel_AISC_LRFD99}.htm`*

# SetOverwrite

## Syntax

SapObject.SapModel.DesignSteel.AISC\_LRFD99.SetOverwrite

## VB6 Procedure

Function SetOverwrite(ByVal Name As String, ByVal Item As Long, ByVal Value As Double, Optional ByValItemType As eItemType = Object) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

Item

This is an integer between 1 and 37, inclusive, indicating the overwrite item considered.

1 = Framing type

2 = Omega0

3 = Consider deflection

4 = Deflection check type

5 = DL deflection limit, L/Value

6 = SDL + LL deflection limit, L/Value

7 = LL deflection limit, L/Value

8 = Total load deflection limit, L/Value

9 = Total camber limit, L/Value

10 = DL deflection limit, absolute

11 = SDL + LL deflection limit, absolute

12 = LL deflection limit, absolute

13 = Total load deflection limit, absolute

14 = Total camber limit, absolute

15 = Specified camber

16 = Net area to total area ratio

17 = Live load reduction factor

18 = Unbraced length ratio, Major

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

20 = Effective length factor, K Major

21 = Effective length factor, K Minor

22 = Moment coefficient, Cm Major

23 = Moment coefficient, Cm Minor

24 = Bending coefficient, Cb

25 = Non-sway moment factor, B1 Major

26 = Non-sway moment factor, B1 Minor

27 = Sway moment factor, B2 Major

28 = Sway moment factor, B2 Minor

29 = Yield stress, Fy

30 = Expected to specified Fy ratio, Ry

31 = Compressive capacity, phi\*Pnc

32 = Tensile capacity, phi\*Pnt

33 = Major bending capacity, phi\*Mn3

34 = Minor bending capacity, phi\*Mn2

35 = Major shear capacity, phi\*Vn2

36 = Minor shear capacity, phi\*Vn3

37 = Demand/capacity ratio limit

Value

The value of the considered overwrite item.

1 = Framing type

0 = Program Default

1 = OMF

2 = IMF

3 = SMF

4 = OCBF

5 = SCBF

6 = EBF

2 = Omega0

Value >= 0; 0 means use a program determined value.

3 = Consider deflection

0 = Program Determined

1 = No

2 = Yes

4 = Deflection check type

0 = Program default

1 = Ratio

2 = Absolute

3 = Both

5 = DL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

6 = SDL + LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

7 = LL deflection limit, L/Value

Value >= 0; 0 means no check for this item.

8 = Total load deflection limit, L/Value

Value >= 0; 0 means no check for this item.

9 = Total camber limit, L/Value

Value >= 0; 0 means no check for this item.

10 = DL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

11 = SDL + LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

12 = LL deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

13 = Total load deflection limit, absolute

Value >= 0; 0 means no check for this item. [L]

14 = Total camber limit, absolute

Value >= 0; 0 means no check for this item. [L]

15 = Specified camber

Value >= 0. [L]

16 = Net area to total area ratio

Value >= 0; 0 means use program default value.

17 = Live load reduction factor

Value >= 0; 0 means use program determined value.

18 = Unbraced length ratio, Major

Value >= 0; 0 means use program determined value.

19 = Unbraced length ratio, Minor Lateral Torsional Buckling

Value >= 0; 0 means use program determined value.

20 = Effective length factor, K Major

Value >= 0; 0 means use program determined value.

21 = Effective length factor, K Minor

Value >= 0; 0 means use program determined value.

22 = Moment coefficient, Cm Major

Value >= 0; 0 means use program determined value.

23 = Moment coefficient, Cm Minor

Value >= 0; 0 means use program determined value.

24 = Bending coefficient, Cb

Value >= 0; 0 means use program determined value.

25 = Nonsway moment factor, B1 Major

Value >= 0; 0 means use program determined value.

26 = Nonsway moment factor, B1 Minor

Value >= 0; 0 means use program determined value.

27 = Sway moment factor, B2 Major

Value >= 0; 0 means use program determined value.

28 = Sway moment factor, B2 Minor

Value >= 0; 0 means use program determined value.

29 = Yield stress, Fy

Value >= 0; 0 means use program determined value. [F/L2]

30 = Expected to specified Fy ratio, Ry

Value >= 0; 0 means use program determined value.

31 = Compressive capacity, phi\*Pnc

Value >= 0; 0 means use program determined value. [F]

32 = Tensile capacity, phi\*Pnt

Value >= 0; 0 means use program determined value. [F]

33 = Major bending capacity, phi\*Mn3

Value >= 0; 0 means use program determined value. [FL]

34 = Minor bending capacity, phi\*Mn2

Value >= 0; 0 means use program determined value. [FL]

35 = Major shear capacity, phi\*Vn2

Value >= 0; 0 means use program determined value. [F]

36 = Minor shear capacity, phi\*Vn3

Value >= 0; 0 means use program determined value. [F]

37 = Demand/capacity ratio limit

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

This function sets the value of a steel design overwrite item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignOverwriteItemAISC\_LRFD99()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-LRFD99")

   'set overwrite item
      ret = SapModel.DesignSteel.AISC\_LRFD99.SetOverwrite("8", 1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

## See Also

[GetOverwrite](GetOverwrite_{Steel_AISC_LRFD99}.htm)



## SetPreference {Steel AISC LRFD99}

*Source file: `SAP2000_API_Fuctions/Design/Steel/aisc_lrfd99/SetPreference_{Steel_AISC_LRFD99}.htm`*

# SetPreference

## Syntax

SapObject.SapModel.DesignSteel.AISC\_LRFD99.SetPreference

## VB6 Procedure

Function GetPreference(ByVal Item As Long, ByRef Value As Double) As Long

## Parameters

Item

This is an integer between 1 and 21, inclusive, indicating the preference item considered.

1 = Framing type

2 = Seismic design capacity

3 = Phi bending

4 = Phi compression

5 = Phi tension - yielding

6 = Phi tension - fracture

7 = Phi shear

8 = Phi shear - torsion

9 = Phi compression, angle

10 = Ignore seismic code

11 = Ignore special seismic code

12 = Is doubler plate plug-welded

13 = Consider deflection

14 = DL deflection limit, L/Value

15 = SDL + LL deflection limit, L/Value

16 = LL deflection limit, L/Value

17 = Total deflection limit, L/Value

18 = Total camber limit, L/Value

19 = Pattern live load factor

20 = Demand capacity ratio limit

21 = Multi-response case design

Value

The value of the considered preference item.

1 = Framing type

1 = OMF

2 = IMF

3 = SMF

4 = OCBF

5 = SCBF

6 = EBF

2 = Seismic design capacity

1 = A

2 = B

3 = C

4 = D

5 = E

6 = F

3 = Phi bending

Value > 0

4 = Phi compression

Value > 0

5 = Phi tension – yielding

Value > 0

6 = Phi tension - fracture

Value > 0

7 = Phi shear

Value > 0

8 = Phi shear - torsion

Value > 0

9 = Phi compression, angle

Value > 0

10 = Ignore seismic code

0 = No

Any other value = Yes

11 = Ignore special seismic code

0 = No

Any other value = Yes

12 = Is doubler plate plug-welded

0 = No

Any other value = Yes

13 = Consider deflection

0 = No

Any other value = Yes

14 = DL deflection limit, L/Value

Value > 0

15 = SDL + LL deflection limit, L/Value

Value > 0

16 = LL deflection limit, L/Value

Value > 0

17 = Total deflection limit, L/Value

Value > 0

18 = Total camber limit, L/Value

Value > 0

19 = Pattern live load factor

Value >= 0

20 = Demand capacity ratio limit

Value > 0

21 = Multi-response case design

  1 = Envelopes

  2 = Step-by-step

  3 = Last step

  4 = Envelopes -- All

  5 = Step-by-step -- All

## Remarks

This function sets the value of a steel design preference item.

The function returns zero if the item is successfully set; otherwise it returns a nonzero value.

## VBA Example

Sub SetSteelDesignPreferenceItemAISC\_LRFD99 ()
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

   'set steel design code
      ret = SapModel.DesignSteel.SetCode("AISC-LRFD99")

   'set preference item
      ret = SapModel.DesignSteel.AISC\_LRFD99.SetPreference(1, 2)

   'close Sap2000
      SapObject.ApplicationExit False
      Set SapModel = Nothing
      Set SapObject = Nothing
End Sub

## Release Notes

Initial release in version 11.03.

Changed Time history design item to Multi-response case design and added additional values in version 15.0.1.

## See Also

[GetPreference](GetPreference_{Steel_AISC_LRFD99}.htm)

