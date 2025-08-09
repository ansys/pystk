AnalysisWorkbenchRoot
=====================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchRoot

   Represents a VGT root.

.. py:currentmodule:: AnalysisWorkbenchRoot

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchRoot.get_template_provider`
              - Return a template provider. The method takes a class name (i.e. ``Satellite``, ``Facility``, etc.).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchRoot.get_provider`
              - Return an instance provider. The method takes a short instance path to an STK object or a central body.(i.e. ``Satellite/Satellite1``, ``CentralBody/Earth``, etc.).

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchRoot.well_known_systems`
              - Return the most commonly used systems (e.g. Sun Fixed, Earth Fixed, etc.).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchRoot.well_known_axes`
              - Return the most commonly used axes (e.g. Sun ICRF, Earth Inertial, etc.).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchRoot


Property detail
---------------

.. py:property:: well_known_systems
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchRoot.well_known_systems
    :type: VectorGeometryToolWellKnownSystems

    Return the most commonly used systems (e.g. Sun Fixed, Earth Fixed, etc.).

.. py:property:: well_known_axes
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchRoot.well_known_axes
    :type: VectorGeometryToolWellKnownAxes

    Return the most commonly used axes (e.g. Sun ICRF, Earth Inertial, etc.).


Method detail
-------------

.. py:method:: get_template_provider(self, class_name: str) -> AnalysisWorkbenchComponentProvider
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchRoot.get_template_provider

    Return a template provider. The method takes a class name (i.e. ``Satellite``, ``Facility``, etc.).

    :Parameters:

        **class_name** : :obj:`~str`


    :Returns:

        :obj:`~AnalysisWorkbenchComponentProvider`

.. py:method:: get_provider(self, inst_path: str) -> AnalysisWorkbenchComponentProvider
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchRoot.get_provider

    Return an instance provider. The method takes a short instance path to an STK object or a central body.(i.e. ``Satellite/Satellite1``, ``CentralBody/Earth``, etc.).

    :Parameters:

        **inst_path** : :obj:`~str`


    :Returns:

        :obj:`~AnalysisWorkbenchComponentProvider`



