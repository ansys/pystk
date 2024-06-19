SOLID_TIDE
==========

.. py:class:: SOLID_TIDE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FULL`
              - Include both time-dependent and time-independent contributions. This option is only available for gravity field models that support a tide model.

            * - :py:attr:`~PERMANENT`
              - Include only the permanent tide - the time-independent contribution.

            * - :py:attr:`~NONE`
              - Exclude solid tide contributions entirely.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SOLID_TIDE


