AnalysisConfiguration
=====================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration

   The configuration for an analysis.

.. py:currentmodule:: AnalysisConfiguration

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration.name`
              - Get or set the configuration name.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration.description`
              - Get or set the configuration description.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration.supported_central_bodies`
              - Get an array of available central bodies.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration.central_body_name`
              - Get the configured central body name.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration.model`
              - Get the analysis configuration model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import AnalysisConfiguration


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration.name
    :type: str

    Get or set the configuration name.

.. py:property:: description
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration.description
    :type: str

    Get or set the configuration description.

.. py:property:: supported_central_bodies
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration.supported_central_bodies
    :type: list

    Get an array of available central bodies.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration.central_body_name
    :type: str

    Get the configured central body name.

.. py:property:: model
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfiguration.model
    :type: IAnalysisConfigurationModel

    Get the analysis configuration model.


