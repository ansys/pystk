OLEDropMode
===========

.. py:class:: ansys.stk.core.stkx.OLEDropMode

   IntEnum


.. py:currentmodule:: OLEDropMode

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~NONE`
              - None. The control does not accept OLE drops and displays the No Drop cursor.

            * - :py:attr:`~MANUAL`
              - Manual. The control triggers the OLE drop events, allowing the programmer to handle the OLE drop operation in code.

            * - :py:attr:`~AUTOMATIC`
              - Automatic. The control automatically accepts OLE drops if the DataObject object contains data in a format it recognizes. No OLE drag/drop events on the target will occur when OLEDropMode is set to eAutomatic.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import OLEDropMode


