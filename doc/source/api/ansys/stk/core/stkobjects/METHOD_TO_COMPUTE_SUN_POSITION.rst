METHOD_TO_COMPUTE_SUN_POSITION
==============================

.. py:class:: ansys.stk.core.stkobjects.METHOD_TO_COMPUTE_SUN_POSITION

   IntEnum


.. py:currentmodule:: METHOD_TO_COMPUTE_SUN_POSITION

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~MTCSP_APPARENT`
              - Apparent: takes into account the time required for light to travel from the sun to the position of the spacecraft.

            * - :py:attr:`~MTCSP_APPARENT_TO_TRUE_CB`
              - Apparent Sun to True Central Body: takes into account the time required for light to travel from the sun to the central body.

            * - :py:attr:`~MTCSP_TRUE`
              - True: assumes that light from the sun reaches the spacecraft instantaneously.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import METHOD_TO_COMPUTE_SUN_POSITION


