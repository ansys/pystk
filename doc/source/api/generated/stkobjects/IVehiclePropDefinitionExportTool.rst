IVehiclePropDefinitionExportTool
================================

.. py:class:: IVehiclePropDefinitionExportTool

   object
   
   Interface used to define the export to data file options.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~export`
              - Export the Propagator (Prop Def) file.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropDefinitionExportTool



Method detail
-------------

.. py:method:: export(self, fileName:str) -> None

    Export the Propagator (Prop Def) file.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`

