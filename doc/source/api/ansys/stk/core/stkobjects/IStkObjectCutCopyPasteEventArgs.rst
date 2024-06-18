IStkObjectCutCopyPasteEventArgs
===============================

.. py:class:: IStkObjectCutCopyPasteEventArgs

   object
   
   Arguments for the OnStkObjectPreCut, OnStkObjectCopy and OnStkObjectPaste events.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~selected_object_path`
            * - :py:meth:`~object_paths`
            * - :py:meth:`~pasted_object_paths`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkObjectCutCopyPasteEventArgs


Property detail
---------------

.. py:property:: selected_object_path
    :canonical: ansys.stk.core.stkobjects.IStkObjectCutCopyPasteEventArgs.selected_object_path
    :type: str

    Selected Object path that is being cut, copied or pasted.

.. py:property:: object_paths
    :canonical: ansys.stk.core.stkobjects.IStkObjectCutCopyPasteEventArgs.object_paths
    :type: list

    Returns an array of object paths that are cut, copied or pasted.

.. py:property:: pasted_object_paths
    :canonical: ansys.stk.core.stkobjects.IStkObjectCutCopyPasteEventArgs.pasted_object_paths
    :type: list

    Returns an array of object paths that are being pasted. The new object paths corresposnd to the old paths at the same array location in ObjectPaths array.


