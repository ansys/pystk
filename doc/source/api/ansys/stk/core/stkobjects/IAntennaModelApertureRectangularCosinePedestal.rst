IAntennaModelApertureRectangularCosinePedestal
==============================================

.. py:class:: IAntennaModelApertureRectangularCosinePedestal

   object
   
   Provide access to the properties and methods defining a rectangular cosine pedestal aperture antenna model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute_mainlobe_gain`
            * - :py:meth:`~mainlobe_gain`
            * - :py:meth:`~backlobe_gain`
            * - :py:meth:`~efficiency`
            * - :py:meth:`~use_backlobe_as_mainlobe_atten`
            * - :py:meth:`~input_type`
            * - :py:meth:`~x_dimension`
            * - :py:meth:`~y_dimension`
            * - :py:meth:`~x_beamwidth`
            * - :py:meth:`~y_beamwidth`
            * - :py:meth:`~pedestal_level`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelApertureRectangularCosinePedestal


Property detail
---------------

.. py:property:: compute_mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosinePedestal.compute_mainlobe_gain
    :type: bool

    Gets or sets the option for computing the mainlobe gain.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosinePedestal.mainlobe_gain
    :type: float

    Gets or sets the mainlobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosinePedestal.backlobe_gain
    :type: float

    Gets or sets the backlobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosinePedestal.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosinePedestal.use_backlobe_as_mainlobe_atten
    :type: bool

    Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosinePedestal.input_type
    :type: RECTANGULAR_APERTURE_INPUT_TYPE

    Gets or sets the input type.

.. py:property:: x_dimension
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosinePedestal.x_dimension
    :type: float

    Gets or sets the x dimension.

.. py:property:: y_dimension
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosinePedestal.y_dimension
    :type: float

    Gets or sets the y dimension.

.. py:property:: x_beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosinePedestal.x_beamwidth
    :type: typing.Any

    Gets or sets the x beamwidth.

.. py:property:: y_beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosinePedestal.y_beamwidth
    :type: typing.Any

    Gets or sets the y beamwidth.

.. py:property:: pedestal_level
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureRectangularCosinePedestal.pedestal_level
    :type: float

    Gets or sets the pedestal level.


