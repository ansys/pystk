VERT_LANDING_MODE
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.VERT_LANDING_MODE

   IntEnum


.. py:currentmodule:: VERT_LANDING_MODE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~VERT_LANDING_INDEPENDENT`
              - The aircraft's heading is independent of its translation.

            * - :py:attr:`~VERT_LANDING_ALIGN_TRANSLATION_COURSE`
              - The aircraft will align its heading with the translation course.

            * - :py:attr:`~VERT_LANDING_INTO_WIND`
              - The aircraft will set its heading into the wind.

            * - :py:attr:`~VERT_LANDING_ALIGN_TRANSLATION_COURSE_OVERRIDE`
              - The aircraft will align its heading with the translation course  will achieve the specified heading upon arriving.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import VERT_LANDING_MODE


