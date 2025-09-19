SpaceEnvironmentSAAFluxLevel
============================

.. py:class:: ansys.stk.core.stkobjects.SpaceEnvironmentSAAFluxLevel

   IntEnum


.. py:currentmodule:: SpaceEnvironmentSAAFluxLevel

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - An invalid SpaceEnvironmentSAAFluxLevel value.

            * - :py:attr:`~GREATER_THAN_BACKGROUND_BY_3_SIGMA`
              - Represents flux values greater than the background environment by 3 sigma.

            * - :py:attr:`~HALF_OF_PEAK`
              - Represents flux values of about half the peak flux value at the given altitude.

            * - :py:attr:`~TENTH_OF_PEAK`
              - Represents flux values of about one-tenth the peak flux value at the given altitude.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SpaceEnvironmentSAAFluxLevel


