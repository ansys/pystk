ScenarioEarthData
=================

.. py:class:: ansys.stk.core.stkobjects.ScenarioEarthData

   Class defining the Earth Orientation Parameters of a Scenario.

.. py:currentmodule:: ScenarioEarthData

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioEarthData.reload_eop`
              - Reload the EOP file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioEarthData.eop_filename`
              - Filename of an EOP file (.dat) located in the DynamicEarthData directory or an EOP file (.txt) provided by CelesTrak, which can be downloaded from http://celestrak.org/SpaceData/.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioEarthData.eop_start_time`
              - Start time of the EOP data. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScenarioEarthData.eop_stop_time`
              - Stop time of the EOP data. Uses DateFormat Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScenarioEarthData


Property detail
---------------

.. py:property:: eop_filename
    :canonical: ansys.stk.core.stkobjects.ScenarioEarthData.eop_filename
    :type: str

    Filename of an EOP file (.dat) located in the DynamicEarthData directory or an EOP file (.txt) provided by CelesTrak, which can be downloaded from http://celestrak.org/SpaceData/.

.. py:property:: eop_start_time
    :canonical: ansys.stk.core.stkobjects.ScenarioEarthData.eop_start_time
    :type: typing.Any

    Start time of the EOP data. Uses DateFormat Dimension.

.. py:property:: eop_stop_time
    :canonical: ansys.stk.core.stkobjects.ScenarioEarthData.eop_stop_time
    :type: typing.Any

    Stop time of the EOP data. Uses DateFormat Dimension.


Method detail
-------------





.. py:method:: reload_eop(self) -> None
    :canonical: ansys.stk.core.stkobjects.ScenarioEarthData.reload_eop

    Reload the EOP file.

    :Returns:

        :obj:`~None`

