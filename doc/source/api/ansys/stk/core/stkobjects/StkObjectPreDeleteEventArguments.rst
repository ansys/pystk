StkObjectPreDeleteEventArguments
================================

.. py:class:: ansys.stk.core.stkobjects.StkObjectPreDeleteEventArguments

   Arguments for the OnStkObjectPreDelete event.

.. py:currentmodule:: StkObjectPreDeleteEventArguments

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectPreDeleteEventArguments.path`
              - Object path.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectPreDeleteEventArguments.continue_object_deletion`
              - The status to continue or stop the object deletion.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StkObjectPreDeleteEventArguments


Property detail
---------------

.. py:property:: path
    :canonical: ansys.stk.core.stkobjects.StkObjectPreDeleteEventArguments.path
    :type: str

    Object path.

.. py:property:: continue_object_deletion
    :canonical: ansys.stk.core.stkobjects.StkObjectPreDeleteEventArguments.continue_object_deletion
    :type: bool

    The status to continue or stop the object deletion.


