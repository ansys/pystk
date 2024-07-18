StkObjectPreDeleteEventArgs
===========================

.. py:class:: ansys.stk.core.stkobjects.StkObjectPreDeleteEventArgs

   Bases: 

   Arguments for the OnStkObjectPreDelete event.

.. py:currentmodule:: StkObjectPreDeleteEventArgs

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectPreDeleteEventArgs.path`
              - Object path.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectPreDeleteEventArgs.continue_method`
              - The status to continue or stop the object deletion.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StkObjectPreDeleteEventArgs


Property detail
---------------

.. py:property:: path
    :canonical: ansys.stk.core.stkobjects.StkObjectPreDeleteEventArgs.path
    :type: str

    Object path.

.. py:property:: continue_method
    :canonical: ansys.stk.core.stkobjects.StkObjectPreDeleteEventArgs.continue_method
    :type: bool

    The status to continue or stop the object deletion.


