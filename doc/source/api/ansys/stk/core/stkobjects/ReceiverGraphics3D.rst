ReceiverGraphics3D
==================

.. py:class:: ansys.stk.core.stkobjects.ReceiverGraphics3D

   Class defining 3D Graphics properties of a Receiver.

.. py:currentmodule:: ReceiverGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverGraphics3D.show_boresight`
              - Opt whether to display boresight graphics for the receiver's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverGraphics3D.show_contours`
              - Opt whether to display contour graphics for the receiver's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverGraphics3D.vector`
              - Get the receiver's Vector properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.ReceiverGraphics3D.volume`
              - Get the receiver's antenna volume graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ReceiverGraphics3D


Property detail
---------------

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.ReceiverGraphics3D.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the receiver's antenna.

.. py:property:: show_contours
    :canonical: ansys.stk.core.stkobjects.ReceiverGraphics3D.show_contours
    :type: bool

    Opt whether to display contour graphics for the receiver's antenna.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.ReceiverGraphics3D.vector
    :type: Graphics3DVector

    Get the receiver's Vector properties.

.. py:property:: volume
    :canonical: ansys.stk.core.stkobjects.ReceiverGraphics3D.volume
    :type: AntennaVolumeGraphics

    Get the receiver's antenna volume graphics interface.


