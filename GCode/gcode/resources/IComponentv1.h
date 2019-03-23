/*****************************************************************************/
/*!
 *  @file 	 IComponent.h
 *  @date 	 2019.02.02
 *  @author  M. Treglia Akka
 *  @brief 	 Interface Component
 *****************************************************************************/

#ifndef __COMPONENT_INTERFACE__
#define __COMPONENT_INTERFACE__

#include <nodelet/nodelet.h>
#include <ros/ros.h>

using nodelet::Nodelet;

namespace future {

/**
 *  @class  IComponent
 *  @brief  Interface for the Component skeletons.
 */
class Internal : public Nodelet {
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
