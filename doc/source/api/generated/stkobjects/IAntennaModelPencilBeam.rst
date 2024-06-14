IAntennaModelPencilBeam
=======================

.. py:class:: IAntennaModelPencilBeam

   object
   
   Provide access to the properties and methods defining a pencil beam antenna model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~mainlobe_gain`
            * - :py:meth:`~sidelobe_gain`
            * - :py:meth:`~beamwidth`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaModelPencilBeam


Property detail
---------------

.. py:property:: mainlobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPencilBeam.mainlobe_gain
    :type: float

    Gets or sets the mainlobe gain.

.. py:property:: sidelobe_gain
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPencilBeam.sidelobe_gain
    :type: float

    Gets or sets the sidelobe gain.

.. py:property:: beamwidth
    :canonical: ansys.stk.core.stkobjects.IAntennaModelPencilBeam.beamwidth
    :type: typing.Any

    Gets the computed beamwidth.


