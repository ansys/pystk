PySTK events
############

In PySTK, events are mechanisms that enable you to respond to specific changes or actions occurring within an STK scenario or the application itself. Events enable you to automate responses to particular triggers, such as when a scenario reaches a certain time, when an object's state changes, or when specific conditions are met during a simulation.

Using events, you can build more dynamic and interactive simulations by attaching custom Python functions or scripts that are executed automatically when predefined conditions are satisfied. For instance, you might want to log specific data whenever a satellite enters a certain region or when a communication link is established between two objects. Events enable you to hook into the STK application's processes and respond in real-time, streamlining workflows and enhancing your scenario's capabilities.

Access events
=============

You can access events directly in applicable parent objects, as displayed in the table below.

[INSERT TABLE]
Event Interface | Parent Object

Events are accessed through the Subscribe() method on the parent object, which returns an event handler subscribed to events on the queried object. You can add or remove Event callbacks in the event handler using the "+=" and "-=" operators; these operators will change the callbacks that will get executed by the event but will not affect whether the handler remains subscribed. The event handler should be unsubscribed using the Unsubscribe() method when event handling is no longer needed. Refer to the following example for using IAgStkObjectRootEvents.

.. code-block:: python

    from agi.stk12.stkengine import STKEngine

    def onScenarioNewCallback(Path:str):
    print(f'Scenario {Path} has been created.')

    stk = STKEngine.StartApplication()
    root = stk.NewObjectRoot()
    stkObjectRootEvents = root.Subscribe()
    stkObjectRootEvents.OnScenarioNew += onScenarioNewCallback
    root.NewScenario('ExampleScenario')
    # callback should be executed now

    # remove the callback from the handler
    stkObjectRootEvents.OnScenarioNew -= onScenarioNewCallback

    # all finished with events, unsubscribe
    stkObjectRootEvents.Unsubscribe()

The STK Desktop application user interface might become unresponsive to user input when Python has event subscribers, and the STK application tries to call back into the Python interpreter to notify of an event. That callback relies on the Windows message loop to be dispatched. To work around this issue, Windows messages need to be dispatched through the Windows message queue. This can be accomplished in different ways depending on the type of Python script that is executing (console or user interface), and on the type of user interface library being used. For instance, if you use the tkinter user interface library, a simple way of accomplishing this with this library is to create a tkinter window while using the desktop application user interface. No action is needed if Python is used only for automation. The following script is an example showing this issue.

.. code-block:: python
    
    from agi.stk12.stkdesktop import STKDesktop
    from agi.stk12.stkobjects import AgESTKObjectType

    def onStkObjectAddedCallback(Path:str):
    print(f'{Path} has been added.')
    stk = STKDesktop.StartApplication(visible=True)
    root = stk.Root
    root.NewScenario('ExampleScenario')
    stkObjectRootEvents = root.Subscribe()
    stkObjectRootEvents.OnStkObjectAdded += onStkObjectAddedCallback
    sc = root.CurrentScenario

    #onStkObjectAddedCallback will be successfully called when the next line is executed
    fac = sc.Children.New(AgESTKObjectType.eFacility, 'AGIHQ')

    #Now switch control to the desktop application and create another facility.
    #The user interface will become unresponsive.

    #Now open a tkinter window that processing COM messages.
    from tkinter import Tk
    window = Tk()
    window.mainloop()
    #Switch control to the desktop application and create another facility.
    #The user interface will be responsive and the event callback will be successful.
