/*****************************************************************************/
/*!
 *  @file 	 template.h
 *  @date 	 2019.01.09
 *  @author  M. Treglia Akka
 *  @brief 	 Template class used by the nodelets.
 *****************************************************************************/

#ifndef PROJECT_NODELET_H
#define PROJECT_NODELET_H

#include <ros/ros.h>

#include <nodelet/nodelet.h>
#include <pluginlib/class_list_macros.h>

#include <benchmarker/benchmarker.h>


namespace base {

  /**
   *  @class  BaseNodelet
   *  @brief  Template for the nodelet implementation.
   */
  class Nodelet : public nodelet::Nodelet {
   public:
    using nodelet::Nodelet::Nodelet;

    /**
     *  @brief Method called by the nodelet to initialize itself.
     */
    void onInit() {
      LoadRosParameters();
      InitializeNodelet();
      EstablishRosCommunication();
    }

    /**
     * @brief Virtual. Loads all the ros parameters.
     */
    virtual void LoadRosParameters() = 0;

    /**
     * @brief Virtual. Initialize all nodelets components.
     */
    virtual void InitializeNodelet() = 0;

    /**
     * @brief Virtual. Open ros topic communications. (Publishers, Subscribers)
     */
    virtual void EstablishRosCommunication() = 0;

  };





  /**
   *  @class  NodeletBenchMark
   *  @brief  Template for the nodelet implementation with the benchmarker tool.
   */
  class NodeletBM : public Nodelet {
   public:
    using Nodelet::Nodelet;

   protected:

    /**
    *  @brief Method called by the nodelet to initialize itself.
    */
    void onInit() final{
      LoadUseBenchMark();
      InitBenchMarker();
      LoadRosParameters();
      InitializeNodelet();
      EstablishRosCommunication();
    }

    /**
     *  Check if the benchmark should be activate
     */
    void LoadUseBenchMark(){
      bool use_benchmarker;
      getPrivateNodeHandle().param("benchmark", use_benchmarker, false);
      UseBenchmarker(use_benchmarker);
    };

    /**
     * Initialize the benchmarker. To be called in the 'InitializeNodelet' method.
     */
    void InitBenchMarker() {
      if (UseBenchmarker())
        benchmarker_ = boost::make_shared<benchmarker::Measure>(getMTPrivateNodeHandle());
    };

    /**
     * @brief BenchMarker Getter
     * @return BenchMarkerPtr
     */
    const benchmarker::MeasurePtr &BenchMarker() { return benchmarker_; };

    /**
     *  Set use_benchmarker
     * @param value bool
     */
    void UseBenchmarker(const bool& value){ use_benchmarker_ = value; };

    /**
     * Get use_benchmarker
     * @return bool
     */
    bool& UseBenchmarker(){ return use_benchmarker_; }

   private:
    benchmarker::MeasurePtr benchmarker_;
    bool use_benchmarker_;

  };



}
