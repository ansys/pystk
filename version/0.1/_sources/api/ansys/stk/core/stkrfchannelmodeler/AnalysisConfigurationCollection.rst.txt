AnalysisConfigurationCollection
===============================

.. py:class:: ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection

   A collection of analysis configurations.

.. py:currentmodule:: AnalysisConfigurationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.remove_at`
              - Remove the analysis configuration at the supplied index.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.remove`
              - Remove the supplied analysis configuration.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.add_new`
              - Add and returns a new analysis configuration.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.add`
              - Add the supplied analysis configuration.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.remove_all`
              - Clear the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.contains`
              - Determine if the collection contains an analysis configuration with the given name.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.find`
              - Find an analysis configuration by name. Returns Null if the configuration name does not exist in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.count`
              - Return the number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkrfchannelmodeler import AnalysisConfigurationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.count
    :type: int

    Return the number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> AnalysisConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~AnalysisConfiguration`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.remove_at

    Remove the analysis configuration at the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove(self, value: AnalysisConfiguration) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.remove

    Remove the supplied analysis configuration.

    :Parameters:

        **value** : :obj:`~AnalysisConfiguration`


    :Returns:

        :obj:`~None`

.. py:method:: add_new(self, model_type: AnalysisConfigurationModelType, configuration_name: str) -> AnalysisConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.add_new

    Add and returns a new analysis configuration.

    :Parameters:

        **model_type** : :obj:`~AnalysisConfigurationModelType`

        **configuration_name** : :obj:`~str`


    :Returns:

        :obj:`~AnalysisConfiguration`

.. py:method:: add(self, value: AnalysisConfiguration) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.add

    Add the supplied analysis configuration.

    :Parameters:

        **value** : :obj:`~AnalysisConfiguration`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.remove_all

    Clear the collection.

    :Returns:

        :obj:`~None`

.. py:method:: contains(self, configuration_name: str) -> bool
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.contains

    Determine if the collection contains an analysis configuration with the given name.

    :Parameters:

        **configuration_name** : :obj:`~str`


    :Returns:

        :obj:`~bool`

.. py:method:: find(self, configuration_name: str) -> AnalysisConfiguration
    :canonical: ansys.stk.core.stkrfchannelmodeler.AnalysisConfigurationCollection.find

    Find an analysis configuration by name. Returns Null if the configuration name does not exist in the collection.

    :Parameters:

        **configuration_name** : :obj:`~str`


    :Returns:

        :obj:`~AnalysisConfiguration`

