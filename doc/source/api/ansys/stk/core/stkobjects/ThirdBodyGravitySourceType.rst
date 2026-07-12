ThirdBodyGravitySourceType
==========================

.. py:class:: ansys.stk.core.stkobjects.ThirdBodyGravitySourceType

   IntEnum


.. py:currentmodule:: ThirdBodyGravitySourceType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CENTRAL_BODY_FILE`
              - Central body file (all bodies): gravitational value from editable central body file shipped with STK.

            * - :py:attr:`~JPL_DEVELOPMENTAL_EPHEMERIS`
              - JPL DE (Sun, Moon and planets): DE 405 ephemerides, covering a time span from 1960 to 2060.

            * - :py:attr:`~USER_SPECIFIED`
              - User-specified: enter the value directly.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ThirdBodyGravitySourceType


