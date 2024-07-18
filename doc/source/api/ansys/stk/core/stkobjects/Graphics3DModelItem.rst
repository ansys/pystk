Graphics3DModelItem
===================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DModelItem

   Bases: 

   Class defining selection and display of 3D models.

.. py:currentmodule:: Graphics3DModelItem

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelItem.switch_time`
              - The time that the display switches between models. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelItem.graphics_3d_model_file`
              - Interface to specify model's file.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DModelItem


Property detail
---------------

.. py:property:: switch_time
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelItem.switch_time
    :type: typing.Any

    The time that the display switches between models. Uses DateFormat Dimension.

.. py:property:: graphics_3d_model_file
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelItem.graphics_3d_model_file
    :type: IGraphics3DModelFile

    Interface to specify model's file.


