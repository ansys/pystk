THIRD_BODY_GRAVITY_SOURCE_TYPE
==============================

.. py:class:: ansys.stk.core.stkobjects.THIRD_BODY_GRAVITY_SOURCE_TYPE

   IntEnum


.. py:currentmodule:: THIRD_BODY_GRAVITY_SOURCE_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CENTRAL_BODY_FILE`
              - Central body file (all bodies): gravitational value from editable central body file shipped with STK.

            * - :py:attr:`~HPOP_HISTORICAL`
              - HPOP historical (Sun and Moon only): hard-coded, uneditable value used in prior versions of HPOP.

            * - :py:attr:`~JPL_DEVELOPMENTAL_EPHEMERIS`
              - JPL DE (Sun, Moon and planets): DE 405 ephemerides, covering a time span from 1960 to 2060.

            * - :py:attr:`~USER_SPECIFIED`
              - User-specified: enter the value directly.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import THIRD_BODY_GRAVITY_SOURCE_TYPE


