# Notes


### Component Interface

The Component Interface is the skeletons of the future component implementation.


```c++
/*****************************************************************************/
/*!
 *  @file 	 IComponent.h
 *  @date 	 2019.02.02
 *  @author  M. Treglia Akka
 *  @brief 	 Interface Component
 *****************************************************************************/

#ifndef __COMPONENT_INTERFACE__
#define __COMPONENT_INTERFACE__

#include <ros/ros.h>
#include <nodelet/nodelet.h>

using nodelet::Nodelet;

namespace future {

  /**
   *  @class  IComponent
   *  @brief  Interface for the Component skeletons.
   */

  class IComponent : public Nodelet {
   public:
     using Nodelet::Nodelet;

    /**
     *  @brief Method called by the nodelet to initialize itself.
     */
    void onInit() {
      RosParameters();
      InitComponent();
      RosTopic();
    }

    /**
     * @brief Virtual. Loading Ros Parameters
     */
    virtual void RosParameters() = 0;

    /**
     * @brief Virtual. Initialize Algorithm Components.
     */
    virtual void InitComponent() = 0;

    /**
     * @brief Virtual. Open Ros topic communications. (Publishers, Subscribers)
     */
    virtual void RosTopic() = 0;

  };
```


### Component Generated

This class is generated from GCode.


```c++

/*****************************************************************************/
/*!
 *  @file 	 GComponent{Name}.h
 *  @date 	 2019.02.02
 *  @author  Generated using GCode (M. Treglia Akka)
 *  @brief 	 Generated ComponentName
 *****************************************************************************/

#ifndef __GENERATED_COMPONENT_NAMECMP__
#define __GENERATED_COMPONENT_NAMECMP__

#include <ros/ros.h>
#include <renault_components/IComponent.h>

using future::IComponent;


namespace generated {

  /**
   *  @class  GComponentName
   *  @brief  Generated ComponentName skeletons.
   */

  class GComponentName : public IComponent {
   public:
     using IComponent::IComponent;

    /**
     * @brief Virtual. Loading Ros Parameters
     */
    virtual void RosParameters() final;

    /**
     * @brief Virtual. Initialize Algorithm Components.
     *        This is not yet implemented. You have to override it
     *        in the next phase
     */
    virtual void InitComponent() = 0;

    /**
     * @brief Virtual. Open Ros topic communications. (Publishers, Subscribers)
     */
    virtual void RosTopic() final;

    /**
    *
    * Generated Topic CallBacks to store the msg in a queue
    *
    */
    void CallbackName(const ros::MsgConstPtr & msg);

  protected:


    /**
    *
    * Get latest unprocessed msg from Data
    *
    **/
    MsgConstPrt& GetMsg();


    // Ros Topic
    Publisher publisher_name_;
    Subscriber subscriber_name_;

    // Ros Parameters
    String publisher_name_topic_;
    String subscriber_name_topic_;

  private:

    /*
    * Add the received msg to the queue
    */
    void AddReceivedMsg(const MsgConstPtr& msg);


    // Data Received
    queue<MsgConstPtr> data_;
    // Data mutex
    mutex data_mutex; // To-Do

  };


```

### Final Component Algorithm



```c++

/*****************************************************************************/
/*!
 *  @file 	 CComponent{Name}.h
 *  @date 	 2019.02.02
 *  @author  Generated using GCode (M. Treglia Akka)
 *  @brief 	 Generated CComponentName
 *****************************************************************************/

#ifndef __ALGORITHM_COMPONENT_NAMECMP__
#define __ALGORITHM_COMPONENT_NAMECMP__


#include <nodelet/nodelet.h>
#include <pluginlib/class_list_macros.h>

#include <current_package/GComponentName.h>

using nodelet::Nodelet;
using generated::GComponentName;


namespace components {

  /**
   *  @class  CComponentName
   *  @brief  Algorithm ComponentName implementation.
   */

  class CComponentName : public GComponentName {
   public:
     using GComponentName::GComponentName;

    /**
     * @brief Virtual. Initialize Algorithm Components
     */
    virtual void InitComponent() final;

    /**
    * Generated Topic CallBacks
    */
    virtual CallbackName(const ros::MsgConstPtr & msg) final;

  private:

    // DEFINE YOUR VARIABLES


  };


  /**
   * Register the nodelet.
   */
  PLUGINLIB_EXPORT_CLASS(components::CComponentName, Nodelet);

```

```python

a = '<library\n\path="lib/libhexagrid_nodelet">    <class            name="perception/HexagonsGrid"            type="renault_nodelets::HexagonsGrid"            base_class_type="nodelet::Nodelet">        <description>            HexagonsGrid Nodelet implementation.        </description>    </class></library>'


```
