AntennaModelApertureCircularCosinePedestal
==========================================

.. py:class:: ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaModel`, :py:class:`~ansys.stk.core.stkobjects.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.ICloneable`

   Class defining a circular cosine pedestal aperture antenna model.

.. py:currentmodule:: AntennaModelApertureCircularCosinePedestal

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.compute_mainlobe_gain`
              - Gets or sets the option for computing the mainlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.mainlobe_gain`
              - Gets or sets the mainlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.backlobe_gain`
              - Gets or sets the backlobe gain.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.efficiency`
              - Gets or sets the efficiency.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.use_backlobe_as_mainlobe_atten`
              - Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.input_type`
              - Gets or sets the input type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.diameter`
              - Gets or sets the diameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.beamwidth`
              - Gets or sets the beamwidth.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.pedestal_level`
              - Gets or sets the pedestal level.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaModelApertureCircularCosinePedestal


Property detail
---------------

.. py:property:: compute_mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.compute_mainlobe_gain
    :type: bool

    Gets or sets the option for computing the mainlobe gain.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.mainlobe_gain
    :type: float

    Gets or sets the mainlobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.backlobe_gain
    :type: float

    Gets or sets the backlobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.efficiency
    :type: float

    Gets or sets the efficiency.

.. py:property:: use_backlobe_as_mainlobe_atten
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.use_backlobe_as_mainlobe_atten
    :type: bool

    Gets or sets the option for using the back lobe gain as a main lobe gain attenuation.

.. py:property:: input_type
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.input_type
    :type: CircularApertureInputType

    Gets or sets the input type.

.. py:property:: diameter
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.diameter
    :type: float

    Gets or sets the diameter.

.. py:property:: beamwidth
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.beamwidth
    :type: typing.Any

    Gets or sets the beamwidth.

.. py:property:: pedestal_level
    :canonical: ansys.stk.core.stkobjects.AntennaModelApertureCircularCosinePedestal.pedestal_level
    :type: float

    Gets or sets the pedestal level.


