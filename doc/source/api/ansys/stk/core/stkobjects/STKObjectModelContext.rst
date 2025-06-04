STKObjectModelContext
=====================

.. py:class:: ansys.stk.core.stkobjects.STKObjectModelContext

   STKObjectModelContext class provides methods to create instance of STKObjectRoot class.

.. py:currentmodule:: STKObjectModelContext

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.STKObjectModelContext.create`
              - Create a non-restrictive root object.
            * - :py:attr:`~ansys.stk.core.stkobjects.STKObjectModelContext.create_restrictive`
              - Create a restrictive root object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import STKObjectModelContext



Method detail
-------------

.. py:method:: create(self) -> STKObjectRoot
    :canonical: ansys.stk.core.stkobjects.STKObjectModelContext.create

    Create a non-restrictive root object.

    :Returns:

        :obj:`~STKObjectRoot`

.. py:method:: create_restrictive(self) -> STKObjectRoot
    :canonical: ansys.stk.core.stkobjects.STKObjectModelContext.create_restrictive

    Create a restrictive root object.

    :Returns:

        :obj:`~STKObjectRoot`

