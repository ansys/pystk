DataProviderResultTimeArrayElements
===================================

.. py:class:: ansys.stk.core.stkobjects.DataProviderResultTimeArrayElements

   Provide a array result of element values for each time array value.

.. py:currentmodule:: DataProviderResultTimeArrayElements

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultTimeArrayElements.get_array`
              - Return an array of values at the specified index.  Valid values of index range from 0 to Count-1.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultTimeArrayElements.valid`
              - Return true if the result is valid, false otherwise.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultTimeArrayElements.count`
              - Get the number of arrays in the result.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderResultTimeArrayElements


Property detail
---------------

.. py:property:: valid
    :canonical: ansys.stk.core.stkobjects.DataProviderResultTimeArrayElements.valid
    :type: bool

    Return true if the result is valid, false otherwise.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.DataProviderResultTimeArrayElements.count
    :type: int

    Get the number of arrays in the result.


Method detail
-------------

.. py:method:: get_array(self, index_or_name: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.DataProviderResultTimeArrayElements.get_array

    Return an array of values at the specified index.  Valid values of index range from 0 to Count-1.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`



