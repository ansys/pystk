IDataProviderInfo
=================

.. py:class:: IDataProviderInfo

   object
   
   Provide methods for retrieving the information about data providers.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_group`
              - Determine if the data provider represents a group.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderInfo


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IDataProviderInfo.name
    :type: str

    Returns a name of the data provider.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IDataProviderInfo.type
    :type: "DATA_PROVIDER_TYPE"

    Returns a type of the data provider.


Method detail
-------------



.. py:method:: is_group(self) -> bool

    Determine if the data provider represents a group.

    :Returns:

        :obj:`~bool`

