
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
        

            * - :py:class:`~ISTKXSSLCertificateErrorEventArgs`
              - Provide information about an SSL certificate that is expired or invalid.

            * - :py:class:`~ISTKXConControlQuitReceivedEventArgs`
              - Arguments for the OnConControlQuitReceived event.

            * - :py:class:`~IPickInfoData`
              - Mouse pick details.

            * - :py:class:`~IRubberBandPickInfoData`
              - Rubber-band mouse pick result.

            * - :py:class:`~ISTKXApplication`
              - STK X Application object.

            * - :py:class:`~IDataObject`
              - IAgDataObject is used for OLE drag and drop operations.

            * - :py:class:`~IObjPathCollection`
              - Collection of object paths.

            * - :py:class:`~IDrawElem`
              - Draw element.

            * - :py:class:`~IDrawElemRect`
              - Define a rectangle in control coordinates.

            * - :py:class:`~IDrawElemCollection`
              - Collection of elements to draw on the control.

            * - :py:class:`~IWinProjectionPosition`
              - Projected window position detail.

            * - :py:class:`~IDrawElemLine`
              - Define a line in control coordinates.

            * - :py:class:`~IExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :py:class:`~IExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :py:class:`~IUiAxGraphics3DCntrl`
              - AGI Globe control.

            * - :py:class:`~IUiAx2DCntrl`
              - AGI Map control.

            * - :py:class:`~ISTKXApplicationPartnerAccess`
              - Access to the application object model for business partners.

            * - :py:class:`~IDataObjectFiles`
              - Collection of file names.

            * - :py:class:`~IUiAxGraphics2DAnalysisCntrl`
              - AGI Gfx Analysis control.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :py:class:`~ExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :py:class:`~UiAxGraphics3DCntrl`
              - AGI Globe control.

            * - :py:class:`~UiAx2DCntrl`
              - AGI Map control.

            * - :py:class:`~PickInfoData`
              - Single mouse pick result.

            * - :py:class:`~STKXApplication`
              - STK X Application object.

            * - :py:class:`~STKXApplicationPartnerAccess`
              - STK X Application Partner Access object.

            * - :py:class:`~DataObject`
              - Data Object for OLE drag & drop operations.

            * - :py:class:`~DataObjectFiles`
              - Collection of files for OLE drag & drop operations.

            * - :py:class:`~RubberBandPickInfoData`
              - Rubber-band mouse pick result.

            * - :py:class:`~ObjPathCollection`
              - Collection of object paths.

            * - :py:class:`~DrawElemRect`
              - Define a rectangle in window coordinates.

            * - :py:class:`~DrawElemCollection`
              - Collection of elements to draw on the control.

            * - :py:class:`~Draw2DElemRect`
              - Define a rectangle in window coordinates for map control.

            * - :py:class:`~Draw2DElemCollection`
              - Collection of elements to draw on map control.

            * - :py:class:`~UiAxGraphics2DAnalysisCntrl`
              - AGI Graphics Analysis Control.

            * - :py:class:`~WinProjectionPosition`
              - Projected window position result.

            * - :py:class:`~DrawElemLine`
              - Define a line in window coordinates.

            * - :py:class:`~STKXSSLCertificateErrorEventArgs`
              - Provide information about an SSL certificate that is expired or invalid.

            * - :py:class:`~STKXConControlQuitReceivedEventArgs`
              - Arguments for the OnConControlQuitReceived event.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~LOG_MSG_TYPE`
              - Log message types.

            * - :py:class:`~LOG_MSG_DISP_ID`
              - Log message destination options.

            * - :py:class:`~LINE_STYLE`
              - Line Style.

            * - :py:class:`~EXEC_MULTI_CMD_RESULT_ACTION`
              - Enumeration defines a set of actions when an error occurs while executing a command batch.

            * - :py:class:`~SHIFT_VALUES`
              - State of the Shift/Ctrl/Alt keys.

            * - :py:class:`~BUTTON_VALUES`
              - Numeric value of the mouse button pressed.

            * - :py:class:`~OLE_DROP_MODE`
              - Specify how to handle OLE drop operations.

            * - :py:class:`~MOUSE_MODE`
              - Mouse modes.

            * - :py:class:`~LOGGING_MODE`
              - Specify the state of the log file.

            * - :py:class:`~GRAPHICS_2D_ANALYSIS_MODE`
              - Specify the mode of Gfx Analysis Control.

            * - :py:class:`~GRAPHICS_2D_DRAW_COORDS`
              - Specify the draw coordinates for Map Control.

            * - :py:class:`~SHOW_PROGRESS_IMAGE`
              - Specify to show progress image.

            * - :py:class:`~FEATURE_CODES`
              - The enumeration values are used to check availability of a given feature.

            * - :py:class:`~PROGRESS_IMAGE_X_ORIGIN`
              - Specify to align progress image X origin.

            * - :py:class:`~PROGRESS_IMAGE_Y_ORIGIN`
              - Specify to align progress image Y origin.


    .. tab-item:: Constants

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 

            * - :py:class:`~constant`
              - 



Description
-----------

STK X allows developers to add advanced STK 2D, 3D visualization and analytical capabilities to applications.

The top of the STK X object model presents the following creatable components:

  * The Application component interfaces to the STK analytical engine. It can be used by itself (in a GUI-less mode), or through the Application property on the Globe and Map controls.   
The main way to communicate with the engine is to send Connect commands.
Connect is a language for accessing and manipulating STK (see the
ExecuteCommand method).  
The Application object also exposes connection points that you can sink to
receive notification about the state of the STK engine (for instance a
scenario has been loaded; an animation step is performed, etc.).  
Notice that you can instantiate many application objects, but they all refer
to the same unique STK engine.

  * The Globe control enables you to insert a 3D view into your application.  
You can use several Globe controls if you wish to have different views of the
same scenario. By default the STK keyboard and mouse interaction mechanism are
used, but various events are available, allowing your application to implement
specific keyboard and mouse interactions and modes.

  * The Map control can be used to insert a 2D view into your application.  
The Map control gives your application a 2D view of the scenario. You can use
several Map controls if you wish to have different views of the same scenario.
By default the STK keyboard and mouse interaction mechanism are used, but
various events are available, allowing your application to implement specific
keyboard and mouse interactions and modes.

  * The Graphics Analysis control allows you to insert graphics analysis capability into your application. The Graphics Analysis Control can perform various analyses when set in any of the following four analysis modes. 
    * Area Tool 
    * AzElMask Tool 
    * Obscuration Tool 
    * Solar Panel Tool

.

Detail
------

.. py:currentmodule:: ansys.stk.core.stkx


.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    
.. py:data:: constant
    :type: 
    :value: 

    

.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     ISTKXSSLCertificateErrorEventArgs<stkx\ISTKXSSLCertificateErrorEventArgs>
     ISTKXConControlQuitReceivedEventArgs<stkx\ISTKXConControlQuitReceivedEventArgs>
     IPickInfoData<stkx\IPickInfoData>
     IRubberBandPickInfoData<stkx\IRubberBandPickInfoData>
     ISTKXApplication<stkx\ISTKXApplication>
     IDataObject<stkx\IDataObject>
     IObjPathCollection<stkx\IObjPathCollection>
     IDrawElem<stkx\IDrawElem>
     IDrawElemRect<stkx\IDrawElemRect>
     IDrawElemCollection<stkx\IDrawElemCollection>
     IWinProjectionPosition<stkx\IWinProjectionPosition>
     IDrawElemLine<stkx\IDrawElemLine>
     IExecCmdResult<stkx\IExecCmdResult>
     IExecMultiCmdResult<stkx\IExecMultiCmdResult>
     IUiAxGraphics3DCntrl<stkx\IUiAxGraphics3DCntrl>
     IUiAx2DCntrl<stkx\IUiAx2DCntrl>
     ISTKXApplicationPartnerAccess<stkx\ISTKXApplicationPartnerAccess>
     IDataObjectFiles<stkx\IDataObjectFiles>
     IUiAxGraphics2DAnalysisCntrl<stkx\IUiAxGraphics2DAnalysisCntrl>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     ExecCmdResult<stkx\ExecCmdResult>
     ExecMultiCmdResult<stkx\ExecMultiCmdResult>
     UiAxGraphics3DCntrl<stkx\UiAxGraphics3DCntrl>
     UiAx2DCntrl<stkx\UiAx2DCntrl>
     PickInfoData<stkx\PickInfoData>
     STKXApplication<stkx\STKXApplication>
     STKXApplicationPartnerAccess<stkx\STKXApplicationPartnerAccess>
     DataObject<stkx\DataObject>
     DataObjectFiles<stkx\DataObjectFiles>
     RubberBandPickInfoData<stkx\RubberBandPickInfoData>
     ObjPathCollection<stkx\ObjPathCollection>
     DrawElemRect<stkx\DrawElemRect>
     DrawElemCollection<stkx\DrawElemCollection>
     Draw2DElemRect<stkx\Draw2DElemRect>
     Draw2DElemCollection<stkx\Draw2DElemCollection>
     UiAxGraphics2DAnalysisCntrl<stkx\UiAxGraphics2DAnalysisCntrl>
     WinProjectionPosition<stkx\WinProjectionPosition>
     DrawElemLine<stkx\DrawElemLine>
     STKXSSLCertificateErrorEventArgs<stkx\STKXSSLCertificateErrorEventArgs>
     STKXConControlQuitReceivedEventArgs<stkx\STKXConControlQuitReceivedEventArgs>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ LOG_MSG_TYPE<stkx\LOG_MSG_TYPE>
    ≔ LOG_MSG_DISP_ID<stkx\LOG_MSG_DISP_ID>
    ≔ LINE_STYLE<stkx\LINE_STYLE>
    ≔ EXEC_MULTI_CMD_RESULT_ACTION<stkx\EXEC_MULTI_CMD_RESULT_ACTION>
    ≔ SHIFT_VALUES<stkx\SHIFT_VALUES>
    ≔ BUTTON_VALUES<stkx\BUTTON_VALUES>
    ≔ OLE_DROP_MODE<stkx\OLE_DROP_MODE>
    ≔ MOUSE_MODE<stkx\MOUSE_MODE>
    ≔ LOGGING_MODE<stkx\LOGGING_MODE>
    ≔ GRAPHICS_2D_ANALYSIS_MODE<stkx\GRAPHICS_2D_ANALYSIS_MODE>
    ≔ GRAPHICS_2D_DRAW_COORDS<stkx\GRAPHICS_2D_DRAW_COORDS>
    ≔ SHOW_PROGRESS_IMAGE<stkx\SHOW_PROGRESS_IMAGE>
    ≔ FEATURE_CODES<stkx\FEATURE_CODES>
    ≔ PROGRESS_IMAGE_X_ORIGIN<stkx\PROGRESS_IMAGE_X_ORIGIN>
    ≔ PROGRESS_IMAGE_Y_ORIGIN<stkx\PROGRESS_IMAGE_Y_ORIGIN>

