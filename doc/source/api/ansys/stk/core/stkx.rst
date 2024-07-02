
The ``stkx`` module
===================


.. py:module:: ansys.stk.core.stkx


Summary
-------

.. tab-set::

 
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkx.ISTKXSSLCertificateErrorEventArgs`
              - Provide information about an SSL certificate that is expired or invalid.

            * - :py:class:`~ansys.stk.core.stkx.ISTKXConControlQuitReceivedEventArgs`
              - Arguments for the OnConControlQuitReceived event.

            * - :py:class:`~ansys.stk.core.stkx.IPickInfoData`
              - Mouse pick details.

            * - :py:class:`~ansys.stk.core.stkx.IRubberBandPickInfoData`
              - Rubber-band mouse pick result.

            * - :py:class:`~ansys.stk.core.stkx.ISTKXApplication`
              - STK X Application object.

            * - :py:class:`~ansys.stk.core.stkx.IDataObject`
              - IAgDataObject is used for OLE drag and drop operations.

            * - :py:class:`~ansys.stk.core.stkx.IObjPathCollection`
              - Collection of object paths.

            * - :py:class:`~ansys.stk.core.stkx.IDrawElem`
              - Draw element.

            * - :py:class:`~ansys.stk.core.stkx.IDrawElemRect`
              - Define a rectangle in control coordinates.

            * - :py:class:`~ansys.stk.core.stkx.IDrawElemCollection`
              - Collection of elements to draw on the control.

            * - :py:class:`~ansys.stk.core.stkx.IWinProjectionPosition`
              - Projected window position detail.

            * - :py:class:`~ansys.stk.core.stkx.IDrawElemLine`
              - Define a line in control coordinates.

            * - :py:class:`~ansys.stk.core.stkx.IExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :py:class:`~ansys.stk.core.stkx.IExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :py:class:`~ansys.stk.core.stkx.IUiAxGraphics3DCntrl`
              - AGI Globe control.

            * - :py:class:`~ansys.stk.core.stkx.IUiAx2DCntrl`
              - AGI Map control.

            * - :py:class:`~ansys.stk.core.stkx.ISTKXApplicationPartnerAccess`
              - Access to the application object model for business partners.

            * - :py:class:`~ansys.stk.core.stkx.IDataObjectFiles`
              - Collection of file names.

            * - :py:class:`~ansys.stk.core.stkx.IUiAxGraphics2DAnalysisCntrl`
              - AGI Gfx Analysis control.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkx.ExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :py:class:`~ansys.stk.core.stkx.ExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :py:class:`~ansys.stk.core.stkx.UiAxGraphics3DCntrl`
              - AGI Globe control.

            * - :py:class:`~ansys.stk.core.stkx.UiAx2DCntrl`
              - AGI Map control.

            * - :py:class:`~ansys.stk.core.stkx.PickInfoData`
              - Single mouse pick result.

            * - :py:class:`~ansys.stk.core.stkx.STKXApplication`
              - STK X Application object.

            * - :py:class:`~ansys.stk.core.stkx.STKXApplicationPartnerAccess`
              - STK X Application Partner Access object.

            * - :py:class:`~ansys.stk.core.stkx.DataObject`
              - Data Object for OLE drag & drop operations.

            * - :py:class:`~ansys.stk.core.stkx.DataObjectFiles`
              - Collection of files for OLE drag & drop operations.

            * - :py:class:`~ansys.stk.core.stkx.RubberBandPickInfoData`
              - Rubber-band mouse pick result.

            * - :py:class:`~ansys.stk.core.stkx.ObjPathCollection`
              - Collection of object paths.

            * - :py:class:`~ansys.stk.core.stkx.DrawElemRect`
              - Define a rectangle in window coordinates.

            * - :py:class:`~ansys.stk.core.stkx.DrawElemCollection`
              - Collection of elements to draw on the control.

            * - :py:class:`~ansys.stk.core.stkx.Draw2DElemRect`
              - Define a rectangle in window coordinates for map control.

            * - :py:class:`~ansys.stk.core.stkx.Draw2DElemCollection`
              - Collection of elements to draw on map control.

            * - :py:class:`~ansys.stk.core.stkx.UiAxGraphics2DAnalysisCntrl`
              - AGI Graphics Analysis Control.

            * - :py:class:`~ansys.stk.core.stkx.WinProjectionPosition`
              - Projected window position result.

            * - :py:class:`~ansys.stk.core.stkx.DrawElemLine`
              - Define a line in window coordinates.

            * - :py:class:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs`
              - Provide information about an SSL certificate that is expired or invalid.

            * - :py:class:`~ansys.stk.core.stkx.STKXConControlQuitReceivedEventArgs`
              - Arguments for the OnConControlQuitReceived event.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkx.LOG_MSG_TYPE`
              - Log message types.

            * - :py:class:`~ansys.stk.core.stkx.LOG_MSG_DISP_ID`
              - Log message destination options.

            * - :py:class:`~ansys.stk.core.stkx.LINE_STYLE`
              - Line Style.

            * - :py:class:`~ansys.stk.core.stkx.EXEC_MULTI_CMD_RESULT_ACTION`
              - Enumeration defines a set of actions when an error occurs while executing a command batch.

            * - :py:class:`~ansys.stk.core.stkx.SHIFT_VALUES`
              - State of the Shift/Ctrl/Alt keys.

            * - :py:class:`~ansys.stk.core.stkx.BUTTON_VALUES`
              - Numeric value of the mouse button pressed.

            * - :py:class:`~ansys.stk.core.stkx.OLE_DROP_MODE`
              - Specify how to handle OLE drop operations.

            * - :py:class:`~ansys.stk.core.stkx.MOUSE_MODE`
              - Mouse modes.

            * - :py:class:`~ansys.stk.core.stkx.LOGGING_MODE`
              - Specify the state of the log file.

            * - :py:class:`~ansys.stk.core.stkx.GRAPHICS_2D_ANALYSIS_MODE`
              - Specify the mode of Gfx Analysis Control.

            * - :py:class:`~ansys.stk.core.stkx.GRAPHICS_2D_DRAW_COORDS`
              - Specify the draw coordinates for Map Control.

            * - :py:class:`~ansys.stk.core.stkx.SHOW_PROGRESS_IMAGE`
              - Specify to show progress image.

            * - :py:class:`~ansys.stk.core.stkx.FEATURE_CODES`
              - The enumeration values are used to check availability of a given feature.

            * - :py:class:`~ansys.stk.core.stkx.PROGRESS_IMAGE_X_ORIGIN`
              - Specify to align progress image X origin.

            * - :py:class:`~ansys.stk.core.stkx.PROGRESS_IMAGE_Y_ORIGIN`
              - Specify to align progress image Y origin.



Description
-----------

STK X allows developers to add advanced STK 2D, 3D visualization and analytical capabilities to applications.

The top of the STK X object model presents the following creatable components:
The Application component interfaces to the STK analytical engine. It can be used by itself (in a GUI-less mode), or through the Application property on the Globe and Map controls.   
The main way to communicate with the engine is to send Connect commands.
Connect is a language for accessing and manipulating STK (see the
ExecuteCommand method).  
The Application object also exposes connection points that you can sink to
receive notification about the state of the STK engine (for instance a
scenario has been loaded; an animation step is performed, etc.).  
Notice that you can instantiate many application objects, but they all refer
to the same unique STK engine.
The Globe control enables you to insert a 3D view into your application.  
You can use several Globe controls if you wish to have different views of the
same scenario. By default the STK keyboard and mouse interaction mechanism are
used, but various events are available, allowing your application to implement
specific keyboard and mouse interactions and modes.
The Map control can be used to insert a 2D view into your application.  
The Map control gives your application a 2D view of the scenario. You can use
several Map controls if you wish to have different views of the same scenario.
By default the STK keyboard and mouse interaction mechanism are used, but
various events are available, allowing your application to implement specific
keyboard and mouse interactions and modes.
The Graphics Analysis control allows you to insert graphics analysis capability into your application. The Graphics Analysis Control can perform various analyses when set in any of the following four analysis modes. 
Area Tool 
AzElMask Tool 
Obscuration Tool 
Solar Panel Tool

.


.. py:currentmodule:: ansys.stk.core.stkx


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     ISTKXSSLCertificateErrorEventArgs<stkx/ISTKXSSLCertificateErrorEventArgs>
     ISTKXConControlQuitReceivedEventArgs<stkx/ISTKXConControlQuitReceivedEventArgs>
     IPickInfoData<stkx/IPickInfoData>
     IRubberBandPickInfoData<stkx/IRubberBandPickInfoData>
     ISTKXApplication<stkx/ISTKXApplication>
     IDataObject<stkx/IDataObject>
     IObjPathCollection<stkx/IObjPathCollection>
     IDrawElem<stkx/IDrawElem>
     IDrawElemRect<stkx/IDrawElemRect>
     IDrawElemCollection<stkx/IDrawElemCollection>
     IWinProjectionPosition<stkx/IWinProjectionPosition>
     IDrawElemLine<stkx/IDrawElemLine>
     IExecCmdResult<stkx/IExecCmdResult>
     IExecMultiCmdResult<stkx/IExecMultiCmdResult>
     IUiAxGraphics3DCntrl<stkx/IUiAxGraphics3DCntrl>
     IUiAx2DCntrl<stkx/IUiAx2DCntrl>
     ISTKXApplicationPartnerAccess<stkx/ISTKXApplicationPartnerAccess>
     IDataObjectFiles<stkx/IDataObjectFiles>
     IUiAxGraphics2DAnalysisCntrl<stkx/IUiAxGraphics2DAnalysisCntrl>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     ExecCmdResult<stkx/ExecCmdResult>
     ExecMultiCmdResult<stkx/ExecMultiCmdResult>
     UiAxGraphics3DCntrl<stkx/UiAxGraphics3DCntrl>
     UiAx2DCntrl<stkx/UiAx2DCntrl>
     PickInfoData<stkx/PickInfoData>
     STKXApplication<stkx/STKXApplication>
     STKXApplicationPartnerAccess<stkx/STKXApplicationPartnerAccess>
     DataObject<stkx/DataObject>
     DataObjectFiles<stkx/DataObjectFiles>
     RubberBandPickInfoData<stkx/RubberBandPickInfoData>
     ObjPathCollection<stkx/ObjPathCollection>
     DrawElemRect<stkx/DrawElemRect>
     DrawElemCollection<stkx/DrawElemCollection>
     Draw2DElemRect<stkx/Draw2DElemRect>
     Draw2DElemCollection<stkx/Draw2DElemCollection>
     UiAxGraphics2DAnalysisCntrl<stkx/UiAxGraphics2DAnalysisCntrl>
     WinProjectionPosition<stkx/WinProjectionPosition>
     DrawElemLine<stkx/DrawElemLine>
     STKXSSLCertificateErrorEventArgs<stkx/STKXSSLCertificateErrorEventArgs>
     STKXConControlQuitReceivedEventArgs<stkx/STKXConControlQuitReceivedEventArgs>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ LOG_MSG_TYPE<stkx/LOG_MSG_TYPE_enum>
    ≔ LOG_MSG_DISP_ID<stkx/LOG_MSG_DISP_ID_enum>
    ≔ LINE_STYLE<stkx/LINE_STYLE_enum>
    ≔ EXEC_MULTI_CMD_RESULT_ACTION<stkx/EXEC_MULTI_CMD_RESULT_ACTION_enum>
    ≔ SHIFT_VALUES<stkx/SHIFT_VALUES_enum>
    ≔ BUTTON_VALUES<stkx/BUTTON_VALUES_enum>
    ≔ OLE_DROP_MODE<stkx/OLE_DROP_MODE_enum>
    ≔ MOUSE_MODE<stkx/MOUSE_MODE_enum>
    ≔ LOGGING_MODE<stkx/LOGGING_MODE_enum>
    ≔ GRAPHICS_2D_ANALYSIS_MODE<stkx/GRAPHICS_2D_ANALYSIS_MODE_enum>
    ≔ GRAPHICS_2D_DRAW_COORDS<stkx/GRAPHICS_2D_DRAW_COORDS_enum>
    ≔ SHOW_PROGRESS_IMAGE<stkx/SHOW_PROGRESS_IMAGE_enum>
    ≔ FEATURE_CODES<stkx/FEATURE_CODES_enum>
    ≔ PROGRESS_IMAGE_X_ORIGIN<stkx/PROGRESS_IMAGE_X_ORIGIN_enum>
    ≔ PROGRESS_IMAGE_Y_ORIGIN<stkx/PROGRESS_IMAGE_Y_ORIGIN_enum>

