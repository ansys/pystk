IDataProvider
=============

.. py:class:: ansys.stk.core.stkobjects.IDataProvider

   Represents the Sub Data Provider (i.e. ``Fixed`` in ``Cartesian Position`` group on satellites, or ``Cartesian Position`` on facilities).

.. py:currentmodule:: IDataProvider

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProvider.is_statistic_available`
              - Is the supplied statistic available for the provided element name?
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProvider.is_time_varying_extremum_available`
              - Is the supplied time varying extremum available for the provided element name?

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProvider.elements`
              - Returns a collection of elements associated with a DataProvider or a SubDataProvider.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProvider.pre_data`
              - The string associated with the current PreData parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProvider.allow_user_interface_for_pre_data`
              - When set to true the data provider will display a user interface to select/enter the pre-data required.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProvider.is_valid`
              - Returns whether the data provider is valid.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProvider.pre_data_required`
              - Returns whether the data provider requires pre data.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProvider.pre_data_description`
              - Returns a description of the required pre data.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProvider


Property detail
---------------

.. py:property:: elements
    :canonical: ansys.stk.core.stkobjects.IDataProvider.elements
    :type: DataProviderElements

    Returns a collection of elements associated with a DataProvider or a SubDataProvider.

.. py:property:: pre_data
    :canonical: ansys.stk.core.stkobjects.IDataProvider.pre_data
    :type: str

    The string associated with the current PreData parameter.

.. py:property:: allow_user_interface_for_pre_data
    :canonical: ansys.stk.core.stkobjects.IDataProvider.allow_user_interface_for_pre_data
    :type: bool

    When set to true the data provider will display a user interface to select/enter the pre-data required.

.. py:property:: is_valid
    :canonical: ansys.stk.core.stkobjects.IDataProvider.is_valid
    :type: bool

    Returns whether the data provider is valid.

.. py:property:: pre_data_required
    :canonical: ansys.stk.core.stkobjects.IDataProvider.pre_data_required
    :type: bool

    Returns whether the data provider requires pre data.

.. py:property:: pre_data_description
    :canonical: ansys.stk.core.stkobjects.IDataProvider.pre_data_description
    :type: str

    Returns a description of the required pre data.


Method detail
-------------








.. py:method:: is_statistic_available(self, statistic: StatisticType, element_name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IDataProvider.is_statistic_available

    Is the supplied statistic available for the provided element name?

    :Parameters:

    **statistic** : :obj:`~StatisticType`
    **element_name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: is_time_varying_extremum_available(self, time_var_extremum: TimeVaryingExtremum, element_name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IDataProvider.is_time_varying_extremum_available

    Is the supplied time varying extremum available for the provided element name?

    :Parameters:

    **time_var_extremum** : :obj:`~TimeVaryingExtremum`
    **element_name** : :obj:`~str`

    :Returns:

        :obj:`~bool`


