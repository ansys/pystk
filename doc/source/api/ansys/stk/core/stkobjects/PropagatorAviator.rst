PropagatorAviator
=================

.. py:class:: ansys.stk.core.stkobjects.PropagatorAviator

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Class defining the Mission Modler propagator for an Aircraft.

.. py:currentmodule:: PropagatorAviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorAviator.get_flight_mission`
              - Return the underlying Flight Mission object.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorAviator.aviator_propagator`
              - Aviator propagator object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorAviator


Property detail
---------------

.. py:property:: aviator_propagator
    :canonical: ansys.stk.core.stkobjects.PropagatorAviator.aviator_propagator
    :type: typing.Any

    Aviator propagator object.


Method detail
-------------


.. py:method:: get_flight_mission(self) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.PropagatorAviator.get_flight_mission

    Return the underlying Flight Mission object.

    :Returns:

        :obj:`~typing.Any`

