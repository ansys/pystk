StkRfcmAnalysisConfigurationCollection
======================================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection

   A collection of analysis configurations.

.. py:currentmodule:: StkRfcmAnalysisConfigurationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.remove_at`
              - Remove the analysis configuration at the supplied index.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.remove`
              - Remove the supplied analysis configuration.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.add_new`
              - Add and returns a new analysis configuration.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.add`
              - Add the supplied analysis configuration.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.remove_all`
              - Clear the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.contains`
              - Determine if the collection contains an analysis configuration with the given name.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.find`
              - Find an analysis configuration by name. Returns Null if the configuration name does not exist in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.count`
              - Returns the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection._new_enum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import StkRfcmAnalysisConfigurationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.count
    :type: int

    Returns the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> StkRfcmAnalysisConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~StkRfcmAnalysisConfiguration`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.remove_at

    Remove the analysis configuration at the supplied index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, value: StkRfcmAnalysisConfiguration) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.remove

    Remove the supplied analysis configuration.

    :Parameters:

    **value** : :obj:`~StkRfcmAnalysisConfiguration`

    :Returns:

        :obj:`~None`

.. py:method:: add_new(self, model_type: RfcmAnalysisConfigurationModelType, configuration_name: str) -> StkRfcmAnalysisConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.add_new

    Add and returns a new analysis configuration.

    :Parameters:

    **model_type** : :obj:`~RfcmAnalysisConfigurationModelType`
    **configuration_name** : :obj:`~str`

    :Returns:

        :obj:`~StkRfcmAnalysisConfiguration`

.. py:method:: add(self, value: StkRfcmAnalysisConfiguration) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.add

    Add the supplied analysis configuration.

    :Parameters:

    **value** : :obj:`~StkRfcmAnalysisConfiguration`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.remove_all

    Clear the collection.

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, configuration_name: str) -> bool
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.contains

    Determine if the collection contains an analysis configuration with the given name.

    :Parameters:

    **configuration_name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: find(self, configuration_name: str) -> StkRfcmAnalysisConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.StkRfcmAnalysisConfigurationCollection.find

    Find an analysis configuration by name. Returns Null if the configuration name does not exist in the collection.

    :Parameters:

    **configuration_name** : :obj:`~str`

    :Returns:

        :obj:`~StkRfcmAnalysisConfiguration`

