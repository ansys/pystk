IGraphics3DModelItem
====================

.. py:class:: IGraphics3DModelItem

   object
   
   AgVOModelItem used to access the Model Item in the ModelCollection.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~switch_time`
            * - :py:meth:`~graphics_3d_model_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DModelItem


Property detail
---------------

.. py:property:: switch_time
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelItem.switch_time
    :type: typing.Any

    The time that the display switches between models. Uses DateFormat Dimension.

.. py:property:: graphics_3d_model_file
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelItem.graphics_3d_model_file
    :type: IAgVOModelFile

    Interface to specify model's file.


