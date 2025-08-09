ITransceiverModel
=================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.ITransceiverModel

   Base interface which defines common properties for a transceiver model.

.. py:currentmodule:: ITransceiverModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.ITransceiverModel.set_antenna_type`
              - Set the transceiver's antenna type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.ITransceiverModel.type`
              - Get the transceiver unique identifier.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.ITransceiverModel.supported_antenna_types`
              - Get the supported antenna types.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.ITransceiverModel.antenna`
              - Get the transceiver's antenna settings.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import ITransceiverModel


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkrfchannelmodeler.ITransceiverModel.type
    :type: TransceiverModelType

    Get the transceiver unique identifier.

.. py:property:: supported_antenna_types
    :canonical: ansys.stk.core.stkrfchannelmodeler.ITransceiverModel.supported_antenna_types
    :type: list

    Get the supported antenna types.

.. py:property:: antenna
    :canonical: ansys.stk.core.stkrfchannelmodeler.ITransceiverModel.antenna
    :type: IAntenna

    Get the transceiver's antenna settings.


Method detail
-------------


.. py:method:: set_antenna_type(self, antenna_type: str) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.ITransceiverModel.set_antenna_type

    Set the transceiver's antenna type.

    :Parameters:

        **antenna_type** : :obj:`~str`


    :Returns:

        :obj:`~None`



