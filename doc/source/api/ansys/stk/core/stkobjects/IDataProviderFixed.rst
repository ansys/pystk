IDataProviderFixed
==================

.. py:class:: IDataProviderFixed

   object
   
   Represents the Fixed Data Provider (i.e. non time dependent like facility position).

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~exec`
              - Compute the data; fixed data providers do not require arguments.
            * - :py:meth:`~exec_elements`
              - Compute the data and returns just the indicated data elements; fixed data providers do not require arguments.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderFixed



Method detail
-------------

.. py:method:: exec(self) -> IDataProviderResult
    :canonical: ansys.stk.core.stkobjects.IDataProviderFixed.exec

    Compute the data; fixed data providers do not require arguments.

    :Returns:

        :obj:`~IDataProviderResult`

.. py:method:: exec_elements(self, elementNames: list) -> IDataProviderResult
    :canonical: ansys.stk.core.stkobjects.IDataProviderFixed.exec_elements

    Compute the data and returns just the indicated data elements; fixed data providers do not require arguments.

    :Parameters:

    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~IDataProviderResult`

