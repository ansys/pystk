IGraphics3DOffset
=================

.. py:class:: IGraphics3DOffset

   object
   
   AgVOOffset used to access the 3D offset attributes.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~rotational`
            * - :py:meth:`~translational`
            * - :py:meth:`~label`
            * - :py:meth:`~attach_point`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DOffset


Property detail
---------------

.. py:property:: rotational
    :canonical: ansys.stk.core.stkobjects.IGraphics3DOffset.rotational
    :type: "IAgVOOffsetRotate"

    Returns the rotational offset attributes.

.. py:property:: translational
    :canonical: ansys.stk.core.stkobjects.IGraphics3DOffset.translational
    :type: "IAgVOOffsetTrans"

    Returns the translational offset attributes.

.. py:property:: label
    :canonical: ansys.stk.core.stkobjects.IGraphics3DOffset.label
    :type: "IAgVOOffsetLabel"

    Returns the label offset attributes.

.. py:property:: attach_point
    :canonical: ansys.stk.core.stkobjects.IGraphics3DOffset.attach_point
    :type: "IAgVOOffsetAttach"

    Returns the attach point offset attributes.


