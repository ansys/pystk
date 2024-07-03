ITextOverlay
============

.. py:class:: ansys.stk.core.graphics.ITextOverlay

   object
   
   A rectangular overlay that contains text.

.. py:currentmodule:: ITextOverlay

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITextOverlay.text`
              - Sets the Text to be rendered to an overlay. Newline characters ('\n') will mark the start of the next line in the text.
            * - :py:attr:`~ansys.stk.core.graphics.ITextOverlay.outline_color`
              - Gets or sets the text's outline color.
            * - :py:attr:`~ansys.stk.core.graphics.ITextOverlay.font`
              - Get the graphics font used to style the text.


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
    :type: IGraphicsFont

    Get the graphics font used to style the text.


