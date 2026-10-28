FlightDynamicsRecordCreator
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator

   Flight dynamics record creator.

.. py:currentmodule:: FlightDynamicsRecordCreator

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.export`
              - Set the converted initial state to be used by the problem.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.reset`
              - Reset the flight dynamics record creator parameters to default values.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.desired_epoch_type`
              - Get or sets the  the state from the ephemeris.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.epoch`
              - Get or set the Date & Time associated with this launch time.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.preview`
              - Get the flight dynamics record preview.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.record_name`
              - Get or set the flight dynamics record name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.segment_name`
              - Get or set the segment to pull the ephemeris from.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.use_default_record_name`
              - Get or set the option for using the default record name.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import FlightDynamicsRecordCreator


Property detail
---------------

.. py:property:: desired_epoch_type
    :canonical: ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.desired_epoch_type
    :type: FlightDynamicsRecordEpochType

    Get or sets the  the state from the ephemeris.

.. py:property:: epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.epoch
    :type: typing.Any

    Get or set the Date & Time associated with this launch time.

.. py:property:: preview
    :canonical: ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.preview
    :type: FlightDynamicsRecordPreview

    Get the flight dynamics record preview.

.. py:property:: record_name
    :canonical: ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.record_name
    :type: str

    Get or set the flight dynamics record name.

.. py:property:: segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.segment_name
    :type: str

    Get or set the segment to pull the ephemeris from.

.. py:property:: use_default_record_name
    :canonical: ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.use_default_record_name
    :type: bool

    Get or set the option for using the default record name.


Method detail
-------------





.. py:method:: export(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.export

    Set the converted initial state to be used by the problem.

    :Returns:

        :obj:`~None`




.. py:method:: reset(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.FlightDynamicsRecordCreator.reset

    Reset the flight dynamics record creator parameters to default values.

    :Returns:

        :obj:`~None`





