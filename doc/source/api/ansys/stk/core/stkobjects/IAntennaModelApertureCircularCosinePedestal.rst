IAntennaModelApertureCircularCosinePedestal
===========================================

.. py:class:: IAntennaModelApertureCircularCosinePedestal

   object
   
   Provide access to the properties and methods defining a circular cosine pedestal aperture antenna model.

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
            * - :py:meth:`~diameter`
            * - :py:meth:`~beamwidth`
            * - :py:meth:`~pedestal_level`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelApertureCircularCosinePedestal


Property detail
---------------

.. py:property:: compute_mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosinePedestal.compute_mainlobe_gain
    :type: bool

    Gets or sets the option for computing the mainlobe gain.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosinePedestal.mainlobe_gain
    :type: float

    Gets or sets the mainlobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosinePedestal.backlobe_gain
    :type: float

    Gets or sets the backlobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosinePedestal.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosinePedestal.use_backlobe_as_mainlobe_atten
    :type: bool

    Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosinePedestal.input_type
    :type: CIRCULAR_APERTURE_INPUT_TYPE

    Gets or sets the input type.

.. py:property:: diameter
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosinePedestal.diameter
    :type: float

    Gets or sets the diameter.

.. py:property:: beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosinePedestal.beamwidth
    :type: typing.Any

    Gets or sets the beamwidth.

.. py:property:: pedestal_level
    :canonical: ansys.stk.core.stkobjects.IAntennaModelApertureCircularCosinePedestal.pedestal_level
    :type: float

    Gets or sets the pedestal level.


