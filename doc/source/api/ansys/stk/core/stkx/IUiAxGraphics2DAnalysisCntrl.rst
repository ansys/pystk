IUiAxGraphics2DAnalysisCntrl
============================

.. py:class:: IUiAxGraphics2DAnalysisCntrl

   object
   
   AGI Gfx Analysis control.

.. py:currentmodule:: ansys.stk.core.stkx

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~picture_put_reference`
              - Set a reference to the splash logo graphic to be displayed in the control.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~back_color`
            * - :py:meth:`~picture`
            * - :py:meth:`~no_logo`
            * - :py:meth:`~vendor_id`
            * - :py:meth:`~ready_state`
            * - :py:meth:`~application`
            * - :py:meth:`~control_mode`
            * - :py:meth:`~picture_from_file`
            * - :py:meth:`~win_id`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import IUiAxGraphics2DAnalysisCntrl


Property detail
---------------

.. py:property:: back_color
    :canonical: ansys.stk.core.stkx.IUiAxGraphics2DAnalysisCntrl.back_color
    :type: agcolor.Color

    The background color of the control.

.. py:property:: picture
    :canonical: ansys.stk.core.stkx.IUiAxGraphics2DAnalysisCntrl.picture
    :type: IPictureDisp

    The splash logo graphic to be displayed in the control.

.. py:property:: no_logo
    :canonical: ansys.stk.core.stkx.IUiAxGraphics2DAnalysisCntrl.no_logo
    :type: bool

    If true, the splash logo is not shown.

.. py:property:: vendor_id
    :canonical: ansys.stk.core.stkx.IUiAxGraphics2DAnalysisCntrl.vendor_id
    :type: str

    This property is deprecated. The identifier of the vendor.

.. py:property:: ready_state
    :canonical: ansys.stk.core.stkx.IUiAxGraphics2DAnalysisCntrl.ready_state
    :type: int

    Returns the ready state of the control.

.. py:property:: application
    :canonical: ansys.stk.core.stkx.IUiAxGraphics2DAnalysisCntrl.application
    :type: "IAgSTKXApplication"

    Reference to the STK X application object.

.. py:property:: control_mode
    :canonical: ansys.stk.core.stkx.IUiAxGraphics2DAnalysisCntrl.control_mode
    :type: "GRAPHICS_2D_ANALYSIS_MODE"

    The Graphics control mode.

.. py:property:: picture_from_file
    :canonical: ansys.stk.core.stkx.IUiAxGraphics2DAnalysisCntrl.picture_from_file
    :type: str

    Gets or sets the splash logo graphic file to be displayed in the control.

.. py:property:: win_id
    :canonical: ansys.stk.core.stkx.IUiAxGraphics2DAnalysisCntrl.win_id
    :type: int

    Window identifier (for Connect commands).


Method detail
-------------




.. py:method:: picture_put_reference(self, pPicture:IPictureDisp) -> None

    Set a reference to the splash logo graphic to be displayed in the control.

    :Parameters:

    **pPicture** : :obj:`~IPictureDisp`

    :Returns:

        :obj:`~None`














