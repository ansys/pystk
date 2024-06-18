IGravityFieldFunction
=====================

.. py:class:: IGravityFieldFunction

   object
   
   Properties for the Gravitational Force gravity model - a complex gravitational force calculation, optionally including solid and ocean tide effects.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~gravity_filename`
            * - :py:meth:`~degree`
            * - :py:meth:`~order`
            * - :py:meth:`~max_degree_text`
            * - :py:meth:`~max_order_text`
            * - :py:meth:`~include_time_dependent_solid_tides`
            * - :py:meth:`~solid_tide_min_amp`
            * - :py:meth:`~use_ocean_tides`
            * - :py:meth:`~ocean_tide_min_amp`
            * - :py:meth:`~min_radius_percent`
            * - :py:meth:`~central_body_name`
            * - :py:meth:`~ocean_tide_max_degree`
            * - :py:meth:`~ocean_tide_max_order`
            * - :py:meth:`~solid_tide_type`
            * - :py:meth:`~truncate_solid_tides`
            * - :py:meth:`~use_secular_variations`
            * - :py:meth:`~partials_degree`
            * - :py:meth:`~partials_order`
            * - :py:meth:`~max_partials_degree_text`
            * - :py:meth:`~max_partials_order_text`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IGravityFieldFunction


Property detail
---------------

.. py:property:: gravity_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.gravity_filename
    :type: str

    Gets or sets the name of the file containing the gravity field.

.. py:property:: degree
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.degree
    :type: int

    Gets or sets the degree of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.

.. py:property:: order
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.order
    :type: int

    Gets or sets the order of geopotential coefficients to be included for Central Body gravity computations. Valid range is from 0 to 90, depending on the gravity model. Dimensionless.

.. py:property:: max_degree_text
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.max_degree_text
    :type: str

    Displays the maximum degree permissible for the gravity model.

.. py:property:: max_order_text
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.max_order_text
    :type: str

    Displays the maximum order permissible for the gravity model.

.. py:property:: include_time_dependent_solid_tides
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.include_time_dependent_solid_tides
    :type: bool

    True if including time dependent solid tides.

.. py:property:: solid_tide_min_amp
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.solid_tide_min_amp
    :type: float

    Gets or sets the minimum amplitude for solid tides; contributors that are below the minimum amplitude will not be factored into the computation. Uses SmallDistance Dimension.

.. py:property:: use_ocean_tides
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.use_ocean_tides
    :type: bool

    True if using ocean tides.

.. py:property:: ocean_tide_min_amp
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.ocean_tide_min_amp
    :type: float

    Gets or sets the minimum amplitude for ocean tides; contributors that are below the minimum amplitude will not be factored into the computation. Uses SmallDistance Dimension.

.. py:property:: min_radius_percent
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.min_radius_percent
    :type: float

    Gets or sets the percentage of the central body's minimum radius at which a modified force model (only the two-body force) will be used - provided there is no altitude stopping condition. Uses Percent Dimension.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.central_body_name
    :type: str

    Get the name of the central body.

.. py:property:: ocean_tide_max_degree
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.ocean_tide_max_degree
    :type: int

    Gets or sets the maximum degree for force contributions from ocean tides that will be included in the computation. Dimensionless.

.. py:property:: ocean_tide_max_order
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.ocean_tide_max_order
    :type: int

    Gets or sets the maximum order for force contributions from ocean tides that will be included in the computation. Dimensionless.

.. py:property:: solid_tide_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.solid_tide_type
    :type: "SOLID_TIDE"

    Gets or sets the type of solid tide contribution to be modeled.

.. py:property:: truncate_solid_tides
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.truncate_solid_tides
    :type: bool

    True if solid tide terms (including permanent tide) won't be included beyond the degree and order selected for the gravity model.

.. py:property:: use_secular_variations
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.use_secular_variations
    :type: bool

    Opt whether to include or ignore secular variations defined by the gravity field model.

.. py:property:: partials_degree
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.partials_degree
    :type: int

    Gets or sets the degree of geopotential coefficients to be included for Central Body gravity state transition matrix computations. Valid range is from 0 to 90, depending on the gravity model and the degree used for state computations. Dimensionless.

.. py:property:: partials_order
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.partials_order
    :type: int

    Gets or sets the order of geopotential coefficients to be included for Central Body gravity state transition matrix computations. Valid range is from 0 to 90, depending on the gravity model and the order used for state computations. Dimensionless.

.. py:property:: max_partials_degree_text
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.max_partials_degree_text
    :type: str

    Displays the maximum degree permissible for the gravity model partials used in the STM.

.. py:property:: max_partials_order_text
    :canonical: ansys.stk.core.stkobjects.astrogator.IGravityFieldFunction.max_partials_order_text
    :type: str

    Displays the maximum order permissible for the gravity model partials used in the STM.


