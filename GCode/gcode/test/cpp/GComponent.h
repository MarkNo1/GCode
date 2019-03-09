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
