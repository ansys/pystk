MarkerBatchSizeSource
=====================

.. py:class:: ansys.stk.core.graphics.MarkerBatchSizeSource

   IntEnum


.. py:currentmodule:: MarkerBatchSizeSource

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FROM_TEXTURE`
              - The size of each marker is the same as the size of its texture. If the marker is not textured, the user defined size is used instead.

            * - :py:attr:`~USER_DEFINED`
              - The size of each marker in the marker batch is user defined. Either all markers have the same size (size) or each marker has a user defined size (SetSizes).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import MarkerBatchSizeSource


