DATA_PROVIDER_TYPE
==================

.. py:class:: ansys.stk.core.stkobjects.DATA_PROVIDER_TYPE

   IntEnum


.. py:currentmodule:: DATA_PROVIDER_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~FIXED`
              - Not time dependent, e.g. facility position.

            * - :py:attr:`~TIME_VARYING`
              - Time varying, e.g. satellite position.

            * - :py:attr:`~INTERVAL`
              - Interval, e.g. lighting data.

            * - :py:attr:`~ALLOW_DUPLICATE_TIMES`
              - Allow duplicated times.

            * - :py:attr:`~STAND_ALONE`
              - Do not mix data from different data providers.

            * - :py:attr:`~RESULTS_DEPEND_ON_INPUT_INTERVALS`
              - Results depend on evaluation interval(s).

            * - :py:attr:`~NOT_AVAILABLE_FORDYNAMIC_GRAPHS_AND_STRIP_CHARTS`
              - Make unavailable for dynamic displays and strip charts.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DATA_PROVIDER_TYPE


