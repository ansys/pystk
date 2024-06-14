
The ``STKXLib`` module
======================


.. py::module:: ansys.stk.core.stkx


Summary
-------

.. tab-set::
    .. tab-items:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~ISTKXSSLCertificateErrorEventArgs`
              - Provide information about an SSL certificate that is expired or invalid.

            * - :pyclass:`~ISTKXConControlQuitReceivedEventArgs`
              - Arguments for the OnConControlQuitReceived event.

            * - :pyclass:`~IPickInfoData`
              - Mouse pick details.

            * - :pyclass:`~IRubberBandPickInfoData`
              - Rubber-band mouse pick result.

            * - :pyclass:`~ISTKXApplication`
              - STK X Application object.

            * - :pyclass:`~IDataObject`
              - IAgDataObject is used for OLE drag and drop operations.

            * - :pyclass:`~IObjPathCollection`
              - Collection of object paths.

            * - :pyclass:`~IDrawElem`
              - Draw element.

            * - :pyclass:`~IDrawElemRect`
              - Define a rectangle in control coordinates.

            * - :pyclass:`~IDrawElemCollection`
              - Collection of elements to draw on the control.

            * - :pyclass:`~IWinProjectionPosition`
              - Projected window position detail.

            * - :pyclass:`~IDrawElemLine`
              - Define a line in control coordinates.

            * - :pyclass:`~IExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :pyclass:`~IExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :pyclass:`~IUiAxGraphics3DCntrl`
              - AGI Globe control.

            * - :pyclass:`~IUiAx2DCntrl`
              - AGI Map control.

            * - :pyclass:`~ISTKXApplicationPartnerAccess`
              - Access to the application object model for business partners.

            * - :pyclass:`~IDataObjectFiles`
              - Collection of file names.

            * - :pyclass:`~IUiAxGraphics2DAnalysisCntrl`
              - AGI Gfx Analysis control.

    
    .. tab-items:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~ExecCmdResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :pyclass:`~ExecMultiCmdResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :pyclass:`~UiAxGraphics3DCntrl`
              - AGI Globe control.

            * - :pyclass:`~UiAx2DCntrl`
              - AGI Map control.

            * - :pyclass:`~PickInfoData`
              - Single mouse pick result.

            * - :pyclass:`~STKXApplication`
              - STK X Application object.

            * - :pyclass:`~STKXApplicationPartnerAccess`
              - STK X Application Partner Access object.

            * - :pyclass:`~DataObject`
              - Data Object for OLE drag & drop operations.

            * - :pyclass:`~DataObjectFiles`
              - Collection of files for OLE drag & drop operations.

            * - :pyclass:`~RubberBandPickInfoData`
              - Rubber-band mouse pick result.

            * - :pyclass:`~ObjPathCollection`
              - Collection of object paths.

            * - :pyclass:`~DrawElemRect`
              - Define a rectangle in window coordinates.

            * - :pyclass:`~DrawElemCollection`
              - Collection of elements to draw on the control.

            * - :pyclass:`~Draw2DElemRect`
              - Define a rectangle in window coordinates for map control.

            * - :pyclass:`~Draw2DElemCollection`
              - Collection of elements to draw on map control.

            * - :pyclass:`~UiAxGraphics2DAnalysisCntrl`
              - AGI Graphics Analysis Control.

            * - :pyclass:`~WinProjectionPosition`
              - Projected window position result.

            * - :pyclass:`~DrawElemLine`
              - Define a line in window coordinates.

            * - :pyclass:`~STKXSSLCertificateErrorEventArgs`
              - Provide information about an SSL certificate that is expired or invalid.

            * - :pyclass:`~STKXConControlQuitReceivedEventArgs`
              - Arguments for the OnConControlQuitReceived event.


    .. tab-items:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~LOG_MSG_TYPE`
              - Log message types.

            * - :pyclass:`~LOG_MSG_DISP_ID`
              - Log message destination options.

            * - :pyclass:`~LINE_STYLE`
              - Line Style.

            * - :pyclass:`~EXEC_MULTI_CMD_RESULT_ACTION`
              - Enumeration defines a set of actions when an error occurs while executing a command batch.

            * - :pyclass:`~SHIFT_VALUES`
              - State of the Shift/Ctrl/Alt keys.

            * - :pyclass:`~BUTTON_VALUES`
              - Numeric value of the mouse button pressed.

            * - :pyclass:`~OLE_DROP_MODE`
              - Specify how to handle OLE drop operations.

            * - :pyclass:`~MOUSE_MODE`
              - Mouse modes.

            * - :pyclass:`~LOGGING_MODE`
              - Specify the state of the log file.

            * - :pyclass:`~GRAPHICS_2D_ANALYSIS_MODE`
              - Specify the mode of Gfx Analysis Control.

            * - :pyclass:`~GRAPHICS_2D_DRAW_COORDS`
              - Specify the draw coordinates for Map Control.

            * - :pyclass:`~SHOW_PROGRESS_IMAGE`
              - Specify to show progress image.

            * - :pyclass:`~FEATURE_CODES`
              - The enumeration values are used to check availability of a given feature.

            * - :pyclass:`~PROGRESS_IMAGE_X_ORIGIN`
              - Specify to align progress image X origin.

            * - :pyclass:`~PROGRESS_IMAGE_Y_ORIGIN`
              - Specify to align progress image Y origin.


    .. tab-items:: Constants

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
              - 

            * - :pyclass:`~constant`
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

    --> ISTKXSSLCertificateErrorEventArgs<ISTKXSSLCertificateErrorEventArgs>
    --> ISTKXConControlQuitReceivedEventArgs<ISTKXConControlQuitReceivedEventArgs>
    --> IPickInfoData<IPickInfoData>
    --> IRubberBandPickInfoData<IRubberBandPickInfoData>
    --> ISTKXApplication<ISTKXApplication>
    --> IDataObject<IDataObject>
    --> IObjPathCollection<IObjPathCollection>
    --> IDrawElem<IDrawElem>
    --> IDrawElemRect<IDrawElemRect>
    --> IDrawElemCollection<IDrawElemCollection>
    --> IWinProjectionPosition<IWinProjectionPosition>
    --> IDrawElemLine<IDrawElemLine>
    --> IExecCmdResult<IExecCmdResult>
    --> IExecMultiCmdResult<IExecMultiCmdResult>
    --> IUiAxGraphics3DCntrl<IUiAxGraphics3DCntrl>
    --> IUiAx2DCntrl<IUiAx2DCntrl>
    --> ISTKXApplicationPartnerAccess<ISTKXApplicationPartnerAccess>
    --> IDataObjectFiles<IDataObjectFiles>
    --> IUiAxGraphics2DAnalysisCntrl<IUiAxGraphics2DAnalysisCntrl>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> ExecCmdResult<>
    --> ExecMultiCmdResult<>
    --> UiAxGraphics3DCntrl<>
    --> UiAx2DCntrl<>
    --> PickInfoData<>
    --> STKXApplication<>
    --> STKXApplicationPartnerAccess<>
    --> DataObject<>
    --> DataObjectFiles<>
    --> RubberBandPickInfoData<>
    --> ObjPathCollection<>
    --> DrawElemRect<>
    --> DrawElemCollection<>
    --> Draw2DElemRect<>
    --> Draw2DElemCollection<>
    --> UiAxGraphics2DAnalysisCntrl<>
    --> WinProjectionPosition<>
    --> DrawElemLine<>
    --> STKXSSLCertificateErrorEventArgs<>
    --> STKXConControlQuitReceivedEventArgs<>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ LOG_MSG_TYPE<LOG_MSG_TYPE>
    ≔ LOG_MSG_DISP_ID<LOG_MSG_DISP_ID>
    ≔ LINE_STYLE<LINE_STYLE>
    ≔ EXEC_MULTI_CMD_RESULT_ACTION<EXEC_MULTI_CMD_RESULT_ACTION>
    ≔ SHIFT_VALUES<SHIFT_VALUES>
    ≔ BUTTON_VALUES<BUTTON_VALUES>
    ≔ OLE_DROP_MODE<OLE_DROP_MODE>
    ≔ MOUSE_MODE<MOUSE_MODE>
    ≔ LOGGING_MODE<LOGGING_MODE>
    ≔ GRAPHICS_2D_ANALYSIS_MODE<GRAPHICS_2D_ANALYSIS_MODE>
    ≔ GRAPHICS_2D_DRAW_COORDS<GRAPHICS_2D_DRAW_COORDS>
    ≔ SHOW_PROGRESS_IMAGE<SHOW_PROGRESS_IMAGE>
    ≔ FEATURE_CODES<FEATURE_CODES>
    ≔ PROGRESS_IMAGE_X_ORIGIN<PROGRESS_IMAGE_X_ORIGIN>
    ≔ PROGRESS_IMAGE_Y_ORIGIN<PROGRESS_IMAGE_Y_ORIGIN>

