VTOL_TRANSLATION_FINAL_COURSE_MODE
==================================

.. py:class:: VTOL_TRANSLATION_FINAL_COURSE_MODE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~TRANSLATE_DIRECT`
              - The aircraft will translate directly along the specified bearing and range.

            * - :py:attr:`~BISECT_INBOUND_OUTBOUND`
              - The aircraft will translate along a bisecting line between the inbound and outbound course.

            * - :py:attr:`~ANTICIPATE_NEXT_TRANSLATION`
              - The aircraft will evaluate the procedure ahead to determine the translation bearing and rate.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import VTOL_TRANSLATION_FINAL_COURSE_MODE


