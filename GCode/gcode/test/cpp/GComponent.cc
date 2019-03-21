/*****************************************************************************/
/*!
 *  @file 	 GComponent{Name}.cc
 *  @date 	 2019.02.02
 *  @author  Generated using GCode (M. Treglia Akka)
 *  @brief 	 Generated ComponentName
 *****************************************************************************/

#include <@PKG/Interal/@Name>

using generate::@Name;


    /**
     * @brief Virtual. Loading Ros Parameters
     */
    virtual void @Name::Parameters() {};


    /**
     * @brief Virtual. Open Ros topic communications. (Publishers, Subscribers)
     */
    virtual void @Name::Topic() {};

    /**
    *
    * Generated Topic CallBacks to store the msg in a queue
    *
    */
    void @Name::CallbackName(const ros::MsgConstPtr & msg);


    /**
     * @brief Virtual. Initialize Algorithm Components.
     *        This is not yet implemented. You have to override it
     *        in the next phase
     */
    virtual void @Name::InitComponent() = 0;

private:
    // Ros Topic
    @RosTopics

    // Ros Parameters
    @RosParams

  };
