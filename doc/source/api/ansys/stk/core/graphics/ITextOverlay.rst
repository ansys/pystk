ITextOverlay
============

.. py:class:: ITextOverlay

   object
   
   A rectangular overlay that contains text.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~text`
            * - :py:meth:`~outline_color`
            * - :py:meth:`~font`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITextOverlay


Property detail
---------------

.. py:property:: text
    :canonical: ansys.stk.core.graphics.ITextOverlay.text
    :type: str

    Sets the Text to be rendered to an overlay. Newline characters ('\n') will mark the start of the next line in the text.

.. py:property:: outline_color
    :canonical: ansys.stk.core.graphics.ITextOverlay.outline_color
    :type: agcolor.Color

    Gets or sets the text's outline color.

.. py:property:: font
    :canonical: ansys.stk.core.graphics.ITextOverlay.font
    :type: IAgStkGraphicsGraphicsFont

    Get the graphics font used to style the text.


