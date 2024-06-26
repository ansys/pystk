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

            * - :py:attr:`~DATA_PROVIDER_RESULT_FIXED`
              - Not time dependent, e.g. facility position.

            * - :py:attr:`~DATA_PROVIDER_RESULT_TIME_VARYING`
              - Time varying, e.g. satellite position.

            * - :py:attr:`~DATA_PROVIDER_RESULT_INTVL`
              - Interval, e.g. lighting data.

            * - :py:attr:`~DATA_PROVIDER_RESULT_DUP_TIME`
              - Allow duplicated times.

            * - :py:attr:`~DATA_PROVIDER_RESULT_STAND_ALONE`
              - Do not mix data from different data providers.

            * - :py:attr:`~DATA_PROVIDER_RESULT_INTVL_DEFINED`
              - Results depend on evaluation interval(s).

            * - :py:attr:`~DATA_PROVIDER_RESULT_DYN_IGNORE`
              - Make unavailable for dynamic displays and strip charts.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DATA_PROVIDER_TYPE


