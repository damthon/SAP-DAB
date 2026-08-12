# Root Overview and Misc Functions

Source: CSI OAPI Documentation (SAP2000) — root

---



## Breaking Changes in v23.0.0, v22.2.0, and v22.1.0

*Source file: `Breaking_Changes_in_v23.0.0,_v22.2.0,_and_v22.1.0.htm`*

# Breaking Changes in v23.0.0, v22.2.0, and v22.1.0

The following inadvertent changes broke compatibility with earlier API versions:

In SAP2000 v22.2.0 (SAP2000v1.dll version 1.9 and CSiAPIv1.dll version 1.9), eMatTypeSteel\_Chinese\_Q345 enumeration got renamed to eMatTypeSteel\_Chinese\_Q355.

## Affected Programs:

* SAP2000 v22.2.0, v22.2.1, v23.0.0
* CSiBridge v22.2.0, v22.2.1, v23.0.0

## Affected API clients:

* Compiled COM clients (e.g. VB6, Delphi) failed to start.
* Interpreted COM clients (e.g. VBA) failed to compile/run if the affected enumeration was used.

## Fix

* eMatTypeSteel\_Chinese\_Q345 enumeration got reinstated.

In SAP2000 v23.0.0 (SAP2000v1.dll version 1.13 and CSiAPIv1.dll version 1.13), cDAlAA\_ASD\_2000 & cDAlAA\_LRFD\_2000 interfaces got removed.

## Affected Programs:

* SAP2000 v23.0.0

## Affected API clients:

* Compiled COM clients (e.g. VB6, Delphi) started but gave an automation error if affected interfaces were used.
* Interpreted COM clients (e.g. VBA) failed to compile/run if the affected interfaces were used.
* Compiled .NET clients started but gave an error if affected interfaces were used.

## Fix

* cDAlAA\_ASD\_2000 & cDAlAA\_LRFD\_2000 interfaces got reinstated.

SAP2000 versions 22.2.0, 22.2.1, and 23.0.0 and corresponding SAP2000v1.dll versions 1.9 and 1.13 & CSiAPIv1.dll versions between 1.9 and 1.13 should not to be used for developing plug-ins and/or API scripts to ensure full compatibility with past and future API versions.

cOAPI.GetOAPIVersionNumber() method can be used to check for incompatible API versions before using affected interfaces to prevent run time errors.

CSiBridge versions 22.2.0, 22.2.1, and 23.0.0 and corresponding CSiBridge1.dll versions 1.9 and 1.13 & CSiAPIv1.dll versions between 1.9 and 1.13 should not to be used for developing plug-ins and/or API scripts to ensure full compatibility with past and future API versions.



## Breaking Changes in v26.0.0

*Source file: `Breaking_Changes_in_v26.0.htm`*

# Breaking Changes in v26.0.0

[1] The Remote API, used to start and/or connect to a running instance of SAP2000 on a Remote Computer, has been disabled with the release of SAP2000 v26.0.0. API functions listed below will return an error code when called:

* cHelper.CreateObjectHost
* cHelper.CreateObjectHostPort
* cHelper.CreateObjectProgIDHost
* cHelper.CreateObjectProgIDHostPort
* cHelper.GetObjectHost
* cHelper.GetObjectHostPort

[2] In SAP2000 v26.0.0 and later, the API is compiled as a .NET Standard 2.0 AnyCPU dynamic link library (DLL). Due to that change, certain late binding VBA calls that may have worked in earlier versions of the API will no longer work. CSI recommends using early binding for VBA, and all other, API client applications, as documented in this help file.

[3] Using CSiAPIv1.dll versions 2.0 and 2.1 (released with ETABS/SAFE v22.0.0 and v22.1.0, respectively) to interact with any version of SAP2000/CSiBridge (including v26.0.0 and future versions), will result in an exception when accessing the following properties of the cLoadCases interface from an external API client/script:

* cLoadCases.HyperStatic As cCaseHyperStatic
* cLoadCases.ModalEigen As cCaseModalEigen
* cLoadCases.ModalRitz As cCaseModalRitz
* cLoadCases.ModHistLinear As cCaseModalHistoryLinear
* cLoadCases.ModHistNonlinear As cCaseModalHistoryNonlinear
* cLoadCases.ResponseSpectrum As cCaseResponseSpectrum
* cLoadCases.StaticLinear As cCaseStaticLinear
* cLoadCases.StaticNonlinear As cCaseStaticNonlinear
* cLoadCases.StaticNonlinearStaged As cCaseStaticNonlinearStaged
* cLoadCases.ExternalResults As cCaseExternalResults
* cLoadCases.Moving As cCaseMovingLoad
* cLoadCases.PSD As cCasePowerSpectralDensity
* cLoadCases.StaticLinearMultistep As cCaseStaticLinearMultistep
* cLoadCases.StaticNonlinearMultistep As cCaseStaticNonlinearMultistep
* cLoadCases.SteadyState As cCaseSteadyState

Similarly, using CSiAPIv1.dll from any version of SAP2000/CSiBridge (including v26.0.0 and future versions) to interact with ETABS/SAFE v22.0.0 and/or v22.1.0 using above properties of the cLoadCases interface from an external API client/script will result in an exception.

ETABS and SAFE versions v22.0.0 and v22.1.0 and corresponding ETABSv1.dll/SAFEv1.dll/CSiAPIv1.dll versions 2.0 and 2.1 should not to be used for developing external API clients/scripts to ensure full compatibility with past and future API versions.

cOAPI.GetOAPIVersionNumber() method can be used to check for incompatible API versions before using affected interfaces to prevent run time errors.



## DeleteLoadDistributedWithGUID

*Source file: `DeleteLoadDistributedWithGUID.htm`*

# DeleteLoadDistributedWithGUID

Type topic text here.



## DeleteLoadForceWithGUID {Point Object}

*Source file: `DeleteLoadForceWithGUID_{Point_Object}.htm`*

# DeleteLoadForceWithGUID {Point Object}

## Syntax

SapObject.SapModel.PointObj.DeleteLoadForceWithGUID

## VB6 Procedure

Function DeleteLoadForceWithGUID(ByVal Name As String, ByVal GUID As String) As Long

## Parameters

Name

The name of an existing point object.

GUID

The global unique ID of one of the point loads on that point object.

## Remarks

This function deletes the point load assignment with the specified global unique ID for the specified point object.

The function returns zero if the load assignment is successfully deleted, otherwise it returns a nonzero value.

## Release Notes

Initial release in version 17.2.0.

## See Also

[GetLoadForceWithGUID](GetLoadForceWithGUID_{Point_Object}.htm)

[SetLoadForceWithGUID](SetLoadForceWithGUID_{Point_Object}.htm)



## GetLoadDistributedWithGUID {Cable Object}

*Source file: `GetLoadDistributedWithGUID_{Cable_Object}.htm`*

# GetLoadDistributedWithGUID

## Syntax

SapObject.SapModel.CableObj.GetLoadDistributedWithGUID

## VB6 Procedure

Function GetLoadDistributedWithGUID(ByVal Name As String, ByRef NumberItems As Long, ByRef CableName() As String, ByRef LoadPat() As String, ByRef MyType() As Long, ByRef CSys() As String, ByRef Dir() As Long, ByRef Value() As Double, ByRefGUID() As String, Optional ByVal ItemType As eItemType = Object) As Long

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

GUID

This is an array that includes the global unique ID of each load.

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

## Release Notes

Initial release in version 17.2.0.

## See Also

[SetLoadDistributedWithGUID](SetLoadDistributedWithGUID_{Cable_Object}.htm)

[DeleteLoadDistributedWithGUID](SAP2000_API_Fuctions/Object_Model/Cable_Object/DeleteLoadDistributedWithGUID_{Cable_Object}.htm)



## GetLoadForceWithGUID {Point Object}

*Source file: `GetLoadForceWithGUID_{Point_Object}.htm`*

# GetLoadForceWithGUID {Point Object}

## Syntax

SapObject.SapModel.PointObj.GetLoadForceWithGUID

## VB6 Procedure

Function GetLoadForceWithGUID(ByVal Name As String, ByRef NumberItems As Integer, ByRef PointName() As String, ByRef LoadPat() As String, ByRef LcStep() As Integer, ByRef CSys() As String, ByRef F1() As Double, ByRef F2() As Double, ByRef F3() As Double, ByRef M1() As Double, ByRef M2() As Double, ByRef M3() As Double, ByRef GUID() As String, Optional ByVal ItemType As eItemType = eItemType.Objects) As Long

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

GUID

This is an array that includes the global unique ID of the distributed load.

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

## Release Notes

Initial release in version 17.2.0.

## See Also

[SetLoadForceWithGUID](SetLoadForceWithGUID_{Point_Object}.htm)

[DeleteLoadForceWithGUID](DeleteLoadForceWithGUID_{Point_Object}.htm)



## GetLoadPointWithGUID {Frame Object}

*Source file: `GetLoadPointWithGUID_{Frame_Object}.htm`*

# GetLoadPointWithGUID

## Syntax

SapObject.SapModel.FrameObj.GetLoadPointWithGUID

## VB6 Procedure

Function GetLoadPointWithGUID(ByVal Name As String, ByRef NumberItems As Integer, ByRef FrameName() As String, ByRef LoadPat() As String, ByRef MyType() As Integer, ByRef CSys() As String, ByRef Dir() As Integer, ByRef RelDist() As Double, ByRef Dist() As Double, ByRef Val() As Double, ByRef GUID() As String, Optional ByVal ItemType As eItemType = eItemType.Objects) As Long

## Parameters

Name

The name of an existing frame object or group depending on the value of the ItemType item.

NumberItems

The total number of point loads retrieved for the specified frame objects.

FrameName

This is an array that includes the name of the frame object associated with each point load.

LoadPat

This is an array that includes the name of the coordinate system in which the point loads are specified.

MyType

This is an array that includes 1 or 2, indicating the type of point load.

1 = Force

2 = Moment

CSys

This is an array that includes the name of the coordinate system in which each point load is defined. It may be Local or the name of a defined coordinate system.

Dir

This is an array that includes an integer between 1 and 11 indicating the direction of the load.

1 = Local 1 axis (only applies when CSys is Local)

2 = Local 2 axis (only applies when CSys is Local)

3 = Local 3 axis (only applies when CSys is Local)

4 = X direction (does not apply when CSys is Local)

5 = Y direction (does not apply when CSys is Local)

6 = Z direction (does not apply when CSys is Local)

7 = Projected X direction (does not apply when CSys is Local)

8 = Projected Y direction (does not apply when CSys is Local)

9 = Projected Z direction (does not apply when CSys is Local)

10 = Gravity direction (only applies when CSys is Global)

11 = Projected Gravity direction (only applies when CSys is Global)

The positive gravity direction (see Dir = 10 and 11) is in the negative Global Z direction.

RelDist

This is an array that includes the relative distance from the I-End of the frame object to the location where the point load is applied.

Dist

This is an array that includes the actual distance from the I-End of the frame object to the location where the point load is applied. [L]

Val

This is an array that includes the value of the point load. [F] when MyType is 1 and [FL] when MyType is 2

GUID

This is an array that includes the global unique ID of the point load.

ItemType

This is one of the following items in the eItemType enumeration:

Object = 0

Group = 1

SelectedObjects = 2

If this item is Object, the assignments are retrieved for the frame object specified by the Name item.

If this item is Group, the assignments are retrieved for all frame objects in the group specified by the Name item.

If this item is SelectedObjects, assignments are retrieved for all selected frame objects, and the Name item is ignored.

## Remarks

This function retrieves the point load assignments to frame objects.

The function returns zero if the load assignments are successfully retrieved, otherwise it returns a nonzero value.

## Release Notes

Initial release in version 17.2.0.

## See Also

[SetLoadPointWithGUID](SAP2000_API_Fuctions/Object_Model/Frame_Object/SetLoadPointWithGUID_{Frame_Object}.htm)

[DeleteLoadPointWithGUID](SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLoadPointWithGUID_{Frame_Object}.htm)



## Important Note

*Source file: `Important_Note.htm`*

# Important Note

This documentation applies to both SAP2000 and CSiBridge.

All examples in this documentation refer to SAP2000. However, users of CSiBridge should refer to CSiBridge. For example,

SAP2000 users can create an instance of the SapObject in VBA as follows

Dim myHelper As SAP2000v1.cHelper

Dim mySapObject As SAP2000v1.cOAPI

Set myHelper= New SAP2000v1.Helper

Set mySapObject = myHelper.CreateObjectProgID("CSI.SAP2000.API.SapObject")

whereas CSiBridge users would create an instance of the SapObject as follows

Dim myHelper As CSiBridge1.cHelper

Dim mySapObject As CSiBridge1.cOAPI

Set myHelper= New CSiBridge1.Helper

Set mySapObject = myHelper.CreateObjectProgID("CSI.CSiBridge.API.SapObject")

Other references to SAP2000/SAP2000.exe/SAP2000v1.dll/SAP2000v1.tlb in the documentation should be interpreted as CSiBridge/CSiBridge.exe/CSiBridge1.dll/CSiBridge1.tlb for users of CSiBridge.

Similarly, references to the .sdb extension in SAP2000 should be interpreted as the .bdb extension for users of CSiBridge.



## Introduction

*Source file: `Introduction.htm`*

# Introduction

The CSI Application Programming Interface (API) is a powerful tool that allows users to automate many of the processes required to build, analyze, and design models and to obtain customized analysis and design results. It also allows users to link SAP2000 or CSiBridge with third-party software, providing a path for two-way exchange of model information with other programs. Please note that SAP2000 or CSiBridge must be installed both on the API client development machine, and on the client end-user's machine.

Most major programming languages can be used to access SAP2000 and CSiBridge through the API. Detailed examples are provided for several popular programming languages, including Visual Basic, C#, Python, MATLAB, Fortran, and Visual Basic for Applications (VBA), which is included in programs such as Microsoft Excel.

With the release of SAP2000 and CSiBridge v26.0.0, the API is defined in the form of a .NET Standard 2.0 dynamic link library (DLL) for improved compatibility with a large variety of client applications. Please refer to the Release Notes page.

This documentation is organized into the following main categories:

* Release Notes explains recent changes in the API, and include instructions for users on how to update their client applications.
* **Getting Started** briefly explains how to use the CSI API and how the CSI API functions are documented.
* **CSI API Functions** identifies each function available in the API and provides an example of how the function might be called using Visual Basic for Applications (VBA).
* **Example Code** provides programming examples using the CSI API. These examples are more extensive than those included with the documentation of each function.
* Obsolete Functions are the result of changes to the software or the API. These obsolete functions have been superseded, but continue to be included to accommodate backwards compatibility.
* Breaking Changes lists recent changes to the API that might break some API clients.
* Plugins explains how to develop and use plugins that can be accessed via program menus.
* Database Tables (Interactive Editing) documents each function available in DatabaseTables class for accessing database tables through the API.
* Alphabetized List of Functions lists all function in alphabetical order.

See Also

[Accessing SAP2000 From An External Application](Getting_Started/Accessing_Sap2000_From_An_External_Application.htm)

[Function Documentation Conventions](Getting_Started/Function_Documentation_Conventions.htm)

[Function Return Values](Getting_Started/Function_Return_Values.htm)

[Units Abbreviations](Getting_Started/Units_Abbreviations.htm)

[Visual Basic Concepts Used In the CSI API](Getting_Started/Visual_Basic_Concepts_Used_In_The_Sap2000_API.htm)



## Launching the Installed Version of SAP2000/CSiBridge Automatically

*Source file: `Launching_the_Installed_Version_of_SAP2000_CSiBridge_Automatically.htm`*

# Launching the Installed Version of SAP2000/CSiBridge Automatically

With the release of SAP2000 and CSiBridge v19.1.0, new functionality has been added to the cHelper interface to allow users to launch the application without supplying the path to the program executable file. The example code is in Visual Basic.

1. Previously, users would launch the program with the function cHelper.CreateObject , providing the full path to the SAP2000.exe as an argument, as below:

Dim mySapObject As SAP2000v19.cOAPI

Dim myHelper as SAP2000v19.cHelper = New SAP2000v19.Helper

mySapObject = myHelper.CreateObject("C:\Program Files (x86)\Computers and Structures\SAP2000 19\SAP2000.exe")

ret = mySapObject.ApplicationStart()

Dim mySapModel As SAP2000v19.cSapModel = mySapObject.SapModel

2. While the code above is still available, a simpler method has been added to cHelper. The CreateObjectProgID function takes the Program ID as an argument, and automatically launches the most recently installed version of SAP2000 or CSiBridge:

Dim mySapObject As SAP2000v19.cOAPI

Dim myHelper as SAP2000v19.cHelper = New SAP2000v19.Helper

mySapObject = myHelper.CreateObjectProgID("CSI.SAP2000.API.SapObject")

ret = mySapObject.ApplicationStart()

Dim mySapModel As SAP2000v19.cSapModel = mySapObject.SapModel

For reference, the Program ID for CSiBridge users is "CSI.CSiBridge.API.SapObject"



## Main

*Source file: `Main.htm`*

Welcome
to CSI API Documentation

Quick Links
   [IMPORTANT NOTE](Important_Note.htm)
    [Introduction](Introduction.htm)

©
by Computers & Structures, Inc., 1978-2024

SAP2000 is a registered trademark of Computers & Structures, Inc.
CSiBridge is a registered trademark of Computers & Structures, Inc.

The computer programs
SAP2000®, CSiBridge®,
and all associated documentation are proprietary and copyrighted products.
Worldwide rights of ownership rest with Computers & Structures, Inc.
Unlicensed use of the program or reproduction of the documentation in
any form, without prior written authorization from Computers & Structures,
Inc., is explicitly prohibited.

Further information and copies
of this documentation may be obtained from:

Computers
& Structures, Inc.

[www.csiamerica.com](http://www.csiamerica.com)

[info@csiamerica.com](mailto:info@csiamerica.com)
(for general information)

[support@csiamerica.com](mailto:support@csiamerica.com)
(for technical support)



## Remote API

*Source file: `Remote_API.htm`*

# Remote API

The SAP2000 API can be used to start and/or connect
to a running instance of SAP2000 on a remote computer that is running
the API Service. This can be particularly useful if you need to run a
large number of load cases (e.g., earthquakes for performance-based design,
moving load cases for bridge design, etc.), and there are multiple machines
available for running analyses simultaneously.

Simultaneous runs can be started on multiple Remote
Computers using an API script or plug-in, and results can be merged to
the Main Computer programmatically, without user intervention, as they
become available. Other applications could include using distributed processing
to run a large parameter study or Monte Carlo simulation.

Terminology

**Main
Computer**: Your primary computer.

**Remote
Computer**: Any other computer that you have access to (physically or
over the network) and that is available for running analyses and/or API
scripts.

**API
Service**: “CSiAPIService.exe” command line utility running on a remote
computer that enables Remote API.

**TCP
Port**: A TCP (Transmission Control Protocol) port is an integer between 0
to 65535 used to identify which service is to receive a packet/message
sent to a Remote Computer.

Requirements & Limitations

Depending on the type of firewall
installed on a Remote Computer, you may have to create a firewall exception
on that Remote Computer to allow the API Service to communicate on your
network. This is done automatically for Windows Firewall during the installation
of SAP2000, but it may have to be manually done for other firewalls and
will require administrative privileges. This is typically a one-time operation.

The
API Service has two modes:

Product-Specific:

+ Listens to
  connections made from SAP2000v1.dll at default TCP port 11650. (For CSiBridge1.dll , the port is 11649 )
+ This is the
  default mode and can be started using the following command:
  “CSiAPIService.exe” or “CSiAPIService.exe --api A”

Cross-Product:

+ Listens to
  connections made from CSiAPIv1.dll at default TCP port 11646.
+ This
  can be started using the following command:
  “CSiAPIService.exe --api C”

Multiple
API Service instances can be run simultaneously on a Remote Computer as
long as they do not use the same TCP port. In case of TCP port conflicts
with other programs, it is possible to assign a specific TCP port to each
API Service instance using the following command:

“CSiAPIService.exe
--port [portNumber]”

where
[portNumber] is between 1024 and 49151.

It is
also possible to override the default TCP port for Product-Specific and
Cross-Product API modes using the following Windows environment variables:

Product-Specific:
“SAP2000v1\_cOAPI\_DEFAULT\_PORT” (For CSiBridge, use “CSiBridge1\_cOAPI\_DEFAULT\_PORT”)

Cross-Product:
“CSiAPIv1\_cOAPI\_DEFAULT\_PORT”

Procedure

Install
the SAP2000 on the Main and Remote Computers.

On
each Remote Computer, open a command prompt and run “CSiAPIService.exe”,
located in the SAP2000 installation folder, to start the API Service.

**Tip**:
Type “CSiAPIService.exe --help” to view a detailed list of options where
you can set

+ The TCP
  port to use.
+ API mode:
  Product-specific or Cross-product.

**Tip**:
You can set the API Service to run automatically when your computer starts
(see [Change
which apps run automatically at startup in Windows 10](https://support.microsoft.com/en-us/help/4026268/windows-10-change-startup-apps) for details).

On
your Main Computer, run a script, program, or SAP2000 Plug-in that uses
one of the following API calls to start (CreateObject…) or connect to
(GetObject…) an instance of SAP2000 on a Remote Computer:

cHelper.CreateObjectHost(

ByVal hostName As String,

ByVal fullPath As String)

cHelper.CreateObjectHostPort(

ByVal hostName As String,

ByVal portNumber As Integer,

ByVal fullPath As String)

cHelper.CreateObjectProgIDHost(

ByVal hostName As String,

ByVal progID As String)

cHelper.CreateObjectProgIDHostPort(

ByVal hostName As String,

ByVal portNumber As Integer,

ByVal progID As String)

cHelper.GetObjectHost(

ByVal hostName As String,

ByVal progID As String)

cHelper.GetObjectHostPort(

ByVal hostName As String,

ByVal portNumber As Integer,

ByVal progID As String)

The above API calls receive the name of the Remote
Computer (e.g. hostName = “myserver”), and optionally a TCP port number,
in addition to the arguments of the regular cHelper.CreateObject() or
GetObject() API calls. Upon successful instantiation at a Remote Computer,
subsequent calls to the returned cOAPI object will execute on the Remote
Computer. API calls can be used to open models, modify them, run analysis
and design, extract results, and/or merge results back to identical models
on the Main Computer.

## Release Notes

Initial release in version 22.1.0



## SetLoadDistributedWithGUID {Cable Object}

*Source file: `SetLoadDistributedWithGUID_{Cable_Object}.htm`*

# SetLoadDistributedWithGUID

## Syntax

SapObject.SapModel.CableObj.SetLoadDistributedWithGUID

## VB6 Procedure

Function SetLoadDistributedWithGUID (ByVal Name As String, ByVal LoadPat As String, ByVal MyType As Long, ByVal Dir As Long, ByVal Value As Double, ByRef GUID As String, Optional ByVal CSys As String = "Global", Optional ByVal Replace As Boolean = True) As Long

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

GUID

This is the global unique ID of a distributed load assigned to the cable object or if it is not the global unique ID of a distributed load assigned to the cable object and it is not blank, the global unique ID which is assigned to the newly assigned load. If left blank, a new load assigned to the cable object and the value of this parameter is set to the global unique ID of the newly assigned load.

CSys

This is Local or the name of a defined coordinate system. It is the coordinate system in which the loads are specified.

Replace

If this item is True and the input GUID is not the GUID of any distributed load assigned to the cable object, all previous distributed loads, if any, assigned to the specified cable object, in the specified load pattern, are deleted before making the new assignment. If the input GUID is the GUID of a distributed load already assigned to the frame object, the parameters of the distributed load are updated with the values provided and this item is ignored.

If this item is True, all previous loads, if any, assigned to the specified cable object(s), in the specified load pattern, are deleted before making the new assignment.

## Remarks

If the cable object is already assigned a distributed load with a global unique ID matching the specified global unique ID, this function modifies that distributed load. Otherwise, this function assigns a new distributed load over the full length of the cable object and sets its global unique ID to the specified global unique ID.

This function assigns uniform distributed loads over the full length of cable objects.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## Release Notes

Initial release in version 17.2.0.

## See Also

[GetLoadDistributedWithGUID](GetLoadDistributedWithGUID_{Cable_Object}.htm)

[DeleteLoadDistributedWithGUID](SAP2000_API_Fuctions/Object_Model/Cable_Object/DeleteLoadDistributedWithGUID_{Cable_Object}.htm)



## SetLoadDistributed {Frame Object}

*Source file: `SetLoadDistributed_{Frame_Object}.htm`*

# SetLoadDistributedWithGUID {Frame Object}

## Syntax

SapObject.SapModel.FrameObj.SetLoadDistributedWithGUID

## VB6 Procedure

Function SetLoadDistributedWithGUID(ByVal Name As String, ByVal LoadPat As String, ByVal MyType As Long, ByVal Dir As Long, ByVal Dist1 As Double, ByVal Dist2 As Double, ByVal Val1 As Double, ByVal Val2 As Double, ByRef GUID As String, Optional ByVal CSys As String = "Global", Optional ByVal RelDist As Boolean = True, Optional ByVal Replace As Boolean = True) As Long

## Parameters

Name

The name of an existing frame object.

LoadPat

The name of a defined load pattern.

MyType

This is 1 or 2, indicating the type of distributed load.

1 = Force per unit length

2 = Moment per unit length

Dir

This is an integer between 1 and 11, indicating the direction of the load.

1 = Local 1 axis (only applies when CSys is Local)

2 = Local 2 axis (only applies when CSys is Local)

3 = Local 3 axis (only applies when CSys is Local)

4 = X direction (does not apply when CSys is Local)

5 = Y direction (does not apply when CSys is Local)

6 = Z direction (does not apply when CSys is Local)

7 = Projected X direction (does not apply when CSys is Local)

8 = Projected Y direction (does not apply when CSys is Local)

9 = Projected Z direction (does not apply when CSys is Local)

10 = Gravity direction (only applies when CSys is Global)

11 = Projected Gravity direction (only applies when CSys is Global)

The positive gravity direction (see Dir = 10 and 11) is in the negative Global Z direction.

Dist1

This is the distance from the I-End of the frame object to the start of the distributed load. This may be a relative distance (0 <= Dist1 <= 1) or an actual distance, depending on the value of the RelDist item. [L] when RelDist is False

Dist2

This is the distance from the I-End of the frame object to the end of the distributed load. This may be a relative distance (0 <= Dist2 <= 1) or an actual distance, depending on the value of the RelDist item. [L] when RelDist is False

Val1

This is the load value at the start of the distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2

Val2

This is the load value at the end of the distributed load. [F/L] when MyType is 1 and [FL/L] when MyType is 2

GUID

This is the global unique ID of a distributed load assigned to the frame object or if it is not the global unique id of a distributed load assigned to the frame object and it is not blank, the global unique ID which is assigned to the newly assigned load. If left blank, a new load is assigned to the frame object and the value of this parameter is set to the global unique ID of the newly assigned load.

CSys

This is Local or the name of a defined coordinate system. It is the coordinate system in which the loads are specified.

RelDist

If this item is True, the specified Dist item is a relative distance, otherwise it is an actual distance.

Replace

If this item is True and the input GUID is not the GUID of any distributed load assigned to the frame object, all previous distributed loads, if any, assigned to the specified frame object, in the specified load pattern, are deleted before making the new assignment. If the input GUID is the GUID of a distributed load already assigned to the frame object, the parameters of the distributed load are updated with the values provided and this item is ignored

## Remarks

If the frame object is already assigned a distributed load with a global unique ID matching the specified global unique ID, this function modifies that distributed load. Otherwise, this function assigns a new distributed load to the frame object and sets its global unique ID to the specified global unique ID.

The function returns zero if the loads are successfully assigned, otherwise it returns a nonzero value.

## Release Notes

Initial release in version 17.2.0.

## See Also

[GetLoadDistributedWithGUID](SAP2000_API_Fuctions/Object_Model/Frame_Object/GetLoadDistributed_{Frame_Object}.htm)

[DeleteLoadDistributedWithGUID](SAP2000_API_Fuctions/Object_Model/Frame_Object/DeleteLoadDistributed_{Frame_Object}.htm)



## SetLoadForceWithGUID {Point Object}

*Source file: `SetLoadForceWithGUID_{Point_Object}.htm`*

# SetLoadForceWithGUID {Point Object}

## Syntax

SapObject.SapModel.PointObj.SetLoadForceWithGUID

## VB6 Procedure

Function SetLoadForceWithGUID(ByVal Name As String, ByVal LoadPat As String, ByRef Value() As Double, ByRef GUID As String, Optional ByVal Replace As Boolean = False, Optional ByVal CSys As String = "Global") As Long

## Parameters

Name

The name of an existing point object.

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

GUID

This is the global unique ID of a load force assigned to the point object or if it is not the global unique id of a load force assigned to the point object and it is not blank, the global unique ID which is assigned to the newly assigned load. If left blank, a new load is assigned to the point object and the value of this parameter is set to the global unique ID of the newly assigned load.

Replace

If this item is True and the input GUID is not the GUID of any load force assigned to the point object, all previous loads force, if any, assigned to the specified point object, in the specified load pattern, are deleted before making the new assignment. If the input GUID is the GUID of a load force already assigned to the point object, the parameters of the distributed load are updated with the values provided and this item is ignored.

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

## Release Notes

Initial release in version 17.2.0.

## See Also

[GetLoadForceWithGUID](GetLoadForceWithGUID_{Point_Object}.htm)

[DeleteLoadForceWithGUID](DeleteLoadForceWithGUID_{Point_Object}.htm)

