TransmitterGraphics3D
=====================

.. py:class:: ansys.stk.core.stkobjects.TransmitterGraphics3D

   Bases: 

   Class defining 3D Graphics properties of a Transmitter.

.. py:currentmodule:: TransmitterGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterGraphics3D.vector`
              - Get the transmitter's Vector properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterGraphics3D.show_boresight`
              - Opt whether to display boresight graphics for the transmitter's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterGraphics3D.show_contours`
              - Opt whether to display contour graphics for the transmitter's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.TransmitterGraphics3D.volume`
              - Gets the transmitter's antenna volume graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TransmitterGraphics3D


Property detail
---------------

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.TransmitterGraphics3D.vector
    :type: IGraphics3DVector

    Get the transmitter's Vector properties.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.TransmitterGraphics3D.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the transmitter's antenna.

.. py:property:: show_contours
    :canonical: ansys.stk.core.stkobjects.TransmitterGraphics3D.show_contours
    :type: bool

    Opt whether to display contour graphics for the transmitter's antenna.

.. py:property:: volume
    :canonical: ansys.stk.core.stkobjects.TransmitterGraphics3D.volume
    :type: IAntennaVolumeGraphics

    Gets the transmitter's antenna volume graphics interface.


