# Migration Notes

Source: CSI OAPI Documentation (SAP2000) — root

---



## Improvements in API Behavior

*Source file: `Migrating_from_Version_16_to_Version_17/Improvements_in_API_Behavior.htm`*

# Improvements in API Behavior

* Starting with SAP2000 v17.2.0, 32-bit and 64-bit API clients can use the same syntax to connect to SAP2000. Please see the examples for specific instructions.
* Starting with SAP2000 v 17.2.0, client applications can connect to instances of SAP2000 that were starting manually, e.g. by clicking on the SAP2000 icon. Please see the examples for specific instructions. The MATLAB example has now been updated with these instructions.
* API-launched instances of SAP2000 can now run in DirectX graphics mode.
* API-launched instances of SAP2000 can now run the analysis out-of-process, allowing larger models to be analyzed.



## Migrating From SAP2000v16 to SAP2000v17

*Source file: `Migrating_from_Version_16_to_Version_17/Migrating_From_SAP2000v16_to_SAP2000v17.htm`*

# Migrating From SAP2000v16 to SAP2000v17

In version 17 of SAP2000, the API has been separated from the main SAP2000 executable into a dynamic link library (DLL). This will change how API client applications connect to CSI software. You will no longer directly reference the SAP2000 executable assembly. Instead, you will reference the API DLL. In addition, you will no longer be able to declare a variable of type SapObject. Instead, create a variable of type SAP2000v17 cOAPI, which is an interface type. Then instantiate an object that implements the cOAPI interface. This process is detailed in the included examples.

# Migrating from CSiBridge16 to CSiBridge17

The same considerations and examples apply to CSiBridge 2015 (v17) as well as to SAP2000v17. In the discussion throughout this document, replace all references to SAP2000 with CSiBridge, all references to Sap2000v16 with CSiBridge16, and all references to Sap2000v17 with CSiBridge17.

See Also

Changes in API Behavior

Instructions for Updating COM clients (VBA example)

Instructions for Updating .NET clients (C# example)

[Breaking Changes](../SAP2000_API_Fuctions/Breaking_Changes_Between_v16_and_v17/Breaking_Changes.htm)

[Breaking Changes to COM Enumerations](../SAP2000_API_Fuctions/Breaking_Changes_Between_v16_and_v17/Breaking_Changes_to_COM_Enumerations.htm)

Breaking Changes to NET Enumerations



## Migrating From SAP2000v20 to SAP2000v1

*Source file: `Migrating_from_Version_20_to_Version_21/Migrating_From_SAP2000v20_to_SAP2000v1.htm`*

# Migrating From SAP2000v20 to SAP2000v1

Starting with Version 21 of SAP2000, the API DLLs will no longer have the program version as part of their name. So, while the name of the API library for SAP2000 version 20 was SAP2000v20.dll, the name of the API library for SAP2000 version 21 is SAP2000v1.dll.

The name of the API library will remain SAP2000v1.dll , even as new major versions of SAP2000 are released. Since improvements will continue to be added to the API, a new function, cHelper. GetOAPIVersionNumber, has been added. This API version number will increment as new API functions are added. However, the API library name will remain SAP2000v1.dll.

Once users reference the new SAP2000v1.dll in their client applications, they will no longer need to update with every major release. The SAP2000v1.dll reference in their client application will automatically use the latest edition of SAP2000v1 that is registered with each product installation.

# Migrating from CSiBridge20 to CSiBridge1

The same considerations and examples apply to CSiBridge but the name of the API library is changing from CSiBridge20.dll to CSiBridge1.dll.

