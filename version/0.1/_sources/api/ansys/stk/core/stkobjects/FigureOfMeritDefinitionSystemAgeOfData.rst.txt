FigureOfMeritDefinitionSystemAgeOfData
======================================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData

   Bases: :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinitionCompute`, :py:class:`~ansys.stk.core.stkobjects.IFigureOfMeritDefinition`

   System Age Of Data Figure of Merit.

.. py:currentmodule:: FigureOfMeritDefinitionSystemAgeOfData

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.command_station_path`
              - Instance path for the commanding object. NONE can be used to clear the commanding object.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.receive_station_path`
              - Instance path for the receiving object. NONE can be used to clear the receiving object.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.command_preparation_time`
              - Amount of time in seconds required for command preparation.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.commanding_time`
              - Amount of time in seconds required for transmission of the prepared command from the CommandStation to the assets.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.pre_collection_time`
              - Amount of time in seconds required from receipt of commanding until a collection can be performed by the assets.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.collection_time`
              - Amount of time in seconds required for data collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.post_collection_time`
              - Amount of time in seconds required from asset collection until data can be transmitted to the ReceiveStation.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.downlink_time`
              - Amount of time in seconds required for transmission of the collected data from the assets to the ReceiveStation.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.allow_forward_crosslink`
              - Determine if a single cross-link between assets is allowed to be used to minimize the response time.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.time_step`
              - Get or set the value in seconds to be used during the computation of satisfaction intervals.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritDefinitionSystemAgeOfData


Property detail
---------------

.. py:property:: command_station_path
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.command_station_path
    :type: str

    Instance path for the commanding object. NONE can be used to clear the commanding object.

.. py:property:: receive_station_path
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.receive_station_path
    :type: str

    Instance path for the receiving object. NONE can be used to clear the receiving object.

.. py:property:: command_preparation_time
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.command_preparation_time
    :type: float

    Amount of time in seconds required for command preparation.

.. py:property:: commanding_time
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.commanding_time
    :type: float

    Amount of time in seconds required for transmission of the prepared command from the CommandStation to the assets.

.. py:property:: pre_collection_time
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.pre_collection_time
    :type: float

    Amount of time in seconds required from receipt of commanding until a collection can be performed by the assets.

.. py:property:: collection_time
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.collection_time
    :type: float

    Amount of time in seconds required for data collection.

.. py:property:: post_collection_time
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.post_collection_time
    :type: float

    Amount of time in seconds required from asset collection until data can be transmitted to the ReceiveStation.

.. py:property:: downlink_time
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.downlink_time
    :type: float

    Amount of time in seconds required for transmission of the collected data from the assets to the ReceiveStation.

.. py:property:: allow_forward_crosslink
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.allow_forward_crosslink
    :type: bool

    Determine if a single cross-link between assets is allowed to be used to minimize the response time.

.. py:property:: time_step
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritDefinitionSystemAgeOfData.time_step
    :type: float

    Get or set the value in seconds to be used during the computation of satisfaction intervals.


