IStkRfcmAnalysisLink
====================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink

   Properties for a transceiver link for an analysis.

.. py:currentmodule:: IStkRfcmAnalysisLink

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.compute`
              - Compute the analysis link at the given time.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.name`
              - Gets the analysis link name.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.transmit_transceiver_identifier`
              - Gets the transmit transceiver identifier.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.transmit_transceiver_name`
              - Gets the transmit transceiver name.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.receive_transceiver_identifier`
              - Gets the receive transceiver identifier.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.receive_transceiver_name`
              - Gets the receive transceiver name.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.transmit_antenna_count`
              - Gets the transmit antenna count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.receive_antenna_count`
              - Gets the receive antenna count.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.analysis_intervals`
              - Gets the analysis intervals array.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import IStkRfcmAnalysisLink


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.name
    :type: str

    Gets the analysis link name.

.. py:property:: transmit_transceiver_identifier
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.transmit_transceiver_identifier
    :type: str

    Gets the transmit transceiver identifier.

.. py:property:: transmit_transceiver_name
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.transmit_transceiver_name
    :type: str

    Gets the transmit transceiver name.

.. py:property:: receive_transceiver_identifier
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.receive_transceiver_identifier
    :type: str

    Gets the receive transceiver identifier.

.. py:property:: receive_transceiver_name
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.receive_transceiver_name
    :type: str

    Gets the receive transceiver name.

.. py:property:: transmit_antenna_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.transmit_antenna_count
    :type: int

    Gets the transmit antenna count.

.. py:property:: receive_antenna_count
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.receive_antenna_count
    :type: int

    Gets the receive antenna count.

.. py:property:: analysis_intervals
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.analysis_intervals
    :type: list

    Gets the analysis intervals array.


Method detail
-------------









.. py:method:: compute(self, time: float) -> IStkRfcmResponse
    :canonical: ansys.stk.core.stkrfchannelmodeler.IStkRfcmAnalysisLink.compute

    Compute the analysis link at the given time.

    :Parameters:

    **time** : :obj:`~float`

    :Returns:

        :obj:`~IStkRfcmResponse`

