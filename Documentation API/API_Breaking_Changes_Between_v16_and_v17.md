# API Breaking Changes Between v16 and v17

Source: CSI OAPI Documentation (SAP2000) — SAP2000_API_Fuctions/Breaking_Changes_Between_v16_and_v17

---



## Breaking Changes

*Source file: `SAP2000_API_Fuctions/Breaking_Changes_Between_v16_and_v17/Breaking_Changes.htm`*

# Breaking Changes

The following items have changed in Version 17 and will require changes in existing source code where they are used.

|  |  |
| --- | --- |
| Version 16 | Version 17 |

|  |  |
| --- | --- |
| cEnumerations.eUnits | eunits |
| cEnumerations.eConstraintType | eConstraintType |
| cEnumerations.eDesignActionType | eDesignActionType |
| cEnumerations.eFramePropType | eFramePropType |
| cEnumerations.eLinkPropType | eLinkPropType |
| cEnumerations.eLoadCaseType | eLoadCaseType |
| cEnumerations.eLoadPatternType | eLoadPatternType |
| cEnumerations.eMatType | eMatType |
| cPointObj.eItemType | eItemType |
| cPointObj.eItemType.[Object] | eItemType.Objects |
| cAnalysisResults.eItemTypeElm | eItemTypeElm |
| eCType | eCNameType |
| SapModel.FrameObj.GetType | SapModel.FrameObj.GetTypeOAPI |
| SapModel.Func.GetType | SapModel.Func.GetTypeOAPI |
| SapModel.GDispl.GetType | SapModel.GDispl.GetTypeOAPI |
| SapModel.GDispl.SetType | SapModel.GDispl.SetTypeOAPI |
| SapModel.LoadCases.GetType | SapModel.LoadCases.GetTypeOAPI |
| SapModel.LoadCases.GetType\_1 | SapModel.LoadCases.GetTypeOAPI\_1 |
| SapModel.PropArea.GetType | SapModel.PropArea.GetTypeOAPI |
| SapModel.PropFrame.GetType | SapModel.PropFrame.GetTypeOAPI |
| SapModel.PropLink.GetType | SapModel.PropLink.GetTypeOAPI |
| SapModel.PropMaterial.GetType | SapModel.PropMaterial.GetTypeOAPI |
| SapModel.RespCombo.GetType | SapModel.RespCombo.GetTypeOAPI |
| SapModel.RespCombo.SetType | SapModel.RespCombo.SetTypeOAPI |



## Breaking Changes to COM Enumerations

*Source file: `SAP2000_API_Fuctions/Breaking_Changes_Between_v16_and_v17/Breaking_Changes_to_COM_Enumerations.htm`*

# Breaking Changes to COM Enumerations

•  e2DFrameType

◦            ConcentricBraced => e2DFrameType\_ConcentricBraced

◦            EccentricBraced  => e2DFrameType\_ EccentricBraced

◦            PortalFrame => e2DFrameType\_ PortalFrame

•  e3DFrameType

◦            Beamslab => e3DFrameType\_Beamslab

◦            FIatPIate => e3DFrameType\_FIatPIate

◦            OpenFrame => e3DFrameType\_OpenFrame

◦            PerimeterFrame => e3DFrameType\_PerimeterFrame

•  eConstraintAxis

◦            AutoAxis => eConstraintAxis\_AutoAxis

◦            x => eConstraintAxis\_X

◦            y => eConstraintAxis\_Y

◦            z => eConstraintAxis\_Z

•  eConstraintType

◦            CONSTRAINT\_BEAM     => eConstraintType\_Beam

◦            CONSTRAINT\_BODY     => eConstraintType\_Body

◦            CONSTRAINT\_DIAPHRAGM => eConstraintType\_Diaphragm

◦            CONSTRAINT\_EQUAL    => eConstraintType\_Equal

◦            CONSTRAINT\_LINE     => eConstraintType\_Line

◦            CONSTRAINT\_LOCAL    => eConstraintType\_Local

◦            CONSTRAINT\_PLATE    => eConstraintType\_Plate

◦            CONSTRAINT\_ROD      => eConstraintType\_Rod

◦            CONSTRAINT\_WELD     => eConstraintType\_Weld

•  eCType => eCNameType

◦            LoadCase => eCNameType\_LoadCase

◦            LoadCombo =>eCNameType\_LoadCombo

•  eDesignActionType

◦            DESIGNACTION\_LONG\_TERM\_COMPOSITE => eDesignActionType\_LongTermComposite

◦            DESIGNACTION\_NON\_COMPOSITE => eDesignActionType\_NonComposite

◦            DESIGNACTION\_OTHER => eDesignActionType\_Other

◦            DESIGNACTION\_SHORT\_TERM\_COMPOSITE => eDesignActionType\_ShortTermComposite

◦            DESIGNACTION\_STAGED => eDesignActionType\_Staged

•  eFramePropType

◦            SECTION\_ANGLE => eFramePropType\_Angle

◦            SECTION\_AUTO => eFramePropType\_Auto

◦            SECTION\_BOX => eFramePropType\_Box

◦            SECTION\_BRIDGE => eFramePropType\_Bridge

◦            SECTION\_BUILTUP\_I\_COVERPIATE => eFramePropType\_BuiltupICoverpIate

◦            SECTION\_BUILTUP\_I\_HYBRID => eFramePropType\_BuiltupIHybrid

◦            SECTION\_BUILTUP\_U\_HYBRID => eFramePropType\_BuiltupUHybrid

◦            SECTION\_CHANNEL => eFramePropType\_Channel

◦            SECTION\_CIRCLE => eFramePropType\_Circle

◦            SECTION\_COLD\_2C => eFramePropType\_Cold\_2C

◦            SECTION\_COLD\_2L => eFramePropType\_Cold\_2L

◦            SECTION\_COLD\_C => eFramePropType\_Cold\_C

◦            SECTION\_COLD\_HAT => eFramePropType\_Cold\_Hat

◦            SECTION\_COLD\_L => eFramePropType\_Cold\_L

◦            SECTION\_COLD\_Z => eFramePropType\_Cold\_Z

◦            SECTION\_DBCHANNEL => eFramePropType\_DbChannel

◦            SECTION\_DBLANGLE => eFramePropType\_DblAngle

◦            SECTION\_GENERAL => eFramePropType\_General

◦            SECTION\_I => eFramePropType\_I

◦            SECTION\_JOIST => eFramePropType\_Joist

◦            SECTION\_PCC\_GIRDER\_I => eFramePropType\_PCCGirderI

◦            SECTION\_PCC\_Girder\_U => eFramePropType\_PCCGirderU

◦            SECTION\_PIPE => eFramePropType\_Pipe

◦            SECTION\_RECTANGULAR => eFramePropType\_Rectangular

◦            SECTION\_SD => eFramePropType\_SD

◦            SECTION\_T => eFramePropType\_T

◦            SECTION\_VARIABLE => eFramePropType\_Variable

•  eItemType

◦            Group => eItemType\_Group

◦            Object => eItemType\_Objects

◦            SelectedObjects => eItemType\_SelectedObjects

•  eItemTypeElm

◦            Element => eItemTypeElm\_Element

◦            GroupElm => eItemTypeElm\_GroupElm

◦            ObjectElm => eItemTypeElm\_ObjectElm

◦            SelectionElm => eItemTypeElm\_SelectionElm

•  eLinkPropType

◦            NLPROP\_DAMPER => eLinkPropType\_Damper

◦            NLPROP\_GAP => eLinkPropType\_Gap

◦            NLPROP\_HOOK => eLinkPropType\_Hook

◦            NLPROP\_ISOLATOR1 => eLinkPropType\_Isolator1

◦            NLPROP\_ISOLATOR2 => eLinkPropType\_Isolator2

◦            NLPROP\_ISOLATOR3 => eLinkPropType\_Isolator3

◦            NLPROP\_LINEAR => eLinkPropType\_Linear

◦            NLPROP\_MULTILINEAR\_ELASTIC => eLinkPropType\_MultilinearElastic

◦            NLPROP\_MULTILINEAR\_PLASTIC => eLinkPropType\_MultilinearPlastic

◦            NLPROP\_PLASTIC\_WEN => eLinkPropType\_PlasticWen

◦            NLPROP\_ISOLATOR4 => eLinkPropType\_Isolator4

◦            NLPROP\_DAMPER\_LINEAR\_EXPONENTIAL => eLinkPropType\_DamperLinearExponential

◦            NLPROP\_DAMPER\_BILINEAR => eLinkPropType\_DamperBilinear

◦            NLPROP\_DAMPER\_FRICTION\_SPRING => eLinkPropType\_DamperFrictionSpring

•  eLoadCaseType

◦            CASE\_BUCKLING => eLoadCaseType\_Buckling

◦            CASE\_HYPERSTATIC => eLoadCaseType\_HyperStatic

◦            CASE\_LINEAR\_DYNAMIC => eLoadCaseType\_LinearDynamic

◦            CASE\_LINEAR\_HISTORY => eLoadCaseType\_LinearHistory

◦            CASE\_LINEAR\_STATIC => eLoadCaseType\_LinearStatic

◦            CASE\_LINEAR\_STATIC\_MULTISTEP => eLoadCaseType\_LinearStaticMultiStep

◦            CASE\_MODAL => eLoadCaseType\_Modal

◦            CASE\_MOVING\_LOAD => eLoadCaseType\_MovingLoad

◦            CASE\_NONLINEAR\_DYNAMIC => eLoadCaseType\_NonlinearDynamic

◦            CASE\_NONLINEAR\_HISTORY => eLoadCaseType\_NonlinearHistory

◦            CASE\_NONLINEAR\_STATIC => eLoadCaseType\_NonlinearStatic

◦            CASE\_POWER\_SPECTRAL\_DENSITY => eLoadCaseType\_PowerSpectralDensity

◦            CASE\_RESPONSE\_SPECTRUM => eLoadCaseType\_ResponseSpectrum

◦            CASE\_STEADY\_STATE => eLoadCaseType\_SteadyState

◦            CASE\_EXTERNAL\_RESULTS => eLoadCaseType\_ExternalResults

•  eLoadPatternType

◦            LTYPE\_ACTIVEEARTHPRESSURE => eLoadPatternType\_ActiveEarthPressure

◦            LTYPE\_BOUYANCY => eLoadPatternType\_Bouyancy

◦            LTYPE\_BRAKING => eLoadPatternType\_Braking

◦            LTYPE\_CENTRIFUGAL => eLoadPatternType\_Centrifugal

◦            LTYPE\_CONSTRUCTION => eLoadPatternType\_Construction

◦            LTYPE\_CREEP => eLoadPatternType\_Creep

◦            LTYPE\_DEAD => eLoadPatternType\_Dead

◦            LTYPE\_DEADMANUFACTURE => eLoadPatternType\_DeadManufacture

◦            LTYPE\_DEADWATER => eLoadPatternType\_DeadWater

◦            LTYPE\_DEADWEARING => eLoadPatternType\_DeadWearing

◦            LTYPE\_DOWNDRAG => eLoadPatternType\_DownDrag

◦            LTYPE\_EARTHHYDROSTATIC => eLoadPatternType\_EarthHydrostatic

◦            LTYPE\_EARTHSURCHARGE => eLoadPatternType\_EarthSurcharge

◦            LTYPE\_EURO\_LM1\_Char => eLoadPatternType\_EuroLm1Char

◦            LTYPE\_EURO\_LM1\_Freq => eLoadPatternType\_EuroLm1Freq

◦            LTYPE\_EURO\_LM2 => eLoadPatternType\_EuroLm2

◦            LTYPE\_EURO\_LM3 => eLoadPatternType\_EuroLm3

◦            LTYPE\_EURO\_LM4 => eLoadPatternType\_EuroLm4

◦            LTYPE\_FRICTION => eLoadPatternType\_Friction

◦            LTYPE\_HORIZONTALEARTHPRESSURE => eLoadPatternType\_HorizontalEarthPressure

◦            LTYPE\_HYPERSTATIC => eLoadPatternType\_Hyperstatic

◦            LTYPE\_ICE => eLoadPatternType\_Ice

◦            LTYPE\_IMPACT => eLoadPatternType\_Impact

◦            LTYPE\_LIVE => eLoadPatternType\_Live

◦            LTYPE\_LIVELOADSURCHARGE => eLoadPatternType\_LiveLoadSurcharge

◦            LTYPE\_LOCKEDINFORCES => eLoadPatternType\_LockedInForces

◦            LTYPE\_MOVE => eLoadPatternType\_Move

◦            LTYPE\_MOVE\_FATIGUE => eLoadPatternType\_MoveFatigue

◦            LTYPE\_MOVE\_FATIGUE\_PERMIT => eLoadPatternType\_MoveFatiguePermit

◦            LTYPE\_MOVE\_PERMIT => eLoadPatternType\_Permit

◦            LTYPE\_NOTIONAL => eLoadPatternType\_Notional

◦            LTYPE\_OTHER => eLoadPatternType\_Other

◦            LTYPE\_PASSIVEEARTHPRESSURE => eLoadPatternType\_PassiveEarthPressure

◦            LTYPE\_PATTERNLIVE => eLoadPatternType\_PatternLive

◦            LTYPE\_PEDESTRIANLL => eLoadPatternType\_PedestrianLL

◦            LTYPE\_PEDESTRIANLLREDUCED => eLoadPatternType\_PedestrianLLReduced

◦            LTYPE\_PRESTRESS => eLoadPatternType\_Prestress

◦            LTYPE\_QUAKE => eLoadPatternType\_Quake

◦            LTYPE\_REDUCELIVE => eLoadPatternType\_ReduceLive

◦            LTYPE\_ROOFLIVE => eLoadPatternType\_Roofive

◦            LTYPE\_SEASTATE  => eLoadPatternType\_SeaState

◦            LTYPE\_SETTLEMENT => eLoadPatternType\_Settlement

◦            LTYPE\_SHRINKAGE => eLoadPatternType\_Shrinkage

◦            LTYPE\_SNOW => eLoadPatternType\_Snow

◦            LTYPE\_SNOWHIGHALTITUDE => eLoadPatternType\_SnowHighAltitude

◦            LTYPE\_STREAMFLOW => eLoadPatternType\_StreamFlow

◦            LTYPE\_SUPERDEAD => eLoadPatternType\_SuperDead

◦            LTYPE\_TEMPERATURE => eLoadPatternType\_Temperature

◦            LTYPE\_TEMPERATUREGRADIENT => eLoadPatternType\_TemperatureGradient

◦            LTYPE\_VEHICLECOLLISION => eLoadPatternType\_VehicleCollision

◦            LTYPE\_VERTICALEARTHPRESSURE => eLoadPatternType\_VerticalEarthPressure

◦            LTYPE\_VESSELCOLLISION => eLoadPatternType\_VesselCollision

◦            LTYPE\_WATERLOADPRESSURE => eLoadPatternType\_WaterloadPressure

◦            LTYPE\_WAVE => eLoadPatternType\_Wave

◦            LTYPE\_WIND => eLoadPatternType\_Wind

◦            LTYPE\_WINDONLIVELOAD => eLoadPatternType\_WindOnLiveLoad

•  eMatType

◦            MATERIAL\_ALUMINUM => eMatType\_Aluminum

◦            MATERIAL\_COLDFORMED => eMatType\_ColdFormed

◦            MATERIAL\_CONCRETE => eMatType\_Concrete

◦            MATERIAL\_MASONRY => eMatType\_Masonry

◦            MATERIAL\_NODESIGN => eMatType\_NoDesign

◦            MATERIAL\_REBAR => eMatType\_Rebar

◦            MATERIAL\_STEEL => eMatType\_Steel

◦            MATERIAL\_TENDON => eMatType\_Tendon

•  eMatTypeAluminum

◦            MATERIAL\_ALUMINUM\_SUBTYPE\_5052\_H34 => eMatTypeAluminum\_SubType\_5052\_H34

◦            MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6 => eMatTypeAluminum\_SubType\_6061\_T6

◦            MATERIAL\_ALUMINUM\_SUBTYPE\_6063\_T6 => eMatTypeAluminum\_SubType\_6063\_T6

•  eMatTypeColdFormed

◦            MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGR33 => eMatTypeColdFormed\_ASTM\_A653SQGr33

◦            MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGR50 => eMatTypeColdFormed\_ASTM\_A653SQGr50

•  eMatTypeConcrete

◦            MATERIAL\_CONCRETE\_SUBTYPE\_CHINESE\_C20\_NORMALWEIGHT => eMatTypeConcrete\_Chinese\_C20\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_CHINESE\_C30\_NORMALWEIGHT => eMatTypeConcrete\_Chinese\_C30\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_CHINESE\_C40\_NORMALWEIGHT => eMatTypeConcrete\_Chinese\_C40\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C12\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C12\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C16\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C16\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C20\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C20\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C25\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C25\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C30\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C30\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C35\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C35\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C40\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C40\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C45\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C45\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C50\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C50\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C55\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C55\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C60\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C60\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C70\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C70\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C80\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C80\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C90\_NORMALWEIGHT => eMatTypeConcrete\_EN\_C90\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC3000\_LIGHTWEIGHT => eMatTypeConcrete\_FC3000\_LightWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC3000\_NORMALWEIGHT => eMatTypeConcrete\_FC3000\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC4000\_LIGHTWEIGHT => eMatTypeConcrete\_FC4000\_LightWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC4000\_NORMALWEIGHT => eMatTypeConcrete\_FC4000\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC5000\_LIGHTWEIGHT => eMatTypeConcrete\_FC5000\_LightWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC5000\_NORMALWEIGHT => eMatTypeConcrete\_FC5000\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC6000\_LIGHTWEIGHT => eMatTypeConcrete\_FC6000\_LightWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC6000\_NORMALWEIGHT => eMatTypeConcrete\_FC6000\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M15\_NORMALWEIGHT => eMatTypeConcrete\_Indian\_M15\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M20\_NORMALWEIGHT => eMatTypeConcrete\_Indian\_M20\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M25\_NORMALWEIGHT => eMatTypeConcrete\_Indian\_M25\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M30\_NORMALWEIGHT => eMatTypeConcrete\_Indian\_M30\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M35\_NORMALWEIGHT => eMatTypeConcrete\_Indian\_M35\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M40\_NORMALWEIGHT => eMatTypeConcrete\_Indian\_M40\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M45\_NORMALWEIGHT => eMatTypeConcrete\_Indian\_M45\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M50\_NORMALWEIGHT => eMatTypeConcrete\_Indian\_M50\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M55\_NORMALWEIGHT => eMatTypeConcrete\_Indian\_M55\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M60\_NORMALWEIGHT => eMatTypeConcrete\_Indian\_M60\_NormalWeight

•  eMatTypeRebar

◦            MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr40 => eMatTypeRebar\_ASTM\_A615Gr40

◦            MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr60 => eMatTypeRebar\_ASTM\_A615Gr60

◦            MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr75 => eMatTypeRebar\_ASTM\_A615Gr75

◦            MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A706 => eMatTypeRebar\_ASTM\_A706

◦            MATERIAL\_REBAR\_SUBTYPE\_CHINESE\_HPB235 => eMatTypeRebar\_Chinese\_HPB235

◦            MATERIAL\_REBAR\_SUBTYPE\_CHINESE\_HRB335 => eMatTypeRebar\_Chinese\_HRB335

◦            MATERIAL\_REBAR\_SUBTYPE\_CHINESE\_HRB400 => eMatTypeRebar\_Chinese\_HRB400

◦            MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_HYSD415 => eMatTypeRebar\_Indian\_HYSD415

◦            MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_HYSD500 => eMatTypeRebar\_Indian\_HYSD500

◦            MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_HYSD550 => eMatTypeRebar\_Indian\_HYSD550

◦            MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_Mild250 => eMatTypeRebar\_Indian\_Mild250

•  eMatTypeSteel

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A36 => eMatTypeSteel\_ASTM\_A36

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A500GrB\_Fy42 => eMatTypeSteel\_ASTM\_A500GrB\_Fy42

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A500GrB\_Fy46 => eMatTypeSteel\_ASTM\_A500GrB\_Fy46

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A53GrB => eMatTypeSteel\_ASTM\_A53GrB

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A572Gr50 => eMatTypeSteel\_ASTM\_A572Gr50

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A913Gr50 => eMatTypeSteel\_ASTM\_A913Gr50

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A992\_Fy50 => eMatTypeSteel\_ASTM\_A992\_Fy50

◦            MATERIAL\_STEEL\_SUBTYPE\_CHINESE\_Q235 => eMatTypeSteel\_Chinese\_Q235

◦            MATERIAL\_STEEL\_SUBTYPE\_CHINESE\_Q345 => eMatTypeSteel\_Chinese\_Q345

◦            MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S235 => eMatTypeSteel\_EN100252\_S235

◦            MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S275 => eMatTypeSteel\_EN100252\_S275

◦            MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S355 => eMatTypeSteel\_EN100252\_S355

◦            MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S450 => eMatTypeSteel\_EN100252\_S450

◦            MATERIAL\_STEEL\_SUBTYPE\_INDIAN\_Fe250 => eMatTypeSteel\_Indian\_Fe250

◦            MATERIAL\_STEEL\_SUBTYPE\_INDIAN\_Fe345 => eMatTypeSteel\_Indian\_Fe345

•  eMatTypeTendon

◦            MATERIAL\_TENDON\_SUBTYPE\_ASTM\_A416Gr250 => eMatTypeTendon\_ASTM\_A416Gr250

◦            MATERIAL\_TENDON\_SUBTYPE\_ASTM\_A416Gr270 => eMatTypeTendon\_ASTM\_A416Gr270

•  eTemplateType

◦            T\_Advanced => eTemplateType\_Advanced

◦            T\_Barrel => eTemplateType\_Barrel

◦            T\_Beam => eTemplateType\_Beam

◦            T\_BracedFrame => eTemplateType\_BracedFrame

◦            T\_Bridge => eTemplateType\_Bridge

◦            T\_BridgeWizard => eTemplateType\_BridgeWizard

◦            T\_CableBridges => eTemplateType\_CableBridges

◦            T\_Clear => eTemplateType\_Clear

◦            T\_Cylinder => eTemplateType\_Cylinder

◦            T\_Dome => eTemplateType\_Dome

◦            T\_EccentricFrame => eTemplateType\_EccentricFrame

◦            T\_Floor => eTemplateType\_Floor

◦            T\_2DFrames => eTemplateType\_Frame2D

◦            T\_3DFrames => eTemplateType\_Frame3D

◦            T\_Grid => eTemplateType\_Grid

◦            T\_PerimeterFrame => eTemplateType\_PerimeterFrame

◦            T\_PipesAndPlates => eTemplateType\_PipesAndPlates

◦            T\_PortalFrame => eTemplateType\_PortalFrame

◦            T\_ShearWall => eTemplateType\_ShearWall

◦            T\_Shells => eTemplateType\_Shells

◦            T\_SlopedTruss => eTemplateType\_SlopedTruss

◦            T\_SolidModels => eTemplateType\_SolidModels

◦            T\_SpaceFrame => eTemplateType\_SpaceFrame

◦            T\_SpaceTruss => eTemplateType\_SpaceTruss

◦            T\_Staircases => eTemplateType\_Staircases

◦            T\_StorageStructures => eTemplateType\_StorageStructures

◦            T\_2DTrusses=> eTemplateType\_Truss2D

◦            T\_3DTrusses => eTemplateType\_Truss3D

◦            T\_UndergoundConcrete => eTemplateType\_UndergoundConcrete

◦            T\_VerticalTruss => eTemplateType\_VerticalTruss

•  eUnits

◦            kgf\_cm\_C => eUnits\_kgf\_cm\_C

◦            kgf\_m\_C => eUnits\_kgf\_m\_C

◦            kgf\_mm\_C => eUnits\_kgf\_mm\_C

◦            kip\_ft\_F => eUnits\_kip\_ft\_F

◦            kip\_in\_F => eUnits\_kip\_in\_F

◦            kN\_cm\_C => eUnits\_kN\_cm\_C

◦            kN\_m\_C => eUnits\_kN\_m\_C

◦            kN\_mm\_C => eUnits\_kN\_mm\_C

◦            lb\_ft\_F => eUnits\_lb\_ft\_F

◦            lb\_in\_F => eUnits\_lb\_in\_F

◦            N\_cm\_C => eUnits\_N\_cm\_C

◦            N\_m\_C => eUnits\_N\_m\_C

◦            N\_mm\_C => eUnits\_N\_mm\_C

◦            Ton\_cm\_C => eUnits\_Ton\_cm\_C

◦            Ton\_m\_C => eUnits\_Ton\_m\_C

◦            Ton\_mm\_C => eUnits\_Ton\_mm\_C



## Breaking Changes to NET Enumerations

*Source file: `SAP2000_API_Fuctions/Breaking_Changes_Between_v16_and_v17/Breaking_Changes_to_NET_Enumerations.htm`*

# Breaking Changes to NET Enumerations

•  eConstraintAxis

◦            x => X

◦            y => Y

◦            z => Z

•  eConstraintType

◦            CONSTRAINT\_BEAM     => Beam

◦            CONSTRAINT\_BODY     => Body

◦            CONSTRAINT\_DIAPHRAGM => Diaphragm

◦            CONSTRAINT\_EQUAL    => Equal

◦            CONSTRAINT\_LINE     => Line

◦            CONSTRAINT\_LOCAL    => Local

◦            CONSTRAINT\_PLATE    => Plate

◦            CONSTRAINT\_ROD      => Rod

◦            CONSTRAINT\_WELD     => Weld

•  eCType => eCNameType

•  eDesignActionType

◦            DESIGNACTION\_LONG\_TERM\_COMPOSITE => LongTermComposite

◦            DESIGNACTION\_NON\_COMPOSITE => NonComposite

◦            DESIGNACTION\_OTHER => Other

◦            DESIGNACTION\_SHORT\_TERM\_COMPOSITE => ShortTermComposite

◦            DESIGNACTION\_STAGED => Staged

•  eFramePropType

◦            SECTION\_ANGLE => Angle

◦            SECTION\_AUTO => Auto

◦            SECTION\_BOX => Box

◦            SECTION\_BRIDGE => Bridge

◦            SECTION\_BUILTUP\_I\_COVERPIATE => BuiltupICoverpIate

◦            SECTION\_BUILTUP\_I\_HYBRID => BuiltupIHybrid

◦            SECTION\_BUILTUP\_U\_HYBRID => BuiltupUHybrid

◦            SECTION\_CHANNEL => Channel

◦            SECTION\_CIRCLE => Circle

◦            SECTION\_COLD\_2C => Cold\_2C

◦            SECTION\_COLD\_2L => Cold\_2L

◦            SECTION\_COLD\_C => Cold\_C

◦            SECTION\_COLD\_HAT => Cold\_Hat

◦            SECTION\_COLD\_L => Cold\_L

◦            SECTION\_COLD\_Z => Cold\_Z

◦            SECTION\_DBCHANNEL => DbChannel

◦            SECTION\_DBLANGLE => DblAngle

◦            SECTION\_GENERAL => General

◦            SECTION\_I => I

◦            SECTION\_JOIST => Joist

◦            SECTION\_PCC\_GIRDER\_I => PCCGirderI

◦            SECTION\_PCC\_Girder\_U => PCCGirderU

◦            SECTION\_PIPE => Pipe

◦            SECTION\_RECTANGULAR => Rectangular

◦            SECTION\_SD => SD

◦            SECTION\_T => T

◦            SECTION\_VARIABLE => Variable

•  eItemType

◦            Object => Objects

•  eLinkPropType

◦            NLPROP\_DAMPER => Damper

◦            NLPROP\_GAP => Gap

◦            NLPROP\_HOOK => Hook

◦            NLPROP\_ISOLATOR1 => Isolator1

◦            NLPROP\_ISOLATOR2 => Isolator2

◦            NLPROP\_ISOLATOR3 => Isolator3

◦            NLPROP\_LINEAR => Linear

◦            NLPROP\_MULTILINEAR\_ELASTIC => MultilinearElastic

◦            NLPROP\_MULTILINEAR\_PLASTIC => MultilinearPlastic

◦            NLPROP\_PLASTIC\_WEN => PlasticWen

◦            NLPROP\_ISOLATOR4 => Isolator4

◦            NLPROP\_DAMPER\_LINEAR\_EXPONENTIAL => DamperLinearExponential

◦            NLPROP\_DAMPER\_BILINEAR => DamperBilinear

◦            NLPROP\_DAMPER\_FRICTION\_SPRING => DamperFrictionSpring

•  eLoadCaseType

◦            CASE\_BUCKLING => Buckling

◦            CASE\_HYPERSTATIC => HyperStatic

◦            CASE\_LINEAR\_DYNAMIC => LinearDynamic

◦            CASE\_LINEAR\_HISTORY => LinearHistory

◦            CASE\_LINEAR\_STATIC => LinearStatic

◦            CASE\_LINEAR\_STATIC\_MULTISTEP => LinearStaticMultiStep

◦            CASE\_MODAL => Modal

◦            CASE\_MOVING\_LOAD => MovingLoad

◦            CASE\_NONLINEAR\_DYNAMIC => NonlinearDynamic

◦            CASE\_NONLINEAR\_HISTORY => NonlinearHistory

◦            CASE\_NONLINEAR\_STATIC => NonlinearStatic

◦            CASE\_POWER\_SPECTRAL\_DENSITY => PowerSpectralDensity

◦            CASE\_RESPONSE\_SPECTRUM => ResponseSpectrum

◦            CASE\_STEADY\_STATE => SteadyState

◦            CASE\_EXTERNAL\_RESULTS => ExternalResults

•  eLoadPatternType

◦            LTYPE\_ACTIVEEARTHPRESSURE => ActiveEarthPressure

◦            LTYPE\_BOUYANCY => Bouyancy

◦            LTYPE\_BRAKING => Braking

◦            LTYPE\_CENTRIFUGAL => Centrifugal

◦            LTYPE\_CONSTRUCTION => Construction

◦            LTYPE\_CREEP => Creep

◦            LTYPE\_DEAD => Dead

◦            LTYPE\_DEADMANUFACTURE => DeadManufacture

◦            LTYPE\_DEADWATER => DeadWater

◦            LTYPE\_DEADWEARING => DeadWearing

◦            LTYPE\_DOWNDRAG => DownDrag

◦            LTYPE\_EARTHHYDROSTATIC => EarthHydrostatic

◦            LTYPE\_EARTHSURCHARGE => EarthSurcharge

◦            LTYPE\_EURO\_LM1\_Char => EuroLm1Char

◦            LTYPE\_EURO\_LM1\_Freq => EuroLm1Freq

◦            LTYPE\_EURO\_LM2 => EuroLm2

◦            LTYPE\_EURO\_LM3 => EuroLm3

◦            LTYPE\_EURO\_LM4 => EuroLm4

◦            LTYPE\_FRICTION => Friction

◦            LTYPE\_HORIZONTALEARTHPRESSURE => HorizontalEarthPressure

◦            LTYPE\_HYPERSTATIC => Hyperstatic

◦            LTYPE\_ICE => Ice

◦            LTYPE\_IMPACT => Impact

◦            LTYPE\_LIVE => Live

◦            LTYPE\_LIVELOADSURCHARGE => LiveLoadSurcharge

◦            LTYPE\_LOCKEDINFORCES => LockedInForces

◦            LTYPE\_MOVE => Move

◦            LTYPE\_MOVE\_FATIGUE => MoveFatigue

◦            LTYPE\_MOVE\_FATIGUE\_PERMIT => MoveFatiguePermit

◦            LTYPE\_MOVE\_PERMIT => Permit

◦            LTYPE\_NOTIONAL => Notional

◦            LTYPE\_OTHER => Other

◦            LTYPE\_PASSIVEEARTHPRESSURE => PassiveEarthPressure

◦            LTYPE\_PATTERNLIVE => PatternLive

◦            LTYPE\_PEDESTRIANLL => PedestrianLL

◦            LTYPE\_PEDESTRIANLLREDUCED => PedestrianLLReduced

◦            LTYPE\_PRESTRESS => Prestress

◦            LTYPE\_QUAKE => Quake

◦            LTYPE\_REDUCELIVE => ReduceLive

◦            LTYPE\_ROOFLIVE => Roofive

◦            LTYPE\_SEASTATE  => SeaState

◦            LTYPE\_SETTLEMENT => Settlement

◦            LTYPE\_SHRINKAGE => Shrinkage

◦            LTYPE\_SNOW => Snow

◦            LTYPE\_SNOWHIGHALTITUDE => SnowHighAltitude

◦            LTYPE\_STREAMFLOW => StreamFlow

◦            LTYPE\_SUPERDEAD => SuperDead

◦            LTYPE\_TEMPERATURE => Temperature

◦            LTYPE\_TEMPERATUREGRADIENT => TemperatureGradient

◦            LTYPE\_VEHICLECOLLISION => VehicleCollision

◦            LTYPE\_VERTICALEARTHPRESSURE => VerticalEarthPressure

◦            LTYPE\_VESSELCOLLISION => VesselCollision

◦            LTYPE\_WATERLOADPRESSURE => WaterloadPressure

◦            LTYPE\_WAVE => Wave

◦            LTYPE\_WIND => Wind

◦            LTYPE\_WINDONLIVELOAD => WindOnLiveLoad

•  eMatType

◦            MATERIAL\_ALUMINUM => Aluminum

◦            MATERIAL\_COLDFORMED => ColdFormed

◦            MATERIAL\_CONCRETE => Concrete

◦            MATERIAL\_MASONRY => Masonry

◦            MATERIAL\_NODESIGN => NoDesign

◦            MATERIAL\_REBAR => Rebar

◦            MATERIAL\_STEEL => Steel

◦            MATERIAL\_TENDON => Tendon

•  eMatTypeAluminum

◦            MATERIAL\_ALUMINUM\_SUBTYPE\_5052\_H34 => SubType\_5052\_H34

◦            MATERIAL\_ALUMINUM\_SUBTYPE\_6061\_T6 => SubType\_6061\_T6

◦            MATERIAL\_ALUMINUM\_SUBTYPE\_6063\_T6 => SubType\_6063\_T6

•  eMatTypeColdFormed

◦            MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGR33 => ASTM\_A653SQGr33

◦            MATERIAL\_COLDFORMED\_SUBTYPE\_ASTM\_A653SQGR50 => ASTM\_A653SQGr50

•  eMatTypeConcrete

◦            MATERIAL\_CONCRETE\_SUBTYPE\_CHINESE\_C20\_NORMALWEIGHT => Chinese\_C20\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_CHINESE\_C30\_NORMALWEIGHT => Chinese\_C30\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_CHINESE\_C40\_NORMALWEIGHT => Chinese\_C40\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C12\_NORMALWEIGHT => EN\_C12\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C16\_NORMALWEIGHT => EN\_C16\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C20\_NORMALWEIGHT => EN\_C20\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C25\_NORMALWEIGHT => EN\_C25\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C30\_NORMALWEIGHT => EN\_C30\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C35\_NORMALWEIGHT => EN\_C35\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C40\_NORMALWEIGHT => EN\_C40\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C45\_NORMALWEIGHT => EN\_C45\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C50\_NORMALWEIGHT => EN\_C50\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C55\_NORMALWEIGHT => EN\_C55\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C60\_NORMALWEIGHT => EN\_C60\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C70\_NORMALWEIGHT => EN\_C70\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C80\_NORMALWEIGHT => EN\_C80\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_EN\_C90\_NORMALWEIGHT => EN\_C90\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC3000\_LIGHTWEIGHT => FC3000\_LightWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC3000\_NORMALWEIGHT => FC3000\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC4000\_LIGHTWEIGHT => FC4000\_LightWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC4000\_NORMALWEIGHT => FC4000\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC5000\_LIGHTWEIGHT => FC5000\_LightWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC5000\_NORMALWEIGHT => FC5000\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC6000\_LIGHTWEIGHT => FC6000\_LightWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_FC6000\_NORMALWEIGHT => FC6000\_Normalweight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M15\_NORMALWEIGHT => Indian\_M15\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M20\_NORMALWEIGHT => Indian\_M20\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M25\_NORMALWEIGHT => Indian\_M25\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M30\_NORMALWEIGHT => Indian\_M30\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M35\_NORMALWEIGHT => Indian\_M35\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M40\_NORMALWEIGHT => Indian\_M40\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M45\_NORMALWEIGHT => Indian\_M45\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M50\_NORMALWEIGHT => Indian\_M50\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M55\_NORMALWEIGHT => Indian\_M55\_NormalWeight

◦            MATERIAL\_CONCRETE\_SUBTYPE\_INDIAN\_M60\_NORMALWEIGHT => Indian\_M60\_NormalWeight

•  eMatTypeRebar

◦            MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr40 => ASTM\_A615Gr40

◦            MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr60 => ASTM\_A615Gr60

◦            MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A615Gr75 => ASTM\_A615Gr75

◦            MATERIAL\_REBAR\_SUBTYPE\_ASTM\_A706 => ASTM\_A706

◦            MATERIAL\_REBAR\_SUBTYPE\_CHINESE\_HPB235 => Chinese\_HPB235

◦            MATERIAL\_REBAR\_SUBTYPE\_CHINESE\_HRB335 => Chinese\_HRB335

◦            MATERIAL\_REBAR\_SUBTYPE\_CHINESE\_HRB400 => Chinese\_HRB400

◦            MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_HYSD415 => Indian\_HYSD415

◦            MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_HYSD500 => Indian\_HYSD500

◦            MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_HYSD550 => Indian\_HYSD550

◦            MATERIAL\_REBAR\_SUBTYPE\_INDIAN\_Mild250 => Indian\_Mild250

•  eMatTypeSteel

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A36 => ASTM\_A36

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A500GrB\_Fy42 => ASTM\_A500GrB\_Fy42

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A500GrB\_Fy46 => ASTM\_A500GrB\_Fy46

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A53GrB => ASTM\_A53GrB

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A572Gr50 => ASTM\_A572Gr50

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A913Gr50 => ASTM\_A913Gr50

◦            MATERIAL\_STEEL\_SUBTYPE\_ASTM\_A992\_Fy50 => ASTM\_A992\_Fy50

◦            MATERIAL\_STEEL\_SUBTYPE\_CHINESE\_Q235 => Chinese\_Q235

◦            MATERIAL\_STEEL\_SUBTYPE\_CHINESE\_Q345 => Chinese\_Q345

◦            MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S235 => EN100252\_S235

◦            MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S275 => EN100252\_S275

◦            MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S355 => EN100252\_S355

◦            MATERIAL\_STEEL\_SUBTYPE\_EN100252\_S450 => EN100252\_S450

◦            MATERIAL\_STEEL\_SUBTYPE\_INDIAN\_Fe250 => Indian\_Fe250

◦            MATERIAL\_STEEL\_SUBTYPE\_INDIAN\_Fe345 => Indian\_Fe345

•  eMatTypeTendon

◦            MATERIAL\_TENDON\_SUBTYPE\_ASTM\_A416Gr250 => ASTM\_A416Gr250

◦            MATERIAL\_TENDON\_SUBTYPE\_ASTM\_A416Gr270 => ASTM\_A416Gr270

