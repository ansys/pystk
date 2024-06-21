IStkObjectPreDeleteEventArgs
============================

.. py:class:: ansys.stk.core.stkobjects.IStkObjectPreDeleteEventArgs

   object
   
   Arguments for the OnStkObjectPreDelete event.

.. py:currentmodule:: IStkObjectPreDeleteEventArgs

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectPreDeleteEventArgs.path`
            * - :py:attr:`~ansys.stk.core.stkobjects.IStkObjectPreDeleteEventArgs.continue_method`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkObjectPreDeleteEventArgs


Property detail
---------------

.. py:property:: path
    :canonical: ansys.stk.core.stkobjects.IStkObjectPreDeleteEventArgs.path
    :type: str

    Object path.

.. py:property:: continue_method
    :canonical: ansys.stk.core.stkobjects.IStkObjectPreDeleteEventArgs.continue_method
    :type: bool

    The status to continue or stop the object deletion.


