ITransmitterGraphics3D
======================

.. py:class:: ITransmitterGraphics3D

   object
   
   IAgTransmitterVO Interface for a transmitter's 3D Graphics properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~vector`
            * - :py:meth:`~show_boresight`
            * - :py:meth:`~show_contours`
            * - :py:meth:`~volume`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITransmitterGraphics3D


Property detail
---------------

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.ITransmitterGraphics3D.vector
    :type: IAgVOVector

    Get the transmitter's Vector properties.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.ITransmitterGraphics3D.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the transmitter's antenna.

.. py:property:: show_contours
    :canonical: ansys.stk.core.stkobjects.ITransmitterGraphics3D.show_contours
    :type: bool

    Opt whether to display contour graphics for the transmitter's antenna.

.. py:property:: volume
    :canonical: ansys.stk.core.stkobjects.ITransmitterGraphics3D.volume
    :type: IAgAntennaVolumeGraphics

    Gets the transmitter's antenna volume graphics interface.


