# API PlugIns

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/PlugIns

---



## Plugin Example for SAP2000 API CHM

*Source file: `SAP2000_API_Fuctions/PlugIns/Plugin_Example_for_SAP2000_API_CHM.htm`*

# **Plugin Example**

## **Remarks**

This page shows how to create a simple plugin using Visual Studio 2022 & Visual Basic that can be called from past and recent versions of multiple CSI programs. This plugin has minimal functionality as it is intended to demonstrate how to implement the cPlugin class: It simply creates an empty model, adds a material, frame section, and a frame object to it.

Starting with version 2.0 (released with SAP2000 & CSiBridge v26.0.0 and ETABS & SAFE v22.0.0), the API is compiled as a .NET Standard 2.0 AnyCPU dynamic link library (DLL). A plugin also targeting .NET Standard 2.0 & referencing the cross-product API CSiAPIv1.dll version 2.0 and up can be called from both SAP2000 & CSiBridge v21.0.0 and up and ETABS & SAFE v19.0.0 and up. Such plugins can be used to implement macro like functionality with no user input (due to lack of user interface elements in .NET Standard 2.0) for a wide range of products.

Below are the steps to create such a plugin. Examples of more complex plugins using other programming languages, user interface elements, and additional dependencies can be found at [CSI Knowledge Base Sample Plugins](https://redirects.csiamerica.com/wiki/x/cod0)

## Procedure

1. Create a new project of type“Class Library” for “Windows” using “Visual Basic” programming language.
2. Give your plugin project a descriptive name (e.g. “PluginExample”) and have it target “.NET Standard 2.0”.
3. Edit the project file to add

<EnableDynamicLoading>true</EnableDynamicLoading> <CopyLocalLockFileAssemblies>true</CopyLocalLockFileAssemblies>

elements to the project to ensure all dependencies of the plugin are copied to the plugin output folder.

![](../../assets/images/Plug_in_Example.jpg)

1. Edit the project file to add a reference to the cross-product API library, CSiAPIv1.dll,  from the program installation folder:

  <ItemGroup>

    <Reference Include="CSiAPIv1">

      <HintPath>C:\Program Files\Computers and Structures\SAP2000 26\CSiAPIv1.dll</HintPath>

      <Private>false</Private>

      <ExcludeAssets>runtime</ExcludeAssets>

    </Reference>

    <Import Include="CSiAPIv1" />

  </ItemGroup>

![](../../assets/images/Plug_in_Example_2.jpg)

<Private>false</Private> and <ExcludeAssets>runtime</ExcludeAssets> elements above are critical & required to prevent conflicts with the API dll already loaded by the program.

1. Paste the example code below into the class file. Please pay attention to the comments in this code block, they contain additional important information
2. Compile the project, selecting either AnyCPU or x64 as the platform. Please note that all CSI programs are 64-bit. The output plugin assembly is a file with the name you selected in Step 2 and a DLL extension.
3. To add this plugin to the Tools menu in SAP2000, navigate to the Tools menu and select **Add/Show Plugins** . This will open the External Plugin Data form shown below

![](../../assets/images/SAP2000_API_Fuctions/PlugIns/Plugin_Example_for_SAP2000_API_CHM_files/Picture4.jpg)

8. In the External Plugin Data form, click **Browse**, then locate and select your plugin assembly DLL .
9. The textbox fields will automatically populate with your plugin information. You can modify the Menu Text field as preferred.
10. Click the **Add** button. Check that the Status field reads OK. You can click the **Info** button to view information about the plugin.
11. Close the External Plugin Data form.
12. Your plugin now appears in the Tools menu drop-down. Click on it to run your plugin.

## Example Code

Imports CSiAPIv1

'''  <summary>

''' This is the class that the CSI program will use when starting your plugin.

''' The name of this class must be cPlugin , with that exact capitalization.

''' It should implement the cPluginContract interface, as demonstrated below.

'''  </summary>

Public Class cPlugin

    Implements cPluginContract

    '''  <summary>

    ''' The entry point for launching the plugin

    '''  </summary>

    '''  <param name="SapModel">

    ''' A reference to the SapModel object upon which all operations will be performed

    '''  </param>

    '''  <param name="ISapPlugin">

    ''' A reference to the callback object, used to retrieve the plugin status and notify the program when the plugin is closed

    '''  </param>

    Public Sub Main(ByRef SapModel As cSapModel, ByRef ISapPlugin As cPluginCallback) Implements cPluginContract.Main

        Dim errorCode As Integer = 1

        Try

            Dim ret As Integer = -1

            ret = SapModel.InitializeNewModel()

            ret = SapModel.File.NewBlank()

            ret = SapModel.PropMaterial.SetMaterial("CONC", eMatType.Concrete)

            ret = SapModel.PropFrame.SetRectangle("R1", "CONC", 12, 12)

            Dim frameName As String = ""

            ret = SapModel.FrameObj.AddByCoord(0, 0, 0, 10, 0, 0, frameName, "R1", "1")

            ret = SapModel.View.RefreshView(0, False)

            errorCode = 0

        Catch ex As Exception

            errorCode = 1

        Finally

            'It is not necessarily required to call ISapPlugin.Finish before the Main method returns.

            'For instance, your plugin may launch an interactive form for users.

            'In that case, you would pass a reference to the ISapPlugin object to your form,

            'and call ISapPlugin.Finish in that form's closing event

            ISapPlugin.Finish(errorCode)

        End Try

    End Sub

    '''  <summary>

    ''' Provides information about the plugin

    '''  </summary>

    '''  <param name="Text">

    ''' Information about the plugin, e.g. author, version, description

    '''  </param>

    '''  <returns>

    ''' Returns zero if the information is successfully retrieved; otherwise it returns a nonzero value

    '''  </returns>

    Public Function Info(ByRef Text As String) As Integer Implements cPluginContract.Info

        Try

            Text = "A simple example plugin. Author, Company, Version, Etc"

        Catch ex As Exception

            Return 1

        End Try

        Return 0

    End Function

End Class

## See Also

[cPluginCallback Interface](cPlugincallback_Properties/cPluginCallback_Interfacey.htm)

[cPluginContract Interface](cPluginContract_Methods/cPluginContract.htm)



## cPluginContract Interface

*Source file: `SAP2000_API_Fuctions/PlugIns/cPluginContract_Methods/cPluginContract.htm`*

# cPluginContract Interface

The cPluginContract interface is used to ensure that
the cPlugin class you create contains the correct methods, so that your plugin can
be successfully added to and run by SAP2000

## Methods

### Main

Sub Main ( ByRef SapModel
As cSapModel, ByRef ISapPlugin As cPluginCallback )Dim instance As cPluginContract

This method is the entry
point for launching the plugin.

SapModel

The parameter SapModel is
a reference to the SapModel object upon which all operations will be performed.
The SapModel object will be provided to your plugin by the main SAP2000
program

ISapPlugin

The parameter ISapPlugin
is a reference to the callback object, used to retrieve the plugin status
and notify the program when the plugin is closed. The callback object
will be passed from the main SAP200 program to your plugin.

### Info

Function Info ( ByRef Text
As String ) As Integer

This method provides information
about the plugin

Text

The parameter Text
should be filled with information about the plugin, e.g. author, version,
description

Return Value

This method returns a zero
if the information is successfully retrieved; otherwise it returns a non-zero
value.

## See Also

[cPluginCallback
Interface](../cPlugincallback_Properties/cPluginCallback_Interfacey.htm)

[Plugin
Example](../Plugin_Example_for_SAP2000_API_CHM.htm)



## cPluginCallback Interface

*Source file: `SAP2000_API_Fuctions/PlugIns/cPlugincallback_Properties/cPluginCallback_Interfacey.htm`*

# cPluginCallback Interface

The cPluginCallback interface is used to check the plugin
state, and tell SAP2000 when the plugin has finished. The callback object
that implements the interface will be passed from the main SAP200 program
to your plugin.

## Methods

### Finish

Sub
Finish ( iVal As Integer)

This method must be called
when the plugin has finished. Otherwise the main SAP2000 program will
wait indefinitely.

iVal

The parameter *iVal*
sets the *ErrorFlag* property

## Properties

### ErrorFlag

ReadOnly
Property ErrorFlag
As Integer

This
proper indicates whether an error has occurred.

It
returns a zero if the plugin completed successfully; a non-zero
value indicates that an error occurred

### Finished

ReadOnly
Property Finished
As Boolean

This
property indicates whether the plugin is finished, i.e. whether the Finish method has been called.

It returns true if the plugin is finished,
otherwise, it returns false.

## See Also

[cPluginContract
Interface](../cPluginContract_Methods/cPluginContract.htm)

[Plugin
Example](../Plugin_Example_for_SAP2000_API_CHM.htm)

