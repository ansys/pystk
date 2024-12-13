AntennaModelApertureRectangularCosineSquaredPedestal
====================================================

.. py:class:: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a rectangular cosine squared pedestal aperture antenna model.

.. py:currentmodule:: AntennaModelApertureRectangularCosineSquaredPedestal

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.compute_mainlobe_gain`
              - Gets or sets the option for computing the mainlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.mainlobe_gain`
              - Gets or sets the mainlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.backlobe_gain`
              - Gets or sets the backlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.efficiency`
              - Gets or sets the efficiency.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.use_backlobe_as_mainlobe_atten`
              - Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.input_type`
              - Gets or sets the input type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.x_dimension`
              - Gets or sets the x dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.y_dimension`
              - Gets or sets the y dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.x_beamwidth`
              - Gets or sets the x beamwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.y_beamwidth`
              - Gets or sets the y beamwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.pedestal_level`
              - Gets or sets the pedestal level.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaModelApertureRectangularCosineSquaredPedestal


Property detail
---------------

.. py:property:: compute_mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.compute_mainlobe_gain
    :type: bool

    Gets or sets the option for computing the mainlobe gain.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.mainlobe_gain
    :type: float

    Gets or sets the mainlobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.backlobe_gain
    :type: float

    Gets or sets the backlobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.use_backlobe_as_mainlobe_atten
    :type: bool

    Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.input_type
    :type: RectangularApertureInputType

    Gets or sets the input type.

.. py:property:: x_dimension
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.x_dimension
    :type: float

    Gets or sets the x dimension.

.. py:property:: y_dimension
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.y_dimension
    :type: float

    Gets or sets the y dimension.

.. py:property:: x_beamwidth
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.x_beamwidth
    :type: typing.Any

    Gets or sets the x beamwidth.

.. py:property:: y_beamwidth
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.y_beamwidth
    :type: typing.Any

    Gets or sets the y beamwidth.

.. py:property:: pedestal_level
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureRectangularCosineSquaredPedestal.pedestal_level
    :type: float

    Gets or sets the pedestal level.


