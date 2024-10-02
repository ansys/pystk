AnalysisWorkbenchProviderRoot
=============================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchProviderRoot

   Represents a VGT root.

.. py:currentmodule:: AnalysisWorkbenchProviderRoot

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProviderRoot.get_template_provider`
              - Return a template provider. The method takes a class name (i.e. \"Satellite\", \"Facility\", etc.).
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProviderRoot.get_provider`
              - Return an instance provider. The method takes a short instance path to an STK object or a central body.(i.e. \"Satellite/Satellite1\", \"CentralBody/Earth\", etc.).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProviderRoot.well_known_systems`
              - Returns the most commonly used systems (e.g. Sun Fixed, Earth Fixed, etc.).
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProviderRoot.well_known_axes`
              - Returns the most commonly used axes (e.g. Sun ICRF, Earth Inertial, etc.).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchProviderRoot


Property detail
---------------

.. py:property:: well_known_systems
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProviderRoot.well_known_systems
    :type: VectorGeometryToolWellKnownSystems

    Returns the most commonly used systems (e.g. Sun Fixed, Earth Fixed, etc.).

.. py:property:: well_known_axes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProviderRoot.well_known_axes
    :type: VectorGeometryToolWellKnownAxes

    Returns the most commonly used axes (e.g. Sun ICRF, Earth Inertial, etc.).


Method detail
-------------

.. py:method:: get_template_provider(self, className: str) -> AnalysisWorkbenchComponentProvider
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProviderRoot.get_template_provider

    Return a template provider. The method takes a class name (i.e. \"Satellite\", \"Facility\", etc.).

    :Parameters:

    **className** : :obj:`~str`

    :Returns:

        :obj:`~AnalysisWorkbenchComponentProvider`

.. py:method:: get_provider(self, instPath: str) -> AnalysisWorkbenchComponentProvider
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProviderRoot.get_provider

    Return an instance provider. The method takes a short instance path to an STK object or a central body.(i.e. \"Satellite/Satellite1\", \"CentralBody/Earth\", etc.).

    :Parameters:

    **instPath** : :obj:`~str`

    :Returns:

        :obj:`~AnalysisWorkbenchComponentProvider`



