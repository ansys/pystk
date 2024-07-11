IReceiverGraphics3D
===================

.. py:class:: ansys.stk.core.stkobjects.IReceiverGraphics3D

   object
   
   IAgReceiverVO Interface for a receiver's 3D Graphics properties.

.. py:currentmodule:: IReceiverGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverGraphics3D.vector`
              - Get the receiver's Vector properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverGraphics3D.show_boresight`
              - Opt whether to display boresight graphics for the receiver's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverGraphics3D.show_contours`
              - Opt whether to display contour graphics for the receiver's antenna.
            * - :py:attr:`~ansys.stk.core.stkobjects.IReceiverGraphics3D.volume`
              - Gets the receiver's antenna volume graphics interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IReceiverGraphics3D


Property detail
---------------

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.IReceiverGraphics3D.vector
    :type: IGraphics3DVector

    Get the receiver's Vector properties.

.. py:property:: show_boresight
    :canonical: ansys.stk.core.stkobjects.IReceiverGraphics3D.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the receiver's antenna.

.. py:property:: show_contours
    :canonical: ansys.stk.core.stkobjects.IReceiverGraphics3D.show_contours
    :type: bool

    Opt whether to display contour graphics for the receiver's antenna.

.. py:property:: volume
    :canonical: ansys.stk.core.stkobjects.IReceiverGraphics3D.volume
    :type: IAntennaVolumeGraphics

    Gets the receiver's antenna volume graphics interface.


