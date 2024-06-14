IFigureOfMeritDefinitionSystemAgeOfData
=======================================

.. py:class:: IFigureOfMeritDefinitionSystemAgeOfData

   IFigureOfMeritDefinitionCompute
   
   System Age of Data Figure of Merit.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~command_station_path`
            * - :py:meth:`~receive_station_path`
            * - :py:meth:`~command_prep_time`
            * - :py:meth:`~commanding_time`
            * - :py:meth:`~pre_collection_time`
            * - :py:meth:`~collection_time`
            * - :py:meth:`~post_collection_time`
            * - :py:meth:`~downlink_time`
            * - :py:meth:`~allow_forward_crosslink`
            * - :py:meth:`~time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritDefinitionSystemAgeOfData


Property detail
---------------

.. py:property:: command_station_path
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemAgeOfData.command_station_path
    :type: str

    Instance path for the commanding object. NONE can be used to clear the commanding object.

.. py:property:: receive_station_path
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemAgeOfData.receive_station_path
    :type: str

    Instance path for the receiving object. NONE can be used to clear the receiving object.

.. py:property:: command_prep_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemAgeOfData.command_prep_time
    :type: float

    Amount of time in seconds required for command preparation.

.. py:property:: commanding_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemAgeOfData.commanding_time
    :type: float

    Amount of time in seconds required for transmission of the prepared command from the CommandStation to the assets.

.. py:property:: pre_collection_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemAgeOfData.pre_collection_time
    :type: float

    Amount of time in seconds required from receipt of commanding until a collection can be performed by the assets.

.. py:property:: collection_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemAgeOfData.collection_time
    :type: float

    Amount of time in seconds required for data collection.

.. py:property:: post_collection_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemAgeOfData.post_collection_time
    :type: float

    Amount of time in seconds required from asset collection until data can be transmitted to the ReceiveStation.

.. py:property:: downlink_time
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemAgeOfData.downlink_time
    :type: float

    Amount of time in seconds required for transmission of the collected data from the assets to the ReceiveStation.

.. py:property:: allow_forward_crosslink
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemAgeOfData.allow_forward_crosslink
    :type: bool

    Determines if a single cross-link between assets is allowed to be used to minimize the response time.

.. py:property:: time_step
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritDefinitionSystemAgeOfData.time_step
    :type: float

    Gets or sets the value in seconds to be used during the computation of satisfaction intervals.


