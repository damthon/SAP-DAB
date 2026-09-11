# Getting Started

Source: CSI OAPI Documentation (SAP2000) — Getting_Started

---



## Accessing SAP2000 From An External Application

*Source file: `Getting_Started/Accessing_Sap2000_From_An_External_Application.htm`*

# Accessing SAP2000 From An External Application

This page contains an outline for connecting to the SAP2000 API, with VBA code examples. For specific instructions for supported programming languages, please refer to the Example Code section.

The first step in using the CSI API from an external application is to reference SAP2000v1.dll or SAP2000v1.tlb from your application. If using Excel VBA, reference SAP2000v1.TLB by opening the VBA editor, clicking the Tools menu > References command and selecting SAP2000v1.TLB from the program installation folder.

Next, within your application, you will create a variable of interface type cOAPI, and an instance of the SAP2000 object which implements cOAPI. In VBA this could be accomplished as:

Dim mySapObject As SAP2000v1.cOAPI

Dim myHelper As SAP2000v1.cHelper

Set myHelper = New SAP2000v1.Helper
Set mySapObject = myHelper.CreateObject(ProgramPath)

The first line creates the interface variable, the second and third lines create a helper class, and the fourth line creates the instance of the SAP2000 object which implements the interface by passing in the path to where the SAP2000.exe program is located. Now that an instance of the SAP2000 object has been created in your application, start SAP2000 using the following VBA command:

SapObject.ApplicationStart

At this point you can open an existing model, or create a new one and perform whatever actions are required. In general, the API commands are accessed through SapObject.SapModel.

It may be helpful to define a SapModel variable so that the API commands are accessed through SapModel instead of SapObject.SapModel. In VBA this could be accomplished as:

Dim mySapModel As cSapModel
Set mySapModel= mySapObject.SapModel

When finished with a model, you may want to close the SAP2000 application. This can be accomplished using the following VBA command:

SapObject.ApplicationExit  True

As a last step, the SapModel and SapObject variables should always be set to Nothing. In VBA this is accomplished as:

Set SapModel= Nothing
Set SapObject= Nothing

Setting the variables to Nothing is a very important step. It breaks the connection between your application and SAP2000 and frees up system resources. If the variables are not set to Nothing, the SAP2000 application may not completely close (you may still see it running in your Windows Task Manager).

Putting all the steps previously described into a single example, a VBA program might consist of the following:

Sub MyProgram
   'dimension variables
      Dim mySapObject As SAP2000v1.cOAPI

      Dim myHelper As SAP2000v1.cHelper
      Dim mySapModel As cSapModel
      Dim ret As Long

   'create an instance of the SAP2000 object

      Set myHelper= New SAP2000v1.Helper
      Set mySapObject= myHelper.CreateObject("C:\Program Files (x86)\Computers and Structures\SAP2000 21\sap2000.exe")

   'start the SAP2000 application
      mySapObject.ApplicationStart

   'create the SapModel object
      Set mySapModel= mySapObject.SapModel

   'initialize model
      ret = mySapModel.InitializeNewModel

   'call SAP2000 API functions here to perform desired tasks
   'in this example a new 2D frame is created from template
      ret = mySapModel.File.New2DFrame(PortalFrame, 3, 124, 3, 200)

   'close the SAP2000 application, if desired
      mySapObject.ApplicationExit False

   'set the objects to Nothing
   'at the end of your program ALWAYS terminate the objects in this manner
      Set mySapModel= Nothing
      Set mySapObject= Nothing
End Sub

See Also

[Introduction](../Introduction.htm)

[Function Documentation Conventions](Function_Documentation_Conventions.htm)

[Function Return Values](Function_Return_Values.htm)

[Units Abbreviations](Units_Abbreviations.htm)

[Visual Basic Concepts Used in the CSI API](Visual_Basic_Concepts_Used_In_The_Sap2000_API.htm)



## Creating an API client in DotNet 6

*Source file: `Getting_Started/Creating_an_API_client_in_DotNet_6.htm`*

# Creating an API client in .NET 6 (for programs older than v26.0.0)

The SAP2000 (or CSiBridge) API is provided as a .NET Framework 4.7.1 class library. The .NET remoting libraries used by the SAP2000 API are no longer supported in .NET 6 . The Visual Basic or C# examples provided in this help file can be compiled in a .NET 6 client but will produce a runtime error.

Users who must create a .NET 6 client can still access the SAP2000 API using COM. This can be done by changing one line in the example code:

## Original Visual Basic Example:

'create API helper object

 Dim myHelper As cHelper

 Try

     myHelper = New Helper

 Catch ex As Exception

     MsgBox("Cannot create an instance of the Helper object")

 End Try

## Modified Visual Basic Example:

'create API helper object

Dim myHelper As cHelper

Try

      myHelper = Activator.CreateInstance(Type.GetTypeFromProgID("SAP2000v1.Helper", True))

Catch ex As Exception

      MsgBox("Cannot create an instance of the Helper object")

End Try

## Original C# Example:

//create API helper object

cHelper myHelper;

try

{

    myHelper = new Helper();

}

catch (Exception ex)

{

    Console.WriteLine("Cannot create an instance of the Helper object");

    return;

}

## Modified C# Example:

//create API helper object

cHelper myHelper;

try

{

    myHelper = (cHelper)Activator.CreateInstance(Type.GetTypeFromProgID("SAP2000v1.Helper", true));

}

catch (Exception ex)

{

    Console.WriteLine("Cannot create an instance of the Helper object");

    return;

}



## Function Documentation Conventions

*Source file: `Getting_Started/Function_Documentation_Conventions.htm`*

# Function Documentation Conventions

The documentation of each function in the API has the following sections:

Syntax

This section provides the syntax of the command as you would call it from an external application without including any parameters

VB6 Procedure

The VB6 procedure shows the function as defined in SAP2000. This function definition shows the variable type of each parameter, which parameters are optional, and which optional parameters have built-in default values.

See [Visual Basic Concepts Used in the CSI API](Visual_Basic_Concepts_Used_In_The_Sap2000_API.htm) for more information about Visual Basic definitions that apply to the CSI API.

Parameters

The Parameters used in the function are briefly described. Parameters that have units associated with them are followed by a [units abbreviation](Units_Abbreviations.htm) in square brackets, such as [F], indicating the units type for the item.

Remarks

The Remarks describe what the function does and provides additional information, if any, that was not explained in the Parameters. See [Function Return Values](Function_Return_Values.htm) for more information.

VBA Example

The VBA example uses the considered function. The examples are written for use in Microsoft Excel VBA.

Release Notes

The release information specific to the considered function is provided.

See Also

Functions that are related to the considered function, if any, are listed in this area.

See Also

[Introduction](../Introduction.htm)

[Accessing SAP2000 From An External Application](Accessing_Sap2000_From_An_External_Application.htm)

[Function Return Values](Function_Return_Values.htm)

[Units Abbreviations](Units_Abbreviations.htm) [Visual Basic Concepts Used in the CSI API](Visual_Basic_Concepts_Used_In_The_Sap2000_API.htm)



## Function Return Values

*Source file: `Getting_Started/Function_Return_Values.htm`*

# Function Return Values

Almost all CSI API functions return a Long (32 bit signed integer) value indicating if the function executed successfully.

A return value of 0 indicates that SAP2000 successfully executed the function.

Any nonzero return value indicates that the function was not successfully executed.

See Also

[Introduction](../Introduction.htm)

[Accessing SAP2000 From An External Application](Accessing_Sap2000_From_An_External_Application.htm)

[Function Documentation Conventions](Function_Documentation_Conventions.htm)

[Units Abbreviations](Units_Abbreviations.htm)

[Visual Basic Concepts Used in the CSI API](Visual_Basic_Concepts_Used_In_The_Sap2000_API.htm)



## Information for Plugin Developers

*Source file: `Getting_Started/Information_for_Plugin_Developers.htm`*

# Information for Plugin Developers

This topic contains the following sections:

* [Plugin Considerations](#Plugin_Considerations:_)
* [The cPlugin Class](#The_cPlugin_Class:)
* [Adding Plugins](#Adding_Plugins)

As an alternative to external API clients, plugins that are accessible via SAP2000 menus can be developed to make use of the SAP2000 API from inside the program.

No license is required to use the API for plugin development, beyond having a valid license for SAP2000 or CSiBridge. However, technical support for developing with the API is not included. For qualified users and third-party developers who would like technical support to help them build solutions and integrations with SAP2000 using the SAP2000 API, Computers and Structures, Inc., has created a subscription-based service, CSI Developer Network (CSIDN)  (see <https://www.csiamerica.com/support>). You would need to subscribe to CSIDN to be eligible for technical support for SAP2000 API.

Plugins can be developed in a .NET compatible language (e.g. Visual Basic, C#, etc.), as a .NET DLL, or by using any language capable of creating a COM server compiled as a DLL. An example plugin project can be found at [CSI Knowledge Base Sample Plugins](https://redirects.csiamerica.com/wiki/x/cod0)

## Plugin Considerations:

### General

The plugin must reference the SAP2000v1 API library (either SAP2000v1.dll for .NET based or SAP2000v1.tlb for COM based plugins), which must be registered on the developer’s and the user’s systems. This registration takes place during the installation of SAP2000, but can be repeated whenever necessary by running the RegisterSAP2000.exe utility included in the program installation folder.

The SAP2000 program targets .NET 8 and is compatible with 64-bit and AnyCPU-compiled plugins referencing SAP2000v1.dll and targeting .NET Standard 2.0, .NET Framework 4.6.1 and newer (including the latest - 4.8.1), .NET Core/.NET 2.0 and newer (including the latest - 8.0) along with 64-bit plugins exposed as COM objects. Any kind of 32-bit plugins are not supported.

Please make sure your plugin is stable, handles errors well, and does not cause any unintended changes to the user’s model as actions performed by plugins are not undoable.

We will attempt to maintain a stable interface in SAP2000, however, that cannot be guaranteed, and updates to your plugin may be required for future versions of SAP2000.

### Plugins Targeting .NET Framework

Please note that plugins targeting .NET Framework

* Should NOT use .NET Framework technologies unavailable on .NET. See <https://learn.microsoft.com/en-us/dotnet/core/porting/net-framework-tech-unavailable> for details.
* Should NOT include SAP2000v1.dll in the plugin folder to prevent conflicts with SAP2000v1.dll located in the program folder.

### Plugins Targeting .NET Core/.NET

Please note that plugins targeting .NET Core/.NET

* Should NOT include SAP2000v1.dll in the plugin folder to prevent conflicts with SAP2000v1.dll located in the program folder.
* Should include all other dependencies of the plugin in the plugin folder.

See <https://learn.microsoft.com/en-us/dotnet/core/tutorials/creating-app-with-plugin-support#simple-plugin-with-no-dependencies> for details.

### Plugins Exposed as COM Objects

Please note that plugins exposed as COM objects

* Must be registered for COM on the user’s system, preferably after SAP2000 has been installed.
* Will require administrative rights to register, which many end users may not have.

It is the plugin developer's responsibility to instruct users how to install the plugin.

### Plugin Compatibility

Please consider the following recommendations when implementing a plugin based on the plugin's functionality and its target audience.

* For simple plugins with no user interface, targeting .NET Standard 2.0 should ensure maximum compatibility with old, current, and future versions of SAP2000.
* For more complex plugins with a user interface, targeting .NET Framework 4.8 should ensure maximum compatibility with old, current, and future versions of SAP2000, provided that the plugin does not use .NET Framework technologies unavailable on .NET.
* For plugins meant to be used with SAP2000 v26.0.0 and later, targeting .NET 8 should enable latest .NET functionality while ensuring maximum compatibility with current and future versions of SAP2000.
* Plugins developed using native languages like C, C++, can be exposed as COM objects. Unlike plugins targeting a version of .NET, plugins exposed as COM objects will need to be registered before they can be used.

## The cPlugin Class:

In order for SAP2000 to be able to launch your plugin, your plugin assembly must contain a class called cPlugin that implements the cPluginContract interface in the SAP2000 API.

Please refer to the [cPluginContract](../SAP2000_API_Fuctions/PlugIns/cPluginContract_Methods/cPluginContract.htm) page for an explanation of its methods. They are also described below.

Class cPlugin  must contain two methods, cPlugin.Info and cPlugin.Main

Public Function Info(ByRef Text As String) As Integer

The function cPlugin.Info has one reference argument, Text, and returns a 32-bit signed integer. The return value should be zero if successful. The string argument should be filled in by the function, and may be plain text or rich text. This string will be displayed when the user first adds the plugin to SAP2000. You can use this string to tell the user the purpose and author of the plugin. This is in addition to any information you may provide when the user executes the plugin.

Public Sub Main(ByRef SapModel As SAP2000v1.cSapModel, ByRef ISapPlugin As SAP2000v1.cPluginCallback)

The subroutine cPlugin.Main is the entry point to launch your plugin. All functionality in your plugin will proceed from this method. If your plugin has an initial form, it should be opened within this method.

cPlugin.Main has two reference arguments of types SAP2000v1.cSapModel and SAP2000v1.cPluginCallback:

The SapModel argument is a reference to the SapModel object upon which all operations will be performed

For the ISapPlugin argument, please refer to the  [cPluginCallback](../SAP2000_API_Fuctions/PlugIns/cPlugincallback_Properties/cPluginCallback_Interfacey.htm)  page for an explanation of its properties. Its only method is very important and explained below.

SAP2000v1.cPluginCallback.Finish(ByVal iVal As Integer)

SAP2000v1.cPluginCallback contains a Finish  subroutine that is to be called immediately before the plugin closes (e.g., if the plugin has a single main window, at the end of the close event of that form). Its one argument, iVal, is an error flag to let SAP2000 know if the operation was successful or not. Zero indicates no error. SAP2000 will wait indefinitely for SAP2000v1.cPluginCallback.Finish to be called, so the plugin programmer must make sure that it is called when the plugin completes

It is OK for  cPlugin.Main  to return before the actual work is completed (e.g., return after displaying a form where the functionality implemented in the plugin can be accessed through different command buttons). However, it is imperative to remember to call  SAP2000v1.cPluginCallback.Finish  to return the control back to SAP2000 when the plugin is ready to close.

Your plugin should include options for the user to obtain information about the product, developer, and technical support. Support for your plugin will not be provided by Computers and Structures, Inc.

As currently implemented, the cPlugin object will be destroyed between invocations from the SAP2000 Tools menu command that calls it, so data cannot be saved.

## Adding Plugins

![](../assets/images/External_Plugin_Data_form.png)

### Adding a COM Plugin

To add a COM plugin to the Tools menu in SAP2000, users will select "Add/Show Plugins" from the Tools menu. In the External Plugin Data form, they will type the name of the COM server DLL in the "Plugin Name" field.

Please note that SAP2000 will look for the plugin by Type Library name (usually the name of the plugin project), which you define when developing your COM server DLL. We suggest using a unique name such as SAP2000PlugIn\_xxx\_yyy, where xxx is your (company) name, and yyy is the name to distinguish the plugin from other plugins that you develop, e.g. SAP2000PlugIn\_OmniCorp\_Robo1.

The "Plugin Name" must exactly match the COM server DLL name. However, the plugin will appear under the Tools menu under the "Menu Text" name. That can be whatever the user likes, but it should be different for each plugin added.

The "Plugin Path" field should be left blank for COM plugins.

After clicking the "Add" button, the "Status" field will indicate whether the plugin was successfully located in the registry and loaded.

### Adding a .NET Plugin

The process for adding a .NET plugin is much simpler. In the External Plugin Data form, the user should simply browse for and select the plugin .NET DLL and click the "Add" button. The rest of the fields will be automatically populated. It is still recommended that .NET plugins be given unique names.



## Interactive Database

*Source file: `Getting_Started/Interactive_Database.htm`*

# Interactive Database

Beginning
with Version 23.0.0, SAP2000 and CSIBridge allow database tables to be
accessed through the API using the DatabaseTables
class.
It is recommended that API users first familiarize themselves with the
database tables using the SAP2000 (or CSiBridge) GUI, to understand how
data can be requested, viewed, modified, and applied to the model.

Generally,
the API user will start with a call
to [GetAvailableTables](../Database_Tables/GetAvailableTables.htm).
They can decide which tables they want to retrieve data from, or edit
and apply to the model. A call to [GetAllFieldsInTable](../Database_Tables/GetAllFieldsInTable.htm)
will
show the user which columns the table has, and which columns can be edited
and imported.

If
the user simply wants to retrieve data, they can use one of the
[GetTableForDisplay](../Database_Tables/GetTableforDisplayArray.htm)...functions.
Functions are provided to set the Load Cases, Load Combinations, Load
Patterns, Generalized Displacements, Section Cuts, Pushover Named Sets,
Plot Function Traces Named Sets, Joint Response Spectra Named Sets, and
Element Virtual Work Named Sets for which data is desired. The
[SetTableOutputOptionsForDisplay](../Database_Tables/GetTableOutputOptionsForDisplay.htm)
function
can be used to set other options for display.

If
the user would like to edit a table and import it into the model, they
should start by calling one of the [GetTableForEditing](../Database_Tables/GetTableForEditingArray.htm)...functions.
This will retrieve the table data in one of several formats. The user
can then edit that data, but they must ensure that the format of the data
is not altered. Then they can import the edited table data with the respective
[SetTableForEditing](../Database_Tables/SetTableforEditingArray.htm)...function.
These functions only operate on one table at a time, but any number of
edited tables can be imported by calling them successively. Finally, to
apply the edited tables to the model, the user will call [ApplyEditedTables](../Database_Tables/ApplyEditedTables.htm).
If for any reason the user would like to clear the internal list of edited
tables set using the [SetTableForEditing](../Database_Tables/SetTableforEditingArray.htm)...
functions,
they can call the [CancelTableEditing](../Database_Tables/CancelTableEditing.htm)
function.

For
thorough descriptions of database table operations, please refer to the
function documentation in DatabaseTables



## Units Abbreviations

*Source file: `Getting_Started/Units_Abbreviations.htm`*

# Units Abbreviations

In the documentation of each CSI API function, parameters that have units associated with them are followed by one of the following abbreviations, to indicate the units for those parameters.

[L] = Length

**[F]** = Force,  [F] = [ML/s2]

**[M]** = Mass

**[s]** = Time, seconds

**[T]** = Temperature

**[cyc]** = Cycles

**[rad]** = Radians (angle measurement)

**[deg]** = Degrees (angle measurement)

Combinations of these abbreviations are used in many cases. For example, moments are indicated as **[FL]** and stresses are indicated as **[F/L2]**.

See Also

[Introduction](../Introduction.htm)

[Accessing SAP2000 From An External Application](Accessing_Sap2000_From_An_External_Application.htm)

[Function Documentation Conventions](Function_Documentation_Conventions.htm)

[Function Return Values](Function_Return_Values.htm)

[Visual Basic Concepts Used in the CSI API](Visual_Basic_Concepts_Used_In_The_Sap2000_API.htm)



## Update to .NET Standard 2.0

*Source file: `Getting_Started/Update_to_.NET_Standard_2.htm`*

# Update to .NET Standard 2.0

With the release of SAP2000 v26.0.0, the API is compiled as a .NET Standard 2.0 AnyCPU dynamic link library (DLL) and supports an increased range of 32-bit and 64-bit API clients targeting .NET Framework 4.6.1 and newer (including the latest - 4.8.1), .NET Core/.NET 2.0 and newer (including the latest - 8.0), along with clients accessing the API via COM. While the file version of the library has been incremented to 2.0.0, the name of the library remains the same, **SAP2000v1.dll**, and source code compatibility with earlier versions is preserved.

Most API developers should be able to update their client applications to reference the latest API without significant disruption, and are encouraged to do so for maximum compatibility with old, current, and future versions of SAP2000. Please refer to the provided examples to see if your client application requires any code changes.

## Forward Compatibility

.NET based client applications referencing older versions of the API library (file version < 2.0.0) **will no longer work with SAP2000 v26.0.0 and newer.** Client applications accessing the API via COM will continue to work. API developers are encouraged to update their clients to reference the latest API for maximum compatibility with old, current, and future versions of SAP2000.

## Backwards Compatibility and Error Handling

.NET based client applications referencing the latest version of the API library and client applications accessing the API via COM are both expected to work with old, current, and future versions of SAP2000 and API developers are encouraged to update their clients to reference the latest API.

Client applications that use the new API library will also benefit from improved error handling. When trying to use a function that is not supported in the version of SAP2000 to which they are connected, a catchable exception with an informative error message will be thrown:

![](../assets/images/Picture1.png)

## Remote API Disabled

The Remote API feature, used to start and/or connect to a running instance of SAP2000 on a Remote Computer, has been disabled with the release of SAP2000 v.26.0.0. This functionality may be added back to the program in a future release. Please refer to the page, Breaking changes in v26.0.0

## Late Binding in VBA Disabled

In SAP2000 v26.0.0 and later, the API is compiled as a .NET Standard 2.0 AnyCPU dynamic link library (DLL). Previously it had been compiled as a .NET Framework 4.7.1 AnyCPU DLL. Due to that change, certain late binding VBA calls that may have worked in earlier versions of the API will no longer work. CSI recommends using early binding for VBA, and all other, API client applications, as documented in this help file.



## Using the Cross-Product API Library

*Source file: `Getting_Started/Using_the_Cross-Product_API_Library.htm`*

# Using the Cross-Product API Library

Starting with Version 21 of SAP2000, API developers have access to a powerful new tool to create API client applications that can work with multiple CSI programs.

New releases of SAP2000, CSiBridge, ETABS, and SAFE all contain a new API library, CSiAPIv1.dll . This library is compatible with all four programs.

Developers can now create API client applications that reference CSiAPIv1.dll , and connect to either SAP2000, CSiBridge, ETABS, or SAFE, without any code changes required.

For more information and examples of how to use CSiAPIv1.dll , please see: [CSI Knowledge Base Cross Product API Examples](https://redirects.csiamerica.com/wiki/x/BoDgCQ)



## Visual Basic Concepts Used In The SAP2000 API

*Source file: `Getting_Started/Visual_Basic_Concepts_Used_In_The_Sap2000_API.htm`*

# Visual Basic Concepts Used in the CSI API

Some of the Visual Basic concepts and definitions that apply to the CSI API are explained herein.

Option Base

Visual Basic 6 allows the default lower bound for arrays to be specified as 0 (the default), or 1. SAP2000 uses a lower bound of 0 for all arrays. Any program that accesses SAP2000 through the API should also use a lower bound of 0 for its arrays.

Fixed-Size and Dynamic Arrays

Arrays can be used to refer to a series of variables by the same name and to use a number (an index) to distinguish them. Visual Basic has two types of arrays: fixed-size and dynamic. A fixed-size array always remains the same size. A dynamic array can change its size while the program is running.

A fixed-size array is declared with the size indicated. For example, the following line declares MyFixedArray dimensioned to 2.

Dim MyFixedArray(2)as Double

Dimensioning the array to 2 means that it holds three data items:

MyFixedArray(0) = first data item

MyFixedArray(1) = second data item

MyFixedArray(2) = third data item

Dynamic arrays are declared with no size indicated as shown here:

Dim MyDynamicArray()as Double

Dynamic arrays are dimensioned sometime after they are declared using a statement such as the following:

ReDim MyDynamicArray(2)

Any array that is dimensioned inside SAP2000 must be declared as a dynamic array so that SAP2000 can redimension it. It is probably a good idea to declare all arrays as dynamic arrays for simplicity. As an example, the analysis results obtained through the CSI API are stored in arrays that are defined as dynamic arrays by the user and then dimensioned and filled inside of SAP2000.

Variable Types

Most of the data in the CSI API is one of the following variable types.

* Boolean: A variable stored as a 16-bit (2-byte) number, but it can only be True or False. When boolean values are converted to other data types, False becomes 0 and True becomes –1.
* Long: A variable stored as a 32-bit (4-byte) number ranging in value from -2,147,483,648 to 2,147,483,647. Note that other programming languages may refer to this data type differently; for example, they may refer to this as an Integer.
* Double: A double-precision floating-point variable stored as an IEEE 64-bit (8-byte) floating-point number ranging in value from -1.79769313486231E308 to -4.94065645841247E-324 for negative values and from 4.94065645841247E-324 to 1.79769313486232E308 for positive values.
* String: A variable length string.

Optional Arguments

Some of the CSI API functions have optional arguments. For example, the CountLoadDispl function has two optional arguments: Name and LoadPat. It is not necessary to include the optional arguments when calling this function. All four of the following calls are valid.

ret = SapModel.PointObj.CountLoadDispl(Count)

ret = SapModel.PointObj.CountLoadDispl(Count, Name)

ret = SapModel.PointObj.CountLoadDispl(Count, , LoadPat)

ret = SapModel.PointObj.CountLoadDispl(Count, Name, LoadPat)

Note in the third example, the first optional item is not included and the second optional item is included. In that case, commas must be included to denote the missing arguments.

Comments

In Visual Basic the Rem statement followed by a space indicates that all of the data on the line to the right of the Rem statement is a comment (or a remark). The Rem statement can be abbreviated using an apostrophe, '. The apostrophe is used in all of the VBA examples in the CSI API documentation to denote a comment.

ByVal and ByRef

Variables are passed to the \ using the ByRef or the ByVal keyword.

* ByVal means that the variable is passed by value. This allows the CSI API to access a copy of the variable but not the original variable. This means the value of the variable in another application can not be changed by the API.
* ByRef, which is the default in VB6 and VBA, means the argument is passed by reference. This passes the address of the variable to the CSI API instead of passing a copy of the value. It allows the CSI API to access the actual variable, and, as a result, allows SAP2000 to change the variable's actual value in an application.

Variables are passed ByRef when data needs to be returned in them from SAP2000 to your application. In addition, Visual Basic requires that all arrays be passed ByRef.

Release Notes

Changed nomenclature from Load Cases, Analysis Cases and Response Combinations to Load Patterns, Load Cases and Load Combinations, respectively, in version 12.00.

See Also

[Introduction](../Introduction.htm)

[Accessing SAP2000 From An External Application](Accessing_Sap2000_From_An_External_Application.htm)

[Function Documentation Conventions](Function_Documentation_Conventions.htm)

[Function Return Values](Function_Return_Values.htm)

[Units Abbreviations](Units_Abbreviations.htm)

