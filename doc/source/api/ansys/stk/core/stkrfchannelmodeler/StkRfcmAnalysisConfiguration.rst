StkRfcmAnalysisConfiguration
============================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration

   The configuration for an analysis.

.. py:currentmodule:: StkRfcmAnalysisConfiguration

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration.name`
              - Get or set the configuration name.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration.description`
              - Get or set the configuration description.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration.supported_central_bodies`
              - Get an array of available central bodies.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration.central_body_name`
              - Get the configured central body name.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration.model`
              - Get the analysis configuration model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import StkRfcmAnalysisConfiguration


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration.name
    :type: str

    Get or set the configuration name.

.. py:property:: description
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration.description
    :type: str

    Get or set the configuration description.

.. py:property:: supported_central_bodies
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration.supported_central_bodies
    :type: list

    Get an array of available central bodies.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration.central_body_name
    :type: str

    Get the configured central body name.

.. py:property:: model
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfiguration.model
    :type: IStkRfcmAnalysisConfigurationModel

    Get the analysis configuration model.


