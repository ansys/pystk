IAnalysisWorkbenchRoot
======================

.. py:class:: IAnalysisWorkbenchRoot

   object
   
   Represents a VGT root object.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_template_provider`
              - Return a template provider. The method takes a class name (i.e. \"Satellite\", \"Facility\", etc.).
            * - :py:meth:`~get_provider`
              - Return an instance provider. The method takes a short instance path to an STK object or a central body.(i.e. \"Satellite/Satellite1\", \"CentralBody/Earth\", etc.).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~well_known_systems`
            * - :py:meth:`~well_known_axes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IAnalysisWorkbenchRoot


Property detail
---------------

.. py:property:: well_known_systems
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchRoot.well_known_systems
    :type: "IAgCrdnWellKnownSystems"

    Returns the most commonly used systems (e.g. Sun Fixed, Earth Fixed, etc.).

.. py:property:: well_known_axes
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchRoot.well_known_axes
    :type: "IAgCrdnWellKnownAxes"

    Returns the most commonly used axes (e.g. Sun ICRF, Earth Inertial, etc.).


Method detail
-------------

.. py:method:: get_template_provider(self, className:str) -> "IAnalysisWorkbenchProvider"

    Return a template provider. The method takes a class name (i.e. \"Satellite\", \"Facility\", etc.).

    :Parameters:

    **className** : :obj:`~str`

    :Returns:

        :obj:`~"IAnalysisWorkbenchProvider"`

.. py:method:: get_provider(self, instPath:str) -> "IAnalysisWorkbenchProvider"

    Return an instance provider. The method takes a short instance path to an STK object or a central body.(i.e. \"Satellite/Satellite1\", \"CentralBody/Earth\", etc.).

    :Parameters:

    **instPath** : :obj:`~str`

    :Returns:

        :obj:`~"IAnalysisWorkbenchProvider"`



