

---
<!-- source: Introduction/New_Features,_Enhancements,_and_Improvements.htm | New Features, Enhancements, and Improvements -->

# New Features, Enhancements, and Improvements

Several changes have been made to Section Designer to enhance its functionality, including the following:

- Materials and their Material Model (Simple, Mander.) for concrete and rebar materials are now defined outside of SD using the Define menu > Materials command in the program within which Section Designer is launched (i.e., SAP, ETABS). When defining Materials for concrete or rebar material types, choose the Advanced Display mode (Show Advanced Properties in SAP2000), modify the Material Properties, and click the Nonlinear Properties button to specify the nonlinear material data.
- Rebar sizes also are defined outside of SD using the Define menu > Section Properties > Reinforcement Bar Sizes command.
- The Caltrans section form has been simplified, and Mander models based on the Core definitions can be viewed.
- For Caltrans sections, cover is still defined to the outside of confinement steel. However, two changes have been made to maintain consistency with the Mander material model:
- - The confinement diameter is defined at the center-line of the confinement steel, rather than outside of the confinement steel.
  - The confined material is placed inside the center-line of the confinement steel, rather than outside of the confinement steel.

- For non-Caltrans sections, cover is still defined to the outside of longitudinal steel. However, similar to the Caltrans section, for Mander models:
- - The confinement diameter is defined at the center-line of the confinement steel, rather than outside of the longitudinal steel.
  - The confined material is placed inside the center-line of the confinement steel, rather than outside of the longitudinal steel.

- A non-Caltrans section drawn to match a Caltrans section gives the same behavior as the Caltrans section.
- Double counting of  overlapping sections has been eliminated
- For overlapping shapes, the top section controls all calculations; it is as if only the top shape is present whenever two shapes overlap.
- A section can be moved forward or backward using the Edit menu. A section that is completely inside another section is always on top.
- The section can be represented by a [fiber model](../Menus/Define/Fiber_Layout.md).
- The fiber model can be used as the basis of a fiber hinge assigned to a frame element.
- The centroid of all solid sections is updated instantly when a solid shape is added.
- When plotting [moment-curvature](../Menus/Display/Show_Moment_Curvature_Curve.md) or [PMM surface](../Menus/Display/Show_Interaction_Surface.md),  the exact integration or the fiber model or both can be shown.
- Moment curvature curves can be drawn for concrete-only sections or steel-only sections.
- Edit menu > Align command actions can be undone using the Undo button or command.
- A solid section containing rebar can be converted into a polygon and a separate rebar shape using the Edit menu > Change Shape to Poly command.
- The color used to display all curves on the moment-curvature curve form can be user specified.


---
<!-- source: Introduction/Organization_of_this_Help.htm | Organization of this Help -->

Section Designer

# Organization of this Help File

Find information in this Help file using any of following:

- Use the Help menu > Search for Help on command to display the Section Designer Help, which offers the following:
- - Contents Tab. Use the Contents to locate help topics for the menu commands.
  - Index Tab. Use the alphabetized Index to locate a specific topic.
  - Search Tab. Use the Search feature to conduct a keyword search of all available help topics.
- With a form displayed on-screen, press the F1 key on the keyboard for context sensitive help about that form.


---
<!-- source: Introduction/Overview.htm | Overview -->

Section
Designer

# Overview

Section Designer is a powerful utility that allows
design of simple and complex cross sections. The following procedure is
intended to introduce the various menu commands available to make generating
a cross section and reviewing interaction surface and moment curvature
plots quick and easy.

Note:  Within
the analysis and design program (e.g., SAP2000, ETABS), use the Define menu > Materials command to define
the material properties and use the Define menu
> Section Properties > Reinforcement Bar Sizes command to
specify rebar to be used in the cross section before beginning the following
process.

1. Use the [Define menu > Fiber Layout command](../Menus/Define/Fiber_Layout.md) to
   define the fiber model. The fiber model  can be used to calculate
   moment-curvature curves and PMM interaction surfaces as well as fiber
   hinges.
2. Use one of the commands
   on the Draw menu to draw a shape and begin generating the cross section
   ([Draw
   Structural Shapes](../Menus/Draw/Draw_Structural_Shapes/Draw_Structural_Shapes.md), [Draw
   Solid Shapes](../Menus/Draw/Draw_Solid_Shapes/Draw_Solid_Shape.md), [Draw
   Poly Shape](../Menus/Draw/Draw_Poly_Shape.md), [Draw
   Caltrans Shape](../Menus/Draw/Draw_Caltrans_Shape.md)).
3. Click the [Display menu > Show Fibers command](../Menus/Display/Show_Fibers.md) to
   view a graphical representation of the fiber model as well as a form
   that provides the data for each fiber generated for the fiber model,
   including the area, coordinates, and material properties.
4. Refine the geometry
   for the cross section. Right click on the shape drawn in Step 2 to
   display the Shape Properties form for
   the type of shape. That form has various options to specify the geometry
   of the shape. After the shape has been drawn, the [Reshape
   Mode](../Menus/Draw/Reshape_Mode.md) can be used to revise the geometry. Use the [Assign Display Colors form](../Menus/Options/Options.md) to specify
   the display colors for the components of the cross section, both for
   on-screen display and for output to a printer.

Note:
 With the Shape
Properties form displayed, click
the F1 key to display a Help topic specific to the form for that particular
type of shape.

TIP:
 The Shape Properties form may include
a Materials drop-down list, depending
on the type of shape. The list will consist of the materials properties
as defined in the analysis and design program within which Section Designer
is accessed (e.g., SAP2000, ETABS). As noted above, make modifications
to the material properties if necessary in the analysis and design program
before accessing Section Designer.

Cross sections
can be generated by combining individual shapes using commands on the
Edit menu.

1. Use the [Edit menu > Replicate command](../Menus/Edit/Replicate.md) to quickly
   add duplicate shapes to the cross section.
2. Use the [Edit
   menu > Align](../Menus/Edit/Align.md) subcommands to align two or more shapes.
   Use the [Nudge feature](../Menus/Edit/Nudge_Feature.md)
   to move shapes in [specified
   increments](../Menus/Options/Preferences.md).
3. The [Edit
   menu > Change Shape to Poly](../Menus/Edit/Change_Shape_to_Poly.md) command can be used to change
   a structural or solid shape to a poly shape. The geometry of structural
   and solid shapes is defined by specified height and width items. The
   geometry of poly shapes is defined by the coordinates of the corner
   points of the poly shape. Converting a structural or solid shape to
   a poly shape allows the geometry of the shape to be tweaked in ways
   that otherwise would not be possible.
4. Use the [Edit
   menu > Check Section for Overlaps](../Menus/Edit/Check_Section_for_Overlaps.md) command to check the
   section for poly areas that overlap. If areas overlap, the top section
   controls. Click on one of the overlapping shapes to select it and
   use the [Edit menu > Move Forward or Edit
   Menu > Move Backward command](../Menus/Edit/Move_Forward_and_Move_Backward.md) to change which shape is
   on top, as needed.
5. Use the  [Edit menu > Merge Two Polys](../Menus/Edit/Merge_Two_Polys.md) command
   to merge two shapes that overlap.
6. Use the [Edit
   menu > Get Two Poly Intersections](../Menus/Edit/Get_Two_Polys_Intersections.md) command to limit the
   resulting shape to the area of overlap for two selected shapes.
7. Use the [Edit menu > Get Two Polys Differences command](../Menus/Edit/Get_Two_Polys_Differences.md)
   to eliminate the area of overlap for two selected shapes.
8. Use the [Edit
   menu > Remove Bottom Polys overlapping area](../Menus/Edit/Remove_Bottom_Polys_overlapping_area.md) command
   to eliminate the areas of overlap for two selected shapes that have
   different material properties.

Note:
 The [Edit
menu > Undo and Redo commands](../Menus/Edit/Undo_and_Redo.md)
and toolbar buttons, ![](../Images/IMG00037.GIF)  ![](../Images/IMG00038.GIF), will reverse the immediately previous action
back to the last time the file was stored.

5. Define the rebar. Depending
   on the type of shape, the Shape Properties
   form has an option to specify that reinforcing be included in the
   shape. The [Draw menu > Draw Reinforcing Shapes subcommands](../Menus/Draw/Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md)
   can also be used to add rebar to a shape.

By default, the program
provides single rebar elements at each corner of a reinforced shape and
rebar line patterns along each face of  a reinforced shape. Note
the following about rebar elements:

1. - Rebar alignment
     is defined by a rebar size, maximum center-to-center spacing and
     clear cover (see the options available on the Shape
     Properties form for the selected shape or on the form associated
     with the appropriate [Draw
     menu > Draw Reinforcing Shapes](../Menus/Draw/Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md) subcommand).
   - The bars are spaced
     equally. The equal spacing is measured from the center of the
     corner bar at one end of the rebar line pattern to the center
     of the corner bar at the other end of the rebar line pattern.
   - Single rebar elements
     at the corners of a shape are defined by a bar size (see Step
     4 with respect to editing corner rebar sizes). The clear cover
     for the corner bars is determined from the clear cover of the
     line rebar on either side of the corner bar.

6. Edit
   the rebar. For [Structural
   Shapes](../Menus/Draw/Draw_Structural_Shapes/Draw_Structural_Shapes.md), [Solid
   Shapes](../Menus/Draw/Draw_Solid_Shapes/Draw_Solid_Shape.md), [Poly Shapes](../Menus/Draw/Draw_Poly_Shape.md),
   and [Reinforcing
   Shapes](../Menus/Draw/Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md) defined by corner points and with a concrete material type,
   the [Edge Reinforcing form](../Menus/Draw/Draw_Reinforcing_Shapes/Edge_Reinforcing_Form.md) can be used to modify
   the edge rebar size, maximum spacing and clear cover. Changes made
   on the Edge Reinforcing form apply to
   all of the bars along an edge. The [Corner Point Reinforcing form](../Menus/Draw/Draw_Reinforcing_Shapes/Corner_Point_Reinforcing_Form.md) can be used
   to change the size of corner rebar only.
7. View
   the section stresses using the [Display
   menu > Show Stresses](../Menus/Display/Show_Stresses.md) command.
8. View
   the section properties using the [Display
   menu > Show Section Properties](../Menus/Display/Show_Section_Properties.md) command.
9. View
   an interaction diagram using the [Display menu > Show Interaction Surface
   command](../Menus/Display/Show_Interaction_Surface.md).
10. View
    a moment-curvature plot using the [Display menu > Show Moment-Curvature Curve
    command](../Menus/Display/Show_Moment_Curvature_Curve.md).
11. Print
    the currently displayed cross section using the [File menu > Print Graphics command](../Menus/File/Print_Graphics.md).
    Use the [File
    menu > Print Setup command](../Menus/File/Print_Setup.md) to specify the page layout
    for the print.


---
<!-- source: Main.htm | Main -->

# Section Designer

Quick
Start:   [Overview](Introduction/Overview.md)

Copyright ©
by Computers and Structures, Inc., 1978-2017  
SAP2000® and
CSiBridge® are
registered trademarks of Computers and Structures, Inc.

The computer programs SAP2000® and CSiBridge® and all associated documentation
are proprietary and copyrighted products. Worldwide rights of ownership
rest with Computers and Structures, Inc. Unlicensed use of the program
or reproduction of the documentation in any form, without prior written
authorization from Computers and Structures, Inc., is explicitly prohibited.

Further information and copies of this documentation
may be obtained from:

Computers
& Structures, Inc.

[www.csiamerica.com](http://www.csiamerica.com)

| [info@csiamerica.com](info%40csiamerica.com) (for general information)  [support@csiamerica.com](support%40csiamerica.com) (for technical support) | Quick Tip:  If you are Drawing shapes and using F1 to pull up a help topic (and this page is appearing rather than the shape-specific help you expect), first right click on the shape and then press F1. |


---
<!-- source: Menus/Define/Fiber_Layout.htm | Fiber Layout -->

Section Designer

# Fiber Layout

Form:  Define Materials, Generated Fibers for SD Section {Section Name}, Fiber Section Properties for SD Section {Section Name}

Use the Define menu > Fiber Layout command to display the Fiber Layout form. Use the form to specify the fiber model that can be used to calculate moment-curvature curves and PMM interaction surfaces as well as fiber hinges.

1. Use one of the Draw menu commands to draw the cross section.
2. Click the Define menu > Fiber Layout command to display the Fiber Layout form.

   - Number of Fibers in 2-Direction and Number of Fibers in 3-Direction edit boxes. Use these edit boxes to specify the number of fibers in the local 2 and local 3 axis directions; the section properties are calculated for these axes. If multiple shapes are used to represent the cross section, the fiber definition applies to all shapes.
   - Fiber Grid Angle or Initial Angle from 2 Axis edit box. The value in this edit box specifies the rotation, in the counterclockwise direction, of the grid used to calculate the fibers with respect to the local 2 axis of the section.
   - Cylindrical Coordinate check box. When this check box is checked, the fibers are aligned in a cylindrical pattern.
   - Lump Rebar Fibers within the same Grid check box. A rectangular or circular grid is used to divide the section into fibers. Within each grid cell, a single fiber is created for each different material, and by default a single fiber is created for each rebar. This option allows all rebar within a single grid cell to be lumped into a single equivalent fiber, for efficiency.
   - Calculate PMM Surface Using Fibers check box. When this check box is checked, the program calculates the PMM surface based on the fiber definition as specified on this form.
   - Calculate Moment Curvature Using Fibers check box. When this check box is checked, the program calculates the moment curvature cure based on the fiber definition as specified on this form.
3. Click the Display menu > Show Fibers command to view a graphical representation of the fiber model as well as the Generated Fibers for SD Section {Section Name} form, which provides the data for each fiber generated for the fiber model, including the area, coordinates, and material properties. The data is provided for review purposes only and cannot be edited.  The fiber associated with the row of data selected in the form will "pulse" in the graphical display. Click the Show Properties button to display the Fiber Section Properties for SD Section {Section Name} form, which lists the fiber section and {shape} section properties in non-editable format.


---
<!-- source: Menus/Display/Override_Axis_Labels_and_Range_Form.htm | Override Axis Labels and Range Form -->

Section Designer

# Override Axis Labels and Range Form

Use the Override Axis Labels And Range form to change the labels and ranges used on moment-curvature curve plots.

- Specify the horizontal axis range for the curve display by typing values in the Min and Max edit boxes in the Horizontal Range area.
- Specify the vertical axis range for the curve display by typing values in the Min and Max edit boxes in the Vertical Range area.
- Use the default labels for the horizontal and vertical axis, or type new labels in the appropriate edit boxes in the Axis Labels area.
- Use the Reset Defaults button to restore all values or suggested text to the program defaults.

| Access the Override Axis Labels and Range form as follows,   1. With a shape drawn in the display area, click the Display menu > Show Moment-Curvature Curve command or   button to display the Moment Curvature Curve form.. 2. Click the Specify Scales/Headings button. |


---
<!-- source: Menus/Display/Show_Caltrans_Interaction_Surface.htm | Show Caltrans Interaction Surface -->

Section Designer

# Show Caltrans Interaction Surface

Use the Display menu > Show Caltrans Interaction Surface command to display the Interaction Surface (Caltrans) form. Use the form to display the interaction surface in accordance with Caltrans specifications. The form has the same options and areas as the [Interaction Surface form](Show_Interaction_Surface.md) that displays when the Display menu > Show Interaction Surface command is used, with the exception that the Options for controlling strength reduction (phi factor) and the reinforcing steel yield stress are not available.


---
<!-- source: Menus/Display/Show_Caltrans_Rebar_Curves.htm | Show Caltrans Rebar Curves -->

Section Designer

# Show Caltrans Rebar Curves

Use the Display menu > Show Caltrans Rebar Curves command to display the Caltrans Rebar Curves form.

1. Highlight a rebar ID in the Stress-Strain Curves display list.
2. Click the Modify/Show Curve button to display the Material Stress-Strain Curve Data form. Use the form to define a material stress-strain curve.

1. - Stress-Strain Curve Name edit box. Use the Caltrans rebar ID name or type in a revised name.
   - Number of Points in Stress-Strain Curve edit box. Use the default or specify a revised value for the number of points defining the stress-strain curve; the larger the number of points, the smoother the curve.
   - Hysteresis Type drop-down list. Select the type of hysteresis from the drop-down list.
   - Stress-Strain Curve Data spreadsheet area. Use the cells of the spreadsheet to specify values for the stress and strain along the specified number of points comprising the stress-strain curve. Thus, to add rows, increase the value entered in the Number of Points in Stress-Strain Curve edit box.
   - Order Rows button. After entering data in this spreadsheet, click this button to reorder the rows, if necessary, in ascending order.
   - Display Color. Click this color box to display the Color form and select a revised display color for the stress-strain curve.
   - Display area. The rebar curve displays in the small grid lined area on the right side of the form.


---
<!-- source: Menus/Display/Show_Fibers.htm | Show Fibers -->

# Show Fibers

The Display menu > Show Fibers command is a toggle. It is used to turn the display of [previously defined fibers](../Define/Fiber_Layout.md) on and off.

Clicking this command also displays the Generated Fibers for SDSection {Name} form. That form displays the size of the area, the coordinates and material type of the fibers generated. Clicking the Show Properties button on the Generated Fibers for SDSection {Name} form displays the Fiber Section Properties for SDSection {Name} form. That form provides the properties of fiber section and the shape section.


---
<!-- source: Menus/Display/Show_Interaction_Surface.htm | Show Interaction Surface -->

Section Designer

# Show Interaction Surface

Form:  Interaction Surface, Interaction Surface (Caltrans)

Use the Display menu > Show Interaction Surface command or  ![](../../Images/ebx_-466038497.gif) button to access the Interaction Surface form for concrete sections that have reinforcing specified. If the section is not concrete and reinforcing is not specified, this command will not be available. In Section Designer the interaction surface is defined by a series of PM curves that are equally spaced around a 360 degree circle. For example, if 24 curves are specified (the default), there is one curve every 15 degrees (360°/24 curves) .

- Spreadsheet area. Any point on one of the interaction curves is identified by a P, M2 and M3 coordinate. P is the axial load, M2 is the moment about the local 2-axis and M3 is the moment about the local 3-axis. The Interaction Surface form displays the P, M2 and M3 coordinates of each of the curves that make up the interaction surface in a tabular format, one curve at a time. Use the arrow buttons below the table to scroll through the various PM curves. Note that an arrow to the left of the table indicates the current line, and that the current curve number and its angle in degrees are reported below the table to the left of the arrows.

Use the Edit menu > Copy All command to copy the data in the table to the Windows clipboard for pasting into another program such as Excel for further review.

- Display areas. Two types of plots appear on the Interaction Surface form. The first is a
- - 2D Plot. This plot cuts through the interaction surface at the specified angle. The angle is shown below the table and can be changed using the arrow keys below the table. The origin of the 2D chart occurs at the intersection of the two red axes.
  - - Design-Code Curve check box. When this check box is checked, the plot shows the curve as specified in accordance with the code selected in SAP2000 using the Design menu > {Type} Design > View/Revise Preferences command.
    - Fiber-Model Curve check box. When this check box is checked, the fiber model curve is added to the 2D plot.
  - 3D Plot. The 3D view is a plot of the interaction surface. Use the controls in the 3D View area of the form to rotate this view into any orientation.
  - - 3D View. The 3D View area provides controls for viewing the 3D chart of the interaction surface. Define the view direction by specifying a plan angle and an elevation angle. All angles are specified in degrees. The view direction defines the location where you are standing as you view the interaction surface from the outside.

Figure a below shows a three dimensional view of an interaction surface using the default view direction of plan angle = 315 degrees and elevation angle = 35 degrees. Figures b and c below illustrate how the plan and elevation angles are defined. Following the figure are explanations of the terms used in the figure.

![](../../Images/IMG00106.GIF)

- - - - The Eye point is the location from which you are viewing the interaction surface.
      - The target point is the origin of the interaction surface.
      - The view direction is defined by a line drawn from the eye point to the target point.
      - The plan angle is the angle (in degrees) from the positive M3-axis to the line defining the view direction measured in a horizontal plane. A positive angle appears counterclockwise as you look down on the interaction surface. Any value between -360 degrees and +360 degrees, inclusive, is allowed for the plan angle.
      - The elevation angle is the angle (in degrees) from the M2-M3 plane to the line defining the view direction. A positive angle starts from the M2-M3 plane and proceeds toward the negative P-axis. A negative angle starts from the M2-M3 plane and proceeds toward the positive P-axis. (Recall that the negative P-axis points upward and the positive P-axis points downward.) Any value between -360 degrees and +360 degrees, inclusive, is allowed for the elevation angle.

The 3D View form has four fast view buttons labeled 3d, MM, PM3 and PM2. The fast view buttons automatically set the plan and elevation angle to display the specified 3D view. The fast view 3d view is as shown in the figure above. The other fast views display 3D perspective views of the specified planes.

- Options Choose the appropriate option:
- - Phi: The code specified strength reduction factors are considered when creating the interaction surface.
  - No phi: The code specified strength reduction factors are not considered (i.e., set to 1.0) when creating the interaction surface.
  - No phi with fy increase: The code specified strength reduction factors are not considered (i.e., set to 1.0) and the reinforcing steel yield stress is increased by a code-specified amount (1.25 for ACI and UBC) to estimate probable strength when creating the interaction surface.

Note:  When the Display menu > Show Caltrans Interaction Surface command is used to display this form, Options for controlling strength reduction (phi factor) and the reinforcing steel yield stress are not available.

- Show Design-Code Results option. When this option is selected, the values in the spreadsheet area show the results as specified in accordance with the code selected in SAP2000 using the Design menu > {Type} Design > View/Revise Preferences command.
- Show Fiber Model Results option. When this option is selected, the values in the spreadsheet area show the fiber model results.

- Edit menu > Copy All command. The Edit menu in the Interaction Surface form has a Copy All command. This command copies the P, M2 and M3 values at each point for each interaction curve in the interaction surface to the Windows clipboard. The values can then be pasted into another program using the Windows paste command.


---
<!-- source: Menus/Display/Show_Moment_Curvature_Curve.htm | Show Moment Curvature Curve -->

Section Designer

# Show Moment Curvature Curve

Additional forms:  Moment Curvature Curve Details for {Curve Number}, Stress/Strain Contours for {Curve Number}

Use the Display menu > Show Moment Curvature Curve command or ![](../../Images/ebx_-1202079413.gif) button to display the Moment Curvature Curve form. Use the form to display moment curvature curves for concrete sections that have reinforcing. If the section is not concrete and does not have reinforcement, this command will not be available.

- Display areas.
- - Curvature plot. The program generates the moment curvature curve with moment on the vertical axis and curvature on the horizontal axis. Click the Details button in the lower right corner of the form to display the Moment Curvature Curve Details for {Curve Number} form. The lower portion of that form shows the moment curvature curve data in tabular form. The number of rows of data in the table and the number of points used to generate the plot are controlled by the number of points specified in the No. of Points edit box.

When the mouse pointer is moved over the plot, a display box below the Curvature plot area shows the value of the moment curvature curve at that point. The curvature is listed first followed by the moment.

1. - Strain Diagram plot. This plot is generated when the mouse pointer is moved over the Curvature plot. The strain diagram illustrates the strain at that particular point on the curve.

When the mouse pointer is moved over the plot, the values for Concrete Strain, Steel Strain, and Neutral Axis are shown for that point in display boxes below the plot.

- Select Type of Graph drop-down list. Choose the type of plot to be displayed.
- Specify Scales/Headings button. Click this button to display the [Override Axial Labels and Range form](Override_Axis_Labels_and_Range_Form.md). Use the edit boxes on that form to change the horizontal and vertical ranges for the plot and the labels used on the horizontal and vertical axes.
- Plot Exact Integration Curve check box and Color box. When this check box is checked, the exact integration curve will be included in the plot using the color shown in the Color box. Click the Color box to display the Color form; use that form to change the color used to display the exact integration curve.
- Plot 3x3 Fiber Model Curve check box and Color box. When this check box is checked, the fiber model curve will be included in the plot using the color shown in the Color box. Click the Color box to display the Color form; use that form to change the color used to display the fiber model curve.
- - Show Numerical Results for Exact-Integration Curve option and Show Numerical Results for Fiber Model Curve option.  The availability of these options depends on if the Plot Exact Integration Curve check box or the Plot 3x3 Fiber Model Curve check box or both are checked.
- Caltrans Idealized Model check box. When this check box is checked, the moment curvature curve is generated in accordance with Caltrans specifications and the options in the Analysis Control area of the form become available.
- - Concrete Failure (Lowest Ultimate Strain) or Concrete Failure (Highest Ultimate Strain) options. When these option are selected, the Curvature plot shows the moment curvature curve for concrete failure at the lowest ultimate strain or the highest ultimate strain, respectively.
  - First Rebar Failure option. When this option is selected, the Curvature plot shows the moment curvature curve for rebar failure.
  - User Defined Curvature option. When this option is selected, an edit box is added to the form; use the edit box to specify the maximum curvature for the Curvature plot in accordance with Caltrans specifications.
- P (Tension +ve) edit box. Enter the axial load for which the moment curvature curve is to be plotted. Tension values are positive and compression values are negative.
- Max Curvature edit box. Enter the maximum curvature that the program is to consider when plotting the moment curvature curve. Note that the section may not be capable of reaching the maximum curvature specified. In other words, the section may fail before reaching the curvature specified in the Max Curvature edit box. If this happens, the maximum curvature shown in the Curvature plot or on the table on the  Moment Curvature Curve Details for {Curve Number} form (displayed by clicking the Details button) may be less than the maximum curvature specified in the Max Curvature edit box. When the maximum curvature reported in the plot or in the table is less than the curvature specified, the section is not capable of carrying the axial load specified in the P edit box at a curvature equal to that specified in the Max Curvature edit box.
- No of Points edit box. Enter the number of points used to construct the moment curvature curve.
- Angle (Deg) edit box. This angle defines the orientation (direction) of the neutral axis, but not its exact location. The angle is measured from the negative local 3-axis of the section. Positive angles appear counterclockwise as you look down on the section. The angle can vary from -360° to +360°.  The figure below illustrates how the angle controls the orientation of the neutral axis. Figure a shows the angle at 0° and Figure b shows the angle at 45°.

![](../../Images/IMG00107.GIF)

The angle also dictates the direction of the moment considered. When the angle is 0 degrees, the direction of moment is in the positive direction of the local 3-axis. Use the right hand rule to get a sense of the direction of this moment. When the angle is 180 degrees, the direction of moment is in the negative direction of the local 3-axis. The above figures illustrate the sense of the moment when the angle is 0 and 45 degrees.

As an example, if the angle specified were 225 degrees, the neutral axis would have the same orientation as that shown in the figure above, but the direction of the moment would be reversed as shown in the following figure.

![](../../Images/IMG00108.GIF)

- Details button. Click this button to display the Moment Curvature Curve Details for {Curve Number} form. The top portion of the form shows a graphic of the Curvature plot. The bottom portion of the form shows a table that lists the moment and curvature values at each of the considered points of the moment curvature curve. The values shown in the table are connected by straight line segments to form the plot. Use the scroll bar on the right-hand side of the form to scroll from top to bottom in the display area.
- - File menu > Print to File command. This command prints the data to an output file (.out).
- Contours button. Click this button to display the Stress/Strain Contours for {Curve Number} form. Use the options on the form to graphically display the stress or strain for a single point or all points. Use the arrow buttons in the lower right-hand corner of the form to cycle through the plot of the various points.
- Add Curve button. Clicking this button will add curves to the plot based on the various choices made on the form. For example, if the Plot 3x3 Fiber Model Curve check box is checked, the curve added will be a Fiber 3x3 Curve. The P (Tension +ve) and Angle (Deg) check boxes also can be used to refine the curve definition; then click the Add Curve button. Note that the curve will be displayed using the color shown in the Selected Curve Color box. Click the Color box to display the Color form; use that form to change the color used to display the curve selected in the Curves display list.
- Delete Curve button. Highlight a curve in the Curves display list, and click this button to delete the selected curve.


---
<!-- source: Menus/Display/Show_Section_Properties.htm | Show Section Properties -->

Section
Designer

# Show Section Properties

Form:  Properties

Use the Display menu > Show
Section Properties command or ![](../../Images/Show%20Section%20Properties%20button.JPG)
button to display the Properties form. This
form serves three functions:

1. The
   form displays the section properties.

2. The
   section base material property can be viewed using this form, but
   not edited. Do not confuse the section base material property with
   the material property of one of the shapes that makes up the section.

3. For
   frame sections only, the form can be used to modify the local axis
   angle for the section. This is the angle from the Section Designer
   X axis to the section local 2-axis. Positive angles appear counterclockwise
   as you look down on them as illustrated in the sketch below. You can
   not modify the local axis angle for wall pier sections; that angle
   is always 0 degrees.

![](../../Images/IMG00102.GIF)

- Section
  Properties

The section properties
are reported with respect to the section local axes (2-3), not the Section
Designer X and Y axes. Furthermore the section properties are reported
assuming that the entire section is transformed into an equivalent area
of the specified base material. In other words, each infinitesimal area
of the section, dA, is multiplied by the ratio Eshape/Ebase when computing the section
properties where Eshape
and Ebase
are defined below. Using this transformation, the following relationship
holds true.

![](../../Images/IMG00103.GIF)

where,

 Asection = Area
reported for the section, length2.

 Ashape   = Area
of a geometric shape (not reinforcing shape) included in the section,
length2.

 Ebase    = Modulus
of elasticity of the base material, force/length2.

 Eshape  = Modulus
of elasticity of the material specified for the shape, force/length2.

 n           = Number
of geometric shapes included in the section, unitless.

Important
note: The reinforcing steel is not
considered when calculating the section properties. This includes the
reinforcing steel defined as a reinforcing shape and the reinforcing steel
that is associated with a geometric shape. The section properties are
based on the gross area of all geometric shapes transformed to an equivalent
area of the base material.

The following section
properties are reported:

1. - A:
     Area of the section, length2.
   - J:
     Torsional constant, length4.
   - I33:
     Moment of inertia about the 3-axis, length4.
   - I22:
     Moment of inertia about the 2-axis, length4.
   - I23:
     Moment of inertia, length4.
     The figure below illustrates the derivation of I23, I22, and I33.

![](../../Images/IMG00104.GIF)

The I23 moment of inertia
is equal to zero when the local 2 and 3 axes are the principal axes of
the section. If the local 2 and 3 axes are not the principal axes of the
section, then I23 is nonzero.

1. - As2:
     Shear area for shear parallel to the 2-axis, length2.
   - As3:
     Shear area for shear parallel to the 3-axis, length2.
   - S33(+face):
     Section modulus about the 3-axis at extreme fiber of the section
     in the positive 2-axis
     direction, length3.
   - S22(+face):
     Section modulus about the 2-axis at extreme fiber of the section
     in the positive 3-axis
     direction, length3.
   - S33(-face):
     Section modulus about the 3-axis at extreme fiber of the section
     in the negative 2-axis
     direction, length3.
   - S22(-face):
     Section modulus about the 2-axis at extreme fiber of the section
     in the negative 3-axis
     direction, length3.
   - r33:
     Radius of gyration about the 3-axis, length.
   - r22:
     Radius of gyration about the 2-axis, length.
   - d33pna:
     The distance to the plastic neutral axis about the 3-axis, measured
     from the section center of gravity, length.
   - d22pna:
     The distance to the plastic neutral axis about the 2-axis, measured
     from the section center of gravity, length.
   - Xcg:
     The Section Designer X-axis coordinate of the center of gravity
     of the section, length.
   - Ycg:
     The Section Designer Y-axis coordinate of the center of gravity
     of the section, length.


---
<!-- source: Menus/Display/Show_Stresses.htm | Show Stresses -->

Section Designer

# Show Stresses

Use the Display menu > Show Stresses command or ![](../../Images/Show%20Stress%20button.JPG)  button to display the Elastic Stress form. Use the options on the form to graphically display the various stress components.


---
<!-- source: Menus/Draw/Concrete_Model_Form.htm | Concrete Model Form -->

Section Designer

# Concrete Model Form

The Concrete Model form displays the concrete model as Mander Confined or Unconfined, depending on the Conc. Model option selected on the Shape Properties form.

- Name display box. The name of the concrete material is displayed in this box.
- Various edit boxes and drop-down lists. Depending on the configuration of the shape and the model type (Mander Unconfined, Mander Confined C, Mander Confined R), the various parameters that define the shape are shown on the form, including, for example, rebar size and area, confinement type and longitudinal spacing and so on. In some cases, the data is presented in editable format. Click in the edit box or drop-down list to change a given parameter.
- Display area. The model curve is displayed in this area. Any changes made in the various edit box and drop-down lists on the form will be reflected in the model display. Run the mouse pointer over the curve in the display area and the values in the lower left-hand corner of the display area will change accordingly .
- View Values or Print button. Click this button to display the Stress-Strain Curve Report form. That form shows a graphical representation of the curve in the upper portion of the display area and a table of the strain and stress at specific points in the lower portion of the display area. The contents of the display area can be printed using a screen capture or using standard Windows copy and paste (Ctrl C and Ctrl V) commands.

| Access the Concrete Model form as follows:   1. Draw a shape with a concrete Material type other than a Caltrans shape. 2. Right-click on the shape to display the Shape Properties form. 3. Click the C Model button. |


---
<!-- source: Menus/Draw/Constrain_Drawn_Line_To.htm | Constrain Drawn Line To -->

Section Designer

# Constrain Drawn Line To

Drawing constraints provide the capability to constrain one of the axes when [poly shapes](Draw_Poly_Shape.md) are drawn or reshaped. Use the drawing constraints to quickly draw the edge of a poly shape parallel to the Section Designer X or Y axes or at any arbitrary angle. The drawing constraint tools can be activated using the Draw menu > Constrain Drawn Line to command or by pressing the X, Y or A key on the keyboard.

Use these three steps with the constraint tools:

1. Locate the first point.

2. Press one of the constraint keys on the keyboard (X, Y or A) or use the Draw menu > Constrain Drawn Line to command.

- - Draw menu > Constrain Drawn Line to> Constant X command or X on the keyboard: Locks the X component of the next point so that it is the same as the previous point.
  - Draw menu > Constrain Drawn Line to> Constant Y command or Y on the keyboard: Locks the Y component of the next point so that it is the same as the previous point.
  - Draw menu > Constrain Drawn Line to> Constant Angle command or A on the keyboard: Allows specification of an angle in degrees in the status bar at the bottom of the Section Designer window. Drawing is then constrained along this angle. The angles are measured from the Section Designer X-axis. Positive angles appear counterclockwise as you look down on the section. Note that when the keyboard command is used to specify a constant angle constraint, every time the A key on the keyboard is pressed, the constant angle changes to be equal to the angle of the line that is within the [screen selection tolerance](../Options/Preferences.md) distance from the mouse pointer. The angle can always be changed by editing it in the Section Designer status bar.
  - Draw menu > Constrain Drawn Line to> None command or Space Bar on the keyboard: Removes the current drawing constraint.

3. Locate the next point. Section Designer only picks up the unconstrained component of the next point. Drawing constraints are always removed as soon as the next point is drawn.

TIP: [Snaps](Snap_to.md) can be used in conjunction with constraints. In that case. only the unconstrained component of the selected snap point is used when a constraint is selected.


---
<!-- source: Menus/Draw/Draw_Caltrans_Shape.htm | Draw Caltrans Shape -->

Section Designer

# Draw Caltrans Shape

Form: Caltrans Section Properties, Core-{Number} Ring-{Number}, Core-{Number} Ring {Number} Steel Stress Strain Curve

Use the Draw menu > Draw Caltrans Shape command and its subcommands (Draw Hexagon, Draw Octagon, Draw Round, Draw Square) to quickly generate cross sections compliant with Caltrans specifications.

1. Click the Draw menu > Draw Caltrans Shape > Draw Hexagon,  Draw menu > Draw Caltrans Shape > Draw Octagon,  Draw menu > Draw Caltrans Shape > Draw Round, or  Draw menu > Draw Caltrans Shape > Draw Square command.
2. Left click anywhere in the active window and Section Designer will generate a cross section of the selected shape.
3. Right click on the shape to display the Caltrans Section Properties form. Many of the edit boxes and drop-down lists are available and values can be entered or new selections can be made.

- - Geometry
  - - Shape drop-down list. This drop-down list shows the type of shape.
    - Chamfer display box. This display box shows the chamfer specified for the shape. In the case of square shapes, this length is used for corners
    - Height edit box. Specify the height of the shape.
    - Width edit box. Specify the width of the shape.
    - Small Base Dimensions check box. When this check box is checked, the Base Height and Base Width edit boxes become enabled and can be modified.
    - - Base Height and Base Width edit boxes. These are optional dimensions that may be less than or equal to the Height and Width specified above. These dimensions determine the location of the reinforcing.  For example, in a flared column, the base height and width are the dimensions of the bottom of the column, and the actual height and width are the dimensions at the current elevation.
    - No. of Cores edit box. Use this edit box to specify the number of cores to be included in the cross section. If the base height and base width are not the same, more than one core can be specified. The maximum number of cores allowed is calculated based on the Ring cover, height and width.
  - Casing. The casing serves two purposes:  confinement and longitudinal strength.
  - - Thickness edit box. Use this edit box to specify the thickness of the casing. The full specified thickness is always assumed to be active for confinement.
    - Longit. Factor edit box. Use this edit box to specify the longitudinal factor for the casing. The longitudinal factor specifies the fraction of the thickness that is assumed to act longitudinally:  If equal to one, the casing is completed bonded to the section and the full thickness contributes to the moment curvature relationship similar to longitudinal rebar. If the factor is zero, the casing is completely unbonded and it serves only to provide confinement. Any value in between may be specified as appropriate.
  - Rings
  - - No. of Rings edit box and Ring Cover edit box(es). Use the No. of Rings edit box to specify the number of rings in the cross section; a minimum of one and a maximum of three is allowed. Use the Ring Cover edit box(es) to specify the thickness of the cover for each ring of reinforcement. The cover is defined as the minimum possible clear distance between the outer surface of the section to the outer surface of the confinement bar ring.
  - Drawing Area. This area of the form shows the location of rebar and the overall shape of the cross section. Zoom in, zoom out, pan and the like are available. Use the mouse scroll button to zoom in and out. Pressing the left mouse button while moving the mouse draws a bounding box for zooming in on the shape. Holding the middle mouse button down and moving the mouse will pan the drawing.  Note that the mouse pointer coordinates are shown below the drawing area.
  - Spreadsheet area. Use the cells in this area to specify the number of bundles of reinforcing, the type of bundle (perimeter, radial, triangle), their diameters, areas, types and so forth in the cross section core and the number of tendons for the cross sections. Click in a cell and enter a new value if the cell is an edit box, or select an item if the cell is a drop-down list.
  - - Core-Ring Show button. Clicking this button will display the Core -{Number} Ring-{Number} form. This form provides rebar data (e.g., area, diameter and so on) and is provided for review purposes only. Clicking the S Model button on that form will display the Core -{Number} Ring-{Number} Steel Stress Strain Curve form, which shows the stress strain curve for the core. Clicking the View/Print button on that form will display the [Stress-Strain Curve Report Form](Stress_Strain_Curve_Report_Form.md) for the core-ring.
    - Prestress Edit button. Clicking this button will display the Prestress Tendon form. Use that form to Add and Delete prestress tendons to the section. Clicking the Show button on that form will display the Core -{Number} Ring-{Number} Steel Stress Strain Curve form, which shows the stress strain curve for the core. Clicking the View/Print button on that form will display the Stress-Strain Curve Report Form. for the tendon core-ring.

- - Concrete Model
  - - Material drop-down list. This drop-down list displays the material property for the concrete.
    - Core Concrete, Outer Concrete and Other Concrete drop-down lists. Use these drop-down list to specify that the concrete be Core 1 (as specified in the spreadsheet area), Simple, Mander-Unconfined or Mander-Confined.
    - Show buttons. Various Show buttons on the form access the Concrete Model form, which provides Stress Strain plots for the concrete (e.g., the outer casting, the core concrete, the outer concrete) and edit boxes to adjust the stress and strain parameters.


---
<!-- source: Menus/Draw/Draw_Poly_Shape.htm | Draw Poly Shape -->

Section Designer

# Draw Poly Shape

Form:  Shape Properties - Poly

Use the Draw menu > Draw Poly Shape command or  toolbar button, ![](../../Images/IMG00079.GIF), to draw a polygon shape (i.e., a poly shape that is defined by the coordinates of its corner points).

1. Click the Draw menu > Draw Poly Shape command or  toolbar button, ![](../../Images/IMG00079.GIF).
2. Click in the active window to define the first point of the polygon. Continue to left click on the other points to define the polygon.
3. Complete the shape by double clicking on a point or single clicking and pressing the Enter or Esc keys on the keyboard.

TIP:  Use the [Drawing Constraints](Constrain_Drawn_Line_To.md) to help draw the Poly shape accurately. Use the [Reshape mode](Reshape_Mode.md) to modify the geometry of the poly shape after it has been drawn.

4. Right click on the poly shape to display the Shape Properties - Poly form. Use that form to review, and where necessary change, the parameters for the polygon:

1. - Type: Identifies the type of shape. It is not editable by the user.
   - Material: The default material property for Polygon shapes is Concrete (CONC). To change the material type, right click in the cell and select any available material property in the resulting drop-down box.
   - Color: Controls the color of the fill for the shape. Left click on the cell to bring up the Color form and set a new color for the fill.
   - Reinforcing: This item is visible only if the material property associated with the shape has a Concrete design type. When this item is set to Yes, the program inserts edge reinforcing bars and corner bars in the shape. If this item is set to No, no reinforcing bars will be included in the shape. When this item set to No, the Draw menu > Draw Reinforcing Shape command can be used to place rebar in the shape. The size and spacing of rebar can be modified using the [Edge Reinforcing form](Draw_Reinforcing_Shapes/Edge_Reinforcing_Form.md). The size of any corner rebar can be changed using the [Corner Point Reinforcing form.](Draw_Reinforcing_Shapes/Corner_Point_Reinforcing_Form.md)

See also:

[Draw Structural Shape](Draw_Structural_Shapes/Draw_Structural_Shapes.md)

[Draw Solid Shape](Draw_Solid_Shapes/Draw_Solid_Shape.md)

[Draw Reinforcing Shape](Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md)

[Draw Reference Lines](Draw_Reference_Lines/Drawing_Reference_Lines.md)


---
<!-- source: Menus/Draw/Draw_Reference_Lines/Drawing_Reference_Lines.htm | Drawing Reference Lines -->

Section Designer

# Drawing Reference Lines

Section Designer offers two types of references lines:

- Draw menu > Draw References Lines > Draw Reference Line command
- Draw menu > Draw Reference Lines > Draw Reference Circle command

See also:

[Draw Structural Shape](../Draw_Structural_Shapes/Draw_Structural_Shapes.md)

[Draw Solid Shape](../Draw_Solid_Shapes/Draw_Solid_Shape.md)

[Draw Poly Shape](../Draw_Poly_Shape.md)

[Draw Reinforcing Shape](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md)


---
<!-- source: Menus/Draw/Draw_Reference_Lines/Line.htm | Draw Reference Line -->

Section Designer

# Draw Reference Line

Use the Draw menu > Draw Reference Lines > Draw Reference Line command or the toolbar button, ![](../../../Images/IMG00090.GIF) to draw a reference line. Reference lines can be used along with the [Snap To](../Snap_to.md) or [Align](../../Edit/Align.md) features to draw or locate shapes accurately.

1. Click the Draw menu > Draw Structural Shape > Draw Reference Lines command or the toolbar button, ![](../../../Images/IMG00090.GIF) to enable the draw mode.
2. Left click anywhere in the active window to locate the start point for the reference line, move the mouse pointer in the required direction, and left click again to locate the end point of the reference line.
3. Right click on the reference line to display the Shape Properties - Reference form and review, and if necessary change, the shape parameters:

- - Type: Identifies the Line reference line type. It is not editable by the user.
  - X1: Specifies the Section Designer X coordinate of the first drawn end point of the line.
  - Y1: Specifies the Section Designer Y coordinate of the first drawn end point of the line.
  - X2: Specifies the Section Designer X coordinate of the second drawn end point of the line.
  - Y2: Specifies the Section Designer Y coordinate of the second drawn end point of the line.

See also:

[Draw Reference Circle](Reference_Circle.md)


---
<!-- source: Menus/Draw/Draw_Reference_Lines/Reference_Circle.htm | Draw Reference Circle -->

Section Designer

# Draw Reference Circle

Use the Draw menu > Draw Reference Lines > Draw Reference Circle command or the toolbar button, ![](../../../Images/IMG00091.GIF) to draw a reference circle. Reference lines can be used along with the [Snap To](../Snap_to.md) or [Align](../../Edit/Align.md) features to draw or locate shapes accurately.

1. Click the Draw menu > Draw Structural Shape > Draw Reference Circle command or the toolbar button, ![](../../../Images/IMG00091.GIF) to enable the draw mode.
2. Left click anywhere in the active window to locate the reference circle. The geometry of the reference circle is defined by the coordinates of the center point and a diameter.
3. Right click on the reference line to display the Shape Properties - Reference form and review, and if necessary change, the shape parameters:

- - Type: Identifies the type of reference line. It is not editable by the user.
  - X Center: Specifies the Section Designer X coordinate of the center of the circle.
  - Y Center: Specifies the Section Designer Y coordinate of the center of the circle.
  - Diameter: Specifies the diameter of the circle.

See also:

[Draw Reference Lines](Drawing_Reference_Lines.md)


---
<!-- source: Menus/Draw/Draw_Reinforcing_Shapes/Circular_Pattern.htm | Circular Pattern -->

Section Designer

# Circular Pattern

Use the Draw menu > Draw Reinforcing Shape > Circular Pattern command or the toolbar button, ![](../../../Images/IMG00086.GIF) to draw a circular pattern reinforcing shape.

1. Click the Draw menu > Draw Reinforcing Shape > Circular Pattern command or the toolbar button, ![](../../../Images/IMG00086.GIF) to enable the draw mode.
2. Left click in the active window to locate the circular pattern reinforcing. The center point of the shape is defined as the center of the bounding lines that outlines the circular pattern. The sides of those bounding lines are parallel to the Section Designer X and Y axes when the rotation of the shape is 0 degrees (see Rotation below). It is likely that center of the reinforcing shape should be placed on top of the center of the shape to which the reinforcing is being added. In that case, left click on the center point of the shape being reinforced. Alternatively, place the reinforcing at any location and use the [Reshape mode](../Reshape_Mode.md) to drag the reinforcing shape to the required location.
3. Right click on the resulting rebar to display the Shape Properties - Reinforcing form. Use the form to review, and where necessary change, the parameters defining the rectangular rebar pattern:

1. - Type: Identifies the type of reinforcing shape. It is not editable by the user.
   - Material: The material property associated with the reinforcing steel. This can be any material property with a Concrete design type. Section Designer uses the steel yield stress from the material property. The modulus of elasticity of the reinforcing is always assumed to be 29000 ksi.
   - X Center: The Section Designer X coordinate of the center of the rectangular bounding box for the reinforcing shape.
   - Y Center: The Section Designer Y coordinate of the center of the rectangular bounding box for the reinforcing shape.
   - Diameter: The diameter of the shape measured from the outside face of rebar to the outside face of rebar.
   - No. of Bars: Number of equally spaced bars for the circular reinforcing pattern.
   - Rotation: Angle (in degrees) measured from the Section Designer X-Axis to the first bar as illustrated in the sketches below. Note that the shape is rotated about the center of the bounding rectangle.

![](../../../Images/IMG00087.GIF)

![](../../../Images/IMG00088.GIF)

- - Bar Size: Specifies the size of the reinforcing bar.

See Also:

[Single Bar](Single_Bar.md)

[Line Pattern](Line_Pattern.md)

[Rectangular Pattern](Rectangular_Pattern.md)


---
<!-- source: Menus/Draw/Draw_Reinforcing_Shapes/Corner_Point_Reinforcing_Form.htm | Corner Point Reinforcing Form -->

Section Designer

# Corner Point Reinforcing Form

Use the Corner Point Reinforcing form to change the size of corner rebar.

1. Left click on the shape to select it.
2. Right click on a corner bar to display the Corner Point Reinforcing form.
3. Choose a revised bar size from the drop-down list.
4. Check the Apply to All Corners check box to specify that the selected bar size apply to all corner bars associated with the reinforcing shape.

| The Corner Point Reinforcing form is available for the following shapes:   - [Rectangular Pattern](Rectangular_Pattern.md) reinforcing shapes - [Rectangular Solid](../Draw_Solid_Shapes/Rectangle.md) shapes - [Angle](../Draw_Structural_Shapes/Angle.md), [Channel,](../Draw_Structural_Shapes/Channel.md) [I/Wide Flange](../Draw_Structural_Shapes/I_Wide_Flange.md), [Plate](../Draw_Structural_Shapes/Plate.md), and [Tee](../Draw_Structural_Shapes/Tee.md) Structural shapes - [Poly](../Draw_Poly_Shape.md) shapes |


---
<!-- source: Menus/Draw/Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.htm | Draw Reinforcing Shape -->

Section Designer

# Draw Reinforcing Shape

Section Designer offers four types of reinforcing shapes:

- [Draw menu > Draw Reinforcing Shape > Single Bar command](Single_Bar.md)
- [Draw menu > Draw Reinforcing Shape > Line Pattern command](Line_Pattern.md)
- [Draw menu > Draw Reinforcing Shape > Rectangular Pattern command](Rectangular_Pattern.md)
- [Draw menu > Draw Reinforcing Shape > Circular Pattern command](Circular_Pattern.md)

See also:

[Draw Structural Shape](../Draw_Structural_Shapes/Draw_Structural_Shapes.md)

[Draw Solid Shape](../Draw_Solid_Shapes/Draw_Solid_Shape.md)

[Draw Poly Shape](../Draw_Poly_Shape.md)

[Draw Reference Lines](../Draw_Reference_Lines/Drawing_Reference_Lines.md)


---
<!-- source: Menus/Draw/Draw_Reinforcing_Shapes/Edge_Reinforcing_Form.htm | Edge Reinforcing Form -->

Section Designer

# Edge Reinforcing Form

Use the Edge Reinforcing form to modify the size and spacing of rebar in a shape. Bars are placed along each edge of the solid and structural shape and the rectangular and circular pattern reinforcing. The bars along any edge are independent from the bars along any other edge. All of the bars along an edge have the same size and spacing.

1. Right click on the rebar to display the Edge Reinforcing form and modify the rebar size and spacing for the rebar.

- - Bar Size drop-down list. Choose a new bar size from this drop-down list. The specified size applies to all bars along the selected edge.
  - Bar Spacing drop-down list. Choose the bar spacing from this drop-down list. The specified spacing applies to all bars along the selected edge.
  - Apply to All Edges check box. When this check box is checked, any changes made to the form will apply to all edges of the shape.

| Access the Edge Reinforcing form by right clicking on any of the following   - Reinforcing shape - Rectangular solid shape with a material type that has a Concrete design type and with Reinforcing specified - Structural shape with a material type that has a Concrete design type and with Reinforcing specified |


---
<!-- source: Menus/Draw/Draw_Reinforcing_Shapes/Line_Pattern.htm | Line Pattern -->

Section Designer

# Line Pattern

Use the Draw menu > Draw Reinforcing Shape > Line Pattern command or the toolbar button, ![](../../../Images/IMG00082.GIF) to draw a line pattern reinforcing shape.

1. Click the Draw menu > Draw Reinforcing Shape > Line Pattern command or the toolbar button, ![](../../../Images/IMG00082.GIF) to enable the draw mode.
2. Left click in the active window to locate the beginning point for the line pattern reinforcing.

TIP: It is likely that the reinforcing shape should be placed on top of the shape to which the reinforcing is being added. Alternatively, place the reinforcing at any location and use the [Reshape mode](../Reshape_Mode.md) to drag the reinforcing shape to the required location.

3. Move the mouse pointer in the required direction and click the left mouse button again to specify the end point for the line pattern reinforcing.
4. Right click on the resulting line pattern reinforcing to display the Shape Properties - Reinforcing form. Use the form to review, and where necessary change, the parameters defining the line pattern reinforcing:

   - Type: Identifies the type of reinforcing shape. It is not editable by the user.
   - Material: The material property associated with the reinforcing steel. This can be any material property with a Concrete design type. Section Designer uses the steel yield stress from the material property. The modulus of elasticity of the reinforcing is always assumed to be 29000 ksi.
   - X1: The Section Designer X coordinate of the starting point of the line pattern reinforcing.
   - Y1: The Section Designer Y coordinate of the starting point of the line pattern reinforcing.
   - X2: The Section Designer X coordinate of the end point of the line pattern reinforcing.
   - Y2: The Section Designer Y coordinate of the end point of the line pattern reinforcing.
   - Bar Spacing: The specified (not necessarily actual) center to center spacing of bars along the specified line. Section Designer calculates the required number of bars by dividing the length of the line by the specified bar spacing and adding one to the result. Usually this calculation leaves some fraction of a bar left over. If that fraction is greater than 0.1, Section Designer rounds the number of bars up; otherwise it rounds the number of bars down. After Section Designer has determined the final number of bars to be used, it calculates the final bar spacing by dividing the length of the line by the final number of bars minus one.
   - Bar Size: The size of all of the reinforcing bars along the specified line.
   - End Bars: If Yes is selected, bars will be placed at the end points of the specified line. If No is selected, the first bar starts one space in from the end of the line. The sketch below illustrates line pattern reinforcing with and without end bars.

![](../../../Images/IMG00083.GIF)

See also:

[Single Bar](Single_Bar.md)

[Rectangular Pattern](Rectangular_Pattern.md)

[Circular Pattern](Circular_Pattern.md)


---
<!-- source: Menus/Draw/Draw_Reinforcing_Shapes/Rectangular_Pattern.htm | Rectangular Pattern -->

Section Designer

# Rectangular Pattern

Use the Draw menu > Draw Reinforcing Shape > Rectangular Pattern command or the toolbar button, ![](../../../Images/IMG00084.GIF) to draw a rectangular patter reinforcing shape.

1. Click the Draw menu > Draw Reinforcing Shape > Rectangular Pattern command or the toolbar button, ![](../../../Images/IMG00084.GIF) to enable the draw mode.
2. Left click anywhere in the active window to locate the rectangular pattern reinforcing. The center point of the shape is defined as the center of the bounding lines that outlines the rectangular pattern. The sides of those bounding lines are parallel to the Section Designer X and Y axes when the rotation of the shape is 0 degrees (see Rotation below). It is likely that center of the reinforcing shape should be placed on top of the center of the shape to which the reinforcing is being added. In that case, left click on the center point of the shape being reinforced. Alternatively, place the reinforcing at any location and use the [Reshape mode](../Reshape_Mode.md) to drag the reinforcing shape to the required location.
3. Right click on the resulting rebar to display the Shape Properties - Reinforcing form. Use the form to review, and where necessary change, the parameters defining the rectangular rebar pattern:

   - Type: Identifies the type of reinforcing shape. It is not editable by the user.
   - Material: Specifies the material property associated with the reinforcing steel. This can be any material property with a Concrete design type. Section Designer uses the steel yield stress from the material property. The modulus of elasticity of the reinforcing is always assumed to be 29000 ksi.
   - X Center: The Section Designer X coordinate of the center of the rectangular bounding box for the reinforcing shape.
   - Y Center: The Section Designer Y coordinate of the center of the rectangular bounding box for the reinforcing shape.
   - Height: Specifies the height of the shape measured from the outside face of rebar at the bottom of the shape to the outside face of rebar at the top of the shape when the rotation angle is equal to 0 degrees.
   - Width: Specifies the width of the shape measured from the outside face of rebar at the left side of the shape to the outside face of rebar at the right side of the shape when the rotation angle is equal to 0 degrees.
   - Rotation: Angle (in degrees) measured from the Section Designer X-Axis to the original horizontal axis of the shape. See the sketch below. Note that the shape is rotated about the center of the bounding rectangle.

![](../../../Images/IMG00085.GIF)

The size and spacing of the rebar can be modified using the [Edge Reinforcing form](Edge_Reinforcing_Form.md). The size of any corner rebar can be changed using the [Corner Point Reinforcing form.](Corner_Point_Reinforcing_Form.md)  

See also:

[Single Bar](Single_Bar.md)

[Line Pattern](Line_Pattern.md)

[Circular Pattern](Circular_Pattern.md)


---
<!-- source: Menus/Draw/Draw_Reinforcing_Shapes/Single_Bar.htm | Single Bar -->

Section Designer

# Single Bar

Use the Draw menu > Draw Reinforcing Shape > Single Bar command or the toolbar button, ![](../../../Images/IMG00081.GIF) to draw a single rebar shape.

1. Click the Draw menu > Draw Reinforcing Shape > Single Bar command or the toolbar button, ![](../../../Images/IMG00081.GIF) to enable the draw mode.
2. Left click anywhere in the active window to locate the single rebar. It is likely that the reinforcing shape should be placed on top of the shape to which the reinforcing is being added. Alternatively, place the reinforcing at any location and use the [Reshape mode](../Reshape_Mode.md) to drag the reinforcing shape to the required location.
3. Right click on the resulting rebar to display the Shape Properties - Reinforcing form. Use the form to review, and where necessary change, the parameters defining the single rebar shape:

   - Type: Identifies the type of reinforcing shape. It is not editable by the user.
   - Material: Specifies the material property for the reinforcing steel. This can be any material property with a Concrete design type. Section Designer uses the steel yield stress from the material property. The modulus of elasticity of the reinforcing is always assumed to be 29000 ksi.
   - X Center: Specifies the X coordinate of the center of the bar.
   - Y Center: Specifies the Y coordinate of the center of the bar.
   - Bar Size: Specifies the size of the reinforcing bar.
   - Steel Model:  Specify the modeling method for the rebar steel. When the Simple or Park method is selected, the program displays a form showing a plot of the stress and strain and edit boxes that can be used to specify the stress and strain parameters. Click the View/Print button to display a form showing the plot and the stress and strain parameters in tabular form. Use the Windows Print Screen and Ctrl V paste features to copy and paste the form into another program for printing purposes.

See also:

[Line Pattern](Line_Pattern.md)

[Rectangular Pattern](Rectangular_Pattern.md)

[Circular Pattern](Circular_Pattern.md)


---
<!-- source: Menus/Draw/Draw_Solid_Shapes/Circle.htm | Circle -->

Section Designer

# Circle

Use the Draw menu > Draw Solid Shape > Circle command or the toolbar button, ![](../../../Images/IMG00071.GIF) to generate a circular cross section.

1. Click the Draw menu > Draw Solid Shape > Circle command or the toolbar button, ![](../../../Images/IMG00071.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the circular shape at that location.
3. Right click on the circular shape to display the Shape Properties - Solid form and review, and if necessary change, the shape parameters:

   - Type: Identifies the type of solid shape. It is not editable by the user.
   - Material: The default material property for Circle shapes is Concrete (CONC). To change the material type, right click in the cell and select any available material property in the resulting drop-down box.
   - Color: Controls the color of the fill for the shape. Left click on the cell to bring up the Color form; use the form to set the color for the fill.
   - X Center: The Section Designer X coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
   - Y Center: The Section Designer Y coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
   - Diameter: The diameter of the circle.
   - Reinforcing: This item is visible only if the material property associated with the shape has a Concrete design type. When this item is set to Yes, the program inserts edge reinforcing bars in the shape. If this item is set to No, no reinforcing bars will be included in the shape. When this item set to No, the [Draw menu > Draw Reinforcing Shape command](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md) can be used to place rebar in the shape.
   - - # of Bars: This item is visible only if the Reinforcing item is set to Yes. Use this option to specify the number of equally spaced bars for the circular reinforcing.
     - Bar Cover: This item is visible only if the Reinforcing item is set to Yes. Use this option to specify the clear cover for the specified rebar.
     - Bar Size: This item is visible only if the Reinforcing item is set to Yes. Use this option to specify the size of the reinforcing bar.
   - Rotation: Angle (in degrees) measured from the Section Designer X-Axis to the first bar as illustrated in the sketch below. Use this option to rotate the reinforcing steel associated with the shape to any angle. Note that the shape is rotated about the center of the bounding rectangle.

![](../../../Images/IMG00072.GIF)

See Also:

[Rectangle](Rectangle.md)

[Sector](Sector.md)

[Segment](Segment.md)


---
<!-- source: Menus/Draw/Draw_Solid_Shapes/Draw_Solid_Shape.htm | Draw Solid Shape -->

Section Designer

# Draw Solid Shape

Use the subcommands on the Draw menu > Draw Solid Shape command to generate solid rectangular or circular cross sections, or add solid segments or sectors to a cross section.

- [Draw menu > Draw Solid Shape > Rectangle command](Rectangle.md)
- [Draw menu > Draw Solid Shape > Circle command](Circle.md)
- [Draw menu > Draw Solid Shape > Segment command](Segment.md)
- [Draw menu > Draw Solid Shape > Sector command](Sector.md)

See also:

[Draw Structural Shapes](../Draw_Structural_Shapes/Draw_Structural_Shapes.md)

[Draw Poly Shape](../Draw_Poly_Shape.md)

[Draw Reinforcing Shape](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md)

[Draw Reference Lines](../Draw_Reference_Lines/Drawing_Reference_Lines.md)


---
<!-- source: Menus/Draw/Draw_Solid_Shapes/Rectangle.htm | Rectangle -->

Section Designer

# Rectangle

Use the Draw menu > Draw Solid Shape > Rectangle command or the toolbar button, ![](../../../Images/IMG00069.GIF) to generate a rectangular cross section.

1. Click the Draw menu > Draw Solid Shape > Rectangle command or the toolbar button, ![](../../../Images/IMG00069.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the rectangular shape at that location.
3. Right click on the Rectangle shape to display the Shape Properties - Solid form and review, and if necessary change, the shape parameters:

- - Type: Identifies the type of solid shape. It is not editable by the user.
  - Material: The default material property for Rectangle shapes is Concrete (CONC). To change the material type,  right click in the cell and select any available material property in the resulting drop-down box.
  - Color: Controls the color of the fill for the shape. Left click on the cell to bring up the Color form; use the form to set the color for the fill.
  - X Center: The Section Designer X coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
  - Y Center: The Section Designer Y coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
  - Height: The height of the shape.
  - Width: The width of the shape.
  - Rotation: Angle (in degrees) measured from the Section Designer X-Axis to the original horizontal axis of the shape. See the sketch below. Note that the shape is rotated about the center of the bounding rectangle. When a Rectangle shape is initially drawn, the height is measured parallel to the Section Designer Y-axis and the width is measured parallel to the Section Designer X-axis. Thus initially the height is vertical and the width is horizontal. Use this option to change that orientation. For example, change this value by 90 degrees and the height will be  horizontal and the width vertical.

![](../../../Images/IMG00070.GIF)

- - Reinforcing: This item is visible only if the material property associated with the shape has a Concrete design type. When this item is set to Yes, the program inserts edge reinforcing bars in the shape. If this item is set to No, no reinforcing bars will be included in the shape. When this item set to No, the [Draw menu > Draw Reinforcing Shape command](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md) can be used to place rebar in the shape. The size and spacing of rebar can be modified using the [Edge Reinforcing form](../Draw_Reinforcing_Shapes/Edge_Reinforcing_Form.md). The size of any corner rebar can be changed using the [Corner Point Reinforcing form.](../Draw_Reinforcing_Shapes/Corner_Point_Reinforcing_Form.md)

See also:

[Circle](Circle.md)

[Sector](Sector.md)

[Segment](Segment.md)


---
<!-- source: Menus/Draw/Draw_Solid_Shapes/Sector.htm | Sector -->

Section Designer

# Sector

Use the Draw menu > Draw Solid Shape > Sector command or the toolbar button, ![](../../../Images/IMG00076.GIF) to add a solid Sector shape to a cross section. No reinforcing will be included with a sector shape. The [Draw menu > Draw Reinforcing Shape command](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md), or the toolbar button, ![](../../../Images/IMG00074.GIF), can be used to place rebar in a sector shape.

1. Click the Draw menu > Draw Solid Shape > Sector command or the toolbar button, ![](../../../Images/IMG00076.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the sector shape at that location.
3. Right click on the sector shape to display the Shape Properties - Solid form and review, and if necessary change, the shape parameters:

   - Type: Identifies the type of solid shape. It is not editable by the user.
   - Material: The default material property for Sector shapes is Concrete (CONC).  To change the material type, right click in the cell and select any available material property in the resulting drop-down box.
   - Color: Controls the color of the fill for the shape. Left click on the cell to bring up the Color form; use the form to set the color for the fill.
   - X Center: The Section Designer X coordinate of the center of the bounding box for the shape. Note that for Sector shapes the bounding box bounds the circle that defines the circular sector. Changing this coordinate relocates the shape.
   - Y Center: The Section Designer Y coordinate of the center of the bounding box for the shape. Note that for Sector shapes the bounding box bounds the circle that defines the circular sector. Changing this coordinate relocates the shape.
   - Angle: The angle (in degrees) between the two radii that define the circular sector. See the following figure for an example.
   - Rotation: The angle (in degrees) measured from the Section Designer X-axis to a radial line that bisects the Sector. See the figure below for an example.

![](../../../Images/IMG00078.GIF)

1. - Radius: The radius of the circle defining the Sector.

See also:

[Rectangle](Rectangle.md)

[Circle](Circle.md)

[Segment](Segment.md)


---
<!-- source: Menus/Draw/Draw_Solid_Shapes/Segment.htm | Segment -->

Section Designer

# Segment

Use the  Draw menu > Draw Solid Shape > Segment command or the toolbar button, ![](../../../Images/IMG00073.GIF) to add a circular segment to a cross section. No reinforcing will be included with a segment shape. The [Draw menu > Draw Reinforcing Shape command](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md), or the toolbar button, ![](../../../Images/IMG00074.GIF), can be used to place rebar in a segment shape.

1. Click the Draw menu > Draw Solid Shape > Segment command or the toolbar button, ![](../../../Images/IMG00073.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the segment shape at that location.
3. Right click on the segment shape to display the Shape Properties - Solid form and review, and if necessary change, the shape parameters:

- - Type: Identifies the type of solid shape. It is not editable by the user.
  - Material: The default material property for Segment shapes is Concrete (CONC). To change the material type, right click in the cell and select any available material property in the resulting drop-down box.
  - Color: Controls the color of the fill for the shape. Left click on the cell to bring up the Color form; use the form to set the color for the fill.
  - X Center: The Section Designer X coordinate of the center of the bounding box for the shape. Note that for Segment shapes the bounding box bounds the circle that defines the circular segment. Changing this coordinate relocates the shape.
  - Y Center: The Section Designer Y coordinate of the center of the bounding box for the shape. Note that for Segment shapes the bounding box bounds the circle that defines the circular segment. Changing this coordinate relocates the shape.
  - Angle: The angle (in degrees) between lines drawn from the center of the circle to the end points of the chord that defines the segment. See the figure below for an example.

![](../../../Images/IMG00075.GIF)

- - Rotation: The angle (in degrees) measured from the Section Designer X-axis to a radial line that bisects the segment. See the above figure.
  - Radius: The radius of the circle defining the Segment.

See also:

[Rectangle](Rectangle.md)

[Circle](Circle.md)

[Sector](Sector.md)


---
<!-- source: Menus/Draw/Draw_Stress_Point.htm | Draw Stress Point -->

Section Designer

# Stress Point

Stress points can be used to specify locations where stresses are to be reported when plotting or tabulating Frame Stress results from analysis. Any number of stress points can be drawn, including multiple points at the same location. Adding a stress point has no effect on the behavior of the section; it is a reference only.

Each stress point has the following properties:

- A name, which is used for reference only
- x and y coordinates that locate the point in the section
- A material property that is used to compute the modular ratio relative to the base material
- An index, varying from 1 to the number of stress points, that is used to identify the stress point when plotting and tabulating stress results

Stress points can be drawn anywhere in the section, including where there is no material. Stress points do not automatically use the material present where the point is drawn, but rather default to the base material. It is up to the user to assign the desired material to each stress point.

If no stress points are drawn, four stress points will be assumed to exist at the corners of the rectangular bounding box of the section, all using the base material. Whether or not any points are drawn, a default stress point (number zero) is always assumed to exist at the centroid of the section, using the base material.

To create a stress point:

1. Click the Draw menu > Draw Stress Point command or the ![](../../Images/bob.png)  button, to enable the draw mode.
2. Left click anywhere in the active window to locate a single stress point.
3. After each click, the Stress Point form will be displayed. The correct material property should be chosen, and the coordinates may be modified as necessary. Use the Up and Down arrows to change the index of the stress point, if needed.
4. Select another draw mode or Select mode to end drawing of stress points.

To modify a stress point, right click on the stress point and make the necessary changes in the Stress Point form.

To delete a stress point, select the point and press the Delete key on your keyboard.


---
<!-- source: Menus/Draw/Draw_Structural_Shapes/Angle.htm | Angle -->

Section Designer

# Angle

Use the Draw menu > Draw Structural Shape > Angle command or the toolbar button, ![](../../../Images/IMG00056.GIF) to draw an angle shape.

1. Click the Draw menu > Draw Structural Shape > Angle command or the toolbar button, ![](../../../Images/IMG00056.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the structural shape at that location. When an Angle shape is initially drawn in Section Designer, one leg of the angle is drawn parallel to the Section Designer X-Axis. This leg is called the flange of the Angle shape. The other leg is drawn parallel to the Section Designer Y-Axis and it is called the web of the angle shape. Thus, initially, the flange is horizontal and the web is vertical. This orientation changes if the Rotation item (see below) is changed. For example, if after drawing the angle shape, the Rotation value is changed by 90 degrees, the flange becomes vertical and the web becomes horizontal.
3. Right click on the shape to display the Shape Properties - Angle form and review, and if necessary change, the shape parameters:

1. - Type: The shape type is User Defined.
   - Material: The default material property for Angle shapes is Steel. To change the material type,  right click in the cell and select any available material property in the resulting drop-down box. If a material property with a Concrete design type is selected, a Reinforcing property for the shape is added to the form (see below).
   - Color: Controls the color of the fill for the shape. Left click on the cell to bring up the Color form; use the form to set the color for the fill.
   - X Center: Specifies the Section Designer X coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
   - Y Center: Specifies the Section Designer Y coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
   - Height: Specifies the height of the shape measured from the top of the web to the bottom of the flange.
   - Width: Specifies the width of the flange of the shape.
   - Flange Thick: Specifies the thickness of the flange of the shape.
   - Web Thick: Specifies the thickness of the web of the shape.
   - Rotation: Specifies the angle (in degrees) measured from the Section Designer X-Axis to the original horizontal axis of the shape. See the sketch below. Note that the shape is rotated about the center of the bounding rectangle.

![](../../../Images/IMG00057.GIF)

1. - Reinforcing: This item is visible only if the material property associated with the shape has a Concrete design type.  When this item is set to Yes, the program inserts edge reinforcing bars in the shape. If this item is set to No, no reinforcing bars will be included in the shape. When this item set to No, the [Draw menu > Draw Reinforcing Shape command](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md) can be used to place rebar in the shape. The size and spacing of rebar can be modified using the [Edge Reinforcing form](../Draw_Reinforcing_Shapes/Edge_Reinforcing_Form.md). The size of any corner rebar can be changed using the [Corner Point Reinforcing form.](../Draw_Reinforcing_Shapes/Corner_Point_Reinforcing_Form.md)

See also:

[I/Wide Flange](I_Wide_Flange.md)

[Channel](Channel.md)

[Tee](Tee.md)

[Double Angle](Double_Angle.md)

[Box/Tube](Box_Tube.md)

[Pipe](Pipe.md)

[Plate](Plate.md)


---
<!-- source: Menus/Draw/Draw_Structural_Shapes/Box_Tube.htm | Box/Tube -->

Section Designer

# Box/Tube

Use the Draw menu > Draw Structural Shape > Box/Tube command or the toolbar button, ![](../../../Images/IMG00061.GIF), to draw a box/tube shape.

1. Click the Draw menu > Draw Structural Shape > Box/Tube command or the toolbar button, ![](../../../Images/IMG00061.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the structural shape at that location. When a Box/Tube shape is initially drawn, the sides parallel to the Section Designer X-axis are called the flanges of the Box/Tube shape. The sides parallel to the Section Designer Y-axis are called the web of the Box/Tube shape. Thus, initially, the flange is horizontal and the web is vertical. This orientation changes if the Rotation item (see below) is changed. For example, if after drawing the angle shape, the Rotation value is changed by 90 degrees, the flange becomes vertical and the web becomes horizontal.
3. Right click on the shape to display the Shape Properties - Angle form and review, and if necessary change, the shape parameters:

- - Type: The shape type is User Defined.
  - Material: The default material property for Box/Tube shapes is Steel. To change the material type, right click in the cell and select any available material property in the resulting drop-down box.
  - Color: Controls the color of the fill for the shape. Left click on the cell to bring up the Color form; use the form to set the color for the fill.
  - X Center: Specifies the Section Designer X coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
  - Y Center: Specifies the Section Designer Y coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
  - Height: Specifies the height of the shape measured from the bottom of the bottom flange to the top of the top flange.
  - Width: Specifies the width of the flanges of the shape.
  - Flange Thick: Specifies the thickness of the flanges of the shape.
  - Web Thick: Specifies the thickness of the webs of the shape.
  - Rotation: Specifies the angle (in degrees) measured from the Section Designer X-Axis to the original horizontal axis of the shape. See the sketch below. Note that the shape is rotated about the center of the bounding rectangle.

![](../../../Images/IMG00063.GIF)

Note:  No reinforcing is included with a Box/Tube shape. Use the Draw menu > Draw Reinforcing Shape command, or the toolbar button, ![](../../../Images/IMG00062.GIF), to place reinforcing in a Box/Tube shape.

See also:

[I/Wide Flange](I_Wide_Flange.md)

[Channel](Channel.md)

[Tee](Tee.md)

[Angle](Angle.md)

[Double Angle](Double_Angle.md)

[Pipe](Pipe.md)

[Plate](Plate.md)


---
<!-- source: Menus/Draw/Draw_Structural_Shapes/Channel.htm | Channel -->

Section Designer

# Channel

Use the Draw menu > Draw Structural Shape > Channel command or the toolbar button, ![](../../../Images/IMG00052.GIF) to draw a channel shape.

1. Click the Draw menu > Draw Structural Shape > Channel command or the toolbar button, ![](../../../Images/IMG00052.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the structural shape at that location. The center point of the shape is defined as the center of the bounding lines that outlines the channel shape. The sides of those bounding lines are parallel to the Section Designer X and Y axes when the rotation of the shape is 0 degrees (see Rotation below).
3. Right click on the shape to display the Shape Properties - Channel form and review, and if necessary change, the shape parameters:

- - Type: The shape type is User Defined.
  - Material: The default material property for Channel shapes is Steel. To change the material type, right click in the cell and select any available material property in the resulting drop-down box. If a material property with a Concrete design type is selected, a Reinforcing property for the shape will be added to the form (see below).
  - Color: This item controls the color of the fill for the shape. Left click on the cell to bring up the Color form; use the form to set the color for the fill.
  - X Center: Specifies the Section Designer X coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
  - Y Center: Specifies the Section Designer Y coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
  - Height: Specifies the height of the shape measured from the bottom of the bottom flange to the top of the top flange.
  - Width: Specifies the width of the top and bottom flanges of the shape.
  - Flange Thick: Specifies the thickness of the top and bottom flanges of the shape.
  - Web Thick: Specifies the thickness of the web of the shape.
  - Rotation: Specifies the angle (in degrees) measured from the Section Designer X-Axis to the original horizontal axis of the shape. See the sketch below. Note that the shape is rotated about the center of the bounding rectangle.

![](../../../Images/IMG00053.GIF)

- - Reinforcing: This item is visible only if the material property associated with the shape has a Concrete design type.  When this item is set to Yes, the program inserts edge reinforcing bars in the shape. If this item is set to No, no reinforcing bars will be included in the shape. When this item set to No, the [Draw menu > Draw Reinforcing Shape command](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md) can be used to place rebar in the shape. The size and spacing of rebar can be modified using the [Edge Reinforcing form](../Draw_Reinforcing_Shapes/Edge_Reinforcing_Form.md). The size of any corner rebar can be changed using the [Corner Point Reinforcing form.](../Draw_Reinforcing_Shapes/Corner_Point_Reinforcing_Form.md)

See also:

[I/Wide Flange](I_Wide_Flange.md)

[Tee](Tee.md)

[Angle](Angle.md)

[Double Angle](Double_Angle.md)

[Box/Tube](Box_Tube.md)

[Pipe](Pipe.md)

[Plate](Plate.md)


---
<!-- source: Menus/Draw/Draw_Structural_Shapes/Double_Angle.htm | Double Angle -->

Section Designer

# Double Angle

Use the Draw menu > Draw Structural Shape > Double Angle command or the toolbar button, ![](../../../Images/IMG00058.GIF) to draw a Double Angle cross section.

1. Click the Draw menu > Draw Structural Shape > Double Angle command or the toolbar button, ![](../../../Images/IMG00056.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the structural shape at that location. When a Double Angle shape is initially drawn, the angle legs parallel to the Section Designer X-axis are called the flange of the Double Angle shape. The angle legs parallel to the Section Designer Y-axis are called the web of the Double Angle shape. Thus, initially, the flange is horizontal and the web is vertical. This orientation changes if the Rotation item (see below) is changed. For example, if after drawing the angle shape, the Rotation value is changed by 90 degrees, the flange becomes vertical and the web becomes horizontal.
3. Right click on the shape to display the Shape Properties - Double Angle form and review, and if necessary change, the shape parameters:

1. - Type: The shape type is User Defined.
   - Material: The default material property for Double Angle shapes is Steel. To change the material type, right click in the cell and select any available material property in the resulting drop-down box.
   - Color: Controls the color of the fill for the shape. Left click on the cell to bring up the Color form; use the form to set the color for the fill.
   - X Center: Specifies the Section Designer X coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
   - Y Center: Specifies the Section Designer Y coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
   - Height: Specifies the height of the shape measured from the bottom of the web to the top of the flange.
   - Width: Specifies the total width of the flange of the shape.
   - Flange Thick: Specifies the thickness of the flange of the shape.
   - Web Thick: Specifies the thickness of the web of one of the angles in the shape.
   - Separation: Specifies the distance between the webs of the two angles.
   - Rotation: Specifies the angle (in degrees) measured from the Section Designer X-Axis to the original horizontal axis of the shape. See the sketch below. Note that the shape is rotated about the center of the bounding rectangle.

![](../../../Images/IMG00060.GIF)

Note: No reinforcing is included with a double angle shape. Use the Draw menu > Draw Reinforcing Shape command, or the toolbar button, ![](../../../Images/IMG00059.GIF), to place reinforcing in a double angle shape.

See also:

[I/Wide Flange](I_Wide_Flange.md)

[Channel](Channel.md)

[Tee](Tee.md)

[Angle](Angle.md)

[Box/Tube](Box_Tube.md)

[Pipe](Pipe.md)

[Plate](Plate.md)


---
<!-- source: Menus/Draw/Draw_Structural_Shapes/Draw_Structural_Shapes.htm | Draw Structural Shapes -->

Section Designer

# Draw Structural Shapes

Section Designer offers eight types of structural shapes

- [Draw menu > Draw Structural Shapes > I/Wide Flange command](I_Wide_Flange.md)
- [Draw menu > Draw Structural Shapes > Channel command](Channel.md)
- [Draw menu > Draw Structural Shapes > Tee command](Tee.md)
- [Draw menu > Draw Structural Shapes > Angle command](Angle.md)
- [Draw menu > Draw Structural Shapes > Double Angle command](Double_Angle.md)
- [Draw menu > Draw Structural Shapes > Box/Tube command](Box_Tube.md)
- [Draw menu > Draw Structural Shapes > Pipe command](Pipe.md)
- [Draw menu > Draw Structural Shapes > Plate command](Plate.md)

See also:

[Draw Solid Shape](../Draw_Solid_Shapes/Draw_Solid_Shape.md)

[Draw Poly Shape](../Draw_Poly_Shape.md)

[Draw Reinforcing Shape](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md)

[Draw Reference Lines](../Draw_Reference_Lines/Drawing_Reference_Lines.md)


---
<!-- source: Menus/Draw/Draw_Structural_Shapes/I_Wide_Flange.htm | I/Wide Flange -->

Section Designer

# I/Wide Flange

Use the Draw menu > Draw Structural Shape > I/Wide Flange command or the toolbar button, ![](../../../Images/IMG00050.GIF) to draw an I/Wide Flange shape.

1. Click the Draw menu > Draw Structural Shape > I/Wide Flange command or the toolbar button, ![](../../../Images/IMG00050.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the structural shape at that location. The center point of the shape is defined as the center of the bounding lines that outlines the I/Wide flange shape. The sides of those bounding lines are parallel to the Section Designer X and Y axes when the rotation of the shape is 0 degrees (see Rotation below).
3. Right click on the shape to display the Shape Properties - I/Wide Flange form and review, and if necessary change, the shape parameters:

1. - Type: The shape type is User Defined.
   - Material: The default material property for I/Wide Flange shapes is Steel. To change the material type,  right click in the cell and select any available material property in the resulting drop-down box. If a material property with a Concrete design type is selected, a Reinforcing property for the shape is added to the form (see below).
   - Color: Controls the color of the fill for the shape. Left click on the cell to bring up the Color form and set the color for the fill.
   - X Center: Specifies the Section Designer X coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
   - Y Center: Specifies the Section Designer Y coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
   - Height: Specifies the height of the shape measured from the bottom of the bottom flange to the top of the top flange.
   - Top Width: Specifies the width of the top flange of the shape.
   - Top Thick: Specifies the thickness of the top flange of the shape.
   - Web Thick: Specifies the thickness of the web of the shape.
   - Bot Width: Specifies the width of the bottom flange of the shape.
   - Bot Thick: Specifies the thickness of the bottom flange of the shape.
   - Rotation: Specifies the angle (in degrees) measured from the Section Designer X-Axis to the original horizontal axis of the shape. See the sketch below. Note that the shape is rotated about the center of the bounding rectangle.

![](../../../Images/IMG00051.GIF)

1. - Reinforcing: This item is visible only if the material property associated with the shape has a Concrete design type. When this item is set to Yes, the program inserts edge reinforcing bars in the shape. If this item is set to No, no reinforcing bars will be included in the shape. When this item set to No, the [Draw menu > Draw Reinforcing Shape command](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md) can be used to place rebar in the shape. The size and spacing of rebar can be modified using the [Edge Reinforcing form](../Draw_Reinforcing_Shapes/Edge_Reinforcing_Form.md). The size of any corner rebar can be changed using the [Corner Point Reinforcing form.](../Draw_Reinforcing_Shapes/Corner_Point_Reinforcing_Form.md)

See also:

[Channel](Channel.md)

[Tee](Tee.md)

[Angle](Angle.md)

[Double Angle](Double_Angle.md)

[Box/Tube](Box_Tube.md)

[Pipe](Pipe.md)

[Plate](Plate.md)


---
<!-- source: Menus/Draw/Draw_Structural_Shapes/Pipe.htm | Pipe -->

Section Designer

# Pipe

Use the Draw menu > Draw Structural Shape > Pipe command or the toolbar button, ![](../../../Images/IMG00064.GIF) to draw a pipe shape.

1. Click the Draw menu > Draw Structural Shape > Pipe command or the toolbar button, ![](../../../Images/IMG00064.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the structural shape at that location. The center point of the shape is defined as the center of the bounding lines that outlines the pipe shape. The sides of those bounding lines are parallel to the Section Designer X and Y axes.
3. Right click on the shape to display the Shape Properties - Pipe form and review, and if necessary change, the shape parameters:

- - Type: The shape type is User Defined.
  - Material: The default material property for Pipe shapes is Steel. To change the material type, right click in the cell and select any available material property in the resulting drop-down box.
  - Color: Controls the color of the fill for the shape. Left click on the cell to bring up the Color form; use the form to set the color for the fill.
  - X Center: Specifies the Section Designer X coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
  - Y Center: Specifies the Section Designer Y coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
  - Outer Diameter: Specifies the diameter of the pipe measured to the outside face of the pipe wall.
  - Wall: Specifies the thickness of the pipe wall.

Note: No reinforcing is included with a Pipe shape. Use the Draw menu > Draw Reinforcing Shape command, or toolbar button, ,![](../../../Images/IMG00065.GIF) to place reinforcing in a Pipe shape.

See also:

[I/Wide Flange](I_Wide_Flange.md)

[Channel](Channel.md)

[Tee](Tee.md)

[Angle](Angle.md)

[Double Angle](Double_Angle.md)

[Box/Tube](Box_Tube.md)

[Plate](Plate.md)


---
<!-- source: Menus/Draw/Draw_Structural_Shapes/Plate.htm | Plate -->

Section Designer

# Plate

Use the Draw menu > Draw Structural Shape > Plate command or the toolbar button,![](../../../Images/IMG00066.GIF) to draw a plate shape.

1. Click the Draw menu > Draw Structural Shape > Plate command or the toolbar button, ![](../../../Images/IMG00066.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the structural shape at that location. The center point of the shape is defined as the center of the bounding lines that outlines the plate shape. The sides of those bounding lines are parallel to the Section Designer X and Y axes when the rotation of the shape is 0 degrees (see Rotation below).
3. Right click on the shape to display the Shape Properties - Plate form and review, and if necessary change, the shape parameters:

1. - Type: This item is Plate to identify the type of structural shape. It is not editable by the user.
   - Material: The default material property for Plate shapes is Steel. To change the material type, right click in the cell and select any available material property in the resulting drop-down box. If a material property with a Concrete design type is selected, a Reinforcing property for the shape is added to the form (see below).
   - Color: Controls the color of the fill for the shape. Left click on the cell to bring up the Color form; use the form to set the color for the fill.
   - X Center: Specifies the Section Designer X coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
   - Y Center: Specifies the Section Designer Y coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
   - Thick: Specifies the thickness of the shape. When the rotation angle is 0 degrees the thickness is measured parallel to the Section Designer Y-axis.
   - Width: Specifies the width of the shape. When the rotation angle is 0 degrees the width is measured parallel to the Section Designer X-axis.
   - Rotation: Specifies the angle (in degrees) measured from the Section Designer X-Axis to the original horizontal axis of the shape. See the sketch below. Note that the shape is rotated about the center of the bounding rectangle.

![](../../../Images/IMG00067.GIF)

1. - Reinforcing: This item is visible only if the material property associated with the shape has a Concrete design type.  When this item is set to Yes, the program inserts edge reinforcing bars in the shape. If this item is set to No, no reinforcing bars will be included in the shape. When this item set to No, the [Draw menu > Draw Reinforcing Shape command](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md) can be used to place rebar in the shape. The size and spacing of rebar can be modified using the [Edge Reinforcing form](../Draw_Reinforcing_Shapes/Edge_Reinforcing_Form.md). The size of any corner rebar can be changed using the [Corner Point Reinforcing form.](../Draw_Reinforcing_Shapes/Corner_Point_Reinforcing_Form.md)

See also:

[I/Wide Flange](I_Wide_Flange.md)

[Channel](Channel.md)

[Tee](Tee.md)

[Angle](Angle.md)

[Double Angle](Double_Angle.md)

[Box/Tube](Box_Tube.md)

[Pipe](Pipe.md)


---
<!-- source: Menus/Draw/Draw_Structural_Shapes/Tee.htm | Tee -->

Section Designer

# Tee

Use the Draw menu > Draw Structural Shape > Tee command or the toolbar button, ![](../../../Images/IMG00054.GIF) to draw a Tee shape.

1. Click the Draw menu > Draw Structural Shape > Tee command or the toolbar button, ![](../../../Images/IMG00054.GIF) to enable the draw mode.
2. Left click anywhere in the active window to place the structural shape at that location. The center point of the shape is defined as the center of the bounding lines that outlines the Tee shape. The sides of those bounding lines are parallel to the Section Designer X and Y axes when the rotation of the shape is 0 degrees (see Rotation below).
3. Right click on the shape to display the Shape Properties - Tee form and review, and if necessary change, the shape parameters:

- - Type: The shape type is User Defined.
  - Material: The default material property for Tee shapes is Steel. To change the material type, right click in the cell and select any available material property in the resulting drop-down box. If a material property with a Concrete design type is selected, a Reinforcing property for the shape is added to the form (see below).
  - Color: This item controls the color of the fill for the shape. Left click on the cell to bring up the Color form; use the form to set the color for the fill.
  - X Center: Specifies the Section Designer X coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
  - Y Center: Specifies the Section Designer Y coordinate of the center of the bounding box for the shape. Changing this coordinate relocates the shape.
  - Height: Specifies the height of the shape measured from the bottom of the web to the top of the flange.
  - Width: Specifies the width of the flange of the shape.
  - Flange Thick: Specifies the thickness of the flange of the shape.
  - Web Thick: Specifies the thickness of the web of the shape.
  - Rotation: Specifies the angle (in degrees) measured from the Section Designer X-Axis to the original horizontal axis of the shape. See the sketch below. Note that the shape is rotated about the center of the bounding rectangle.

![](../../../Images/IMG00055.GIF)

- - Reinforcing: This item is visible only if the material property associated with the shape has a Concrete design type.  When this item is set to Yes, the program inserts edge reinforcing bars in the shape. If this item is set to No, no reinforcing bars will be included in the shape. When this item set to No, the [Draw menu > Draw Reinforcing Shape command](../Draw_Reinforcing_Shapes/Draw_Reinforcing_Shape.md) can be used to place rebar in the shape. The size and spacing of rebar can be modified using the [Edge Reinforcing form](../Draw_Reinforcing_Shapes/Edge_Reinforcing_Form.md). The size of any corner rebar can be changed using the [Corner Point Reinforcing form.](../Draw_Reinforcing_Shapes/Corner_Point_Reinforcing_Form.md)

See also:

[I/Wide Flange](I_Wide_Flange.md)

[Channel](Channel.md)

[Angle](Angle.md)

[Double Angle](Double_Angle.md)

[Box/Tube](Box_Tube.md)

[Pipe](Pipe.md)

[Plate](Plate.md)


---
<!-- source: Menus/Draw/Reshape_Mode.htm | Reshape Mode -->

Section
Designer

# Reshape Mode

Click the Draw menu > Reshape
Mode command or the Reshaper button,
![](../../Images/IMG00047.GIF),  to activate the Reshape Mode,
and complete any of the following actions:

- Left
  click on a shape and while holding down the left mouse button drag
  the shape to a new location.

- For
  poly shapes, left click on the shape once to display selection handles
  at the end or corner points of the shape; then perform the following
  actions:
- - Left
    click on a selection handle at the end or corner point of the
    shape, hold down the mouse left button, and drag that point to
    a new location.
  - Right
    click on a selection handle at the end or corner point of the
    shape to bring up the Edit Selected Point
    form. There are two options:
  - Change
    Coordinates to: Enter new *X* and *Y* coordinates
    for the point and/or enter a non-zero *Radius* to “round”
    the corner point with an arc tangent to the two adjacent edges.
    A *Radius* of zero indicates no rounding.
  - Delete
    This Point: The corner point will be deleted, and the two
    adjacent edges will be replaced with a single straight line
    from the previous corner point to the next corner point.- Right
    click on a polygon edge to divide the edge into several edges.
    New corner points will be created between adjacent new edges.
    There are two options:
  - Divide
    into Specified Number of Segments: Choose two or more segments.
    Specify the *Last/First Length Ratio* as unity for equal-length
    segments, specify a larger value for gradually increasing
    lengths from the start to the end of the original edge, or
    a smaller value for decreasing lengths. The difference in
    length between any pair of adjacent new segments is constant.
  - Divide
    at Specified Distance from I-end of Edge: Specify the relative
    or absolute distance from the start of the edge to a single
    new corner point that divides the edge into two new segment.
- For
  shapes that are not poly shapes and are not rotated (i.e., Rotation
  = 0°), left
  click on the shape once to display selection handles on a bounding
  box around the shape; then perform the following actions:
- - Left
    click on a selection handle, hold down the mouse left button,
    and drag the selection handle to change the dimensions of the
    shape.
  - Right
    click on the shape to access the Shape
    Properties form. Use that form to change the X and Y coordinates
    of the point and then click the OK
    button.

Exit the Reshape Mode as follows:

- Click
  the Pointer button, ![](../../Images/IMG00048.GIF)

- Press
  the Esc key on the keyboard.

- Choose
  one of the drawing options from the Draw menu or the side toolbar.

- Click
  a Select menu command.

- Exit
  Section Designer.


---
<!-- source: Menus/Draw/Select_Mode.htm | Select Mode -->

Section Designer

# Select Mode

Use the Draw menu > Select Mode command or click the Pointer button, ![](../../Images/IMG00046.GIF), to enable the select mode; then click the mouse to select objects in the active window. The select mode can also be activated using any of the Select menu command, or by pressing the Esc key on the keyboard when any of the Draw commands (e.g., Draw Structural Shape, Draw Solid Shape and so forth) or the Reshape Mode are active.

The Option menu > Preference command provides access to the Screen Snap To Tolerance option. Use that option to specify the minimum distance between the mouse pointer and the shape being selected for the selection to be effective.


---
<!-- source: Menus/Draw/Snap_to.htm | Snap To -->

Section Designer

# Snap To

Use the Draw menu > Snap To commands when drawing or editing lines or poly shapes to facilitate accurate connectivity. Section Designers offers six features that can be toggled on or off in any combination using the Draw menu > Snap to command or the six snap feature toolbar buttons on the side toolbar.

- Guideline Intersections and Points, ![](../../Images/IMG00092.GIF): Snaps to guideline intersections and to the corner, end and center points of shapes.

- Line Ends and Midpoints, ![](../../Images/IMG00093.GIF): Snaps to the ends and midpoints of lines and edges of shapes. Note that the end of an edge of a shape is a corner point of the shape.

- Line Intersections, ![](../../Images/IMG00094.GIF): Snaps to the intersections of lines with other lines and with the edges of shapes. It does not snap to the intersection of the edge of one shape with the edge of another shape.

- Perpendicular Projections, ![](../../Images/IMG00095.GIF): To use this feature, first draw the first point for a [line](Draw_Reference_Lines/Line.md) or [shape](Draw_Poly_Shape.md). Then, if this snap feature is active, place the mouse pointer over another line or edge of a shape and left click. A line object or edge of a shape is drawn from the first point perpendicular to the line object or edge of a shape that the mouse pointer was over when the second point was clicked.

- Lines and Edges, ![](../../Images/IMG00096.GIF): Snaps to guidelines, lines and edges of shapes.

- Snap to Fine Grid, ![](../../Images/IMG00097.GIF): Snaps to an invisible grid of points. The spacing of the points is controlled by the Fine Grids Between Guidelines option on the Preferences form, which can be accessed using the [Options menu > Preferences command](../Options/Preferences.md).

Use the following procedure for the snap commands:

1. If the appropriate snap tool is not already activated, select it from the side toolbar or from the Draw menu > Snap to command.
2. Move the mouse pointer in the graphics window. When a snap location is found close to the mouse pointer, a dot appears at the snap location as well as a pop-up text field describing the snap location (i.e., point, line edge, and so forth).

Note: The distance that the pointer must be from a snap location before it snaps to that location is controlled by the Screen Snap to Tolerance itemon the Preferences form, which can be accessed using the [Options menu > Preferences command](../Options/Preferences.md).

3. When the desired snap location has been found, click the left mouse button to accept it.
4. Modify the snap options if necessary and continue drawing or editing objects.

The snap options are evaluated in the order they are listed above. If more than one snap option is active and the mouse pointer is located such that it is within the screen snap to tolerance of two different snap features, the program will apply the snap feature that is first in the list above. This is true even if the item associated with the other snap feature is closer to the mouse pointer, as long as both items are still within the screen snap to tolerance.

As an example, assume that Snap to Line Intersections and Snap to Fine Grids are both active. Assume that the mouse pointer is located such that it is within the screen snap to tolerance of both an intersection of two lines and one of the invisible grid points. The snap will be to the intersection of the two lines because this snap feature occurs first in the above list.

When two items from the same snap feature are within the screen snap to tolerance of the mouse pointer, the snap occurs to the first drawn item which may or may not be the closest item.


---
<!-- source: Menus/Draw/Steel_Model_Form.htm | Steel Model Form -->

Section Designer

# Steel Model Form

The Steel Model form displays a plot of the steel model.

- Name display box. The name of the steel material is displayed in this box.
- Various edit boxes and drop-down lists. The various parameters that define the shape are shown on the form in edit and display boxes. The parameters are shown for informational purposes only and cannot be edited using this form.
- Display area. The model curve is displayed in this area. Run the mouse pointer over the curve in the display area and the values for that point in the curve display in the lower left-hand corner of the display area.
- View/Print button. Click this button to display the Stress-Strain Curve Report form. That form shows a graphical representation of the curve in the upper portion of the display area and a table of the strain and stress at specific points in the lower portion of the display area. The contents of the display area can be printed using a screen capture or using standard Windows copy and paste (i.e., Ctrl C and Ctrl V) commands.

| Access the Steel Model form as follows:   1. Draw a shape with a steel Material type other than a Caltrans shape. 2. Right-click on the shape to display the Shape Properties form. 3. Click the S Model button. |


---
<!-- source: Menus/Draw/Stress_Strain_Curve_Report_Form.htm | Stress Strain Curve Report Form -->

Section Designer

# Stress-Strain Curve Report Form

The Stress-Strain Curve Report form provides a graphical representation of the concrete or steel model in the upper portion of the display area. A table of the strain and stress values for each point on the curve is provided in the lower portion of the form. Use the scroll bar on the right-hand side of the display area to scroll from top to bottom.

The data shown in the display area can be printed by performing a screen capture, or by using standard Windows copy and paste commands (Ctrl C and Crrl V) to paste the graphic and table into other software, such as Excel or Word, for printing.

Screen Capture:

1. Press the Print Screen key on the keyboard to copy the entire screen as a picture to the clipboard, including the title bars and toolbar. Pressing the Alt key and the Print Screen key simultaneously will copy only the Stress-Strain Curve Report form to the clipboard.
2. Use Window's  Ctrl V feature to paste the screen capture into another Windows  program, such as Word, Excel, PowerPoint or Access.

Copy and Paste:

1. Click in the display area of the Stress-Strain Curve Report form.
2. Drag the mouse over the area to be copied.
3. Press Ctrl V on the keyboard to copy the selection to the clipboard.
4. Switch to the program into which the copied material is to be pasted.
5. Press Ctrl C to paste the material into the target program.

| Access the Stress-Strain Curve Report form as follows:   1. Draw a shape other than a Caltrans shape. 2. Right-click on the shape to display the Shape Properties form. 3. Click the C Model or  S Model button to display the Concrete Model or Steel Model form, respectively.     - On the Concrete Model form, click the View Values or Print button.    - On the Steel Model form, click the View/Print button.   This form also displays when various View Values or Print buttons and View/Print buttons on forms associated with the Caltrans Section Properties form. |


---
<!-- source: Menus/Edit/Align.htm | Align -->

Section Designer

# Align

Use the Edit menu > Align command to align two or more shapes in a section. To understand how the align command works, visualize each shape enclosed by an imaginary bounding rectangle. The sides of the bounding rectangle always remain parallel to the Section Designer X and Y axes regardless of the rotation angle specified for the shape. In most cases (except for circles), changing the rotation angle can change the size of the imaginary bounding box.

Special note: For segments and sectors the bounding box is taken around the circle that defines the segment or sector rather than just the segment or sector itself.

1. Select at least two shapes to be aligned.

TIP: The Edit menu > Align command always aligns the selected shapes to the first selected shape. Thus,select the shape to which the others will be aligned, rather than windowing to select all of the shapes at the same time

2. Click the Edit menu > Align command and the appropriate subcommand:

1. - X Left: Horizontally aligns the left side of the imaginary bounding rectangle of each selected shape to the left side of the imaginary bounding rectangle of the first selected shape.
   - X Center: Horizontally aligns the center of the imaginary bounding rectangle of each selected shape to the center of the imaginary bounding rectangle of the first selected shape.
   - X Right: Horizontally aligns the right side of the imaginary bounding rectangle of each selected shape to the right side of the imaginary bounding rectangle of the first selected shape.
   - Y Top: Vertically aligns the top of the imaginary bounding rectangle of each selected shape to the top of the imaginary bounding rectangle of the first selected shape.
   - Y Middle: Vertically aligns the middle (center) of the imaginary bounding rectangle of each selected shape to the middle (center) of the imaginary bounding rectangle of the first selected shape.
   - Y Bottom: Vertically aligns the bottom of the imaginary bounding rectangle of each selected shape to the bottom of the imaginary bounding rectangle of the first selected shape.


---
<!-- source: Menus/Edit/Change_Bar_Shape_to_Single_Bars.htm | Change Bar Shape to Single Bars -->

Section Designer

# Change Bar Shape to Single Bars

Use the Edit menu > Change Bar Shape to Single Bars command to change [line pattern](../Draw/Draw_Reinforcing_Shapes/Line_Pattern.md), [rectangular pattern](../Draw/Draw_Reinforcing_Shapes/Rectangular_Pattern.md) and [circular pattern](../Draw/Draw_Reinforcing_Shapes/Circular_Pattern.md) reinforcing shapes, and the reinforcing directly associated with [poly shapes](../Draw/Draw_Poly_Shape.md), to a series of single bar reinforcing shapes. This command does not apply to structural or solid shapes.

Select the reinforcing by left clicking on it before using this command.

To change the bars associated with a solid or structural shape to single bars, first use the [Edit menu > Change Shape to Poly command](Change_Shape_to_Poly.md) to change the structural or solid shape to a poly shape.


---
<!-- source: Menus/Edit/Change_Shape_to_Poly.htm | Change Shape to Poly -->

Section Designer

# Change Shape to Poly

Use the Edit menu > Change Shape to Poly command to convert [structural shapes](../Draw/Draw_Structural_Shapes/Draw_Structural_Shapes.md) and [solid shapes](../Draw/Draw_Solid_Shapes/Draw_Solid_Shape.md) to [poly shapes](../Draw/Draw_Poly_Shape.md). The geometry of structural and solid shapes is defined by specified height and width items. The geometry of poly shapes is defined by the coordinates of the corner points of the poly shape. Converting a structural or solid shape to a poly shape allows the geometry of the shape to be tweaked in ways that otherwise would not be possible.

1. Select the shape by left clicking on.
2. Click the Edit menu > Change Shape to Poly command.

See Also

[Merge Two Polys](Merge_Two_Polys.md)

[Get Two Polys Differences](Get_Two_Polys_Differences.md)

[Get Two Polys Intersections](Get_Two_Polys_Intersections.md)

[Remove Bottom Polys overlapping area](Remove_Bottom_Polys_overlapping_area.md)

[Divide Selected Polys](Divide_Selected_Polys.md)


---
<!-- source: Menus/Edit/Check_Section_for_Overlaps.htm | Check Section for Overlaps -->

Section Designer

# Check Section for Overlaps

Use the Edit menu > Check Section for Overlaps command to check the section for areas that overlap.

It is not necessary to select the section or shapes before using this command.

A message box will appear to confirm that the section has been checked and no warnings have been generated, or the message box will display the warning message.

If a warning message is displayed, the areas of overlap can be [merged](Merge_Two_Polys.md) if the shapes have the same material property or [removed](Remove_Bottom_Polys_overlapping_area.md) if the shapes have different material properties.


---
<!-- source: Menus/Edit/Delete.htm | Delete -->

Section Designer

# Delete

Select a shape(s) in the display area and click the Edit menu > Delete command to delete the selected shape(s) and all of its associated properties from the section definition. The Delete key on the keyboard also can be used to delete selected shapes.

TIP:  The Undo ![](../../Images/IMG00037.GIF) can be used to restore a shape that has been deleted accidentally.


---
<!-- source: Menus/Edit/Divide_Selected_Polys.htm | Divide Selected Polys -->

Section Designer

# Divide Selected Polys

Use the Edit menu > Divide Selected Polys command when two or move shapes overlap.

1. Select the polys shapes to be divided. Note that the shapes must be poly shapes and must share an overlap. This command does not work for structural, solid, or Caltrans shapes. The Edit menu > Change Shape to Poly command can be used to change structural and solid shapes into poly shapes before using this command (Caltrans shapes cannot be changed to poly shapes).
2. Click the Edit menu > Divide Selected Polys command. The program will divide the shapes into individual shapes, with the area of overlap becoming a shape and the areas outside the overlap becoming a separate shapes.

See Also

[Remove Bottom Polys overlapping area](Remove_Bottom_Polys_overlapping_area.md)

[Merge Areas](Merge_Two_Polys.md)

.


---
<!-- source: Menus/Edit/Get_Two_Polys_Differences.htm | Get Two Polys Differences -->

Section Designer

# Get Two Polys Differences

Use the Edit menu > Get Two Polys Differences command to eliminate the area of overlap for two selected shapes. Select the shapes by left clicking on them before using this command.

The shapes must overlap for the command to be available. An error message will display if more than two shapes are selected or if the selected areas do not overlap. The outline of the resulting shape will consist of the outline of the two shapes excluding any areas of overlap.

See Also

[Merge Areas](Merge_Two_Polys.md)

[Get Two Polys Intersections](Get_Two_Polys_Intersections.md)

[Remove Overlapping Areas](Remove_Bottom_Polys_overlapping_area.md)

[Check Section for Overlaps](Check_Section_for_Overlaps.md)


---
<!-- source: Menus/Edit/Get_Two_Polys_Intersections.htm | Get Two Polys Intersections -->

Section Designer

# Get Two Polys Intersections

Use the Edit menu > Get Two Polys Intersections command to limit the resulting shape to the area of overlap for two selected shapes. Select the shapes by left clicking on them before using this command.

The shapes must overlap for the command to be available. An error message will display if more than two shapes are selected or if the selected areas do not overlap. The outline of the resulting shape will consist of the outline of the two shapes where they overlap only.

See Also

[Merge Areas](Merge_Two_Polys.md)

[Get Two Polys Differences](Get_Two_Polys_Differences.md)

[Remove Overlapping Areas](Remove_Bottom_Polys_overlapping_area.md)

[Check Section for Overlaps](Check_Section_for_Overlaps.md)


---
<!-- source: Menus/Edit/Merge_Two_Polys.htm | Merge Two Polys -->

Section Designer

# Merge Two Polys

Use the Edit menu > Merge Two Polys command to merge two selected shapes that have the same material property. Select the shapes by left clicking on them before using this command.

The shapes must overlap for the command to be available. An error message will display if more than two shapes are selected or if the selected areas do not overlap. The outline of the resulting shape will consist of the outline of the two shapes where they do not overlap.

If reinforcing is present in one of the shapes selected for merging, the reinforcing will be distributed throughout the resulting merged shape. If reinforcing is present in both shapes, the default rebar size and spacing will be applied to the resulting shape. Thus, if areas are to be merged and specific sizing or spacing of rebar is required, it is more efficient to merge the shapes and then specify the size and spacing of rebar.

See Also

[Get Two Polys Intersections](Get_Two_Polys_Intersections.md)

[Get Get Two Polys Differences](Get_Two_Polys_Differences.md)

[Remove Bottom Polys overlapping Area](Remove_Bottom_Polys_overlapping_area.md)

[Check Section for Overlaps](Check_Section_for_Overlaps.md)


---
<!-- source: Menus/Edit/Move_Forward_and_Move_Backward.htm | Move Forward and Move Backward -->

Section Designer

# Move Forward and Move Backward

Use the Edit menu > Move Forward and Edit menu > Move Backward commands to arrange two shapes such that one is on top of the other. Recall that the top shape controls the calculations for the shape, including properties, fibers, interaction surface, moment-curvature and so on. Thus, the section acts as if only the shape on top (i.e., the shape moved forward in this context) is present whenever two shapes overlap. The shape on the bottom (i.e., the shape moved backward in this context) is hidden beneath the other shape and is excluded from calculations. Note, however, that any shape that is entirely within another shape is ALWAYS treated as being on top, regardless of user settings.

1. Click the shape to be moved forward or backward.
2. Click the Edit menu > Move Forward or Edit menu > Move Backward command.

See Also

[Get Two Polys Differences](Get_Two_Polys_Differences.md)

[Get Two Polys Intersections](Get_Two_Polys_Intersections.md)


---
<!-- source: Menus/Edit/Nudge_Feature.htm | Nudge Feature -->

Section Designer

# Nudge Feature

Section Designer includes a nudge feature that can be used to modify the geometry of a section by "nudging" shapes. To use the nudge feature, select the shape(s) to be nudged by left clicking on it and then press the Ctrl key and one of the arrow keys on the keyboard simultaneously. Note the following about the nudge feature:

- Pressing the Ctrl key plus the right arrow key nudges the object in the positive Section Designer X direction.

- Pressing the Ctrl key plus the left arrow key nudges the object in the negative Section Designer X direction.

- Pressing the Ctrl key plus the up arrow key nudges the object in the positive Section Designer Y direction.

- Pressing the Ctrl key plus the down arrow key nudges the object in the negative Section Designer Y direction.

The distance that the shape(s) is nudged (moved) is controlled by the Nudge Value item in the Section Designer [Preferences](../Options/Preferences.md).


---
<!-- source: Menus/Edit/Remove_Bottom_Polys_overlapping_area.htm | Remove Bottom Polys overlapping area -->

Section Designer

# Remove Bottom Polys overlapping area

Use the Edit menu > Remove Bottom Polys overlapping area command to eliminate the areas of overlap for two selected shapes that have different material properties. Select the shapes by left clicking on them before using this command.

The shapes must overlap for the command to be available. A message to select two shapes with different material properties will display if the two shapes selected have the same material property. The material property of a shape can be verified as well as changed by right clicking on the shape to display the Shape Properties form. Use the Material drop-down list to select a new material property.

The resulting shape will consist of the two shapes with the area of overlap of one of the shapes removed.

See Also

[Merge Areas](Merge_Two_Polys.md)

[Get Two Polys Intersections](Get_Two_Polys_Intersections.md)

[Get Two Polys Differences](Get_Two_Polys_Differences.md)

[Check Section for Overlaps](Check_Section_for_Overlaps.md)


---
<!-- source: Menus/Edit/Replicate.htm | Replicate -->

Section Designer

# Replicate

Form: Replicate

Use the Edit menu > Replicate command to speed drawing operations by adding duplicate shapes quickly.

1. Select the objects to be replicated.
2. Click the Edit menu > Replicate command and choose the Linear, Radial, or Mirror tab to complete the following types of replication.

- Replicate in a Linear Array

- - 1. Click the Linear tab.
    2. Fill in the dx, dy and dz offset distances in the Increments edit boxes.
    3. Type the number of times the selected entities are to be replicated in the Number edit box.
    4. Click the OK button.

- Replicate in a Radial Array

- - 1. Click on the Radial tab.
    2. Type the ordinates to shift the radial replication in the edit boxes in the Intersection of Plane with XY Plane area of the form.
    3. Type the increment angle and the number of times the selected entities is to be replicated in the Increment Data edit boxes.
    4. Click the OK button.
  - Replicate Using the Mirroring Option

- 1. Click on the Mirror tab.
  2. Select the axis (X Axis, Y Axis) or define a General Line about which the selected object should be replaced. Define the General Line by entering coordinate values in the x1/y1 and x2/y2 edit boxes.
  3. Click the OK button.


---
<!-- source: Menus/Edit/Undo_and_Redo.htm | Undo and Redo -->

Section Designer

# Undo and Redo

Use the Edit menu > Undo command or Undo ![](../../Images/IMG00037.GIF) button to reverse actions performed on the shape(s) shown in the display area. The Undo feature works for multiple steps back to when the current Section Designer session was initiated. For example, if the properties of one or more objects is changed, the Edit menu > Undo command or Undo button can be used to restore the former section property in the order in which it was defined. That is, the command or button cannot be used to selectively reverse a drawing action out of sequence.

Use the Edit menu > Redo command or  Redo button,![](../../Images/IMG00038.GIF), to restore actions that have been undone.


---
<!-- source: Menus/File/Exit_Return_to_Sap.htm | Exit Return to Sap -->

Section Designer

# Exit - Return to SAP2000

Click the File menu > Exit - Return to SAP2000 command to close Section Designer and return to the SD Section Data form in SAP2000.  If a cross section has been drawn/defined using Section Designer, the OK button on the SD Section Data form will be enabled, allowing the cross section definition to be saved. If no cross section was created using Section Designer, the OK button will not be enabled; click the Cancel button to close the SD Section Data form without adding a new section definition to the model.

Note:  The SAP2000 model file must be saved for the section definition created using Section Designer to be saved.


---
<!-- source: Menus/File/Import_Section_from_DXF.htm | Import Section from DXF -->

Section
Designer

# Import Section from DXF

Use the File menu > Import
Section from DXF command to import geometry into Section Designer
from a \*.dxf AutoCAD Drawing Interchange File.

Upon executing the command, a dialog will appear
to choose a DXF file to import.

After selecting a DXF file the DXF Import form is
displayed with data that was read from the selected DXF file. The columns
of data on this form include:

- Import - indicates whether a particular entity
  will be imported
- DXF Layer - the layer in the DXF file that
  the entity is on
- DXF Entity - the entity type in the DXF file
- SD Material - the material to be assigned
  to the entity when imported
- Import As - the Section Designer shape type
  to import the entity as
- Radius/Thickness - the radius or thickness
  for applicable shape types
- Rebar - the reinforcement bar size when the
  Import As option is a rebar shape type
- Spacing - the spacing of reinforcement bars

The shape types currently supported in the Import
As column include:

- Plate
- Polygon
- Reference Line
- Reference Circle
- Rebar
- Line Bar
- Rectangle Bar
- Circle Bar
- Pipe
- Box
- Rectangle
- Circle

Section Designer will use the following defaults
for the various DXF entity types when the DXF file is first selected.

|  |  |  |  |
| --- | --- | --- | --- |
| **DXF Entity** | **Material** | **Import As** | **Remarks** |
| **LINE** | Default Steel | Plate |  |
| **LWPOLYLINE** | Default Concrete | Polygon | Only straight segments allowed. |
| **POLYLINE** | Default Concrete | Polygon | Only straight segments allowed and they must be in a 2-D plane. All Z coordinates are ignored. |
| **CIRCLE** | Default Concrete | Polygon |  |
| **POINT** | Default Rebar | Rebar |  |
| **3DFACE** | Default Concrete | Rectangle |  |
| **ARC** |  |  | Not currently supported. |

The following options are available for importing
the different DXF entity types.

|  |  |  |  |
| --- | --- | --- | --- |
| **DXF Entity** | **Material** | **Import As** | **Remarks** |
| **LWPOLYLINE** | NONE | N/A |  |
|  | OPENING | Opening | Only straight segments allowed. |
|  | Concrete | Polygon | Only straight segments allowed. |
|  | Steel | Polygon | Only straight segments allowed. |
| **POLYLINE** | NONE | N/A |  |
|  | OPENING | Opening | Only straight segments allowed and they must be in a 2-D plane. All Z coordinates are ignored. |
|  | Concrete | Polygon | Only straight segments allowed and they must be in a 2-D plane. All Z coordinates are ignored. |
|  | Steel | Polygon | Only straight segments allowed and they must be in a 2-D plane. All Z coordinates are ignored. |
| **CIRCLE** | NONE | Reference Circle |  |
|  | OPENING | Circle |  |
|  | OPENING | Pipe |  |
|  | Concrete | Circle |  |
|  | Concrete | Polygon |  |
|  | Concrete | Pipe |  |
|  | Steel | Circle |  |
|  | Steel | Pipe |  |
|  | Rebar | Circle Bar |  |
| **POINT** | NONE | N/A |  |
|  | OPENING | N/A |  |
|  | Rebar | Point Rebar |  |
|  | Tendon | Point Tendon |  |
| **LINE** | NONE | Reference Line |  |
|  | OPENING | N/A |  |
|  | Rebar | Line Bar |  |
|  | Tendon | Line Bar |  |
|  | Concrete | Plate |  |
|  | Steel | Plate |  |
| **3DFACE** | NONE | N/A |  |
|  | OPENING | Rectangle |  |
|  | OPENING | Box |  |
|  | Concrete | Rectangle |  |
|  | Concrete | Box |  |
|  | Steel | Rectangle |  |
|  | Steel | Box |  |
|  | Rebar | Rect Bar |  |
|  | Tendon | Rect Bar |  |


---
<!-- source: Menus/File/Print_Graphics.htm | Print Graphics -->

Section Designer

# Print Graphics

Use the File menu > Print Graphics command of the Print Graphics button, ![](../../Images/IMG00036.GIF), to print a graphic representation (to scale) of the current section.

The File menu > Print Graphics command prints only the graphical representation of the section. It does not print the properties of the section. To print the properties, first display the Shape Properties form by right clicking on the shape or display the Properties form by clicking the Display menu > Show Section Properties command or ![](../../Images/Show%20Section%20Properties%20button.JPG)  button. Then, perform a screen capture (see Tip) and paste the screen capture into a word processing, spreadsheet or other type of graphics-compatible file.

The File menu > Print Graphics command also does not print information for the interaction surface or the moment curvature curves. In that case, display the Interaction Surface form (click the Display menu > Show Interaction Surface command or  ![](../../Images/ebx_-466038497.gif) button) or the Moment Curvature Curve form  (click the Display menu > Show Moment-Curvature Curve command or ![](../../Images/ebx_-1202079413.gif)  button). Then perform a screen capture as described below.

TIP:  Windows built-in screen capture feature is an alternative method of generating graphical output.  
  
1.  Press the Print Screen key on the keyboard to copy the entire screen as a picture to the clipboard, including the title bars and toolbar. Pressing the Alt key and the Print Screen key simultaneously will copy only the active window to the clipboard.  
  
2.  Use Window's  Ctrl V feature to paste the picture into another Windows  program, such as Word, Excel, PowerPoint or Access.


---
<!-- source: Menus/File/Print_Setup.htm | Print Setup -->

Section Designer

# Print Setup

Use the File menu > Print Setup command to access the Print Setup form. Use the form to specify the page setup for the print. Any changes made apply to the current session of Section Designer only.

- Lines Per Page
- - No Page Ejects check box. Check this check box when continuous feed paper, such as sheets from a plotter, are being used in the output device.
  - Default option. With this option, the program default of 56 lines per page is used (generally fits 8.5-x-11-inch paper).
  - User Defined option. With this option, the edit box associated with this option becomes available. Type the required lines per page in this edit box.
- Titles. Use the Project Name and Data edit boxes to note project-related information.
- Color Printer (Graphics) check box. Check this check box if the print is to be made using a printer capable of printing in color. Use the Options menu > Colors command to control the colors used to display the various components of the section.
- Setup button. Click the Setup button to display the Print Setup form for the printer to be used for printing the file. That form is the standard form for the selected printing device and the options available depend on the printing device.

After specifying the page setup, use the File menu > Print Graphics commands to send the print to the printing device.


---
<!-- source: Menus/Options/Options.htm | Colors -->

Section Designer

# Colors

Use the Options menu > Colors command to display the Assign Display Colors form. Use the form to specify the display colors for the components of the cross section, both for on-screen display and for output to a printer.

Note:  The fill color for geometric shapes (I-sections, rectangles, etc.,) is set using the Shape Properties form and is not controlled in any way by the options chosen on this form.

- Click to Change Colors area. Left click on any of the colors shown for the following to display the Color form. Choose the revised color and click the OK button to change the display color for the associated item.
- - Reinforcing:  Controls the color of the rebar in reinforcing shapes and geometric shapes.
  - XY Axes:  Controls the color of the Section Designer X and Y axes.
  - Guide Lines:  Controls the color of the guidelines. Use the View menu > Show Guide Lines command  to toggle  guidelines on and off.
  - Local Axes:  Controls the color of the section local 2 and 3 axes.
  - Reference Lines:  Controls the color of reference lines and circles. It also controls the color of the line associated with line pattern reinforcing shapes and the color of the bounding line associated with rectangular and circular reinforcing shapes.
  - Background:  Controls the background color of the Section Designer window. The outline of geometric shapes (I-sections, rectangles, etc.,) is always displayed in a contrasting color relative to the background color (e.g., if the background is black, the outline is white; if the background is yellow, the outline is black).   
      
    This item does not control the background color of the display windows for the interaction surface and the moment curvature curve. Those background colors can not be changed.
- Device Type: Use this option to indicate if  the colors being specified are for screen display, output to a non-color printer or output to a color printer. Note that different display colors can be specified for each of the three device types.
- Reset Defaults button: Resets the colors to the default colors. The Reset Defaults button resets the colors for all three device types, regardless of which one is currently chosen.

See also:

[Preferences](Preferences.md)


---
<!-- source: Menus/Options/Preferences.htm | Preferences -->

Section Designer

# Preferences

Use the Options menu > Preference command to display the Preferences form. Use the form to control the spacing, grid sizes, tolerances, line thicknesses, pan margins and zoom step sizes.

- Background Guideline Spacing: Controls the spacing of the background guidelines in length units.

- Fine Grids between Guidelines: Controls the number of equally spaced invisible grid lines between guidelines. As an example, specifying 3 means that there is a fine grid line at the one-quarter point, half-point and three-quarter point between guidelines.

- Nudge Value: Controls the distance that a [nudged shape](../Edit/Nudge_Feature.md) moves. This item is entered in length units.

- Screen Selection Tolerance: Specifies the minimum distances between the mouse pointer the [shape being selected](../Draw/Select_Mode.md) for the selection to be effective. This item is entered in pixels. The screen selection tolerance has no effect on selection by windowing. The Section Designer default for this item is 3 pixels.

- Screen Snap To Tolerance: Specifies the minimum distance between the mouse pointer and the snap location for the [snap operation](../Draw/Snap_to.md) to be effective.  This item is entered in pixels. The Section Designer default for this item is 12 pixels.

- Screen Line Thickness: Controls the thickness of all lines on the screen. The thickness is entered in pixels. The Section Designer default for this item is 1 pixel.

- Printer Line Thickness: Controls the thickness of lines and fonts in printed output. The thickness is entered in pixels. The Section Designer default for this item is 4 pixels.

- Pan margin: Controls the distance beyond the edge of a view that can be [panned](../View/Pan_Command.md).

- Auto zoom step: Controls the size of the step used for the View menu > Zoom In One Step command and the View menu > Zoom Out One Step command. This parameter is entered as a percentage. The magnification of all objects in a view is increased or decreased by this percentage.
- Max Mesh Size (Absolute):  Controls the maximum size of the mesh used to display [section properties](../Display/Show_Section_Properties.md).
- Max Mesh Size/Overall Dim.: Controls the size of the mesh as a relative dimension.
- Mesh Merge Tolerance:  This tolerance is shown in Section Designer for review purposes only. It cannot be changed in Section Designer. The value can be changes within SAP2000 using the Options menu.


---
<!-- source: Menus/Select/All.htm | All -->

Section Designer

# All

Use the Select menu > Select > All command to select all shapes in the active window.


---
<!-- source: Menus/Select/Clear_Selection.htm | Clear Selection -->

Section Designer

# Clear Selection

Use the Select menu > Clear Selection command or the Clear Selection button, ![](../../Images/IMG00099.GIF), to clear the selection of all currently selected shapes. It is an all or nothing command. Only a portion of a selection can not be cleared using this command.

To selectively clear a selection, left click on the selected objects one at a time or use a [Deselect command](Deselect.md).


---
<!-- source: Menus/Select/Deselect.htm | Deselect -->

Section Designer

# Deselect

The Select menu > Deselect command displays a submenu with three choices:

- Pointer/Window:  Use this command to deselect shapes by left clicking on them or windowing over them.

- Intersecting Line: Use this command to deselect shapes by drawing an intersecting line through them.

- All:  Use this command to automatically deselect all shapes in the section.


---
<!-- source: Menus/Select/Get_Previous_Selection.htm | Get Previous Selection -->

Section Designer

# Get Previous Selection

Use the Select menu > Get Previous Selection command or the Restore Previous Selection toolbar button, ![](../../Images/IMG00098.GIF), to reselect shapes that were previously selected. For example, if some shapes were selected by clicking on them so that the Draw menu > Align > Tops command could be used to align them, the Select menu > Get Previous Selection command or toolbar button can be used to reselect the shapes so that another operation could be performed on them, such as changing them to poly shapes.


---
<!-- source: Menus/Select/Select.htm | Select -->

Section Designer

# Select

The Select menu > Select command brings up a submenu with three choices. Those choices are:

- Pointer/Window: This command sets Section Designer in its default select mode where you can select shapes either by left clicking on them or windowing them. Anytime you are in select mode (not draw mode) this is the default mode of selection. Thus in most instances it is not necessary to click this command before making a selection. You can just simply make the selection by left clicking or windowing.  The primary use for this command is to switch you out of draw mode into select mode.

- Intersecting Line: This command sets Section Designer in the intersecting line select mode.

- All: This command automatically selects all shapes in the section.


---
<!-- source: Menus/Select/Selection_by_Intersecting_Line.htm | Selection by Intersecting Line -->

Section Designer

# Intersecting Line

Use the Select menu > Select > Intersecting Line command or the Set Intersecting Line Select Mode button, ![](../../Images/IMG00100.GIF) to select shapes by drawing a line through them.

1. Click the  Select menu > Select > Intersecting Line command or the Set Intersecting Line Select Mode button, ![](../../Images/IMG00100.GIF).
2. Position the mouse pointer to one side of the shapes(s)  to be selected.
3. Click the left mouse button and hold it down while dragging the mouse across the shape(s) to be selected.
4. Release the left mouse button to select the shape(s). Note the following about the intersecting line selection method:

- - A "rubberband line" appears as the mouse is dragged across the shape(s). Any shape intersected (crossed) by the rubberband line when the mouse is released is selected.
  - The Select menu > Select > Intersecting Line command or the Set Intersecting Line Select Mode button, ![](../../Images/IMG00100.GIF) must be used every time this selection method is used.


---
<!-- source: Menus/Select/Selection_by_Left_Click.htm | Selection by Left Click -->

Section Designer

# Pointer/Window

Use the Select menu > Select > Pointer/Window command enables the select mode. In that mode, left click on a shape to select it. If multiple shapes are arranged one on top of the other, hold down the Ctrl key on the keyboard as you left click on the shapes and a form will appear that lists the various shape IDs. Select the desired shape from the list to select it. The select mode is the default mode for the program.

See Also

[Selection by Windowing](Selection_by_Windowing.md)


---
<!-- source: Menus/Select/Selection_by_Windowing.htm | Selection by Windowing -->

Section Designer

# Selection by Windowing

To select by windowing you draw a window around one or more shapes to select them. To draw a window around a shape first position your mouse pointer above and to the left of the shape(s) that you want to window. Then depress and hold down the left button on your mouse. While keeping the left button depressed drag your mouse to a position below and to the right of the shape(s) that you want to select. Finally release the left mouse button. Note the following about window selection:

- As you drag your mouse a "rubberband window" appears. The rubberband window is a dashed rectangle that changes shape as you drag the mouse. One corner of the rubberband window is at the point where you first depressed the left mouse button. The diagonally opposite corner of the rubberband window is at the current mouse pointer position. Any shape that is completely inside the rubberband window when you release the left mouse button is selected.

- You do not necessarily have to start the window above and to the left of the shape(s) you are selecting. You could alternatively start the window above and to the right, below and to the left or below and to the right of the shapes(s) you want to select. In all cases you would then drag your mouse diagonally across the shapes(s) you want to select.

An entire shape must lie within the rubberband window for the shape to be selected.


---
<!-- source: Menus/View/Pan_Command.htm | Pan -->

Section Designer

# Pan Command

Use the View menu > Pan command or the Pan button, ![](../../Images/IMG00044.GIF), to move a view within the window so that items beyond the original edges of the view are displayed in the active window. The distance a view can move beyond the original edge of the view is controlled by the Pan Margin item in the [Preferences](../Options/Preferences.md).

1. Click the View menu > Pan command or the Pan button, ![](../../Images/IMG00044.GIF).
2. Left click on  the view, hold down the left mouse button and drag the mouse to pan the view.


---
<!-- source: Menus/View/Previous_Zoom.htm | Previous Zoom -->

Section Designer

# Previous Zoom

Use the View menu > Previous Zoom command or the Restore Previous Zoom button ![](../../Images/IMG00041.GIF) to return immediately to the previous zoom setting.  The command or button can not be used to go back more than one zoom setting.

The command or button has no effect in the following circumstances:

- Immediately after a window is first displayed.
- Immediately after the View menu > Restore Full View command is used.


---
<!-- source: Menus/View/Refresh_Window.htm | Refresh Window -->

Section Designer

# Refresh Window

Use the View menu > Refresh Window command or the Refresh Window button, ![](../../Images/IMG00045.GIF),  to refresh (redraw) the shape(s) shown in the active window. This command does not rescale the view in any way.

To refresh the view and rescale it to fill the window, use the View menu > Restore Full View command or toolbar button ![](../../Images/IMG00040.GIF).


---
<!-- source: Menus/View/Restore_Full_View.htm | Restore Full View -->

Section Designer

# Restore Full View

Use the  View menu > Restore Full View command or the Restore Full View button![](../../Images/IMG00040.GIF) to return to a full view of the section. The view is sized such that the entire section is visible in the Section Designer window.


---
<!-- source: Menus/View/Rubberband_Zoom.htm | Rubberband Zoom -->

Section Designer

# Rubberband Zoom

Use the View menu > Rubber Band Zoom command or the Rubber Band Zoom button ![](../../Images/IMG00039.GIF) to zoom in on the section by windowing.

1. Click the View menu > Rubber Band Zoom command or the Rubber Band Zoom button ![](../../Images/IMG00039.GIF).
2. Place the mouse pointer at the edge of the area to be windowed.
3. Click the left mouse button and hold it down. With the left button depressed, drag the mouse to draw a "rubber band" window around the area of interest. The rubber band window appears as a dashed line on the screen.
4. Release the mouse button to display the new view.


---
<!-- source: Menus/View/Show_Axes.htm | Show Axes -->

Section Designer

# Show Axes

Use the View menu > Show Axes command to toggle the display of the section local axes and the Section Designer X and Y axes on and off. Note the following about these axes.

The color of the local axes is controlled by the Local Axes item and the color of the Section Designer X and Y axes is controlled by the Text item, both on the [Assign Display Colors form](../Options/Options.md).


---
<!-- source: Menus/View/Show_Grid_Lines.htm | Show Grid Lines -->

Section Designer

# Show Grid Lines

Use the View menu > Show Grid Lines command to toggle the display of grid lines off and on in the active window.


---
<!-- source: Menus/View/Zoom_In_One_Step.htm | Zoom In One Step -->

Section Designer

# Zoom In One Step

The View menu > Zoom In One Step command  or the Zoom In One Step button ![](../../Images/IMG00042.GIF) to zoom in on the section one step. The size of the step is controlled by the Auto Zoom Step item in the [Preferences.](../Options/Preferences.md)

The default value for the Auto Zoom Step item is 10 percent. Thus,  when the View menu > Zoom In One Step command is used, the program increases the magnification of all objects in the view by 10 percent.


---
<!-- source: Menus/View/Zoom_Out_One_Step.htm | Zoom Out One Step -->

Section Designer

# Zoom Out One Step

Use the View menu > Zoom Out One Step command or the Zoom Out One Step button ![](../../Images/IMG00043.GIF) to zoom out one step on the section. The size of the step is controlled by the Auto Zoom Step item in the [Preferences](../Options/Preferences.md).

The default value for the Auto Zoom Step item is 10 percent. Thus, when the View menu > Zoom Out One Step command is used, the program decreases the magnification of all objects in the view by 10 percent.
