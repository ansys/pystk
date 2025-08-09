ChainConstraints
================

.. py:class:: ansys.stk.core.stkobjects.ChainConstraints

   Chain constraints.

.. py:currentmodule:: ChainConstraints

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.use_minimum_angle`
              - Opt to constrain a chain so that access to or from the chain is limited by the minimum vector angle among the objects in the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.minimum_angle`
              - Get or set the minimum vector angle among the objects in the chain. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.use_maximum_angle`
              - Opt to constrain a chain so that access to or from the chain is limited by the maximum vector angle among the objects in the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.maximum_angle`
              - Get or set the maximum vector angle among the objects in the chain. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.use_minimum_link_time`
              - Opt to constrain a chain so that accesses of shorter duration than the specified minimum value are excluded from chain access results.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.minimum_link_time`
              - User-specified minimum access duration. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.filter_access_intervals_by_file`
              - Opt to use an .int file to filter the computed chain access intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.load_interval_file`
              - Get or set the name of the .int file used to filter the computed chain access intervals.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ChainConstraints


Property detail
---------------

.. py:property:: use_minimum_angle
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.use_minimum_angle
    :type: bool

    Opt to constrain a chain so that access to or from the chain is limited by the minimum vector angle among the objects in the chain.

.. py:property:: minimum_angle
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.minimum_angle
    :type: float

    Get or set the minimum vector angle among the objects in the chain. Uses Angle Dimension.

.. py:property:: use_maximum_angle
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.use_maximum_angle
    :type: bool

    Opt to constrain a chain so that access to or from the chain is limited by the maximum vector angle among the objects in the chain.

.. py:property:: maximum_angle
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.maximum_angle
    :type: float

    Get or set the maximum vector angle among the objects in the chain. Uses Angle Dimension.

.. py:property:: use_minimum_link_time
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.use_minimum_link_time
    :type: bool

    Opt to constrain a chain so that accesses of shorter duration than the specified minimum value are excluded from chain access results.

.. py:property:: minimum_link_time
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.minimum_link_time
    :type: float

    User-specified minimum access duration. Uses Time Dimension.

.. py:property:: filter_access_intervals_by_file
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.filter_access_intervals_by_file
    :type: bool

    Opt to use an .int file to filter the computed chain access intervals.

.. py:property:: load_interval_file
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.load_interval_file
    :type: str

    Get or set the name of the .int file used to filter the computed chain access intervals.


