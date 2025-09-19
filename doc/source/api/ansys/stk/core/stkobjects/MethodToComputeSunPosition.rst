MethodToComputeSunPosition
==========================

.. py:class:: ansys.stk.core.stkobjects.MethodToComputeSunPosition

   IntEnum


.. py:currentmodule:: MethodToComputeSunPosition

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~APPARENT`
              - Apparent: takes into account the time required for light to travel from the sun to the position of the spacecraft.

            * - :py:attr:`~APPARENT_TO_TRUE_CENTRAL_BODY_LOCATION`
              - Apparent Sun to True Central Body: takes into account the time required for light to travel from the sun to the central body.

            * - :py:attr:`~TRUE`
              - True: assumes that light from the sun reaches the spacecraft instantaneously.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import MethodToComputeSunPosition


