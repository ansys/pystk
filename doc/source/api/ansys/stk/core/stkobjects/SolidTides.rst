SolidTides
==========

.. py:class:: ansys.stk.core.stkobjects.SolidTides

   Class defining the contribution of solid tides.

.. py:currentmodule:: SolidTides

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SolidTides.include_time_dependent_solid_tides`
              - Time-dependent solid tide effects: opt whether to account for the secondary contribution from certain effects of loading the crust and core.
            * - :py:attr:`~ansys.stk.core.stkobjects.SolidTides.minimum_amplitude`
              - Minimum tidal amplitude to include in the computation. Uses SmallDistanceUnit Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SolidTides.truncate_solid_tides`
              - True if solid tide terms (including permanent tide) won't be included beyond the degree and order selected for the gravity model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SolidTides


Property detail
---------------

.. py:property:: include_time_dependent_solid_tides
    :canonical: ansys.stk.core.stkobjects.SolidTides.include_time_dependent_solid_tides
    :type: bool

    Time-dependent solid tide effects: opt whether to account for the secondary contribution from certain effects of loading the crust and core.

.. py:property:: minimum_amplitude
    :canonical: ansys.stk.core.stkobjects.SolidTides.minimum_amplitude
    :type: float

    Minimum tidal amplitude to include in the computation. Uses SmallDistanceUnit Dimension.

.. py:property:: truncate_solid_tides
    :canonical: ansys.stk.core.stkobjects.SolidTides.truncate_solid_tides
    :type: bool

    True if solid tide terms (including permanent tide) won't be included beyond the degree and order selected for the gravity model.


