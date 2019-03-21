/*****************************************************************************/
/*!
 *  @file 	 GComponent{Name}.h
 *  @date 	 2019.02.02
 *  @author  Generated using GCode (M. Treglia Akka)
 *  @brief 	 Generated ComponentName
 *****************************************************************************/

#ifndef __GENERATED_@ComponentName__
#define __GENERATED_@ComponentName__

#include <ros/ros.h>
#include <renault_components/IComponent.h>

using future::IComponent;


namespace generated {

  /**
   *  @class  GComponentName
   *  @brief  Generated ComponentName skeletons.
   */

  class G@ComponentName : public IComponent {
   public:
     using IComponent::IComponent;

    /**
     * @brief Virtual. Loading Ros Parameters
     */
    virtual void Parameters() final;


    /**
     * @brief Virtual. Open Ros topic communications. (Publishers, Subscribers)
     */
    virtual void Topic() final;

    /**
    *
    * Generated Topic CallBacks to store the msg in a queue
    *
    */
    void CallbackName(const ros::MsgConstPtr & msg);


    /**
     * @brief Virtual. Initialize Algorithm Components.
     *        This is not yet implemented. You have to override it
     *        in the next phase
     */
    virtual void InitComponent() = 0;


  private:

    // Ros Topic
    @RosTopics

    // Ros Parameters
    @RosParams

  };
