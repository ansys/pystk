GraphicsAnalysisControlBase
===========================

.. py:class:: ansys.stk.core.stkx.GraphicsAnalysisControlBase

   AGI Graphics Analysis Control.

.. py:currentmodule:: GraphicsAnalysisControlBase

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.GraphicsAnalysisControlBase.picture_put_reference`
              - Set a reference to the splash logo graphic to be displayed in the control.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.GraphicsAnalysisControlBase.application`
              - Reference to the STK X application object.
            * - :py:attr:`~ansys.stk.core.stkx.GraphicsAnalysisControlBase.back_color`
              - The background color of the control.
            * - :py:attr:`~ansys.stk.core.stkx.GraphicsAnalysisControlBase.control_mode`
              - The Graphics control mode.
            * - :py:attr:`~ansys.stk.core.stkx.GraphicsAnalysisControlBase.no_logo`
              - If true, the splash logo is not shown.
            * - :py:attr:`~ansys.stk.core.stkx.GraphicsAnalysisControlBase.picture`
              - The splash logo graphic to be displayed in the control.
            * - :py:attr:`~ansys.stk.core.stkx.GraphicsAnalysisControlBase.picture_from_file`
              - Get or set the splash logo graphic file to be displayed in the control.
            * - :py:attr:`~ansys.stk.core.stkx.GraphicsAnalysisControlBase.ready_state`
              - Return the ready state of the control.
            * - :py:attr:`~ansys.stk.core.stkx.GraphicsAnalysisControlBase.vendor_id`
              - Do not use this property, as it is deprecated. The identifier of the vendor.
            * - :py:attr:`~ansys.stk.core.stkx.GraphicsAnalysisControlBase.window_id`
              - Window identifier (for Connect commands).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import GraphicsAnalysisControlBase


Property detail
---------------

.. py:property:: application
    :canonical: ansys.stk.core.stkx.GraphicsAnalysisControlBase.application
    :type: STKXApplication

    Reference to the STK X application object.

.. py:property:: back_color
    :canonical: ansys.stk.core.stkx.GraphicsAnalysisControlBase.back_color
    :type: Color

    The background color of the control.

.. py:property:: control_mode
    :canonical: ansys.stk.core.stkx.GraphicsAnalysisControlBase.control_mode
    :type: Graphics2DAnalysisMode

    The Graphics control mode.

.. py:property:: no_logo
    :canonical: ansys.stk.core.stkx.GraphicsAnalysisControlBase.no_logo
    :type: bool

    If true, the splash logo is not shown.

.. py:property:: picture
    :canonical: ansys.stk.core.stkx.GraphicsAnalysisControlBase.picture
    :type: IPictureDisp

    The splash logo graphic to be displayed in the control.

.. py:property:: picture_from_file
    :canonical: ansys.stk.core.stkx.GraphicsAnalysisControlBase.picture_from_file
    :type: str

    Get or set the splash logo graphic file to be displayed in the control.

.. py:property:: ready_state
    :canonical: ansys.stk.core.stkx.GraphicsAnalysisControlBase.ready_state
    :type: int

    Return the ready state of the control.

.. py:property:: vendor_id
    :canonical: ansys.stk.core.stkx.GraphicsAnalysisControlBase.vendor_id
    :type: str

    Do not use this property, as it is deprecated. The identifier of the vendor.

.. py:property:: window_id
    :canonical: ansys.stk.core.stkx.GraphicsAnalysisControlBase.window_id
    :type: int

    Window identifier (for Connect commands).


Method detail
-------------












.. py:method:: picture_put_reference(self, picture: IPictureDisp) -> None
    :canonical: ansys.stk.core.stkx.GraphicsAnalysisControlBase.picture_put_reference

    Set a reference to the splash logo graphic to be displayed in the control.

    :Parameters:

        **picture** : :obj:`~IPictureDisp`


    :Returns:

        :obj:`~None`






