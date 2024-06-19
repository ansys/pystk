IScenario3dFont
===============

.. py:class:: IScenario3dFont

   object
   
   IAgSc3dFont Interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_font_available`
              - Return whether the specified font is installed in the system.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~point_size`
            * - :py:meth:`~bold`
            * - :py:meth:`~italic`
            * - :py:meth:`~available_fonts`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScenario3dFont


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IScenario3dFont.name
    :type: str

    Gets or sets the font name.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.IScenario3dFont.point_size
    :type: SCENARIO_3D_POINT_SIZE

    Font size in points.

.. py:property:: bold
    :canonical: ansys.stk.core.stkobjects.IScenario3dFont.bold
    :type: bool

    Specify whether the font is bold.

.. py:property:: italic
    :canonical: ansys.stk.core.stkobjects.IScenario3dFont.italic
    :type: bool

    Specify whether the font is italic.

.. py:property:: available_fonts
    :canonical: ansys.stk.core.stkobjects.IScenario3dFont.available_fonts
    :type: list

    Names of fonts installed in the system.


Method detail
-------------










.. py:method:: is_font_available(self, name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IScenario3dFont.is_font_available

    Return whether the specified font is installed in the system.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`

