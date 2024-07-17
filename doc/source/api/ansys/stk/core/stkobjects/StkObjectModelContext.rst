StkObjectModelContext
=====================

.. py:class:: ansys.stk.core.stkobjects.StkObjectModelContext

   Bases: 

   AgStkObjectModelContext class provides methods to create instance of AgStkObjectRoot class.

.. py:currentmodule:: StkObjectModelContext

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectModelContext.create`
              - Create a non-restrictive root object.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectModelContext.create_restrictive`
              - Create a restrictive root object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StkObjectModelContext



Method detail
-------------

.. py:method:: create(self) -> StkObjectRoot
    :canonical: ansys.stk.core.stkobjects.StkObjectModelContext.create

    Create a non-restrictive root object.

    :Returns:

        :obj:`~StkObjectRoot`

.. py:method:: create_restrictive(self) -> StkObjectRoot
    :canonical: ansys.stk.core.stkobjects.StkObjectModelContext.create_restrictive

    Create a restrictive root object.

    :Returns:

        :obj:`~StkObjectRoot`

