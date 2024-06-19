SET_HINT
========

.. py:class:: SET_HINT

   IntEnum


.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~INFREQUENT`
              - Rendering is optimized for static geometry. The primitive's vertices are not going to be updated with Set() or SetPartial() calls. Calls to SetPartial() will fail. Calls to Set() are allowed but may not be as efficient as SetHintFrequent.

            * - :py:attr:`~PARTIAL`
              - Rendering is optimized for dynamic geometry. The primitive's vertices are expected to be updated with SetPartial() - some or all of the vertices will change but the number of vertices will not.

            * - :py:attr:`~FREQUENT`
              - Rendering is optimized for streaming geometry. The primitive's vertices are expected to be updated with Set() - all the vertices will change and/or the number of vertices will change. Calls to SetPartial() will fail.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SET_HINT


