IStkObjectModelContext
======================

.. py:class:: ansys.stk.core.stkobjects.IStkObjectModelContext

   object
   
   Represents a factory class to create instances of the AgStkObjectRoot class.

.. py:currentmodule:: IStkObjectModelContext

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectModelContext.create`
              - Create a non-restrictive root object.
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectModelContext.create_restrictive`
              - Create a restrictive root object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkObjectModelContext



Method detail
-------------

.. py:method:: create(self) -> IStkObjectRoot
    :canonical: ansys.stk.core.stkobjects.IStkObjectModelContext.create

    Create a non-restrictive root object.

    :Returns:

        :obj:`~IStkObjectRoot`

.. py:method:: create_restrictive(self) -> IStkObjectRoot
    :canonical: ansys.stk.core.stkobjects.IStkObjectModelContext.create_restrictive

    Create a restrictive root object.

    :Returns:

        :obj:`~IStkObjectRoot`

