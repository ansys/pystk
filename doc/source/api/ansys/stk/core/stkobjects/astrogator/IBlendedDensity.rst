IBlendedDensity
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.IBlendedDensity

   object
   
   Properties for the blended atmospheric density propagator function.

.. py:currentmodule:: IBlendedDensity

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBlendedDensity.atm_density_model`
              - Embeds a nominal atmosphere model from the component browser.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBlendedDensity.low_altitude_atm_density_model`
              - Embeds a low altitude atmosphere model from the component browser.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBlendedDensity.density_blending_altitude_range`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBlendedDensity.atm_density_model_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBlendedDensity.low_altitude_atm_density_model_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBlendedDensity.use_approx_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBlendedDensity.lower_bound_upper_atm_model`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IBlendedDensity


Property detail
---------------

.. py:property:: density_blending_altitude_range
    :canonical: ansys.stk.core.stkobjects.astrogator.IBlendedDensity.density_blending_altitude_range
    :type: float

    Gets or sets the blending range (distance dimension), begins at lower bound of upper model.

.. py:property:: atm_density_model_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IBlendedDensity.atm_density_model_name
    :type: str

    Returns the name of the embedded nominal atmospheric model.

.. py:property:: low_altitude_atm_density_model_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IBlendedDensity.low_altitude_atm_density_model_name
    :type: str

    Returns the name of the embedded low altitude atmospheric model.

.. py:property:: use_approx_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IBlendedDensity.use_approx_altitude
    :type: bool

    True if using approximate altitude formula (enforced on embedded models).

.. py:property:: lower_bound_upper_atm_model
    :canonical: ansys.stk.core.stkobjects.astrogator.IBlendedDensity.lower_bound_upper_atm_model
    :type: float

    Get the lowest valid altitude of the upper atmospheric density model.


Method detail
-------------

.. py:method:: atm_density_model(self, pInVal: IComponentInfo) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IBlendedDensity.atm_density_model

    Embeds a nominal atmosphere model from the component browser.

    :Parameters:

    **pInVal** : :obj:`~IComponentInfo`

    :Returns:

        :obj:`~None`

.. py:method:: low_altitude_atm_density_model(self, pInVal: IComponentInfo) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IBlendedDensity.low_altitude_atm_density_model

    Embeds a low altitude atmosphere model from the component browser.

    :Parameters:

    **pInVal** : :obj:`~IComponentInfo`

    :Returns:

        :obj:`~None`








