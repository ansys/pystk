
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
        

            * - :py:class:`~ansys.stk.core.stkx.IDrawElement`
              - Draw element.

            * - :py:class:`~ansys.stk.core.stkx.IDrawElementCollection`
              - Collection of elements to draw on the control.

            * - :py:class:`~ansys.stk.core.stkx.IDrawElementRect`
              - Define a rectangle in control coordinates.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkx.DataObject`
              - Data Object for OLE drag & drop operations.

            * - :py:class:`~ansys.stk.core.stkx.DataObjectFiles`
              - Collection of files for OLE drag & drop operations.

            * - :py:class:`~ansys.stk.core.stkx.Draw2DElemCollection`
              - Collection of elements to draw on map control.

            * - :py:class:`~ansys.stk.core.stkx.Draw2DElemRect`
              - Define a rectangle in window coordinates for map control.

            * - :py:class:`~ansys.stk.core.stkx.DrawElementCollection`
              - Collection of elements to draw on the control.

            * - :py:class:`~ansys.stk.core.stkx.DrawElementLine`
              - Define a line in window coordinates.

            * - :py:class:`~ansys.stk.core.stkx.DrawElementRect`
              - Define a rectangle in window coordinates.

            * - :py:class:`~ansys.stk.core.stkx.Graphics2DControlBase`
              - AGI Map control.

            * - :py:class:`~ansys.stk.core.stkx.Graphics3DControlBase`
              - AGI Globe control.

            * - :py:class:`~ansys.stk.core.stkx.GraphicsAnalysisControlBase`
              - AGI Graphics Analysis Control.

            * - :py:class:`~ansys.stk.core.stkx.ObjectPathCollection`
              - Collection of object paths.

            * - :py:class:`~ansys.stk.core.stkx.PickInfoData`
              - Single mouse pick result.

            * - :py:class:`~ansys.stk.core.stkx.RubberBandPickInfoData`
              - Rubber-band mouse pick result.

            * - :py:class:`~ansys.stk.core.stkx.STKXApplication`
              - STK X Application object.

            * - :py:class:`~ansys.stk.core.stkx.STKXApplicationPartnerAccess`
              - STK X Application Partner Access object.

            * - :py:class:`~ansys.stk.core.stkx.STKXConControlQuitReceivedEventArgs`
              - Arguments for the OnConControlQuitReceived event.

            * - :py:class:`~ansys.stk.core.stkx.STKXSSLCertificateErrorEventArgs`
              - Provide information about an SSL certificate that is expired or invalid.

            * - :py:class:`~ansys.stk.core.stkx.WindowProjectionPosition`
              - Projected window position result.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.stkx.ButtonValues`
              - Numeric value of the mouse button pressed.

            * - :py:class:`~ansys.stk.core.stkx.FeatureCodes`
              - The enumeration values are used to check availability of a given feature.

            * - :py:class:`~ansys.stk.core.stkx.Graphics2DAnalysisMode`
              - Specify the mode of Gfx Analysis Control.

            * - :py:class:`~ansys.stk.core.stkx.Graphics2DDrawCoordinates`
              - Specify the draw coordinates for Map Control.

            * - :py:class:`~ansys.stk.core.stkx.LoggingMode`
              - Specify the state of the log file.

            * - :py:class:`~ansys.stk.core.stkx.MouseMode`
              - Mouse modes.

            * - :py:class:`~ansys.stk.core.stkx.OLEDropMode`
              - Specify how to handle OLE drop operations.

            * - :py:class:`~ansys.stk.core.stkx.ProgressImageXOrigin`
              - Specify to align progress image X origin.

            * - :py:class:`~ansys.stk.core.stkx.ProgressImageYOrigin`
              - Specify to align progress image Y origin.

            * - :py:class:`~ansys.stk.core.stkx.ShiftValues`
              - State of the Shift/Ctrl/Alt keys.

            * - :py:class:`~ansys.stk.core.stkx.ShowProgressImage`
              - Specify to show progress image.



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

     IDrawElement<stkx/IDrawElement>
     IDrawElementCollection<stkx/IDrawElementCollection>
     IDrawElementRect<stkx/IDrawElementRect>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     DataObject<stkx/DataObject>
     DataObjectFiles<stkx/DataObjectFiles>
     Draw2DElemCollection<stkx/Draw2DElemCollection>
     Draw2DElemRect<stkx/Draw2DElemRect>
     DrawElementCollection<stkx/DrawElementCollection>
     DrawElementLine<stkx/DrawElementLine>
     DrawElementRect<stkx/DrawElementRect>
     Graphics2DControlBase<stkx/Graphics2DControlBase>
     Graphics3DControlBase<stkx/Graphics3DControlBase>
     GraphicsAnalysisControlBase<stkx/GraphicsAnalysisControlBase>
     ObjectPathCollection<stkx/ObjectPathCollection>
     PickInfoData<stkx/PickInfoData>
     RubberBandPickInfoData<stkx/RubberBandPickInfoData>
     STKXApplication<stkx/STKXApplication>
     STKXApplicationPartnerAccess<stkx/STKXApplicationPartnerAccess>
     STKXConControlQuitReceivedEventArgs<stkx/STKXConControlQuitReceivedEventArgs>
     STKXSSLCertificateErrorEventArgs<stkx/STKXSSLCertificateErrorEventArgs>
     WindowProjectionPosition<stkx/WindowProjectionPosition>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ ButtonValues<stkx/ButtonValues>
    ≔ FeatureCodes<stkx/FeatureCodes>
    ≔ Graphics2DAnalysisMode<stkx/Graphics2DAnalysisMode>
    ≔ Graphics2DDrawCoordinates<stkx/Graphics2DDrawCoordinates>
    ≔ LoggingMode<stkx/LoggingMode>
    ≔ MouseMode<stkx/MouseMode>
    ≔ OLEDropMode<stkx/OLEDropMode>
    ≔ ProgressImageXOrigin<stkx/ProgressImageXOrigin>
    ≔ ProgressImageYOrigin<stkx/ProgressImageYOrigin>
    ≔ ShiftValues<stkx/ShiftValues>
    ≔ ShowProgressImage<stkx/ShowProgressImage>

