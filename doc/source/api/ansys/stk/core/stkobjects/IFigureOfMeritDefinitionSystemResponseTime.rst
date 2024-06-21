IFigureOfMeritDefinitionSystemResponseTime
==========================================

.. py:class:: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime

   IFigureOfMeritDefinitionCompute
   
   System Response Time Figure of Merit.

.. py:currentmodule:: IFigureOfMeritDefinitionSystemResponseTime

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.command_station_path`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.receive_station_path`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.command_perp_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.commanding_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.pre_collection_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.collection_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.post_collection_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.downlink_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.allow_forward_crosslink`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritDefinitionSystemResponseTime


Property detail
---------------

.. py:property:: command_station_path
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.command_station_path
    :type: str

    Instance path for the commanding object. NONE can be used to clear the commanding object.

.. py:property:: receive_station_path
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.receive_station_path
    :type: str

    Instance path for the receiving object. NONE can be used to clear the receiving object.

.. py:property:: command_perp_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.command_perp_time
    :type: float

    Amount of time in seconds required for command preparation.

.. py:property:: commanding_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.commanding_time
    :type: float

    Amount of time in seconds required for transmission of the prepared command from the CommandStation to the assets.

.. py:property:: pre_collection_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.pre_collection_time
    :type: float

    Amount of time in seconds required from receipt of commanding until a collection can be performed by the assets.

.. py:property:: collection_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.collection_time
    :type: float

    Amount of time in seconds required for data collection.

.. py:property:: post_collection_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.post_collection_time
    :type: float

    Amount of time in seconds required from asset collection until data can be transmitted to the ReceiveStation.

.. py:property:: downlink_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.downlink_time
    :type: float

    Amount of time in seconds required for transmission of the collected data from the assets to the ReceiveStation.

.. py:property:: allow_forward_crosslink
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.allow_forward_crosslink
    :type: bool

    Determines if a single cross-link between assets is allowed to be used to minimize the response time.

.. py:property:: time_step
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemResponseTime.time_step
    :type: float

    Gets or sets the value in seconds to be used during the computation of satisfaction intervals.


