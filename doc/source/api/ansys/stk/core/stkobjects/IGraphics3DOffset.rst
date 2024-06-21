IGraphics3DOffset
=================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DOffset

   object
   
   AgVOOffset used to access the 3D offset attributes.

.. py:currentmodule:: IGraphics3DOffset

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DOffset.rotational`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DOffset.translational`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DOffset.label`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DOffset.attach_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DOffset


Property detail
---------------

.. py:property:: rotational
    :canonical: ansys.stk.core.stkobjects.IGraphics3DOffset.rotational
    :type: IGraphics3DOffsetRotate

    Returns the rotational offset attributes.

.. py:property:: translational
    :canonical: ansys.stk.core.stkobjects.IGraphics3DOffset.translational
    :type: IGraphics3DOffsetTransformation

    Returns the translational offset attributes.

.. py:property:: label
    :canonical: ansys.stk.core.stkobjects.IGraphics3DOffset.label
    :type: IGraphics3DOffsetLabel

    Returns the label offset attributes.

.. py:property:: attach_point
    :canonical: ansys.stk.core.stkobjects.IGraphics3DOffset.attach_point
    :type: IGraphics3DOffsetAttach

    Returns the attach point offset attributes.


