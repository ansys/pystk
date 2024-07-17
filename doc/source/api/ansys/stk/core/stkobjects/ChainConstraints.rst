ChainConstraints
================

.. py:class:: ansys.stk.core.stkobjects.ChainConstraints

   Bases: 

   Chain constraints.

.. py:currentmodule:: ChainConstraints

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.use_min_angle`
              - Opt to constrain a chain so that access to or from the chain is limited by the minimum vector angle among the objects in the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.min_angle`
              - Gets or sets the minimum vector angle among the objects in the chain. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.use_max_angle`
              - Opt to constrain a chain so that access to or from the chain is limited by the maximum vector angle among the objects in the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.max_angle`
              - Gets or sets the maximum vector angle among the objects in the chain. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.use_min_link_time`
              - Opt to constrain a chain so that accesses of shorter duration than the specified minimum value are excluded from chain access results.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.min_link_time`
              - User-specified minimum access duration. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.use_load_interval_file`
              - Opt to use an .int file to filter the computed chain access intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainConstraints.load_interval_file`
              - Gets or sets the name of the .int file used to filter the computed chain access intervals.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ChainConstraints


Property detail
---------------

.. py:property:: use_min_angle
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.use_min_angle
    :type: bool

    Opt to constrain a chain so that access to or from the chain is limited by the minimum vector angle among the objects in the chain.

.. py:property:: min_angle
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.min_angle
    :type: float

    Gets or sets the minimum vector angle among the objects in the chain. Uses Angle Dimension.

.. py:property:: use_max_angle
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.use_max_angle
    :type: bool

    Opt to constrain a chain so that access to or from the chain is limited by the maximum vector angle among the objects in the chain.

.. py:property:: max_angle
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.max_angle
    :type: float

    Gets or sets the maximum vector angle among the objects in the chain. Uses Angle Dimension.

.. py:property:: use_min_link_time
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.use_min_link_time
    :type: bool

    Opt to constrain a chain so that accesses of shorter duration than the specified minimum value are excluded from chain access results.

.. py:property:: min_link_time
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.min_link_time
    :type: float

    User-specified minimum access duration. Uses Time Dimension.

.. py:property:: use_load_interval_file
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.use_load_interval_file
    :type: bool

    Opt to use an .int file to filter the computed chain access intervals.

.. py:property:: load_interval_file
    :canonical: ansys.stk.core.stkobjects.ChainConstraints.load_interval_file
    :type: str

    Gets or sets the name of the .int file used to filter the computed chain access intervals.


