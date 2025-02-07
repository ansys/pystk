IDataProviderInfo
=================

.. py:class:: ansys.stk.core.stkobjects.IDataProviderInfo

   Provide methods for retrieving the information about data providers.

.. py:currentmodule:: IDataProviderInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderInfo.is_group`
              - Determine if the data provider represents a group.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderInfo.name`
              - Return a name of the data provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderInfo.type`
              - Return a type of the data provider.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderInfo


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IDataProviderInfo.name
    :type: str

    Return a name of the data provider.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IDataProviderInfo.type
    :type: DataProviderType

    Return a type of the data provider.


Method detail
-------------



.. py:method:: is_group(self) -> bool
    :canonical: ansys.stk.core.stkobjects.IDataProviderInfo.is_group

    Determine if the data provider represents a group.

    :Returns:

        :obj:`~bool`

