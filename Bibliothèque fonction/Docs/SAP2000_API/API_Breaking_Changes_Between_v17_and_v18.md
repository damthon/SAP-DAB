# API Breaking Changes Between v17 and v18

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Breaking_Changes_Between_v17_and_v18

---



## Breaking Changes

*Source file: `SAP2000_API_Fuctions/Breaking_Changes_Between_v17_and_v18/Breaking_Changes_v18.htm`*

# Breaking Changes

The following items have changed in Version 18 and will require changes in existing source code where they are used.

* The following steel design codes have been removed, including their GetOverwrite, GetPreference, SetOverwrite, and SetPreference functions. This will also require updating calls to SapObject.SapModel.DesignSteel.GetCode and SetCode where these removed codes are used.
* + AISC-ASD01
  + AISC-LRFD99
  + BS5950 90
  + CAN/CSA-S16-01
  + CISC 95
  + EUROCODE 3-1993
  + Indian IS:800-1998
  + Italian UNI 10011
  + Norsok N-004
  + UBC97-ASD
  + UBC97-LRFD

* The following concrete frame design codes have been removed, including their GetOverwrite, GetPreference, SetOverwrite, and SetPreference functions. This will also require updating calls to SapObject.SapModel.DesignConcrete.GetCode and SetCode where these removed codes are used.
* + ACI 318-99
  + ACI 318-02
  + ACI 318-05/IBC2003
  + AS 3600-01
  + BS8110 89
  + CSA-A23.3-94
  + EUROCODE 2-1992
  + Hong Kong CP 2004
  + Italian DM 14-2-92
  + Mexican RCDF 2001
  + NZS 3101-95
  + UBC97

