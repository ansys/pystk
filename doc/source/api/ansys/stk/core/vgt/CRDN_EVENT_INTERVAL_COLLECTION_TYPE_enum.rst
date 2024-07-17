CRDN_EVENT_INTERVAL_COLLECTION_TYPE
===================================

.. py:class:: ansys.stk.core.vgt.CRDN_EVENT_INTERVAL_COLLECTION_TYPE

   IntEnum


.. py:currentmodule:: CRDN_EVENT_INTERVAL_COLLECTION_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported interval collection types.

            * - :py:attr:`~LIGHTING`
              - Defined by computing sunlight, penumbra and umbra intervals as seen at specified location using specified selection of eclipsing bodies.

            * - :py:attr:`~SIGNALED`
              - Determine what interval list collection is recorded at target clock location by performing signal transmission of original interval list collection between base and target clock locations.

            * - :py:attr:`~CONDITION`
              - Interval collection containing intervals during which condition set is satisfied.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CRDN_EVENT_INTERVAL_COLLECTION_TYPE


