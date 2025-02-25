# Copyright (C) 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from test_util import *
from code_snippets.code_snippets_test_base import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects import *
from ansys.stk.core.vgt import *


@category("Graphics Tests")
class StkObjectVOSnippets(CodeSnippetsTestBase):
    def __init__(self, *args, **kwargs):
        super(StkObjectVOSnippets, self).__init__(*args, **kwargs)

    # region OneTimeSetUp
    @staticmethod
    def setUpClass():
        CodeSnippetsTestBase.Initialize()

    # endregion

    # region OneTimeTearDown
    @staticmethod
    def tearDownClass():
        CodeSnippetsTestBase.Uninitialize()

    # endregion

    # region TestSetUp
    def setUp(self):
        pass

    # endregion

    # region TestTearDown
    def tearDown(self):
        pass

    # endregion

    # region ConfigureVOModelFile
    def test_ConfigureVOModelFile(self):
        satellite: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "satellite1"), Satellite
        )
        model: "IGraphics3DModel" = satellite.graphics_3d.model

        self.ConfigureVOModelFile(model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "satellite1")

    def ConfigureVOModelFile(self, model: "IGraphics3DModel"):
        # Set new ModelFile.Filename
        model.model_type = ModelType.FILE
        modelFile: "Graphics3DModelFile" = clr.CastAs(model.model_data, Graphics3DModelFile)
        modelFile.filename = r"\STKData\VO\Models\Space\alexis.glb"

        # Configure basic settings
        model.visible = True
        model.scale_value = 4.8

    # endregion

    # region ConfigureVOArticulations
    def test_ConfigureVOArticulations(self):
        satellite: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "satellite1"), Satellite
        )
        model: "IGraphics3DModel" = satellite.graphics_3d.model

        # Set new ModelFile.Filename
        model.model_type = ModelType.FILE
        modelFile: "Graphics3DModelFile" = clr.CastAs(model.model_data, Graphics3DModelFile)
        modelFile.filename = r"\STKData\VO\Models\Space\satellite.glb"

        self.ConfigureVOModelArticulations(model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "satellite1")

    def ConfigureVOModelArticulations(self, model: "IGraphics3DModel"):
        # Configure articulation
        modelArticulation: "Graphics3DModelArticulation" = model.articulation
        modelArticulation.enable_default_save = False
        modelArticulation.save_articulation_file_on_save = True

        # Set our articulation and transformations
        # For this sample, these articulations exist for a default satellite model
        levelOfDetail: int = 0
        articulation: str = "Satellite"
        transformation: str = "Size"

        # Get the current transition value
        currentTransVal: float = modelArticulation.get_transformation_value(levelOfDetail, articulation, transformation)

        # Change the value
        newTransVal: float = currentTransVal * 0.5

        # Set our new transition value
        modelArticulation.set_transformation_value(levelOfDetail, articulation, transformation, newTransVal)

    # endregion

    # region ListVOModelArticulations
    def test_ListVOModelArticulations(self):
        satellite: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "satellite1"), Satellite
        )
        model: "IGraphics3DModel" = satellite.graphics_3d.model

        self.ListVOModelArticulations(satellite, model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "satellite1")

    def ListVOModelArticulations(self, satellite: "Satellite", model: "IGraphics3DModel"):
        # Enumerating through the transformation collection is helpful if you do not
        # know what tranformations exist or their value ranges

        modelArticulation: "Graphics3DModelArticulation" = model.articulation

        lod: int = 0
        while lod < modelArticulation.level_of_detail_count:
            # Get all articulations
            # GetAvailableArticulations returns a one dimensional array of articulation names
            articulations = modelArticulation.get_available_articulations(lod)

            articulation: int = 0
            while articulation < Array.Length(articulations):
                # We need the articulation string to call the GetAvailableTransformations function
                articulationString: str = str(articulations[articulation])

                # Get all transformations
                transformations: "Graphics3DModelTransformationCollection" = (
                    modelArticulation.get_available_transformations(lod, articulationString)
                )

                # Enumerate through available transformations
                trans: "Graphics3DModelTransformation"

                # Enumerate through available transformations
                for trans in transformations:
                    Console.WriteLine(
                        "Name: {0}, Current {1}, Max {2}, Min {3}",
                        trans.name,
                        trans.value,
                        trans.maximum,
                        trans.minimum,
                    )

                articulation += 1

            lod += 1

    # endregion

    # region ConfigureVOModelLevelOfDetail
    def test_ConfigureVOModelLevelOfDetail(self):
        satellite: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "satellite1"), Satellite
        )
        model: "IGraphics3DModel" = satellite.graphics_3d.model

        self.ConfigureVOModelLevelOfDetail(model)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "satellite1")

    def ConfigureVOModelLevelOfDetail(self, model: "IGraphics3DModel"):
        # Configure level of details
        detail: "Graphics3DDetailThreshold" = model.detail_threshold
        detail.enable_detail_threshold = True

        # (assuming unit preferences set to km)
        detail.all = 2.51189
        detail.model_label = 158489
        detail.marker_label = 2511890.0
        detail.marker = 25110000.0
        detail.point = 1000000000000.0

    # endregion

    # region ConfigureVOVector
    def test_ConfigureVOVector(self):
        vehicle: "GroundVehicle" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.GROUND_VEHICLE, "gv1"),
            GroundVehicle,
        )

        self.ConfigureVOVector(vehicle.graphics_3d.vector)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.GROUND_VEHICLE, "gv1")

    def ConfigureVOVector(self, vector: "Graphics3DVector"):
        # See AvailableCrdns for supported elements
        vector.vector_geometry_tool_components.add(
            GeometricElementType.VECTOR_ELEMENT,
            (
                IAnalysisWorkbenchComponent(
                    CodeSnippetsTestBase.m_Root.central_bodies["Earth"].analysis_workbench_components.vectors["Moon"]
                )
            ).qualified_path,
        )
        vector.vector_geometry_tool_components.add(
            GeometricElementType.AXES_ELEMENT,
            (
                IAnalysisWorkbenchComponent(
                    CodeSnippetsTestBase.m_Root.central_bodies["Moon"].analysis_workbench_components.vectors["Position"]
                )
            ).qualified_path,
        )
        vector.vector_geometry_tool_components.add(
            GeometricElementType.VECTOR_ELEMENT,
            (
                IAnalysisWorkbenchComponent(
                    CodeSnippetsTestBase.m_Root.central_bodies["Sun"].analysis_workbench_components.vectors[
                        "Velocity(Barycenter)"
                    ]
                )
            ).qualified_path,
        )

        # Draw on Central Body
        body: "Graphics3DReferenceVector" = clr.CastAs(
            vector.vector_geometry_tool_components.get_component_by_name(
                GeometricElementType.AXES_ELEMENT,
                (
                    IAnalysisWorkbenchComponent(
                        CodeSnippetsTestBase.m_Root.central_bodies["Earth"].analysis_workbench_components.vectors[
                            "Moon"
                        ]
                    )
                ).qualified_path,
            ),
            Graphics3DReferenceVector,
        )
        (body).color = Colors.Yellow
        body.draw_at_central_body = True
        body.axes = "CentralBody/Earth Fixed Axes"

        vector.scale_relative_to_model = True
        vector.angle_size_scale = 4.5

    # endregion

    # region ConfigureVODataDisplay
    def test_ConfigureVODataDisplay(self):
        sat: "Satellite" = clr.CastAs(
            CodeSnippetsTestBase.m_Root.current_scenario.children.new(STKObjectType.SATELLITE, "sat1"), Satellite
        )
        (sat).set_propagator_type(PropagatorType.TWO_BODY)
        tb: "PropagatorTwoBody" = clr.CastAs((sat).propagator, PropagatorTwoBody)
        tb.propagate()
        ddc: "Graphics3DDataDisplayCollection" = sat.graphics_3d.data_display
        self.ConfigureVODataDisplay(ddc)

        CodeSnippetsTestBase.m_Root.current_scenario.children.unload(STKObjectType.SATELLITE, "sat1")

    def ConfigureVODataDisplay(self, datadisplaycol: "Graphics3DDataDisplayCollection"):
        # Add existing data display
        # See AvailableData property for available data display
        displayElement: "Graphics3DDataDisplayElement" = datadisplaycol.add("Solar Intensity")

        # Configure data display as needed
        displayElement.title_text = "Sol. Intensity"
        displayElement.show_graphics = True
        displayElement.location = Graphics3DLocation.WINDOW_3D
        displayElement.font_color = Colors.White
        displayElement.font_size = Graphics3DFontSize.SMALL
        displayElement.use_background = True
        displayElement.background_color = Colors.Orange
        displayElement.use_automatic_size_width = False
        displayElement.use_automatic_size_height = False
        displayElement.background_height = 55
        displayElement.background_width = 260
        displayElement.background_translucency = 0.5
        displayElement.use_background_texture = False
        displayElement.use_background_border = True
        displayElement.background_border_color = Colors.White

    # endregion
