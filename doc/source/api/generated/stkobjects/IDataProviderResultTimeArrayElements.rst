IDataProviderResultTimeArrayElements
====================================

.. py:class:: IDataProviderResultTimeArrayElements

   object
   
   Provide a array result of element values for each time array value.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_array`
              - Return an array of values at the specified index.  Valid values of index range from 0 to Count-1.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~valid`
            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderResultTimeArrayElements


Property detail
---------------

.. py:property:: valid
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultTimeArrayElements.valid
    :type: bool

    Returns true if the result is valid, false otherwise.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultTimeArrayElements.count
    :type: int

    Get the number of arrays in the result.


Method detail
-------------

.. py:method:: get_array(self, indexOrName:typing.Any) -> list

    Return an array of values at the specified index.  Valid values of index range from 0 to Count-1.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`



