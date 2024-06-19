IDataObjectFiles
================

.. py:class:: IDataObjectFiles

   object
   
   Collection of file names.

.. py:currentmodule:: ansys.stk.core.stkx

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Get the file name at the specified index (0-based).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import IDataObjectFiles


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkx.IDataObjectFiles._NewEnum
    :type: EnumeratorProxy

    Returns an object that can be used to iterate through all the file names in the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkx.IDataObjectFiles.count
    :type: int

    Number of file names contained in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkx.IDataObjectFiles.item

    Get the file name at the specified index (0-based).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


