DataObjectFiles
===============

.. py:class:: ansys.stk.core.stkx.DataObjectFiles

   Collection of files for OLE drag & drop operations.

.. py:currentmodule:: DataObjectFiles

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.DataObjectFiles.item`
              - Get the file name at the specified index (0-based).

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.DataObjectFiles._new_enum`
              - Return an object that can be used to iterate through all the file names in the collection.
            * - :py:attr:`~ansys.stk.core.stkx.DataObjectFiles.count`
              - Number of file names contained in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import DataObjectFiles


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkx.DataObjectFiles._new_enum
    :type: EnumeratorProxy

    Return an object that can be used to iterate through all the file names in the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkx.DataObjectFiles.count
    :type: int

    Number of file names contained in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkx.DataObjectFiles.item

    Get the file name at the specified index (0-based).

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~str`


