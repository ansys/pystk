ProfileMode
===========

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileMode

   IntEnum


.. py:currentmodule:: ProfileMode

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ITERATE`
              - Iterate - the Target Sequence will run the profile as it is configured in an attempt to attain the desired solution.

            * - :py:attr:`~NOT_ACTIVE`
              - Not Active - the Target Sequence will ignore the profile when running.

            * - :py:attr:`~RUN_ONCE`
              - Run Once - the Target Sequence will run the profile once according to its current configuration.

            * - :py:attr:`~ACTIVE`
              - Active - the Target Sequence will apply the change that the profile passes when running.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileMode


