StkObjectPreDeleteEventArgs
===========================

.. py:class:: ansys.stk.core.stkobjects.StkObjectPreDeleteEventArgs

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
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectPreDeleteEventArgs.continue_object_deletion`
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

.. py:property:: continue_object_deletion
    :canonical: ansys.stk.core.stkobjects.StkObjectPreDeleteEventArgs.continue_object_deletion
    :type: bool

    The status to continue or stop the object deletion.


