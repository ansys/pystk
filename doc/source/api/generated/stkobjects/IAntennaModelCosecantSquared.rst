IAntennaModelCosecantSquared
============================

.. py:class:: IAntennaModelCosecantSquared

   object
   
   Provide access to the properties and methods defining a cosecant squared antenna model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~sidelobe_type`
            * - :py:meth:`~cutoff_angle`
            * - :py:meth:`~azimuth_beamwidth`
            * - :py:meth:`~mainlobe_gain`
            * - :py:meth:`~backlobe_gain`
            * - :py:meth:`~efficiency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelCosecantSquared


Property detail
---------------

.. py:property:: sidelobe_type
    :canonical: ansys.stk.core.stkobjects.IAntennaModelCosecantSquared.sidelobe_type
    :type: "ANTENNA_MODEL_COSECANT_SQUARED_SIDELOBE_TYPE"

    Gets the Cosecant Squared antenna sidelobe type enumeration.

.. py:property:: cutoff_angle
    :canonical: ansys.stk.core.stkobjects.IAntennaModelCosecantSquared.cutoff_angle
    :type: typing.Any

    Gets or sets the cutoff angle.

.. py:property:: azimuth_beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelCosecantSquared.azimuth_beamwidth
    :type: typing.Any

    Gets or sets the azimuth beamwidth.

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelCosecantSquared.mainlobe_gain
    :type: float

    Gets or sets the mainlobe gain.

.. py:property:: backlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelCosecantSquared.backlobe_gain
    :type: float

    Gets or sets the sidelobe gain.

.. py:property:: efficiency
    :canonical: ansys.stk.core.stkobjects.IAntennaModelCosecantSquared.efficiency
    :type: float

    Gets or sets the efficiency.


