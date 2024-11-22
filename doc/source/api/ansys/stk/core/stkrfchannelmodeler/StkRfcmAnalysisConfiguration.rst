StkRfcmAnalysisConfiguration
============================

.. py:class:: ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration

   The configuration for an analysis.

.. py:currentmodule:: StkRfcmAnalysisConfiguration

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration.name`
              - Gets or sets the configuration name.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration.description`
              - Gets or sets the configuration description.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration.supported_central_bodies`
              - Gets an array of available central bodies.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration.central_body_name`
              - Gets the configured central body name.
            * - :py:attr:`~ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration.model`
              - Get the analysis configuration model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfcm import StkRfcmAnalysisConfiguration


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration.name
    :type: str

    Gets or sets the configuration name.

.. py:property:: description
    :canonical: ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration.description
    :type: str

    Gets or sets the configuration description.

.. py:property:: supported_central_bodies
    :canonical: ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration.supported_central_bodies
    :type: list

    Gets an array of available central bodies.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration.central_body_name
    :type: str

    Gets the configured central body name.

.. py:property:: model
    :canonical: ansys.stk.core.stkrfcm.StkRfcmAnalysisConfiguration.model
    :type: IStkRfcmAnalysisConfigurationModel

    Get the analysis configuration model.


