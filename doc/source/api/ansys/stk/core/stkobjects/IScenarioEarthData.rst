IScenarioEarthData
==================

.. py:class:: IScenarioEarthData

   object
   
   IAgScEarthData Interface for Earth Orientation Parameters.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reload_eop`
              - Reload the EOP file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~eop_filename`
            * - :py:meth:`~eop_start_time`
            * - :py:meth:`~eop_stop_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScenarioEarthData


Property detail
---------------

.. py:property:: eop_filename
    :canonical: ansys.stk.core.stkobjects.IScenarioEarthData.eop_filename
    :type: str

    Filename of an EOP file (.dat) located in the DynamicEarthData directory or an EOP file (.txt) provided by CelesTrak, which can be downloaded from http://celestrak.org/SpaceData/.

.. py:property:: eop_start_time
    :canonical: ansys.stk.core.stkobjects.IScenarioEarthData.eop_start_time
    :type: typing.Any

    Start time of the EOP data. Uses DateFormat Dimension.

.. py:property:: eop_stop_time
    :canonical: ansys.stk.core.stkobjects.IScenarioEarthData.eop_stop_time
    :type: typing.Any

    Stop time of the EOP data. Uses DateFormat Dimension.


Method detail
-------------





.. py:method:: reload_eop(self) -> None

    Reload the EOP file.

    :Returns:

        :obj:`~None`

